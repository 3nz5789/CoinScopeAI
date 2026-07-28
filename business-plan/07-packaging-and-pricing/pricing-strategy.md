# Pricing Strategy

**Status:** Wave 2 · v1.1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** §6 v1 LOCKED (`business-plan/06-pricing-monetization.md`)
**Changelog v1 → v1.1:** §2 rewritten as forward-looking strategic framing (was a restatement of §6.6); founder-cohort band widened to ≈25–35% to reflect locked per-tier values; PA1 reprice timing clarified against the in-validation lock; §4 / §5 / §6 phrasing tightened; §9 anti-overclaim audit consolidated under `13-support-and-trust-ops/public-claims-guardrails.md`; gaps closed (per-seat density callout, founder-cohort P1 financial framing, mid-cycle upgrade behavior, competitor reprice trigger, VAT-driven billing migration distinction).

---

## 1. Pricing philosophy

CoinScopeAI prices **for trust durability first, revenue second.** Three operating beliefs:

1. **Price is a positioning act.** It signals seriousness, sets the buyer's expectation of support and reliability, and filters the cohort. A wrong price damages positioning before any feature can recover it.
2. **Price must trace to capability maturity, not aspiration.** What we charge for has to match what we can defensibly deliver today. Any forward-looking capability is priced at a *Preview* or *coming-with-v2* tier — never as the headline tier.
3. **Predictability beats optimization at this stage.** A flat, defensible monthly price the buyer can budget against beats a clever metering or volume curve that requires explanation. Disciplined buyers (P1 Omar specifically) reject pricing they cannot model.

The underlying rule: **a careful buyer reading the pricing page should not be able to find a contradiction between the price, the capability, and the trust posture.**

---

## 2. Recommended initial pricing direction

The locked v1 prices (§6.6) are calibrated. This section frames what that direction *says* about positioning, what its sensitivities are, and where the next reprice pressure is most likely to come from. Restating the numbers without that framing belongs in `plan-matrix.md`.

### 2.1 At a glance — locked v1 prices

| Tier | Standard monthly | Standard annual (paid yearly, ≈17% off) | Founder cohort\* (60-day window) |
|---|---|---|---|
| **Free** | $0 | $0 | $0 |
| **Trader** | **$79/mo** | **$790/yr** ($65/mo equiv) | $59/mo |
| **Desk Preview** | **$399/mo** | **$3,990/yr** ($332/mo equiv) | $299/mo |
| **Desk Full v2** | **$1,199/mo** | **$11,990/yr** ($999/mo equiv) | $899/mo |
| Desk Full — partner read-only seat | **$149/mo** | $1,490/yr | $99/mo |
| Desk Full — analyst seat | **$249/mo** | $2,490/yr | $179/mo |

\* Founder-cohort pricing is time-bounded per §6.7. Locks through one renewal cycle from signup; auto-converts to standard at the next renewal after the 60-day eligibility window. Discount magnitude across tiers is **≈25–35% off standard** (specific per-tier values above; see §6.6 for the locked numbers). Per §5.3.3, no grandfather discount.

### 2.2 What this direction is calibrated for

- **Trader $79** sits at the mid-band of the locked $40–$150 P1 Omar WTP zone (§6.2), and ≈60% beneath the ~$200/mo cobbled bundle the same buyer is currently paying. Mid-band placement is deliberate: top-of-band invites churn at first reprice; bottom-of-band signals casual product.
- **Desk Preview $399** is mid-band of the $250–$500 zone, ~5x Trader. The 5x multiple is the recognizable Preview-tier step that signals "different operating shape" — not "more features".
- **Desk Full v2 $1,199 + per-seat** is calibrated to *replace* P3 Layla's currently-paid ~$2,100/mo cobbled bundle with switching-friction discount. **Per-seat density is the #1 highest-impact sensitivity in §6.9** — average seat count per Desk Full v2 account is the variable most likely to drive a v2-era reprice in either direction.

### 2.3 Where the next reprice pressure most likely comes from

The lock window is **≥6 months post-validation** (§6 v1). No reprice within that window. After it, three pressure points are most likely, in priority order:

| # | Pressure point | Likely trigger | Direction of reprice |
|---|---|---|---|
| 1 | **Per-seat $149 / $249** | Per-seat density below 1.5/account at Desk Full v2 (PA6) | Restructure as % of base rather than fixed |
| 2 | **Trader $79** | Free → Trader conversion underdelivers vs. 5% base case (PA1) | Test $69 or $89 post-P2; not in-validation |
| 3 | **Annual prepay 17%** | Annual attach below 40% on Trader (PA4) | Tighten or widen — removing annual is structural and out of scope for tuning |

### 2.4 Founder-cohort financial implication during P1

PD1 recommends giving all 40 P1 cohort users founder-cohort pricing automatically. At Trader founder-cohort price ($59/mo) × 40 users = a **~$2,360/mo MRR ceiling for P1 at full Trader saturation**. This is a deliberate trust-acceleration spend, not a leak in the model. §11 financial model treats it as the cohort's known revenue envelope.

If P1 cohort mix lands closer to the target (~30 P1 / ~8 P3 / ~2 P2 per `08-go-to-market/gtm-strategy.md` §3), the effective MRR is higher because Desk Preview founder-cohort ($299/mo) carries the P3 candidates. The point is not the number; the point is the discipline of treating the discount as funded trust-building, not pricing experiment.

### 2.5 Operating posture

- **Currency:** USD-primary globally; AED conversion shown at checkout for MENA users at the AED 3.673 USD peg (display-only — no AED-denominated SKU at v1).
- **Billing:** Stripe. UAE entity; below VAT threshold (AED 375k ≈ $102k) at v1 → no VAT collection in P1; flag at ≈AED 30–35k/month revenue.
- **Term:** Monthly anchor; annual paid-yearly with ≈17% discount.
- **Cadence:** Pricing locks for **≥6 months post-validation** per §6 v1 — no surprise repricing during P1 or P2.
- **Founder cohort:** ≈25–35% off standard, time-bounded to first 60 days post-public-launch (P2). Soft-launch (P1) users get founder-cohort pricing automatically per PD1.

---

## 3. Monthly vs. annual structure

### 3.1 Both ship at every paid tier from P1 onward

| Dimension | Monthly | Annual (paid yearly) |
|---|---|---|
| Price | Sticker (e.g. $79) | Pay for 10 months, get 12 (e.g. $790 vs $948 sticker × 12) |
| Discount | None | ≈17% (pay for 10 months, get 12) |
| Refund window | 14 days from first charge | 14 days from first charge — pro-rated |
| Lock-in | 1 month, cancel anytime | 12 months, cancel-at-renewal |
| Founder-cohort stacking | Allowed (at ≈25–35% off) | **Not allowed** — annual prepay locks at standard 17% |
| Switch direction | Allowed only at renewal boundary | Allowed only at renewal boundary |

### 3.2 Why monthly is the anchor and annual is the discount

- **Monthly carries the trust message.** A monthly price is the buyer's risk surface — "I can leave at any renewal." That message matters more than ARR optimization at validation phase.
- **Annual is a commitment signal.** Buyers who choose annual are signaling they expect the product to deliver across a year; they also fund our working capital. The 17% discount is fair compensation for both.
- **Stacking annual + founder-cohort would damage clarity.** §6.7 prohibits stacking. Buyers choose one path: discounted-because-early or discounted-because-committed.
- **No mid-cycle annual switch.** Switching annual ↔ monthly only at renewal boundary keeps billing math clean and prevents prepay-then-refund abuse.

### 3.3 Mid-cycle tier-upgrade behavior on founder-cohort pricing

Per `plan-matrix.md` §9: a founder-cohort user who upgrades mid-window (e.g., Trader → Desk Preview in week 30 of their eligibility) keeps founder-cohort pricing **at the new tier**, within the original eligibility window. Pro-rated charge for the remainder of the period. Cohort lock duration does not reset on upgrade. This belongs on the pricing-page FAQ.

### 3.4 Annual mix assumptions for §11

Working hypotheses for the financial model — to validate at P1 cohort review:

| Tier | Base case (annual / monthly mix) | Why |
|---|---|---|
| Trader | 40% / 60% | P1 Omar is monthly-default; annual converts after 1–2 renewals of trust |
| Desk Preview | 60% / 40% | P3 Layla is budget-forward; annual lines up with her budgeting cycle |
| Desk Full v2 | 75% / 25% | Partner-money obligations + audit cadence drive annual default |

