# Testing Strategy

> **Measured:** 2026-07-28 | **Runner:** `pytest --cov` across `tests/`
> **Total repo coverage:** 38% (9,889 statements, 3,721 hit)

## Coverage Targets vs. Measured

| Module (canonical name) | Actual file path | Target | Measured | Status |
|---|---|---|---|---|
| Scoring engine | `engine/signals/scoring_fixed.py` | ≥ 80% | **84%** | 🟢 |
| Circuit breaker / Safety gate | `services/paper_trading/safety.py` | ≥ 90% | **97%** | 🟢 |
| Risk management (RiskGate) | `risk_management/risk_gate.py` | ≥ 90% | **0%** | 🔴 |
| Risk management (HMM regime detector) | `risk_management/hmm_regime_detector.py` | ≥ 70% | **0%** | 🔴 |
| Risk management (Kelly sizer) | `risk_management/kelly_position_sizer.py` | ≥ 70% | **0%** | 🔴 |
| Risk management (Regime features) | `risk_management/regime_features.py` | ≥ 70% | **0%** | 🔴 |
| Risk management (Regime predictor) | `risk_management/regime_predictor.py` | ≥ 70% | **0%** | 🔴 |
| Scale-up manager | `engine/core/scale_up_manager.py` | ≥ 70% | **68%** | 🟡 |
| Order manager | `services/paper_trading/order_manager.py` | ≥ 70% | **79%** | 🟢 |
| Event bus | `services/market_data/event_bus.py` | ≥ 70% | **86%** | 🟢 |
| Alpha generators (base) | `services/market_data/alpha/base.py` | ≥ 70% | **96%** | 🟢 |
| Market data models | `services/market_data/models.py` | ≥ 70% | **99%** | 🟢 |

## Key Findings

1. **`services/paper_trading/safety.py` (97%)** — The safety gate and circuit breaker layer is well-tested. The 5 missing lines are edge-case branches (kill-switch file I/O error handling, exception paths).

2. **`engine/signals/scoring_fixed.py` (84%)** — Core scoring logic is covered. Missing lines are the `score_liquidity` function (lines 236–253) and error-handling branches (lines 288–296). The liquidity-scoring gap is notable because the validator uses a proxy (`spread = high − low`) while live code expects `bid_ask_spread` — see issue #52.

3. **`risk_management` package (0%)** — **Critical gap.** The entire `risk_management/` package shows 0% coverage because no tests import it. However, it IS used in production by `engine/core/master_orchestrator.py` and `engine/api.py` (which also show 0% coverage). The tests instead exercise the newer `services/paper_trading/safety.py` layer. This creates a coverage blind spot for the orchestrator → risk gate path.

4. **`engine/core/scale_up_manager.py` (68%)** — Just below the 70% threshold. Missing lines cover the progression-to-max-profile logic and error paths.

## Missing Branches (high-impact uncovered code)

| File | Lines | What they do |
|---|---|---|
| `risk_management/risk_gate.py` | 12–345 | Entire RiskGate class (stop-loss, take-profit, Kelly sizing, circuit breakers) |
| `risk_management/hmm_regime_detector.py` | 12–174 | EnsembleRegimeDetector (used by master_orchestrator) |
| `risk_management/kelly_position_sizer.py` | 12–115 | KellyRiskController (used by master_orchestrator) |
| `risk_management/regime_predictor.py` | 12–229 | HMMRegimePredictor (used by engine/api.py) |
| `engine/signals/scoring_fixed.py` | 236–253 | `score_liquidity` — live-vs-validator proxy mismatch site |
| `engine/core/scale_up_manager.py` | 100–119 | Profile progression logic |

## CI Coverage Gate (future)

Once the Red modules above are brought above 70%, add this to `.github/workflows/ci.yml`:

```yaml
- name: Run tests with coverage
  run: |
    python3 -m pytest tests/ \
      --cov=risk_management --cov=engine --cov=services \
      --cov-fail-under=70 \
      --cov-report=term-missing
```

## Related Issues

- #40 — This issue (pinning coverage numbers)
- #52 — Liquidity-proxy bias measurement (`score_liquidity` gap)
- #34 — Duplicate-position rejection (safety.py)
- #58 — Gate-decision journaling persistence (safety.py)
