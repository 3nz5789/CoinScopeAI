# Phase 2 Charter — Monetization

**Owner:** Founder / Strategy Chief of Staff
**Phase window:** Jul–Sep 2026 (overlaps tail of P0 Validation Cohort, full P1 Narrow Ship, opening of P2 Vendor Expansion)
**Sits on top of:** Phase 1 strategic-foundation lock (`_phase-1/00-phase-1-charter.md`) and v1 framework LOCKED 2026-05-01 (`00-framework.md` + `_decisions/decision-log.md`)
**Last updated:** 2026-05-04

---

## 1. Goal

Convert the Phase 1 strategic foundation into a working **commercial system**: the precise way CoinScopeAI is packaged, priced, sold-into-funnel, onboarded, and supported. Five workstreams determine *what we ship as the commercial offer, what we charge, how the funnel converts, what the new-user lands into, and how we keep them safely operating* during P1 Narrow Ship and into P2:

1. **PACKAGING** — tier structure, free vs paid boundary, gating logic, plan comparison surface.
2. **PRICING** — Track B v1 ratify-or-revise, founder-cohort policy operationalized, refund + dunning, AED courtesy display.
3. **ONBOARDING** — signup → account verification → exchange connection → first-signal-seen → first-gate-decision-seen, with §3.5 "we'll be back" sub-$5k flow.
4. **SUPPORT** — runbooks, escalation, incident comms, vendor-outage posture, trust-load handling, refund-handling SOP.
5. **GTM** — funnel mechanics for the Narrow Ship: offer, pricing page, beta-cohort conversion, founder-cohort comms. **Channel-mix selection (founder-led vs content vs partnerships vs paid) remains deferred to Phase 3** per Phase 1 charter §8.

Phase 2 is **not** about: channel selection, paid acquisition, content calendars, fundraising posture, financial-model build-out (that consumes Phase 2 outputs in Phase 4), or compliance counsel deep dive.

---

## 2. Scope (in / out)

| In scope (Phase 2) | Out of scope (defer) |
|---|---|
| Tier structure (count, naming, gating) ratifying or revising Track B | Channel mix, paid acquisition (Phase 3) |
| Free vs paid boundary, gating type per feature, upgrade-prompt rules | Content calendar, long-form publishing (Phase 3) |
| Plan comparison table v1 (pricing-page surface) | Marketing-driven trust assets, PR (Phase 3) |
| Track B v1 ratify-or-revise (Trader $79 / Desk Preview $399 / Desk Full $1,199) | Financial-model build (Phase 4 — consumes Phase 2 outputs) |
| Per-seat $149 vs $249 final lock | Fundraising narrative + posture (Phase 4) |
| Founder-cohort policy operationalized (eligibility, lock window, comms) | Compliance counsel deep dive, license filings (Phase 4) |
| Refund / dunning / past-due / chargeback SOP | Bybit and other venues (P2 design-only per phase map) |
| AED courtesy display final form, Stripe configuration | Layla Phase-5 Desk Full v2 flow (Phase 5 input only) |
| Signup → first-signal funnel; account-size floor enforcement | High-touch white-glove onboarding (Phase 5 concept only) |
| Exchange-connection UX (Binance USDT-M only at P1) | API / data-product as separate package (Phase 3 concept only) |
| "We'll be back" sub-$5k flow operational form | |
| Support runbooks: triage, severity, escalation, refund SLA | |
| Vendor-outage support comms (Binance / CoinGlass / Tradefeeds / CoinGecko / Claude minimal stack) | |
| Founder-cohort recruiting + conversion mechanics | |
| Pricing-page copy + anti-overclaim audit on every monetization surface | |

---

## 3. Entry criteria

All four must be true before Phase 2 activates:

1. **Phase 1 PRODUCT outputs locked** — Product Value Ladder + MVP/Beta/Scale Feature Matrix + Decision Register entry **Pr-4** (Free-tier limits) DONE. PACKAGING NOW tasks are dependency-blocked on these per `_phase-2-pending/packaging-canonical-list.md`.
2. **Phase 1 POSITIONING outputs locked** — positioning sentence (P-1), anti-claim list (P-2), Surface Variant Table available. Pricing-page copy and plan-comparison surface inherit from these.
3. **Phase 1 BRAND outputs at NEXT-or-later maturity** — Voice + Tone Guidelines and Patternbook available so PRICING / PACKAGING / ONBOARDING copy can be brand-checked before lock.
4. **§6 v1 framework available** as the canonical reference: tier prices, Free-tier scope (Scope B), founder-cohort policy at v1, refund policy v1, AED handling v1.

