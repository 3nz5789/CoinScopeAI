# Canonical Operator Workflow

**Status:** current
**Audience:** the operator running the engine during P0 testnet validation
**Phase:** P0 — May 2026, Binance Testnet only
**Related:**
- [`daily-ops.md`](daily-ops.md) — event-driven response playbook
- [`daily-market-scan-runbook.md`](daily-market-scan-runbook.md) — detailed scan procedure
- [`release-checklist.md`](release-checklist.md) — deploy gate
- [`../risk/failsafes-and-kill-switches.md`](../risk/failsafes-and-kill-switches.md) — kill switch and circuit breaker reference

This document is the single entry point for running a complete operator session. It defines the lifecycle from session start to session close — every step, in order, with no assumed knowledge of what came before. All other runbooks are referenced from here; do not repeat their content.

**Guiding principle: Capital preservation first. Every step that looks optional is a risk control in disguise. Do not skip.**

---

## The lifecycle at a glance

```
SESSION START
     │
     ▼
[1] ENVIRONMENT CHECK    — engine, adapters, breakers, kill switch
     │
     ▼
[2] RISK GATE CHECK      — is trading open today?
     │ gate closed → stop here, log, close session
     ▼
[3] MARKET SCAN          — score candidates across tracked symbols
     │ no signals ≥ 5.5 → log, optionally retry in 30 min
     ▼
[4] SIGNAL REVIEW        — regime · MTF · funding · OI delta
     │ signal fails review → discard, return to [3]
     ▼
[5] POSITION SIZING      — Kelly-fractional size query
     │ size + existing heat > 80% → reduce or skip
     ▼
[6] TRADE EXECUTION      — manual entry on Binance Testnet
     │
     ▼
[7] JOURNAL              — log to Notion and engine journal endpoint
     │
     ▼
[8] MONITORING           — watch during session, respond to alerts
     │
     ▼
[9] SESSION CLOSE        — performance review, operator log, sync
     │
     ▼
SESSION END
```

---

## Step 1 — Environment check

Run before any trading activity. If any check fails, resolve it before proceeding.

```bash
# Engine health
curl -s https://api.coinscope.ai/health | python3 -m json.tool
curl -s https://api.coinscope.ai/ready | python3 -m json.tool
```

Expected: both return `"status": "ok"`. `/ready` additionally shows adapter and artifact states — every field must be `"ok"` or `"healthy"`.

```bash
# Or use the daily status script (polls all 6 endpoints)
./scripts/daily_status.sh
```

**If the engine is down:**

1. SSH to VPS: `ssh <vps-host>`
2. `cd <engine-dir> && docker compose up -d --force-recreate`
3. Wait 15 seconds, re-run health check.
4. If still failing, see [`troubleshooting.md`](troubleshooting.md).

**If the engine is up but adapters are degraded:** Check Binance Testnet status at `https://testnet.binancefuture.com`. If the issue is on Binance's side, wait — do not trade on degraded data.

---

## Step 2 — Risk gate check

The gate is the first decision point. If it is closed, the session ends here.

```bash
curl -s https://api.coinscope.ai/risk-gate | python3 -m json.tool
```

Read three fields:

| Field | Safe value | Meaning if triggered |
|---|---|---|
| `daily_loss_limit_hit` | `false` | Daily 5% loss reached — no new trades today |
| `drawdown_limit_hit` | `false` | 10% drawdown from peak — kill switch protocol |
| `kill_switch.engaged` | `false` | All entries halted — investigate before disarming |

**If any field is `true`:**

- `daily_loss_limit_hit` → Stop. Log to Notion operator log. Close session. Resets at 00:00 UTC.
- `drawdown_limit_hit` → Kill switch protocol. See [`../risk/failsafes-and-kill-switches.md`](../risk/failsafes-and-kill-switches.md). Do not resume without a written review.
- `kill_switch.engaged` → Determine who engaged it and why before touching anything.

**If the gate is open (`all false`):** Proceed to Step 3.

---

## Step 3 — Market scan

