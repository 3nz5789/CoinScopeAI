# Financial Assumptions

This document is the **assumption contract** for any current or future financial work on CoinScopeAI. Every number that appears in a model, deck, or fundraising narrative must trace back to a row in the table below — or the model is wrong.

---

> ## Validation Gate Rule (load-bearing)
>
> **Any assumption that has not been observed in a real cohort for ≥60 days is downgraded to "directional only" in any model that uses it.**
>
> This rule applies to every row below. A row's `Status` field reflects whether this gate has been cleared. An assumption can be load-bearing in a *plan* and "directional only" in a *model* simultaneously — the discipline is to mark which is which.

---

## Column legend

- **#** — stable identifier; never reused.
- **Area** — workstream tag.
- **Assumption** — the claim itself, sharply phrased.
- **Risk grade**: **H** (high — load-bearing, validate first), **M** (medium), **L** (low).
- **Type**: `ASSUMPTION` (best estimate to validate), `REQUIRED INPUT` (we must collect data), `DECISION NEEDED` (leadership choice).
- **Status**: `Not validated` (no real data yet), `Validating` (data being collected), `Validated` (≥60 days real cohort confirms within band), `Invalidated` (data falsifies; row needs revision).

The two tables below share row numbers. Table A is the scannable assumption list; Table B holds the cross-references, decision IDs, deadlines, and downstream propagation paths.

---

## 1. Master assumption table — Table A (claim + grade + status)

| # | Area | Assumption | Risk | Type | Status |
|---|---|---|---|---|---|
| 1 | Pricing — Trader | $79/mo monthly is the activation tier | H | ASSUMPTION | Not validated |
| 2 | Pricing — Desk Preview | $399/mo bridges Trader and Desk Full v2 | M | ASSUMPTION | Not validated |
| 3 | Pricing — Desk Full v2 | $1,199/mo + per-seat $149 OR $249 | M | DECISION NEEDED | Not validated |
| 4 | Annual prepay | Not offered before PCC v2 G4 + 60 days stable | **H** | DECISION NEEDED | Not validated |
| 5 | Free tier role | Trust-builder, not funnel filler — no upsell hard-press | M | ASSUMPTION | Not validated |
| 6 | Free → Trader conversion (mature) | 3–7% on activated free users at maturity¹ | H | ASSUMPTION | Not validated |
| 7 | Trader → Desk Preview conversion | 5–12% at maturity, only after P2 | M | ASSUMPTION | Not validated |
| 8 | Desk Preview → Desk Full v2 conversion | 10–25% material only after P5 launch | L | ASSUMPTION | Not validated |
| 9 | Trader monthly churn at maturity | 5–10% range | H | ASSUMPTION | Not validated |
| 10 | Trader monthly churn at early cohort | Up to 10–20% before activation flow stabilizes | H | ASSUMPTION | Not validated |
| 11 | Refund rate target | <2% of MRR/month, never >5% in any single month | **H** | ASSUMPTION | Not validated |
| 12 | Support load — Trader | ≤30 min/user/month at maturity, including incident overhead | H | ASSUMPTION | Not validated |
| 13 | Support load — Desk Preview | ≤90 min/user/month | M | ASSUMPTION | Not validated |
| 14 | Support load — Desk Full v2 | Materially higher; per-seat support time costed at SKU activation | M | ASSUMPTION | Not validated |
| 15 | Vendor cost — exchanges | Binance USDT-M only at P1; Bybit added at P2 | M | ASSUMPTION | Validating |
| 16 | Vendor cost — derivatives data | CoinGlass single-source through P2 | H | ASSUMPTION | Validating |
| 17 | Vendor cost — AI/LLM | Claude as primary, OpenAI as fallback; per-user cost capped via cache + throttle | H | ASSUMPTION | Not validated |
| 18 | Stripe blended take-rate | 3.0–3.9% MENA; 2.9–3.4% global EN | M | REQUIRED INPUT | Not validated |
| 19 | Founder internal rate | $100/hr placeholder for internal cost recognition | M | DECISION NEEDED | Not validated |
| 20 | Hiring pace — first hire | No hire before P2 (Aug–Sep 2026) at earliest | H | ASSUMPTION | Validating |
| 21 | Hiring pace — support | Part-time contractor at first; full-time only post-P3 | M | ASSUMPTION | Not validated |
| 22 | Hiring pace — engineering | Single contractor for selective workstreams (vendor integrations) before headcount | M | ASSUMPTION | Not validated |
| 23 | Product readiness — P1 narrow ship | Requires PCC v2 G3 stable for ≥30 days | H | ASSUMPTION | Validating |
| 24 | Product readiness — P2 vendor expansion | Requires P1 monetization validated for ≥60 days | H | ASSUMPTION | Not validated |
| 25 | Product readiness — P5 Desk Full v2 | Requires per-seat audit, role-based access, compliance posture upgrade | H | ASSUMPTION | Not validated |
| 26 | Real-capital trading | Not authorized at any phase until §8 Capital Cap criteria met | H | ASSUMPTION (firm) | Validated (firm posture) |
| 27 | Geographic mix | UAE/MENA primary + global EN; US blocked at signup | M | ASSUMPTION | Validated (firm posture) |
| 28 | Trial model | Free tier serves as trial; no time-boxed paid trial pre-P2 | M | DECISION NEEDED | Not validated |
| 29 | Cohort size — P0 validation | Capped at 40 users by design | L | ASSUMPTION (firm) | Validated (firm by design) |
| 30 | Discount policy | No standing discounts before P2 | M | DECISION NEEDED | Not validated |
| 31 | Cash runway floor | ≥9 months at all times; escalate exec discussion below threshold | M | ASSUMPTION | Not validated |
| 32 | Validation cohort completion | ≥70% of P0 cohort completes 30-day window with no incident-driven termination | H | ASSUMPTION | Validating |
| 33 | Activation rate (D7) | ≥40% of weekly signups complete activation definition within 7 days² | H | ASSUMPTION | Not validated |
| 34 | Day-7 retention | ≥60% of activated users still active on D7² | H | ASSUMPTION | Not validated |
| 35 | Day-30 retention | ≥40% of D7-retained users still active on D30² | H | ASSUMPTION | Not validated |
| 36 | Vendor cost / revenue ceiling | Total vendor cost ≤25% of MRR at maturity; alarms fire above | H | ASSUMPTION | Not validated |
| 37 | Single-vendor concentration | No single vendor >40% of total vendor cost | M | ASSUMPTION | Not validated |

