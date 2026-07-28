# Engine Daily Brief — Artifact Spec

**Status:** DESIGN ONLY — blocked by COI-68 (VPS engine restart) AND COI-59 (Notion sync) for path A; or a `coinscope-engine` MCP build for path B.
**Author:** Scoopy session 2026-05-11
**Artifact ID (when built):** `coinscope-engine-brief`
**Sister artifacts:** `coinscope-connector-health`, `linear-open-tracker`, `coinscope-calendar-today`, `coinscope-drive-recent`

---

## Why the design is needed even though we can't ship yet

The artifact-sandbox blocks all network except 3 CDN URLs, so the artifact **cannot** call `https://api.coinscope.ai/*` directly. It must read engine state through an MCP. Today there is no engine MCP, and the Notion sync (path A) has been silent since 2026-04-05 (COI-59). This spec captures the layout + data contract so the moment either path unblocks, we can ship in ~1 hour without re-deciding the UX.

---

## Header

```
Engine Daily Brief — CoinScopeAI                    Last refreshed HH:MM:SS
Live trading engine state. Validation phase, testnet only — capital preservation first.
```

If data is stale (sync >2h old OR engine API last-success >5min ago), prepend a banner:

```
⚠ Engine data is N hours stale (last sync 2026-05-11 03:14). Check COI-68 / COI-59.
```

---

## Top stats (5 cells, single row)

| Cell | Source | Color rules |
|---|---|---|
| **P&L today** | `/performance` (or daily Trade Journal sum) | Green if positive, red if negative, faint if zero |
| **Open positions / max** | `/risk-gate` (`open_positions / MAX_OPEN_POSITIONS=5`) | Amber if ≥4, red if =5 |
| **Heat used** | `/risk-gate` (`current_heat / POSITION_HEAT_CAP_PCT=80`) | Amber if ≥60%, red if ≥80% |
| **Drawdown** | `/risk-gate` (`current_dd / MAX_DRAWDOWN_PCT=10`) | Amber if ≥5%, red if ≥10% |
| **Daily loss used** | `/risk-gate` (`daily_loss / MAX_DAILY_LOSS_PCT=5`) | Amber if ≥3%, red if ≥5% (gate flips to BLOCK) |

Click any cell → opens a focused detail in a modal or inline expansion.

---

## Section 1 — Risk Gate Status

A single prominent card showing:

- **Gate state:** `OPEN` (green) / `THROTTLED` (amber) / `BLOCKED` (red) — pulled from `/risk-gate`
- **If THROTTLED or BLOCKED:** the reason (e.g. "daily_loss=5.2% > 5% cap", "drawdown=10.1% > 10% cap")
- **Active thresholds:** show all 6 canonical thresholds with current vs. cap as small bars

Source: `GET /risk-gate`. Required fields in response: `state`, `reason?`, `thresholds: { max_leverage, max_open_positions, max_drawdown_pct, max_daily_loss_pct, position_heat_cap_pct, kelly_hard_cap_pct }`, `current: { open_positions, heat_pct, dd_pct, daily_loss_pct }`.

---

## Section 2 — Top Scan Candidates

Table from `/scan` showing top 10 scored candidates (or all candidates with score ≥ 8.0 — the Telegram alert threshold):

| Symbol | Side | Score | Regime | Confidence | Entry | Notes |
|---|---|---|---|---|---|---|
| BTCUSDT | LONG | 9.4/12 | Trending (87%) | high | 67,420 | RSI+EMA+Vol+CVD+Entry confluence |
| ... | | | | | | |

Color rules: score ≥ 9 → green; 8–8.99 → amber; <8 → faint. Regime color matches the regime taxonomy (Trending=emerald, Mean-Reverting=cyan, Volatile=amber, Quiet=muted).

Click row → opens a modal with the full scoring breakdown (`/journal` lookup).

Source: `GET /scan`. If path A: read from `NOTION_SCAN_HISTORY_DB=e72c5b69-fbbb-4a54-9dac-e6d4de3eb1a4`, sort by timestamp DESC, dedupe by symbol keeping latest.

---

## Section 3 — Open Positions

Table of currently-open positions:

| Symbol | Side | Entry | Current | Unrealized P&L | Size | Leverage | Heat | Age |
|---|---|---|---|---|---|---|---|---|

P&L colored green/red. Heat-warning if a single position is >40% of total heat cap.

Source: `GET /performance` or dedicated `/positions` if exposed. If path A: filter `NOTION_TRADE_JOURNAL_DB=43a542f4-b58d-4b1a-8979-043e72e9a6dd` where `status=OPEN`.

---

## Section 4 — Recent Decisions (last 24h)

Stream from `/journal` showing last ~15 entries — each row is a single gate decision or trade event:

```
03:42  GATE PASSED  BTCUSDT LONG  size=0.4% lev=3x  → ARMED
03:38  GATE FAILED  ETHUSDT LONG  reason: daily_loss=5.2% > 5%
03:21  REGIME CHANGE  SOLUSDT  Trending → Volatile (conf 0.71)
03:18  SCAN  12 candidates evaluated, 3 above 8.0
```

