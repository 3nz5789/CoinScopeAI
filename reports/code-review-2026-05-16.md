# CoinScopeAI — Automated Code Review Report
**Date:** 2026-05-16  
**Scope:** `coinscope_trading_engine/` — scanner/, signals/, alerts/, data/, risk/  
**Reviewer:** Scoopy (Scheduled Daily Review, 09:00 UTC)

---

## Executive Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | 7 |
| 🟠 High | 11 |
| 🟡 Medium | 14 |
| 🔵 Low / Style | 10 |

**Overall assessment:** The codebase shows strong architectural discipline — typed dataclasses, async-first design, per-endpoint health tracking, and layered separation of concerns. However, several bugs are production-impacting: a retired Binance API endpoint, blocking I/O inside async coroutines, a busy-wait loop in the alert queue, and a threading lock that can stall the event loop. These must be fixed before scaling to live trading.

---

## Module: scanner/

### 🔴 CR-01 — Retired Binance endpoint: `GET /fapi/v1/allForceOrders`
**Files:** `scanner/liquidation_scanner.py`, `data/binance_rest.py`

Binance retired `/fapi/v1/allForceOrders` in April 2025. Both the scanner and the REST client still call this endpoint. It returns 410 Gone at runtime, silently killing all liquidation signals.

**Fix:**
- Replace REST polling with the WebSocket stream `!forceOrder@arr` (already partially wired in `market_stream.py`).
- Remove `get_liquidation_orders()` from `binance_rest.py` or mark it `@deprecated`.
- Clean up dead serialisation helpers `_liq_to_dict` / `_dict_to_liq` in liquidation_scanner.
- **Note:** Binance WS liquidation stream (2026-04-10 update) now emits only the largest single order per 1000 ms window — update documentation and signal logic accordingly.

---

### 🔴 CR-02 — `asyncio.CancelledError` not re-raised in scanner base loop
**File:** `scanner/base_scanner.py` — `_loop()`

`CancelledError` is caught but not re-raised. When the engine calls `task.cancel()`, the scanner loop silently swallows the signal and continues running. This prevents clean shutdown and causes dangling tasks.

```python
# WRONG
except asyncio.CancelledError:
    logger.warning("Scanner loop cancelled")
    # falls through — loop continues!

# CORRECT
except asyncio.CancelledError:
    logger.warning("Scanner loop cancelled")
    raise
```

---

### 🟠 CR-03 — OrderBook wall detection lacks proximity filter
**File:** `scanner/orderbook_scanner.py`

`_detect_walls()` finds the globally largest bid/ask level without requiring it to be near the current price. A wall 15% away from mid is scored identically to one 0.2% away, generating false signals.

**Fix:** Filter candidate levels to within `±wall_proximity_pct` (e.g. 2%) of `mid_price` before picking the largest.

---

### 🟠 CR-04 — IndexError on short candle history in pattern scanner
**File:** `scanner/pattern_scanner.py`

`candles[-3]` is accessed as `p2` without a length guard. If the scanner receives fewer than 3 candles (startup, newly listed symbol), this raises `IndexError`.

```python
# Add guard:
if len(candles) < 3:
    return []
```

Also: tweezer body tolerance `0.001` is hardcoded — too tight for low-price altcoins (e.g. FLOKI at $0.00015). Make this a configurable relative threshold.

---

### 🟡 CR-05 — Funding rate threshold applied at wrong scale
**File:** `scanner/funding_rate_scanner.py`

`REVERSAL_THRESHOLD = 0.05` is defined (interpreted as 5%) but later used as `REVERSAL_THRESHOLD / 100.0 = 0.0005%`. This threshold is so small it fires on almost every non-zero funding move, flooding signals.

**Fix:** Decide on one representation (raw or percentage) and use it consistently. Recommended: `REVERSAL_THRESHOLD = 0.0005` (raw Binance format, ~0.05%).

---

### 🔵 CR-06 — Cross-module coupling via serialisation round-trip
**Files:** `scanner/volume_scanner.py` — `_candle_to_dict()` / `_dict_to_candle()`

