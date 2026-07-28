# 07 — Packaging and Pricing

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/06-pricing-monetization.md` v1 LOCKED (2026-05-01) — this folder operationalizes that file, it does not supersede it.

---

## 1. Folder purpose

This folder defines **how CoinScopeAI packages and prices its offer** in a way that matches:

- the actual product maturity (validation-phase, testnet-first, real-capital-gated)
- the trust-sensitive positioning (anti-overclaim, capital-preservation default)
- the locked target ICPs (P1 Omar primary, P3 Layla strategic secondary, P2 Karim watch-list)
- the gated real-capital posture (PCC v2 §8 Capital Cap)
- the current and near-term monetization readiness (Stripe-only, UAE sole prop, below VAT threshold)

It is **operator-grade**, not marketing-grade. Every recommendation is implementation-ready and is traceable to a Wave 1 source.

---

## 2. File list

| File | What it contains |
|---|---|
| `README.md` | This file — folder map, dependencies, reading order, open questions |
| `packaging-strategy.md` | Packaging philosophy, offer structure, core/premium/deferred separation, packaging risks |
| `pricing-strategy.md` | Pricing philosophy, initial direction, monthly vs. annual, signal effects, mistakes to avoid |
| `plan-matrix.md` | Plan-level matrix — names, intended buyers, feature access, support differences, anti-fit, default offer |
| `trial-and-discount-policy.md` | Trial structure, free-tier vs. trial decision, discount guardrails, refund logic, promo constraints |

---

## 3. Why this folder matters

CoinScopeAI's commercial credibility is **structurally fragile in early P0/P1**: a single overpriced, overpromised, or under-trust-supported tier can destroy the cohort signal that the product is trying to earn. Equally, underpricing damages perceived seriousness with P3 Layla and undermines the buy-vs-build math for P2 Karim.

Packaging and pricing therefore function as **trust signals first, revenue mechanisms second**. This folder treats them in that order:

1. Does the package match what the product can actually deliver today?
2. Does the price match the validation-stage trust the buyer can reasonably extend?
3. Does the matrix degrade gracefully if a tier ships ahead of its readiness gate?
4. Does the trial/discount/refund logic protect cohort quality, not maximize signups?

Get this wrong and §11 financial model breaks, §07-GTM funnel breaks, §13-trust-ops absorbs the damage. Get it right and the cohort earns the next funding round.

---

## 4. Dependencies on prior folders

| Source | What we inherit |
|---|---|
| `01-executive-summary/business-model-summary.md` | Track B tier matrix (Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + per-seat) |
| `01-executive-summary/strategic-priorities.md` | Validation-phase posture; capital-preservation default; founder-led distribution |
| `02-company-overview/strategic-constraints.md` | Custody-free; testnet-first; UAE sole prop; no paid acquisition pre-CAC |
| `03-market-thesis/` | Comp pricing landscape; $0–$30 / $30–$150 / $200–$800 bands |
| `04-icp-and-segmentation/primary-icp.md` | P1 Omar at Trader $79 anchor; ICP buying behavior and trust requirements |
| `04-icp-and-segmentation/pains-triggers-wtp.md` | WTP per persona (P1 M, P2 M, P3 H) |
| `05-positioning/positioning-statement.md` | Locked positioning lines; "trader operating system" frame |
| `06-product-strategy/feature-prioritization.md` | Core vs. premium vs. deferred capability split |
| `06-product-strategy/mvp-vs-beta-vs-scale.md` | What ships at MVP / Beta / Scale; readiness gates |
| `business-plan/06-pricing-monetization.md` | **§6 v1 LOCKED** — comp landscape, WTP per persona, Model C hybrid, tier prices, refund/discount policy, AED handling |

This folder is a Wave 2 **operational restatement** of §6, structured for execution rather than analysis. Where the locked file gives the *what*, this folder gives the *how*.

---

## 5. Recommended reading order

For a founder/operator picking this up cold:

1. `README.md` (this file) — orientation
2. `plan-matrix.md` — see the offer at a glance before reading the rationale
3. `packaging-strategy.md` — understand why the matrix is shaped this way
4. `pricing-strategy.md` — understand why each tier sits at its price
5. `trial-and-discount-policy.md` — understand how the funnel and the trust posture interact

For a designer or marketer building the pricing page:

1. `plan-matrix.md` → first
2. `pricing-strategy.md` §6 (anti-overclaim audit) → must-read before writing copy
3. `trial-and-discount-policy.md` § "we'll be back" messaging → required for sub-$5k handling

For someone preparing a fundraising deck:

1. `pricing-strategy.md` § signal effects → ARPU and positioning anchors
2. `plan-matrix.md` § default offer + deferrals → roadmap-aligned revenue ramp
3. `06-pricing-monetization.md` §6.9 → LTV/CAC sensitivity (do **not** restate it here; reference it)

---

## 6. Open questions

Carried forward from Wave 1 §6.10 + introduced by Wave 2 operationalization. **DECISION NEEDED** items must be resolved before P1 cohort opens (Jun 2026).

1. **DECISION NEEDED — Trial mechanic.** Free tier as evergreen trial vs. time-bounded paid trial vs. demo-mode. Recommendation in `trial-and-discount-policy.md` §2; needs founder lock.
2. **DECISION NEEDED — Annual prepay attach target.** §6.9 base case is 40% annual / 60% monthly for Trader. P1 cohort will validate; commit to a target now or at P1 close?
3. **DECISION NEEDED — Founder-cohort eligibility window.** §6.7 says first 60 days post-public-launch. Confirm that "public-launch" means P2 (Aug–Sep 2026) and not P1 soft-launch (Jun–Jul 2026).
4. **DECISION NEEDED — Per-seat pricing for Desk Full v2.** §6.6 locked $149 partner read-only and $249 analyst, but the Desk Full v2 launch is P5 (Mar–May 2027). Lock now or revisit at P3?
5. **REQUIRED INPUT — Counsel sign-off on refund policy language.** 14-day money-back, no-refund-after-14-days, anti-stacking rules. Cross-reference `_data/legal/Counsel_Brief_v2.md`.
6. **REQUIRED INPUT — Stripe configuration of founder-cohort time-bounded promo codes.** Verify the 60-day auto-revert behavior is configurable in our Stripe account.
7. **ASSUMPTION — P2 Karim's buy-vs-build threshold.** $79/mo Trader assumed beneath the build-it-myself line. Validate at P1 cohort review (M3).
8. **ASSUMPTION — P3 Layla's audit-grade reporting WTP.** §6.2 frames up-to-1%-of-book-per-month if partner reporting reaches audit-grade; v1 only delivers static-PDF. Validate at P5 launch.
9. **ASSUMPTION — No price change before P5.** §6 v1 locks pricing for ≥6 months post-validation. Confirm this stands across the P2 vendor expansion.
10. **OPEN — Crypto payment acceptance.** Deferred per §6.8. Revisit post-v2 if MENA users repeatedly request it.

---

## 7. Cross-references

- §6 v1 LOCKED canonical: `business-plan/06-pricing-monetization.md`
- Phase 2 packaging working notes: `business-plan/_phase-2/_packaging/`
- Phase 2 pricing working notes: `business-plan/_phase-2/_pricing/`
- Decision log: `business-plan/_decisions/decision-log.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
