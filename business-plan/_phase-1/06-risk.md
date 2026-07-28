# 06 — RISK (Phase 1)

**Purpose:** Translate the engine's risk envelope (PCC v2 G1–G4 + §8 Capital Cap; canonical 5 tokens 10x / 10% / 5% / 5 / 80%) into the *business-plan layer* — i.e., decide what we are **allowed to claim** and what we **must explicitly not claim** at each risk-state.
**v1 reference:** `12-risk-compliance-trust.md`, `_data/operations/Production_Candidate_Criteria_v2.md`, `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`.
**Phase 1 outcome:** A risk-state → claim-allowance matrix (signed by founder), plus the runbook for what happens when a gate would force a downgrade.

---

## Why RISK matters specifically for CoinScopeAI

For most software companies "risk" is a section in a security questionnaire. For CoinScopeAI it is the *core product narrative* — the engine's reason for being is to enforce a risk envelope before the trader does anything. Three Phase-1 reasons it must be planned at the business-plan layer:

1. **Risk numbers are public.** The five canonical tokens (10x leverage / 10% drawdown / 5% daily loss / 5 max positions / 80% heat) are referenced in copy, docs, and the bot intro. If the business plan and the engine ever diverge on these numbers, we have a credibility crisis.
2. **§8 Capital Cap is a sales surface, not just an ops surface.** The promise "we will not let you ramp real capital until G1–G4 + §8 Phase 1 are open" is a *trust feature*. It must be readable, dateable, and verifiable.
3. **Dependency risk is business risk.** Binance USDT-M is the only venue in P0/P1. CoinGlass, Tradefeeds, CoinGecko are upstream. Their outage is *our* outage. The business-plan layer needs to commit to a posture (incident comms, refund policy, status page integration) before paid acquisition.

---

## Required subsections

1. **Canonical risk-token table** — the 5 numbers, their authoritative source, and the rules for changing them.
2. **PCC v2 + §8 in plain English** — the gate map and what each gate means for capital exposure.
3. **Risk-state matrix** — Validation / Narrow Ship / Vendor Expansion / Desk Full → what may be claimed, what must not.
4. **Vendor / dependency risk posture** — what we say publicly when an upstream provider fails.
5. **Real-capital decision flow** — the runbook from "user is in cohort" to "user has approved real-capital usage".
6. **Downgrade runbook** — what happens to claims and to product behavior if a gate would force a state downgrade.

---

## Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Canonical risk-token table (this doc) | MD | Founder + Eng lead |
| PCC v2 public summary (cross-listed in TRUST T-2) | MD → live page | Founder |
| Risk-state claim allowance matrix | MD, in this file | Founder |
| Real-capital approval runbook | MD in `_data/operations/` | Founder + Eng lead |
| Vendor incident comms template | MD in `_data/operations/` | Ops + Founder |
| Downgrade runbook | MD in `_data/operations/` | Founder + Eng lead |

---

## 1. Canonical risk tokens (single source of truth)

| Token | Value | Authoritative source | Rule for change |
|---|---|---|---|
| Max leverage | **10x** per position | PCC v2 §8 Capital Cap (locked 2026-05-01) | Change requires Decision Log entry + memory `feedback_risk_threshold_reconciliation` patch in same pass |
| Max drawdown | **10%** account, hard stop | engine config + PCC v2 | Same |
| Daily loss limit | **5%** rolling 24h, halts trading | engine config + PCC v2 | Same |
| Max open positions | **5** concurrent | engine config | Same |
| Position heat cap | **80%** per position | engine config | Same |

**Public copy rule:** every public reference to any of these numbers must be paired with the disclaimer: *"Testnet only. 30-day validation phase. No real capital."* during P0/P1. After §8 Phase 1 opens, the disclaimer may be reworded to specify the live phase.

---

## 2. PCC v2 + §8 in plain English (the gate map)

