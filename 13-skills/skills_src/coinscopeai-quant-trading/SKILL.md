---
name: coinscopeai-quant-trading
description: |
  Guidelines for reading and writing Python quantitative trading algorithms in
  the CoinScopeAI project. Use this skill when implementing scanners, signal
  generators, regime detectors, position sizers, backtests, or risk components.
---

# CoinScopeAI Quantitative Trading Algorithms

## Scope

This skill applies whenever you create or modify Python code that:
- Generates or scores trading signals
- Detects market regimes
- Sizes positions or manages risk
- Backtests strategies
- Integrates exchange data (Binance Futures, REST, WebSocket)

## Architecture principles

1. **Minimal, well-tested components**
   - Add a single function or class that solves one quant problem well.
   - Expose clear inputs/outputs, add a docstring, and include a runnable example or test.
   - Avoid premature abstraction.

2. **Use project conventions and existing modules**
   - Import from `coinscope_trading_engine` using relative imports.
   - Reuse `Candle`, `SignalDirection`, `ScannerHit`, `TradeSetup`, `PositionSize`, and `RiskGate`.
   - Do not invent parallel data structures.

3. **Vectorized and deterministic numeric code**
   - Use `numpy`/`pandas` for indicator math.
   - Set `np.random.seed` in tests.
   - Avoid Python loops over price bars.

4. **Respect locked risk and validation rules**
   - Do not change `MAX_LEVERAGE=10`, `MAX_OPEN_POSITIONS=5`, `MAX_DAILY_LOSS_PCT=5`, or `MAX_DRAWDOWN_PCT=10`.
   - New algorithms must pass through `RiskGate`.
   - Default to Binance Testnet mode.

## Common patterns

### Signal generator / scanner

- Subclass `BaseScanner` in `coinscope_trading_engine/scanner/` or add a function in `coinscope_trading_engine/signals/`.
- Emit `ScannerHit` objects:
  ```python
  ScannerHit(
      scanner="MyScanner",
      symbol=symbol,
      direction=SignalDirection.LONG,
      strength=HitStrength.MEDIUM,
      score=65.0,
      reason="rsi oversold + volume spike",
  )
  ```
- Keep scanner logic focused; let `ConfluenceScorer` aggregate.

### Regime detector

- Place in `coinscope_trading_engine/intelligence/`.
- Accept returns/volatility arrays.
- Return `{"regime": "bull"|"bear"|"chop", "confidence": float}`.
- Fit on historical data; do not refit in production without validation approval.

### Position sizer

- Use `KellyRiskController` or `PositionSizer`.
- Cap risk per trade, cap total position, reduce size in drawdown.
- Return USD size or a `PositionSize` dataclass.

### Backtest component

- Add a script in `research/` or a test in `coinscope_trading_engine/tests/`.
- Use `TradeJournal` for logging trades.
- Report win rate, Sharpe, max drawdown, profit factor.

## Template for a new module

```python
"""
<one-line purpose>
"""
from __future__ import annotations

import numpy as np


class MyQuantComponent:
    """Docstring describing inputs, outputs, and assumptions."""

    def __init__(self, param: float = 1.0) -> None:
        self.param = param

    def compute(self, prices: np.ndarray) -> dict:
        """Return a dict with regime/signal/score keys."""
        return {"signal": 0.0}
```

## Quality checklist

- [ ] Input validation and guard clauses for empty/zero-length arrays.
- [ ] Unit test with synthetic data covering LONG, SHORT, and NEUTRAL cases.
- [ ] No unguarded `assert` in library code; use explicit `ValueError`/`RuntimeError`.
- [ ] All secrets loaded from `settings` or environment, never hard-coded.
- [ ] Type hints on public functions/classes.