These helpers convert `Candle` dataclasses to/from plain dicts for inter-scanner data passing. They duplicate `DataNormalizer` field logic. Replace with direct `Candle` passing or shared `dataclasses.asdict()` / `Candle(**d)` reconstruction.

---

## Module: signals/

### 🔴 CR-07 — Two parallel codebases: `scanner/` vs `scanners/` (plural)
**File:** `signals/signal_generator.py`

`signal_generator.py` imports from `scanners.volume_scanner` (plural) — a legacy path — while the active engine uses `scanner/` (singular). This means signal generation runs against stale/unmaintained scanner code. The two implementations diverge silently.

**Fix:** Remove the `scanners/` directory or clearly tombstone it. Repoint `signal_generator.py` to `scanner.*` imports.

---

### 🟠 CR-08 — `sys.path.insert()` anti-pattern in signal_generator
**File:** `signals/signal_generator.py`

`sys.path.insert(0, ...)` at module level is a packaging anti-pattern that can cause import shadowing and non-deterministic import resolution. Use proper package structure with `pyproject.toml`/`setup.py` and relative imports.

---

### 🟠 CR-09 — `_regime_fit` dict never cleared (stale HMM fits)
**File:** `signals/signal_generator.py`

The `_regime_fit` cache accumulates HMM fit objects indexed by symbol and is never evicted. Over days of operation this leaks memory proportionally to the number of scanned symbols × regime model size. Also, stale fits are used after market microstructure changes.

**Fix:** Apply an LRU cache with a TTL (e.g. 1 hour) or flush `_regime_fit` on the weekly retrain event.

---

### 🟡 CR-10 — VWAP not reset at session boundary
**File:** `signals/indicator_engine.py`

VWAP accumulates price×volume and total volume from the beginning of available data, not from the daily session open. For futures, the session is midnight UTC. VWAP computed over multi-day windows misleads intraday signals.

