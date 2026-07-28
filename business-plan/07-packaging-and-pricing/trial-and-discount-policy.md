# Trial and Discount Policy

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** §6.5 (Free tier scope) + §6.7 (Refund / discount / founder-cohort) — both LOCKED v1

---

## 1. Philosophy

Trials and discounts are **trust filters, not conversion levers** at validation phase. The goal is to build a cohort that is:

- ICP-aligned (P1 Omar primary)
- Anti-ICP filtered (sub-$5k disciplined routed to "we'll be back"; copy-trade and alpha-seekers blocked at brand-voice and signup)
- Sized to what founder-led ops can support (40-user P1 cap)
- High-signal on retention, rule-respect, and referral

Every mechanic below is evaluated by: **does it improve cohort signal quality, or just inflate signups?** Mechanics that pass the first test ship; mechanics that fail it are rejected even if they would lift conversion in a normal SaaS context.

---

## 2. Recommended trial structure

### Decision: Free-as-evergreen-entry, not time-bounded paid trial

**Recommendation:** Use the **locked Free tier as the evergreen evaluation path**. Do **not** introduce a time-bounded paid trial during P1 or P2.

**Reasoning:**

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| **Free tier as evergreen entry (locked Scope B per §6.5)** | Already shipped; ICP-filtered ("we'll be back" for sub-$5k); zero billing friction; matches P1 Omar's slow-evaluation pattern | Doesn't expose paid-tier capability before payment; some buyers want to "feel" Trader before committing | **Recommended** |
| **14-day free trial of Trader (no card)** | Lowers commitment threshold; lets P2 Karim run buy-vs-build comparison properly | Adds support load for non-buyers; weakens cohort signal; can be gamed by anti-ICP signups | Reject at P1 |
| **14-day free trial of Trader (card on file)** | Filters serious buyers; converts to paid by default | Creates a refund-equivalent that complicates the 14-day money-back guarantee; messy stack with founder-cohort discount | Reject at P1 |
| **30-day demo-mode (live data, no real config)** | Showcases engine fidelity; useful for P3 Layla evaluation | Adds product surface area; ops cost; degrades cohort quality | Reject at P1; revisit P2 |
| **Money-back guarantee on first month (no separate trial)** | Clean — buyer commits, has a 14-day backout | Requires upfront billing | **Already locked § 6.7 — ship as primary trial mechanism** |

The **operative trial mechanism is the 14-day money-back guarantee on the first paid charge** (§6.7), paired with the **evergreen Free tier** (§6.5) for pre-purchase evaluation. No additional time-bounded trial during P1 or P2.

**DECISION NEEDED — revisit at P2 close (Sep 2026):** if cohort data shows P3 Layla evaluations consistently stalled before paid signup, consider a 14-day demo-mode for Desk Preview specifically. Do not implement broadly.

---

## 3. Free tier as the evaluation path

**The Free tier already ships as a controlled evaluation experience** (§6.5 Scope B). Its job is **not** to be a feature trial; its job is to:

1. **Verify the user has an exchange account** (any size, account-verified at signup).
2. **Show capability without giving paid-tier surface area away.** Read-only top-5 signal list (delayed, daily refresh), per-symbol regime label without confidence, demo-trade view of the risk gate, capital-preservation primitives on demo trades.
3. **Filter for ICP fit.** Sub-$5k disciplined users get the "we'll be back" path — they are recognized as future ICP, prompted at the $5k threshold, and not pressured.
4. **Pre-build trust via methodology documentation.** Engine methodology, validation-phase status, and the "What CoinScopeAI does not do" reference page are public regardless of tier — readable on Free.

The Free tier is **deliberately not journal-access, not real-time signals, not Telegram bot, not API.** Per §5.3.2 packaging principle — no paid-feature exception on Free.

### What Free is **not** allowed to do

- It is not allowed to nag sub-$5k users to upgrade. The "we'll be back" copy is the product.
- It is not allowed to hide validation-phase status. The disclaimer is visible on every Free surface.
- It is not allowed to surface a "Pro upgrade modal" on every signal click. ICP-aligned restraint is the conversion mechanism.
- It is not allowed to expire. There is no "Free for 30 days" — Free is evergreen.

---

## 4. Discount policy guardrails

Locked v1 per §6.7 + §5.3.5. Restated here for operator clarity.

