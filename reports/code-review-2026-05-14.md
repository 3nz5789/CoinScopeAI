# CoinScopeAI Daily Code Review
**Date:** 2026-05-14  
**Modules Reviewed:** `scanner/`, `signals/`, `alerts/`, `data/`, `risk/`  
**Findings:** 3 Critical · 6 High · 8 Medium · 8 Low

---

## CRITICAL

### CRIT-1 — Live Credentials in `.env` File
**File:** `coinscope_trading_engine/.env` (lines 3–4, 13–14)

Real Binance Testnet API keys and a live Telegram Bot Token are committed to the project:
```
BINANCE_TESTNET_API_KEY=JuSaQ6j7zzf1M2dHGRLDVtXciniPQJC6PPBvMi09mAsXgpEo9XbXXaHenA6F8uZx
BINANCE_TESTNET_API_SECRET=P4njvs2ZvMt8phXiFOkhU1OG24Soh0IsshvO8dMlmqW594V9m3TZMFuIk2cHl5qZ
TELEGRAM_BOT_TOKEN=8318444001:AAFc6wBXqufO2j8h3_XJ3G369Nb71nfKfho
TELEGRAM_CHAT_ID=7296767446
```
**Action:** Rotate all credentials immediately. Add `.env` to `.gitignore`. Verify git history doesn't already expose them. Commit only `.env.example` with placeholder values.

---

### CRIT-2 — Blocking `requests.post()` in Async Event Loop
**File:** `alerts/telegram_alerts.py` lines 28–36

`TelegramAlerts` (legacy class, still imported by some orchestrators) uses synchronous `requests.post()`. Called from the asyncio event loop, this blocks everything — scanning, WebSocket processing, signal generation — for up to 5 seconds per call.

```python
# WRONG — blocks the event loop
def _send(self, text: str):
    requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", timeout=5)

# FIX — use the async TelegramNotifier (already exists in alerts/telegram_notifier.py)
```
**Action:** Remove all imports of `TelegramAlerts`. Replace with `TelegramNotifier` everywhere.

---

### CRIT-3 — Threading + `time.sleep` in Async Codebase
**File:** `scanners/liquidation_scanner.py` line 143

The legacy scanner uses `threading.Thread` + `threading.Lock` + `time.sleep(5)` for reconnect. Mixed with the asyncio event loop, this creates a fragile concurrency model prone to deadlocks and unclean shutdown.

**Action:** Consolidate on the new `scanner/liquidation_scanner.py` (already async). Delete `scanners/` or move to `archive/`.

---

## HIGH

### HIGH-1 — Dual Scanner Modules with Incompatible Interfaces
**Files:** `scanner/` (async, new) vs `scanners/` (sync/threading, legacy)

`signals/signal_generator.py` imports from the **old** `scanners/` module while all other infrastructure uses `scanner/`. The two modules have incompatible return types (`dict` vs `ScannerResult`), making them impossible to use interchangeably.

**Action:** Migrate `signal_generator.py` to `scanner/`. Delete `scanners/`. This is a production blocker.

---

### HIGH-2 — Race Condition in `AlertRateLimiter.allow_signal()`
**File:** `alerts/rate_limiter.py` lines 261–265

Symbol token is consumed under a `threading.Lock` but the refund writes `_tokens` directly without acquiring the lock:
```python
# BUG — refund outside lock, can over-credit
self._get_symbol_bucket(symbol)._tokens = min(capacity, tokens + 1)

# FIX — add a locked _refund() method on _TokenBucket
def _refund(self, n: int = 1):
    with self._lock:
        self._tokens = min(self._capacity, self._tokens + n)
```

---

### HIGH-3 — `ExposureTracker` Properties Read `_positions` Without Lock
**File:** `risk/exposure_tracker.py` lines 195–231

All `@property` accessors (`total_notional`, `unrealised_pnl`, `is_over_exposed`, etc.) iterate `self._positions` without acquiring the asyncio lock. A concurrent `close_position()` can mutate the dict mid-iteration causing `RuntimeError: dictionary changed size during iteration` or stale risk reads.

**Action:** Convert read-heavy properties to `async` methods that acquire the lock, or snapshot the dict while locked.

---

