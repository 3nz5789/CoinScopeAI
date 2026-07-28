# CoinScopeAI Daily Code Review — 2026-05-17

**Automated review generated at 09:00 AM**
**Modules reviewed:** `scanner/`, `signals/`, `alerts/`, `data/`, `risk/`
**Reviewer:** Scoopy (automated scheduled review)

---

## Executive Summary

This review covers the full current state of the CoinScopeAI trading engine codebase (no git history was available; a complete module-by-module audit was performed). **7 bugs were found** — 2 critical, 3 significant, 2 minor. Additionally, several performance concerns, best-practice violations, and improvement opportunities are documented below.

**Severity legend:** 🔴 Critical | 🟠 Significant | 🟡 Minor | 🔵 Info / Improvement

---

## 1. Critical Bugs

### 🔴 BUG-001 — `signal_generator.py`: Broken import path (`scanners.` vs `scanner.`)

**File:** `coinscope_trading_engine/signals/signal_generator.py`
**Risk:** Runtime `ImportError` — `SignalGenerator` fails to instantiate, halting all signal production.

The module imports from `scanners.` (plural), but the actual package directory is named `scanner.` (singular):

```python
# CURRENT (broken):
from scanners.scanner_registry import ScannerRegistry
from scanners.base_scanner import ScannerHit

# CORRECT:
from scanner.scanner_registry import ScannerRegistry
from scanner.base_scanner import ScannerHit
```

Additionally, `sys.path.insert(0, ...)` is used at module level to work around this. This is an anti-pattern that pollutes the interpreter path for the entire process lifetime. The correct fix is to resolve the package naming inconsistency and use proper relative imports or a clean `PYTHONPATH`.

**Fix:**
1. Rename the import paths to match the actual directory name.
2. Remove `sys.path.insert` — configure `PYTHONPATH` in deployment environment or use `pyproject.toml`/`setup.cfg` package entry points.

---

### 🔴 BUG-002 — `rate_limiter.py`: Race condition on token refund in `allow_signal()`

**File:** `coinscope_trading_engine/alerts/rate_limiter.py`
**Risk:** Token bucket corruption under concurrent coroutines — a symbol could burn its entire token budget in a burst or return more tokens than it started with.

```python
def allow_signal(self, symbol: str) -> bool:
    if not self.allow_symbol(symbol):
        return False
    if not self.allow_telegram():
        # BUG: Reads and writes _tokens without holding the lock
        bucket = self._get_symbol_bucket(symbol)
        bucket._tokens = min(
            self._symbol_capacity,
            bucket._tokens + 1,      # read
        )                             # write — not atomic, not locked
        return False
    return True
```

`allow_symbol()` drains a token from the bucket under `threading.Lock`. If `allow_telegram()` then returns `False`, the code refunds the token — but does so outside the lock. A concurrent call can interleave between the read and write, causing the refund to be lost or doubled.

**Fix:**

```python
def allow_signal(self, symbol: str) -> bool:
    with self._lock:
        if not self._allow_symbol_locked(symbol):
            return False
        if not self._allow_telegram_locked():
            # Refund symbol token — still inside the lock
            bucket = self._get_symbol_bucket(symbol)
            bucket._tokens = min(self._symbol_capacity, bucket._tokens + 1)
            return False
    return True
```

Refactor `allow_symbol()` and `allow_telegram()` to expose locked variants callable from within the same critical section.

---

## 2. Significant Bugs

### 🟠 BUG-003 — `exposure_tracker.py`: `_trade_count` never resets on daily rollover

**File:** `coinscope_trading_engine/risk/exposure_tracker.py`
**Risk:** Trade count accumulates across days, making any metrics or limits based on daily trade count incorrect after Day 1.

```python
def reset_daily_pnl(self) -> None:
    """Call at start of each trading day."""
    self._realised_pnl = 0.0
    # BUG: _trade_count is NOT reset here — accumulates forever
    logger.info("Daily PnL reset. trade_count=%d", self._trade_count)
```

The log line even prints `trade_count`, implying it should represent *today's* trades — but it never resets.

**Fix:**

```python
def reset_daily_pnl(self) -> None:
    """Call at start of each trading day."""
    self._realised_pnl = 0.0
    self._trade_count = 0           # ADD THIS LINE
    logger.info("Daily PnL reset.")
```

---