| Gate | What it requires | What it gates | Phase-1 status |
|---|---|---|---|
| **G1** | Engine + risk envelope green on testnet for the validation window | Cohort can run the full Scan → Score → Gate → Size loop on testnet | In progress (P0 cohort) |
| **G2** | Vendor reliability (Binance + supporting providers) hits the documented uptime / drift thresholds | Public claim allowance widens (e.g., "validated on Binance USDT-M") | Pending |
| **G3** | Operational runbooks (incident, downgrade, vendor failure) are live + rehearsed | Status page, paid acquisition allowance | Pending |
| **G4** | Cohort exit memo signed (positive + transparent) | "30-day cohort closed" claim allowed | Pending |
| **§8 Capital Cap, Phase 1** | All G1–G4 + per-user manual approval + small-notional cap | Real capital allowed under cap | Closed in P1 (opens conditionally late-Jul / Aug) |
| **§8 Capital Cap, Phase 2+** | Documented widening of cap with telemetry-justified ramp | Larger notional, pre-Desk Preview surface | Out of Phase 1 (P2+) |

---

## 3. Risk-state → claim allowance matrix

This is the core deliverable of the Phase 1 RISK workstream.

| Risk-state (engine) | Public claim **allowed** | Public claim **disallowed** | Default disclaimer |
|---|---|---|---|
| **Validation (now → cohort close)** | "Validated on testnet"; "30-day validation phase pending"; "Risk gate enforces 10x / 10% / 5% / 5 / 80%"; "Built around a documented Production Candidate Criteria"; "Cohort cap of 40" | "Live trading"; "production-ready"; "battle-tested"; "proven"; any P&L or win-rate; "trade with real capital" | *"Testnet only. 30-day validation phase. No real capital."* |
| **Narrow Ship (post-cohort, pre-§8 Phase 1)** | All of Validation + "30-day cohort closed"; "Cohort exit memo published"; "Available to self-directed traders for testnet validation"; pricing mentioned with the testnet caveat | "Live trading on real capital"; copy implying capital-at-risk decisions | *"Risk-gated. Validation cohort closed [date]. Real-capital usage gated by §8 Capital Cap, currently closed."* |
| **§8 Phase 1 open (small-notional, manual approval)** | All previous + "Real-capital usage available under documented Capital Cap, with per-user manual approval"; specific notional cap can be stated | Anything implying open / unrestricted real-capital usage; any return claims without methodology page; "institutional-grade" still disallowed | *"Real-capital usage gated by §8 Capital Cap Phase 1 (small-notional, manual approval). Risk Disclosure required."* |
| **§8 Phase 2+ (widening)** | Conditional on Phase-2 charter — out of Phase 1 scope | Same | TBD |
| **Desk Full v2 (Phase 5 entry, Mar–May 2027)** | "Desk-grade" claims allowed if cohort + §8 Phase 2+ evidence supports them; "institutional-grade" still requires explicit founder + counsel sign-off | Out of Phase 1 scope | TBD |

**Implication for Phase 1 copy:** *all* P0/P1 marketing surfaces operate under either the **Validation** or **Narrow Ship** rows. Anything else is premature.

---

## 4. Vendor / dependency risk posture

| Dependency | Failure impact | Phase 1 public posture |
|---|---|---|
| Binance USDT-M (price/exec) | Hard outage = no signals, no execution | Status page incident; pause new-user onboarding; cohort comms via Telegram within 15 min |
| CoinGlass | OI/liquidation/funding feed degraded | Engine continues with degraded signals; UI marks degraded state; incident logged |
| Tradefeeds | Macro/news feed degraded | Same — degrade visibly |
| CoinGecko | Spot reference degraded | Engine continues; no UI flagging required |
| Claude (alerting / Scoopy) | Bot quality degraded | Bot replies fall back to deterministic templates; incident logged |

**Rule:** every dependency listed publicly (T-12 in TRUST) must have a corresponding incident comms template *before* it is listed. Listing a dependency without its incident template is worse than not listing it.

---

## 5. Real-capital decision flow (Phase 1 runbook)

Each cohort member who wants to move from testnet to real-capital under §8 Phase 1 must pass the following ordered checks. **No automation. No batch.**