**Footnotes:**

¹ Row 6 depends on `21-decision-log` row **D-01** (activation definition lock, currently `OPEN — High`). Until D-01 is `DECIDED`, Row 6 is **directional only** regardless of the band shown.

² Rows 33, 34, 35 inherit Row 6's D-01 dependency. The activation definition gates what these metrics measure.

---

## 2. Master assumption table — Table B (cross-refs + triggers + propagation)

| # | Source | Decision-log ID | Deadline / Re-review trigger | Downstream models affected |
|---|---|---|---|---|
| 1 | `07-packaging-and-pricing` | A-03 | Re-review post P1 + 60 days revenue | revenue-model; scenario-model-inputs (best/worst) |
| 2 | `07-packaging-and-pricing` | A-03 | Re-review at P2 entry | revenue-model; tier-mix |
| 3 | `07-packaging-and-pricing` | A-03; B-02 | Lock by 2026-12-31 (pre-P5) | Desk Full v2 economics; M8 milestone |
| 4 | `15-financial-framework/revenue-model.md` §4 | B-01 | Decide by 2026-07-31 (pre-P2) | Stripe config; refund exposure; cash-flow shape |
| 5 | `04-icp-and-segmentation`; A-01 | A-01 (input) | Re-review at P2 | revenue-model; conversion bands |
| 6 | `12-onboarding-and-activation`; `kpi-map.md` §2 | D-01 (blocking) | Lock D-01 by 2026-06-07 | revenue-model conversion; NSM; financial scenario |
| 7 | `15-financial-framework/revenue-model.md` §3 | A-03 | Re-review at P2 + 60 days | revenue-model; tier-mix |
| 8 | `06-product-strategy` phase map | A-04; H-03 | Re-review at P5 entry | Desk Full v2 ramp; M8 |
| 9 | `15-financial-framework/revenue-model.md` §8 | (none — direct measurement) | Trigger: first paid cohort D60 | revenue-model; scenario worst-case; NSM (TRAS) |
| 10 | `12-onboarding-and-activation` | D-01; D-02 | Trigger: first 90 days post-launch | revenue-model; activation iteration trigger |
| 11 | `15-financial-framework/revenue-model.md` §7; `13-support-and-trust-ops` | C-05 | Decide playbook by 2026-06-07 | Trust Ops scope; Stripe behavior; scenario worst-case |
| 12 | `13-support-and-trust-ops`; `cost-structure.md` §6 | G-01 (drives) | Trigger: first paid cohort 30 days | cost-structure variable; first-hire timing |
| 13 | `13-support-and-trust-ops` | G-01 (drives) | Trigger: first Preview customer 30 days | cost-structure variable |
| 14 | `17-team-and-operating-model/role-priorities.md` Role #8 | (per-SKU at activation) | Trigger: M8 launch | Desk Full v2 economics |
| 15 | `06-product-strategy` phase map; `project_phased_rollout.md` (memory) | A-04; H-02 | Re-review at P2 | cost-structure; vendor-concentration |
| 16 | `project_phased_rollout.md` (memory); `cost-structure.md` §3 | (no specific) | Re-review at every monthly exec | cost-structure; vendor-concentration; QG-04 |
| 17 | `cost-structure.md` §4 | (no specific) | Trigger: 30 days paid usage | cost-structure variable; Trader margin |
| 18 | `cost-structure.md` §2; Stripe live data | F-05 | Test by 2026-06-07; measure post first paid month | revenue-model net; scenario take-rate |
| 19 | `cost-structure.md` §9 | F-01 | Decide by 2026-05-31 | cost recognition; opportunity-cost framing; first-hire ROI |
| 20 | `17-team-and-operating-model/team-design.md` §8 | G-01 | Trigger: P2 entry signal | cost-structure; financial scenarios |
| 21 | `13-support-and-trust-ops`; `17-team-and-operating-model/role-priorities.md` Role #3 | G-01; G-02 | Trigger: support-load threshold | cost-structure; team-design |
| 22 | `06-product-strategy` phase map | G-03 | Trigger: P2 vendor expansion | cost-structure (project SOWs) |
| 23 | `14-risk-compliance-and-safeguards` | A-04; A-05; H-01 | Trigger: PCC v2 G3 30-day stability | All monetization timing; M2 milestone |
| 24 | `06-product-strategy` phase map | A-04 | Trigger: P1 + 60 days defensible cohort | Desk Preview activation; M5 |
| 25 | `06-product-strategy`; M7+M8 | A-04; H-03 | Re-review at P3 entry | Desk Full v2 launch; M8 |
| 26 | `14-risk-compliance-and-safeguards` §8 | C-01 | Re-review at every monthly exec (default firm) | All monetization claims; brand voice; risk posture |
| 27 | `02-company-overview` | A-06 | Re-review at every phase transition | revenue-model geographic mix; compliance |
| 28 | `15-financial-framework/revenue-model.md` §3 | B-04 | Decide by 2026-06-30 | Onboarding flow; conversion path |
| 29 | `06-product-strategy` validation phase | (firm by design) | Closes naturally at P0 → P1 | Cohort sizing; M1 milestone |
| 30 | `15-financial-framework/revenue-model.md` §9 | B-03 | Decide by 2026-06-30 | Tier-ladder integrity; pricing memo |
| 31 | `cost-structure.md` §9 | F-03 | Re-review monthly; alarm if <9 months | Hiring cadence; vendor commitments; GTM spend timing |
| 32 | `kpi-map.md` §8 (Product-Readiness) | (M1 milestone) | Trigger: P0 close-out | M1 milestone; P1 readiness; revenue-model timing |
| 33 | `kpi-map.md` §2 | D-01 (blocking) | Trigger: first 4 weeks post-launch | NSM (TRAS); cohort retention; financial scenario |
| 34 | `kpi-map.md` §2 | D-01 (blocking) | Trigger: first paid cohort D7 | revenue-model; cohort curves; M3 |
| 35 | `kpi-map.md` §3 | D-01 (blocking) | Trigger: first paid cohort D30 | revenue-model; cohort curves; M3; TRAS knob lock (H-04) |
| 36 | `cost-structure.md` §3 §9 | F-02 | Decide threshold by 2026-05-31; measure post first paid month | cost discipline; vendor decisions; scenario worst-case |
| 37 | `cost-structure.md` §3 | (no specific) | Re-review at every monthly exec | vendor management; concentration risk; resilience |

