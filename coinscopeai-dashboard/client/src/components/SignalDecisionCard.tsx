/**
 * SignalDecisionCard.tsx
 * Operator-grade signal decision card.
 *
 * Layout (top → bottom):
 *   ┌─ HEADER ──────────────────────────────────────────────────────┐
 *   │  [REGIME ACCENT BORDER]                                       │
 *   │  Symbol · Direction pill · LIVE badge   Score arc   Timestamp │
 *   ├─ GATE ROW ─────────────────────────────────────────────────────┤
 *   │  ✓ MTF  ✓ Regime  ✓ Anomaly  — gate checks at a glance        │
 *   ├─ PRICE GRID ───────────────────────────────────────────────────┤
 *   │  Entry  ▸  Stop  ▸  TP1  ▸  TP2   R:R badge                  │
 *   ├─ INDICATORS ───────────────────────────────────────────────────┤
 *   │  RSI  ADX  Trend  Momentum  Volatility                        │
 *   ├─ EVIDENCE ─────────────────────────────────────────────────────┤
 *   │  Reason tags + scanner hits                                    │
 *   ├─ FOOTER ───────────────────────────────────────────────────────┤
 *   │  [Execute button]  [Details toggle]                           │
 *   └────────────────────────────────────────────────────────────────┘
 */

import { cn } from '@/lib/utils';
import { formatUSD } from '@/lib/mockData';
import {
  Activity,
  AlertTriangle,
  CheckCircle2,
  ChevronDown,
  ChevronUp,
  Clock,
  Play,
  TrendingUp,
  TrendingDown,
  Minus,
  XCircle,
} from 'lucide-react';
import { useState } from 'react';

// ─── Types ────────────────────────────────────────────────────────────────────

interface SignalSetup {
  entry?: number | null;
  stop_loss?: number | null;
  tp1?: number | null;
  tp2?: number | null;
  tp3?: number | null;
  rr_ratio?: number | null;
  valid: boolean;
  reason?: string | null;
}

interface SignalIndicators {
  rsi?: number | null;
  adx?: number | null;
  trend?: string | null;
  momentum?: string | null;
  volatility?: string | null;
}

interface SignalAnomaly {
  detected: boolean;
  severity?: string | null;
  types?: string[];
}

export interface SignalData {
  symbol: string;
  direction: 'LONG' | 'SHORT' | 'NEUTRAL';
  score: number;
  strength?: string | null;
  scanners: string[];
  reasons: string[];
  actionable: boolean;
  setup?: SignalSetup | null;
  regime?: string | null;
  htf_trend?: string | null;
  htf_agrees?: boolean;
  anomaly?: SignalAnomaly | null;
  indicators?: SignalIndicators | null;
  scanned_at: number;
}

