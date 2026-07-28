# PRICING — Price-to-Margin Sensitivity Model

**Task:** `[FINANCE] PRICING — Price-to-Margin Sensitivity Model`
**Type:** NOW
**Owner:** FinOps + Founder
**Status:** DRAFT v0.1 — lightweight sensitivity model; spreadsheet build deferred to Phase 4 §11
**Anchored to:** §6.6 Track B prices; §6.9 LTV/CAC sensitivity inputs (sensitivity ranks #1–#6); PRICING `03-monthly-vs-annual-offer-structure.md` mix-sensitivity tables; project memory `project_phased_rollout` (P1 narrow ship vendor stack: CCXT 4-ex, CoinGlass, Tradefeeds, CoinGecko, Claude minimal).

---

## 1. Purpose and scope

Phase 2 lightweight sensitivity model. Surfaces the highest-leverage pricing inputs and their revenue / margin impact across a 24-month horizon. **Not a financial model** — that's §11 Phase 4 work. This is the input framework §11 consumes.

In scope: revenue sensitivity to cohort mix, per-seat density, annual mix, founder-cohort drag. Gross-margin sensitivity to vendor stack, Stripe processing, VAT step-function.

Out of scope: working-capital model (Phase 4), CAC modeling (Phase 3 channel mix locks first), salaries / opex (Phase 4), fundraising scenarios (Phase 4).

---

## 2. Inputs (consolidated from §6.6 + §6.9)

### Tier prices

| Tier | Monthly | Annual | Founder-cohort monthly | LTV (per §6.9 base) |
|---|---|---|---|---|
| Trader | $79 | $790 | $59 | $1,580 (~2y tenure) |
| Desk Preview | $399 | $3,990 | $299 | $10,000 (~2.5y tenure) |
| Desk Full v2 | $1,199 | $11,990 | $899 | $52,000 (~3y, incl. seats) |
| Partner read-only | $149 | $1,490 | $99 | (per-seat addition) |
| Analyst seat | $249 | $2,490 | $179 | (per-seat addition) |

### Conversion assumptions (per §6.9)

| Conversion | Base | Upside | Downside |
|---|---|---|---|
| Free → Trader (over 90 days) | 5% | 10% | 2% |
| Trader → Desk Preview (over 12 months) | 8% | 15% | 4% |
| Desk Preview → Desk Full v2 (at v2 launch) | 70% | 90% | 50% |

### Annual mix (per §6.9 + `_pricing/03`)

| Tier | Base | Upside | Downside |
|---|---|---|---|
| Trader | 40% | 55% | 25% |
| Desk Preview | 60% | 75% | 45% |
| Desk Full v2 | 75% | 90% | 60% |

### Per-seat density (per §6.9 base)

| Scenario | Avg seats per DF account |
|---|---|
| Base | 2.5 (1 PM + 1.5 partner read-only) |
| Upside | 4 (1 PM + 3 partner read-only) |
| Downside | 1 (PM only, no partners) |

### Founder-cohort drag

- Discount magnitude: ~25–30% off standard for first renewal cycle
- Eligibility window: 60 days post-public-launch
- Estimated effective drag on first-2-month revenue: **20–30%** of would-be standard ARPU during the window
- After 60-day window: zero drag

### Cohort retention (per §6.9, ASSUMPTION pending validation)

| Tier | 12-month retention |
|---|---|
| Trader | 60% |
| Desk Preview → Desk Full transition | 70% |
| Desk Full v2 (post-launch) | 80% |

---

## 3. §6.9 sensitivity ranking (consolidated)

Per §6.9, ranked by impact on base-case unit economics:

| Rank | Sensitivity | Magnitude per delta | Action implication |
|---|---|---|---|
| 1 | Per-seat density at Desk Full v2 | Each +1 seat = +$1,800/yr revenue per DF account; base 2.5 → upside 4 = +$2,700/yr per account | Pk-3 + DF UX must drive seat additions; per-seat density is tracked separately in §13 |
| 2 | Free → Trader conversion | Base 5% → downside 2% = 2.5x cohort size delta | Pk-2 (Free vs Paid boundary) is the lever; PrQ-1 is the falsifier |
| 3 | Annual mix | ~5% ARR draw per tier; large working-capital benefit | Pr2-2 sets the policy; §13 tracks actual mix |
| 4 | Desk Preview → Desk Full v2 migration rate | Critical for §15 fundraising narrative; investors model directly | Phase 5 launch comms + DF-specific incentives |
| 5 | Trader → Desk Preview conversion | Lower volume, higher per-event revenue | Karim P2 API trigger (per §6.2) is the structural conversion driver |
| 6 | Founder-cohort effective ARPU | Material only in 60-day window; small effect on 24-month total | Pr2-4 sets the magnitude; rank 6 confirms not over-investing |

---

## 4. Revenue scenarios — 24-month horizon

Toy scenarios. Single cohort assumption. Ignores churn beyond the 12-month retention assumption above. Purpose: visualize ARR magnitude across realistic Phase 2-locked variable ranges.

### Scenario A — Conservative (downside on every input)

| Variable | Value |
|---|---|
| Free signups in 24 months | 5,000 (REQUIRED INPUT — Phase 3 channel mix unlocks this) |
| Free → Trader 90-day conv | 2% |
| Trader cohort | 100 |
| Trader → Desk Preview 12-mo conv | 4% |
| Desk Preview cohort | 4 |
| Desk Full v2 migration at v2 launch | 50% |
| Desk Full v2 cohort | 2 |
| Per-seat density | 1.0 (PM only) |
| Annual mix | 25% / 45% / 60% |
| Trader 12-mo retention | 60% |

**24-month revenue (rough, ignoring intra-period churn smoothing):**

- Trader: 100 × ~$948 weighted by mix = ~$90,850 ARR × 60% retention through year 2 = ~$145k 24-mo cumulative
- Desk Preview: 4 × ~$4,433 weighted = ~$17,700 ARR × ~70% transition retention = ~$28k 24-mo cumulative
- Desk Full v2: 2 × ~$13,193 weighted = ~$26,400 ARR (only year 2; v2 launches Mar–May 2027) × no per-seat = ~$26k

**Cumulative 24-mo revenue (Scenario A):** ~$199k

### Scenario B — Base case (every input at base)

| Variable | Value |
|---|---|
| Free signups in 24 months | 10,000 (REQUIRED INPUT) |
| Free → Trader 90-day conv | 5% |
| Trader cohort | 500 |
| Trader → Desk Preview 12-mo conv | 8% |
| Desk Preview cohort | 40 |
| Desk Full v2 migration at v2 launch | 70% |
| Desk Full v2 cohort | 28 |
| Per-seat density | 2.5 |
| Annual mix | 40% / 60% / 75% |
| Trader 12-mo retention | 60% |

**24-month revenue (rough):**

- Trader: 500 × ~$948 weighted by 40% annual = ~$442,400 ARR × 60% = ~$708k 24-mo cumulative
- Desk Preview: 40 × ~$4,310 weighted = ~$172,400 ARR × ~70% transition = ~$276k 24-mo cumulative
- Desk Full v2: 28 × ~$12,590 weighted by 75% annual = ~$352,500 ARR base + 28 × 1.5 partner seats × ~$1,664 (annual-weighted) = +$70,000 = ~$422,500 ARR (year 2 only)

**Cumulative 24-mo revenue (Scenario B):** ~$1.41M

### Scenario C — Aggressive (upside on every input)

| Variable | Value |
|---|---|
| Free signups in 24 months | 25,000 (REQUIRED INPUT) |
| Free → Trader 90-day conv | 10% |
| Trader cohort | 2,500 |
| Trader → Desk Preview 12-mo conv | 15% |
| Desk Preview cohort | 375 |
| Desk Full v2 migration at v2 launch | 90% |
| Desk Full v2 cohort | 338 |
| Per-seat density | 4 |
| Annual mix | 55% / 75% / 90% |
| Trader 12-mo retention | 60% |

**24-month revenue (rough):**

- Trader: 2,500 × ~$861 weighted by 55% annual = ~$2,153k ARR × 60% = ~$3.45M 24-mo cumulative
- Desk Preview: 375 × ~$4,189 weighted = ~$1,571k ARR × ~70% transition = ~$2.51M 24-mo cumulative
- Desk Full v2: 338 × ~$12,229 weighted by 90% annual = ~$4,134k ARR base + 338 × 3 partner seats × ~$1,564 (annual-weighted) = +$1,586k = ~$5,720k ARR (year 2 only)

**Cumulative 24-mo revenue (Scenario C):** ~$11.7M

### Scenario read

| Scenario | Cumulative 24-mo revenue | Multiplier vs base |
|---|---|---|
| Conservative | ~$199k | 0.14x |
| Base | ~$1.41M | 1.0x |
| Aggressive | ~$11.7M | 8.3x |

The 60x range from conservative to aggressive is dominated by:
1. Free signups (assumed input — Phase 3 channel mix-driven)
2. Per-seat density on DF v2 (Sensitivity Rank #1)
3. Trader → DP conversion rate (compounds through funnel)

These are also the three highest-volatility inputs. Phase 4 §11 should model with explicit confidence intervals on each, not point estimates.

---

## 5. Gross margin draws

Per-revenue-dollar costs that must come out of ARR before margin contribution:

| Cost line | Per-dollar draw | Source / scaling | Phase / Step-function trigger |
|---|---|---|---|
| Stripe processing | ~3.5% blended (per §6.9) | Cards ~2.9% + $0.30; ACH lower; AED FX ~1% | Per transaction; non-step |
| Vendor stack: CCXT 4-exchange | Fixed cost (REQUIRED INPUT) | per memory `project_phased_rollout` P1 vendor stack | Step at venue addition (Bybit P2) |
| Vendor stack: CoinGlass | Fixed cost (REQUIRED INPUT) | P1 stack | Step at tier upgrade |
| Vendor stack: Tradefeeds | Fixed cost (REQUIRED INPUT) | P1 stack | Step at tier upgrade |
| Vendor stack: CoinGecko | Fixed cost (REQUIRED INPUT) | P1 stack | Step at tier upgrade |
| Claude API | Variable (REQUIRED INPUT — usage-based) | "Minimal" stack at P1 per memory | Variable per inference |
| VAT collection (post-threshold) | 5% of UAE revenue | At AED 375k (~$102k) annual revenue | Step-function at threshold |
| Per-seat invoicing complexity | Light at v1 | Stripe handles natively | None at v1; possibly light support cost |
| Hosting / infra | (REQUIRED INPUT — out of PRICING scope) | Eng / DevOps owns | None |

### Vendor-stack cost shape (qualitative)

The P1 vendor stack is **mostly fixed** at low volume. Per-customer marginal cost is near-zero until per-vendor tier limits trigger:

- Below vendor tier limits → fixed cost regardless of customer count
- At vendor tier limit → step-function cost increase to next vendor tier
- Each step likely sized at 1–10x the previous tier (typical SaaS vendor pricing INFERENCE)

**Implication:** gross margin per customer *improves* as cohort grows (fixed vendor cost amortizes); but step-function cost increases at vendor-tier thresholds produce margin cliffs. Phase 4 §11 must model both.

### Estimated gross margin range

Without locked vendor cost numbers (REQUIRED INPUT), rough qualitative estimate:

| Scenario | Estimated gross margin | Reasoning |
|---|---|---|
| Conservative cohort (~$199k revenue) | Likely sub-30% margin | Vendor stack cost dominates at low volume |
| Base case (~$1.4M revenue) | Likely 50–65% margin | Vendor stack cost amortizes; Stripe + VAT visible drags |
| Aggressive (~$11.7M revenue) | Likely 70–80% margin (pre-step-functions) | Vendor cost largely amortized; possible vendor-tier step-up |

**These are placeholder ranges. §11 Phase 4 must replace with actual vendor pricing pulled from current contracts (REQUIRED INPUT).**

---

## 6. Founder-cohort drag estimate

Founder-cohort applies to monthly billing within 60-day window, ~25–30% off. Annual is at standard discount, not stackable.

**Drag estimate:** during the 60-day window, monthly billers signing up under founder-cohort generate ~70–75% of standard ARPU. Annual billers generate standard ARPU (no stacking).

Estimated monthly mix during window: ~50% monthly (per Pr2-3 no-trial, monthly is the experimentation cadence) → effective ARPU during window ≈ 0.5 × 0.725 + 0.5 × 1.0 = **~86% of standard ARPU during window**.

**Total revenue drag over 24 months:** assuming public launch month + 60-day window ≈ first-2-months effect → ~14% effective ARPU drag for ~2 months = ~2.3% drag over 24 months. Material in cohort comms + first-2-months cash flow; immaterial in 24-month aggregate.

§6.9 Sensitivity Rank #6 confirms this is correctly low priority.

---

## 7. LTV/CAC tolerance (per §6.9)

| Tier | LTV (per §6.9) | LTV/CAC ≥ 3 floor → CAC ceiling | Realistic CAC range (per §6.9) |
|---|---|---|---|
| Trader | $1,580 | ~$525 | $80–$300 (organic + light paid) |
| Desk Preview | $10,000 | ~$3,300 | $300–$1,500 (relationship-driven) |
| Desk Full v2 | $52,000 (incl. seats avg 3) | ~$17,000 | $2,000–$8,000 |

Phase 3 channel-mix selection consumes these as the per-channel acceptance criteria. Channels with realized CAC above tier-specific CAC ceiling are out by construction.

---

## 8. Step-function operational costs to flag for §11

Per §6.9:

1. **VAT registration at AED 375k (~$102k) annual revenue.** Adds tax-collection and remittance overhead. UAE 5%. Other-GCC VAT below materiality threshold at v1.
2. **Stripe processing at scale.** ~2.9% + $0.30 cards; ACH lower; AED FX ~1%. Blended ~3.5%. Negotiable above ~$1M/yr volume (REQUIRED INPUT — confirm Stripe Atlas tiering).
3. **Per-seat invoicing.** Light at v1 (Stripe native). Support volume scales with seat count; estimate 1–2 support tickets per 10 seat changes.
4. **Vendor-stack tier upgrades.** Per §2 vendor-stack cost shape — step-function at unknown thresholds (REQUIRED INPUT).

---

## 9. Sensitivity model decision register

Outputs feeding §11 and §13:

| Output | Consumed by | Phase |
|---|---|---|
| Three-scenario revenue projection (A/B/C) | §11 financial model; §15 investor narrative | Phase 4 |
| §6.9 sensitivity ranks confirmed | §11 + §13 KPI prioritization | Phase 2 → Phase 4 |
| Vendor-stack cost shape (fixed-then-step) | §11 cost model | Phase 4 |
| LTV/CAC tolerance per tier | Phase 3 channel-mix selection | Phase 3 |
| Founder-cohort drag estimate (~2.3% 24-mo) | §11 + Pr2-4 evaluation | Phase 2 |
| VAT step-function trigger at ~AED 375k | §11 + §10 ops | Phase 4 |

---

## 10. REQUIRED INPUT items (consolidated)

| Input | Source | Affects |
|---|---|---|
| CCXT 4-exchange annual cost | Eng / vendor contract | Margin per scenario |
| CoinGlass tier and annual cost | Vendor contract | Margin |
| Tradefeeds tier and annual cost | Vendor contract | Margin |
| CoinGecko tier and annual cost | Vendor contract | Margin |
| Claude API expected monthly spend | Eng usage projection | Margin |
| Vendor-stack step-function thresholds (when do we hit next tier per vendor?) | Vendor contracts | Step-function modeling |
| Stripe Atlas UAE tier rates and volume-discount thresholds | Stripe direct | Margin at scale |
| Free signup volume per channel per month (for Scenario inputs) | Phase 3 channel mix | Conversion volume |

These must be filled before §11 Phase 4 build can produce defensible numbers. Phase 2 sensitivity model proceeds with placeholder ranges; §11 replaces with locked numbers.

---

## 11. What this unlocks

- §11 Phase 4 financial model has the input framework + scenario structure ready.
- Phase 3 channel-mix selection has CAC tolerance per tier (§7).
- §13 KPI framework has §6.9 sensitivity ranks to prioritize KPI investment.
- Pr2-4 founder-cohort decision has the drag estimate (~2.3% 24-mo) for cost-of-cohort calculation.
- §15 fundraising narrative has three-scenario revenue projection structure.
- `[FINANCE] PRICING — Revenue Mix Scenario Analysis` (LATER) inherits this as starting point.
