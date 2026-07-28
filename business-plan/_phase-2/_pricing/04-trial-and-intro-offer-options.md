# PRICING — Trial and Intro Offer Options

**Task:** `[DOC] PRICING — Trial and Intro Offer Options`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — recommends **no free trial**; founder-cohort + beta-access offers are the intro-offer set
**Feeds decision:** **Pr2-3**
**Anchored to:** §6.5 Free Scope B (LOCKED); §6.7 founder-cohort policy; PRICING `02-initial-pricing-philosophy.md` Principles 1, 4, 5; PACKAGING `Beta Access Offer Design` (NEXT, **Pk-6**); `_packaging/05-packaging-friction-review.md` Class C anti-patterns.

---

## TL;DR

**Recommend: no free trial of paid tiers.** Free Scope B is the substitute and is permanent. Two intro offers exist, both anchored to specific cohort moments:

1. **Founder-cohort discount** (per §6.7) — 25–30% off, 60-day window after public launch, locks through 1 renewal cycle.
2. **Beta-access offer** (per `_packaging/Beta Access Offer Design`, NEXT, **Pk-6**) — terms for P0 → P1 transition cohort.

Three trial alternatives evaluated and rejected. One conditional revision path defined.

---

## 1. Why no free trial

### Reason 1 — Free Scope B is the trust demo

Per §6.5, Free is **account-verified, includes the regime label + top-5 delayed signals + demo-trade gate behavior + methodology docs**. This is a working trust demo, not a stripped product. A 14-day Trader trial would *replace* the Free Scope B value proposition with a time-limited paid-tier preview, breaking the §3.5 "we'll be back" sub-$5k branch and the trust-demo positioning.

### Reason 2 — Trial-then-charge violates Principle 4 (anti-surprise)

Per `02-initial-pricing-philosophy.md` Principle 4 — pricing is predictable, no surprise charges. Auto-converting trials with card-on-file are the highest-trust-cost mechanic in SaaS pricing (Class C anti-pattern in `_packaging/05-packaging-friction-review.md`). Even with reminders, ~30% of trial-converters report unintended charge in industry surveys (INFERENCE, varies by study).

### Reason 3 — Trial creates adverse-selection at the wrong moment

A free Trader trial attracts the price-sensitive end of the funnel — the same segment §3.5 explicitly de-prioritizes (sub-$5k disciplined are addressed via Free Scope B + "we'll be back" framing; casual-retail are anti-ICP). A trial without a price filter brings in casual users who churn out within the first cycle without ever validating Trader-tier WTP.

### Reason 4 — Trial cannibalizes founder-cohort

Founder-cohort is the time-bounded conversion incentive. A simultaneous free trial competes for the same conversion event, dilutes both signals, and violates Principle 3 (time-bounded, non-stackable).

### Reason 5 — Support load + entitlement complexity

A trial mechanic adds: trial-state Stripe configuration, trial-state entitlement flag (per `_packaging/04-premium-feature-gating-rules.md` §6 entitlement schema), trial-conversion notifications, trial-failed-conversion edge cases, and refund-handling for "I forgot to cancel." All add support load without conversion lift commensurate with the cost.

---

## 2. Three trial alternatives evaluated and rejected

### Alternative T1 — 14-day free Trader trial with card-on-file, auto-convert

**Shape:** New user enters card; gets 14 days of full Trader; auto-charges $79 on day 15 unless cancelled.

**Industry conversion benchmark:** 40–60% trial-to-paid conversion (INFERENCE for SaaS; crypto-tooling tends lower).

**Pro:** High conversion mechanic; standard SaaS pattern; lifts Free → Trader rate.

**Con:**
- Violates Principle 4 (Reason 2). Card-on-file + auto-convert = surprise charge for a meaningful fraction of users.
- Trust-load violation per §6.10 anti-overclaim discipline. Pricing surface that auto-charges erodes the BRAND voice.
- Cannibalizes Free Scope B's role (Reason 1). Free becomes "the option for people who didn't enter a card" rather than the trust demo.
- Class C anti-pattern in `_packaging/05-packaging-friction-review.md`. Refund-then-cancel pattern requires anti-abuse policy enforcement.

**Reject.** Conversion lift not worth trust cost.

### Alternative T2 — 7-day Trader trial without card-on-file, manual convert

**Shape:** New user gets 7 days of Trader without entering payment; must explicitly subscribe at end of trial to continue.

**Industry conversion benchmark:** 5–15% trial-to-paid conversion (INFERENCE).

**Pro:** No surprise charges (Principle 4 preserved). Less aggressive than T1.

**Con:**
- Still cannibalizes Free Scope B's positioning. Free becomes "what you have after the 7-day Trader expires."
- 5–15% conversion is roughly equivalent to the §6.9 base case Free → Trader rate (5%) at higher operational cost (entitlement state for trial users + reminder emails + support burden for "where did my features go" tickets).
- Adverse-selection still operative — short trial filters for users who have time *this week*, not users who actually fit Trader.

**Reject.** Marginal lift over Free Scope B; meaningful operational drag; positioning cost.

### Alternative T3 — 30-day money-back guarantee on Trader (no trial mechanic)

**Shape:** No trial. Customer pays $79; if dissatisfied within 30 days, full refund. (This is a *policy*, not a *trial*.)