### 🟠 BUG-004 — `risk_gate.py`: `circuit_breaker_active` and `daily_pnl` never auto-reset

**File:** `coinscope_trading_engine/core/risk_gate.py`
**Risk:** The circuit breaker, once tripped, stays permanently open unless the process restarts. Daily P&L drawdown tracking is never zeroed, so the daily loss limit is effectively a lifetime loss limit.

From prior review:
- `circuit_breaker_active` is set to `True` on breach but has no reset path in the state machine.
- `daily_pnl` is an accumulated float with no scheduled reset logic wired in.

**Fix:**
1. Wire `reset_daily_pnl()` from `exposure_tracker.py` to a daily scheduler (midnight UTC reset).
2. Add a `reset_circuit_breaker()` method and call it at session open or after the cooldown window:
```python
def reset_circuit_breaker(self) -> None:
    self.circuit_breaker_active = False
    logger.info("Circuit breaker reset at session open.")
```

---

### 🟠 BUG-005 — `circuit_breaker.py`: COOLDOWN state is dead code

**File:** `coinscope_trading_engine/risk/circuit_breaker.py`
**Risk:** The intended three-state machine (CLOSED → OPEN → COOLDOWN → CLOSED) is architecturally broken. COOLDOWN is defined in the enum but never entered — OPEN transitions directly to CLOSED. This means there is no cooldown period: a breaker that trips immediately re-arms, defeating its own protection.

```python
class CircuitState(Enum):
    CLOSED   = "closed"
    OPEN     = "open"
    COOLDOWN = "cooldown"   # defined but never reached

# State machine only handles CLOSED → OPEN → CLOSED
# COOLDOWN is never set anywhere in the codebase
```

Additionally, `reset_daily()` resets `_consecutive_losses = 0` but does NOT reset `_state` — a breaker that is OPEN at midnight stays OPEN the next trading day.

**Fix:**

```python
def _transition_to_cooldown(self) -> None:
    self._state = CircuitState.COOLDOWN
    self._cooldown_until = time.monotonic() + self._cooldown_seconds
    logger.warning("Circuit breaker entering COOLDOWN for %ds", self._cooldown_seconds)

def check(self) -> bool:
    if self._state == CircuitState.COOLDOWN:
        if time.monotonic() >= self._cooldown_until:
            self._state = CircuitState.CLOSED
            self._consecutive_losses = 0
        else:
            return False   # Still in cooldown
    # ... rest of check logic ...
```

---

## 3. Minor Bugs

### 🟡 BUG-006 — `exposure_tracker.py`: `Position.unrealised_pnl` fails if `mark_price == 0.0`

**File:** `coinscope_trading_engine/risk/exposure_tracker.py`

```python
@property
def unrealised_pnl(self) -> float:
    if not self.mark_price:   # BUG: True when mark_price is 0.0 (falsy float)
        return 0.0
    return (self.mark_price - self.entry_price) * self.qty * self.direction
```

`if not self.mark_price` is `True` when `mark_price` is `0.0`. A mark price of exactly zero is theoretically possible during extreme market events or data gaps, and would silently return 0.0 unrealised P&L instead of calculating it.

**Fix:**

```python
if self.mark_price is None:
    return 0.0
```

---

### 🟡 BUG-007 — `confluence_scorer.py`: Scanner `reasons` overwritten by bonus reasons

**File:** `coinscope_trading_engine/signals/confluence_scorer.py`

When the scorer assembles a `Signal` object, it replaces the original scanner `reasons` list with the bonus `reasons` list:

```python
signal.reasons = bonus_reasons   # Overwrites scanner hit reasons
```

This means the final signal carries only the indicator-bonus reasons, not the scanner triggers that generated the hit. Debugging and alert message context are degraded.

**Fix:**

```python
signal.reasons = signal.reasons + bonus_reasons   # Append, don't replace
```

---

## 4. Performance & Scalability Concerns

### Unbounded Memory Growth

Several data structures grow without eviction:

| Location | Structure | Growth trigger |
|---|---|---|
| `scanner/base_scanner.py` | `_results: Dict[str, ScannerHit]` | One entry per symbol, never pruned |
| `alerts/rate_limiter.py` | `_symbol_buckets: Dict[str, TokenBucket]` | One entry per unique symbol seen, never evicted |
| `core/risk_gate.py` | `trades_history: List[Trade]` | Appended on every trade, never trimmed |
| `alerts/telegram_notifier.py` | `_seen: Dict[str, float]` (dedup cache) | Eviction is O(N) scan on every `_is_duplicate()` call |

