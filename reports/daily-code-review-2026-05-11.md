# CoinScopeAI Daily Code Review — 2026-05-11

**Modules reviewed:** `scanner/`, `scanners/`, `signals/`, `alerts/`, `data/`, `risk/`, `core/risk_gate.py`
**Generated:** 2026-05-11 (automated)

---

## 1. Executive Summary

The codebase is generally well-structured and documented. The new modular `scanner/` architecture (BaseScanner → subclasses → ConfluenceScorer) is clean and extensible. However, several issues were found that warrant attention before the next live session — one critical bug (`daily_pnl` never resets), two medium bugs (sync HTTP blocking the event loop; duplicate scanner packages with divergent implementations), and several lower-severity items.

---

## 2. Critical Issues

### 2.1 `RiskGate.daily_pnl` Never Resets (core/risk_gate.py)

**Severity: CRITICAL**

`RiskGate` initialises `self.daily_pnl = 0` at construction time but has no `reset_daily()` method. The circuit-breaker check compares `daily_pnl` against a percentage of `initial_capital`, so after the first trading day the accumulating negative `daily_pnl` will permanently hold the gate open.

Compare: `CircuitBreaker` correctly implements `reset_daily()` — `RiskGate` does not.

```python
# core/risk_gate.py — MISSING METHOD
def reset_daily(self) -> None:
    """Call at midnight / start of each trading session."""
    self.daily_pnl = 0
    self.consecutive_losses = 0   # reset per-day also
    logger.info("RiskGate daily state reset.")
```

**Recommended fix:** Add `reset_daily()` and call it from the main loop's daily-reset hook (same place `CircuitBreaker.reset_daily()` is called).

---

## 3. Security Findings

### 3.1 Synchronous `requests` in `TelegramAlerts` (alerts/telegram_alerts.py)

**Severity: MEDIUM-HIGH**

`TelegramAlerts._send()` uses the blocking `requests` library. The rest of the engine is fully async (`aiohttp`, `asyncio`). Every Telegram alert fired from an `async` context blocks the event loop for the network round-trip (up to the 5-second timeout).

```python
# Current — blocks event loop
requests.post(
    f"https://api.telegram.org/bot{self.token}/sendMessage",
    json={...},
    timeout=5,
)

# Fix — use aiohttp (already a project dependency)
async def _send(self, text: str) -> None:
    if not self.enabled:
        print(f"[TELEGRAM] {text}")
        return
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(
                f"https://api.telegram.org/bot{self.token}/sendMessage",
                json={"chat_id": self.chat_id, "text": text, "parse_mode": "Markdown"},
                timeout=aiohttp.ClientTimeout(total=5),
            )
    except Exception as e:
        logger.error("Telegram error: %s", e)
```

Note: all public methods (`send_signal`, `send_trade_closed`, etc.) must also become `async def` and callers must `await` them.

### 3.2 `key_vault.py` — Missing Authentication Data (AEAD Tag Validation)

**Severity: LOW (informational)**

`key_vault.encrypt_key` passes `None` as the `associated_data` argument to `AESGCM.encrypt`. This is fine for confidentiality but means the ciphertext is not bound to any contextual metadata (e.g., user ID). If a ciphertext were moved to another user's row in the database, decryption would still succeed. Consider binding ciphertexts to `user_id`:

```python
def encrypt_key(plaintext: str, user_id: str) -> str:
    ...
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), user_id.encode())
```

---

## 4. Bugs and Edge Cases

### 4.1 Duplicate Scanner Packages — Divergent Implementations

**Severity: MEDIUM**

There are two parallel scanner packages:

| Package | Used by | `VolumeScanner` API |
|---------|---------|---------------------|
| `scanner/` | `api.py`, `signals/confluence_scorer.py` | `async scan(symbol) → ScannerResult` |
| `scanners/` | `signals/signal_generator.py` | `score_signal(df, funding, oi_delta) → dict` |

These are completely different classes with the same name. `signal_generator.py` imports from `scanners/` while the rest of the system imports from `scanner/`. The two code paths use different scoring models and neither knows about the other's signals.

**Recommended action:** Deprecate `scanners/` (plural) and migrate `signal_generator.py` to use the `scanner/` (singular) hierarchy. Document this as a tracked ticket.

### 4.2 `CircuitBreaker` Rapid Loss — Unit Ambiguity

**Severity: MEDIUM**

