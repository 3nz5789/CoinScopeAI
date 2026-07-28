# 06 — Product Strategy

**Status:** Wave 1 scaffolding · v1 · 2026-05-07
**Owner:** Founder (Mohammed)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## Folder purpose

This folder declares **what CoinScopeAI is strategically building** — and equally important, what it is **not** building yet. It commits to a single canonical product strategy, names the core product pillars, draws bright lines between MVP / beta / scale stages, and prioritizes the feature surface so that engineering capacity (founder + P4 contractor at v2 build) is spent where it has the most leverage on validation pass + P1 cohort signal.

It is the document that should be read before any roadmap conversation, any feature request, any vendor pitch, and any "could we add this?" thought. The discipline embedded here is: **necessary features beat impressive features**, and **execution discipline + risk gating remain central across every stage.**

---

## File list

| File | Purpose | Audience |
|---|---|---|
| `README.md` | Folder map, dependencies, reading order, open questions | Anyone entering the folder |
| `product-strategy.md` | Strategic product overview; who it serves first; core workflow; trust/risk in strategy; product boundaries; excellence vs limited-by-design |
| `core-product-pillars.md` | Five pillars (Market Intelligence / AI-Assisted Signal Context / Risk-Aware Decision Support / Execution Discipline & Workflow / Journaling & Performance Feedback) with table-stakes vs differentiator classification |
| `mvp-vs-beta-vs-scale.md` | MVP / beta / scale-stage product definitions tied to the locked phase map; what belongs in each stage; readiness gates; business implications of premature expansion |
| `feature-prioritization.md` | Must-have / should-have / later matrix; features by trust / activation / retention / monetization lens; deferral register; rationale |

---

## Why this folder matters

Three failure modes this folder exists to prevent:

- **Scope bloat under launch pressure.** P1 (June 2026) is two months away. Without a hard product-strategy lock, every advisor suggestion, vendor pitch, or P3-Layla preview becomes a "let's add this." Engineering capacity is the binding constraint; spending it on the wrong things means missing PCC v2 §8 pass.
- **Tier-matrix erosion.** The locked tier matrix (Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + per-seat) only holds if features stay correctly classified across tiers. Without a feature-prioritization lock, premium features leak into Trader, free features become contested, and pricing rationale weakens.
- **Drift away from "execution discipline as the product."** It is technically possible to build many things on top of the engine. Most of them dilute the locked Vision A. This folder names the discipline-software identity and protects it.

---

## Dependencies on prior folders

| Inherited from `01-executive-summary/` | Used in this folder |
|---|---|
| Strategic priorities P1, P3, P8, P9 (validation pass · anti-overclaim · testnet hard gate · Desk Preview quality bar) | MVP scope and readiness gates |
| Tier matrix Free / $79 / $399 / $1,199 + per-seat | Feature-by-tier classification |
| 10 hard business-model constraints | Product boundaries |
| Phase map P0 → P1 → P2 → P5 | Stage-to-phase mapping |

| Inherited from `02-company-overview/` | Used in this folder |
|---|---|
| Strategic constraints (R1–R10 risk · T1–T10 trust · P1–P10 provider · O1–O10 onboarding-support) | Feature must-haves and disallowed |
| Current-state assessment (Confirmed / Likely / Not-yet-validated) | Honest MVP scoping |
| Vision A + Mission 1 | Product-strategy spine |

| Inherited from `03-market-thesis/` | Used in this folder |
|---|---|
| Three structural shifts | Why each pillar matters |
| Adoption obstacles | Features that disarm objection |
| Invalidation signals I1–I10 | Features that produce validation evidence |

| Inherited from `04-icp-and-segmentation/` | Used in this folder |
|---|---|
| P1 Omar primary ICP | MVP must-haves; quality bar |
| Jobs-to-be-done emphasis matrix | Feature mapping |
| WTP indicators by segment | Tier-based premium features |
| Anti-fit signals | Features explicitly *not* on the roadmap |

