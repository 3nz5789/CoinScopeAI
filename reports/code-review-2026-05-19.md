# CoinScopeAI — Daily Code Review
**Date:** 2026-05-19  
**Scope:** `scanner/`, `signals/`, `alerts/`, `data/`, `risk/`  
**Reviewer:** Automated (Scoopy / Claude)  
**Engine commit:** HEAD (no git log available)

---

## Executive Summary

The codebase is well-structured and shows consistent design discipline — the abstract scanner pattern, the priority alert queue, and the correlation/exposure risk layer are all production-quality. However, **two critical blocking issues** exist that would cause hard failures in production: a blocking synchronous HTTP call in an async codebase, and a broken module-path import strategy in the signal generator. Three medium-severity bugs also need attention before the next live trading session.

| Severity | Count | Files |
|---|---|---|
| 🔴 Critical | 2 | `alerts/telegram_alerts.py`, `signals/signal_generator.py` |
| 🟠 High | 2 | `alerts/rate_limiter.py`, `data/binance_rest.py` |
| 🟡 Medium | 3 | `signals/confluence_scorer.py`, `risk/circuit_breaker.py`, `alerts/alert_queue.py` |
| 🔵 Low | 2 | `risk/position_sizer.py`, `scanner/funding_rate_scanner.py` |

---

## 1. Critical Issues

### 🔴 C-1 — Blocking `requests` library in async context (`alerts/telegram_alerts.py`)

**Severity:** Critical — event loop blocking  
**File:** `coinscope_trading_engine/alerts/telegram_alerts.py`

The legacy `TelegramAlerts` class uses the synchronous `requests.post()` to send every Telegram message. Because the engine runs entirely on a single asyncio event loop, each Telegram send **freezes the entire event loop** for the duration of the HTTP round-trip — typically 200–600 ms. During high-volatility moments when the circuit breaker fires, this blocks risk management callbacks, scanner loops, and all other coroutines.

```python
# CURRENT — BROKEN: blocks the event loop on every send
import requests

def _send(self, text: str) -> bool:
    url = f"https://api.telegram.org/bot{self._token}/sendMessage"
    resp = requests.post(url, json={...}, timeout=10)  # ← blocks event loop
    return resp.ok
```

**Fix:** Use `httpx` (already a project dependency — `telegram_notifier.py` uses it correctly) or `aiohttp`:

```python
# CORRECT — non-blocking
import httpx

async def _send(self, text: str) -> bool:
    url = f"https://api.telegram.org/bot{self._token}/sendMessage"
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(url, json={...})
    return resp.is_success
```

**Note:** `telegram_notifier.py` already has the correct async implementation using `httpx`. `telegram_alerts.py` appears to be a legacy module that should be deprecated and removed. Confirm all callers reference `TelegramNotifier` (from `telegram_notifier.py`) rather than `TelegramAlerts`.

---

### 🔴 C-2 — `sys.path` hack and mismatched import paths (`signals/signal_generator.py`)

**Severity:** Critical — `ImportError` at runtime  
**File:** `coinscope_trading_engine/signals/signal_generator.py`

Two distinct problems in this file will cause `ImportError` when `signal_generator` is imported as part of the installed package:

**Problem A — `sys.path.insert` at module level:**
```python
# Lines 1–5 (approximate)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```
This is a development workaround that breaks as soon as the package is installed via `pip install -e .` or run from any directory other than the repo root. It also hides import errors.

**Problem B — Wrong module name (`scanners` vs `scanner`):**
```python
# WRONG — module does not exist
from scanners.volume_scanner import VolumeScanner
from scanners.liquidation_scanner import LiquidationScanner

# CORRECT — actual package name is scanner (singular)
from scanner.volume_scanner import VolumeScanner
from scanner.liquidation_scanner import LiquidationScanner
```

The physical directory is `coinscope_trading_engine/scanner/` (singular). The `scanners` (plural) package does not exist. This import will fail silently in dev (if `sys.path` accidentally includes a stale cached copy) or loudly with `ModuleNotFoundError` in production.

**Fix:**
1. Remove the `sys.path.insert` block entirely.
2. Correct the import paths:

