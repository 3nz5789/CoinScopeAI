# CoinScopeAI — Daily Code Review Report
**Date:** 2026-05-15  
**Modules Reviewed:** `scanner/`, `signals/`, `alerts/`, `data/`, `risk/`  
**Reviewer:** Automated (Scoopy Daily Review)

---

## Executive Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical (bugs / runtime errors) | 1 |
| 🟠 High (logic errors / data integrity) | 2 |
| 🟡 Medium (maintainability / inconsistency) | 4 |
| 🟢 Low (style / optimization) | 5 |

The most urgent finding is a **silent coroutine bug** in `signal_generator.py` where an async scanner method is called without `await`, returning a coroutine object instead of actual signal data. This affects live signal generation.

---

## 🔴 CRITICAL: Async Scanner Called Synchronously in `signal_generator.py`

**File:** `signals/signal_generator.py`, around line 101  
**Impact:** `_liquidation_signal()` always returns the wrong data, silently corrupting the weighted vote.

### Problem

`LiquidationScanner.scan()` in `scanner/liquidation_scanner.py` is defined as `async def scan(...)`. However, `signal_generator.py` calls it directly without `await`:

```python
# signals/signal_generator.py (current — BROKEN)
def _liquidation_signal(self, symbol: str) -> float:
    res = self.liq_scan.scan(symbol)   # <-- returns coroutine, not result
    return int(res["signal"])          # <-- TypeError / KeyError at runtime
```

When an `async def` function is called without `await` in a synchronous context, Python returns a **coroutine object** — not the function's return value. Attempting `res["signal"]` on a coroutine object raises a `TypeError`. If this is caught by a broad exception handler upstream, the liquidation component silently contributes `0.0` to the score on every call.

The 10% weight assigned to liquidation signals (`liquidation=0.10`) is effectively dead.

### Fix

**Option A — Await inside an async wrapper (recommended):**
```python
# signals/signal_generator.py
async def _liquidation_signal(self, symbol: str) -> float:
    try:
        res = await self.liq_scan.scan(symbol)
        return float(res.direction.value) if res.hit else 0.0
    except Exception as e:
        logger.warning(f"Liquidation signal failed for {symbol}: {e}")
        return 0.0

# And in generate():
async def generate(self, symbol: str, ...) -> Signal:
    ...
    liq_score = await self._liquidation_signal(symbol)
```

**Option B — Run in executor (if `generate()` must remain sync):**
```python
import asyncio

def _liquidation_signal(self, symbol: str) -> float:
    try:
        loop = asyncio.get_event_loop()
        res = loop.run_until_complete(self.liq_scan.scan(symbol))
        return float(res.direction.value) if res.hit else 0.0
    except Exception as e:
        logger.warning(f"Liquidation signal failed: {e}")
        return 0.0
```

Option A is strongly preferred — the whole signal generation pipeline should be async.

---

## 🟠 HIGH: Duplicate Scanner Packages with Incompatible Interfaces

**Files:** `scanner/` (canonical) vs `scanners/` (legacy)  
**Impact:** Confusion, inconsistent behavior, maintenance burden; old module may be missing production fixes.

Two parallel scanner packages exist:

| | `scanner/` (canonical) | `scanners/` (legacy) |
|---|---|---|
| Base class | `BaseScanner` ABC | None |
| Interface | `async scan() -> ScannerResult` | `scan_dataframe()` / sync |
| `VolumeScanner` | Ratio vs rolling avg + taker imbalance | Z-score (pandas) |
| `LiquidationScanner` | WS buffer + dominance ratio | Threading + deque |
| Used by | `confluence_scorer.py`, `api.py` | `signal_generator.py` |

`signal_generator.py` still imports `VolumeScanner` and `LiquidationScanner` from `scanners/` (old), while `confluence_scorer.py` and `api.py` import from `scanner/` (new). This means:
- The `signal_generator.py` codepath uses stale logic that doesn't benefit from new improvements (Binance 2026-04-10 liquidation change, taker imbalance check, etc.)
- Two different volume spike implementations produce inconsistent signals

**Recommendation:** Migrate `signal_generator.py` to import from `scanner/` (canonical). Once confirmed working, deprecate and remove `scanners/`.