### Standard discounts

| Discount type | Magnitude | Window | Stackable? | Locked? |
|---|---|---|---|---|
| **Annual prepay** | ≈17% (10 months for the price of 12) | Always available at all paid tiers | No (does not stack with founder-cohort) | ✅ Locked |
| **Founder cohort** | ≈25–35% off standard pricing (specific per-tier values per §6.6 — the partner read-only seat lands at ≈34%, the upper end of the band) | First 60 days post-public-launch (P2). Soft-launch (P1) users get founder-cohort pricing automatically | No (does not stack with annual prepay) | ✅ Locked |
| **Promotional pricing** | ≤25% off, time-bounded | ≤30 days, auto-revert to standard | No (does not stack with founder-cohort or annual prepay) | ✅ Locked |
| **Partnership-driven discount** | Case-by-case, ≤25% off | Time-bounded, explicit terms | No (cannot stack) | Approved on a per-deal basis |
| **Affiliate / referral revenue share** | None at v1 | n/a | n/a | ❌ Not allowed at P1–P2 |

### Anti-stacking enforcement

- A customer can be on **at most one** discount mechanism at any time.
- The system enforces single-discount-per-account at the Stripe promo-code layer (no two promo codes apply to the same subscription).
- Founder-cohort + annual prepay: the customer chooses one path. The pricing page makes this choice explicit.
- Promotional pricing during a founder-cohort window: not allowed. We do not run sales on top of founder-cohort.
- Partnership discounts during a founder-cohort window: not allowed. Partnerships during P1–P2 are deferred per §8.

### Maximum discount ceiling

- **No standard tier price is ever discounted by more than 35%** without explicit founder approval.
- 25% is the conventional ceiling for promotional pricing; ≈25–35% is the locked range for founder-cohort exclusively (specific per-tier values per §6.6 — the partner read-only seat at $99 / $149 lands at the upper end of the band).
- The ceiling exists to protect price credibility on next-renewal and to avoid race-to-the-bottom signaling against competitors.

### Discount communication rules

Per §6.10 Flag 1, never use any of:

- "lifetime", "forever", "always", "founder discount locked-in"
- "limited-time forever" (oxymoron, do not use)
- "permanent founder pricing"
- "grandfather pricing"
- "lock in this rate forever"

Acceptable language:

- "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies."
- "Annual prepay — pay yearly, save ≈17%."
- "Promotional pricing — ends [DATE]. Auto-reverts to standard at next renewal."

---

## 5. Refund logic

Locked v1 per §6.7. Operator restatement:

### 14-day money-back guarantee

- Available on **first-time paid customers** at any tier.
- **Single-use per account.** Triggered by the first paid charge regardless of tier; subsequent re-signups do not get a fresh 14-day window.
- Applies to monthly and annual subscriptions.
- Annual prepay refunds are **pro-rated only within the 14-day window**. After day 14, annual is locked through the term — user can cancel at next renewal.

### After day 14

- **No refunds.**
- User can cancel anytime; access remains until end of current billing period.
- For annual: access remains for the full annual term.

### Per-seat refunds (Desk Full v2 only)

- First-time-seat-add gets the 14-day window.
- Subsequent additions are non-refundable but cancel at next renewal.

### Anti-abuse

- The 14-day guarantee is **not stackable** across re-signups.
- Account-level enforcement: one refund window **per email or payment method, whichever is more restrictive**.
- Refund-then-resubscribe pattern: anti-abuse caps refunds at one per account lifetime.
- Chargebacks: account immediately suspended pending review. Chargeback abuse triggers permanent ban.

### Failed payment handling

- Retry 3 times over 7 days.
- Account moves to "past due" with read-only access.
- After 14 days past due → suspended.
- Data retained per cancellation policy (90 days for reactivation).

### Mid-cycle changes

| Change | Effective | Refund? |
|---|---|---|
| Tier upgrade | Immediate | None — pro-rated charge for remainder of period |
| Tier downgrade | Next renewal | No immediate refund |
| Per-seat add | Immediate | Pro-rated charge |
| Per-seat remove | Next renewal | None |
| Annual ↔ monthly | Renewal boundary only | n/a |

---

## 6. Promotional pricing constraints

Promotions during P1–P2 are constrained, deliberately.