---

## 3. Definitions (locked vocabulary)

These terms are used throughout this folder, the KPI map, and the scenario inputs. They are pinned here once so they don't drift.

| Term | Definition |
|---|---|
| **Early cohort** | A paid-tier cohort within ≤90 days of that tier's launch (or within ≤90 days of the customer's signup). |
| **Mature cohort** | A paid-tier cohort ≥90 days past the tier's launch AND past the individual customer's 90-day mark. Both conditions must hold. |
| **Activated free user** | A free user who has completed the activation definition locked in `21-decision-log` row **D-01**. Until D-01 is `DECIDED`, all rows referencing this term are **directional only**. |
| **Validated assumption** | An assumption whose `Status` has moved to `Validated` because ≥60 days of real cohort data confirm within the assumption's stated band. |
| **Directional only** | An assumption whose Type permits planning use, but whose Status (Not validated / Validating) means it must NOT be used as a load-bearing input in financial models. |
| **Drawdown-correlated churn** | A churn delta correlated with crypto-market drawdowns >20% in a calendar month. Magnitude expectation: 1.5–2x normal churn (qualitative; not yet validated against internal data). |
| **At maturity** | Used in band statements (e.g., "Trader churn 5–10% at maturity") — refers to the mature-cohort definition above, not to a calendar age of the company. |

