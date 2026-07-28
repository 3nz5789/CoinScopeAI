# Executive Summary — v1 (Operator-Grade)

**Status:** Wave 1 · v1 · 2026-05-07
**Companion to:** `business-plan/01-executive-summary.md` (locked v1 single-page narrative, 2026-05-01)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **operator-grade** summary. It is structured for execution — current state, value prop, risks, success conditions, priorities — not for narrative or pitch use. The locked v1 narrative file is for stakeholders reading one piece; this file is for anyone who has to *do* something.

---

## 1. Strategic summary

CoinScopeAI is **AI-driven capital-preservation infrastructure for disciplined crypto-perpetuals traders and small funds.** The product evaluates signals on USDT-perp venues, classifies market regime in real time (Trending / Mean-Reverting / Volatile / Quiet), and runs configurable risk gates (drawdown, daily loss, leverage, position heat, max open positions) at user-defined thresholds before any trade arms. Capital remains in the user's exchange account. We do not generate alpha, deliver signals, custody capital, execute autonomously without authorization, or provide fund-formation tooling.

The strategic premise is that three structural shifts overlap inside a 24–36 month window:

| Force | What's shifting | What it enables for CoinScopeAI |
|---|---|---|
| Demand | Surviving disciplined retail perp traders reject signal-group economics; they buy *process* over *signals* | Willingness to pay for risk infrastructure (not alpha) at $79–$1,199/mo |
| Supply | AI collapses the cost of building institutional-grade quant tooling — small teams ship 2019 hedge-fund engineering | Solo-founder + contractor team can credibly compete on quality |
| Geography | MENA moves from downstream market to crypto-native infrastructure hub; UAE clarity, family-office allocation rising | UAE-built, MENA-rooted positioning has structural credibility, not narrative-only |

Defensible share lives at the intersection. The window closes as Force 2 brings competitors online, so execution discipline during validation matters as much as the validation itself.

---

## 2. Current business context

| Dimension | Current state | What it is *not* |
|---|---|---|
| Legal entity | UAE founder, sole prop | Not yet a regulated entity, not yet a fund, not yet a registered investment adviser |
| Geography | Target UAE/MENA + global EN; US blocked at signup | Not licensed in the US; not pursuing US users in P0–P2 |
| Funding | Bootstrap-efficient, founder-funded | Not raised; no priced round before validation passes |
| Team | Solo founder, P4 contractor support planned at v2 build (~3 months at highest-risk phase) | Not a founding team; no full-time engineers besides founder |
| Validation | P0 active (May 2026) — 30-day validation phase against PCC v2 §8 Capital Cap criteria | Not production-ready; no real capital deployed |
| Cohort | Soft launch (P1) opens 2026-06-01 — 40 paid users at founder-cohort pricing | Not a public launch; not yet open to general signup |

**ASSUMPTION:** P0 validation passes on schedule. If it does not, P1 slips and the strategic priorities below shift toward extending validation, not toward growth.

---

## 3. Current product posture

| Layer | State | Notes |
|---|---|---|
| Engine | Live on Binance Testnet only | Real-capital gate is hard; no real orders during validation |
| Endpoints | `/scan`, `/risk-gate`, `/position-size`, `/regime/{symbol}`, `/performance`, `/journal` | API is internal during P0; documented for P1 |
| Vendor stack (P1 narrow) | CCXT (4 venues), CoinGlass, Tradefeeds, CoinGecko, Claude (minimal) | P2 expansion deferred; no Bybit until P2 |
| Risk thresholds (locked) | 10% max drawdown · 5% daily loss · 10x max leverage · 5 max open positions · 80% position heat | Locked 2026-05-01 (PCC v2 §8) |
| Regimes (v3 ML) | Trending / Mean-Reverting / Volatile / Quiet | Confidence + gate-result surfaced on every signal |
| Surfaces | Web dashboard (coinscope.ai), Telegram (@ScoopyAI_bot) | Product-tier voice on both — no marketing fluff |
| Onboarding | Auth → exchange connection → testnet sandbox | No real-capital path during validation |
| Billing | Stripe-ready; $79 / $399 / $1,199 + per-seat ($149 or $249) | Live for P1 cohort, not for general public |