Color: green for ARMED/PROFIT, amber for SKIPPED/THROTTLED, red for BLOCKED/LOSS, faint for SCAN/REGIME.

Source: `GET /journal`. If path A: `NOTION_SIGNAL_LOG_DB=d4bf243e-8e87-494d-838b-a96658af395b` ordered by timestamp DESC limit 15.

---

## Section 5 — Performance Snapshot

Compact set of metrics from `/performance`:

- Today: P&L, # trades, hit rate, avg R
- Last 7d: P&L, # trades, hit rate, avg R, max DD intraweek
- Last 30d: P&L, # trades, hit rate, Sharpe, max DD
- Cumulative since validation phase start (2026-04-08): P&L, # trades, hit rate

If path A: roll up `NOTION_TRADE_JOURNAL_DB` rows where `status=CLOSED`.

---

## Section 6 — Regime Map (watched symbols)

Compact grid of symbols → current regime:

```
BTCUSDT   ●Trending  87%
ETHUSDT   ●Trending  82%
SOLUSDT   ●Volatile  71%   ← changed from Trending 22min ago
XRPUSDT   ●Mean-Rev  68%
…
```

Color matches regime taxonomy. Bold/animated dot if regime changed in the last hour.

Source: `GET /regime/{symbol}` for each watched symbol (parallel calls). If path A: derive from latest scan entries per symbol.

---

## Footer

```
Probes 6 engine endpoints (path B) OR 3 Notion DBs (path A) on every reload. Validation phase
through ~2026-05-31; capital preservation first. Reload via header button.
Memory rule: feedback_cowork_callmcp_envelope.md — always unwrap MCP responses.
```

---

## Color taxonomy (consistent with sister artifacts)

| Color | Means |
|---|---|
| Green | Healthy, profit, gate open, trending regime |
| Red | Failure, loss, gate blocked, urgent, volatile risk |
| Amber | Warning, throttled, approaching cap, volatile regime, focus block |
| Blue | In-progress, todo, mean-reverting regime |
| Violet | All-day event, special category |
| Faint gray | Quiet regime, backlog, not-yet-loaded, OOO |

---

## Data contract (path A — Notion DBs)

For the Notion-mediated path to work, the engine needs to write the following fields on each event:

### NOTION_SCAN_HISTORY_DB (e72c5b69)
Required properties: `timestamp` (date), `symbol` (title), `side` (select: LONG/SHORT), `score` (number), `regime` (select), `regime_confidence` (number), `entry_price` (number), `conditions_met` (multi-select), `alert_dispatched` (checkbox).

### NOTION_SIGNAL_LOG_DB (d4bf243e)
Required: `timestamp` (date), `symbol` (title), `event_type` (select: SCAN/GATE_PASSED/GATE_FAILED/REGIME_CHANGE/ARMED/EXECUTED/CLOSED), `reason` (rich_text), `score` (number), `regime` (select), `confidence` (number).

### NOTION_TRADE_JOURNAL_DB (43a542f4)
Required: `timestamp` (date), `symbol` (title), `side` (select), `status` (select: OPEN/CLOSED/CANCELLED), `entry_price` (number), `exit_price` (number, nullable), `size_pct_equity` (number), `leverage` (number), `pnl_usd` (number, nullable), `pnl_r` (number, nullable), `regime_at_entry` (select), `gate_state_at_entry` (select).

If actual schemas drift from this contract, update the artifact's parser BEFORE shipping.

---

## Data contract (path B — engine MCP)

Required MCP tools (when built — server name TBD, suggest `coinscope-engine`):

| MCP tool | Wraps | Args | Returns |
|---|---|---|---|
| `mcp__coinscope-engine__scan` | `GET /scan` | none or `min_score` | `{ candidates: [{symbol, side, score, regime, regime_confidence, entry_price, conditions_met}] }` |
| `mcp__coinscope-engine__risk_gate` | `GET /risk-gate` | none | `{ state, reason?, thresholds, current }` |
| `mcp__coinscope-engine__regime` | `GET /regime/{symbol}` | `symbol` | `{ symbol, regime, confidence, ts }` |
| `mcp__coinscope-engine__performance` | `GET /performance` | optional `period` | `{ today: {...}, last_7d: {...}, last_30d: {...}, cumulative: {...} }` |
| `mcp__coinscope-engine__journal` | `GET /journal` | optional `limit`, `since` | `{ entries: [{ts, type, symbol, ...}] }` |
| `mcp__coinscope-engine__position_size` | `POST /position-size` | `{symbol, side, score}` | `{ size_pct_equity, kelly_fraction, applied_cap, reason }` |

Read-only by convention. Never expose any write/execute path.

---

## Build trigger

Artifact will be built when EITHER:
- Path A: COI-68 closed AND COI-59 closed AND a single test row appears in each of the 3 Notion DBs (verifies sync is actually flowing). Then build + ship in ~1 hour.
- Path B: A `coinscope-engine` MCP is built and connected. Then build + ship in ~1 hour.

Until then this spec is the source of truth for the design.