These are **ASSUMPTION** values per §6.9. Actuals may differ; the cohort tracker measures attach rate by tier from M1.

---

## 4. Trust and readiness considerations that affect pricing

Pricing is **constrained** by what the product can defensibly stand behind today. Five trust constraints, each with a pricing consequence:

| Trust constraint | Pricing consequence |
|---|---|
| **Validation-phase, testnet-only, no real capital deployed** | Headline tier (Trader $79) must be priced beneath the buyer's cobbled-bundle alternative (~$200/mo) so the trial is a clear win even at this stage |
| **Anti-overclaim posture (§6.10)** | No "Pro" / "Premium" / "Enterprise" tier names, no "100x your account" / "guaranteed ROI" / "beat the market" copy, no aspirational ROI math on the pricing page |
| **Founder-led, solo-founder bus factor** | SLAs at Trader cannot be priced as if a 24/7 team supports them; price is calibrated to "best-effort + transparent ops" not "named-CSM" |
| **PCC v2 §8 Capital Cap (real capital is gated)** | No tier price implies live-trading authorization; "Desk Full v2" deliberately deferred to P5 because the v2 capability set requires §8-pass evidence |
| **Founder cohort exists for trust acceleration, not pricing innovation** | Founder-cohort discount is bounded (≈25–35%, 60 days, one renewal cycle) — it must not become a quasi-permanent price floor |

The implication: **pricing is the surface where trust posture becomes a number.** When trust has not yet been earned, the number is conservative; when trust accumulates (post-validation, post-§8), the number can be revisited — but not before, and not faster than ≥6 months per §6 v1.

---

## 5. What pricing should signal to the market

The pricing page is read by P1 Omar, P3 Layla, and a much smaller number of P2 Karims. It should signal three things — explicitly:

1. **"This product is for serious operators."**
   Trader at $79/mo signals that we expect a buyer who is already paying ≈$200/mo for a cobbled bundle. We are not chasing the $0–$30 charting-baseline market (TradingView Pro band per §6.1); that audience is anti-ICP.

2. **"This product respects your discipline; it doesn't replace it."**
   The pricing page describes capabilities in terms of *enforcement* of the user's framework (configurable gates, R-multiple journal, regime-and-confidence on every signal) — not in terms of *outperformance* (no win-rate claims, no leaderboards, no ROI ranges).

3. **"This product is at validation phase, and our pricing matches that posture."**
   Tier names ("Preview", "v2") and disclaimers ("validation phase", "testnet only") are visible on the pricing surface itself — not buried in an FAQ. The price acts as a credibility anchor: it's high enough to take seriously, low enough to match validation-stage maturity.

A buyer who reads the pricing page and walks away thinking *"these people understand what they are and aren't"* has received the intended signal.

---

## 6. What pricing mistakes to avoid

Ten failure modes, ranked by historical frequency at trust-sensitive trading products. Each is a lock for `13-support-and-trust-ops/public-claims-guardrails.md` review.

| # | Mistake | Why it kills CoinScopeAI specifically | Guard |
|---|---|---|---|
| **M1** | **Underpricing Trader below the $40 floor of the locked $40–$150 WTP band** | Damages perceived seriousness; attracts sub-$5k churners; signals "casual product" | Trader at $79 — locked in §6.6 mid-band |
| **M2** | **Pricing Desk Preview as if v2 capabilities ship now** | Buyer pays $399 expecting audit-grade reporting; gets static PDF; trust collapse | Preview labeling on every surface; static-PDF capability stated explicitly |
| **M3** | **"Founder discount forever" framing** | Becomes contractually time-bounded but psychologically permanent → next renewal feels like a price hike | Locked language: "founding-member pricing — through your first renewal cycle, then standard pricing applies" |
| **M4** | **Stackable discounts (annual + founder + promo)** | Erodes price credibility; race-to-the-bottom; ARPU distortion | §6.7 — stacking explicitly disallowed |
| **M5** | **Performance-tied add-ons** ("upgrade to win-rate boost") | Anti-positioning; gambling-adjacency; alpha-seeking signal | Never. No SKU is performance-conditioned at any tier |
| **M6** | **Surprise mid-cycle reprice** | "We're raising prices on Tuesday" → trust damage out of proportion to revenue gain | Pricing locks ≥6 months post-validation per §6 v1; any reprice is announced ≥30 days ahead |
| **M7** | **Hidden fees or per-trade variability** | "But the page said $79" → support escalations + churn | Single sticker; no usage overage at any tier; per-seat clearly disclosed at Desk Full v2 |
| **M8** | **Pricing page that hides validation status** | Contradicts every other trust surface; cohort buyers notice immediately | Validation-phase disclaimer **on the pricing page itself**, not just the footer |
| **M9** | **General-promo discounting Desk Preview to "land" P3 Layla** | Signals desperation; damages the Desk Full v2 anchor | Promotional pricing capped at 25% off, time-bounded to 30 days, never on Desk Full v2. (Carve-out: explicit partnership-driven discount per §6.7 is allowed under counsel/brand-voice review.) |
| **M10** | **Re-introducing a "Pro" or "Premium" tier name** | Implies a maturity claim PCC v2 has not certified | §5.3.3 — locked tier names; any new tier name passes brand-voice review before publication |