### HIGH-4 — `BreakerState.COOLDOWN` Is a Dead State
**File:** `risk/circuit_breaker.py` lines 57, 115

`COOLDOWN` is declared in the enum but never assigned. `_trip()` sets `OPEN`, and `_maybe_auto_reset()` goes directly `OPEN → CLOSED`. Any code checking `state == BreakerState.COOLDOWN` always gets `False`.

**Action:** Either insert `self._state = BreakerState.COOLDOWN` during the auto-reset wait period, or remove the enum value.

---

### HIGH-5 — `signal_generator.py` Calls Old Sync Scanner Interface
**File:** `signals/signal_generator.py` lines 101–102

```python
res = self.liq_scan.scan(symbol)   # old sync dict interface
return int(res["signal"])           # breaks silently on ScannerResult
```
After fixing HIGH-1, this will `TypeError` silently (wrapped in `try/except`). Update to `await` the new async scanner.

---

### HIGH-6 — EMA Computed with Pure Python Loop — CPU Bottleneck
**File:** `signals/indicator_engine.py` lines 324–331

`_ema()` uses a Python `for` loop called 10+ times per `compute()`. Under heavy multi-symbol scanning this becomes a significant CPU drain.

```python
# SLOW — Python loop
for i in range(1, len(data)):
    out[i] = data[i] * k + out[i-1] * (1 - k)

# FAST — vectorised pandas
import pandas as pd
pd.Series(data).ewm(span=period, adjust=False).mean().to_numpy()
```

---

## MEDIUM

| ID | File | Issue |
|---|---|---|
| MED-1 | `alerts/alert_queue.py` | `AlertQueue` not wired to `AlertRateLimiter` — rate limits bypass-able |
| MED-2 | `scanner/pattern_scanner.py` | Runtime imports of private functions from `volume_scanner` — hidden coupling |
| MED-3 | `scanner/liquidation_scanner.py` | Late `import api` circular dependency — makes unit testing impossible |
| MED-4 | `signals/indicator_engine.py` | RSI guard `n >= 15` too low — Wilder smoothing never runs; change to `n >= 29` |
| MED-5 | `data/cache_manager.py` | `get_all_signals()` uses `REDIS KEYS *` (O(N), blocking) — replace with `SCAN` cursor |
| MED-6 | `risk/position_sizer.py` | `float = None` type mismatch; `or` pattern fails silently if value is `0` |
| MED-7 | `alerts/scale_up_manager.py` | State file written to relative path — resets if engine launched from wrong dir |
| MED-8 | `data/scanner` | `rest.is_throttled` property exists but never checked before scan API calls |

---

## LOW

| ID | File | Issue |
|---|---|---|
| LOW-1 | `signals/indicator_engine.py` | OBV resets to 0 each call — window-relative semantics undocumented |
| LOW-2 | `alerts/` | Two Telegram senders (`telegram_alerts.py`, `telegram_notifier.py`) — unclear authority |
| LOW-3 | `signals/confluence_scorer.py` | `score_all()` is O(S×R) — fix with `defaultdict` groupby before loop |
| LOW-4 | `alerts/webhook_dispatcher.py` | `hmac.new()` deprecated since Python 3.4 — use `hmac.HMAC()` |
| LOW-5 | `scanner/base_scanner.py` | Exceptions stored as `str(exc)` — type info lost; add `exc_info=True` to logger |
| LOW-6 | `signals/indicator_engine.py` | EMA recomputed redundantly on same array 5+ times; memoize within `compute()` |
| LOW-7 | `risk/position_sizer.py` | `leverage_used` is a heuristic formula, not actual exchange leverage — misleading |
| LOW-8 | `data/cache_manager.py` | `CacheManager.keys()` docstring says "use sparingly" but called in hot API path |

---

## Recommended Priority Order

1. **Immediately:** Rotate `.env` credentials (CRIT-1)
2. **This sprint:** Fix CRIT-2/3, HIGH-1 (scanner consolidation), HIGH-3 (lock gap in ExposureTracker)
3. **Next sprint:** HIGH-4/5/6, MED-4 (RSI guard), MED-5 (Redis KEYS), MED-8 (throttle enforcement)
4. **Backlog:** All LOW items and remaining MEDs

---

*Generated by Scoopy automated daily review · 2026-05-14 09:00*
