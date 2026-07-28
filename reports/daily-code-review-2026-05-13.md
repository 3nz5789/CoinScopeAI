# CoinScopeAI Daily Code Review — 2026-05-13

**Modules reviewed:** `scanner/`, `scanners/`, `signals/`, `alerts/`, `data/`, `risk/`, `core/`
**Reviewer:** Scoopy (automated daily review, 9:00 AM)

---

## Executive Summary

The codebase is in solid shape overall — the new `scanner/` architecture (v2) is well-structured with clean async patterns, good separation of concerns, and a proper base class. However, there are **three issues that need attention before moving to production candidate**: a dual-pipeline architectural conflict, a thread-safety bug in the rate limiter, and a positional gap between the old and new risk gate implementations. Several lower-priority bugs and performance improvements are also documented below.

---

## 1. Critical / Must Fix

### 1.1 Dual Scanner Architecture — Two Independent Signal Pipelines (Architectural)

**Files:** `signals/signal_generator.py`, `scanners/` (legacy), `scanner/` (v2), `signals/confluence_scorer.py`

`signal_generator.py` imports from the **legacy** `scanners/` directory:
```python
from scanners.volume_scanner import VolumeScanner    # old, sync, DataFrame-based
from scanners.liquidation_scanner import LiquidationScanner  # old, threading-based
```

Meanwhile, all tests (`test_scanners.py`), `tasks.py`, `benchmark.py`, and `confluence_scorer.py` use the **new** `scanner/` v2 architecture:
```python
from scanner.volume_scanner import VolumeScanner    # new, async, BaseScanner subclass
from scanner.liquidation_scanner import LiquidationScanner  # new, async, WS-fed
```

These are two completely separate signal pipelines that never talk to each other. The v1 `SignalGenerator` (used by the old orchestrator path) computes signals independently of the v2 `ConfluenceScorer`. This means:
- A symbol could simultaneously show a LONG from v1 and a SHORT from v2
- The new scoring/bonus/indicator system in `confluence_scorer.py` is bypassed entirely when going through `signal_generator.py`
- `scanners/volume_scanner.py` uses a z-score approach (threshold=2.0) while `scanner/volume_scanner.py` uses a multiplier approach (threshold=3.0) — different signals from the same market data

**Recommendation:** `signal_generator.py` should be refactored to delegate to `ConfluenceScorer` + the v2 `scanner/` modules. The legacy `scanners/` directory should be archived once the migration is confirmed complete.

---

### 1.2 Rate Limiter Thread-Safety Bug — Token Refund Without Lock (`alerts/rate_limiter.py`)

**Location:** `allow_signal()` method, lines that attempt to refund a symbol token

```python
def allow_signal(self, symbol: str) -> bool:
    if not self.allow_symbol(symbol):
        return False
    if not self.allow_telegram():
        # symbol token was already consumed — refund it
        self._get_symbol_bucket(symbol)._tokens = min(   # ← BUG: no lock held
            self._symbol_capacity,
            self._get_symbol_bucket(symbol)._tokens + 1,
        )
        return False
    return True
```

The refund writes directly to `_tokens` without acquiring `_TokenBucket._lock`. Under concurrent access (e.g., multiple symbols being checked simultaneously), this is a data race. The fix:

```python
def allow_signal(self, symbol: str) -> bool:
    if not self.allow_symbol(symbol):
        return False
    if not self.allow_telegram():
        # Refund symbol token via the thread-safe reset path
        bucket = self._get_symbol_bucket(symbol)
        with bucket._lock:
            bucket._tokens = min(bucket.capacity, bucket._tokens + 1.0)
        return False
    return True
```

---

### 1.3 Dual Risk Gate Implementations — `core/risk_gate.py` vs `risk/circuit_breaker.py`

Two separate circuit breaker implementations exist:
- `core/risk_gate.py` — monolithic, synchronous, older style. Daily loss check uses `self.initial_capital` as the reference, not current equity
- `risk/circuit_breaker.py` — clean async, well-decomposed, feature-complete

The daily loss comparison in `core/risk_gate.py` reads:
```python
if self.daily_pnl < -self.initial_capital * self.max_daily_loss_pct:
```

This is semantically wrong after significant account growth — a trader who doubled their capital should be using current equity as the reference, not the starting value. The v2 `circuit_breaker.py` receives `daily_loss_pct` from the caller (which should be computed against current balance), so it's correctly decoupled.

**Recommendation:** Confirm which risk gate is on the hot path for the active orchestrator. Retire `core/risk_gate.py` once the v2 risk module is fully wired in. The PCC v2 thresholds (5% daily loss, 10% max drawdown) are correctly configured in both, but only one should be authoritative.

