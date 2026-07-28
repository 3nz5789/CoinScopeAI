/* Overview — Operator command-console front page.
 *
 * Layout follows the kit's canonical Overview reference:
 *   ┌─ Page header ──────────────────────────────────────────────┐
 *   │  [icon] Overview · LIVE                       Tue, 13:37 UTC│
 *   ├─ 4 KPI tiles ──────────────────────────────────────────────┤
 *   │  PORTFOLIO  · UNREALIZED P&L · TOTAL RETURN · WIN RATE     │
 *   ├─ Equity Curve (7) ─────────────┬─ Risk Gate widget (5) ────┤
 *   │  emerald area chart            │  4 gauges + kill switch    │
 *   ├─ Top Signals (5) ──┬─ Positions (4) ─┬─ Market Prices (3) ──┤
 *   │  6 rows           │  open positions │  live prices         │
 *   └────────────────────────────────────────────────────────────┘
 *
 * All values are wired to live engine hooks; the page is fully usable
 * on an empty backend (renders graceful empty states).
 */
import DashboardLayout from '@/components/DashboardLayout';
import MetricCard from '@/components/MetricCard';
import {
  useAccount,
  useAccountPositions,
  useCircuitBreaker,
  useConfig,
  useEquityCurve,
  useExposure,
  useLivePrices,
  usePerformance,
  useSignals,
} from '@/lib/engine/hooks';
import { formatUSD } from '@/lib/mockData';
import { cn } from '@/lib/utils';
import {
  Activity,
  ArrowDownRight,
  ArrowUpRight,
  BarChart3,
  DollarSign,
  LayoutDashboard,
  Power,
  Radar,
  Shield,
  ShieldAlert,
  ShieldCheck,
  TrendingUp,
  Wallet,
} from 'lucide-react';
import { useEffect, useState } from 'react';
import { Area, AreaChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

// ─── Helpers ───────────────────────────────────────────────────────────────

/** Returns the running max-to-current drawdown % on an equity series.
 *  0 if the series is empty / monotonic up. */
function computeDrawdownPct(points: { equity: number }[]): number {
  if (points.length === 0) return 0;
  let peak = -Infinity;
  let worst = 0;
  for (const p of points) {
    if (p.equity > peak) peak = p.equity;
    if (peak > 0) {
      const dd = ((peak - p.equity) / peak) * 100;
      if (dd > worst) worst = dd;
    }
  }
  return worst;
}

/** Small gauge — eyebrow label + value/limit + 5px progress track.
 *  Colour ramps nominal → warning → critical at 50% / 80%. */
function RiskGauge({
  label,
  value,
  limit,
  unit = '%',
}: {
  label: string;
  value: number;
  limit: number;
  unit?: string;
}) {
  const ratio = limit > 0 ? value / limit : 0;
  const pct = Math.max(0, Math.min(100, ratio * 100));
  const state = ratio >= 0.8 ? 'critical' : ratio >= 0.5 ? 'warning' : 'nominal';
  const barCls =
    state === 'critical' ? 'bg-crimson' :
    state === 'warning'  ? 'bg-amber-warn' : 'bg-emerald';
  const txtCls =
    state === 'critical' ? 'text-crimson' :
    state === 'warning'  ? 'text-amber-warn' : 'text-emerald';

  return (
    <div className="space-y-1">
      <div className="flex items-center justify-between text-[10px] font-semibold tracking-[0.12em] uppercase">
        <span className="text-muted-foreground">{label}</span>
        <span className={cn('font-mono tabular-nums', txtCls)}>
          {value.toFixed(unit === 'x' ? 1 : 1)}{unit}
          <span className="text-muted-foreground">/{limit}{unit}</span>
        </span>
      </div>
      <div className="h-[5px] bg-muted rounded-full overflow-hidden">
        <div
          className={cn('h-full transition-all duration-500', barCls)}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

// ─── Page ──────────────────────────────────────────────────────────────────

export default function Overview() {
  const account     = useAccount();
  const acctPos     = useAccountPositions();
  const exposure    = useExposure();
  const cb          = useCircuitBreaker();
  const perf        = usePerformance();
  const equity      = useEquityCurve();
  const config      = useConfig();
  const signals     = useSignals();
  const prices      = useLivePrices();

  // Page-header clock — updated once per second
  const [now, setNow] = useState(new Date());
  useEffect(() => {
    const id = setInterval(() => setNow(new Date()), 1000);
    return () => clearInterval(id);
  }, []);
  const headerTime = now.toLocaleString('en-US', {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    timeZone: 'UTC',
  });

  // ── Account-derived KPIs ─────────────────────────────────────────────────
  const liveAccount = account.data;
  const balance     = liveAccount?.total_wallet_balance ?? exposure.data?.balance ?? 0;
  const marginBal   = liveAccount?.total_margin_balance ?? balance;
  const unrealised  = liveAccount?.total_unrealized_pnl ?? exposure.data?.unrealised_pnl ?? 0;
  const posCount    = liveAccount?.position_count ?? acctPos.data?.count ?? 0;

  // ── Equity curve ─────────────────────────────────────────────────────────
  const equityPoints = (equity.data?.points ?? []).map((p: any) => ({
    date: p.date ?? p.ts ?? '',
    equity: Number(p.equity ?? 0),
  }));
  const firstEq = equityPoints[0]?.equity ?? 0;
  const lastEq  = equityPoints[equityPoints.length - 1]?.equity ?? 0;
  const eqChangePct = firstEq > 0 ? ((lastEq - firstEq) / firstEq) * 100 : 0;
  const drawdownPct = computeDrawdownPct(equityPoints);

  // ── Performance ──────────────────────────────────────────────────────────
  const totalReturnPct = perf.data?.total_return_pct ?? 0;
  const totalReturn    = perf.data?.total_return ?? 0;
  const winRate        = perf.data?.win_rate ?? 0;
  const totalTrades    = perf.data?.total_trades ?? 0;
  const sharpe         = perf.data?.sharpe_ratio ?? 0;

  // ── Risk gate state ──────────────────────────────────────────────────────
  const cbState        = cb.data?.state ?? 'CLOSED';
  const killActive     = cbState !== 'CLOSED';
  const dailyLossPct   = Math.abs(exposure.data?.daily_loss_pct ?? 0);
  const maxDailyLoss   = cb.data?.max_daily_loss_pct ?? 5;
  const maxDrawdown    = cb.data?.max_drawdown_pct ?? 10;
  const heatPct        = exposure.data?.total_exposure_pct ?? 0;
  const maxHeat        = exposure.data?.max_total_exposure_pct ?? 80;
  const livePositions  = acctPos.data?.positions ?? [];
  const currentLev     = livePositions.length > 0
    ? Math.max(...livePositions.map(p => p.leverage ?? 1))
    : 0;
  const maxLev         = config.data?.max_leverage ?? 10;

  const riskState =
    cbState === 'CLOSED'
      ? (dailyLossPct >= maxDailyLoss * 0.8 || heatPct >= maxHeat * 0.8 || drawdownPct >= maxDrawdown * 0.8
          ? 'WARNING'
          : 'NOMINAL')
      : 'CRITICAL';

  const RiskIcon =
    riskState === 'CRITICAL' ? ShieldAlert
  : riskState === 'WARNING'  ? Shield
                             : ShieldCheck;
  const riskChipCls =
    riskState === 'CRITICAL' ? 'cs-chip-dn'
  : riskState === 'WARNING'  ? 'cs-chip-wn'
                             : 'cs-chip-em';

  // ── Top signals (best by score, max 6) ───────────────────────────────────
  const topSignals = [...(signals.data?.signals ?? [])]
    .sort((a, b) => (b.score ?? 0) - (a.score ?? 0))
    .slice(0, 6);

  // ── Open positions (max 5) ───────────────────────────────────────────────
  const showPositions = livePositions.slice(0, 5);

  // ── Market prices (config'd scan pairs) ──────────────────────────────────
  const priceRows = prices.data?.prices ?? [];

  return (
    <DashboardLayout>
      {/* ── Page header ─────────────────────────────────────────────────── */}
      <header className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <LayoutDashboard className="w-5 h-5 text-emerald shrink-0" />
          <h1 className="text-xl font-semibold text-foreground tracking-tight leading-none">
            Overview
          </h1>
          <span className="cs-pill cs-chip-em">
            <span className="dot animate-pulse-dot" />
            LIVE
          </span>
        </div>
        <span className="font-mono text-xs text-muted-foreground tabular-nums">
          {headerTime} UTC
        </span>
      </header>

      {/* ── 4 KPI tiles ─────────────────────────────────────────────────── */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-3">
        <MetricCard
          label="Portfolio Value"
          value={balance >= 10_000 ? `$${(balance / 1000).toFixed(1)}K` : formatUSD(balance)}
          subValue={equityPoints.length > 0 ? `${eqChangePct >= 0 ? '+' : ''}${eqChangePct.toFixed(2)}% (30d)` : `Margin ${formatUSD(marginBal)}`}
          trend={eqChangePct >= 0 ? 'up' : 'down'}
          icon={Wallet}
        />
        <MetricCard
          label="Unrealized P&L"
          value={formatUSD(unrealised)}
          subValue={`${posCount} open position${posCount === 1 ? '' : 's'}`}
          trend={unrealised >= 0 ? 'up' : 'down'}
          icon={DollarSign}
        />
        <MetricCard
          label="Total Return"
          value={`${totalReturnPct >= 0 ? '+' : ''}${totalReturnPct.toFixed(2)}%`}
          subValue={formatUSD(totalReturn)}
          trend={totalReturnPct >= 0 ? 'up' : 'down'}
          icon={Activity}
        />
        <MetricCard
          label="Win Rate"
          value={`${winRate.toFixed(1)}%`}
          subValue={`${totalTrades} trades · sharpe ${sharpe.toFixed(2)}`}
          icon={Radar}
        />
      </div>

      {/* ── Equity Curve (7) + Risk Gate (5) ─────────────────────────────── */}
      <div className="grid grid-cols-1 xl:grid-cols-12 gap-3 mb-3">
        {/* Equity Curve */}
        <div className="xl:col-span-7 hud-panel overflow-hidden">
          <div className="cs-card-head">
            <div className="flex items-baseline">
              <span className="cs-card-title">Equity Curve</span>
              <span className="cs-card-sub">30-DAY</span>
            </div>
            <a className="cs-card-link">Full Chart →</a>
          </div>
          <div className="p-4">
            {equityPoints.length > 0 ? (
              <ResponsiveContainer width="100%" height={240}>
                <AreaChart data={equityPoints} margin={{ top: 5, right: 5, bottom: 0, left: 5 }}>
                  <defs>
                    <linearGradient id="ovEqGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stopColor="#00FFB8" stopOpacity={0.25} />
                      <stop offset="100%" stopColor="#00FFB8" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="date" tick={{ fontSize: 10, fill: 'oklch(0.556 0.02 264.05)' }} tickLine={false} axisLine={false} tickFormatter={(v) => String(v).slice(5)} />
                  <YAxis tick={{ fontSize: 10, fill: 'oklch(0.556 0.02 264.05)' }} tickLine={false} axisLine={false} tickFormatter={(v) => `$${(v / 1000).toFixed(0)}k`} domain={['auto', 'auto']} />
                  <Tooltip
                    contentStyle={{ background: 'oklch(0.185 0.02 264.05)', border: '1px solid oklch(0.3 0.015 264.05)', borderRadius: '6px', fontSize: '12px' }}
                    labelStyle={{ color: 'oklch(0.75 0.01 264.05)' }}
                    itemStyle={{ color: 'oklch(0.696 0.17 162.48)' }}
                    formatter={(value: number) => [formatUSD(value), 'Equity']}
                  />
                  <Area type="monotone" dataKey="equity" stroke="oklch(0.696 0.17 162.48)" strokeWidth={1.6} fill="url(#ovEqGrad)" />
                </AreaChart>
              </ResponsiveContainer>
            ) : (
              <div className="h-[240px] flex items-center justify-center text-xs text-muted-foreground">
                {equity.isLoading ? 'Loading equity history…' : 'No equity history yet — run some trades.'}
              </div>
            )}
          </div>
        </div>

        {/* Risk Gate widget — gauges + kill switch row */}
        <div className="xl:col-span-5 hud-panel overflow-hidden">
          <div className="cs-card-head">
            <span className="cs-card-title">Risk Gate</span>
            <span className={cn('cs-chip', riskChipCls)}>
              <RiskIcon />
              {riskState}
            </span>
          </div>
          <div className="p-4 space-y-3">
            <RiskGauge label="Daily Loss"   value={dailyLossPct} limit={maxDailyLoss} />
            <RiskGauge label="Drawdown"     value={drawdownPct}  limit={maxDrawdown} />
            <RiskGauge label="Position Heat" value={heatPct}      limit={maxHeat} />
            <RiskGauge label="Leverage"     value={currentLev}   limit={maxLev} unit="x" />

            <div className="flex items-center justify-between pt-3 mt-1 border-t border-border/60">
              <span className="text-[10px] font-semibold tracking-[0.12em] uppercase text-muted-foreground">
                Kill Switch
              </span>
              <span className={cn('cs-chip', killActive ? 'cs-chip-dn' : 'cs-chip-em')}>
                <Power />
                {killActive ? 'ARMED' : 'DISARMED'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* ── Bottom row: Top Signals (5) + Open Positions (4) + Market Prices (3) ── */}
      <div className="grid grid-cols-1 xl:grid-cols-12 gap-3">
        {/* Top Signals */}
        <div className="xl:col-span-5 hud-panel overflow-hidden">
          <div className="cs-card-head">
            <span className="cs-card-title">Top Signals</span>
            <a className="cs-card-link" href="/scanner">All Signals →</a>
          </div>
          <div className="px-4 py-1">
            {topSignals.length === 0 ? (
              <div className="py-6 text-center text-xs text-muted-foreground">
                {signals.isLoading ? 'Loading signals…' : 'No signals yet — run a scan.'}
              </div>
            ) : (
              topSignals.map((s, i) => {
                const isLong = s.direction === 'LONG';
                const Arrow = isLong ? ArrowUpRight : ArrowDownRight;
                const score = Math.max(0, Math.min(100, s.score ?? 0));
                const scoreCls = score >= 80 ? 'bg-emerald' : score >= 60 ? 'bg-amber-warn' : 'bg-muted-foreground';
                return (
                  <div
                    key={`${s.symbol}-${i}`}
                    className={cn(
                      'flex items-center justify-between py-2',
                      i < topSignals.length - 1 && 'border-b border-border/40'
                    )}
                  >
                    <div className="flex items-center gap-2">
                      <span className={cn(
                        'font-mono text-[11px] font-semibold inline-flex items-center gap-0.5',
                        isLong ? 'text-emerald' : 'text-crimson',
                      )}>
                        <Arrow className="w-3 h-3" />
                        {s.direction}
                      </span>
                      <span className="font-mono text-xs font-semibold text-foreground">{s.symbol}</span>
                      <span className="text-[10px] text-muted-foreground capitalize">
                        {s.scanners?.[0]?.replace('Scanner', '').replace(/_/g, ' ').toLowerCase() ?? '—'}
                      </span>
                    </div>
                    <div className="flex items-center gap-2 shrink-0">
                      <div className="w-12 h-1 bg-muted rounded-full overflow-hidden">
                        <div className={cn('h-full transition-all duration-500', scoreCls)} style={{ width: `${score}%` }} />
                      </div>
                      <span className="font-mono text-[10px] tabular-nums text-muted-foreground w-6 text-right">
                        {score.toFixed(0)}%
                      </span>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Open Positions */}
        <div className="xl:col-span-4 hud-panel overflow-hidden">
          <div className="cs-card-head">
            <span className="cs-card-title">Open Positions</span>
            <a className="cs-card-link" href="/positions">All Positions →</a>
          </div>
          <div className="px-4 py-1">
            {showPositions.length === 0 ? (
              <div className="py-6 text-center text-xs text-muted-foreground">
                {acctPos.isLoading ? 'Loading…' : 'No open positions'}
              </div>
            ) : (
              showPositions.map((p, i) => {
                const isLong = p.side === 'LONG';
                const pnl   = p.unrealized_pnl ?? 0;
                const profit = pnl >= 0;
                return (
                  <div
                    key={`${p.symbol}-${i}`}
                    className={cn(
                      'flex items-center justify-between py-2',
                      i < showPositions.length - 1 && 'border-b border-border/40'
                    )}
                  >
                    <div className="flex items-center gap-2">
                      <span className={cn(
                        'cs-chip',
                        isLong ? 'cs-chip-em' : 'cs-chip-dn',
                      )}>
                        {p.side}
                      </span>
                      <span className="font-mono text-xs font-semibold text-foreground">{p.symbol}</span>
                      <span className="cs-chip cs-chip-wn">{p.leverage}x</span>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className="font-mono text-[11px] text-muted-foreground tabular-nums">
                        ${(p.mark_price ?? p.entry_price)?.toLocaleString()}
                      </span>
                      <span className={cn(
                        'font-mono text-xs font-semibold tabular-nums',
                        profit ? 'text-emerald' : 'text-crimson',
                      )}>
                        {profit ? '+' : '-'}${Math.abs(pnl).toFixed(2)}
                      </span>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Market Prices */}
        <div className="xl:col-span-3 hud-panel overflow-hidden">
          <div className="cs-card-head">
            <div className="flex items-baseline">
              <span className="cs-card-title">Market Prices</span>
              <span className="cs-card-sub">24H Δ</span>
            </div>
          </div>
          <div className="px-4 py-1">
            {priceRows.length === 0 ? (
              <div className="py-6 text-center text-xs text-muted-foreground">
                {prices.isLoading ? 'Loading…' : 'No live feed'}
              </div>
            ) : (
              priceRows.slice(0, 8).map((row, i) => (
                <div
                  key={row.symbol}
                  className={cn(
                    'flex items-center justify-between py-1.5',
                    i < Math.min(priceRows.length, 8) - 1 && 'border-b border-border/40'
                  )}
                >
                  <span className="font-mono text-xs font-semibold text-foreground">{row.symbol}</span>
                  <span className="font-mono text-[11px] text-foreground tabular-nums">
                    {formatUSD(row.mark_price, row.mark_price < 10 ? 4 : 2)}
                  </span>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Status footer — sync state */}
      <div className="mt-4 flex items-center gap-2 text-[10px] text-muted-foreground">
        <span className={cn(
          'w-1.5 h-1.5 rounded-full',
          liveAccount?.age_s != null && liveAccount.age_s < 30 ? 'bg-emerald animate-pulse-dot' : 'bg-amber-warn',
        )} />
        {account.isLoading && !liveAccount ? 'Syncing account…'
          : liveAccount?.error ? `Sync error: ${liveAccount.error}`
          : liveAccount?.age_s != null && liveAccount.age_s < 30 ? `Account live · ${liveAccount.age_s.toFixed(0)}s ago`
          : 'Account stale'}
        <span className="ml-auto">
          <BarChart3 className="w-3 h-3 inline-block mr-1 opacity-50" />
          Binance Futures Demo · {liveAccount?.can_trade ? 'trading enabled' : 'read-only'}
        </span>
      </div>
    </DashboardLayout>
  );
}
