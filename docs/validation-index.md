# Validation Index

> **Measured:** 2026-07-28 | **Status:** Partial — coverage numbers now pinned

## Code / Pytest

| Module | Target | Measured | Status | Notes |
|---|---|---|---|---|
| `engine/signals/scoring_fixed.py` | ≥ 80% | **84%** | 🟢 | Missing: `score_liquidity` (proxy mismatch) |
| `services/paper_trading/safety.py` | ≥ 90% | **97%** | 🟢 | 5 missing lines: exception/kill-switch edge cases |
| `risk_management/risk_gate.py` | ≥ 90% | **0%** | 🔴 | No tests import this module |
| `risk_management/hmm_regime_detector.py` | ≥ 70% | **0%** | 🔴 | Used by `master_orchestrator` (also 0%) |
| `risk_management/kelly_position_sizer.py` | ≥ 70% | **0%** | 🔴 | Used by `master_orchestrator` |
| `risk_management/regime_features.py` | ≥ 70% | **0%** | 🔴 | Used by `train_hmm_regime.py` script |
| `risk_management/regime_predictor.py` | ≥ 70% | **0%** | 🔴 | Used by `engine/api.py` (also 0%) |
| `engine/core/scale_up_manager.py` | ≥ 70% | **68%** | 🟡 | 2% short; profile-progression branches uncovered |
| `services/paper_trading/order_manager.py` | ≥ 70% | **79%** | 🟢 | Close-order edge cases |
| `services/market_data/models.py` | ≥ 70% | **99%** | 🟢 | Near-complete |
| `services/market_data/event_bus.py` | ≥ 70% | **86%** | 🟢 | Handler-exception path uncovered |
| `services/market_data/alpha/base.py` | ≥ 70% | **96%** | 🟢 | Well covered |
| **Total repo coverage** | — | **38%** | 🔴 | 6,168 of 9,889 statements missed |

## System / Integration

| Area | Status | Evidence |
|---|---|---|
| Alert path (Telegram + dashboard) | 🔴 Red | No smoke test — see issue #39 |
| Invariant matrix | 🟢 Green | `scripts/invariant_matrix_check.py` passes |
| Evidence gate | 🟢 Green | CI job runs on every PR |
| Directory boundaries | 🟡 Yellow | `tests/test_directory_boundaries.py` partially passing |

## Validation Runs

| Run | Date | Type | Status |
|---|---|---|---|
| WFV | 2026-05-13 | Walk-forward validation | See `docs/validation/runs/2026-05-13/wfv.md` |
| CPCV | 2026-05-13 | Combinatorial purged CV | See `docs/validation/runs/2026-05-13/cpcv.md` |

## Outstanding Gaps

1. **Risk management package (0%)** — The `risk_management/` directory is imported by production code (`engine/core/master_orchestrator.py`, `engine/api.py`) but has zero test coverage. This is the highest-priority gap.

2. **Master orchestrator + API (0%)** — Integration layer that wires `risk_management` → `engine` → `exchange` is completely untested.

3. **Liquidity proxy calibration** — `engine/signals/scoring_fixed.py::score_liquidity` is uncovered because offline validation and live trading use different spread representations. Tracked in issue #52.

4. **Scale-up manager (68%)** — Two percentage points below threshold.

## Related Documents

- `docs/testing-strategy.md` — Full coverage table with missing-branch details
- `docs/validation/invariant-matrix.md` — Invariant matrix (I13, I14, I5)
- `docs/validation/p0-evidence-pack.md` — Evidence pack §0.1, §0.4, §5