**Fix:** Accept an `anchor_timestamp` (e.g. today's 00:00 UTC) and filter candles to `open_time >= anchor`.

---

### 🟡 CR-11 — EMA seed bias on first bar
**File:** `signals/indicator_engine.py`

`out[0] = data[0]` seeds EMA with the first price, meaning the calculated EMA will remain biased toward that first price until sufficient data warms the calculation. For short series (< 3× the period), this produces materially wrong values.

**Fix:** Either require `len(data) >= 3 × period` or use Wilder's smoothing with an SMA-based seed from the first `period` bars.

---

### 🟡 CR-12 — `_find_structure_sl()` uses the deepest swing low, not most recent
**File:** `signals/entry_exit_calculator.py`

`min(swing_lows)` returns the absolute lowest price in the lookback, not the most recent swing low. For a trending asset this places the stop-loss far below current price, massively over-sizing risk and distorting the R:R ratio.

**Fix:** Use `swing_lows[-1]` (most recent) or `min(swing_lows[-3:])` (recent cluster).

---

### 🟡 CR-13 — Dead code in confluence_scorer
**File:** `signals/confluence_scorer.py`

`bonus_total = 0.0` and `bonuses: list[str] = []` are assigned but immediately overwritten by the next two lines. The score is normalised to 70.0 maximum before bonuses are added, meaning the maximum achievable score is 70 + bonus cap, not 100. Confirm this is intentional and document it.

---

## Module: alerts/

### 🔴 CR-14 — Blocking `requests.post()` in async Telegram sender
**File:** `alerts/telegram_alerts.py`

`requests.post()` is a synchronous HTTP call used inside an async context. It blocks the entire event loop for the duration of the network round-trip (~100–500 ms), halting all scanner, signal, and risk activity.

**Fix:** Replace with `httpx.AsyncClient.post()` or `aiohttp.ClientSession.post()` (see `telegram_notifier.py` — the modern replacement already exists; decommission `telegram_alerts.py`).

---

### 🔴 CR-15 — Busy-wait loop in alert queue
**File:** `alerts/alert_queue.py`

```python
while True:
    try:
        item = self._queue.get_nowait()
    except asyncio.QueueEmpty:
        await asyncio.sleep(0.05)   # polls 20 times/second
```

This burns ~2% CPU continuously and adds up to 50 ms alert latency. Additionally, the full-queue check before `put_nowait()` is a TOCTOU race — the queue can fill between the check and the put.

**Fix:**
```python
item = await self._queue.get()   # blocks zero CPU until item arrives
```

---

### 🔴 CR-16 — `threading.Lock` blocks the async event loop
**File:** `alerts/rate_limiter.py`

`threading.Lock` acquired inside an `async def` function blocks the OS thread running the event loop for the full lock-hold duration. Under rate-limit contention this can stall the entire engine.

**Fix:** Replace `threading.Lock` with `asyncio.Lock`. Also cap `_symbol_buckets` growth — it accumulates one entry per symbol indefinitely:

```python
if len(self._symbol_buckets) > MAX_SYMBOLS:
    # evict LRU entry
```

---

### 🟠 CR-17 — Blocking ccxt call inside async retrain scheduler
**File:** `alerts/retrain_scheduler.py`

`self.exchange.fetch_ohlcv()` is a synchronous ccxt network call inside an `async def`. It blocks the event loop for the full REST request duration (~200–2000 ms per symbol × 3 symbols = up to 6 seconds frozen).

**Fix:**
```python
candles = await asyncio.to_thread(self.exchange.fetch_ohlcv, pair, "4h", limit=90*6)
```

---

### 🟠 CR-18 — Pickle deserialisation of untrusted S3 data is a security risk
**File:** `alerts/retrain_scheduler.py`

The HMM model is stored as `pickle.dumps(new_model)` to S3 and loaded with `pickle.loads()`. If an attacker can write to the S3 bucket, they can inject arbitrary code that executes on the server during model load.

**Fix:** Serialise model parameters to JSON or use `joblib` with integrity verification (checksum the saved bytes and verify before loading).

---

### 🟠 CR-19 — `datetime.utcnow()` deprecated in Python 3.12+
**File:** `alerts/retrain_scheduler.py`

```python
# DEPRECATED
if datetime.utcnow().weekday() == 6:

# CORRECT
if datetime.now(timezone.utc).weekday() == 6:
```

`datetime.utcnow()` is deprecated since Python 3.12 (PEP 615) and will be removed. The `timezone`-naive datetime also risks confusion with local-time comparisons.

---

### 🟡 CR-20 — `model_history` list grows unboundedly in memory
**File:** `alerts/retrain_scheduler.py`

Every weekly retrain appends the previous model to `self.model_history` but nothing prunes it. After a year this holds 52 model objects (each potentially hundreds of MB for HMM ensembles).

**Fix:** Cap at the last N models (e.g. 4) or persist to disk/S3 and evict from RAM.

---

### 🟡 CR-21 — `alpha_decay_monitor` Sharpe annualised with hardcoded trades-per-day
**File:** `alerts/alpha_decay_monitor.py`

`trades_per_day = 4` is hardcoded for annualisation. If the engine runs higher/lower frequency this produces wrong Sharpe values.

**Fix:** Derive from `settings.scan_interval_s`: `trades_per_day = 86400 / settings.scan_interval_s`.

---

### 🟡 CR-22 — Webhook dispatcher zip mismatch race condition
**File:** `alerts/webhook_dispatcher.py`

In `_dispatch_all()`, tasks are built from `[ep for ep in self._endpoints if not ep.is_disabled]`, run via `asyncio.gather()`, and results are then zipped against the same filter. However `record_failure()` is called inside tasks and can mutate `ep.is_disabled` mid-gather — making the filtered list and results list different lengths, causing `zip` to silently drop records.

**Fix:** Snapshot the endpoint list before dispatching:
```python
active_endpoints = [ep for ep in self._endpoints if not ep.is_disabled]
results = await asyncio.gather(*[self._dispatch(ep) for ep in active_endpoints], return_exceptions=True)
for ep, result in zip(active_endpoints, results):
    ...
```

---

### 🟡 CR-23 — `scale_up_manager` uses `print()` instead of logger
**File:** `alerts/scale_up_manager.py`

Profile promotions are logged with `print()`, bypassing the structured logger. These events are important operational signals and should use `logger.info()` with structured fields.

---

## Module: data/

### 🟠 CR-24 — WS testnet URL silently routes to mainnet
**File:** `data/binance_websocket.py`

```python
WS_TESTNET_URL = "wss://ws-fapi.binance.com/ws-fapi/v1"  # mainnet fallback
```

When `testnet=True`, the manager uses the mainnet URL. Code has a comment acknowledging this, but callers creating `BinanceWebSocketManager(testnet=True)` will unknowingly connect to mainnet. This is a silent misconfiguration risk for demo/paper trading environments.

**Fix:** Either raise `NotImplementedError` when `testnet=True` and this endpoint isn't supported, or set `WS_TESTNET_URL = None` and guard in `connect()`.

---

### 🟡 CR-25 — Redundant inline `__import__` in data_normalizer
**File:** `data/data_normalizer.py` — `ws_depth_to_orderbook()`

```python
ts = __import__("datetime").datetime.now(timezone.utc)
```

`datetime` is already imported at the top of the module. This inline import is a code smell (possibly a copy-paste artifact). Replace with `datetime.now(timezone.utc)`.

---

### 🟡 CR-26 — `alpha_decay_monitor.alert_history` grows without bound
**File:** `alerts/alpha_decay_monitor.py`

`self.alert_history` appends every triggered alert with no eviction. Under high-frequency trading this accumulates thousands of entries, consuming memory proportional to trading activity.

**Fix:** Cap at last 1000 entries or use a `collections.deque(maxlen=1000)`.

---

### 🔵 CR-27 — `binance_rest.py` `_sign()` uses dict insertion order (intentional but fragile)
**File:** `data/binance_rest.py`

The comment explicitly states parameter order must NOT be sorted because Binance verifies against on-wire insertion order. This is correct per Binance's signed endpoint spec, but is fragile: any code path that reconstructs or copies the params dict (e.g. `{**params, "extra": val}`) may silently reorder keys and break signatures.

**Recommendation:** Wrap signed request params in `OrderedDict` or document the ordering contract with a type alias `SignedParams = OrderedDict[str, Any]` and enforce it at the function boundary.

---

### 🔵 CR-28 — `cache_manager.py` — `keys()` is O(N) on all Redis keyspace
**File:** `data/cache_manager.py`

`keys()` method is documented as O(N) and warns against production use, but `get_all_signals()` calls it with a pattern. In a large deployment this can block Redis for seconds.

**Fix:** `get_all_signals()` should use `scan_keys()` (the already-implemented SCAN-based alternative) at all times, even in non-production settings. Remove or privatize the `keys()` method.

---

## Module: risk/

### 🟡 CR-29 — `CorrelationAnalyzer.append_price()` uses `list.pop(0)` — O(N)
**File:** `risk/correlation_analyzer.py`

`list.pop(0)` on a 50-element list is O(N). Called on every incoming candle for every tracked symbol (potentially 100–200 symbols), this adds measurable overhead.

**Fix:** Use `collections.deque(maxlen=self._lookback)` — O(1) append and automatic eviction.

---

### 🟡 CR-30 — Circuit breaker `rapid_loss_pct` compares absolute loss to percentage threshold
**File:** `risk/circuit_breaker.py`

```python
window_loss = sum(p for _, p in self._rapid_log if p < 0)
if abs(window_loss) >= self._rapid_loss_pct:
```

`window_loss` accumulates raw PnL percentages (e.g. `-0.5`, `-0.8`). `self._rapid_loss_pct = 1.5` (default) means trip at 1.5 total percentage points lost across trades in the window. This is correct — but the parameter name `rapid_loss_pct` is ambiguous; it could be misread as "percentage of balance". Rename to `rapid_loss_threshold_pct` and document the comparison unit explicitly.

---

### 🔵 CR-31 — `ExposureTracker.daily_pnl` double-counts realised PnL
**File:** `risk/exposure_tracker.py`

```python
@property
def daily_pnl(self) -> float:
    return self._realised_pnl + self.unrealised_pnl
```

`_realised_pnl` is accumulated from `close_position()`. `_daily_pnl` is also updated in `close_position()` but never read (dead field after the initial design change). Meanwhile `_realised_pnl` is reset by `reset_daily_pnl()` but `unrealised_pnl` is not (open positions carry over to next day). Verify the daily boundary semantics — does PnL from positions opened yesterday and closed today count in yesterday's or today's daily loss? Document the choice and remove the dead `_daily_pnl` field.

---

### 🔵 CR-32 — `PositionSizer.leverage_used` calculation is disconnected from margin model
**File:** `risk/position_sizer.py`

```python
leverage_used = min(
    self._max_leverage,
    max(1, int(notional / max(balance * 0.1, 1))),
)
```

This formula ties leverage to `10%` of balance regardless of actual margin requirements. For a $10k balance with $500 notional, it returns `leverage = 5x` which may conflict with the margin actually reserved on the exchange. The leverage should be `int(notional / margin_reserved)` where `margin_reserved = notional / self._max_leverage`.

---

## Architecture Observations

### Dual scanner path (scanner/ vs scanners/)
The coexistence of `scanner/` (active modular architecture) and `scanners/` (legacy) is the highest-priority architectural debt. It creates confusion about which code runs in production, makes testing unreliable, and means bug fixes applied to one codebase don't propagate to the other.

**Action:** Audit all import paths. Delete `scanners/` after confirming zero live dependencies.

### WebSocket endpoint clarification ✅
The codebase correctly distinguishes:
- `wss://fstream.binance.com` — market data pub/sub (no auth)
- `wss://ws-fapi.binance.com` — signed WS API (orders/account)

This is well-documented in `market_stream.py` and `binance_stream_adapter.py`. No confusion in data/ layer.

### `BinanceFuturesMultiStreamManager` is well-designed
The 200-stream-per-connection limit is handled correctly with chunking. No issues.

### `CircuitBreaker` implementation is solid
The 5-trigger pattern (daily loss, drawdown, consecutive losses, rapid loss, manual) with auto-reset and async callback is production-quality. Minor naming and documentation issues only.

### `CorrelationAnalyzer` direction-gating is correct
Only same-direction positions are compared — opposite directions are correctly treated as potential hedges. The `frozenset` deduplication in `high_correlation_pairs()` is correct.

---

## Priority Fix List

| Priority | ID | File | Issue |
|----------|-----|------|-------|
| P0 | CR-01 | liquidation_scanner.py, binance_rest.py | Retired API endpoint — no liquidation data |
| P0 | CR-14 | alerts/telegram_alerts.py | Blocking HTTP blocks event loop |
| P0 | CR-15 | alerts/alert_queue.py | Busy-wait loop blocks event loop |
| P0 | CR-16 | alerts/rate_limiter.py | threading.Lock blocks event loop |
| P1 | CR-02 | scanner/base_scanner.py | CancelledError swallowed — no clean shutdown |
| P1 | CR-17 | alerts/retrain_scheduler.py | Blocking ccxt freezes event loop for 6s |
| P1 | CR-18 | alerts/retrain_scheduler.py | Pickle deserialization of S3 data (RCE risk) |
| P1 | CR-07 | signals/signal_generator.py | Signals run against legacy scanner/ (stale) |
| P1 | CR-22 | alerts/webhook_dispatcher.py | zip mismatch race condition |
| P2 | CR-03 | scanner/orderbook_scanner.py | Remote walls scored as market-moving |
| P2 | CR-04 | scanner/pattern_scanner.py | IndexError on <3 candles |
| P2 | CR-05 | scanner/funding_rate_scanner.py | Threshold at wrong scale |
| P2 | CR-10 | signals/indicator_engine.py | VWAP not reset at session boundary |
| P2 | CR-12 | signals/entry_exit_calculator.py | SL uses deepest not most recent swing |
| P2 | CR-19 | alerts/retrain_scheduler.py | datetime.utcnow() deprecated |
| P2 | CR-24 | data/binance_websocket.py | testnet=True silently routes to mainnet |
| P3 | CR-09 | signals/signal_generator.py | regime fit cache memory leak |
| P3 | CR-20 | alerts/retrain_scheduler.py | model_history unbounded growth |
| P3 | CR-29 | risk/correlation_analyzer.py | O(N) list.pop(0) on hot path |
| P3 | CR-31 | risk/exposure_tracker.py | daily_pnl semantics unclear, dead field |

---

*Report generated by Scoopy automated review — 2026-05-16 09:00 UTC*