`record_trade_result(pnl_pct)` sums raw `pnl_pct` values (e.g., `0.02` for a 2% loss), but the threshold `rapid_loss_pct` defaults to `1.5`. The docstring says "% loss", implying the caller should pass `2.0` (not `0.02`). If callers pass decimal fractions (which `close_position` in `RiskGate` uses for `pnl_pct`), the breaker never trips (would need 150% aggregate loss in 5 minutes).

```python
# circuit_breaker.py line 205
window_loss = sum(p for _, p in self._rapid_log if p < 0)
if abs(window_loss) >= self._rapid_loss_pct:   # 1.5 — but pnl_pct is 0.02-style
```

**Fix:** Either document the expected unit explicitly and enforce it in the method signature, or normalise internally:

```python
def record_trade_result(self, pnl_pct: float) -> None:
    """
    Args:
        pnl_pct: Trade P&L as a decimal fraction (e.g., -0.02 for -2% loss).
                 rapid_loss_pct threshold is also in decimal (default 0.015 = 1.5%).
    """
```

And update the default: `rapid_loss_pct: float = 0.015`.

### 4.3 `LiquidationScanner` Silent No-Op Outside API Context

**Severity: LOW-MEDIUM**

`scanner/liquidation_scanner.py` does a late `import api` at scan time to read the WebSocket liquidation buffer. When run outside `api.py` (test suite, script), it silently returns no liquidations with only a one-time `WARNING` log. This makes it impossible to distinguish "no liquidations occurred" from "the feed is unavailable".

```python
# Current: silent no-op
return []

# Better: return an error ScannerResult so callers know
return ScannerResult(
    scanner=self.name, symbol=symbol,
    error="WS liquidation feed unavailable — run within api.py context"
)
```

### 4.4 `_dict_to_candle` Late Import in Hot Path (scanner/volume_scanner.py)

**Severity: LOW (performance)**

The `_dict_to_candle` function does deferred imports (`from datetime import ...`, `from data.data_normalizer import Candle as C`) inside the function body. On every cache hit this function is called once per candle. Python caches modules so repeat imports are cheap, but the lookup overhead is non-zero on a hot path. The `Candle` alias `C` is also confusing.

```python
# Current
def _dict_to_candle(d: dict, symbol: str, interval: str) -> Candle:
    from datetime import datetime, timezone
    from data.data_normalizer import Candle as C
    return C(...)

# Fix — move imports to module top-level (already imported: DataNormalizer, Candle)
def _dict_to_candle(d: dict, symbol: str, interval: str) -> Candle:
    return Candle(
        symbol=symbol, interval=interval,
        open_time  = datetime.fromisoformat(d["open_time"]),
        ...
    )
```

### 4.5 `HMM Regime Fit Once Per Symbol` — Stale Model Risk (signals/signal_generator.py)

**Severity: LOW-MEDIUM**

`SignalGenerator._regime_fit` tracks whether an `EnsembleRegimeDetector` was fitted per symbol. Once fitted, the same model is reused for all subsequent predictions with no re-fitting. In volatile or regime-shifting markets, the HMM parameters may become stale within hours.

```python
# Current — fit once and never again
if symbol not in self._regime_fit:
    self.regime_det.fit(r, v)
    self._regime_fit[symbol] = True
```

**Recommended fix:** Track the fit timestamp and re-fit periodically (e.g., every 4 hours or after N new candles):

```python
FIT_INTERVAL_S = 4 * 3600   # re-fit every 4 hours

if symbol not in self._regime_fit or (time.time() - self._regime_fit[symbol]) > FIT_INTERVAL_S:
    self.regime_det.fit(r, v)
    self._regime_fit[symbol] = time.time()
```

---

## 5. Performance Optimisations

### 5.1 `CircuitBreaker._rapid_log` — Use `collections.deque`

**Severity: LOW**

The rapid-loss log prunes stale entries using list comprehension on every trade, creating a new list each time. For high-frequency operation, a `deque` with `maxlen` or a bisect-based window is more efficient:

```python
from collections import deque

# In __init__:
self._rapid_log: deque[tuple[float, float]] = deque()

# In record_trade_result:
now = time.monotonic()
self._rapid_log.append((now, pnl_pct))
cutoff = now - self._rapid_window_s
while self._rapid_log and self._rapid_log[0][0] < cutoff:
    self._rapid_log.popleft()   # O(1) vs O(n) list comprehension
```

### 5.2 `VolumeScanner` Cache TTL Calculation on Every Call