```bash
curl -s https://api.coinscope.ai/scan | python3 -m json.tool
```

Or via the scanner script for a full formatted table:

```bash
python scripts/market_scanner.py --top 5 --min-score 5.5 --tf 4h
```

**Score filter:** Discard anything below 5.5. Do not lower this threshold to force a trade.

**If no signals ≥ 5.5:** Log "no signals" to the Notion Scan History DB and either:
- Wait 30 minutes and re-scan, or
- Close the session — no trade is a valid outcome.

Do not force a trade when the scanner sees no opportunity.

**Scan History DB:** `e72c5b69-fbbb-4a54-9dac-e6d4de3eb1a4`

---

## Step 4 — Signal review

For each candidate above the score threshold, apply this review in order. A single failure discards the signal.

### 4a — Regime check

```bash
curl -s https://api.coinscope.ai/regime/BTCUSDT | python3 -m json.tool
```

(Replace `BTCUSDT` with the candidate symbol — no slash, engine format.)

| Regime | Confidence required | Action |
|---|---|---|
| Trending | ≥ 0.65 | Full size eligible |
| Mean-Reverting | ≥ 0.70 | Eligible — oscillator signals only |
| Volatile | ≥ 0.75 | Eligible at 0.3× Kelly — only scores ≥ 8.0 |
| Quiet | ≥ 0.75 | Eligible at 0.3× Kelly — only scores ≥ 8.0 |

If confidence is below the threshold for the regime, treat the regime as indeterminate — apply Volatile/Quiet rules.

### 4b — Multi-timeframe confirmation

Look at the `mtf_confirmation` field in the scan output.

- `✅` → confirmed across 15m / 1h / 4h — proceed
- `⚠️` → partial — proceed at reduced size (50%)
- `❌` → conflicting — discard the signal

### 4c — Funding rate

Check the `funding_rate` field in the scan output.

- Long signal + funding rate > +0.08% → mean-reversion risk — skip or wait for funding reset
- Short signal + funding rate < -0.08% → mean-reversion risk — skip or wait for funding reset

Funding resets every 8 hours on Binance Perpetuals (00:00, 08:00, 16:00 UTC).

### 4d — Open interest delta

Check `oi_change_1h` in the scan output.

- OI declining while price is rising on a long signal → divergence — reduce confidence, consider skipping
- OI declining while price is falling on a short signal → short-covering likely — skip

If the signal passes all four checks (4a–4d), proceed to Step 5.

---

## Step 5 — Position sizing

```bash
curl -s "https://api.coinscope.ai/position-size?symbol=BTCUSDT" | python3 -m json.tool
```

The endpoint returns `recommended_size_usdt` and `leverage` calculated by the fractional Kelly pipeline.

**Before accepting the recommendation, verify the hard limits:**

```bash
# Check current heat (total deployed capital)
curl -s https://api.coinscope.ai/risk-gate | python3 -c "import json,sys; d=json.load(sys.stdin); print('heat:', d.get('position_heat_pct','?'), '%')"
```

| Hard limit | Value | Override |
|---|---|---|
| Max leverage | 10× | Never exceed |
| Max open positions | 5 | Count open positions before entry |
| Position heat cap | 80% | (heat + new size) must be ≤ 80% |
| Per-trade size cap | 2% of equity | Kelly hard cap — engine enforces |
| Daily loss limit | 5% | Gate enforces — still your responsibility to track manually |

If adding this position would breach any limit: reduce the size to fit, or skip the trade.

---

## Step 6 — Trade execution

**Binance Testnet only during P0. Do not execute on mainnet.**

Testnet: `https://testnet.binancefuture.com`

1. Open the position manually using the recommended size and leverage from Step 5.
2. Set a stop-loss immediately upon entry. Do not leave a position without a stop.
3. Set a take-profit target. Record entry, stop, and target before proceeding to Step 7.

**Suggested stop placement:** 1.5× ATR from entry (the scanner reports ATR in the signal output). Tighter stops are acceptable; wider stops reduce the effective R and may require further size reduction to stay within the 2% per-trade cap.

