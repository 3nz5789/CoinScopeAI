# PRICING — Workstream Index

**Phase:** 2 — Monetization
**Status:** All five NOW deliverables drafted at v0.1. Workstream-NOW complete pending decisions Pr2-1 through Pr2-7 and REQUIRED INPUT items.
**Closed:** 2026-05-04

---

## Files

| # | File | Type | Status | Feeds decision |
|---|---|---|---|---|
| 0 | `00-readme.md` | Index | DONE | — |
| 1 | `01-pricing-strategy-recommendation.md` | RESEARCH NOW | DRAFT v0.1 | **Pr2-1** |
| 2 | `02-initial-pricing-philosophy.md` | DOC NOW | DRAFT v0.1 | (audits all PRICING decisions) |
| 3 | `03-monthly-vs-annual-offer-structure.md` | DOC NOW | DRAFT v0.1 | **Pr2-2** |
| 4 | `04-trial-and-intro-offer-options.md` | DOC NOW | DRAFT v0.1 | **Pr2-3** |
| 5 | `05-price-to-margin-sensitivity-model.md` | FINANCE NOW | DRAFT v0.1 | (feeds §11 Phase 4) |

---

## NEXT (queued, not started)

- `[RESEARCH] PRICING — Price Validation Interview Script`
- `[DOC] PRICING — Discount Policy Guardrails` → **Pr2-7**
- `[DOC] PRICING — Refund and Billing Policy Draft` → **Pr2-5**
- `[METRICS] PRICING — Conversion Benchmarks and KPI Targets`
- `[QA] PRICING — Stripe Plan Mapping Review`

## LATER (queued, not started)

- `[DOC] PRICING — Team and Institutional Pricing Concept` · Phase 5 input
- `[FINANCE] PRICING — Revenue Mix Scenario Analysis` · Phase 4 input

---

## Decisions surfaced (consolidated)

These ride into the Phase 2 decision register (`_phase-2/08-decision-register.md` when written):

| ID | Decision | Recommendation | Locks at |
|---|---|---|---|
| **Pr2-1** | Track B prices ratify or revise | **Ratify §6.6 numbers** ($79 / $399 / $1,199 + per-seat $149 / $249) | After P0 cohort exit memo; 5 revision triggers defined |
| **Pr2-2** | Annual discount magnitude | **Ratify ~17%** (10/12) | Before pricing-page lock |
| **Pr2-3** | Trial posture | **No free trial** — Free Scope B is the substitute | Before pricing-page lock |
| **Pr2-4** | Founder-cohort effective discount | **Ratify 25–30%** per §6.6 | Before P1 Narrow Ship public launch |
| **Pr2-5** | Refund SLA per tier | TBD — recommend uniform 14d per §6.7 unless cohort feedback flags DP/DF needing more | Before pricing-page lock |
| **Pr2-6** | Stripe configuration form | **Stripe Atlas UAE** (recommended per §6.8) | Before billing goes live |
| **Pr2-7** | Discount policy ceiling | **Per §6.7** — max 25%, max 30 days, no stacking | Before any non-founder-cohort discount runs |

---

## Open questions surfaced (consolidated)

These ride into Phase 2 open questions (`_phase-2/09-open-questions.md` when written):

1. **Pr2Q-1** — P0 cohort exit memo: do any of the 5 revision triggers fire? (`01-pricing-strategy-recommendation.md` §3)
2. **Pr2Q-2** — Stripe Atlas UAE actual fee schedule + volume-discount thresholds — does ~3.5% blended hold? (REQUIRED INPUT)
3. **Pr2Q-3** — Vendor-stack annual costs (CCXT 4-ex, CoinGlass, Tradefeeds, CoinGecko, Claude minimal) — needed to lock margin scenarios in §11 (REQUIRED INPUT)
4. **Pr2Q-4** — Vendor-stack step-function thresholds — at what scale do we hit each vendor's next tier? (REQUIRED INPUT)
5. **Pr2Q-5** — Free signup volume by channel per month for Scenario A/B/C inputs (depends on Phase 3 channel mix)
6. **Pr2Q-6** — Stripe Atlas configuration: does it natively support pre-renewal notification at 7-day monthly / 30-day annual cadence? (REQUIRED INPUT, also flagged in PACKAGING)
7. **Pr2Q-7** — UAE counsel review on customer-facing refund + billing policy draft (Phase 4 trigger)
8. **Pr2Q-8** — Annual mix on each tier — does it land at base case after first 6 months post-launch?
9. **Pr2Q-9** — Founder-cohort uptake in 60-day window — does it hit ≥40% of in-window signups?
10. **Pr2Q-10** — Per-seat density on DF v2 — does it average ≥1.5 per account in first year of v2?

---

## REQUIRED INPUT items (consolidated)

Pending vendor contracts, Eng confirmations, and Stripe Atlas configuration. Drafts proceed; lock waits.