**Maturity honest framing:** the engine is functional and instrumented; the product is testnet-validated, not production-validated. Saying anything stronger violates anti-overclaim discipline.

---

## 4. Core user segments

Three personas, locked v1 (internal names only):

| ID | Name | One-line | Primary pain | Willingness to pay |
|---|---|---|---|---|
| P1 | Omar — Self-Taught Methodist | Solo retail trader who built his own discipline framework after losing once | Tools either replace his framework or ignore it | Trader $79/mo |
| P2 | Karim — Engineer Trader | Quant-curious software engineer trading perps part-time | Wants programmable risk and clean APIs, not signal feeds | Trader $79 → Desk Preview $399 over time |
| P3 | Layla — Solo PM | Solo portfolio manager running $200k–$1M aggregate book | Needs institutional-grade risk surface without institutional overhead | Desk Preview $399 → Desk Full $1,199 + per-seat over time |

**Deferred (post-P2):** funds >$5M AUM, prop desks, signal resellers, US-domiciled traders.

**REQUIRED INPUT:** §3.7 interview validation in flight; persona reconfirmation expected before P1 mid-cohort review.

---

## 5. Value proposition (operator-grade restatement)

> **AI-driven capital-preservation infrastructure that enforces the discipline you've already built.**

What this means for the buyer:

1. **Risk gates run *before* trade arming, not as a post-hoc audit.** Drawdown, daily loss, leverage, heat, and position count are first-class UI; rejected trades come with the explicit gate that fired.
2. **Regime is named, not implied.** Every signal carries a regime label (Trending / Mean-Reverting / Volatile / Quiet) and a confidence score, so the buyer can decide whether the signal fits their framework.
3. **The buyer's capital stays in the buyer's account.** No custody, no pooled capital, no fund vehicle. Exchange is the source of truth.
4. **Anti-overclaim is built-in.** We do not call ourselves production-ready until §8 Capital Cap criteria are met. We do not claim ARR we haven't earned. We do not show signals we cannot evidence.

What we explicitly do *not* sell: alpha, signals-as-a-service, autonomous execution without authorization, custody, fund formation, copy-trading.

---

## 6. Key risks (top 7, severity-ordered)

| # | Risk | Severity | Mitigation in plan |
|---|---|---|---|
| 1 | P0 validation fails or extends — P1 launch slips | High | PCC v2 G1–G4 gates; explicit Capital Cap; Validation_Phase_Exit_Memo template |
| 2 | Vendor outage or API degradation (Binance, CoinGlass, etc.) | High | Vendor_Failure_Mode_Mapping_v1; P1 stack narrow; redundancy at P2 |
| 3 | Regulatory framing of US/EU users tightens before licensure path is chosen | High | US blocked at signup; counsel brief v2; jurisdictional posture documented |
| 4 | Solo-founder bus factor — no second engineer until v2 contractor window | High | P4 contractor support planned at highest-risk phase; documentation discipline |
| 5 | Anti-overclaim discipline drifts under launch pressure | Medium-High | Locked v1 narrative; brand-voice enforcement skill; review pass before any external claim |
| 6 | Real-capital gate breach (testnet → mainnet bug) | Critical-if-realized | Hard gate at code level; PCC v2 §8 Capital Cap; daily kill-switch |
| 7 | Persona drift — actual paid users diverge from P1/P2/P3 | Medium | §3.7 interview validation; cohort review at P1 mid-point |

Severity assumes pre-mitigation. Post-mitigation severity is materially lower for #1–#5; #6 is critical regardless and must remain the focus of the highest-care review pass.

---

## 7. What makes the business credible if executed well

