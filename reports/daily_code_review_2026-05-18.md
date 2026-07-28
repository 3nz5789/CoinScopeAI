# CoinScopeAI Daily Code Review — 2026-05-18

**Reviewer:** Automated (Scoopy / Claude)
**Scope:** `scanner/`, `signals/`, `alerts/`, `data/`, `risk/` modules
**Previous reviews:** `code-review-2026-05-14.md`, `code-review-2026-05-16.md`, `daily_code_review_2026-05-17.md`

---

## Executive Summary

This review covers 20 files across 5 modules. **6 high-severity bugs** were identified that can cause silent data corruption, race conditions, or production crashes. **4 medium-severity architectural issues** affect reliability and scalability. **12 low-severity issues** affect maintainability and correctness at the margins. The most critical issues are the WebSocket double-reconnect race condition, the backtester's uncapped position sizing, the exposure tracker's unlocked property reads, and the systemic `or`-pattern bug that silently ignores zero-valued configuration.

---

## Systemic Issue: `or`-Pattern Configuration Bug

**Severity: HIGH | Files affected: 7+**

A pattern of the form `self._x = param or settings.x` is used throughout the codebase to provide settings fallback. This silently treats `0`, `0.0`, and `""` as absent, meaning any intentional zero-value override falls through to the default.

```python
# Pattern in volume_scanner.py, position_sizer.py, entry_exit_calculator.py,
# cache_manager.py, rate_limiter.py, signal_generator.py, backtester.py:
self._spike_multiplier = spike_multiplier or settings.volume_spike_multiplier
self._risk_per_trade = risk_per_trade_pct or settings.risk_per_trade_pct
self._min_rr = min_rr or settings.min_risk_reward_ratio
self._default_ttl = default_ttl or settings.redis_cache_ttl_seconds
```

**Fix — use `None` sentinel consistently:**
```python
self._spike_multiplier = spike_multiplier if spike_multiplier is not None else settings.volume_spike_multiplier
self._default_ttl = default_ttl if default_ttl is not None else settings.redis_cache_ttl_seconds
```

---

## Module: `scanner/`

### `base_scanner.py`

#### [BUG-HIGH] `_results` dict grows unbounded — memory leak
`self._results: dict[str, ScannerResult] = {}` accumulates one entry per scanned symbol and is never evicted. With 200+ USDT-M perpetuals scanning continuously, this leaks indefinitely.

```python
# Current
self._results[symbol] = result  # never removed

# Fix
MAX_RESULT_CACHE = 500
if len(self._results) >= MAX_RESULT_CACHE:
    oldest = next(iter(self._results))
    del self._results[oldest]
self._results[symbol] = result
```

#### [ISSUE-LOW] No exponential backoff on per-symbol errors
Repeated errors for a broken symbol hit the same retry path at full speed. Add per-symbol error counters with exponential backoff (cap at ~5 min) before disabling the symbol.

---

### `liquidation_scanner.py`

#### [BUG-MEDIUM] `_feed_warned` set dynamically — AttributeError risk
`self._feed_warned` is assigned inside a method (`if not hasattr(self, '_feed_warned')`) rather than declared in `__init__`. If the attribute is accessed before the first warning, code breaks. Initialize in `__init__`:

```python
def __init__(self, ...):
    self._feed_warned: set[str] = set()
```

#### [ISSUE-LOW] Late `import api` inside method
`from coinscope_trading_engine import api` is imported inside a method to avoid circular imports. This is fragile — restructure to use a lazy-loaded module reference or dependency injection.

---

### `pattern_scanner.py`

#### [ISSUE-MEDIUM] Cross-module coupling with `volume_scanner`
`pattern_scanner.py` imports serialization helpers from `volume_scanner`. These utilities should live in a shared `scanner/utils.py` module. This creates an implicit dependency between two sibling modules.

#### [ISSUE-LOW] Pin Bar double-fires with Hammer / Shooting Star
On certain candles, both the Pin Bar detector and the Hammer/Shooting Star detector can emit signals for the same candle. Add deduplication by (symbol, timestamp, pattern_type) at the base scanner level.

---

### `volume_scanner.py`