---

## 2. Bugs / Edge Cases

### 2.1 Stale `_daily_pnl` Field in `ExposureTracker` (`risk/exposure_tracker.py`)

`ExposureTracker` has both `_daily_pnl` (incremented in `close_position`) and `_realised_pnl`, but `daily_pnl` property returns `self._realised_pnl + self.unrealised_pnl` — the `_daily_pnl` field is dead code and never read. `reset_daily_pnl()` also only resets `_realised_pnl`, not `_daily_pnl`. This creates confusion about the source of truth.

```python
# close_position — stale write
self._daily_pnl += pnl    # never read anywhere

# daily_pnl property — correct implementation
return self._realised_pnl + self.unrealised_pnl
```

**Fix:** Remove `_daily_pnl` entirely and rename `reset_daily_pnl()` to also reset `_realised_pnl = 0.0` (which it already does). Just delete the stale field.

---

### 2.2 LiquidationScanner (v2) Uses Fragile Private `api` Import (`scanner/liquidation_scanner.py`)

```python
async def _fetch_liquidations(self, symbol: str) -> list:
    try:
        import api  # late import to avoid circular at module load
        return api._get_recent_liquidations(symbol, self._lookback_minutes)
    except Exception as exc:
        ...
        return []
```

Calling `api._get_recent_liquidations` (a private function) creates a hard coupling to the API module's internal structure. If that function is renamed, moved, or the scanner is run outside the API context (e.g., during backtesting or unit tests), it silently returns empty results without surfacing a clear error. The `_feed_warned` flag suppresses repeated warnings after the first failure, which means subsequent failures in tests are silent.

**Recommendation:** Extract a `LiquidationFeed` abstraction (or use Redis pub/sub via `CacheManager`) that the scanner reads from, rather than importing the API module directly. This would also make the scanner testable in isolation.

---

### 2.3 RSI Seeding Method Inconsistency (`signals/indicator_engine.py`)

The docstring labels the RSI as "Wilder-smoothed RSI" but the initialization uses a simple mean of the first `period` gains/losses:

```python
avg_gain = np.mean(gains[:period])   # Cutler's method (simple SMA seed)
avg_loss = np.mean(losses[:period])
for i in range(period, len(gains)):
    avg_gain = (avg_gain * (period - 1) + gains[i]) / period  # ← Wilder smoothing
```