- **Validated cohort data, not founder narrative.** Post-validation, the conversation shifts from "we believe" to "the cohort showed." That is the structural credibility unlock.
- **MENA-built, MENA-rooted.** UAE founder, UAE entity path, MENA-first positioning is durable — not a marketing veneer added after the fact.
- **Anti-overclaim track record.** Each version of the plan and each external claim passes a documented audit. Stakeholders learn over time that we don't oversell.
- **Risk-first product surface.** Risk controls are first-class UI, not a hidden setting. This is observable in 30 seconds of using the product.
- **Capital stays with the user.** The custody-free posture is structurally aligned with regulatory direction across UAE/EU/US, even if specific licensures vary.

---

## 8. What must be true for success

If any of these is false, the plan is wrong, not late.

| # | Must be true | How we test it |
|---|---|---|
| MT1 | Disciplined retail perp traders will pay $79/mo for risk infrastructure (not signals) | P1 cohort retention + churn at month 1, 2, 3 |
| MT2 | Solo PMs will pay $399 → $1,199 for institutional-grade risk surface | Desk Preview cohort signal in P1, full validation at P5 |
| MT3 | Founder-led distribution scales to ~500 paid users without paid acquisition | M5 paid-acquisition trigger only if Trader CAC validates |
| MT4 | UAE/MENA + global EN demand is large enough at our price points | Geographic mix in P1 cohort, refined in P2 |
| MT5 | The engine remains stable under P2 vendor expansion (Bybit, additional providers) | P2 charter exit criteria |
| MT6 | Anti-overclaim discipline holds under acquisition pressure | Founder discipline + brand-voice enforcement skill in production |

**REQUIRED INPUT:** Acceptance thresholds for each MT belong in `13-kpi-okr.md` (already locked v1) and should be cross-referenced here in the next pass.

---

## 9. Top strategic priorities (executive view)

Full ranked list with rationale lives in `strategic-priorities.md`. Executive view:

1. Pass P0 validation against PCC v2 §8 Capital Cap criteria
2. Open P1 soft launch on 2026-06-01 with a 40-user cohort under cohort pricing discipline
3. Hold the line on anti-overclaim across product, brand, and external claims
4. Run §3.7 interviews to confirm or revise the three locked personas before P1 mid-cohort review
5. Lock vendor failure-mode runbooks before P2 expansion
6. Decide the post-validation legal-entity posture before structured raise opens
7. Stand up support and incident operations sufficient for 40 paid users
8. Maintain testnet-only discipline with zero real-capital deployment until §8 criteria pass
9. Ship Desk Preview ($399) value-delivery surface at quality bar before P1 close
10. Write the post-validation fundraising narrative against actual cohort data, not projections

---

## 10. Near-term vs. medium-term focus

| Horizon | Window | Focus | Out of scope |
|---|---|---|---|
| **Near-term** | Now → P1 close (Jul 2026) | Validation pass · soft-launch ops · cohort observation · anti-overclaim discipline | Paid acquisition, US users, fund-grade tier, Bybit |
| **Medium-term** | P2 (Aug–Sep 2026) → end-2026 | Vendor expansion · public launch · founder-led distribution at scale · post-validation fundraise prep | Desk Full v2 GA, signal-resellers, copy-trading, custody products |
| **Long-term** | 2027 → 2028 | Desk Full v2 launch (P5, Mar–May 2027) · per-seat scaling · MENA institutional inroads · jurisdictional licensure if warranted | Becoming a fund, alpha generation as a product, exchange business |

---

## 11. Cross-references

- Locked v1 single-page narrative: `business-plan/01-executive-summary.md`
- Strategic priorities (full list): `business-plan/01-executive-summary/strategic-priorities.md`
- Business-model summary: `business-plan/01-executive-summary/business-model-summary.md`
- Decision log: `business-plan/_decisions/decision-log.md`
- PCC v2 (gates + §8 Capital Cap): `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Validation exit memo template: `business-plan/_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