interface SignalDecisionCardProps {
  signal: SignalData;
  onExecute?: (signal: SignalData) => void;
  minScore?: number;
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function relTime(ts: number): string {
  const secs = Math.max(0, Math.floor(Date.now() / 1000 - ts));
  if (secs < 60) return `${secs}s ago`;
  if (secs < 3600) return `${Math.floor(secs / 60)}m ago`;
  return `${Math.floor(secs / 3600)}h ago`;
}

function fmt(n: number | null | undefined, digits = 2): string {
  if (n == null || n === 0) return '—';
  return formatUSD(n, n < 10 ? 4 : digits);
}

// Regime → border accent color class
function regimeAccent(regime: string | null | undefined): string {
  if (!regime) return 'border-l-navy-700';
  const r = regime.toLowerCase();
  if (r.includes('trend') || r === 'bull') return 'border-l-emerald';
  if (r.includes('mean') || r.includes('rang') || r === 'bear') return 'border-l-cyan-accent';
  if (r.includes('vol')) return 'border-l-amber-warn';
  if (r.includes('quiet') || r === 'chop') return 'border-l-[oklch(0.40_0.03_250)]';
  return 'border-l-navy-700';
}

// Score → color
function scoreColor(score: number): string {
  if (score >= 80) return 'text-emerald';
  if (score >= 65) return 'text-cyan-accent';
  if (score >= 50) return 'text-amber-warn';
  return 'text-crimson';
}

function scoreBg(score: number): string {
  if (score >= 80) return 'bg-emerald';
  if (score >= 65) return 'bg-cyan-accent';
  if (score >= 50) return 'bg-amber-warn';
  return 'bg-crimson';
}

// Gate check pill
function GateCheck({
  label,
  pass,
  warn,
}: {
  label: string;
  pass: boolean | null;
  warn?: boolean;
}) {
  return (
    <div
      className={cn(
        'flex items-center gap-1 text-[10px] font-semibold tracking-wide px-2 py-1 rounded-sm border',
        pass === true && !warn
          ? 'bg-emerald/8 border-emerald/25 text-emerald'
          : pass === true && warn
          ? 'bg-amber-warn/8 border-amber-warn/25 text-amber-warn'
          : pass === false
          ? 'bg-crimson/8 border-crimson/25 text-crimson'
          : 'bg-muted/30 border-border text-muted-foreground',
      )}
    >
      {pass === true && !warn && <CheckCircle2 className="w-3 h-3" />}
      {pass === true && warn && <AlertTriangle className="w-3 h-3" />}
      {pass === false && <XCircle className="w-3 h-3" />}
      {pass === null && <Minus className="w-3 h-3" />}
      {label}
    </div>
  );
}

// Price point in the price rail
function PricePoint({
  label,
  value,
  color,
  entry,
}: {
  label: string;
  value: number | null | undefined;
  color: string;
  entry?: number | null;
}) {
  const pct =
    entry && value && entry > 0
      ? (((value - entry) / entry) * 100).toFixed(2)
      : null;

  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-[9px] font-semibold tracking-[0.14em] uppercase text-muted-foreground">
        {label}
      </span>
      <span className={cn('font-mono text-sm font-semibold tabular-nums', color)}>
        {fmt(value)}
      </span>
      {pct && (
        <span
          className={cn(
            'text-[10px] font-mono tabular-nums',
            parseFloat(pct) >= 0 ? 'text-emerald/70' : 'text-crimson/70',
          )}
        >
          {parseFloat(pct) >= 0 ? '+' : ''}
          {pct}%
        </span>
      )}
    </div>
  );
}

// Indicator pill
function IndicatorPill({ label, value }: { label: string; value: string | number | null | undefined }) {
  if (value == null) return null;
  return (
    <div className="flex flex-col gap-0.5">
      <span className="text-[9px] font-semibold tracking-[0.12em] uppercase text-muted-foreground">
        {label}
      </span>
      <span className="text-xs font-mono tabular-nums text-foreground">
        {typeof value === 'number' ? value.toFixed(1) : value}
      </span>
    </div>
  );
}

// ─── Main Component ────────────────────────────────────────────────────────────