| Inherited from `05-positioning/` | Used in this folder |
|---|---|
| Category lock (C-primary trader operating system + D-anchor institutional-grade signal/risk platform) | Feature-naming language; tier surface naming |
| 5 core differentiators (D1 gate before arming · D2 regime named · D3 custody-free · D4 anti-overclaim · D5 UAE-built) | Non-negotiable features |
| Locked phrasing rules | In-product copy guardrails |
| Disallowed claims | Disallowed features (autonomous execution, custody, signal-as-deliverable) |

This folder also pulls from prior locked v1 work, especially:

- `business-plan/05-product-strategy.md` (locked v1) — single source of truth for any conflict
- `business-plan/_phase-1/04-product.md`
- `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- `business-plan/_data/operations/mvp-readiness-checklist.md`
- `business-plan/_decisions/decision-log.md`

If anything here contradicts locked v1 §5, the locked file wins until pre-mortem + decision-log update.

---

## Recommended reading order

For a new collaborator:

1. `01-executive-summary/strategic-priorities.md` (upstream — what we're spending on)
2. `04-icp-and-segmentation/jobs-to-be-done.md` (upstream — what the buyer is hiring the product to do)
3. `05-positioning/differentiation-framework.md` (upstream — what must remain a differentiator)
4. `06-product-strategy/product-strategy.md` (start here — the spine)
5. `06-product-strategy/core-product-pillars.md` (the 5 pillars)
6. `06-product-strategy/mvp-vs-beta-vs-scale.md` (stage gates and phase mapping)
7. `06-product-strategy/feature-prioritization.md` (the operating list)
8. Locked v1 `business-plan/05-product-strategy.md` for the deeper feature-by-feature commitment

For folder authors and contractors:

1. `feature-prioritization.md` first — what to actually do
2. `mvp-vs-beta-vs-scale.md` — what stage we're in, what the next gate is
3. `core-product-pillars.md` for any feature requiring pillar classification
4. PCC v2 alongside, always

For anyone authoring product copy:

1. `core-product-pillars.md` for feature-naming language
2. `05-positioning/messaging-hierarchy.md` §8 for in-product voice rules

---

## Open questions

- **Q1** — Should the Desk Preview "advanced gates" feature set (per-account override of system thresholds, conditional combination gates, time-of-day gates) ship at P1 close, or split across P1 and P2? **DECISION NEEDED** before P1 close — Founder
- **Q2** — Is read API on Desk Preview ($399) sufficient, or does P2 Karim segment need a write API at any tier? Working recommendation: read-only at Desk Preview through P2; write API not on roadmap pre-P5. **DECISION NEEDED** at P2 charter — Founder
- **Q3** — Per-seat tier ($149 vs $249 at Desk Full v2): which anchor? Working recommendation: revisit at P5 charter against P3 Layla cohort feedback. **DECISION NEEDED** before Desk Full v2 GA — Founder
- **Q4** — Should the Free tier expose any risk-gate output, or remain scanner+regime read-only? Working recommendation: scanner + regime sample only; risk-gate output is the paid surface. **DECISION NEEDED** — Founder
- **Q5** — Bybit at P2 — full feature parity with Binance USDT-M, or read-only scanning at first? Working recommendation: phased — read-only scan first, gate-and-arm parity after stability proven. **DECISION NEEDED** at P2 charter — Founder
- **Q6** — Native mobile app — durable defer (post-P5 only if cohort demands), or revisit at P2? Working recommendation: durable defer; web + Telegram cover the cohort. **DECISION NEEDED** — Founder
- **Q7** — Audit log on threshold changes (T3 in jobs-to-be-done) — first-class at Desk Preview or at Desk Full v2 only? Working recommendation: first-class at Desk Preview; the surface is small and the trust value is high. **DECISION NEEDED** — Founder

---

## Cross-document consistency commitments

- Vision A + Mission 1
- Personas P1 Omar / P2 Karim / P3 Layla — internal only
- Tier matrix Free / $79 / $399 / $1,199 + per-seat ($149 or $249)
- Risk numbers (10x / 10% / 5% / 5 pos / 80%)
- Phase map P0 → P1 → P2 → P5
- Posture: testnet-only, US blocked, UAE/MENA + global EN
- Anti-overclaim discipline; locked phrasing
- Custody-free, user-authorized, no signal-as-deliverable
