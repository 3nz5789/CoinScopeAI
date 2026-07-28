# PRICING — Monthly vs Annual Offer Structure

**Task:** `[DOC] PRICING — Monthly vs Annual Offer Structure`
**Type:** NOW
**Owner:** Strategy CoS + FinOps
**Status:** DRAFT v0.1 — recommends ratifying ~17% annual discount; mix-sensitivity table provided
**Feeds decision:** **Pr2-2**
**Anchored to:** §6.6 prices LOCKED; §6.7 mid-cycle changes; §6.9 annual-mix base case; PRICING `02-initial-pricing-philosophy.md` Principle 3 (time-bounded, non-stackable).

---

## 1. The offer in one paragraph

Two billing cadences per paid tier: monthly (no commitment, no discount) and annual prepay (~17% discount, single charge, locked through term). Annual is **not** the default — both prices are visible side-by-side on every paid tier card. Customers choose explicitly. Annual cannot stack with founder-cohort. Switching cadence is allowed only at renewal boundary, not mid-cycle.

---

## 2. Discount math (per §6.6)

| Tier | Monthly | Annual prepay | Implicit monthly | Discount magnitude | Months "free" |
|---|---|---|---|---|---|
| Trader | $79 | $790 | $65.83 | 17% | 2.0 of 12 |
| Desk Preview | $399 | $3,990 | $332.50 | 17% | 2.0 of 12 |
| Desk Full v2 | $1,199 | $11,990 | $999.17 | 17% | 2.0 of 12 |
| Partner read-only seat | $149 | $1,490 | $124.17 | 17% | 2.0 of 12 |
| Analyst seat | $249 | $2,490 | $207.50 | 17% | 2.0 of 12 |

The "10 months for the price of 12" (~17%) is consistent across all tiers. Per §6.6 rationale:

- **Cash flow.** Annual prepay smooths revenue and reduces working-capital needs at the founder/operator scale modeled in §11.
- **Retention.** Annual commitment reduces involuntary churn and gives §13 cohort retention metrics cleaner monthly cohorts.
- **Anchor.** Monthly price is the reference; annual is the discount. Avoids signaling that monthly is overpriced.

---

## 3. Annual-mix base case (per §6.9)

Recommended Phase 2 base case for §11:

| Tier | Annual mix base | Annual mix upside | Annual mix downside | Reasoning |
|---|---|---|---|---|
| Trader | 40% | 55% | 25% | P1/P2 buyers test before commitment; expect lower annual mix at entry tier |
| Desk Preview | 60% | 75% | 45% | P3 buyers expect predictable budget; annual aligns with their book-management cadence |
| Desk Full v2 | 75% | 90% | 60% | P3 scaling buyers commit; partner / analyst seats also annual-skewed for budget alignment |

§13 KPI tracks actual annual mix per tier; downside / upside thresholds trigger Pr2-2 reopening if breached for two consecutive quarters.

---

## 4. Mix-sensitivity table (annualized revenue per 100 paid customers)

Toy model — single snapshot, ignores churn, ignores per-seat density variance, ignores founder-cohort drag. Purpose: visualize annual-mix sensitivity per tier.

### Trader (100 customers)

| Annual mix | Monthly cohort revenue | Annual cohort revenue | Total ARR per 100 | Notes |
|---|---|---|---|---|
| 25% (downside) | 75 × $948 = $71,100 | 25 × $790 = $19,750 | **$90,850** | Lowest mix; preserves margin (no discount drag) but worst working capital |
| 40% (base) | 60 × $948 = $56,880 | 40 × $790 = $31,600 | **$88,480** | Recommended base case |
| 55% (upside) | 45 × $948 = $42,660 | 55 × $790 = $43,450 | **$86,110** | Best working capital + retention; ~3% revenue draw vs downside |

Annual mix shifts ARR by ~5% at the tier level; the working-capital benefit (cash collected up-front) dominates the small revenue draw.

### Desk Preview (100 customers)

| Annual mix | Monthly cohort revenue | Annual cohort revenue | Total ARR per 100 |
|---|---|---|---|
| 45% (downside) | 55 × $4,788 = $263,340 | 45 × $3,990 = $179,550 | **$442,890** |
| 60% (base) | 40 × $4,788 = $191,520 | 60 × $3,990 = $239,400 | **$430,920** |
| 75% (upside) | 25 × $4,788 = $119,700 | 75 × $3,990 = $299,250 | **$418,950** |

### Desk Full v2 (100 customers, base case)

Excluding per-seat add-ons; assumes 1 PM seat only.

| Annual mix | Monthly cohort revenue | Annual cohort revenue | Total ARR per 100 |
|---|---|---|---|
| 60% (downside) | 40 × $14,388 = $575,520 | 60 × $11,990 = $719,400 | **$1,294,920** |
| 75% (base) | 25 × $14,388 = $359,700 | 75 × $11,990 = $899,250 | **$1,258,950** |
| 90% (upside) | 10 × $14,388 = $143,880 | 90 × $11,990 = $1,079,100 | **$1,222,980** |

### Cross-tier read

- ARR is mildly *negatively* sensitive to annual mix (more annual → less ARR) at every tier because of the 17% discount.
- Working-capital benefit (cash-up-front × annual mix) is positively sensitive — the higher the annual mix, the lower the working capital required to operate.
- §11 should model both ARR and free cash flow; the trade-off is the load-bearing decision, not ARR alone.