#### [BUG-HIGH] `or`-pattern treats `spike_multiplier=0.0` as absent
See systemic issue section above. A caller trying to disable spike detection with `spike_multiplier=0.0` gets the settings default instead.

---

## Module: `signals/`

### `indicator_engine.py`

#### [BUG-HIGH] Truthy check on EMA values — silent failures at price=0.0
`_trend_label` uses `if ind.ema_9 and ind.ema_21:` — if either EMA resolves to exactly 0.0 (degenerate series, test data), the condition is False and the trend label silently falls to the default. Use explicit `is not None`:

```python
# Current
if ind.ema_9 and ind.ema_21:

# Fix
if ind.ema_9 is not None and ind.ema_21 is not None:
```

#### [BUG-MEDIUM] EMA warm-up bias — `out[0] = data[0]` seeds incorrectly
The EMA initializer sets `out[0] = data[0]` with no warm-up period. For short candle series, this biases the EMA toward the first data point. Standard practice seeds from the SMA of the first `period` bars:

```python
def _ema(data: np.ndarray, period: int) -> np.ndarray:
    out = np.full(len(data), np.nan)
    if len(data) < period:
        return out
    k = 2.0 / (period + 1)
    out[period - 1] = data[:period].mean()  # SMA seed
    for i in range(period, len(data)):
        out[i] = data[i] * k + out[i - 1] * (1 - k)
    return out
```

#### [BUG-MEDIUM] RSI seeding not true Wilder method
`_rsi()` initializes `avg_gain`/`avg_loss` incorrectly. True Wilder RSI seeds with the SMA of the first `period` gains/losses, then applies Wilder smoothing. The current implementation introduces a bias in the first ~14 bars.

#### [BUG-LOW] `_stochastic` slice artifact from zero-filled array
The stochastic calculation allocates a zero-filled array, then computes from index `period-1` onward. Values before the slice index are left as 0.0 rather than `np.nan`, making them indistinguishable from a valid 0% stochastic reading.

#### [BUG-MEDIUM] ADX `_wilder()` off-by-one — skips index 0
```python
out[p] = np.sum(arr[1: p + 1])  # Bug: starts from index 1, skips arr[0]
# Fix:
out[p] = np.sum(arr[0: p + 1])  # or arr[:p+1]
```

#### [ISSUE-MEDIUM] VWAP never session-reset
VWAP accumulates across all candles in the input list rather than resetting at each session open. This makes VWAP meaningless for any candle list spanning multiple trading days. Add a session-boundary reset based on the candle timestamp (midnight UTC for crypto).

#### [ISSUE-LOW] `macd_bullish_cross` is not a crossover check
`macd_bullish_cross = macd_hist > 0` detects "histogram positive" — it is `True` for the entire bullish phase, not just the bar the histogram crosses zero. Rename to `macd_hist_positive` or implement a real crossover:
```python
macd_bullish_cross = (macd_hist[-1] > 0) and (macd_hist[-2] <= 0)
```

---

### `signal_generator.py`

#### [BUG-HIGH] Suppressed `regime_weight` not reflected in `max_possible`
When regime is "chop" with confidence > 0.55, `regime_weight` is set to 0.0 but `max_possible` stays at `sum(WEIGHTS.values()) = 1.0`. The normalized score is artificially deflated by ~25% for every signal in a choppy regime.

```python
# Current
regime_weight = 0.0 if regime == "chop" and conf > 0.55 else WEIGHTS["regime"]
max_possible = sum(WEIGHTS.values())  # always 1.0 — WRONG

# Fix
weights_used = dict(WEIGHTS)
if regime == "chop" and conf > 0.55:
    weights_used["regime"] = 0.0
max_possible = sum(weights_used.values())  # correctly reflects active weights
```

#### [BUG-MEDIUM] `_regime_fit` dict grows unbounded — memory leak
`self._regime_fit: dict[str, Any] = {}` stores fitted regime model data per symbol and is never evicted. Add an LRU cache or TTL-based eviction:

```python
from functools import lru_cache
# or cap at MAX_SYMBOLS entries with oldest-first eviction
MAX_FIT_CACHE = 300
if len(self._regime_fit) >= MAX_FIT_CACHE:
    oldest = next(iter(self._regime_fit))
    del self._regime_fit[oldest]
```

#### [ISSUE-MEDIUM] `_regime_signal` fits model once, never refits
The model is fit on first call per symbol and cached indefinitely. Regime models go stale as market structure changes. Add TTL-based refit (e.g., every 4 hours or every N signals).

#### [ISSUE-LOW] Confidence saturates immediately above threshold
```python
confidence = min(abs(norm_score) / SIGNAL_THRESHOLD, 1.0)
```
Any score barely above `SIGNAL_THRESHOLD` produces `confidence = 1.0`. This makes the confidence field meaningless for downstream filtering. Use a steeper scaling:
```python
confidence = min((abs(norm_score) - SIGNAL_THRESHOLD) / (1.0 - SIGNAL_THRESHOLD), 1.0)
```

#### [ISSUE-LOW] Imports from `scanners/` (secondary directory)
`signal_generator.py` imports from `scanners/` while all other modules use `scanner/`. Consolidate to one canonical directory to eliminate the import confusion and potential module-duplication bugs.

---

### `confluence_scorer.py`

#### [BUG-MEDIUM] `MAX_RAW_SCORE = 300.0` hardcoded — won't scale
When new scanners are added, the raw score can exceed 300.0, capping the normalized score at > 1.0 (or causing silent signal suppression if clamped). Derive this constant dynamically from the registered scanners or increase it with a documented rationale.

#### [BUG-LOW] `reasons` list overwritten without merging bonus reasons
Bonus scanner reasons are appended to a new list that overwrites the main reasons list. The final reasons output will be missing entries. Merge with `extend()`, not reassignment.

#### [ISSUE-LOW] `score_all` has no per-symbol exception handling
A single bad symbol will abort the entire batch scan. Wrap the inner loop body in `try/except` with logging.

---

### `entry_exit_calculator.py`

#### [BUG-HIGH] Structure SL for LONG uses `min(swing_lows)` — SL too far below
```python
# Current — wrong: picks the deepest swing low (furthest from entry)
swing_lows = [c.low for c in recent if c.low < entry]
sl_candidate = min(swing_lows) - atr * 0.1

# Fix — use the nearest (highest) swing low below entry
sl_candidate = max(swing_lows) - atr * 0.1
```
This bug causes every LONG trade's structure-based SL to be placed much deeper than intended, inflating the apparent risk-reward and letting through trades that should fail the min-RR gate.

#### [ISSUE-LOW] `or`-pattern on `min_rr` — see systemic section above

---

### `backtester.py`

#### [BUG-HIGH] Uncapped position sizing — notional can exceed balance
```python
sl_pct = safe_divide(abs(trade.entry_price - trade.stop_loss), trade.entry_price) * 100
position_pct = safe_divide(self._config.risk_per_trade_pct, sl_pct)  # uncapped
notional = balance * position_pct  # can be >> balance for tight SL
```
A 0.01% SL with 1% risk-per-trade produces a 100x position. Add a hard cap:
```python
position_pct = min(safe_divide(self._config.risk_per_trade_pct, sl_pct), self._config.max_position_pct)
```

#### [BUG-MEDIUM] `BacktestResults.sharpe_ratio` uses population std (N denominator)
```python
# Current
sharpe = mean_ret / np.std(returns)  # population std — biased for small N

# Fix
sharpe = mean_ret / np.std(returns, ddof=1)  # sample std
```

#### [BUG-MEDIUM] `_generate_signal` reproduces EMA truthy-check bug
The backtester duplicates `if ind.ema_9 and ind.ema_21:` from `indicator_engine.py`. If the indicator engine bug is fixed, the backtester will silently diverge. Extract to a shared helper.

#### [ISSUE-MEDIUM] `allowed_directions` raw string comparison — typo-unsafe
```python
if self._config.allowed_directions == "LONG_ONLY":  # silent typo risk
```
Use an Enum:
```python
class Direction(str, Enum):
    LONG_ONLY = "LONG_ONLY"
    SHORT_ONLY = "SHORT_ONLY"
    BOTH = "BOTH"
```