---

## 4. Assumptions about pricing

**Load-bearing:**

- Trader at $79/mo is the conversion target SKU.
- Desk Full v2 anchors the upper revenue ceiling — but it is **time-locked to P5** by product readiness, not by demand.
- Per-seat economics on Desk Full v2 are the lever that makes the SKU economically meaningful at small fund scale.

**What we are NOT assuming:**

- That the price ladder will hold without adjustment after first cohort feedback. Pricing should be re-tested after P1 + 60 days of revenue.
- That regional pricing variants are needed near-term. They are a P3+ decision.

## 5. Assumptions about conversion

We deliberately frame conversion as **ranges by cohort maturity**, not point estimates:

| Stage | Cohort | Plausible range | Confidence | Row |
|---|---|---|---|---|
| Free → Trader | Early cohort (P0–P1) | 1–4% | Low | (Row 6 lower bound at maturity) |
| Free → Trader | Mature cohort | 3–7% | Low–Med | Row 6 |
| Trader → Desk Preview | Mature (P2+) | 5–12% | Low | Row 7 |
| Desk Preview → Desk Full v2 | Mature (post-P5) | 10–25% | Very Low | Row 8 |

**These are not forecasts.** They are the bands beyond which results should be treated as anomalous and investigated. The bands are based on adjacent-market reasoning (B2B SaaS conversion patterns adjusted downward for trust-sensitivity and Crypto-trading-tool informal benchmarks), not internal data. ASSUMPTION grade reflects this — they tighten only after first-cohort validation.

The Validation Gate Rule (top of this document) governs how these bands flow into models.

## 6. Assumptions about churn / retention

- **Trader maturity churn 5–10%/month** (Row 9) is the load-bearing planning band.
- **Early-cohort churn 10–20%/month** (Row 10) is acceptable for ≤90 days post-launch IF activation flow improvements are actively being shipped.
- **Drawdown-correlated churn** is real; magnitude expectation 1.5–2x normal churn during BTC drawdowns >20%/month. Qualitative until internal data validates.

What we are NOT assuming:

- That Desk Preview / Desk Full v2 churn will look like Trader churn. Higher-tier customers churn less but more expensively (longer sales cycle, larger refund exposure).
- That a single retention experiment will move churn meaningfully. Trust-driven retention compounds slowly.

## 7. Assumptions about support load

| Tier | Average min/user/month | p95 min/user/month | Row | Notes |
|---|---|---|---|---|
| Free | 0–5 | 30 | (informational) | Self-serve; KB + canned responses |
| Trader | ≤30 | 90 | Row 12 | Including incident overhead |
| Desk Preview | ≤90 | 240 | Row 13 | Higher expectations, slower escalation |
| Desk Full v2 | TBD per-seat | TBD | Row 14 | Modeled at SKU activation, not before |

**Hidden assumption:** when a market regime flip causes a wave of "is the system broken" tickets, average minutes don't capture the burst. Capacity planning should use p95, not mean.

## 8. Assumptions about vendor costs

The vendor-cost rules below are now first-class numbered rows (36, 37) — they are no longer narrative-only.

