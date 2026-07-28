# 02 — Company Overview

**Status:** Wave 1 scaffolding · v1 · 2026-05-07
**Owner:** Founder (Mohammed)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## Folder purpose

This folder defines the **factual operating context** for CoinScopeAI. Where folder `01` makes the strategic case and lays out priorities, folder `02` answers the more boring but more load-bearing questions:

1. What is the company, in plain terms, today?
2. What does the product look like *right now* — confirmed, partially built, in-progress?
3. What constraints are non-negotiable, and which are negotiable but should not be touched yet?

It is the document a careful new collaborator (advisor, contractor, counsel, vendor) should read second — after the executive summary — to calibrate their expectations against reality.

---

## File list

| File | Purpose | Audience |
|---|---|---|
| `README.md` | Folder map, dependencies, reading order, open questions | Anyone entering the folder |
| `company-overview.md` | Company description, vision, mission, users, product scope, posture, business-model direction, trust/risk orientation, "how to describe ourselves today" | Founder, advisors, vendors, future hires |
| `current-state-assessment.md` | Confirmed / Likely / Not-Yet-Validated readiness across business, GTM, product, operations | Founder, contractors, advisors |
| `strategic-constraints.md` | Hard constraints across risk, trust, provider, compliance, onboarding, support, billing, growth + explicit "do not yet" list | Founder, anyone making roadmap or scope decisions |

---

## Why this folder matters

Three reasons, each tied to a real failure mode that this folder exists to prevent:

- **Stops aspiration from being reported as fact.** New collaborators meeting CoinScopeAI for the first time often ask "what does the product do?" The honest answer changes if you say *what it does today on testnet for the validation cohort* vs. *what it will do at Desk Full v2*. This folder makes that distinction enforceable.
- **Anchors decisions to constraints, not preferences.** When a vendor pushes a feature, an advisor pitches a partnership, or a paid-ad agency offers an introductory deal, the constraint set in `strategic-constraints.md` is the document we open before saying yes. It is the operating contract.
- **Calibrates fundraising and hiring conversations.** Saying "we are pre-validation, sole-prop, testnet-only" is structurally different from "we are pre-revenue." This folder gives the founder the honest framing without softening it for fundraising audiences.

---

## Dependencies on folder 01

This folder inherits — and must not contradict — the following from `01-executive-summary/`:

| Inherited from `01` | Used in `02` |
|---|---|
| Strategic frame ("AI-driven capital-preservation infrastructure") | `company-overview.md` description and posture |
| Three personas (P1 Omar / P2 Karim / P3 Layla) | `company-overview.md` intended users |
| Tier matrix (Free / $79 / $399 / $1,199 + per-seat) | `company-overview.md` business-model direction |
| Phase map (P0 → P1 → P2 → P5) and validation-phase posture | `current-state-assessment.md` readiness levels |
| 10 hard constraints (testnet-only, US blocked, no paid acquisition pre-CAC validation, etc.) | `strategic-constraints.md` (extended and elaborated) |
| Locked risk numbers (10x / 10% / 5% / 5 pos / 80%) | Both `company-overview.md` and `strategic-constraints.md` |
| Anti-overclaim discipline | All three files; especially "how CoinScopeAI should describe itself today" |

If a reader notices any drift between `01` and `02`, the `01-executive-summary/` files are the upstream truth. Update `02` in the same pass.

This folder also pulls from prior locked v1 work:

- `business-plan/00-framework.md`
- `business-plan/_decisions/decision-log.md`
- `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Memory: `project_vision_mission.md`, `project_engine_thresholds.md`, `project_phased_rollout.md`, `project_jurisdictional.md`

---

## Recommended reading order

For a new collaborator:

1. `01-executive-summary/executive-summary-v1.md` (upstream)
2. `02-company-overview/company-overview.md` (this folder — start here)
3. `02-company-overview/current-state-assessment.md` (this folder — sober calibration)
4. `02-company-overview/strategic-constraints.md` (this folder — operating contract)
5. `01-executive-summary/strategic-priorities.md` (back upstream — what we are doing about it)
6. `01-executive-summary/business-model-summary.md` (mechanics)

For folder authors writing `03 → 06`:

1. `02-company-overview/strategic-constraints.md` first — most downstream-binding
2. `02-company-overview/company-overview.md` for tone and posture
3. `02-company-overview/current-state-assessment.md` for readiness calibration

---

## Open questions

- **Q1** — Is there a single approved one-liner for "what CoinScopeAI is" across product, brand, fundraising, and recruiting? `company-overview.md` proposes one; **DECISION NEEDED** to ratify across surfaces — Founder
- **Q2** — Should `current-state-assessment.md` be re-run on a fixed cadence (e.g., end of each phase) or only on material change? **DECISION NEEDED** — Founder
- **Q3** — Are there constraints in `strategic-constraints.md` that should be promoted to "code-level enforced" rather than "policy-level enforced"? **REQUIRED INPUT** from a focused review pass with the test-and-simulation lab — Founder
- **Q4** — Does the company-overview language match the brand-voice rules well enough to be lifted directly into external surfaces (about page, deck, recruiting)? **REQUIRED INPUT** from brand-voice enforcement skill audit — Founder
- **Q5** — Are any constraints obsolete or in tension with the locked v1 narrative as it stood on 2026-05-01? **ASSUMPTION:** none, pending pre-mortem review at any threshold change — Founder
- **Q6** — Does the readiness assessment surface any item that should escalate to a near-term priority in `01-executive-summary/strategic-priorities.md`? **REQUIRED INPUT** from review pass — Founder

---

## Cross-document consistency commitments

These must remain identical to `01`. Any drift fixed in the same pass:

- Vision A (capital-preservation default) + Mission 1 (operational) — locked 2026-04-22
- Personas P1 Omar / P2 Karim / P3 Layla
- Tier matrix Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + per-seat ($149 or $249)
- Risk numbers 10% drawdown · 5% daily loss · 10x leverage · 5 max positions · 80% heat (PCC v2 §8)
- Phase map P0 May 2026 → P1 Jun–Jul 2026 → P2 Aug–Sep 2026 → P5 Mar–May 2027
- Posture: Testnet only · 30-day validation phase · No real capital · US blocked at signup · UAE/MENA + global EN target