```python
# Remove sys.path hack entirely, then fix imports:
from scanner.volume_scanner import VolumeScanner
from scanner.liquidation_scanner import LiquidationScanner
```

Ensure `pyproject.toml` / `setup.cfg` lists `coinscope_trading_engine` as the root package so all relative imports resolve correctly.

---

## 2. High Severity Issues

### 🟠 H-1 — Race condition in `AlertRateLimiter.allow_signal()` token refund (`alerts/rate_limiter.py`)

**Severity:** High — data race, possible negative token count  
**File:** `coinscope_trading_engine/alerts/rate_limiter.py`

In `allow_signal()`, when the per-symbol token is consumed but the Telegram bucket is exhausted, the code refunds the symbol token by directly mutating `_tokens` without holding the bucket lock:

```python
async def allow_signal(self, symbol: str) -> bool:
    symbol_ok = self._symbol_bucket(symbol).try_consume()  # acquires lock internally
    if not symbol_ok:
        return False

    telegram_ok = self._telegram_bucket.try_consume()
    if not telegram_ok:
        # BUG: direct attribute access outside the lock
        self._symbol_buckets[symbol]._tokens += 1.0   # ← no lock held here
        return False
    return True
```

`_TokenBucket._tokens` is a `float` attribute protected by `threading.Lock` inside `try_consume()`, but the refund bypasses that lock entirely. Under concurrent access (e.g., two symbols arriving simultaneously), this produces a race condition that can corrupt `_tokens`.

**Fix:** Add a `refund()` method to `_TokenBucket` that acquires the lock:

```python
@dataclass
class _TokenBucket:
    ...
    def refund(self, amount: float = 1.0) -> None:
        with self._lock:
            self._tokens = min(self._tokens + amount, self.capacity)

# In allow_signal():
if not telegram_ok:
    self._symbol_buckets[symbol].refund()
    return False
```

---

### 🟠 H-2 — Throttle property not enforced automatically (`data/binance_rest.py`)

**Severity:** High — rate limit violations under load  
**File:** `coinscope_trading_engine/data/binance_rest.py`

The client tracks Binance API weight via `X-MBX-USED-WEIGHT-1M` response headers and exposes `is_throttled` as a property:

```python
@property
def is_throttled(self) -> bool:
    return self._used_weight >= int(self._rate_limit * 0.85)
```

However, no request method checks `is_throttled` before firing the next call. Under a full-symbol scan of 200+ pairs, the engine can exceed the 85% threshold and continue making requests until Binance returns HTTP 429 or bans the IP.

**Fix:** Add a guard at the top of `_request()` (the private dispatcher that all public methods call through):

```python
async def _request(self, method: str, endpoint: str, **kwargs):
    if self.is_throttled:
        wait_s = 60 - (time.monotonic() % 60) + 1   # wait until next 1-min window
        logger.warning(
            "Rate limit at %.0f%% — sleeping %.1fs before request.",
            (self._used_weight / self._rate_limit) * 100, wait_s
        )
        await asyncio.sleep(wait_s)
    # ... existing retry/sign logic
```

Alternatively, implement a semaphore or token bucket that mirrors the Binance weight budget.

---

## 3. Medium Severity Issues

### 🟡 M-1 — `bonuses` list shadowed, bonus reasons never recorded (`signals/confluence_scorer.py`)

**Severity:** Medium — silent data loss in signal reasoning  
**File:** `coinscope_trading_engine/signals/confluence_scorer.py`

Inside `ConfluenceScorer.score()`, `_apply_indicator_bonuses()` is called twice — once to compute the total, and the local `bonuses` name is then overwritten by the second call's return value. The `reasons` list that is included in the returned `Signal` only captures hit reasons, never bonus reasons, making it impossible to audit why a signal scored higher than its raw hit score:

```python
# Approximate reproduction of the bug:
bonus_total, bonuses = self._apply_indicator_bonuses(hits, direction)
# ... some computation ...
bonus_total, bonuses = self._apply_indicator_bonuses(hits, direction)  # ← overwrites first bonuses
reasons = [h.reason for h in hits]  # ← bonuses never added to reasons
```