- **Row 36 — Vendor cost ≤25% of MRR at maturity** (H risk if violated).
- **Row 37 — Single-vendor concentration ≤40%** of total vendor cost. Concentration is a structural fragility, not a price problem.
- **Overage budget is treated as planned spend, not surprise.** Every vendor with overage exposure has a monthly cap with hard alarms.

## 9. Assumptions about team / hiring pace

- **Founder-only through P1.** No hires before P2 (Row 20).
- **First hire is a contract support / trust-ops contractor** (Rows 21, G-01), not an engineer.
- **First engineering contractor** is for vendor integration work (Bybit at P2, additional data feeds), scoped per project, not retainer (Row 22, G-03).
- **First full-time hire** is not before P3, and the role is dictated by the bottleneck observed at P2, not by a pre-set org chart.
- **Founder time is recognized as a real cost** at the internal rate (Row 19 — DECISION NEEDED, $100/hr placeholder, deadline 2026-05-31).

## 10. Assumptions about product readiness and launch pacing

- **P0 (validation, May 2026):** cohort cap 40 (Row 29), no monetization pressure, Binance Testnet only.
- **P1 (Jun–Jul 2026):** narrow ship, Trader tier monetized, only after PCC v2 G3 stable ≥30 days (Row 23).
- **P2 (Aug–Sep 2026):** vendor expansion (Bybit, additional feeds — Row 15), Desk Preview activation (Row 24).
- **P3 (late 2026 / early 2027):** scale + first compliance posture upgrade work begins.
- **P5 (Mar–May 2027):** Desk Full v2 launch, per-seat features, audit-grade exports (Row 25).

**No tier launches without its prerequisite gate.** Pulling SKU launches forward to chase revenue is the single most likely way the financial framework becomes a fiction.

## 11. Highest-risk assumptions (validate first)

Sorted by leverage on the model — these are the assumptions where being wrong by 30% changes everything:

1. **#9 / #10 — Trader churn bands.** A 50% churn delta on a small base is catastrophic. Validate within 60 days of paid launch.
2. **#6 — Free → Trader conversion.** If the upgrade rate is below the floor of the band, the entire monetization thesis fails. Note: blocked by D-01 closure.
3. **#33 / #34 / #35 — Activation rate, D7 retention, D30 retention.** Upstream of #6 and load-bearing for NSM (TRAS).
4. **#12 — Support load per Trader user.** Mis-estimating this drives the wrong first-hire decision.
5. **#16 — CoinGlass single-source dependency.** A vendor change here is product-blocking.
6. **#17 — LLM cost per user.** Superlinear scaling here erodes Trader margin first.
7. **#11 — Refund rate target.** Refund-wave under stress is the financial expression of trust-event risk; H grade reflects this.
8. **#36 — Vendor cost / MRR ceiling.** Breach of the 25% threshold is the dominant cost-shape failure mode.
9. **#23 — P1 narrow-ship readiness gate (G3 stable ≥30 days).** Slipping this slips everything downstream.
10. **#26 — Real-capital authorization gate.** This is firm, not validated. If business pressure forces it earlier, the entire risk posture is invalidated.
11. **#19 — Founder internal rate.** Cosmetic until a fundraise; then suddenly load-bearing.
12. **#32 — Validation cohort completion.** Direct input to M1 milestone and P1 readiness.

## 12. How to use this file

- **Every financial deliverable** (deck slide, sheet model, fundraising narrative) must cite assumption numbers from Table A.
- **Every model input** must be checked against `Status` in Table A. If Status is `Not validated` or `Validating`, the input is `directional only` per the Validation Gate Rule at the top of this document.
- **When an assumption is validated** against real data, update its `Status` field to `Validated` and add a note in `21-decision-log` referencing the validating dataset.
- **When an assumption is invalidated**, do NOT silently change downstream models. Log the change in `21-decision-log` first, propagate to every "Downstream models affected" target in Table B, then update Status to `Invalidated`.
- **Phase transitions** force a full review of this file. Specifically, every row's `Status` and `Deadline / Re-review trigger` must be re-evaluated at P0→P1, P1→P2, etc.
- **Cross-walk on every monthly exec review.** Pull Table B's `Decision-log ID` column against `21-decision-log` to confirm no decisions silently moved without propagating to this file.

---

*Last reviewed: 2026-05-08. Next mandatory review: at P1 narrow-ship decision (H-01) or 2026-06-07, whichever comes first.*