| Item | Source | Affects |
|---|---|---|
| CCXT 4-exchange annual cost | Vendor contract | Sensitivity model margin |
| CoinGlass tier + annual cost | Vendor contract | Margin |
| Tradefeeds tier + annual cost | Vendor contract | Margin |
| CoinGecko tier + annual cost | Vendor contract | Margin |
| Claude API expected monthly spend | Eng usage projection | Margin |
| Vendor-stack step-function thresholds | Vendor contracts | §11 Phase 4 step-function modeling |
| Stripe Atlas UAE actual fees | Stripe direct | Margin |
| Stripe Atlas volume-discount threshold | Stripe direct | Margin at scale |
| Stripe pre-renewal notification config | Eng / Stripe | Notification spec |
| Free signup volume by channel | Phase 3 channel mix | Scenario inputs |
| UAE counsel review on refund/billing terms | Counsel (Phase 4) | Pr2-5 customer-facing form |

---

## Anti-overclaim audit roll-up

Every NOW draft was authored against the §6.10 anti-overclaim flags. Consolidated audit pass:

- **Flag 1 (founder-cohort drift to "lifetime"):** clean. Canonical phrasing "Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies" reproduced verbatim across `01`, `02`, `03`, `04`. No "lifetime / forever / always" language anywhere.
- **Flag 2 (Trader "stabilizing in cohort" must be visible):** referenced in `02-initial-pricing-philosophy.md` Principle 7 + `03-monthly-vs-annual-offer-structure.md` §6 founder-cohort communication. Pricing-page surface delegated to PACKAGING `_packaging/03-plan-comparison-table-v1.md` §1 header.
- **Flag 3 (AED display vs local-entity implication):** referenced in `02-initial-pricing-philosophy.md` Principle 7. Pricing-page surface delegated to PACKAGING `_packaging/03-plan-comparison-table-v1.md` §1 footer.

No new overclaim risks introduced by these drafts. PRICING contributes a clean baseline to the Phase 2 → Phase 3 anti-overclaim audit handoff.

---

## Cross-workstream linkages

PRICING produces inputs consumed by:

| Consumer | What | Where |
|---|---|---|
| PACKAGING | Founder-cohort policy operationalized | `_packaging/03` pricing-page surface; `_packaging/04` upgrade-prompt copy |
| PACKAGING `Beta Access Offer Design` (NEXT) | Trial posture (no free trial) constrains beta-access design space to Pk-6 options a/b/c | `_packaging/01-packaging.md` §6 Pk-6 |
| ONBOARDING (forthcoming) | Sub-$5k "we'll be back" branch consumes Free Scope B (locked) | `02-pricing.md` §3 Free posture |
| ONBOARDING (forthcoming) | Founder-cohort window comms drives signup-flow copy | `_pricing/03` §6 + `_pricing/04` §3 |
| SUPPORT (forthcoming) | Refund SLA per tier defines support response time | `02-pricing.md` §6 Pr2-5 |
| SUPPORT (forthcoming) | Dunning flow + chargeback posture defines support SOP | `02-pricing.md` §7 failure modes + §6.7 |
| GTM (forthcoming) | Pricing-page v1 spec sourced from `_packaging/03` + this workstream's posture | `_packaging/03` + `_pricing/02` Principle 7 |
| GTM (forthcoming) | Anti-pressure pricing rules constrain marketing copy | `_pricing/02` Principle 5 |
| §11 Phase 4 financial model | All sensitivity scenarios + LTV/CAC tolerance | `_pricing/05` |
| §13 KPI framework | Conversion benchmarks + falsifier conditions | `_pricing/05` §3 + `_pricing/03` §3 |

---

## Linkage to Phase 2 charter exit criteria

Phase 2 charter §4 requires (PRICING row):

> **PRICING** — Track B v1 ratified or revised with explicit reason; per-seat $149 / $249 split locked; founder-cohort policy operational (eligibility, comms, Stripe promo-code wiring); refund / dunning / chargeback SOP signed; AED display form locked. Documented in `_phase-2/02-pricing.md`.

Status against exit criteria:

- ✓ Track B ratify recommendation drafted (`01-pricing-strategy-recommendation.md`); lock pending Pr2-1 (P0 cohort exit memo).
- ✓ Per-seat $149 / $249 split addressed in PACKAGING (Pk-3) and ratified in PRICING strategy rec (consistent).
- ✓ Founder-cohort policy operational form drafted in `03` §6–§7; Stripe promo-code spec in `03` §7.
- ⏳ Refund / dunning / chargeback **SOP** belongs to NEXT `[DOC] PRICING — Refund and Billing Policy Draft` (customer-facing) + SUPPORT workstream (operational SOP). Phase 2 lock requires both.
- ✓ AED display form referenced in `02-initial-pricing-philosophy.md` Principle 7 + delegated to PACKAGING `_packaging/03` §1 footer.

PRICING workstream NOW work is **draft-complete**. Lock requires the seven **Pr2-*** decisions, the eleven REQUIRED INPUT items above, and execution of the five NEXT tasks (notably `[QA] PRICING — Stripe Plan Mapping Review` before any pricing change ships).