#### [ISSUE-LOW] Inline `import numpy` in hot loop
`import numpy as _np` inside the per-bar `_replay` loop body. Python caches imports but repeated name lookups in a tight loop across thousands of bars add measurable overhead. Move to module level.

#### [ISSUE-LOW] `_settle_trade` has confusing API — side-effects and return value
`_settle_trade` returns PnL but also mutates `trade.pnl_pct` and `trade.rr_achieved`. Document this clearly or split into a pure PnL calculator and a separate mutating settler.

---

## Module: `alerts/`

### `telegram_notifier.py`

#### [BUG-MEDIUM] `_dedup_cache` dict has no size cap — memory leak
Cache grows without bound for high-throughput signal environments. Add a max size with LRU eviction or use `cachetools.TTLCache`:

```python
from cachetools import TTLCache
self._dedup_cache: TTLCache = TTLCache(maxsize=10_000, ttl=DEDUP_TTL_SECONDS)
```

#### [BUG-LOW] `_chunk_text` only splits on `\n` — single long line overflows
A message with a line > 4096 chars is sent as-is to Telegram, which will reject it. Add hard character-level splitting as a fallback:
```python
if len(chunk) > MAX_MSG_LEN:
    # force-split at MAX_MSG_LEN
    yield chunk[:MAX_MSG_LEN]
    chunk = chunk[MAX_MSG_LEN:]
```

---

### `alert_queue.py`

#### [BUG-MEDIUM] `_worker` uses polling (`get_nowait` + sleep) instead of `await queue.get()`
```python
# Current — 50ms busy-wait, wastes CPU, adds latency
async def _worker(self) -> None:
    while self._running:
        try:
            item = self._queue.get_nowait()
        except asyncio.QueueEmpty:
            await asyncio.sleep(WORKER_SLEEP_S)
            continue

# Fix — zero latency, no CPU waste
async def _worker(self) -> None:
    while self._running:
        item = await self._queue.get()
        ...
        self._queue.task_done()
```

#### [ISSUE-LOW] `AlertType` is a plain `str` subclass — no exhaustiveness checking
Using `str` subclass means typos in alert type strings are silently accepted. Convert to `enum.Enum`.

---

### `rate_limiter.py`

#### [BUG-HIGH] `allow_signal` symbol token refund mutates `_tokens` without `_lock`
```python
# Current — race condition: refund without lock
self._symbol_buckets[symbol]._tokens = min(...)

# Fix — use the existing lock
async with self._lock:
    bucket = self._symbol_buckets[symbol]
    bucket._tokens = min(bucket._tokens + refund, bucket._capacity)
```

#### [BUG-MEDIUM] `_symbol_buckets` dict grows unbounded
Symbols that are delisted or rotated out remain in the dict permanently. Add periodic cleanup (e.g., evict buckets not accessed for > 1 hour):
```python
cutoff = time.monotonic() - 3600
self._symbol_buckets = {k: v for k, v in self._symbol_buckets.items() if v.last_used > cutoff}
```

#### [BUG-LOW] `self._lock = asyncio.Lock()` defined but never used
`_lock` is initialized in `__init__` but all lock usage references `self._global_bucket._lock`. Either use it for the dict-level operations above or remove the dead field.

---

### `webhook_dispatcher.py`

#### [BUG-MEDIUM] `is_disabled` property has state-mutating side effects
`_EndpointHealth.is_disabled` mutates `self.disabled_until` and `self.state` on every read. This is a violation of the property contract and causes the TOCTOU bug below. Move the mutation to an explicit `check_and_recover()` method.

#### [BUG-MEDIUM] `_dispatch_all` evaluates `is_disabled` twice — TOCTOU race
```python
if ep.health.is_disabled:   # First check — may mutate state
    ...
    continue
# ... time passes ...
await self._dispatch_one(ep, ...)  # is_disabled state may have changed
```
Evaluate once per iteration and store the result.

