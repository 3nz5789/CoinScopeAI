# 02 — PRICING

**Workstream:** PRICING
**Phase:** 2 — Monetization
**Status:** Canonical task list absorbed verbatim 2026-05-04. Source of truth for the Phase 2 PRICING workstream.
**Canonical authorities:** v1 framework `06-pricing-monetization.md` LOCKED 2026-05-01 (§6.1 comp, §6.2 WTP, §6.3 Model C, §6.5 Free Scope B, §6.6 Track B prices, §6.7 refund + founder-cohort, §6.8 currency, §6.9 LTV/CAC sensitivity, §6.10 anti-overclaim audit). PACKAGING workstream (`_phase-2/01-packaging.md`).

---

## 1. Purpose

Lock the **commercial pricing system**: ratify or revise Track B v1 numbers, operationalize founder-cohort, monthly-vs-annual offer mechanics, refund/dunning, intro-offer posture, and a working price-to-margin sensitivity model that feeds §11 in Phase 4. PRICING translates §6 v1 from *committed structure* into *committed numbers* validated against P0 cohort data and ready for Stripe.

## 2. Why this matters specifically for CoinScopeAI

- **Track B numbers are committed at v1 but not yet validated against cohort data.** Phase 2 either ratifies (preferred path) or revises with explicit reason from the P0 cohort exit memo.
- **Pricing is a trust signal.** Per §6.10 anti-overclaim audit and the BRAND voice (anti-pressure, methodical), every pricing surface — page, modal, email, invoice — is a trust-load surface. Drift here loses capital-preservation positioning faster than feature drift.
- **§11 financial model unblocks on Phase 2 PRICING outputs.** Phase 4 cannot start fundraising work without locked unit economics; Phase 2 produces the inputs.
- **Founder-cohort policy is operational here, not in marketing.** Stripe promo-code wiring, eligibility comms, the 60-day window, "founding-member" copy guards (§6.10 Flag 1) all happen as PRICING engineering work.
- **AED handling and VAT step-function** matter for cash-flow modeling and for the §11 sensitivity rank.
- **The decision NOT to ship a free trial** is itself a pricing decision (Free Scope B is the substitute). It needs to be explicit so Phase 3 GTM doesn't quietly add one.

## 3. Required subsections

1. **Pricing strategy recommendation** — ratify-or-revise Track B with reasoning + revision triggers.
2. **Initial pricing philosophy** — durable principles (anti-pressure, anti-race-to-bottom, capital-preservation alignment).
3. **Monthly vs annual offer structure** — discount math, anchor logic, switching rules, mix sensitivity.
4. **Trial and intro offer options** — explicit no-free-trial; founder-cohort and beta-access as the intro offers.
5. **Price-to-margin sensitivity model** — lightweight v0 of §11, scenarios across cohort mix and per-seat density.
6. **Price validation interview script** (NEXT) — instrument for testing tier prices with prospective P3 buyers.
7. **Discount policy guardrails** (NEXT) — operational rules for any non-founder-cohort discount.
8. **Refund and billing policy draft** (NEXT) — codifies §6.7 into customer-facing terms.
9. **Conversion benchmarks and KPI targets** (NEXT METRICS) — locks §6.9 inputs as Phase 2 KPI targets.
10. **Stripe plan mapping review** (NEXT QA) — entitlement-to-billing audit on the Stripe side.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Pricing Strategy Recommendation | MD; signed by founder | Founder + Strategy CoS |
| Initial Pricing Philosophy | MD principles doc | Founder |
| Monthly vs Annual Offer Structure | MD with mix-sensitivity table | Strategy CoS + FinOps |
| Trial and Intro Offer Options | MD with rejected alternatives | Founder + Strategy CoS |
| Price-to-Margin Sensitivity Model | MD + lightweight spreadsheet (xlsx in Phase 4) | FinOps + Founder |
| Price Validation Interview Script | MD interview guide + scoring rubric | Strategy CoS |
| Discount Policy Guardrails | MD with edge-case decision tree | Founder |
| Refund and Billing Policy Draft | MD customer-facing terms | Founder + Counsel (Phase 4 review) |
| Conversion Benchmarks + KPI Targets | MD KPI table | Strategy CoS + FinOps |
| Stripe Plan Mapping Review | MD audit + remediation backlog | Eng + FinOps |