---

## 7. Assumptions that must be validated before locking prices longer-term

Pricing is locked for **≥6 months post-validation**. Within the lock window (P0 → P2 close + ≥6 months), no reprice fires regardless of the assumptions below. Beyond that, the following assumptions need cohort evidence before re-locking. Cross-reference §6.9 sensitivity ranking and `business-model-summary.md` §8 BMA1–BMA10.

| # | Assumption | Validation source | Window | Outcome if false |
|---|---|---|---|---|
| **PA1** | $79 Trader sits inside P1 Omar's WTP and beneath his cobbled-bundle | P1 cohort retention M1–M3; churn-reason capture; price-objection rate at signup | M3 evidence captured during P1; **informs the post-P2 reprice review** (no in-validation reprice) | Test $69 or $89 in the post-P2 window; do not move prices in P0–P2 |
| **PA2** | $399 Desk Preview sits inside P3 Layla's bundle-replacement band | P1 + P2 Desk Preview signup volume; signup-source attribution | P1–P2 evidence captured; reprice consideration post-lock | Reposition Preview as "Desk: bundle replacement" or test $349 |
| **PA3** | $1,199 Desk Full v2 + per-seat is the right anchor for solo PMs | P5 launch cohort + intent letters in P3–P4 window | P5 (Mar–May 2027) | Restructure pricing pre-P5 launch; consider $999 anchor with higher per-seat |
| **PA4** | 17% annual discount is enough to drive >40% annual mix on Trader | P1 cohort prepay attach rate by M3 | P1 evidence captured; reprice consideration post-lock | Tighten or widen the discount magnitude; **removing annual is a structural change requiring its own decision-log entry**, not a tuning option |
| **PA5** | ≈25–35% founder-cohort discount drives meaningful early-supporter conversion vs. standard | P2 public-launch cohort signup pace at standard vs. founder pricing | P2 (Aug–Sep 2026) | Tighten to 15–20% if attach rate dilutes margin without lifting volume |
| **PA6** | Per-seat $149 / $249 captures partner-count value at Desk Full v2 | P5+ per-seat density observation | P5 onwards | Restructure per-seat as % of base rather than fixed |
| **PA7** | AED display-only (no AED-denominated SKU) is sufficient for MENA conversion | MENA conversion rate vs. global EN at P1–P2 | P2 | Build AED-denominated SKU with bank-transfer support |
| **PA8** | Pricing locks ≥6 months without competitor pressure | Comp-set monitoring (CoinGlass, Nansen, CryptoQuant). **Trigger for interim re-evaluation:** a comp-set product launches with material capability overlap (regime classification + risk gating) at >30% lower price, OR CoinGlass extends Pro tier into our space (per §12 R-007) | Continuous; flag at vendor expansion (P2) and pre-P5 | Counsel + brand-voice + decision-log entry before any reactive reprice |
| **PA9-a** | Stripe per-seat billing supports the Desk Full v2 model without manual ops | Implementation review pre-P5 | P3–P4 | If Stripe-specific limits are hit at P5 scale, evaluate Chargebee or similar |
| **PA9-b** | Stripe ToS coverage adequate post-VAT-threshold; merchant-of-record migration not required | Compliance review at AED 30–35k/mo trigger | At threshold approach | Evaluate Paddle merchant-of-record if VAT compliance burden becomes meaningful |