#### [BUG-LOW] `except (httpx.HTTPError, Exception)` — superset swallows `CancelledError`
`Exception` is a superset of `httpx.HTTPError`, making the first clause unreachable. More critically, `asyncio.CancelledError` (a `BaseException` in Python 3.8+) is caught only on Python < 3.8. On current Python it is not caught, which is correct — but the intent is unclear. Remove the redundant `httpx.HTTPError` or restructure:
```python
except asyncio.CancelledError:
    raise  # always propagate cancellation
except Exception as exc:
    self._handle_dispatch_error(ep, exc)
```

---

## Module: `data/`

### `binance_websocket.py`

#### [BUG-HIGH] Double-reconnect race condition
`_watchdog_loop` closes the WebSocket connection, which triggers a `ConnectionClosed` exception in `_recv_loop`. Both tasks then attempt reconnection concurrently, potentially creating duplicate connections and corrupting `_pending` state:

```python
# _watchdog_loop
await self._ws.close()       # causes ConnectionClosed in _recv_loop
await self._do_connect()     # both tasks now in _do_connect simultaneously

# Fix: cancel _recv_loop before reconnecting
if self._recv_task:
    self._recv_task.cancel()
    await asyncio.shield(self._recv_task)
await self._do_connect()
```

#### [BUG-MEDIUM] First reconnect never counted in `stats.reconnects`
```python
# Current — falsy check: when reconnects=0, condition is False, always adds 0
self.stats.reconnects += 1 if self.stats.reconnects else 0

# Fix
self.stats.reconnects += 1
```

#### [BUG-LOW] `session_logon` `or`-pattern — see systemic issue
`api_key or settings.active_api_key.get_secret_value()` — empty string `""` falls through to settings.

#### [ISSUE-LOW] `PendingRequest.sent_at` recorded but never used
The field exists for stale-request detection but no sweep runs. Add a periodic cleanup task to expire requests older than `timeout_s * 2`.

#### [ISSUE-LOW] `get_klines` uses `if start_time:` falsy check
`startTime=0` (epoch start) is a valid value but would be skipped. Use `if start_time is not None:`.

---

### `binance_rest.py`

#### [ISSUE-MEDIUM] API key/secret resolved at construction time
Secrets are read once at instantiation and never refreshed. If secrets are rotated (production best practice), the running client will continue using stale credentials until restart. Use a callable or lazy-resolve pattern:

```python
@property
def _api_key(self) -> str:
    return settings.active_api_key.get_secret_value()
```

#### [NOTE] Testnet URL updated correctly
`REST_TESTNET_BASE = "https://demo-fapi.binance.com"` reflects the 2026-04 Binance migration from `testnet.binancefuture.com`. ✓

---

### `cache_manager.py`

#### [BUG-HIGH] `or`-pattern on `default_ttl` — `0` (no expiry) falls through to settings
`self._default_ttl = default_ttl or settings.redis_cache_ttl_seconds` — a caller passing `default_ttl=0` to disable key expiry will get the default TTL instead. Use `is not None` sentinel.

#### [BUG-MEDIUM] Pub/sub connection leak on abnormal context manager exit
```python
sub_client = aioredis.from_url(self._url, socket_timeout=None)
# if exception raised before explicit close, connection leaks
```
Wrap in `try/finally`:
```python
sub_client = aioredis.from_url(...)
try:
    yield sub_client
finally:
    await sub_client.aclose()
```

#### [BUG-MEDIUM] `keys()` method is O(N) and production-unsafe
`await self._client.keys(pattern)` blocks Redis for the duration of a full keyspace scan. Use `SCAN` instead:
```python
async def scan_keys(self, pattern: str) -> list[str]:
    keys = []
    async for key in self._client.scan_iter(pattern):
        keys.append(key)
    return keys
```

#### [ISSUE-MEDIUM] No connection health check or reconnect logic
Redis connection drops (network blip, Redis restart) cause unhandled exceptions throughout the engine. Add a health-check method and reconnect wrapper:
```python
async def ping(self) -> bool:
    try:
        return await self._client.ping()
    except Exception:
        await self._reconnect()
        return False
```

---

## Module: `risk/`

### `circuit_breaker.py`