1. Cohort exit memo signed by founder (cohort-wide gate).
2. Per-user check: G1–G4 attestation written + signed for that user's account.
3. Per-user check: account profile passes jurisdictional rules (US-blocked at signup; UAE/MENA + global EN allowed).
4. Per-user check: Risk Disclosure v1 + Privacy Policy v1 signed (recorded).
5. Per-user check: requested notional ≤ §8 Phase 1 cap.
6. Founder manual approval (recorded with date + reason).
7. Engine flag flipped per-account; Telegram + dashboard banner shows new state.

**Rollback:** any breach of any token (10x / 10% / 5% / 5 / 80%) on a real-capital account triggers immediate flag-flip back to testnet for that account, plus an internal incident.

---

## 6. Downgrade runbook (when a gate would force a state downgrade)

| Trigger | Action | Public posture |
|---|---|---|
| Vendor uptime falls below G2 threshold | Engine downgrades signal display; status page incident opened | "Operating under degraded vendor [X]"; no claim widening |
| Cohort exit memo not signed by deadline | Narrow Ship launch deferred; pricing pages remain in "Validation" copy | "Cohort window extended"; honest |
| Real-capital incident (token breach) on §8 Phase 1 user | Account flag rolled back to testnet; incident published if material | Counsel + founder review whether to continue §8 Phase 1 admissions |
| Repeated vendor failure (≥2 in 30d) | Vendor placed on watch list; no new dependency added that touches it | "Vendor X is on our internal reliability watch — see status page" |

---

## Decisions required (Phase 1)

| # | Decision | Recommendation | Owner |
|---|---|---|---|
| R-1 | Lock the canonical risk-token table | Yes — exactly as listed; aligned with PCC v2 §8 | Founder |
| R-2 | Lock the risk-state claim allowance matrix | Yes — as drafted; counsel pre-review on Validation + Narrow Ship rows | Founder + counsel |
| R-3 | Real-capital approval flow: manual or batch | **Manual, per-user, no batch** in Phase 1 | Founder |
| R-4 | Vendor incident comms cadence | Status page within 15 min; Telegram cohort alert within 30 min | Ops + Founder |
| R-5 | Public publication of PCC v2 summary | Yes, by P0 invite-out (cross-listed TRUST T-2) | Founder |
| R-6 | Downgrade runbook authority | Founder may downgrade unilaterally; upgrade requires founder + Eng lead + counsel where copy changes | Founder |

---

## Failure modes to avoid

- **Numbers drift between engine, copy, and docs.** The token table is one source of truth; any change touches engine config, public copy, docs, master prompt, and memory in the same pass (per `feedback_risk_threshold_reconciliation`).
- **"§8 is closed" buried in fine print.** During P0/P1 this is a *headline* trust signal. Make it loud.
- **Vendor risk glossed over.** Failing to acknowledge dependency risk publicly is read as either ignorance or dishonesty. Acknowledging it (with incident templates ready) is a trust signal.
- **Auto-promote to real capital.** Even a single "we'll auto-enable for cohort members who pass" decision contradicts the §8 promise. Manual or nothing.
- **Quiet downgrades.** A degraded vendor without a public incident is a bigger trust hit than a noisy outage with a clear status page entry.

---

## Tasks (canonical — user-supplied 2026-05-04; see `08-task-backlog.md` for the full four-field backlog)

**NOW**

- `[DOC] RISK — Business Risk Register v1`
- `[DOC] RISK — Provider Dependency Risk Matrix`
- `[DOC] RISK — Operational Failure Scenario Map`
- `[DOC] RISK — Exchange Outage Business Response Plan`
- `[RISK] RISK — Product Promise vs Risk Exposure Review`

**NEXT**

- `[DOC] RISK — Drawdown and Reputation Risk Framework`
- `[DOC] RISK — Billing and Churn Risk Review`
- `[DOC] RISK — Counterparty and Vendor Risk Policy`
- `[OPS] RISK — Risk Review Cadence`
- `[METRICS] RISK — Leading Risk Indicators Dashboard`

**LATER**

- `[DOC] RISK — Scale-Stage Risk Governance Model`
- `[DOC] RISK — External Audit Readiness Requirements`