```python
# signals/signal_generator.py — change imports
# OLD:
from scanners.volume_scanner import VolumeScanner
from scanners.liquidation_scanner import LiquidationScanner

# NEW:
from scanner.volume_scanner import VolumeScanner
from scanner.liquidation_scanner import LiquidationScanner
```

After migration, also update `_volume_signal()` and `_liquidation_signal()` to use the `ScannerResult` / `ScannerHit` interface rather than the old dict-based return values.

---

## 🟠 HIGH: `scalp_scanner.py` References a Non-Existent Import Path

**File:** `scanners/scalp_scanner.py`, lines 8–21  
**Impact:** `ScalpScanner` will fail to import in the current project layout, making it dead code.

The file contains:
```python
from app.integrations.binance import get_klines, get_funding_rate, get_orderbook, get_open_interest
```

The current engine module structure has no `app.integrations` package — Binance integration lives in `data/binance_rest.py` and `data/market_stream.py`. This import will raise `ModuleNotFoundError` at runtime.

The file header comments acknowledge this (`# Exchange helpers must come from app.integrations.<provider>`), suggesting this was copied from a different project structure and never adapted.

**Recommendation:** Either:
1. Update the imports to `from data.binance_rest import BinanceRestClient` and refactor accordingly, OR
2. Remove `scalp_scanner.py` from `scanners/` if its logic is superseded by `scanner/pattern_scanner.py` and `scanner/orderbook_scanner.py`

---

## 🟡 MEDIUM: Circular Dependency via Late Import in `liquidation_scanner.py`

**File:** `scanner/liquidation_scanner.py`, `_fetch_liquidations()` method  
**Impact:** Fragile — breaks if the scanner is used outside the `api.py` context.

```python
# scanner/liquidation_scanner.py
def _fetch_liquidations(self, symbol: str, lookback_minutes: int) -> list:
    try:
        import api  # late import to avoid circular at module load
        data = api._get_recent_liquidations(symbol, lookback_minutes)
        ...
    except Exception:
        return []
```

This pattern:
- Hides the dependency from static analysis tools
- Makes the scanner non-functional in test environments or standalone usage
- Accessing a private function (`_get_recent_liquidations`) couples the scanner tightly to `api.py` internals

**Recommendation:** Extract the liquidation buffer into a shared `data/liquidation_buffer.py` singleton that both `api.py` and `liquidation_scanner.py` import:

```python
# data/liquidation_buffer.py
from collections import deque
from threading import Lock

class LiquidationBuffer:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._buffer = {}
            cls._instance._lock = Lock()
        return cls._instance
    
    def push(self, symbol: str, event: dict) -> None:
        with self._lock:
            if symbol not in self._buffer:
                self._buffer[symbol] = deque(maxlen=500)
            self._buffer[symbol].append(event)
    
    def get_recent(self, symbol: str, lookback_minutes: int) -> list:
        ...
```

---

## 🟡 MEDIUM: Two Telegram Senders — Consolidation Incomplete

**Files:** `alerts/telegram_alerts.py` (legacy sync) and `alerts/telegram_notifier.py` (canonical async)  
**Impact:** `alpha_decay_monitor.py` uses the legacy sender, missing deduplication and retry logic.

`telegram_alerts.py` (83 lines, synchronous `requests`):
- No deduplication
- No retry on rate limits
- Markdown parse mode (can fail on special chars)
- 5s hard timeout, exception swallowed

`telegram_notifier.py` (canonical):
- SHA-256 fingerprint deduplication (120s TTL)
- 3-retry exponential backoff
- HTML parse mode (safer)
- 4096-char chunking

`alpha_decay_monitor.py` imports and uses `TelegramAlerts` (legacy). Decay alerts can be duplicated if the monitor fires multiple times before the TTL window.

**Recommendation:** Replace the `TelegramAlerts` usage in `alpha_decay_monitor.py` with `TelegramNotifier`. Then mark `telegram_alerts.py` as deprecated with a `DeprecationWarning` in `__init__`.

---

## 🟡 MEDIUM: Backtester Uses Simplified Signal Logic — Results May Be Misleading