**Fix:** Merge bonus notes into `reasons`:

```python
bonus_total, bonus_notes = self._apply_indicator_bonuses(hits, direction)
reasons = [h.reason for h in hits] + bonus_notes
signal = Signal(..., reasons=reasons)
```

Also remove the duplicate `_apply_indicator_bonuses` call if it exists.

---

### 🟡 M-2 — `COOLDOWN` state is dead code (`risk/circuit_breaker.py`)

**Severity:** Medium — misleading state machine  
**File:** `coinscope_trading_engine/risk/circuit_breaker.py`

`BreakerState.COOLDOWN` is defined in the enum but is **never assigned** anywhere in the module. The state machine transitions directly from `OPEN` to `CLOSED` after `cooldown_minutes`. Any code that checks `state == BreakerState.COOLDOWN` (e.g., dashboard display, external monitoring) will never be `True`.

```python
class BreakerState(str, Enum):
    CLOSED   = "closed"
    OPEN     = "open"
    COOLDOWN = "cooldown"   # ← never set; dead code
```

**Two valid resolutions:**

Option A — Remove `COOLDOWN` from the enum (simplest, keeps current behavior):
```python
class BreakerState(str, Enum):
    CLOSED = "closed"
    OPEN   = "open"
```

Option B — Actually implement the COOLDOWN intermediate state, where the breaker accepts read-only queries but blocks new trades while the cooldown timer runs. This gives operators a visible "warming up" phase:
```python
# In _maybe_auto_reset():
elapsed = (datetime.now(timezone.utc) - self._tripped_at).total_seconds()
if elapsed >= self._cooldown_s * 0.5:
    self._state = BreakerState.COOLDOWN   # halfway through → allow monitoring
if elapsed >= self._cooldown_s:
    self._state = BreakerState.CLOSED
```

---

### 🟡 M-3 — `AlertType` not using `Enum`, `_sequence` counter not thread-safe (`alerts/alert_queue.py`)

**Severity:** Medium — type safety and theoretical concurrency issue  
**File:** `coinscope_trading_engine/alerts/alert_queue.py`

**Problem A:** `AlertType` inherits from `str` but defines class-level string constants instead of using `StrEnum` or `Enum`. This means `isinstance(item.alert_type, AlertType)` always returns `True` for any string, and there is no exhaustive-check guarantee at the `if t == AlertType.SIGNAL` dispatch switch:

```python
# CURRENT — no enum protection
class AlertType(str):
    SIGNAL = "signal"
    STATUS = "status"
    ...

# BETTER — use StrEnum (Python 3.11+) or enum.Enum
from enum import StrEnum

class AlertType(StrEnum):
    SIGNAL          = "signal"
    STATUS          = "status"
    ERROR           = "error"
    CIRCUIT_BREAKER = "circuit_breaker"
    DAILY_SUMMARY   = "daily_summary"
    STARTUP         = "startup"
```

**Problem B:** `_sequence` is incremented via `self._sequence += 1` inside `_next_seq()` without a lock. If `enqueue_signal()` and `enqueue_error()` are called concurrently from different coroutines (which is the intended usage), two items could receive the same sequence number, breaking FIFO ordering within a priority tier.

```python
# CURRENT — not thread-safe
def _next_seq(self) -> int:
    self._sequence += 1
    return self._sequence

# FIX — use itertools.count which is thread-safe in CPython
import itertools
self._sequence = itertools.count(1)

def _next_seq(self) -> int:
    return next(self._sequence)
```

---

## 4. Low Severity / Code Quality

### 🔵 L-1 — `leverage_used` is a heuristic, inconsistent with `margin_usdt` (`risk/position_sizer.py`)

**File:** `coinscope_trading_engine/risk/position_sizer.py`

`leverage_used` is estimated as `max(1, int(notional / max(balance * 0.1, 1)))`, which assumes 10% initial margin — a rough guess that does not match Binance's actual tiered margin requirements. Meanwhile, `margin_usdt` is computed as `notional / max_leverage` (at maximum leverage), not at `leverage_used`. The two fields are therefore internally inconsistent:

```python
# leverage_used uses 10% margin assumption
leverage_used = max(1, int(notional / max(balance * 0.1, 1)))

# margin_usdt uses max_leverage — not the leverage_used above
margin_usdt = notional / max_leverage   # should be notional / leverage_used
```

**Fix:** Either consistently use `max_leverage` for both, or derive `leverage_used` from the actual configured leverage and reconcile `margin_usdt` accordingly:

```python
leverage_used = settings.default_leverage   # use the configured value
margin_usdt   = notional / leverage_used    # consistent
```

---

### 🔵 L-2 — `_classify_absolute` edge case: rate exactly at `threshold` returns WEAK with score `15.0 + 0 = 15.0` (`scanner/funding_rate_scanner.py`)

**File:** `coinscope_trading_engine/scanner/funding_rate_scanner.py`  
**Lines:** 172–179

When `abs_rate == threshold` exactly (the minimum trigger), `_classify_absolute` returns `HitStrength.WEAK` with a score of `15.0 + (0) * 300 = 15.0`. This is correct and expected, but the function has no guard for the case where `abs_rate < threshold` — which should never reach this function (the caller checks the threshold before calling), but a defensive `assert` or early return would make the contract explicit:

```python
def _classify_absolute(self, rate: float) -> tuple[HitStrength, float]:
    abs_rate  = abs(rate)
    threshold = self._threshold
    if abs_rate < threshold:
        # Defensive guard — caller should never reach here
        raise ValueError(f"rate {abs_rate:.6f} is below threshold {threshold:.6f}")
    ...
```

---

## 5. Code Quality Observations (No Action Required)

These observations reflect positively on the codebase and are noted for awareness:

**`scanner/base_scanner.py`** — Excellent. The `BaseScanner` ABC with `_make_result()` / `_make_hit()` builders enforces consistent output structure across all scanner implementations. The `start()/stop()` lifecycle is clean and the background loop uses proper asyncio patterns.

**`alerts/alert_queue.py`** — The priority queue architecture (CRITICAL=0 through LOW=3) with FIFO tie-breaking via sequence number is well-designed. Graceful drain on shutdown with a configurable timeout is production-quality.

**`alerts/telegram_notifier.py` & `alerts/webhook_dispatcher.py`** — Both use `httpx` with proper `async with` context management, retry logic with exponential backoff, and per-endpoint health tracking (webhook dispatcher). The message deduplication TTL cache in `telegram_notifier.py` is a nice touch that prevents alert storms.

**`risk/exposure_tracker.py`** — `asyncio.Lock` on all position mutations is correct. The `_would_exceed_exposure()` guard on `open_position()` is properly inside the lock, preventing TOCTOU issues.

**`risk/correlation_analyzer.py`** — Using numpy for Pearson correlation without a pandas dependency keeps the memory footprint low. The rolling price-history approach is appropriate for real-time use.

**`scanner/volume_scanner.py`** — Cache-first pattern with TTL set to half the candle duration is a solid design choice that balances freshness against Binance API weight.

---

## 6. Recommended Priority Order

| Priority | Action | Effort |
|---|---|---|
| 1 | Deprecate `telegram_alerts.py`, confirm all callers use `TelegramNotifier` | 30 min |
| 2 | Fix import paths in `signal_generator.py` + remove `sys.path` hack | 20 min |
| 3 | Add `refund()` method to `_TokenBucket` and fix `allow_signal()` | 20 min |
| 4 | Add `is_throttled` check in `binance_rest._request()` | 30 min |
| 5 | Fix `bonuses` shadowing in `confluence_scorer.score()` | 15 min |
| 6 | Resolve `COOLDOWN` state (remove or implement) in `circuit_breaker.py` | 20 min |
| 7 | Convert `AlertType` to `StrEnum`, fix `_sequence` counter | 15 min |
| 8 | Align `leverage_used` / `margin_usdt` in `position_sizer.py` | 15 min |

---

*Generated by Scoopy automated daily review — 2026-05-19 09:00 UTC*