The `timeframe_to_seconds(self._timeframe)` call inside `_fetch_candles` is on the REST fallback path. Since `_timeframe` is constant for the lifetime of the scanner, compute the TTL once in `__init__`:

```python
def __init__(self, ...):
    ...
    from utils.helpers import timeframe_to_seconds
    self._cache_ttl = max(5, timeframe_to_seconds(self._timeframe) // 2)
```

---

## 6. Best Practice Violations

### 6.1 Mixed Logging Styles in `core/risk_gate.py`

`RiskGate` uses f-string logging (`logger.warning(f"🛑 Position blocked: {reason}")`) while all other modules use %-style formatting (`logger.warning("%s error for %s: %s", ...)`). F-string logging evaluates the format string even if the log level is suppressed, wasting CPU on filtered messages.

```python
# Replace throughout core/risk_gate.py:
logger.warning("Position blocked: %s", reason)
logger.info("Position opened: %s %+d @ %.2f | SL: %.2f | TP: %.2f | Size: %.4f",
            symbol, direction, entry_price, stop_loss, take_profit, position_size)
```

### 6.2 `scalp_scanner.py` Import Path Inconsistency

`scanners/scalp_scanner.py` imports from `app.integrations.binance` and `app.integrations.okx` — a path that does not exist relative to its location in `coinscope_trading_engine/scanners/`. This file will raise `ModuleNotFoundError` if imported directly. It appears to be written for a monorepo layout that has since been restructured.

**Action:** Verify whether `scalp_scanner.py` is actively used in production. If so, update its import paths to match the current layout.

### 6.3 Missing `__slots__` on High-Frequency Dataclasses

`ScannerHit` and `ScannerResult` are instantiated thousands of times per scan cycle. Adding `__slots__` reduces per-instance memory by ~30% and speeds up attribute access:

```python
@dataclass
class ScannerHit:
    __slots__ = ("scanner", "symbol", "direction", "strength", "score", "reason", "metadata", "timestamp")
    ...
```

Note: `field(default_factory=...)` works with `__slots__` in Python 3.10+.

---

## 7. Alerts Module — Historical Instability Note

The `alerts/` module contains many inline `# BUG-N FIX` comments (BUG-5, -6, -7, -8, -14, -15) indicating a history of patched regressions. The fixes appear correct but the pattern suggests this module needs a focused refactor and proper unit test coverage. Current test coverage for `alerts/` was not observed in the `tests/` directory.

**Recommended:** Add `tests/test_alerts.py` covering at minimum:
- `rate_limiter.py` token bucket allow/deny behaviour
- `alert_queue.py` enqueue/dequeue ordering
- `scale_up_manager.py` promotion state persistence across restarts

---

## 8. Summary Table

| # | Module | Issue | Severity | Action |
|---|--------|-------|----------|--------|
| 1 | `core/risk_gate.py` | `daily_pnl` never resets | 🔴 Critical | Add `reset_daily()` |
| 2 | `alerts/telegram_alerts.py` | Blocking `requests` in async context | 🟠 Medium-High | Migrate to `aiohttp` |
| 3 | `scanner/` vs `scanners/` | Duplicate packages with divergent APIs | 🟠 Medium | Deprecate `scanners/`, migrate callers |
| 4 | `risk/circuit_breaker.py` | `rapid_loss_pct` unit ambiguity | 🟠 Medium | Document + normalise units |
| 5 | `scanner/liquidation_scanner.py` | Silent no-op outside API context | 🟡 Low-Med | Return error ScannerResult |
| 6 | `signals/signal_generator.py` | HMM fit once, never refreshed | 🟡 Low-Med | Add time-based re-fit |
| 7 | `scanner/volume_scanner.py` | Late import in hot path `_dict_to_candle` | 🟡 Low | Move to module level |
| 8 | `risk/circuit_breaker.py` | List comprehension pruning on every trade | 🟡 Low | Use `deque` |
| 9 | `core/risk_gate.py` | F-string logging style | 🔵 Info | Use %-style |
| 10 | `scanners/scalp_scanner.py` | Invalid import paths post-restructure | 🟡 Low | Fix or remove |
| 11 | `core/key_vault.py` | No AEAD associated data binding | 🔵 Info | Bind ciphertext to user_id |
| 12 | `alerts/` module | Missing unit tests for patched bugs | 🟡 Low | Add `test_alerts.py` |

---

*Next review: 2026-05-12 09:00*