**Recommended fixes:**
- `trades_history`: Use `collections.deque(maxlen=1000)` instead of a plain list.
- `_symbol_buckets`: Add TTL-based eviction or a `maxsize` LRU wrapper.
- Dedup cache: Replace with `cachetools.TTLCache` or a Redis-backed set (already have Redis in the stack).

### Redis `keys()` Exposed as Public API

**File:** `coinscope_trading_engine/data/cache_manager.py`

The `keys(pattern)` method calls `await self._redis.keys(pattern)` directly. On a large keyspace this is O(N) and blocks the Redis event loop for all other clients. This is a well-known Redis footgun.

**Fix:** Replace with `SCAN` cursor iteration:

```python
async def keys(self, pattern: str) -> List[str]:
    results = []
    cursor = 0
    while True:
        cursor, batch = await self._redis.scan(cursor, match=pattern, count=100)
        results.extend(batch)
        if cursor == 0:
            break
    return results
```

---

## 5. Best Practice Violations

### Deprecated `datetime.utcnow()` in `telegram_alerts.py`

**File:** `coinscope_trading_engine/alerts/telegram_alerts.py`

```python
# DEPRECATED (Python 3.12+):
timestamp = datetime.utcnow().strftime(...)

# CORRECT:
timestamp = datetime.now(timezone.utc).strftime(...)
```

### Blocking HTTP in Async Context (`telegram_alerts.py`)

The old `telegram_alerts.py` uses synchronous `requests.post()` inside coroutines. This blocks the entire event loop during the HTTP call. The new `telegram_notifier.py` correctly uses `httpx.AsyncClient`. **The old file should be fully removed** to prevent accidental re-import.

**Action:** Delete or archive `alerts/telegram_alerts.py`. Ensure all imports reference `telegram_notifier.py`.

### EMA Seed Bias on Short Series

**File:** `coinscope_trading_engine/signals/indicator_engine.py`

```python
def _ema(data: np.ndarray, period: int) -> np.ndarray:
    out[0] = data[0]   # Seeds with first value, not a warmup SMA
```

For the first `period` candles, this systematically biases the EMA toward the first data point. On short series (< 2× period) this materially affects signal quality.

**Fix:** Seed with the SMA of the first `period` values:

```python
def _ema(data: np.ndarray, period: int) -> np.ndarray:
    k = 2.0 / (period + 1)
    out = np.zeros(len(data))
    if len(data) >= period:
        out[period - 1] = np.mean(data[:period])   # Proper SMA seed
        start = period
    else:
        out[0] = data[0]   # Fallback for very short series
        start = 1
    for i in range(start, len(data)):
        out[i] = data[i] * k + out[i - 1] * (1 - k)
    return out
```

### VWAP is Not Session-Anchored

**File:** `coinscope_trading_engine/signals/indicator_engine.py`

VWAP is computed over all candles passed in, not anchored to the trading session open. This means it drifts with lookback window rather than resetting at session boundaries.

**Fix:** Accept a `session_open_ts` parameter and slice the input arrays to the current session before computing VWAP. For perpetual futures with no daily session open, use a rolling 24-hour anchor.

### HMM Regime Model Fitted Once and Never Re-Fitted

**File:** `coinscope_trading_engine/signals/signal_generator.py`

```python
# Fitted once at first call per symbol:
self._regime_models[symbol] = EnsembleRegimeDetector()
self._regime_models[symbol].fit(features)
# Never re-fitted → model goes stale as market regime evolves
```

As market conditions change, a model fitted hours or days ago will produce increasingly incorrect regime labels. Over a trending session this could suppress all signals in the wrong direction.

**Fix:** Re-fit the model periodically (e.g., every 4 hours or 500 candles):

```python
should_refit = (
    symbol not in self._regime_models or
    self._regime_last_fit.get(symbol, 0) < time.time() - 4 * 3600
)
if should_refit:
    self._regime_models[symbol] = EnsembleRegimeDetector()
    self._regime_models[symbol].fit(features)
    self._regime_last_fit[symbol] = time.time()
```

### Scoring Weight Imbalance in Chop Regime

**File:** `coinscope_trading_engine/signals/signal_generator.py`