If entry criteria #1–#3 are not met when Phase 2 opens, Phase 2 starts with PRICING (which can ratify §6 v1 directly without Phase 1 PRODUCT output) and ONBOARDING NOW tasks that don't depend on the feature matrix; PACKAGING and pricing-page-surface work hold until #1–#3 clear.

---

## 4. Exit criteria

Phase 2 is *complete* when **all five** are true:

1. **PACKAGING** — Tier structure final; Free vs Paid Feature Boundary locked; Plan Comparison Table v1 signed; Premium Feature Gating Rules with per-feature gating type (hard / soft / degraded / read-only). Documented in `_phase-2/01-packaging.md`.
2. **PRICING** — Track B v1 ratified or revised with explicit reason; per-seat $149 / $249 split locked; founder-cohort policy operational (eligibility, comms, Stripe promo-code wiring); refund / dunning / chargeback SOP signed; AED display form locked. Documented in `_phase-2/02-pricing.md`.
3. **ONBOARDING** — End-to-end flow specified: signup → email verification → exchange connection (Binance USDT-M, testnet-first) → first-signal-seen → first-gate-decision-seen → first-billing event. "We'll be back" sub-$5k branch defined. Documented in `_phase-2/03-onboarding.md`.
4. **SUPPORT** — Severity matrix (P1–P4), triage SOP, escalation paths, vendor-outage runbooks per vendor in P1 stack, refund-handling SOP, trust-load comms templates. Documented in `_phase-2/04-support.md`.
5. **GTM** — Pricing page v1 spec; founder-cohort recruiting pack; beta-cohort conversion offer; anti-overclaim audit on every monetization surface; one-pager for the Narrow Ship offer. **No channel selection.** Documented in `_phase-2/05-gtm.md`.

Plus: Phase 2 backlog (`06-task-backlog.md`) has every NOW task either Done or moved to Phase 3 / Phase 5 backlog with reason.

---

## 5. Phase 2 risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Pricing change before validation closes | A Track B revision before P0 cohort exit memo lands invalidates §11 financial-model assumptions and §13 KPI baselines | Pricing changes only after P0 cohort exit memo; if a revision is unavoidable mid-phase, run pre-mortem skill (per memory `feedback_premortem_required`) before locking |
| Free tier scope drift | Loosening Scope B (adding journal, real-time feed, configurable risk gate) breaks §5.3.2 packaging principle and removes the conversion trigger | Scope B is locked at §6.5; any change requires explicit amendment to §6.5 with founder sign-off and a §13 KPI re-baseline |
| Onboarding promises real-capital readiness | If onboarding copy implies the system is production-ready for live capital before PCC v2 §8 gates pass, we credibly mislead users into testing real capital prematurely | Every onboarding step bears the canonical disclaimer: "Testnet only. 30-day validation phase. No real capital." Real-capital gating language traces to PCC v2 §8 |
| Support load underestimated for Desk Preview | P3 buyers expect responsive, knowledgeable support; understaffed support at $399/mo creates churn at the highest-revenue tier | Desk Preview support SLA committed at Phase 2 lock; staffing implication flagged to §10 ops; refund SLA tighter than Trader |
| Founder-cohort comms drift to "lifetime" framing | §6.10 Flag 1 — "founder discount locked-in" implications create a class of legacy users the business can't sustain | §9 messaging matrix rule enforced: "founding-member pricing — locked through your first renewal cycle, then standard pricing applies." Brand-voice review on every founder-cohort surface |
| Vendor-outage support unprepared | Binance / CoinGlass / Tradefeeds / CoinGecko / Claude all have outage history; without runbooks, support absorbs trust damage | Per-vendor outage runbook in `04-support.md`; user-facing comms templates pre-approved; §12 risk register cross-ref |
| Stripe entitlement drift | Billing tier ≠ feature flags = revenue loss + trust damage. Highest expected support cost | `[QA] PACKAGING — Billing-to-Entitlement Logic Review` runs before any pricing change ships |
| Phase 2 scope creep into Phase 3 | Channel selection, paid acquisition, content calendar all naturally surface during pricing-page work; absorbing them blows Phase 2 timing | Phase 2 charter §2 out-of-scope is the contract; surface-level pricing-page copy is in scope, channel-level distribution is not |

---

## 6. Concrete outputs

