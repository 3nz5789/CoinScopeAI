# 04 — ICP and Segmentation

**Status:** Wave 1 scaffolding · v1 · 2026-05-07
**Owner:** Founder (Mohammed)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## Folder purpose

This folder answers **who CoinScopeAI should target first, and why** — and equally important, **who it should not target yet**. It exists to prevent the most common GTM failure mode for a small validation-phase team: broad, unfocused targeting that produces tepid signal and burns the validation window.

It commits to a recommended **primary ICP**, classifies the other locked personas as **secondary**, and tags the deferred segments explicitly. It then maps jobs-to-be-done, pains, triggers, and willingness-to-pay across segments so that downstream folders (`05-positioning/`, `06-product-strategy/`, plus eventually `07-packaging-pricing` and `08-gtm-strategy`) inherit a single source of truth about who buys, why, and what they need to trust before they pay.

This folder does **not** restate the locked v1 §3 persona cards — those live at `business-plan/03-icp-segmentation.md` and are interview-pending until §3.7/§3.8 data lands. It is the **operator-grade** companion that turns those cards into prioritization, focus, and packaging decisions.

---

## File list

| File | Purpose | Audience |
|---|---|---|
| `README.md` | Folder map, dependencies, reading order, open questions | Anyone entering the folder |
| `primary-icp.md` | Recommended primary ICP with rationale, ideal-account characteristics, evaluation behavior, trust requirements, success and churn definitions | Founder, anyone shaping P1 launch and content |
| `secondary-icps.md` | Secondary segments, why deferred, risks of leading with them, conditions to revisit, deferred-segment register | Founder, anyone tempted to broaden too early |
| `jobs-to-be-done.md` | Functional · emotional · risk-reduction · workflow · team/collab JTBD across segments | Founder, product, brand, support |
| `pains-triggers-wtp.md` | Pain points, buying / activation triggers, trust triggers, WTP indicators, anti-fit signals, messaging and packaging implications | Founder, GTM, brand, sales |

---

## Why this folder matters

Three reasons, each tied to a specific failure mode:

- **Stops persona drift under launch pressure.** When P1 opens on 2026-06-01 with a 40-user cohort cap, the temptation to take any signup that arrives is real. This folder declares which signups are the cohort we want to study, and which are courtesy-served-but-not-led-with.
- **Anchors content and channel choices.** A "trader operating system" can market to many audiences. Locking primary ICP here makes content and channel choices in `_phase-2/_gtm/` defensible rather than reactive.
- **Forces honest pricing and packaging logic.** WTP indicators and JTBD by segment are the inputs to `06-pricing-monetization.md` and the locked tier matrix. Without ICP focus, pricing logic drifts toward "what do we hope they pay" instead of "what does the primary segment actually pay."

---

## Dependencies on prior folders

| Inherited from `01-executive-summary/` | Used in this folder |
|---|---|
| Three personas (P1 Omar / P2 Karim / P3 Layla) | Primary / secondary classification |
| Tier matrix Free / $79 / $399 / $1,199 + per-seat ($149 or $249) | WTP anchors per segment |
| Phase map P0 → P1 → P2 → P5 | When each segment becomes leadable |
| Strategic priorities (P4: persona interviews) | This folder's interview-validation hook |
| Must-be-true tests MT1, MT2, MT3 | Segment validation criteria |

| Inherited from `02-company-overview/` | Used in this folder |
|---|---|
| Posture (testnet-only, US blocked, UAE/MENA + global EN) | Geography + jurisdiction filter on segments |
| 7 categories of strategic constraints | Anti-fit signals; deferred-segment justifications |
| Current state assessment | Realism on what we can support per cohort cap |

| Inherited from `03-market-thesis/` | Used in this folder |
|---|---|
| Three structural shifts | Force-to-persona alignment |
| Category framing options (recommended C-primary + D-anchor) | Tier mapping per segment |
| Demand drivers, adoption obstacles | Pains, triggers, anti-fit signals |
| Invalidation signals I1, I4–I7 | Segment-validation thresholds |

This folder also draws from prior locked v1 work, especially:

- `business-plan/03-icp-segmentation.md` — locked v1, persona cards, anti-personas, interview plan
- `business-plan/_decisions/decision-log.md` — locked primary ICP framing (2026-05-01)
- `_phase-1/02-icp.md`
- `business-plan/04-problem-value-prop.md`

If anything in this folder contradicts the locked v1 §3 file, the locked file wins until pre-mortem + decision-log update.

---

## Recommended reading order

For a new collaborator:

1. `01-executive-summary/executive-summary-v1.md` (upstream)
2. `02-company-overview/company-overview.md` (upstream — posture)
3. `03-market-thesis/market-thesis.md` (upstream — category framing)
4. `04-icp-and-segmentation/primary-icp.md` (start here)
5. `04-icp-and-segmentation/jobs-to-be-done.md`
6. `04-icp-and-segmentation/pains-triggers-wtp.md`
7. `04-icp-and-segmentation/secondary-icps.md`
8. Locked v1 `business-plan/03-icp-segmentation.md` for full persona cards

For folder authors writing `05` and `06`:

1. `primary-icp.md` for positioning and product-strategy anchors
2. `pains-triggers-wtp.md` for messaging and packaging logic
3. `jobs-to-be-done.md` for product-surface decisions

---

## Open questions

- **Q1** — Will §3.7 interviews confirm P1 Omar as the strongest validated segment, or surface a fourth archetype ("disciplined-by-habit" or "disciplined-intuitive") that should broaden Persona 1's origin definition? **REQUIRED INPUT** from interview cohort — Founder
- **Q2** — At what unprompted "discipline-first" rate in §3.7 do we declare Force 1 confirmed (locked v1 suggests ~30%)? **DECISION NEEDED** before P1 mid-cohort review — Founder
- **Q3** — Should P3 Layla be promoted from "strategic secondary" to "co-primary" if P1 cohort produces strong Layla signal in the first 20 paid users? **DECISION NEEDED** at P1 mid-cohort review — Founder
- **Q4** — Are anti-personas (US retail, sub-$5k accounts, copy-traders, fund LPs) honored consistently across signup, billing, support, and content? **REQUIRED INPUT** from anti-overclaim audit pass — Founder
- **Q5** — Should "prop-firm-funded traders" (locked secondary in v1) remain at served-not-led status, or do they need elevated treatment given their natural fit with risk gates? **DECISION NEEDED** by end of P1 — Founder
- **Q6** — Is the "no fund LPs" anti-persona durable through P5 Desk Full v2 launch, given that small-fund GPs who buy Desk Full could in principle service LPs downstream? **DECISION NEEDED** with counsel before P5 — Founder + counsel

---

## Cross-document consistency commitments

These items must remain identical to `01`, `02`, and `03`:

- Vision A + Mission 1
- Personas P1 Omar / P2 Karim / P3 Layla — internal names only
- Anti-personas: US-resident retail, sub-$5k accounts, copy-traders / signal-group buyers, fund LPs
- Tier matrix and per-seat scaling
- Risk numbers (10x / 10% / 5% / 5 pos / 80%)
- Phase map (P0 → P1 → P2 → P5)
- Posture: testnet-only, US blocked, UAE/MENA + global EN, no paid acquisition pre-CAC
- Anti-overclaim discipline; "institutional-grade" reserved phrasing