export default function SignalDecisionCard({
  signal,
  onExecute,
  minScore = 65,
}: SignalDecisionCardProps) {
  const [expanded, setExpanded] = useState(false);
  const score = Math.max(0, Math.min(100, signal.score));
  const entry = signal.setup?.entry ?? 0;
  const sl = signal.setup?.stop_loss ?? 0;
  const tp1 = signal.setup?.tp1 ?? 0;
  const tp2 = signal.setup?.tp2 ?? 0;
  const rr = signal.setup?.rr_ratio ?? 0;

  const isLong = signal.direction === 'LONG';
  const isShort = signal.direction === 'SHORT';
  const canExecute = signal.actionable && signal.setup?.valid && onExecute;

  // Gate checks
  const mtfPass = signal.htf_trend != null
    ? signal.htf_agrees ?? false
    : null;
  const anomalyPass = signal.anomaly
    ? !signal.anomaly.detected
    : null;
  const regimePass = signal.regime
    ? !signal.regime.toLowerCase().includes('unknown')
    : null;

  const allGatesPass = mtfPass !== false && anomalyPass !== false && regimePass !== false;

  // Score ring SVG
  const R = 22;
  const C = 2 * Math.PI * R;
  const dash = (score / 100) * C;

  return (
    <div
      className={cn(
        'hud-panel border-l-4 transition-all duration-200',
        regimeAccent(signal.regime),
        signal.actionable
          ? 'hover:border-t-emerald/20'
          : 'opacity-90',
      )}
    >
      {/* ── HEADER ── */}
      <div className="p-4 pb-3">
        <div className="flex items-start justify-between gap-3">
          {/* Left: symbol + direction + badges */}
          <div className="flex flex-col gap-1.5">
            <div className="flex items-center gap-2.5">
              <span className="text-lg font-semibold tracking-tight text-foreground leading-none">
                {signal.symbol.replace('USDT', '')}
                <span className="text-muted-foreground font-normal text-sm">/USDT</span>
              </span>

              {/* Direction pill */}
              <span
                className={cn(
                  'text-[11px] font-bold px-2.5 py-0.5 rounded-sm tracking-wider',
                  isLong && 'bg-emerald/12 text-emerald border border-emerald/30',
                  isShort && 'bg-crimson/12 text-crimson border border-crimson/30',
                  !isLong && !isShort && 'bg-muted/30 text-muted-foreground border border-border',
                )}
              >
                {isLong ? '▲ LONG' : isShort ? '▼ SHORT' : 'NEUTRAL'}
              </span>

              {/* Live/Actionable badge */}
              {signal.actionable ? (
                <span className="text-[9px] font-bold text-emerald bg-emerald/10 px-1.5 py-0.5 rounded-sm border border-emerald/30 tracking-widest animate-pulse">
                  LIVE
                </span>
              ) : (
                <span className="text-[9px] font-semibold text-muted-foreground bg-muted/20 px-1.5 py-0.5 rounded-sm border border-border tracking-wider">
                  {score < minScore ? `${(score).toFixed(0)} < ${minScore}` : 'BELOW'}
                </span>
              )}
            </div>

            {/* Regime + 4h HTF */}
            <div className="flex items-center gap-2 text-xs">
              {signal.regime && signal.regime !== 'UNKNOWN' && (
                <span
                  className={cn(
                    'text-[10px] font-semibold px-1.5 py-0.5 rounded-sm border tracking-wide',
                    signal.regime.toLowerCase().includes('trend') || signal.regime === 'bull'
                      ? 'bg-emerald/8 border-emerald/20 text-emerald'
                      : signal.regime.toLowerCase().includes('vol')
                      ? 'bg-amber-warn/8 border-amber-warn/20 text-amber-warn'
                      : 'bg-cyan-accent/8 border-cyan-accent/20 text-cyan-accent',
                  )}
                >
                  {signal.regime}
                </span>
              )}
              {signal.htf_trend && (
                <span
                  className={cn(
                    'text-[10px] font-semibold px-1.5 py-0.5 rounded-sm border tracking-wide',
                    signal.htf_agrees
                      ? 'bg-emerald/8 border-emerald/20 text-emerald'
                      : signal.htf_trend === 'neutral'
                      ? 'bg-muted/20 border-border text-muted-foreground'
                      : 'bg-crimson/8 border-crimson/20 text-crimson',
                  )}
                  title={signal.htf_agrees ? '4h confirms direction' : '4h opposes direction'}
                >
                  4H {signal.htf_trend.toUpperCase()}
                  {signal.htf_agrees ? ' ✓' : ' ✗'}
                </span>
              )}
            </div>
          </div>

          {/* Right: score ring + timestamp */}
          <div className="flex flex-col items-end gap-1.5 shrink-0">
            {/* Score arc */}
            <div className="relative">
              <svg width="56" height="56" className="-rotate-90">
                {/* Track */}
                <circle
                  cx="28" cy="28" r={R}
                  stroke="oklch(0.25 0.03 260)"
                  strokeWidth="4"
                  fill="none"
                />
                {/* Progress */}
                <circle
                  cx="28" cy="28" r={R}
                  stroke="currentColor"
                  strokeWidth="4"
                  fill="none"
                  strokeDasharray={`${dash} ${C}`}
                  strokeLinecap="round"
                  className={cn(
                    'transition-all duration-500',
                    score >= 80 ? 'text-emerald' : score >= 65 ? 'text-cyan-accent' : score >= 50 ? 'text-amber-warn' : 'text-crimson',
                  )}
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className={cn('text-base font-bold font-mono leading-none tabular-nums', scoreColor(score))}>
                  {score.toFixed(0)}
                </span>
                <span className="text-[8px] text-muted-foreground tracking-wider mt-0.5">SCORE</span>
              </div>
            </div>

            {/* Timestamp */}
            <div className="flex items-center gap-1 text-[10px] text-muted-foreground">
              <Clock className="w-3 h-3" />
              {relTime(signal.scanned_at)}
            </div>
          </div>
        </div>
      </div>

      {/* ── GATE ROW ── */}
      <div className="px-4 pb-3">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="text-[9px] font-semibold tracking-[0.14em] uppercase text-muted-foreground mr-1">
            Gates
          </span>
          <GateCheck label="4H MTF" pass={mtfPass} />
          <GateCheck label="Regime" pass={regimePass} />
          <GateCheck label="No Anomaly" pass={anomalyPass} warn={signal.anomaly?.detected} />
          <GateCheck label="Setup Valid" pass={signal.setup?.valid ?? null} />
          {!allGatesPass && (
            <span className="text-[10px] text-crimson font-semibold ml-1">⚠ Gate flags</span>
          )}
        </div>
      </div>

      {/* ── PRICE RAIL ── */}
      {signal.setup?.valid && entry > 0 && (
        <div className="mx-4 mb-3 p-3 bg-navy-900/60 rounded-md border border-border/60">
          <div className="flex items-start gap-0 relative">
            {/* Direction arrow line */}
            <div
              className={cn(
                'absolute top-4 left-[52px] right-[calc(25%+8px)] h-px',
                isLong ? 'bg-gradient-to-r from-foreground/30 to-emerald/50' : 'bg-gradient-to-r from-crimson/50 to-foreground/30',
              )}
            />

            {/* Stop */}
            <div className={cn('flex-1 pr-2', isShort && 'order-last')}>
              <PricePoint label="STOP" value={sl} color="text-crimson" entry={entry} />
            </div>

            {/* Entry (center, larger) */}
            <div className="flex-1 px-2 border-x border-border/40 relative z-10">
              <PricePoint label="ENTRY" value={entry} color="text-foreground" />
            </div>

            {/* TP1 */}
            <div className="flex-1 px-2">
              <PricePoint label="TP1" value={tp1} color="text-emerald/70" entry={entry} />
            </div>

            {/* TP2 */}
            <div className="flex-1 pl-2">
              <PricePoint label="TP2" value={tp2} color="text-emerald" entry={entry} />
            </div>

            {/* R:R badge */}
            {rr > 0 && (
              <div className="flex flex-col items-end justify-center ml-3 shrink-0">
                <span className="text-[9px] font-semibold tracking-[0.12em] uppercase text-muted-foreground">R:R</span>
                <span
                  className={cn(
                    'text-sm font-bold font-mono tabular-nums',
                    rr >= 2.5 ? 'text-emerald' : rr >= 1.5 ? 'text-cyan-accent' : 'text-amber-warn',
                  )}
                >
                  {rr.toFixed(2)}×
                </span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* ── EXPANDED: INDICATORS + EVIDENCE ── */}
      {expanded && (
        <div className="px-4 pb-3 space-y-3 animate-in slide-in-from-top-2 duration-150">
          {/* Indicators */}
          {signal.indicators && (
            <div>
              <div className="text-[9px] font-semibold tracking-[0.14em] uppercase text-muted-foreground mb-2">
                Indicators
              </div>
              <div className="grid grid-cols-5 gap-3">
                <IndicatorPill label="RSI" value={signal.indicators.rsi} />
                <IndicatorPill label="ADX" value={signal.indicators.adx} />
                <IndicatorPill label="Trend" value={signal.indicators.trend} />
                <IndicatorPill label="Momentum" value={signal.indicators.momentum} />
                <IndicatorPill label="Volatility" value={signal.indicators.volatility} />
              </div>
            </div>
          )}

          {/* Scanners */}
          {signal.scanners.length > 0 && (
            <div>
              <div className="text-[9px] font-semibold tracking-[0.14em] uppercase text-muted-foreground mb-2">
                Scanner Hits
              </div>
              <div className="flex flex-wrap gap-1.5">
                {signal.scanners.map((s) => (
                  <span
                    key={s}
                    className="text-[10px] px-2 py-0.5 bg-navy-800 border border-border/60 rounded-sm text-foreground/80 font-medium"
                  >
                    {s.replace('Scanner', '')}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Evidence / Reasons */}
          {signal.reasons.length > 0 && (
            <div>
              <div className="text-[9px] font-semibold tracking-[0.14em] uppercase text-muted-foreground mb-2">
                Signal Evidence
              </div>
              <div className="flex flex-wrap gap-1.5">
                {signal.reasons.map((r, i) => (
                  <span
                    key={i}
                    className="text-[10px] px-2 py-0.5 bg-emerald/5 border border-emerald/15 rounded-sm text-emerald/80"
                  >
                    {r}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Anomaly detail */}
          {signal.anomaly?.detected && (
            <div className="flex items-start gap-2 p-2 bg-amber-warn/5 border border-amber-warn/20 rounded-md text-xs">
              <AlertTriangle className="w-3.5 h-3.5 text-amber-warn shrink-0 mt-0.5" />
              <span className="text-amber-warn/90">
                Anomaly detected — severity: {signal.anomaly.severity ?? 'unknown'}
                {signal.anomaly.types?.length ? ` · ${signal.anomaly.types.join(', ')}` : ''}
              </span>
            </div>
          )}
        </div>
      )}

      {/* ── FOOTER ── */}
      <div className="px-4 pb-4 pt-1 flex items-center justify-between gap-3 border-t border-border/40">
        {/* Strength label */}
        <span className="text-[10px] font-semibold tracking-wider text-muted-foreground uppercase">
          {signal.strength ?? '—'}
        </span>

        <div className="flex items-center gap-2">
          {/* Expand / collapse */}
          <button
            onClick={() => setExpanded((v) => !v)}
            className="flex items-center gap-1 text-[10px] text-muted-foreground hover:text-foreground transition-colors px-2 py-1 rounded-sm hover:bg-muted/20"
          >
            {expanded ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
            {expanded ? 'Less' : 'Details'}
          </button>

          {/* Execute */}
          <button
            disabled={!canExecute}
            onClick={() => canExecute && onExecute!(signal)}
            title={
              !signal.setup?.valid
                ? 'Setup invalid'
                : !signal.actionable
                ? `Score ${score.toFixed(0)} below threshold ${minScore}`
                : `Execute ${signal.direction} on ${signal.symbol}`
            }
            className={cn(
              'flex items-center gap-1.5 text-xs font-bold px-4 py-1.5 rounded-md transition-all duration-150',
              canExecute
                ? isLong
                  ? 'bg-emerald/12 text-emerald border border-emerald/40 hover:bg-emerald/20 hover:border-emerald/60 active:scale-95'
                  : 'bg-crimson/12 text-crimson border border-crimson/40 hover:bg-crimson/20 hover:border-crimson/60 active:scale-95'
                : 'bg-muted/20 text-muted-foreground/50 border border-border/50 cursor-not-allowed',
            )}
          >
            <Play className="w-3 h-3" />
            Execute {signal.direction !== 'NEUTRAL' ? signal.direction : ''}
          </button>
        </div>
      </div>
    </div>
  );
}