### What is allowed

- **One** time-bounded promotional event coinciding with **P2 public launch** (Aug–Sep 2026).
- ≤25% off, ≤30-day window, auto-revert to standard at next renewal.
- Promotion cannot stack with founder-cohort or annual prepay.
- Promotion cannot apply to **Desk Full v2** (preserve the v2 anchor).
- Promotion copy must include the end-date and the standard-pricing post-revert price.

### What is not allowed

- Standing discount programs ("get 20% off forever if you refer 3 friends" — no).
- Discount stacking under any combination.
- Cyber-Monday / seasonal sale framing — incongruent with anti-overclaim posture.
- "Black box" promo codes shared in influencer or copy-trade channels — anti-ICP.
- Co-marketing or bundled promotions with anti-ICP products (signal groups, copy-trade products, leverage-maximizer content).
- Affiliate-driven discount classes — deferred to post-P5 with brand-voice review gate.
- Permanent "loyalty" or "tenure-based" discounts. Pricing is the same on M1 as on M36.

### Partnership-driven discounts (e.g., prop-firm partnerships per §8)

- Structured as **fixed-amount or percentage discount** with explicit time-bounded terms.
- Single founder approval required per partnership.
- Maximum discount: 25% off standard pricing for the partnership-cohort users.
- Partnership terms include a sunset date — no permanent affiliate discount classes.

---

## 7. How to avoid attracting low-fit users

Trial / discount design is a **filter**, not just an offer. The following mechanics are explicit ICP-fit guards.

| Mechanic | What it filters | Where it sits |
|---|---|---|
| **Free tier requires exchange account verification** | Casual / curious / non-trader audiences | Signup form |
| **US-residents blocked at signup** | US regulatory audience | Signup form |
| **Free tier sub-$5k → "we'll be back" routing** | Sub-$5k disciplined treated as future ICP, not pressured to convert | Account-size detection at signup |
| **Free tier excludes journal / real-time / Telegram / API** | Anti-ICP looking for free signals or copy-trade adjacency | Feature-gating |
| **No "free trial of full Trader" with no card** | Anti-ICP looking for short-term extraction | Trial mechanism choice |
| **14-day money-back single-use per account/email/payment method** | Refund abuse / serial-resignup pattern | Stripe + DB enforcement |
| **No co-marketing with signal groups, copy-trade, leverage maximizers** | Adjacent anti-ICP audience contamination | §5.3.3 + brand-voice review |
| **No affiliate or referral revenue share at P1–P2** | Affiliate-driven low-quality cohort | Locked off at v1 |
| **No volume / per-trade pricing** | "Pay-per-trade" adverse-incentive audience | §6.3 — Model C |
| **Pricing-page validation-phase disclosure** | Buyers who reject testnet-first / validation posture self-select out | Pricing page surface |
| **No "win rate" or "ROI" copy on pricing page** | Alpha-seeking audience self-selects out | §6.10 anti-overclaim audit |

The combined effect is a funnel that **converts at lower volume but higher cohort quality** than a typical SaaS pricing page would. That is the explicit goal.

---

## 8. How trial structure should align with trust and onboarding readiness

The trial mechanism must match the operating posture. Three alignment points:

### 8.1 Onboarding-readiness alignment

The Free tier requires **account verification** at signup. This is operationally heavier than a no-card free tier — users must complete an exchange-account verification step. The cost is signup friction; the benefit is cohort-quality signal from the first interaction.

Cross-reference `12-onboarding-and-activation/` (Wave 2 next folder). The signup-to-exchange-connection flow is the gating step; if onboarding readiness is low (engine instability, exchange API issues), the trial mechanism cannot exceed onboarding capacity.

**Implication:** during a known-degraded period (vendor incident, post-deploy stabilization), Free signups can be temporarily paused. The trial mechanism does not promise a level of access that ops cannot uphold.

### 8.2 Trust-readiness alignment

A trial mechanism is a trust commitment. The 14-day money-back guarantee says **"we will return your money without arguing if you don't see value within two weeks."** That commitment requires:

- A clean refund process (Stripe-native, no manual dunning)
- A documented support workflow for refund requests (`13-support-and-trust-ops/`)
- A founder-level commitment to honor refunds without escalation, even on edge cases