## 5. Assumptions to validate

1. **ASSUMPTION** — §6.6 mid-band Track B prices ($79 / $399 / $1,199) are the right anchors. P0 cohort exit memo + price validation interviews are the validation instruments.
2. **ASSUMPTION** — ~17% annual discount is sufficient retention incentive without leaving margin. Mix-sensitivity model tests upside/downside.
3. **ASSUMPTION** — Founder-cohort 25–30% off drives soft-launch conversion without setting bad pricing precedents (per §6.10 Flag 1 mitigation).
4. **ASSUMPTION** — No free trial is the right posture; Free Scope B is the trial-substitute. Validate against cohort feedback in §6.9 sensitivity.
5. **ASSUMPTION** — VAT step-function at AED 375k (~$102k) annual revenue is the only material tax-handling step within 24-month base case. Other-GCC VAT is below materiality threshold.
6. **ASSUMPTION** — Stripe processing blended at ~3.5% is the realistic margin draw. Confirm against actual Stripe Atlas account fee schedule for UAE.

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **Pr2-1** | Track B prices ratify or revise | (a) Ratify §6.6 numbers as-is. (b) Revise based on P0 exit memo. (c) Hold prices but adjust founder-cohort magnitude. | Founder | After P0 cohort exit memo | §11 financial model, pricing page |
| **Pr2-2** | Annual discount magnitude | (a) Ratify ~17% (10/12). (b) Increase to 20% (~9.6/12) for retention push. (c) Decrease to 12% to preserve margin. | Founder | Before pricing-page lock | Annual mix, working capital |
| **Pr2-3** | Trial posture | (a) No free trial — Free Scope B is the substitute (recommended). (b) 14-day Trader trial with card-on-file. (c) 7-day Trader trial without card. | Founder | Before pricing-page lock | Funnel mechanics, support load |
| **Pr2-4** | Founder-cohort effective discount | (a) Ratify 25–30% per §6.6 numbers. (b) Tighten to 20% (less drag on §11). (c) Widen to 35% (cohort-recruitment incentive). | Founder | Before P1 Narrow Ship public launch | §11 first-2-months revenue, cohort comms |
| **Pr2-5** | Refund SLA per tier | (a) Uniform 14-day per §6.7. (b) Tier-tiered: 14d Trader, 30d Desk Preview, 30d Desk Full. (c) 14d uniform but DF gets a "first 30 days return any seat" carve-out. | Founder | Before pricing-page lock | Support SLA, churn rate |
| **Pr2-6** | Stripe configuration form | (a) Stripe Atlas UAE account (recommended per §6.8). (b) Stripe direct merchant account. (c) Paddle merchant-of-record. | Founder + Eng | Before billing goes live | Billing complexity, VAT handling |
| **Pr2-7** | Discount policy ceiling | (a) Per §6.7 — max 25%, max 30 days, no stacking (recommended). (b) Stricter: max 15%. (c) Looser: case-by-case to 40%. | Founder | Before any non-founder-cohort discount runs | Pricing-power signal, anti-ICP guard |

## 7. Failure modes to avoid