#### [BUG-HIGH] `BreakerState.COOLDOWN` defined but never assigned — broken state machine
The state machine transitions from OPEN to CLOSED directly, skipping the COOLDOWN state entirely. Either remove COOLDOWN from the enum or implement the transition:
```python
elif self.state == BreakerState.COOLDOWN:
    if time.monotonic() - self._state_changed_at >= self._cooldown_seconds:
        self._transition(BreakerState.CLOSED)
```

#### [BUG-MEDIUM] `asyncio.create_task()` called without verified running loop
`asyncio.create_task(coro)` will raise `RuntimeError` if called before the event loop is running (e.g., in `__init__` or synchronous initialization paths). Guard with:
```python
try:
    loop = asyncio.get_running_loop()
    loop.create_task(coro)
except RuntimeError:
    # No running loop — schedule for later or use asyncio.ensure_future
    asyncio.ensure_future(coro)
```

---

### `position_sizer.py`

#### [ISSUE-MEDIUM] `leverage_used` heuristic may not match exchange leverage
The position sizer infers leverage from notional/balance ratios rather than querying the exchange. In cross-margin mode or when liquidation prices are asymmetric, this heuristic can be materially wrong. Query `GET /fapi/v2/positionRisk` for true leverage.

#### [ISSUE-LOW] `or`-pattern on `risk_per_trade_pct` — see systemic section

---

### `correlation_analyzer.py`

#### [BUG-HIGH] O(N) `list.pop(0)` in hot path — should be `deque`
```python
# Current — O(N) shift on every price tick for every symbol
def append_price(self, symbol: str, price: float) -> None:
    self._prices[symbol].append(price)
    if len(self._prices[symbol]) > self._lookback:
        self._prices[symbol].pop(0)  # O(N)

# Fix
from collections import deque
self._prices: dict[str, deque[float]] = defaultdict(lambda: deque(maxlen=self._lookback))

def append_price(self, symbol: str, price: float) -> None:
    self._prices[symbol].append(price)  # deque auto-evicts oldest
```
With 200 symbols and a 100-bar lookback, this saves ~4M operations per minute.

#### [BUG-HIGH] No thread safety on `_prices` dict
`update_prices` (called from the scanner loop) and `pearson` / `is_safe_to_add` (called from signal gating) access `_prices` concurrently without a lock. Add `asyncio.Lock`:

```python
self._lock = asyncio.Lock()

async def append_price(self, symbol: str, price: float) -> None:
    async with self._lock:
        self._prices[symbol].append(price)

async def pearson(self, sym_a: str, sym_b: str) -> float | None:
    async with self._lock:
        ...
```

#### [ISSUE-LOW] Insufficient data treated as "safe" — undocumented design decision
`is_safe_to_add` returns `True` when correlation cannot be computed (insufficient data). This means a new symbol added to the portfolio bypasses the correlation gate entirely until enough history is accumulated. Document this behaviour explicitly or add a conservative fallback.

---

### `exposure_tracker.py`

#### [BUG-HIGH] `_daily_pnl` field is dead code — `reset_daily_pnl()` doesn't reset it
```python
# In __init__:
self._daily_pnl = 0.0              # defined

# In close_position:
self._daily_pnl += pnl             # incremented

# In daily_pnl property:
return self._realised_pnl + self.unrealised_pnl  # _daily_pnl never referenced

# In reset_daily_pnl:
self._realised_pnl = 0.0           # resets _realised_pnl, NOT _daily_pnl
```
Either expose `_daily_pnl` through the property and reset it correctly, or remove it entirely to avoid confusion.

#### [BUG-HIGH] Race condition on read-only properties — unlocked access to `_positions`
```python
@property
def unrealised_pnl(self) -> float:
    return sum(p.unrealised_pnl for p in self._positions.values())  # no lock!

@property
def total_notional(self) -> float:
    return sum(abs(p.notional) for p in self._positions.values())  # no lock!
```
While `update_all_prices` holds `_lock` and iterates `_positions`, a concurrent read from `unrealised_pnl` can produce a torn read or KeyError. Either use `asyncio.Lock` consistently on all property access, or use a snapshot pattern:

```python
@property
def unrealised_pnl(self) -> float:
    positions_snapshot = list(self._positions.values())  # atomic copy in CPython
    return sum(p.unrealised_pnl for p in positions_snapshot)
```

#### [ISSUE-HIGH] No persistence — engine restart loses all position tracking
All portfolio state (`_positions`, `_realised_pnl`, `_daily_pnl`) is in-memory only. A service restart silently resets to zero, causing the risk gate to believe there are no open positions. Add startup reconciliation against the exchange:

```python
async def reconcile_with_exchange(self, binance_rest: BinanceRestClient) -> None:
    positions = await binance_rest.get_position_risk()
    for pos in positions:
        if abs(pos["positionAmt"]) > 0:
            self._positions[pos["symbol"]] = Position.from_exchange(pos)
```

---

## Priority Remediation Checklist

| Priority | Bug | File | Effort |
|----------|-----|------|--------|
| P0 | Double-reconnect race condition | `data/binance_websocket.py` | Medium |
| P0 | Race condition on `_prices` dict (correlation) | `risk/correlation_analyzer.py` | Small |
| P0 | Race condition on exposure properties | `risk/exposure_tracker.py` | Small |
| P0 | Uncapped position sizing in backtester | `signals/backtester.py` | Small |
| P0 | `allow_signal` token refund without lock | `alerts/rate_limiter.py` | Small |
| P1 | Structure SL for LONG uses `min()` not `max()` | `signals/entry_exit_calculator.py` | Small |
| P1 | Regime weight suppression not in `max_possible` | `signals/signal_generator.py` | Small |
| P1 | `COOLDOWN` state never assigned in circuit breaker | `risk/circuit_breaker.py` | Small |
| P1 | `_daily_pnl` dead code + wrong reset | `risk/exposure_tracker.py` | Small |
| P1 | `keys()` O(N) production-unsafe in cache manager | `data/cache_manager.py` | Small |
| P1 | Systemic `or`-pattern config bug (7 files) | multiple | Medium |
| P2 | Unbounded caches: `_results`, `_regime_fit`, `_dedup_cache`, `_symbol_buckets` | multiple | Medium |
| P2 | VWAP never session-reset | `signals/indicator_engine.py` | Small |
| P2 | `macd_bullish_cross` not a real crossover | `signals/indicator_engine.py` | Small |
| P2 | Alert queue polling → `await queue.get()` | `alerts/alert_queue.py` | Small |
| P2 | O(N) `list.pop(0)` → `deque` | `risk/correlation_analyzer.py` | Small |
| P2 | No persistence / reconciliation on restart | `risk/exposure_tracker.py` | Large |
| P3 | EMA warm-up bias | `signals/indicator_engine.py` | Medium |
| P3 | RSI non-Wilder seeding | `signals/indicator_engine.py` | Medium |
| P3 | Sharpe ratio uses population std | `signals/backtester.py` | Trivial |
| P3 | `reconnects` counter bug (first reconnect) | `data/binance_websocket.py` | Trivial |

---

## Recommendations

1. **Introduce `is not None` throughout** — run a codebase-wide replacement of `x or settings.x` → `x if x is not None else settings.x` for all numerical configuration parameters.

2. **Consolidate `scanner/` vs `scanners/`** — pick one canonical directory name and fix all imports. This is a latent import-confusion bug waiting to surface in production.

3. **Add startup position reconciliation** — the exposure tracker must reconcile against the exchange on every restart before the risk gate goes live. Otherwise, the engine can trade as if it has no open positions after a crash.

4. **Use `collections.deque(maxlen=N)` for all rolling buffers** — the correlation analyzer `list.pop(0)` is the most critical instance, but audit other rolling buffers in the codebase.

5. **Audit all asyncio property reads for lock consistency** — any property that reads from a dict/list that is mutated in an async task should either use a lock or provide a documented guarantee of atomic access (e.g., CPython GIL + single-element operations only).

6. **Add integration test for WebSocket reconnect** — the double-reconnect race condition is difficult to reproduce manually. Write a test that simulates `_watchdog_loop` and `_recv_loop` firing simultaneously.

---

*Report generated by automated daily review task. Next review: 2026-05-19 09:00 AM.*
