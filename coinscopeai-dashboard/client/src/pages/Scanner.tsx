/**
 * Scanner.tsx — Operator-Grade Signal Decision Feed
 *
 * Replaces the flat row table with SignalDecisionCard components.
 * Each card is a self-contained briefing: regime accent, score arc,
 * gate checks, price rail, and collapsible evidence — all in one view.
 */
import DashboardLayout from '@/components/DashboardLayout';
import ExecuteOrderDialog from '@/components/ExecuteOrderDialog';
import PageHeader from '@/components/PageHeader';
import SignalDecisionCard, { type SignalData } from '@/components/SignalDecisionCard';
import { qk, useConfig, useScan, useSignals } from '@/lib/engine/hooks';
import { cn } from '@/lib/utils';
import { useQueryClient } from '@tanstack/react-query';
import { Filter, RefreshCw, Zap } from 'lucide-react';
import { useState } from 'react';
import { toast } from 'sonner';

type DirectionFilter = 'ALL' | 'LONG' | 'SHORT';
type ActionFilter = 'ALL' | 'LIVE' | 'WATCH';

export default function Scanner() {
  const signals = useSignals();
  const config  = useConfig();
  const scan    = useScan();
  const qc      = useQueryClient();

  const [dirFilter, setDirFilter] = useState<DirectionFilter>('ALL');
  const [actionFilter, setActionFilter] = useState<ActionFilter>('ALL');
  const [executeTarget, setExecuteTarget] = useState<{
    symbol: string;
    side: 'BUY' | 'SELL';
    entry: number;
    stopLoss?: number | null;
    takeProfit?: number | null;
    scoreLabel?: string;
  } | null>(null);

  const allSignals: SignalData[] = (signals.data?.signals ?? []) as SignalData[];
  const pairs = config.data?.scan_pairs ?? [];
  const minScore = config.data?.min_confluence_score ?? 65;
  const loop = signals.data?.loop;

  // Filters
  const filtered = allSignals
    .filter((s) => dirFilter === 'ALL' || s.direction === dirFilter)
    .filter((s) => {
      if (actionFilter === 'LIVE') return s.actionable;
      if (actionFilter === 'WATCH') return !s.actionable && s.score >= minScore * 0.75;
      return true;
    })
    .sort((a, b) => {
      // Actionable first, then by score descending
      if (a.actionable !== b.actionable) return a.actionable ? -1 : 1;
      return b.score - a.score;
    });

  const liveCount = allSignals.filter((s) => s.actionable).length;
  const watchCount = allSignals.filter((s) => !s.actionable && s.score >= minScore * 0.75).length;

  async function runScan() {
    try {
      await scan.mutateAsync({ pairs, timeframe: '1h', limit: 100 });
      await qc.invalidateQueries({ queryKey: qk.signals });
      toast.success('Scan complete');
    } catch (err: any) {
      toast.error(`Scan failed: ${err?.response?.data?.detail ?? err?.message ?? err}`);
    }
  }

  function handleExecute(signal: SignalData) {
    setExecuteTarget({
      symbol:     signal.symbol,
      side:       signal.direction === 'SHORT' ? 'SELL' : 'BUY',
      entry:      signal.setup?.entry ?? 0,
      stopLoss:   signal.setup?.stop_loss ?? null,
      takeProfit: signal.setup?.tp2 ?? signal.setup?.tp1 ?? null,
      scoreLabel: `${signal.strength ?? ''} ${signal.score.toFixed(0)}`,
    });
  }

  return (
    <DashboardLayout>
      <PageHeader
        title="Signal Decision Feed"
        subtitle={`${pairs.length} pair${pairs.length === 1 ? '' : 's'} · min score ${minScore} · operator view`}
      >
        <div className="flex items-center gap-3 text-xs">
          {/* Loop status */}
          {loop && (
            <div className="flex items-center gap-2">
              <span className={cn('flex items-center gap-1.5', loop.running ? 'text-emerald' : 'text-muted-foreground')}>
                <span className={cn('w-1.5 h-1.5 rounded-full', loop.running ? 'bg-emerald animate-pulse' : 'bg-muted')} />
                {loop.running
                  ? loop.seconds_to_next != null && loop.seconds_to_next > 0
                    ? `Next scan in ${loop.seconds_to_next.toFixed(0)}s`
                    : 'Scanning…'
                  : 'Idle'}
              </span>
              <span className="text-muted-foreground hidden sm:inline">
                tick #{loop.scans_total} · {loop.last_duration_ms}ms
              </span>
            </div>
          )}

          {/* Run scan button */}
          <button
            onClick={runScan}
            disabled={scan.isPending}
            className="flex items-center gap-2 bg-emerald/10 border border-emerald/30 text-emerald text-xs font-semibold px-3 py-1.5 rounded-md hover:bg-emerald/20 disabled:opacity-50 transition-colors"
          >
            <RefreshCw className={cn('w-3.5 h-3.5', scan.isPending && 'animate-spin')} />
            {scan.isPending ? 'Scanning…' : 'Run Scan'}
          </button>
        </div>
      </PageHeader>

      {/* ── Filters + Stats Bar ── */}
      <div className="flex items-center gap-3 mb-5 flex-wrap">
        {/* Signal counts */}
        <div className="flex items-center gap-3 text-xs mr-2">
          <span className="text-muted-foreground">
            <span className="font-semibold text-foreground">{allSignals.length}</span> signals
          </span>
          {liveCount > 0 && (
            <span className="flex items-center gap-1 text-emerald font-semibold">
              <Zap className="w-3 h-3" />
              {liveCount} live
            </span>
          )}
          {watchCount > 0 && (
            <span className="text-amber-warn font-semibold">{watchCount} watch</span>
          )}
        </div>

        <div className="flex items-center gap-1.5 ml-auto">
          <Filter className="w-3 h-3 text-muted-foreground" />

          {/* Direction filter */}
          <div className="flex rounded-md border border-border overflow-hidden text-[10px] font-semibold tracking-wider">
            {(['ALL', 'LONG', 'SHORT'] as DirectionFilter[]).map((d) => (
              <button
                key={d}
                onClick={() => setDirFilter(d)}
                className={cn(
                  'px-2.5 py-1 transition-colors',
                  dirFilter === d
                    ? d === 'LONG'
                      ? 'bg-emerald/15 text-emerald'
                      : d === 'SHORT'
                      ? 'bg-crimson/15 text-crimson'
                      : 'bg-muted/40 text-foreground'
                    : 'bg-transparent text-muted-foreground hover:text-foreground hover:bg-muted/20',
                )}
              >
                {d}
              </button>
            ))}
          </div>

          {/* Action filter */}
          <div className="flex rounded-md border border-border overflow-hidden text-[10px] font-semibold tracking-wider">
            {(['ALL', 'LIVE', 'WATCH'] as ActionFilter[]).map((a) => (
              <button
                key={a}
                onClick={() => setActionFilter(a)}
                className={cn(
                  'px-2.5 py-1 transition-colors',
                  actionFilter === a
                    ? a === 'LIVE'
                      ? 'bg-emerald/15 text-emerald'
                      : 'bg-muted/40 text-foreground'
                    : 'bg-transparent text-muted-foreground hover:text-foreground hover:bg-muted/20',
                )}
              >
                {a}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* ── Card Grid ── */}
      {signals.isLoading && allSignals.length === 0 ? (
        <div className="hud-panel p-12 text-center text-sm text-muted-foreground animate-pulse">
          Loading signals…
        </div>
      ) : filtered.length === 0 ? (
        <div className="hud-panel p-12 text-center space-y-3">
          <p className="text-sm text-muted-foreground">
            {allSignals.length === 0
              ? 'No signals yet — click Run Scan to evaluate the configured pairs.'
              : 'No signals match the current filters.'}
          </p>
          {allSignals.length === 0 && (
            <button
              onClick={runScan}
              disabled={scan.isPending}
              className="mx-auto flex items-center gap-2 bg-emerald/10 border border-emerald/30 text-emerald text-sm font-semibold px-4 py-2 rounded-md hover:bg-emerald/20 disabled:opacity-50 transition-colors"
            >
              <RefreshCw className={cn('w-4 h-4', scan.isPending && 'animate-spin')} />
              {scan.isPending ? 'Scanning…' : 'Run First Scan'}
            </button>
          )}
        </div>
      ) : (
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-3">
          {filtered.map((sig) => (
            <SignalDecisionCard
              key={`${sig.symbol}-${sig.scanned_at}`}
              signal={sig}
              onExecute={handleExecute}
              minScore={minScore}
            />
          ))}
        </div>
      )}

      {/* ── Legend ── */}
      <div className="mt-6 hud-panel p-4">
        <div className="flex items-center gap-1 mb-3">
          <h3 className="text-[10px] font-semibold tracking-[0.14em] uppercase text-muted-foreground">
            Decision Guide
          </h3>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs text-muted-foreground">
          <div className="space-y-1.5">
            <div className="text-[9px] font-semibold tracking-wider uppercase text-muted-foreground/70">Score</div>
            <div className="space-y-1">
              <div><span className="text-emerald">●</span> 80–100 Strong — all systems</div>
              <div><span className="text-cyan-accent">●</span> 65–79 Moderate — confirm setup</div>
              <div><span className="text-amber-warn">●</span> 50–64 Weak — watch only</div>
              <div><span className="text-crimson">●</span> &lt;50 Noise — skip</div>
            </div>
          </div>
          <div className="space-y-1.5">
            <div className="text-[9px] font-semibold tracking-wider uppercase text-muted-foreground/70">Regime Border</div>
            <div className="space-y-1">
              <div><span className="text-emerald">▌</span> Trending — full size eligible</div>
              <div><span className="text-cyan-accent">▌</span> Mean-Rev — oscillators favoured</div>
              <div><span className="text-amber-warn">▌</span> Volatile — 0.3× Kelly</div>
              <div><span className="text-muted-foreground">▌</span> Quiet — 0.3× Kelly</div>
            </div>
          </div>
          <div className="space-y-1.5">
            <div className="text-[9px] font-semibold tracking-wider uppercase text-muted-foreground/70">Gate Checks</div>
            <div className="space-y-1">
              <div>4H MTF — higher-timeframe trend</div>
              <div>Regime — valid classifier output</div>
              <div>No Anomaly — no data spikes</div>
              <div>Setup Valid — entry/SL/TP set</div>
            </div>
          </div>
          <div className="space-y-1.5">
            <div className="text-[9px] font-semibold tracking-wider uppercase text-muted-foreground/70">Execute Gate</div>
            <div className="space-y-1">
              <div>Score ≥ {minScore} threshold</div>
              <div>Setup valid (entry, SL set)</div>
              <div>Circuit breaker CLOSED</div>
              <div>TESTNET_MODE=true enforced</div>
            </div>
          </div>
        </div>
      </div>

      {/* Execute dialog */}
      {executeTarget && (
        <ExecuteOrderDialog
          open={executeTarget !== null}
          onOpenChange={(v) => !v && setExecuteTarget(null)}
          {...executeTarget}
        />
      )}
    </DashboardLayout>
  );
}