- **Pricing change before P0 cohort exit memo.** Invalidates §11 baseline; reads as panic. Hold pricing through P0 unless an exit-memo trigger fires.
- **Trial-creep.** "Just 7 days of Trader for free, no card needed" sounds harmless, breaks the Free-Scope-B trust demo, and creates a class of converts who never see Free's permanent value. **Pr2-3 default is no free trial.**
- **Annual discount inflation.** Bumping annual to 25%+ to chase a retention KPI compresses margin and trains buyers to expect deeper discounts. Hold ~17%.
- **Founder-cohort comms drift.** "Founder discount locked in" / "lifetime founding-member rate" — every variant violates §6.10 Flag 1. Single canonical phrasing: "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies."
- **Cohort over-discounting.** 35%+ founder-cohort drains §11 first-2-months revenue and signals "we needed to bribe people." 25–30% is the band.
- **Per-seat hidden charges.** Adding a partner seat must show pro-rated charge and next-renewal recurring charge before the user confirms. Surprise per-seat invoices are the Class D Class-E friction in `_packaging/05-packaging-friction-review.md`.
- **AED display drift to AED billing.** The §6.8 + §6.10 Flag 3 mitigation is "approximate AED equivalent — billed in USD." Drift to native-AED billing without UAE local-entity checks is a §12 risk-register escalation, not a quiet PRICING tweak.
- **Stripe entitlement drift.** Promo-code stacking, free-extension promos, manually-applied discounts that diverge from §6.7 ceilings produce audit nightmares. `[QA] PRICING — Stripe Plan Mapping Review` runs before any pricing change ships.
- **Discount stacking with affiliate / referral.** Per §6.7 — no stacking with founder-cohort or annual. If Phase 3 introduces partnerships (prop firms, etc.), the stacking ban must hold.
- **Refund-then-resubscribe loop tolerated.** Per §6.7 — anti-abuse caps refunds at one per account lifetime. Lax enforcement creates revenue washing.

## 8. Tasks (canonical list — verbatim)

### NOW

**`[RESEARCH] PRICING — Pricing Strategy Recommendation`**
- **Objective:** Recommend the pricing strategy for Phase 2 — ratify §6.6 Track B numbers or revise based on P0 cohort exit memo. Defines explicit revision-trigger conditions.
- **Why:** Track B is committed at §6 v1 but the *numbers* are not validated against cohort behavior. The recommendation is the input to every other PRICING task; locks the unit-economics baseline for §11.
- **Dependency:** §6.6 Track B (LOCKED); P0 cohort exit memo (when available); PACKAGING `01-tier-structure-recommendation.md`.
- **Output:** Pricing strategy MD; signed; feeds Decision Register entry **Pr2-1**.

**`[DOC] PRICING — Initial Pricing Philosophy`**
- **Objective:** Codify the durable pricing principles that govern every pricing decision, including future ones outside the Track B horizon.
- **Why:** Without an explicit philosophy, Phase 3 / 4 / 5 pricing decisions drift toward category norms (race-to-bottom, lifetime deals, opaque enterprise pricing). Philosophy is the audit standard for any pricing change after Phase 2.
- **Dependency:** §6 v1 LOCKED; Phase 1 BRAND voice; PACKAGING friction review (`_packaging/05-packaging-friction-review.md`).
- **Output:** Pricing philosophy MD; principles list; signed.

**`[DOC] PRICING — Monthly vs Annual Offer Structure`**
- **Objective:** Define the operational mechanics of monthly + annual: discount math, anchor logic, switching rules, mix-sensitivity to revenue and working capital.
- **Why:** Annual mix is §11 sensitivity rank #3 (cash flow + retention math). Wrong discount magnitude either compresses margin or fails to drive conversion.
- **Dependency:** §6.6 Track B; §6.9 sensitivity inputs.
- **Output:** Offer-structure MD with mix-sensitivity table. Feeds **Pr2-2**.

**`[DOC] PRICING — Trial and Intro Offer Options`**
- **Objective:** Catalogue trial / intro-offer options, explicitly recommend no free trial (Free Scope B as substitute), and document founder-cohort + beta-access as the intro offers.
- **Why:** Trial-creep is a top failure mode. Explicit decision-with-reason prevents Phase 3 GTM from quietly adding one. Founder-cohort and beta-access are the cohort-conversion intro offers; their roles need to be distinct.
- **Dependency:** §6.5 Free Scope B; §6.7 founder-cohort policy; PACKAGING `Beta Access Offer Design` (NEXT).
- **Output:** Trial / intro-offer MD with rejected alternatives. Feeds **Pr2-3**.

**`[FINANCE] PRICING — Price-to-Margin Sensitivity Model`**
- **Objective:** Build a lightweight v0 sensitivity model: revenue scenarios across cohort mix, per-seat density, annual-mix, and founder-cohort drag. Surfaces the §11 sensitivity-rank inputs for §11 Phase 4 buildout.
- **Why:** §11 financial model unblocks on this. Phase 4 fundraising narrative cannot start without unit economics scenarios. Senstivity here exposes the highest-leverage pricing levers.
- **Dependency:** §6.6 Track B; §6.9 LTV/CAC sensitivity inputs; PACKAGING tier-structure recommendation.
- **Output:** Sensitivity model MD + spreadsheet outline (Phase 4 builds the actual xlsx).

