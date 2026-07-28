---
name: coinscopeai-trading-rules
description: CoinScopeAI Trading & Risk Rules. Use this skill to understand the risk gate thresholds, kill switch states, position sizing logic, regime detection, validation phase rules, and the primary goal of capital preservation.
---

# CoinScopeAI Trading & Risk Rules

**Last updated:** 2026-05-19 | **Locked:** PCC v2 §8, commit `3d6362d` (2026-05-01)

---

## Risk Gate Thresholds (CANONICAL — LOCKED)

> ⚠️ These are immutable during the validation phase. Any deviation is a critical violation.

| Threshold | Value | Enforcement |
|---|---|---|
| `MAX_LEVERAGE` | **10x** | NOT 20x — old docs showing 20x are wrong and superseded |
| `MAX_OPEN_POSITIONS` | **5** | Revised 2026-05-03 from =3 (see decision-log `max-open-positions-revised-3-to-5`) |
| `MAX_DRAWDOWN_PCT` | **10%** | From peak — triggers kill switch |
| `MAX_DAILY_LOSS_PCT` | **5%** | 24h rolling — halts all trading |
| `POSITION_HEAT_CAP_PCT` | **80%** | Total deployed capital cap |

**Guardrail script:** `python3 scripts/risk_threshold_guardrail.py` — scans entire codebase for violations.

---

## Kill Switch

- **Armed state:** Halts all new entries; closes open positions if thresholds breached
- **Disarmed state:** Normal trading resumes, subject to risk gate checks
- **Manual engage:** `curl -X POST http://localhost:8001/kill-switch -d '{"engage": true, "reason": "manual"}'`
- **Manual disengage:** `curl -X POST http://localhost:8001/kill-switch -d '{"engage": false, "reason": "manual"}'`
- Kill switch state persists across restarts — intentional design

---

## Position Sizing

Calculated via `/position-size` endpoint, using:

- Current account equity
- Symbol volatility and recent performance
- Stop-loss distance for the specific setup
- Kelly fraction with hard cap per-trade

---

## Regime Detection

The engine classifies market conditions into four regimes:

| Regime | Description | Design Token |
|---|---|---|
| **Trending** | Strong directional movement — trend-following strategies favored | Emerald |
| **Mean-Reverting** | Range-bound — oscillators and S/R levels favored | Cyan |
| **Volatile** | High fluctuations — wider stops, reduced position sizes | Amber |
| **Quiet** | Low vol/volume — often precedes breakout | Muted |

Regime confidence threshold: `MIN_REGIME_CONFIDENCE=0.55` (signals suppressed below this).

---

## Validation Phase Rules (active through ~May 31, 2026)

**Blocked during validation:**

- Any canonical risk threshold change
- Setting `BINANCE_TESTNET=false`
- Removing or bypassing any circuit breaker
- Retraining or replacing ML artifacts
- Changing order submission semantics

**All trading:** Binance Testnet only (`testnet.binancefuture.com`).

**VPS status:** ✅ Live — AWS ap-southeast-1, `ubuntu@ip-172-31-15-30`, `/opt/coinscopeai/`. `MAX_OPEN_POSITIONS=5` and `MAX_LEVERAGE=10` confirmed on VPS 2026-05-19. COI-68 Done.

---

## Bundled Scripts

| Script | Purpose |
|---|---|
| `python3 scripts/risk_threshold_guardrail.py` | Scan codebase for threshold violations |
| `python3 scripts/drift_detector.py` | Check canonical docs for token consistency |
| `./scripts/daily_status.sh` | Morning engine brief (all 6 endpoints) |

---

## Primary Goal

**Capital Preservation** is the overarching priority. Profit generation is secondary to protecting the initial account balance. Every gate, threshold, and kill switch exists to enforce this.