**Note:** §6.7 already commits a 14-day money-back guarantee for first-time paid customers. T3 would extend it to 30 days for Trader specifically.

**Pro:**
- Preserves Free Scope B positioning (no trial mechanic).
- Increases Trader-tier confidence (longer return window).
- Aligns with Principle 4 (reversibility).

**Con:**
- Adds support load: 14d → 30d roughly doubles refund-handling volume.
- Anti-abuse complexity: longer window enables more sophisticated refund-then-resubscribe patterns.
- Tier-non-uniform: Why 30d for Trader and 14d for DP/DF? Either uniform or principled exception.

**Conditional.** Defer to **Pr2-5** (refund SLA per tier). If Pr2-5 lands at uniform 14d (recommended), T3 is rejected. If Pr2-5 lands at tier-tiered (option b), T3 is implicit in that decision.

---

## 3. The two intro offers we *do* run

### Intro offer 1 — Founder-cohort discount (per §6.7)

| Mechanic | Spec |
|---|---|
| Eligibility | Sign-ups during the first 60 days post-public-launch (P2 phase per §5.4). Soft-launch users (P0/P1) automatic. |
| Discount magnitude | 25–30% off standard pricing per §6.6 numbers |
| Applies to | Monthly billing within the 60-day window. Not stackable with annual. |
| Lock duration | One renewal cycle from signup; converts to standard pricing at next renewal |
| Stripe implementation | Time-bounded promo code; per-customer single-use; auto-expires |
| Communication | "Founder-cohort pricing available through [LAUNCH DATE + 60 days]." Account dashboard shows next-renewal price. 14-day-prior expiration notification. |
| Anti-Flag-1 mitigation | Never "lifetime," "forever," "always." Canonical phrasing only. |

**Why this works as an intro offer:** time-bounded (Principle 3), explicit (Principle 2), reversible by user (Principle 4), and pays for the early-supporter risk premium without setting bad pricing precedents (Principle 5).

### Intro offer 2 — Beta-access offer (per `_packaging/Beta Access Offer Design`, NEXT, Pk-6)

| Mechanic | Spec (TBD per Pk-6) |
|---|---|
| Eligibility | P0 → P1 transition cohort (validation cohort cap 40 per §14) |
| Form | TBD — three options under evaluation in Pk-6: (a) automatic founder-cohort pricing, (b) 30-day Trader extension at grandfathered price, (c) free Trader for first 90 days of P1 |
| Lock duration | TBD per option chosen; bounded |
| Communication | Direct cohort comms, not pricing-page-public |
| Coordination | Documented in Pk-6 (PACKAGING) and Pr2-3 (PRICING) jointly |

**Why this works as an intro offer:** rewards early users without setting bad pricing precedents (per `_packaging/01-packaging.md` §8 NEXT rationale). Distinct from founder-cohort because P0 cohort members get explicit cohort-level treatment, not a generic post-launch discount.

---

## 4. Conditional revision path

If Pr2-1 revision triggers fire post-cohort and any of the following surfaces from cohort feedback:

| Trigger | Possible response | Notes |
|---|---|---|
| ≥30% of cohort cite "no way to evaluate Trader before paying" as conversion blocker | Reopen Pr2-3; reconsider Alternative T2 (7-day no-card trial) | Free Scope B clearly insufficient as trial-substitute for the surveyed cohort |
| ≥40% of cohort cite "$79/mo first-month commitment too high" | Consider Alternative T3 (30-day money-back guarantee on Trader) | Indicates trust gap, not trial gap |
| Founder-cohort uptake <40% in window | Reopen Pr2-4; deepen founder-cohort to 33% OR widen window to 90 days | Per `01-pricing-strategy-recommendation.md` revision trigger #4 |

If none surface: hold no-trial posture; preserve Free Scope B as substitute; ratify Pr2-3 at "no free trial."

---

## 5. Failure modes specific to intro offers

- **Founder-cohort comms drift to "lifetime."** §6.10 Flag 1. Single canonical phrasing only.
- **Beta-access offer extends past P0 → P1 transition window.** Becomes de facto generic discount; cannibalizes founder-cohort.
- **Stacking attempts.** Founder-cohort + annual + beta-access stacked = race-to-bottom signal. Stripe configuration must enforce mutual exclusion at the promo-code level.
- **Beta-access "free for 90 days" option (Pk-6 option c).** Highest cohort-affinity but riskiest — sets expectation that future cohorts get free access. Pk-6 evaluation must weigh this.
- **Auto-renewal of founder-cohort pricing.** If Stripe auto-renews at the founder-cohort price beyond the lock window, system-level Flag-1 violation. QA must verify this.

---

## 6. What this unlocks

- **Pr2-3** can be marked recommended at "no free trial; Free Scope B is the substitute."
- Pricing-page copy can avoid trial-related surfaces entirely.
- Stripe configuration scoped to: standard prices + founder-cohort time-bounded promo + (TBD per Pk-6) beta-access offer.
- `[QA] PRICING — Stripe Plan Mapping Review` (NEXT) inherits the no-trial constraint as an audit failure if any trial product / coupon exists in Stripe.
- Phase 3 GTM cannot quietly add a trial mechanic without explicit Pr2-3 reopen.