**File:** `signals/backtester.py`  
**Impact:** Backtest win rates / Sharpe ratios don't reflect live scanner-stack behavior.

`BacktestConfig.mtf_filter_enabled = False` by default, and `_generate_signal()` uses a lightweight EMA crossover + RSI + MACD instead of the full `ConfluenceScorer` pipeline. This means:

- Backtests miss scanner contributions (volume spikes, liquidation cascades, funding rate extremes, orderbook walls, pattern detection)
- The 60-point minimum confluence threshold is not enforced in backtests
- `DEFAULT_COMMISSION_PCT = 0.04` — this is Binance maker rate, but taker fills (market orders) are 0.05%; slippage default of 0.01% is optimistic for illiquid pairs

**Recommendation:**
1. Add a `use_full_scanner_stack: bool = False` config option that, when `True`, runs the full `ConfluenceScorer` (requires cached candle data)
2. Update commission default to `0.05` (taker) with a note that makers can use `0.04`
3. Add a slippage model that scales with ATR for illiquid pairs

---

## 🟡 MEDIUM: `position_sizer.py` — Kelly Fraction Applied Without Win Rate Validation

**File:** `risk/position_sizer.py`, `_kelly_fraction()` (lines 192–201)  
**Impact:** Kelly sizing with default/invalid win rate produces nonsensical position sizes.

```python
def _kelly_fraction(self) -> float:
    win_rate = self._win_rate      # defaults to 0.55 if not set
    avg_win = self._avg_win_rr     # defaults to 1.5
    avg_loss = self._avg_loss_rr   # defaults to 1.0
    kelly = win_rate - (1 - win_rate) / (avg_win / avg_loss)
    return min(max(kelly * 0.5, 0.0), MAX_KELLY_FRACTION)
```

If `avg_win / avg_loss = 0` (division by zero if `avg_loss = 0`), or if the stats come from fewer than 20 trades, the Kelly fraction is unreliable. The half-Kelly cap of 25% is a safety net, but the underlying math can produce `0` or near-zero fractions with poor inputs, silently switching to minimal sizing.

**Recommendation:**
```python
def _kelly_fraction(self) -> float:
    MIN_TRADES_FOR_KELLY = 20
    if self._trade_count < MIN_TRADES_FOR_KELLY:
        logger.info(f"Insufficient trades ({self._trade_count}) for Kelly; using fixed-fractional")
        return self._fixed_fraction  # fall back gracefully
    
    if self._avg_loss_rr <= 0 or self._avg_win_rr <= 0:
        logger.warning("Invalid Kelly inputs (zero RR); falling back to fixed-fractional")
        return self._fixed_fraction
    
    kelly = self._win_rate - (1 - self._win_rate) / (self._avg_win_rr / self._avg_loss_rr)
    return min(max(kelly * 0.5, 0.0), MAX_KELLY_FRACTION)
```

---

## 🟢 LOW: `circuit_breaker.py` — Rapid Loss Window Uses Wall Clock, Not Trade Time

**File:** `risk/circuit_breaker.py`  
**Impact:** Minor — rapid loss trigger (`5 losses in 5 minutes`) is correct for live trading but incorrectly triggers during paper trading replays.

The 5-minute rapid loss window uses `datetime.now()`. During paper trading sessions that replay history quickly, multiple simulated losses within seconds can trip the circuit breaker based on wall clock proximity, even if the trades were hours apart in market time.

**Recommendation:** Accept an optional `trade_time: datetime` parameter in the loss recording method and use it when provided.

---

## 🟢 LOW: `rate_limiter.py` — No Persistence Across Process Restarts

**File:** `alerts/rate_limiter.py`  
**Impact:** After a restart, rate limit token buckets reset. An engine restart mid-alert-burst can send more messages than the Telegram bot allows.

**Recommendation:** Persist bucket state to Redis on update and restore on init:
```python
async def _load_from_redis(self) -> None:
    for key in self._buckets:
        saved = await self._cache.get(f"ratelimit:{key}")
        if saved:
            self._buckets[key].tokens = saved["tokens"]
            self._buckets[key].last_refill = saved["last_refill"]
```

---

## 🟢 LOW: `orderbook_scanner.py` — Imbalance Threshold Is Hardcoded