---

## Step 7 — Journal

Log every trade and every scan — whether or not a trade was taken.

### Scan log (every session, always)

Log to Notion Scan History DB (`e72c5b69-fbbb-4a54-9dac-e6d4de3eb1a4`):

| Field | What to record |
|---|---|
| Timestamp | UTC |
| Pairs scanned | Full list |
| Top signal | Pair, direction, score, regime |
| Gate status | Open / closed at scan time |
| Action | Trade taken / skipped / no signals |
| Mode | Engine / Standalone |

### Trade log (only when a trade is entered)

Log to Notion Trade Journal (`43a542f4-b58d-4b1a-8979-043e72e9a6dd`):

| Field | What to record |
|---|---|
| Symbol | e.g. BTCUSDT |
| Side | LONG / SHORT |
| Entry price | Exact fill |
| Stop loss | Price level |
| Take profit | Price level |
| Signal score | From scanner |
| Position size (USDT) | Actual, post-sizing |
| Leverage | Actual |
| Regime at entry | Label + confidence |

### Engine journal (every session)

```bash
curl -s "https://api.coinscope.ai/journal?limit=10" | python3 -m json.tool
```

Confirm the latest gate decisions and trade events are recorded. If a trade was taken and is missing from the journal, flag it — the journal is append-only and the primary audit trail.

---

## Step 8 — Monitoring during session

You do not need to watch continuously. Check once per hour, or when a Telegram alert fires.

### Routine hourly check (30 seconds)

```bash
curl -s https://api.coinscope.ai/risk-gate | python3 -c "
import json,sys
d=json.load(sys.stdin)
print('daily_loss:', d.get('daily_loss_limit_hit'))
print('drawdown:  ', d.get('drawdown_limit_hit'))
print('kill_sw:   ', d.get('kill_switch',{}).get('engaged'))
print('heat:      ', d.get('position_heat_pct','?'), '%')
"
```

All fields should be `False` / `False` / `False`. Heat should be below 80%.

### When a Telegram alert fires

| Severity | Alert type | Action |
|---|---|---|
| 🔴 CRITICAL | Max drawdown breaker | Do not reset immediately — read journal first. See [`daily-ops.md`](daily-ops.md) |
| 🔴 CRITICAL | Kill switch engaged | Investigate before touching anything |
| 🔴 CRITICAL | Adapter banned (HTTP 418) | Engine halted — wait for Binance ban to clear |
| 🟡 WARN | Daily loss breaker | Auto-resets 00:00 UTC — review trades, do not add positions |
| 🟡 WARN | Consecutive-losses breaker | Auto-resets 24h — review the four losses for pattern |
| 🟡 WARN | WebSocket reconnect | Isolated = ignore. Repeating = engage kill switch, investigate |
| ℹ️ INFO | Daily P&L digest (21:00 UTC) | Read and log to weekly validation doc |
| ℹ️ INFO | Signal alert (score ≥ 8.0) | Review — not an instruction to trade, a candidate to evaluate |

Full response procedures: [`daily-ops.md`](daily-ops.md).

---

## Step 9 — Session close

Run at the end of every session, regardless of whether any trades were taken.

### 9a — Performance snapshot

```bash
curl -s https://api.coinscope.ai/performance | python3 -m json.tool
```

Note:
- `win_rate` — target ≥ 55% over rolling 30 days
- `profit_factor` — target ≥ 1.5
- `current_drawdown` — flag in the operator log if > 7% (alert zone before 10% hard stop)
- `open_positions` — confirm count and that each has a stop set

### 9b — Operator log entry

Every session gets one line in `docs/validation/operator-log.md`:

```
YYYY-MM-DD HH:MM UTC — [SESSION START/CLOSE] <brief note>
Examples:
2026-05-12 18:30 UTC — session close. 1 scan, 1 trade (BTC LONG 8.5 score). No alerts. Drawdown 1.2%.
2026-05-12 09:00 UTC — session close. Gate open. 2 scans, no signals above 5.5. No trades.
2026-05-12 14:00 UTC — session close. Daily loss breaker tripped at 13:44. No new trades. Gate resets 00:00.
```