If any of those are not in place, the 14-day guarantee should not ship. At P1, all three are in place.

### 8.3 Cohort-readiness alignment

The trial mechanism must produce cohort observation data that §3.7 / §3.8 can analyze. This means:

- Free signups capture: account size band, geography, source attribution, methodology indicators (read time on docs, demo-trade engagement)
- Paid signups capture: tier choice, monthly vs. annual, founder-cohort eligibility, discount applied
- Refund requests capture: reason category (bug, fit, expectation mismatch), time from signup to refund

Cross-reference `business-plan/_data/operations/Validation_Data_Analysis_Plan_v1.md`. The trial mechanism instruments the cohort; it is not just a billing artifact.

---

## 9. Specific operator decisions and locks

| # | Decision | Status | Owner |
|---|---|---|---|
| **TD1** | No time-bounded paid trial during P1–P2 | Recommended (this file §2) | Founder |
| **TD2** | 14-day money-back guarantee, single-use per account | Locked §6.7 | Founder |
| **TD3** | Free tier evergreen, no expiry | Locked §6.5 | Founder |
| **TD4** | Anti-stacking enforcement at Stripe promo-code layer | Required pre-P1 | Founder + Stripe ops |
| **TD5** | One time-bounded promo at P2 launch (≤25%, ≤30 days, no Desk Full v2) | Recommended (this file §6) | Founder + GTM owner |
| **TD6** | No affiliate / referral revenue share at P1–P2 | Locked §6.7 | Founder |
| **TD7** | "Founding-member pricing" copy locked, no "lifetime" framing | Locked §6.10 Flag 1 | Founder + brand-voice review |
| **TD8** | Founder-cohort applies to soft-launch P1 users automatically; 60-day window applies to P2 public launch | Recommended (this file + `pricing-strategy.md`) | Founder |
| **TD9** | Free tier sub-$5k "we'll be back" messaging is ICP-aligned, not nagware | Locked §6.5 | Founder + design |
| **TD10** | Pricing-page validation-phase disclosure visible (not footer) | Locked §6.10 Flag 2 | Founder + design |

---

## 10. Open questions

Carried over plus introduced by Wave 2:

1. **DECISION NEEDED — Demo-mode for Desk Preview at P2.** If P3 Layla evaluations stall before paid signup, do we ship a 14-day demo-mode? Revisit at P2 close.
2. **DECISION NEEDED — Refund-reason capture.** Add a structured "reason for refund" field to the cancel/refund flow? Recommended, but adds friction; needs design review.
3. **REQUIRED INPUT — Counsel sign-off on refund policy language** (especially "single-use per account/email/payment method, whichever more restrictive"). Cross-reference `_data/legal/Counsel_Brief_v2.md`.
4. **REQUIRED INPUT — Stripe configuration of time-bounded promo codes that auto-revert.** Confirm 60-day eligibility window is configurable; confirm anti-stacking is enforceable.
5. **ASSUMPTION — Free tier conversion rate base case 5%.** §6.9 sensitivity #2; validate at P1 cohort review (M3).
6. **ASSUMPTION — 14-day refund rate stays under 5%.** Industry typical is 2–4%; if higher, reason-capture analysis identifies whether it's a fit problem or a product problem.
7. **OPEN — Reactivation pricing.** §6.7 says reactivation within 90 days restores prior tier and pricing. Confirm reactivation **does not** reactivate founder-cohort discount if outside the original eligibility window.
8. **OPEN — Per-seat 14-day refund handling at Desk Full v2.** Confirm first-time-seat-add gets the 14-day window even on a non-first-time account.

---

## 11. Cross-references

- §6.5 Free tier scope: `business-plan/06-pricing-monetization.md` §6.5
- §6.7 Refund / discount / founder-cohort: `business-plan/06-pricing-monetization.md` §6.7
- §6.10 Anti-overclaim audit: `business-plan/06-pricing-monetization.md` §6.10
- Plan matrix: `07-packaging-and-pricing/plan-matrix.md`
- Pricing strategy: `07-packaging-and-pricing/pricing-strategy.md`
- Onboarding (forthcoming): `12-onboarding-and-activation/`
- Support ops (forthcoming): `13-support-and-trust-ops/`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Validation data analysis plan: `business-plan/_data/operations/Validation_Data_Analysis_Plan_v1.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