Validation cadence: **review at P1 close (Jul 2026), P2 close (Sep 2026), P5 launch (Mar–May 2027).** No interim repricing inside the lock window.

---

## 8. Pricing decision points for leadership

Decisions that **must** be made by an explicit owner before a calendar-driven event. Each links into the broader decision log.

| # | Decision | Why it matters | Recommendation | Owner | Deadline |
|---|---|---|---|---|---|
| **PD1** | Lock the founder-cohort eligibility window — soft-launch (P1) inclusive, or only public-launch (P2) | Affects which signups get founder pricing; affects §11 ARPU during P1; CA-11 counsel-review-pending applies to the framing language | Soft-launch users get founder-cohort pricing automatically (P1); the 60-day P2 eligibility window is for the public launch | Founder + counsel | Before 2026-06-01 (P1 cohort open) |
| **PD2** | Confirm 14-day refund window (vs. 30-day or none) | Affects effective ARPU and refund-abuse exposure; CA-10 counsel-review-pending | 14-day, single-use per account; no stacking — per §6.7 | Founder + counsel | Before 2026-06-01 (P1 cohort open) |
| **PD3** | Confirm annual prepay rate at 17% (vs. 15% or 20%) | Affects annual attach rate and ARPU | 17% (pay for 10 months, get 12) — locked §6.6 | Founder | Locked |
| **PD4** | Confirm no AED-denominated SKU at v1 | Operational simplicity vs. MENA conversion friction | USD-only billing; AED conversion display at peg — locked §6.8 | Founder | Locked |
| **PD5** | Lock the Desk Full v2 per-seat structure pre-launch | Affects §11 sensitivity #1 (per-seat density) | $149 partner / $249 analyst — locked §6.6, validate at P5 | Founder | Locked, revisit P5 |
| **PD6** | Decide if a Desk Preview → Desk Full v2 migration credit applies at P5 | Bundle-replacement buyers may resist re-anchoring | Apply 1-month credit at v2 migration; do not extend founder-cohort discount | Founder | P3–P4 (Sep 2026 – Feb 2027) |
| **PD7** | Decide promotional pricing cadence at P2 public launch | Avoid race-to-the-bottom; avoid leaving conversion on the table | One time-bounded promo (≤25% off, ≤30 days) coinciding with P2 launch announcement; none thereafter without explicit founder approval | Founder + GTM owner | Pre-P2 (Aug 2026) |
| **PD8** | Decide pricing-page disclosure of "validation phase" — visible vs. footer | Trust posture vs. conversion friction | **Visible.** Disclosure on the pricing page itself, not buried | Founder | Before 2026-06-01 (P1 cohort open) |

---

## 9. Anti-overclaim audit on pricing surfaces

The canonical anti-overclaim audit lives in **`13-support-and-trust-ops/public-claims-guardrails.md`** (with §6.10 and §9 as the upstream sources). Pricing-surface-specific applications:

- **Founder-cohort framing.** Per §6.10 Flag 1: never "lifetime", "forever", "always", or "founder discount locked-in". Always "founding-member pricing — locked through your first renewal cycle, then standard pricing applies."
- **Trader "stabilizing" status.** Per §6.10 Flag 2: pricing page must surface validation-phase status alongside the price: *"Trader — $79/mo. Includes engine API + dashboard (stabilizing in cohort during validation phase)."*
- **AED display.** Per §6.10 Flag 3: AED conversion shown as *"Approximate AED equivalent — billed in USD. UAE sole prop (Mohammed). Other GCC users responsible for any local tax obligations."*
- **No performance language anywhere on the pricing surface.** No "win rate", no "ROI", no "average user makes X". Pricing is a credibility surface, not a conversion-optimization surface.

A pricing page that fails any of the canonical guardrails (per `public-claims-guardrails.md` § allowed/forbidden) is rejected at brand-voice review and not shipped.

---

## 10. Cross-references

- §6 v1 LOCKED canonical: `business-plan/06-pricing-monetization.md`
- Phase 2 pricing notes: `business-plan/_phase-2/_pricing/`
- Plan matrix: `07-packaging-and-pricing/plan-matrix.md`
- Trial / discount: `07-packaging-and-pricing/trial-and-discount-policy.md`
- Anti-overclaim canonical: `13-support-and-trust-ops/public-claims-guardrails.md`
- Brand messaging: `business-plan/09-brand-messaging.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