When `regime_weight` is set to `0.0` in a choppy market, the maximum achievable signal score drops from 1.0 to 0.75 (regime's 0.25 weight is zeroed but not redistributed). The `SIGNAL_THRESHOLD` remains unchanged, making it effectively 33% harder to generate a signal in chop — which may be intended but is not documented.

**Recommendation:** Either document this as intentional suppression, or redistribute the weight:

```python
active_weights = {k: v for k, v in WEIGHTS.items() if component_scores[k] is not None}
total = sum(active_weights.values())
normalised = {k: v / total for k, v in active_weights.items()}
```

---

## 6. Security Notes

### Binance Testnet URL Points to Mainnet

**File:** `coinscope_trading_engine/data/binance_websocket.py`

```python
WS_TESTNET_URL = "wss://stream.binance.com:9443"  # WARNING: This is mainnet
# Binance demo/testnet doesn't support signed WebSocket streams as of 2026-04
```

Any code path that sets `use_testnet=True` expecting sandbox behavior will silently connect to mainnet. This is a live capital risk.

**Fix:** Raise a `NotImplementedError` or `ConfigurationError` if `use_testnet=True` is requested until testnet support is available:

```python
if use_testnet:
    raise NotImplementedError(
        "Binance signed WebSocket testnet is not supported as of 2026-04. "
        "Set use_testnet=False to use mainnet, or omit the testnet flag."
    )
```

### Token Bucket Lock Is `threading.Lock`, Not `asyncio.Lock`

**File:** `coinscope_trading_engine/alerts/rate_limiter.py`

Using `threading.Lock` in an asyncio application works but can cause priority inversion if the lock is ever held during I/O. The lock should be `asyncio.Lock` and the call sites should use `async with self._lock`. Given that `allow_signal()` is called from async coroutines, this is worth addressing proactively.

---

## 7. Summary Table

| ID | File | Severity | Category | Status |
|---|---|---|---|---|
| BUG-001 | `signals/signal_generator.py` | 🔴 Critical | Import error | Open |
| BUG-002 | `alerts/rate_limiter.py` | 🔴 Critical | Race condition | Open |
| BUG-003 | `risk/exposure_tracker.py` | 🟠 Significant | Logic error | Open |
| BUG-004 | `core/risk_gate.py` | 🟠 Significant | State management | Open |
| BUG-005 | `risk/circuit_breaker.py` | 🟠 Significant | Dead code / logic | Open |
| BUG-006 | `risk/exposure_tracker.py` | 🟡 Minor | Falsy-float check | Open |
| BUG-007 | `signals/confluence_scorer.py` | 🟡 Minor | Data integrity | Open |
| PERF-001 | Multiple | 🟠 Significant | Unbounded memory | Open |
| PERF-002 | `data/cache_manager.py` | 🟠 Significant | Redis O(N) keys() | Open |
| STYLE-001 | `alerts/telegram_alerts.py` | 🟡 Minor | Deprecated API | Open |
| STYLE-002 | `alerts/telegram_alerts.py` | 🟠 Significant | Blocking I/O in async | Open |
| STYLE-003 | `signals/indicator_engine.py` | 🟡 Minor | EMA seed bias | Open |
| STYLE-004 | `signals/indicator_engine.py` | 🟡 Minor | VWAP not anchored | Open |
| STYLE-005 | `signals/signal_generator.py` | 🟠 Significant | Stale regime model | Open |
| SEC-001 | `data/binance_websocket.py` | 🔴 Critical | Testnet→Mainnet URL | Open |

---

## 8. Recommended Priority Order

1. **BUG-001** — Fix `scanners.` import → `scanner.` or the engine won't start.
2. **SEC-001** — Guard testnet path to prevent accidental mainnet trading.
3. **BUG-002** — Fix race condition in rate limiter refund path before high-volume trading.
4. **STYLE-002** — Remove or archive `telegram_alerts.py`; confirm all callers use `telegram_notifier.py`.
5. **BUG-004 + BUG-005** — Wire daily resets and fix circuit breaker state machine.
6. **BUG-003** — Fix `_trade_count` reset in daily rollover.
7. **PERF-001 + PERF-002** — Add memory bounds and replace Redis `keys()` with `scan`.
8. Remaining minor/style issues can be addressed in a maintenance sprint.

---

*Review completed: 2026-05-17. Next scheduled review: 2026-05-18 09:00 AM.*