**File:** `scanner/orderbook_scanner.py`  
**Impact:** The 65% bid/ask imbalance threshold cannot be tuned without code changes.

```python
IMBALANCE_THRESHOLD = 0.65  # hardcoded constant
```

**Recommendation:** Move to `config.py` as `orderbook_imbalance_threshold: float = Field(default=0.65, ge=0.5, le=0.95)` and wire it through settings.

---

## 🟢 LOW: `webhook_dispatcher.py` — No Exponential Backoff on Retry

**File:** `alerts/webhook_dispatcher.py`  
**Impact:** On transient endpoint errors, the dispatcher retries immediately, potentially hammering a recovering endpoint.

**Recommendation:** Add jittered exponential backoff on retries:
```python
for attempt in range(MAX_RETRIES):
    try:
        response = await session.post(endpoint.url, ...)
        break
    except aiohttp.ClientError:
        if attempt < MAX_RETRIES - 1:
            await asyncio.sleep(2 ** attempt + random.uniform(0, 1))
```

---

## 🟢 LOW: `cache_manager.py` — TTL Not Set on Some Keys

**File:** `data/cache_manager.py`  
**Impact:** Without TTL, Redis memory grows unboundedly on write-heavy paths.

Spot-check the callers: some `set()` calls pass `ttl=None`. Confirm all keys that accumulate per-symbol data have a maximum TTL set (e.g., `orderbook_snapshot` — if not consumed in 5s it's stale anyway).

**Recommendation:** Add a default TTL guard in `CacheManager.set()`:
```python
async def set(self, key: str, value: Any, ttl: int | None = DEFAULT_TTL) -> None:
    if ttl is None:
        logger.warning(f"Cache set without TTL: {key} — defaulting to {DEFAULT_TTL}s")
        ttl = DEFAULT_TTL
    ...
```

---

## Positive Observations

These are done well and should be preserved:

- **`binance_rest.py` HMAC signing** — insertion-order preservation for query params is correctly documented and implemented. Testnet URLs updated to `demo-fapi.binance.com` (post-April 2026 migration).
- **`alert_queue.py`** — priority queue with 200-item cap and graceful drain on shutdown is production-quality.
- **`telegram_notifier.py`** — SHA-256 deduplication with 120s TTL prevents duplicate alert storms during reconnects.
- **`correlation_analyzer.py`** — rolling Pearson on log-returns (not raw prices) is the correct approach; the 0.80 correlation gate is appropriately conservative.
- **`exposure_tracker.py`** — `asyncio.Lock` on position updates prevents race conditions in concurrent scan loops.
- **`cache_manager.py`** — uses `SCAN` (not `KEYS`) for production-safe key enumeration; pub/sub namespace is clean.
- **`indicator_engine.py`** — pure numpy implementation avoids TA-Lib dependency; all indicators are vectorized correctly.

---

## Action Items (Priority Order)

| Priority | Task | File | Effort |
|----------|------|------|--------|
| P0 | Fix async/sync mismatch in `_liquidation_signal()` | `signals/signal_generator.py` | 30 min |
| P1 | Migrate `signal_generator.py` to use `scanner/` (canonical) | `signals/signal_generator.py` | 2 hrs |
| P1 | Fix or remove `scalp_scanner.py` broken imports | `scanners/scalp_scanner.py` | 1 hr |
| P2 | Replace `TelegramAlerts` with `TelegramNotifier` in `alpha_decay_monitor.py` | `alerts/alpha_decay_monitor.py` | 30 min |
| P2 | Extract liquidation buffer to break circular dependency | `scanner/liquidation_scanner.py` | 2 hrs |
| P2 | Add trade count guard to Kelly fraction | `risk/position_sizer.py` | 30 min |
| P3 | Persist rate limit state to Redis | `alerts/rate_limiter.py` | 1 hr |
| P3 | Move hardcoded thresholds to config | `scanner/orderbook_scanner.py` | 30 min |
| P3 | Add backoff to webhook retries | `alerts/webhook_dispatcher.py` | 30 min |
| P3 | Add default TTL guard in cache manager | `data/cache_manager.py` | 15 min |

---

*Generated by Scoopy automated code review — 2026-05-15 09:00 AM*
