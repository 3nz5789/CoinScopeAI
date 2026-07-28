# 14 — Risk, Compliance, and Safeguards

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/12-risk-compliance-trust.md` v1 LOCKED (41-entry risk register, anti-probability framing); `business-plan/_data/legal/Counsel_Brief_v2.md`; `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`

---

## 1. Folder purpose

This folder defines **the business-level risk, compliance sensitivity, and safeguard structure for CoinScopeAI**. Its job is to keep leadership from making growth, pricing, messaging, or product decisions that outrun operational safety or legal clarity.

It answers four operator questions:

1. **What can break the business, and which signs come first?** — `business-risk-register.md`
2. **What are we currently assuming that counsel needs to verify?** — `compliance-assumptions.md`
3. **What guardrails sit between the business and a bad outcome — and what unlocks each gate?** — `safeguards-framework.md`
4. **What specific questions need to go to counsel?** — `regulatory-question-list.md`

It is **operator-grade**, not legal-grade. Final legal conclusions live in counsel-reviewed documents under `_data/legal/`. This folder is the discipline layer that determines what reaches counsel, what doesn't reach the buyer until counsel clears it, and what business decisions are blocked until specific evidence accumulates.

---

## 2. File list

| File | What it contains |
|---|---|
| `README.md` | This file — folder map, dependencies, reading order, open questions |
| `business-risk-register.md` | Operator-grade business risk view (8 categories), severity + status framing, mitigation direction, early warning indicators |
| `compliance-assumptions.md` | Compliance-sensitive assumptions currently in force, counsel-review areas, product/billing/claims/comms/jurisdiction assumptions, the "do not assume without validation" list, planning posture under uncertainty |
| `safeguards-framework.md` | Safeguard philosophy, business/product/operational safeguards split, gating logic, what must exist before more aggressive monetization or growth, breach-escalation logic, what not to relax too early |
| `regulatory-question-list.md` | Structured questions for counsel/compliance, organized by area (positioning / automation / signals / billing / claims / jurisdiction / launch-timing) |

---

## 3. Why this folder matters

CoinScopeAI's business model places **risk discipline on the same priority footing as growth and product**. The reasons are structural:

- The validation-phase posture ("testnet only, no real capital, gated by §8") is itself the business model's defense against existential risks. Letting it slip would invalidate the moat.
- The cohort is the marketing. A single mishandled risk event during P1 (regulatory inquiry, vendor outage handled poorly, brand-voice violation, security concern) damages cohort signal and downstream P2 funnel.
- Sole-prop operating posture with named-founder visibility means founder mistakes are existential, not abstract. Risk discipline is the founder's discipline, by structure.
- Counsel-uncertainty in crypto-futures-AI tooling is real and ongoing. Assumptions that look reasonable today may be wrong; the discipline is to track them as assumptions, not facts, and validate them before scale-relevant decisions hinge on them.

The corollary: **a slower, more disciplined posture is not a constraint — it is the strategy**. This folder makes that posture executable for the founder running P1 and pre-P2 planning.

---

## 4. Dependencies on prior folders

| Source | What we inherit |
|---|---|
| `01-executive-summary/business-model-summary.md` | Custody-free; testnet-first; US-blocked-at-signup; named-founder; UAE sole prop |
| `01-executive-summary/strategic-priorities.md` | Priority 1 (validation pass); Priority 3 (anti-overclaim); Priority 5 (vendor runbooks); Priority 6 (entity decision); Priority 8 (testnet hard gate) |
| `02-company-overview/strategic-constraints.md` | Real-capital deployment is gated; no production-ready claim until §8 |
| `04-icp-and-segmentation/secondary-icps.md` | Anti-ICP segments; explicit decline patterns |
| `05-positioning/positioning-statement.md` | Anti-claim list; locked positioning lines |
| `06-product-strategy/feature-prioritization.md` | What ships at MVP / Beta / Scale; readiness gates |
| `07-packaging-and-pricing/pricing-strategy.md` | Pricing locks ≥6 months post-validation; founder-cohort time-bounded |
| `07-packaging-and-pricing/trial-and-discount-policy.md` | Refund policy; anti-stacking rules |
| `08-go-to-market/gtm-strategy.md` | Founder-led; no paid acquisition pre-CAC validation; deferred channels |
| `08-go-to-market/launch-plan.md` | Stage gates; stop-the-line conditions inherited from §14 |
| `08-go-to-market/trust-first-growth.md` | Trust signals; review/checkpoint cadence |
| `12-onboarding-and-activation/` | Sub-$5k routing; US-block at signup; exchange-connection scope discipline |
| `13-support-and-trust-ops/trust-framework.md` | Trust gaps + building priorities |
| `13-support-and-trust-ops/public-claims-guardrails.md` | Forbidden claims; review process |
| `13-support-and-trust-ops/incident-communications.md` | Incident comms templates; what cannot be claimed |
| `business-plan/12-risk-compliance-trust.md` | **§12 v1 LOCKED** — 41-entry risk register; severity + status framing |
| `business-plan/14-launch-roadmap.md` | Phase gates; stop-the-line conditions |
| `business-plan/16-scenario-planning.md` | Anti-probability scenario framing |
| `business-plan/_data/operations/Production_Candidate_Criteria_v2.md` | PCC v2 G1–G4 + §8 Capital Cap |
| `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md` | Vendor incident scenarios |
| `business-plan/_data/legal/Counsel_Brief_v2.md` | Counsel engagement scope + open items |
| `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` | Tools-not-advice posture (counsel-review pending) |
| `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md` | User-facing risk disclosure (counsel-review pending) |

This folder is a Wave 2 **operator restatement** of the locked §12 risk register, the counsel brief, and the validation-phase posture. Where the working notes give the entry-by-entry detail, this folder gives the strategic shape and the discipline rules.

---

## 5. Recommended reading order

For a founder reviewing risk and compliance posture pre-P1:

1. `README.md` (this file) — orientation
2. `business-risk-register.md` — what can break, in what order to worry
3. `safeguards-framework.md` — what guards each risk
4. `compliance-assumptions.md` — what we are assuming that needs validation
5. `regulatory-question-list.md` — what to send to counsel and when
6. `_data/legal/Counsel_Brief_v2.md` — when activating the engagement

For a counsel onboarding to the engagement:

1. `_data/legal/Counsel_Brief_v2.md` — the engagement scope
2. `regulatory-question-list.md` (this folder) — the prioritized question set
3. `compliance-assumptions.md` (this folder) — what we have been assuming
4. `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` and `Risk_Disclosure_v0_DRAFT.md` — current draft posture

For a contractor or advisor reviewing the business plan from a risk angle:

1. `business-risk-register.md` (this folder)
2. `safeguards-framework.md` (this folder)
3. `business-plan/12-risk-compliance-trust.md` (full §12 v1 LOCKED register)
4. `business-plan/16-scenario-planning.md` (anti-probability scenarios)

---

## 6. Open questions

Carried forward from §12 + Counsel Brief plus introduced by Wave 2.

1. **DECISION NEEDED — Counsel selection and engagement start date.** Per Counsel Brief F-9. Pre-P1.
2. **DECISION NEEDED — Post-validation entity restructure path.** DMCC FZE / mainland LLC / other. Per Strategic Priority 6. Post-P0 pass.
3. **DECISION NEEDED — Risk Disclosure language final.** Pre-P1 launch (gates user access via ToS-gate).
4. **DECISION NEEDED — No Investment Advice memo final version.** Pre-P1 launch.
5. **DECISION NEEDED — "Institutional-grade" usage scope.** Counsel sign-off on approved usages per `13-support-and-trust-ops/public-claims-guardrails.md` §6.
6. **REQUIRED INPUT — Counsel review of incident comms templates** before P1.
7. **REQUIRED INPUT — Counsel review of refund policy language** (single-use per account / email / payment method).
8. **REQUIRED INPUT — Counsel review of US-block enforcement language** at signup.
9. **REQUIRED INPUT — Vendor failure-mode runbook dry-run** before P1.
10. **REQUIRED INPUT — Brand-voice review process** documented and active before any external surface ships.
11. **ASSUMPTION — UAE sole-prop posture is sufficient through validation phase.** Validate at counsel engagement start.
12. **ASSUMPTION — Below-VAT-threshold posture (no VAT collection at v1) is correct.** Validate at counsel engagement start.
13. **ASSUMPTION — Tools-not-advice positioning holds across MENA + global EN jurisdictions.** Validate at counsel engagement start.
14. **OPEN — US licensure path** (deferred per Strategic Priority Deferral D2; revisit post-P5).
15. **OPEN — GCC cross-border VAT obligations** post-MENA expansion. Tracking per §12 R-003.
16. **OPEN — Crypto payments acceptance.** Deferred per `07-packaging-and-pricing/trial-and-discount-policy.md`. Revisit post-v2 with counsel.

---

## 7. Cross-references

- §12 v1 LOCKED canonical: `business-plan/12-risk-compliance-trust.md`
- §14 v1 LOCKED launch roadmap: `business-plan/14-launch-roadmap.md`
- §16 v1 LOCKED scenario planning: `business-plan/16-scenario-planning.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- No Investment Advice memo: `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`
- Risk Disclosure: `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications: `business-plan/13-support-and-trust-ops/incident-communications.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