True Wilder RSI seeds the first average as a simple mean and then uses the EMA multiplier `(period-1)/period` — which is what this code does. So the implementation is actually correct (Wilder's method); the internal variable naming just implies otherwise. However, the `_ema()` function uses `k = 2/(period+1)` (standard EMA), not `1/period` (Wilder EMA). If `_ema()` is ever used on RSI internals, this will produce different results. The separation is currently clean — just needs a comment clarifying the distinction.

---

### 2.4 `sys.path.insert` in Library Code (`signals/signal_generator.py`)

```python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

Modifying `sys.path` in non-entrypoint code is an anti-pattern that can cause import ordering issues, duplicate module loading, and unexpected behavior in testing. The engine should rely on proper package installation (`pyproject.toml` / `PYTHONPATH` in `docker-compose.yml`). Remove this line.

---

### 2.5 `requests` Library Used in Async Context (`alerts/telegram_alerts.py`)

The legacy `TelegramAlerts` class uses the synchronous `requests` library:

```python
import requests
...
requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", ...)
```

This blocks the asyncio event loop for the full HTTP roundtrip (up to 5 seconds at the configured timeout). The new `TelegramNotifier` correctly uses `httpx.AsyncClient`. As long as `TelegramAlerts` is only used in the legacy sync orchestrator path, the immediate risk is contained — but it should be removed or replaced when the v2 path becomes primary.

---

## 3. Performance Issues

### 3.1 `_ema()` Uses Python For-Loop Instead of Vectorized Numpy (`signals/indicator_engine.py`)

```python
def _ema(data: np.ndarray, period: int) -> np.ndarray:
    k   = 2.0 / (period + 1)
    out = np.zeros(len(data))
    out[0] = data[0]
    for i in range(1, len(data)):         # ← O(N) Python loop
        out[i] = data[i] * k + out[i - 1] * (1 - k)
    return out
```

For 200 candles this is negligible, but `_ema` is called 7 times per `compute()` call (EMA-9, 21, 50, 200, MACD×2 + signal, ADX wilder×3). For high-frequency scans over 50 symbols × 5 timeframes, this adds up. A vectorized alternative using `scipy.signal.lfilter` or `pandas.ewm` would be ~10× faster. Alternatively, using `numba.njit` on the hot path would eliminate Python overhead without changing the algorithm.

Quick vectorized drop-in (no deps beyond numpy):
```python
def _ema(data: np.ndarray, period: int) -> np.ndarray:
    alpha = 2.0 / (period + 1)
    out = np.empty_like(data, dtype=float)
    out[0] = data[0]
    # scipy.signal.lfilter([alpha], [1, alpha - 1], data[1:], zi=[(1-alpha)*data[0]])
    # — or keep the loop, just jit-compile it
    for i in range(1, len(data)):
        out[i] = alpha * data[i] + (1 - alpha) * out[i - 1]
    return out
```

(The loop itself is the same — profile first to confirm it's actually the bottleneck before rewriting.)

---

### 3.2 N² Calls to `np.corrcoef` in `CorrelationAnalyzer` (`risk/correlation_analyzer.py`)

`correlation_matrix()` calls `self.pearson(sym_a, sym_b)` for each pair, and each call to `pearson()` calls `np.corrcoef()` which allocates a new 2×2 matrix. For 20 symbols this is 190 corrcoef calls per cycle.

**Fix:** Build the full return matrix once and compute the full correlation matrix in a single `np.corrcoef(returns_matrix)` call:

```python
def correlation_matrix(self) -> dict[str, dict[str, float]]:
    symbols = [s for s in self._prices if len(self._prices[s]) >= 5]
    if len(symbols) < 2:
        return {}
    returns = np.array([_log_returns(self._prices[s]) for s in symbols])
    # Trim to shortest
    min_len = min(r.shape[0] for r in returns)
    matrix = np.corrcoef(np.vstack([r[-min_len:] for r in returns]))
    ...
```

This reduces N² numpy calls to a single vectorized operation.

---

### 3.3 `PatternScanner` Cross-Module Import Dependency for Serialisation (`scanner/pattern_scanner.py`)

```python
# In pattern_scanner.py:
from scanner.volume_scanner import _dict_to_candle, _candle_to_dict
```

`PatternScanner` borrows private serialization helpers from `VolumeScanner`. This creates an implicit coupling — if `VolumeScanner`'s internal dict format changes, `PatternScanner` silently breaks. The candle serialization helpers should be moved to `data/data_normalizer.py` or a shared `scanner/utils.py` and imported from there by both scanners.

---

## 4. Best Practice Violations

### 4.1 Order Book TTL Is Dangerously Short (`scanner/orderbook_scanner.py`)

```python
await self.cache.set(cache_key, _book_to_dict(book), ttl=2)  # 2 seconds
```

A 2-second TTL on order book data is correct for production (books change rapidly), but when the scanner loop runs on all symbols with a short `scan_interval_seconds`, it means the cache is rarely hit. Every scan cycle incurs a full REST call to `/fapi/v1/depth`. At 50 symbols × 2-second TTL, the REST weight cost is `50 × 2 = 100 weight/minute` just for order books. Combined with klines and mark price calls, this approaches the Binance weight limit faster than expected.

**Recommendation:** Switch to WebSocket-fed order book updates (store in Redis on ingest) and let the scanner read from cache with a longer TTL fallback (e.g., 10s). This also improves data freshness since WS is push-based.

---

### 4.2 Duplicate `telegram_alerts.py` / `telegram_notifier.py` — Two Alert Systems

| File | Style | Library | Features |
|------|-------|---------|----------|
| `alerts/telegram_alerts.py` | Sync | `requests` | Basic, no dedup, no chunking, no retry |
| `alerts/telegram_notifier.py` | Async | `httpx` | Full featured, dedup, chunking, retry |

Both are active in the repo. The legacy one has no rate limiting integration with `rate_limiter.py`. Any code path that reaches `TelegramAlerts` bypasses the `AlertRateLimiter`. Consolidate on `TelegramNotifier` and remove the legacy file.

---

### 4.3 Missing Symbol Input Validation Across Scanner Classes

None of the scanner `scan()` implementations validate the `symbol` parameter before passing it to REST calls. An empty string, `None`, or malformed symbol (e.g., `"btcusdt"` instead of `"BTCUSDT"`) would propagate directly to the API and return a Binance error that gets logged as a generic exception. Consider a shared validator in `BaseScanner`:

```python
# In base_scanner.py
async def scan(self, symbol: str) -> ScannerResult:
    if not symbol or not isinstance(symbol, str):
        return ScannerResult(scanner=self.name, symbol=str(symbol),
                             error="Invalid symbol")
    symbol = symbol.upper().strip()
    ...
```

---

### 4.4 `confluence_scorer.py` — Neutral Hits Are Silently Discarded

`PatternScanner` can emit `SignalDirection.NEUTRAL` hits (e.g., Doji patterns). In `ConfluenceScorer.score()`:

```python
for hit in result.hits:
    if hit.direction == SignalDirection.LONG:
        long_hits.append(hit)
    elif hit.direction == SignalDirection.SHORT:
        short_hits.append(hit)
    # NEUTRAL hits are silently dropped here
```

Neutral hits (indecision candles, wide spreads from `OrderBookScanner`) carry useful information — they should either reduce the final confidence score or be surfaced separately. At minimum, log a debug note when neutral hits are dropped.

---

## 5. Optimization Opportunities

### 5.1 `FundingRateScanner` — History Fetched Even When Absolute Check Already Strong

The relative extreme and reversal checks (steps 2 and 3) are only useful when the absolute check (step 1) didn't fire at the STRONG level. Currently, the full history is always fetched regardless. A minor optimization for high-frequency scans:

```python
# After absolute check fires at STRONG strength, skip history fetch
if hits and hits[0].strength == HitStrength.STRONG:
    return self._make_result(symbol, hits, ...)
history = await self._fetch_funding_history(symbol)
```

This saves one cache/REST lookup per strong signal cycle.

---

### 5.2 `BaseScanner._loop` — No Backpressure on Slow Symbols

The loop iterates symbols sequentially:
```python
for symbol in symbols:
    result = await self.scan(symbol)
```

If one symbol's API call is slow (e.g., Binance returns slowly for a low-liquidity pair), it delays all subsequent symbols in that cycle. Consider running scans concurrently with `asyncio.gather()` and a semaphore for rate-limit safety:

```python
semaphore = asyncio.Semaphore(5)  # max 5 concurrent REST calls

async def scan_with_limit(symbol):
    async with semaphore:
        return await self.scan(symbol)

results = await asyncio.gather(*[scan_with_limit(s) for s in symbols],
                                return_exceptions=True)
```

---

## 6. Security Notes

- **`binance_rest.py` HMAC signing** is correctly implemented (no param sorting, preserving insertion order per Binance spec). The comment explaining this is clear — good defensive documentation.
- **`TelegramNotifier` dedup fingerprinting** uses SHA-256 truncated to 24 hex chars on the first 300 characters. Collision probability is negligible for this use case.
- **`core/key_vault.py`** (not reviewed in depth today) — ensure API keys are never logged even at DEBUG level. The `_safe_url` helper in `cache_manager.py` is a good pattern to replicate for any string that may contain credentials.
- **No input sanitization** on `signal.reasons` passed to Telegram HTML formatter — `_esc()` is correctly applied in `TelegramNotifier._format_signal()` but not in the legacy `TelegramAlerts.send_signal()`.

---

## Priority Summary

| Priority | Issue | File | Effort |
|---|---|---|---|
| 🔴 P1 | Dual scanner pipeline — two independent signal paths | `signals/signal_generator.py` | Medium |
| 🔴 P1 | Rate limiter token refund without lock | `alerts/rate_limiter.py` | Small |
| 🔴 P1 | Two risk gate implementations, wrong reference in old one | `core/risk_gate.py` | Medium |
| 🟡 P2 | Stale `_daily_pnl` field | `risk/exposure_tracker.py` | Trivial |
| 🟡 P2 | Fragile `import api` in LiquidationScanner | `scanner/liquidation_scanner.py` | Medium |
| 🟡 P2 | `sys.path.insert` in library code | `signals/signal_generator.py` | Trivial |
| 🟡 P2 | Blocking `requests` in async context | `alerts/telegram_alerts.py` | Small |
| 🟢 P3 | EMA loop not vectorized | `signals/indicator_engine.py` | Small |
| 🟢 P3 | N² correlation matrix computation | `risk/correlation_analyzer.py` | Small |
| 🟢 P3 | Candle serialiser cross-module import | `scanner/pattern_scanner.py` | Trivial |
| 🟢 P3 | Order book REST per-scan vs WS-fed | `scanner/orderbook_scanner.py` | Large |
| 🟢 P3 | Neutral hits silently discarded | `signals/confluence_scorer.py` | Trivial |
| 🟢 P3 | Symbol input validation missing | All scanners | Small |
| 🟢 P3 | Duplicate Telegram implementations | `alerts/` | Small |

---

*Generated by Scoopy daily code review (scheduled task). Next review: 2026-05-14 09:00.*