---

## 5. Switching rules (per §6.7)

| Direction | Behavior | Reasoning |
|---|---|---|
| Monthly → Annual | Allowed at renewal boundary only. Not mid-cycle. | Avoids partial-month proration math and anti-abuse (re-up to capture annual discount during long-month cycles). |
| Annual → Monthly | Allowed at renewal boundary only. Not mid-cycle. No early-termination refund for annual. | Annual is a 12-month commitment with 14-day refund window per §6.7. |
| Mid-cycle tier upgrade with cadence change | Cadence stays same, tier upgrades immediately with pro-rated charge. | One change at a time; cadence change deferred to next renewal. |
| Founder-cohort + annual | Mutually exclusive. Customer picks one. | Per §6.7 — no stacking. |
| Annual + promotional discount | Mutually exclusive. Customer picks one. | Per §6.7 — no stacking. Annual is the standard discount. |

**Anti-pattern guard:** never quietly auto-default a customer to annual at first signup. Both options are equally surfaced; the customer chooses.

---

## 6. Founder-cohort interaction

Per §6.7 (full):

- **Founder-cohort applies only to monthly billing within the 60-day window.** Annual prepay locks at the standard ~17% discount, not stackable with founder-cohort.
- **Customer chooses.** Monthly + founder-cohort (e.g., $59/mo for Trader) for 1 renewal cycle, OR annual + standard discount ($790/yr).
- **Math on the choice for Trader:**
  - Monthly + founder-cohort: $59 × 12 = $708 (then $79 × 12 = $948 from year 2)
  - Annual + standard: $790 × 12 = $790 (locked) + ~17% discount in year 2 if renewed annually
  - Year-1 customer pays slightly less on monthly + founder-cohort ($708 vs $790); year-2 onward, annual prepay wins.
  - Trade-off communicated honestly on pricing page; customer picks fit.

This dual-incentive structure naturally segments year-1-experimenters (monthly + founder-cohort) from year-1-committers (annual + standard discount). Both are valid; both are discounted; neither stacks.

---

## 7. Founder-cohort window mechanics

| Mechanic | Spec |
|---|---|
| Eligibility | Sign-ups during the first 60 days post-public-launch (P2 phase per §5.4 roadmap) |
| Soft-launch users (P0/P1) | Get founder-cohort pricing automatically, no window check |
| Discount magnitude | 25–30% off standard pricing per §6.6 numbers ($79 → $59, $399 → $299, $1,199 → $899, $149 → $99, $249 → $179) |
| Lock duration | Founder-cohort price locks through one renewal cycle from signup |
| Stripe implementation | Time-bounded promo code; auto-expires after 60 days; per-customer single-use |
| Communication | Pricing-page sub-header: "Founder-cohort pricing available through [LAUNCH DATE + 60 days]." Account dashboard shows "Founding-member pricing — locked through [NEXT RENEWAL DATE]." |
| Anti-Flag-1 mitigation | Never use "lifetime," "forever," "always," "founder discount locked-in." Single canonical phrasing. |

---

## 8. Pre-renewal notification

Per `_packaging/05-packaging-friction-review.md` design rule 5 (self-serve everything) and Class B anti-pattern (auto-renewal without notification):

| Cadence | Notification | Reasoning |
|---|---|---|
| Monthly | 7 days prior to renewal | Sufficient lead time to cancel without missing the cycle |
| Annual | 30 days prior to renewal | Annual is a larger commitment; longer lead time appropriate |
| Founder-cohort expiring | 14 days prior to expiration with explicit price-change notice | Critical anti-Flag-1 mitigation — customer knows the founder rate is ending |
| Per-seat addition / removal | At time of change, with confirmation of next-billing-cycle effect | Per §6.7 mid-cycle changes |

Notification delivered via email + in-app banner. (REQUIRED INPUT — confirm Stripe Atlas configuration supports this notification cadence natively, or build email layer.)

---

## 9. Mix-sensitivity decision register

| If observed | Action | Rationale |
|---|---|---|
| Annual mix on Trader < 25% for 2 consecutive quarters | Reopen Pr2-2; consider 20% annual discount (vs current 17%) | Downside breached; need stronger annual incentive |
| Annual mix on Desk Preview < 45% for 2 consecutive quarters | Reopen Pr2-2; investigate Desk Preview annual-objection cause | Downside breached; segment-specific |
| Annual mix on Desk Full v2 > 90% sustained | No action; this is upside | Working capital + retention both improve |
| Trader churn on annual cohort < 60% / 12-month retention | Continue ratifying current ~17% | Retention assumption holding |
| Founder-cohort uptake < 40% in window | Consider widening window to 90 days OR deepening to 33% (max) | Per `01-pricing-strategy-recommendation.md` revision trigger #4 |

---

## 10. What this unlocks

- **Pr2-2** can be marked recommended at ~17% annual discount (10 of 12 months).
- §11 financial model has annual-mix base case + sensitivity inputs.
- Pricing page has explicit dual-cadence rendering spec.
- §13 KPI framework gets annual-mix-by-tier as a tracked metric.
- Stripe configuration spec includes founder-cohort + annual mutually-exclusive promo logic.
