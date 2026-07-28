# PRICING — Pricing Strategy Recommendation

**Task:** `[RESEARCH] PRICING — Pricing Strategy Recommendation`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — pending P0 cohort exit memo for ratify-or-revise lock
**Feeds decision:** **Pr2-1**
**Anchored to:** §6.6 Track B (LOCKED 2026-05-01); §6.2 WTP per persona; §6.9 LTV/CAC sensitivity; PACKAGING `01-tier-structure-recommendation.md`.

---

## TL;DR

**Recommend: ratify §6.6 Track B numbers as the Phase 2 lock.** Hold prices through P0 unless an explicit revision-trigger fires from the cohort exit memo. Five revision triggers defined below.

| Tier | Recommended Phase 2 lock | §6.6 anchor |
|---|---|---|
| Free | $0 | $0 |
| Trader | $79/mo · $790/yr | mid-band of $40–$150 P1 zone |
| Desk Preview | $399/mo · $3,990/yr | mid-band of $250–$500 P3 entry zone |
| Desk Full v2 | $1,199/mo · $11,990/yr | mid-band of $750–$1,500 P3 scaling zone |
| + partner read-only seat | $149/mo | ~12% of DF base |
| + analyst seat | $249/mo | ~21% of DF base |
| Founder-cohort discount | 25–30% off, 60-day window | locks through 1 renewal cycle |
| Annual prepay discount | ~17% (10/12) | not stackable with founder-cohort |

---

## 1. Why ratify

1. **§6 v1 LOCKED 2026-05-01** with the full §6.5 / §6.6 / §6.7 / §6.8 / §6.9 / §6.10 chain committed. Every downstream artifact (§9 messaging, §11 financial model, §13 KPIs, §15 investor narrative) cross-references the locked numbers. Changing Track B in Phase 2 forces re-derivation of all four.
2. **WTP bands fit cleanly** (per §6.2):
   - Trader $79 sits inside P1's $40–$150 band and inside P2's $50–$150 buy-vs-build band. Below P1's ~$200/mo cobbled-bundle (60% switching savings).
   - Desk Preview $399 sits inside P3's $250–$500 entry band; ~0.08% of $500k book — comfortable bundle-replacement drag.
   - Desk Full v2 $1,199 sits inside P3's $750–$1,500 scaling band; 0.24% of $500k book at base; with 2–3 partner seats reaches $1,500–$1,800/mo total — replaces P3's currently-paid $2,100/mo cobbled bundle with switching-friction discount.
3. **Anchor logic is conservative.** Mid-band positioning leaves room to test upward (annual price hikes after retention validation) without leaving room to test downward (downward tests train discount expectation per `_packaging/05-packaging-friction-review.md` §3 rule 3).
4. **Pricing-power asymmetry preserved.** Per §6.2 — P3 carries 5–10x P1 per-user revenue at equivalent drag-tolerance; the per-seat structure captures this without distorting P1/P2 tier pricing.
5. **Anti-overclaim audit clean.** §6.10 cleared all four tier prices. No flag-triggered changes required at v0.1.

## 2. Why not revise pre-cohort

- **Cohort exit memo is the validation instrument.** Revising before the exit memo lands is opinion-driven; revising after is data-driven. Phase 2 is the data-driven pass.
- **Pricing volatility erodes positioning.** Per BRAND voice (anti-overclaim, methodical) — visible price changes during validation read as panic or as "they're still figuring it out." Hold through P0.
- **§11 financial model unblocks faster on a stable baseline.** Pr2-1 lock at "ratify pending exit memo" allows §11 work to start with Track B inputs immediately; revision is a Phase 2-late event with explicit re-derivation.

## 3. Five revision-trigger conditions

If the P0 cohort exit memo (per `_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`) surfaces one or more of the following, reopen Pr2-1 and revise:

| # | Trigger | Implies | Recommended revision |
|---|---|---|---|
| 1 | Cohort price-objection rate ≥ 30% on Trader | $79 is above WTP for the surveyed P1/P2 cohort | Test Trader at $59 (low end of $40–$150 band); rerun unit economics |
| 2 | Cohort intent-to-pay <50% at Desk Preview $399 across qualified P3 candidates | $399 is mispositioned for the segment | Test Desk Preview at $299 or restructure as DF discounted (Alternative A in PACKAGING tier-structure rec) |
| 3 | Per-seat density forecast <1.5 from cohort interviews | P3 buyers don't add partners at expected rate | Reopen Pk-3 first (per-seat structure); pricing revision is downstream |
| 4 | Cohort founder-cohort uptake <40% in window | 25–30% discount insufficient or window too short | Widen founder-cohort window to 90 days OR deepen to 33%; do not exceed 35% (anti-pattern guard) |
| 5 | Annual prepay uptake <20% in cohort | ~17% discount insufficient incentive | Test 20% (~9.6/12) annual; rerun working-capital model |

If none trigger: ratify, lock Pr2-1, close.

## 4. Strategy posture (one-paragraph)

CoinScopeAI prices for fit, not for friction. Track B mid-band positions Trader for P1/P2 traders cobbling $200–$300/mo of disconnected tools, Desk Preview for Solo PMs entering structured tooling at the $200k–$1M book scale, and Desk Full v2 for the same Solo PMs scaling with partner accountability. Per-seat add-on captures the asymmetry of P3's variable scale without distorting P1/P2 tiers. Founder-cohort and annual discount are time-bounded, non-stackable, and anti-pressure — prices do not race to the bottom because trust does not. Pricing changes are exit-memo-driven, not opinion-driven; once locked at Phase 2, prices hold for ≥6 months per §14.

## 5. Revision discipline

If a revision is approved at Phase 2 close:

1. **Pre-mortem required** per memory `feedback_premortem_required` ("changing risk thresholds" and "engine config" trigger pre-mortem; pricing change has equivalent downstream blast radius and inherits the rule).
2. **Patch in same pass** per memory `feedback_risk_threshold_reconciliation` — every pricing reference (§6.6, §11 inputs, §13 KPI targets, §9 messaging matrix, pricing page, FAQ Q4 + Q6, Stripe products, founder-cohort comms templates).
3. **Anti-overclaim audit re-run** on the revised numbers and on every surface that mentions them.
4. **Decision-log entry** with the trigger that fired, the data that confirmed it, and the new numbers with explicit reasoning.
5. **§13 KPI re-baseline** if conversion rates or annual mix expectations change.

## 6. What this unlocks

- **Pr2-1** can be marked recommended-ratify pending P0 cohort exit memo.
- `[DOC] PRICING — Initial Pricing Philosophy` proceeds against ratified Track B.
- `[DOC] PRICING — Monthly vs Annual Offer Structure` has fixed numbers to model against.
- `[FINANCE] PRICING — Price-to-Margin Sensitivity Model` consumes Track B as the base case directly.
- §11 financial model can begin Phase 4 buildout with stable inputs.