| Output | File | Format | Status |
|---|---|---|---|
| Phase 2 charter (this doc) | `00-phase-2-charter.md` | MD | DONE |
| PACKAGING scaffold | `01-packaging.md` | MD | NOW |
| PRICING scaffold | `02-pricing.md` | MD | NOW |
| ONBOARDING scaffold | `03-onboarding.md` | MD | NOW |
| SUPPORT scaffold | `04-support.md` | MD | NOW |
| GTM scaffold | `05-gtm.md` | MD | NOW |
| Phase 2 task backlog | `06-task-backlog.md` | MD | NOW |
| Phase 2 deliverable map | `07-deliverable-map.md` | MD | NOW |
| Phase 2 decision register | `08-decision-register.md` | MD | NOW |
| Phase 2 open questions | `09-open-questions.md` | MD | NOW |

---

## 7. Workstream → v1 framework crosswalk

| Phase 2 workstream | Authoritative v1 file(s) | Phase 2 layer adds |
|---|---|---|
| PACKAGING | `06-pricing-monetization.md` (§6.3 Model C, §6.5 Free scope), `05-product-strategy.md` | Tier structure final; Free vs Paid feature boundary; gating-type-per-feature; plan comparison surface; upgrade-path UX |
| PRICING | `06-pricing-monetization.md` v1 (§6.6 Track B, §6.7 refund/founder-cohort, §6.8 currency, §6.9 LTV/CAC sensitivity), `_data/operations/Production_Candidate_Criteria_v2.md` | Track B ratify-or-revise based on P0 cohort exit memo; per-seat $149/$249 lock; founder-cohort operationalization (Stripe promo codes, eligibility comms); dunning + chargeback SOP |
| ONBOARDING | `10-operations-support.md`, `12-risk-compliance-trust.md`, `_data/operations/Production_Candidate_Criteria_v2.md` §8 | End-to-end flow spec; sub-$5k "we'll be back" branch; exchange-connection UX (Binance USDT-M only, testnet-first); first-signal / first-gate-decision instrumentation |
| SUPPORT | `10-operations-support.md`, `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`, `12-risk-compliance-trust.md` | Severity matrix P1–P4; triage SOP; vendor-outage runbooks per vendor in P1 stack; refund SOP; trust-load comms templates |
| GTM | `07-gtm-strategy.md`, `09-brand-messaging.md`, `_phase-1/03-positioning.md`, `_phase-1/07-brand.md` | Pricing-page v1 spec; founder-cohort recruiting pack; beta-cohort conversion offer; Narrow Ship one-pager; anti-overclaim audit on every monetization surface |

---

## 8. Decisions deferred *out* of Phase 2 (deliberate)

These are real decisions but belong to Phase 3+. Recording them so they don't leak in:

- **Channel-mix selection** — founder-led vs content vs partnerships vs paid. **Phase 3.**
- **Content calendar / publishing cadence.** **Phase 3.**
- **Fundraising narrative + bootstrap-vs-venture posture.** **Phase 4.**
- **§11 financial-model build-out** — Phase 2 outputs feed it; Phase 4 builds it.
- **Compliance counsel engagement / license filings.** **Phase 4.**
- **Bybit and other venues** — design-only at P2, no Phase 2 packaging changes.
- **Layla Phase-5 Desk Full v2 surface** — Phase 5; Phase 2 produces concept-only Fund/Desk Plan note.
- **High-touch white-glove onboarding** — Phase 5; concept only at Phase 2.
- **API / data-product as separate package** — Phase 3 concept; not a Phase 2 commitment.

---

## 9. How to read Phase 2 docs

- Each workstream scaffold (`01–05`) follows the same eight-block structure: purpose → why for CSAI → required subsections → recommended artifacts → assumptions → decisions → failure modes → tasks.
- `06-task-backlog.md` is the **execution surface**. Tasks named `[TYPE] [AREA] — Action / Deliverable`. Grouped by area, ordered NOW / NEXT / LATER.
- `07-deliverable-map.md` rows include explicit Phase 1 dependency where applicable.
- `08-decision-register.md` lists only the decisions that block Phase 2 exit (Pk-* for PACKAGING, Pr-* for PRICING, On-* for ONBOARDING, Su-* for SUPPORT, G-* for GTM).
- `09-open-questions.md` lists only the questions whose answers Phase 2 needs.

---

## 10. Phase 2 → Phase 3 handoff

Phase 2 produces these as inputs Phase 3 consumes:

- Pricing-page v1 (live surface) — Phase 3 distributes traffic to it.
- Founder-cohort offer fully operationalized — Phase 3 channel mix decides where to recruit from.
- Conversion-event instrumentation (signup → first-signal → first-gate-decision → first-billing) — Phase 3 needs this to attribute channel performance.
- Support runbooks live — Phase 3 paid acquisition cannot turn on without this.
- Anti-overclaim audit clean across every monetization surface — Phase 3 content + paid acquisition inherit the same audit discipline.

If any of these is missing at Phase 2 exit, Phase 3 cannot open.