This log is reviewed end-to-end at validation close. Missing entries are worse than terse ones.

### 9c — Drift and guardrail check (if any files were edited this session)

```bash
python3 scripts/drift_detector.py
python3 scripts/risk_threshold_guardrail.py
```

Both must pass clean. If either fails, do not close the session — resolve the discrepancy first.

### 9d — Git sync (if code or docs were changed)

```bash
cd ~/Projects/coinscope-ai
git add -A
git status
```

Review the diff. If the changes are what you expect, commit and push via a branch — never directly to `main`.

---

## Quick reference — canonical values

| Parameter | Value | Variable |
|---|---|---|
| Max leverage | 10× | `MAX_LEVERAGE` |
| Max open positions | 5 | `MAX_OPEN_POSITIONS` |
| Max drawdown | 10% from peak | `MAX_DRAWDOWN_PCT` |
| Daily loss limit | 5% rolling 24h | `MAX_DAILY_LOSS_PCT` |
| Position heat cap | 80% deployed | `POSITION_HEAT_CAP_PCT` |
| Per-trade size cap | 2% of equity | `KELLY_HARD_CAP_PCT` |
| Min signal score | 5.5 | `SIGNAL_MIN_SCORE` |
| Telegram alert threshold | 8.0 | hardcoded in alert layer |
| P0 validation window | May 2026 | — |

All values above are locked for P0. Any PR touching them is blocked by CI guardrail.

---

## What a clean session looks like (no trade taken)

```
09:00 UTC  → Step 1: ./scripts/daily_status.sh — all green
09:01 UTC  → Step 2: /risk-gate — gate open
09:02 UTC  → Step 3: scan — 2 candidates, scores 5.8 and 4.9
09:03 UTC  → Step 4: review — 5.8 signal fails MTF (❌ conflicting)
             → 4.9 below threshold, discarded
09:04 UTC  → No eligible signals. Logged to Notion Scan History.
09:05 UTC  → Session close. Operator log: "09:05 UTC — 1 scan, no eligible signals. Gate open."
```

Total time: 5 minutes. No trade is a valid and often correct outcome.

---

## What a clean session looks like (trade taken)

```
13:00 UTC  → Step 1: health + ready — green
13:01 UTC  → Step 2: risk-gate — open, heat 22%
13:02 UTC  → Step 3: scan — ETHUSDT LONG, score 8.2
13:03 UTC  → Step 4: regime Trending 0.89 ✅ · MTF ✅ · funding -0.002% ✅ · OI +1.8% ✅
13:04 UTC  → Step 5: /position-size → 480 USDT, 5× leverage. Heat check: 22% + 480/balance < 80% ✅
13:05 UTC  → Step 6: entered ETHUSDT LONG on testnet. Stop 1.5× ATR below entry. TP set.
13:06 UTC  → Step 7: logged to Notion Scan History + Trade Journal. Engine /journal confirms.
13:06 UTC  → Step 8: monitoring active. Check /risk-gate hourly.
16:30 UTC  → TP hit. Position closed.
16:31 UTC  → Step 9a: /performance — win rate 61%, drawdown 0.8%
16:32 UTC  → Step 9b: operator log entry written.
16:33 UTC  → Session close.
```

---

## Hard stops — conditions that end the session immediately

| Condition | Action |
|---|---|
| `drawdown_limit_hit: true` | Stop all activity. Kill switch protocol. No exceptions. |
| Engine returning stale or mock data | Engage kill switch. Investigate data source before resuming. |
| Binance Testnet unreachable > 15 min | Close open positions manually if accessible. Do not trade blind. |
| You are unsure about any step | Stop. Review the relevant runbook. If still unclear, do not trade. |

---

*Last updated: 2026-05-12 | Applies to: P0 validation phase (Binance Testnet only)*
*For post-P0 mainnet procedures, see [`release-checklist.md`](release-checklist.md) — Mainnet Cutover section.*
