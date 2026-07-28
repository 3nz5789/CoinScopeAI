# 13 — Support and Trust Operations

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_support/` (operating model, SLA framework, ticket routing, issue taxonomy, inbox workflow); `business-plan/09-brand-messaging.md`; `business-plan/10-operations-support.md`

---

## 1. Folder purpose

This folder defines **how CoinScopeAI earns and maintains trust operationally**. It treats trust not as a marketing message but as a continuous operational practice — built and tested every time a user files a support ticket, sees a public claim, or experiences an incident.

It answers four operator questions:

1. **How do we run support at this stage?** — `support-operating-model.md`
2. **What does trust mean for this product, and how do we build it?** — `trust-framework.md`
3. **What can we say in public, and what must we never say?** — `public-claims-guardrails.md`
4. **When something breaks, how do we communicate?** — `incident-communications.md`

It is **operator-grade**, not legal-grade. Final language for legal documents (Terms, Privacy, No-Investment-Advice memo, Risk Disclosure) lives in `_data/legal/` under counsel review. This folder gives the founder + ops the operational discipline that makes those documents defensible in practice.

---

## 2. File list

| File | What it contains |
|---|---|
| `README.md` | This file — folder map, dependencies, reading order, open questions |
| `support-operating-model.md` | Philosophy, recommended model for current stage, channels, escalation logic, support boundaries, billing/support separation, exchange/provider issue handling, who needs higher-touch support, maturity progression |
| `trust-framework.md` | Trust principles, definition for this category, signals to build, product/operational/brand trust split, testnet-first as trust amplifier, current trust gaps, building priorities |
| `public-claims-guardrails.md` | Approved claim categories, risky claims to avoid, performance language, automation language, "institutional-grade" usage, AI claims, review process, good vs. bad phrasing examples |
| `incident-communications.md` | Communication philosophy, incident categories, internal vs. external rules, comms priorities for each incident type, templates, what cannot be delayed, what cannot be claimed |

---

## 3. Why this folder matters

For a trust-sensitive trading product running in validation phase with a 40-user cohort cap, **operational discipline is the entire moat**. A single mishandled incident, a single overclaim in support copy, a single delayed status-page update can collapse months of accumulated cohort trust faster than any marketing investment can rebuild.

Three failure modes destroy this:

- **Support failure** — a user with a real-capital concern (even a misunderstanding) sees a delayed or careless response; the cohort talks about it.
- **Claim drift** — a marketing surface or support reply uses "production-ready" / "guaranteed" / "outperforms" language; the brand-voice moat dies in one screenshot.
- **Incident-comms failure** — an exchange outage degrades signals; we do not say so quickly enough; the user discovers it themselves and concludes the product is unreliable AND opaque.

Each is independently fatal. Each is also **structurally avoidable** if the support workflow, the claim guardrails, and the incident comms plan are pre-committed and rehearsed. This folder is that pre-commitment.

---

## 4. Dependencies on prior folders

| Source | What we inherit |
|---|---|
| `01-executive-summary/business-model-summary.md` | Custody-free; testnet-first; trust posture is structural |
| `01-executive-summary/strategic-priorities.md` | Priority 3 (anti-overclaim); Priority 7 (support stand-up); Priority 8 (testnet hard gate); Priority 5 (vendor runbooks) |
| `02-company-overview/strategic-constraints.md` | UAE sole prop; named founder; no production-ready claim until §8 passes |
| `04-icp-and-segmentation/primary-icp.md` | P1 Omar trust requirements (math transparency, anti-overclaim, founder credibility, incident transparency) |
| `04-icp-and-segmentation/primary-icp.md` §8 | Five churn triggers (math wrong; alert fatigue; anti-overclaim drift; unhandled incident; framework not respected) |
| `05-positioning/positioning-statement.md` | Locked positioning; "trader operating system" frame; explicit non-claims |
| `05-positioning/messaging-hierarchy.md` | Tier-by-tier messaging; locked phrasing |
| `06-product-strategy/` | What ships, what doesn't, readiness gates |
| `07-packaging-and-pricing/plan-matrix.md` § support and access differences | Per-tier SLA expectations; assisted onboarding for P3 |
| `07-packaging-and-pricing/trial-and-discount-policy.md` | Refund handling; cohort-quality filtering |
| `08-go-to-market/trust-first-growth.md` | Trust principles; allowed/forbidden claims; review/checkpoint cadence |
| `12-onboarding-and-activation/activation-milestones.md` § stuck indicators | Triage triggers feed support |
| `12-onboarding-and-activation/onboarding-strategy.md` § exchange-connection failures | First support load category |
| `business-plan/_phase-2/_support/` | Locked support operating model, SLA framework, ticket routing, issue taxonomy |
| `business-plan/09-brand-messaging.md` | Locked phrasing list; anti-claim discipline |
| `business-plan/10-operations-support.md` | Operations + support framework inputs |
| `business-plan/_data/operations/Production_Candidate_Criteria_v2.md` | PCC v2 — referenced by every public claim |
| `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md` | Vendor incident scenarios + runbook entry points |
| `business-plan/_data/legal/Counsel_Brief_v2.md` | Legal posture; counsel review gates |

This folder is a Wave 2 **operational restatement** of the locked support, trust, and brand-claims work. Where the working notes give the gate-by-gate detail, this folder gives the strategic shape and the discipline rules.

---

## 5. Recommended reading order

For a founder running P1 cohort support:

1. `README.md` (this file) — orientation
2. `support-operating-model.md` — what we promise, what we do not
3. `trust-framework.md` — the principles
4. `incident-communications.md` — read **before** the first incident
5. `public-claims-guardrails.md` — keep this open during any external surface review
6. `_phase-2/_support/01-support-operating-model.md` and `02-support-sla-framework.md` — gate-by-gate detail when implementing

For a brand / content contractor onboarding:

1. `public-claims-guardrails.md` § allowed/forbidden + good/bad examples → must-read first
2. `trust-framework.md` § what trust means here
3. `08-go-to-market/trust-first-growth.md` § allowed/forbidden claims
4. `09-brand-messaging.md` (Wave 1) — locked phrasing

For a counsel review pass:

1. `public-claims-guardrails.md` § review process
2. `incident-communications.md` § what cannot be claimed during incidents
3. `_data/legal/Counsel_Brief_v2.md` and `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`

---

## 6. Open questions

Carried forward plus introduced by Wave 2.

1. **DECISION NEEDED — Support coverage hours at P2.** Locked v1 = Sun–Thu 09:00–15:00 GMT+4. Confirm or extend at P2 close.
2. **DECISION NEEDED — First support hire trigger.** Threshold defined in `_phase-2/_support/01-support-operating-model.md`; confirm dollar / ticket-volume threshold pre-P2.
3. **DECISION NEEDED — Status page hosting.** Statuspage / BetterUptime / self-hosted simple page. Recommendation: lightweight third-party at v1.
4. **DECISION NEEDED — Public postmortem cadence.** Every incident vs. only severity ≥ medium. Recommendation in `incident-communications.md` §5: every incident severity ≥ medium.
5. **DECISION NEEDED — Brand-voice review SLA.** Maximum review time for any external-facing surface (target: <24h for non-launch surfaces; <72h for launch surfaces).
6. **REQUIRED INPUT — Counsel sign-off on incident comms templates** before P1 launch.
7. **REQUIRED INPUT — Counsel sign-off on "institutional-grade" usage** (current positioning includes the phrase; counsel must confirm legal exposure).
8. **REQUIRED INPUT — Vendor failure-mode runbook dry-run** before P1 launch (per `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`).
9. **ASSUMPTION — Founder bandwidth supports 40-user cohort + 30 hours/week support coverage simultaneously.** Validate at P1 mid-cohort review.
10. **ASSUMPTION — Email + in-product form covers ≥95% of support inbound.** Validate at P1 close.
11. **OPEN — Telegram-as-support pressure.** @ScoopyAI_bot is alerts-only by design. Cohort users may attempt to reply to it for support; design a clear-and-honest "support is via email" auto-response.
12. **OPEN — Multilingual support.** Arabic post-P5 per Strategic Priority deferrals; not at v1.

---

## 7. Cross-references

- Phase 2 support canonical: `business-plan/_phase-2/_support/`
- Brand messaging: `business-plan/09-brand-messaging.md`
- Operations + support: `business-plan/10-operations-support.md`
- Risk / compliance / trust: `business-plan/12-risk-compliance-trust.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor Failure Mode Mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- No Investment Advice memo: `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`
- Risk Disclosure: `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