### NEXT

**`[RESEARCH] PRICING — Price Validation Interview Script`**
- **Objective:** Build the interview instrument for testing Track B prices against prospective P3 buyers and a sample of P1/P2 buyers.
- **Why:** Pricing strategy recommendation locks tentatively against P0 exit memo; validation interviews are the second confirmation pass for the Desk Preview / Desk Full anchors.
- **Dependency:** Pricing strategy recommendation; ICP definitions.
- **Output:** Interview script MD + scoring rubric.

**`[DOC] PRICING — Discount Policy Guardrails`**
- **Objective:** Operational rules for any non-founder-cohort discount: who can approve, max magnitude (25% per §6.7), max duration (30 days), anti-stacking, anti-ICP guard.
- **Why:** Without explicit guardrails, ad-hoc discounts proliferate, train buyers to negotiate, and produce audit-trail headaches. Explicit policy is the operational form of §6.7.
- **Dependency:** §6.7 discount policy; pricing philosophy.
- **Output:** Discount guardrails MD with edge-case decision tree. Feeds **Pr2-7**.

**`[DOC] PRICING — Refund and Billing Policy Draft`**
- **Objective:** Translate §6.7 (refund / mid-cycle / cancellation / dunning / chargeback) into a customer-facing policy draft. Counsel review queued for Phase 4.
- **Why:** §6.7 is internal policy form. Customer-facing form needs plain-language drafting + legal review. Required for pricing-page footer link + Stripe customer portal.
- **Dependency:** §6.7; PACKAGING `Upgrade Path Design` (NEXT).
- **Output:** Customer-facing refund + billing policy MD draft. Feeds **Pr2-5**.

**`[METRICS] PRICING — Conversion Benchmarks and KPI Targets`**
- **Objective:** Lock the §6.9 base-case conversion rates as Phase 2 KPI targets with explicit upside/downside thresholds and falsifier conditions.
- **Why:** Phase 2 cannot exit without locked KPI baselines. §13 KPI/OKR system inherits from this.
- **Dependency:** §6.9 sensitivity inputs; PACKAGING `Free vs Paid Boundary`.
- **Output:** KPI target table — name, definition, base / upside / downside, source, falsifier.

**`[QA] PRICING — Stripe Plan Mapping Review`**
- **Objective:** Audit Stripe products / prices / coupons / promo codes against locked Track B + founder-cohort + discount policy. Verify entitlement integration matches per `_packaging/04-premium-feature-gating-rules.md` §6.
- **Why:** Stripe drift is the single most expensive billing failure mode. Audit before any pricing change ships and before the founder-cohort window opens.
- **Dependency:** Track B locked; founder-cohort policy locked; Stripe Atlas account configured; entitlement YAML.
- **Output:** Stripe audit report + remediation backlog.

### LATER

**`[DOC] PRICING — Team and Institutional Pricing Concept`**
- **Objective:** Concept the team / institutional pricing surface for Phase 5 Desk Full v2 + per-seat scaling, including anything beyond the seat model (volume discounts, multi-account institutional packaging).
- **Why:** Phase 5 input. Concept-only in Phase 2.
- **Dependency:** PACKAGING `Fund/Desk Plan Concept` (NEXT, concept-only); Layla Phase-5 Pre-read.
- **Output:** Concept MD; *no commitments*.

**`[FINANCE] PRICING — Revenue Mix Scenario Analysis`**
- **Objective:** Three-scenario revenue projection (conservative / base / aggressive) using the sensitivity model. Inputs to fundraising narrative in Phase 4.
- **Why:** Phase 4 fundraising deck needs this; producing the structure now reduces Phase 4 ramp.
- **Dependency:** Price-to-Margin Sensitivity Model; Conversion Benchmarks.
- **Output:** Revenue mix MD + scenario tables.
