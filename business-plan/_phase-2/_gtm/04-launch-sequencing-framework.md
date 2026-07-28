# GTM — Launch Sequencing Framework

**Task:** `[DOC] GTM — Launch Sequencing Framework`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — P0 → P1 → P2 → P5 entry/exit + per-phase GTM beat
**Anchored to:** §14 launch roadmap; phase map per memory `project_phased_rollout` (P0 May 2026 → P1 Jun-Jul 2026 → P2 Aug-Sep 2026 → P5 Mar-May 2027); PCC v2 §8; PACKAGING tier structure (P5 trigger); ONBOARDING `_onboarding/01-first-time-user-journey.md` 6 gates; PRICING `_pricing/03-monthly-vs-annual-offer-structure.md` §7 founder-cohort window mechanics.

---

## 1. The sequencing principle

Phase 2 GTM is sequenced across four phases. Each has explicit entry criteria (what must be true to start), exit criteria (what must be true to declare "done"), in-phase GTM beat (the dominant motion), explicit anti-actions (what we don't do during the phase), and risks. The framework reserves Phase 5 (Desk Full v2 launch) capacity now so P1/P2 doesn't accidentally over-commit into a channel mix that won't carry DF v2 buyers.

---

## 2. Phase overview

| Phase | Window | Vendor stack (per memory `project_phased_rollout`) | GTM beat | Audience | Customer count target |
|---|---|---|---|---|---|
| **P0 — Validation cohort** | May 2026 (~30 days) | Binance Testnet only; CCXT / CoinGlass / Tradefeeds / CoinGecko / Claude minimal | Recruit + run cohort; document; no public marketing | Validation cohort cap 40 | 40 cohort members |
| **P1 — Narrow Ship** | Jun–Jul 2026 (~8 weeks) | P1 narrow ship vendor stack live; Binance USDT-M production read-only context | Public launch; founder-cohort window; founder-led distribution | UAE/MENA + global EN; Omar / Karim / Layla | 100–200 paid customers |
| **P2 — Vendor expansion** | Aug–Sep 2026 (~8 weeks) | + Bybit integration; vendor-stack tier-up as cohort grows | Steady-state; cohort retention; Phase 3 channel-mix evaluation begins | P1 audience + expanded reach | 300–500 paid customers |
| **P3 — Scale (Phase 3 charter)** | Oct 2026–Feb 2027 | (Phase 3 owns) | Channel-mix lock; first paid acquisition test; first hire | (Phase 3 charter) | (Phase 3 charter) |
| **P4 — Pre-DF-v2 (Phase 4 charter)** | (Phase 4 charter) | (Phase 4 charter) | (Phase 4 charter) | (Phase 4 charter) | (Phase 4 charter) |
| **P5 — DF v2 launch** | Mar–May 2027 | DF v2 platform; per-seat infra | Layla scaling; partner-seat motion; audit-grade reporting v2 launch | Existing DP cohort + new Layla recruits | DP→DF v2 migration ≥70% per `_pricing/05` §6.9 |

Phases 3 and 4 are owned by their respective phase charters when those open. Phase 2 GTM only sequences through P0 / P1 / P2 / P5 directly; P3 / P4 are placeholders for sequencing continuity.

---

## 3. P0 — Validation cohort (May 2026)

### Entry criteria

- Engine API endpoints live (/scan, /risk-gate, /position-size, /regime/{symbol}, /performance, /journal).
- Binance Testnet integration validated.
- PCC v2 §8 published.
- Validation Phase Exit Memo template in place (`_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`).
- Phase 1 outputs LOCKED (per `_phase-2/00-phase-2-charter.md` §3 Phase 2 entry criteria 1–3).

### GTM beat

- **No public marketing.** Cohort recruiting via founder direct outreach to known Karim / Layla / Omar profiles per `03-founder-led-distribution-plan.md` §5.
- **Cap at 40.** Per §14 + memory `project_state_2026-05-02`. No exceptions.
- **Mix target 50/30/20 (P2/P1/P3) per `_decisions/decision-log.md`** — recruitment ratio target, not constraint. Mix floats with who qualifies.
- **Cohort comms cadence per `03-founder-led-distribution-plan.md` §6** — 2x weekly during cohort.
- **Document everything.** Engine update notes, regime classifier behavior, gate-rejection patterns, cohort feedback. This output feeds P1 launch comms (`Trust-First Launch Campaign Plan`, NEXT).

### In-phase anti-actions

- **Don't open public signup.** Cohort is closed; non-cohort signups are deferred to P1 launch.
- **Don't run paid acquisition.** Per Phase 2 charter §2.
- **Don't accept founder-cohort signups.** Founder-cohort is post-public-launch; cohort gets cohort-pricing automatic per `_pricing/03` §7 ("Soft-launch users get founder-cohort pricing automatically").
- **Don't promise P1 launch date publicly.** Validation phase outcome is unknown; promising dates we might miss erodes trust.
- **Don't write press pieces during validation.** Press is downstream of methodology + cohort outcome.

### Exit criteria

P0 → P1 transition requires:

1. Validation cohort completed (~30 days running).
2. Validation Phase Exit Memo signed (per `_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`).
3. PCC v2 §8 gate-status documented (whether or not §8 gates pass — even if gates don't pass, the document is signed).
4. Cohort retention through validation ≥70% (per `03-founder-led-distribution-plan.md` §9 KPI; <50% = §14 stop-the-line condition).
5. PACKAGING `_packaging/00-readme.md` Pk-1 / Pk-2 / Pk-3 / Pk-4 / Pk-5 / Pk-6 ratify-or-revise lock based on exit memo.
6. PRICING `_pricing/00-readme.md` Pr2-1 ratify-or-revise lock based on exit memo.
7. ONBOARDING `_onboarding/05-friction-audit-across-current-flow.md` P0 remediation backlog cleared.
8. SUPPORT `_support/00-readme.md` 8 Su-* decisions locked.
9. Production engine surfaces ready for public load (engine status page, methodology docs, "what we don't do" page — all live).

### Risks

| Risk | Mitigation |
|---|---|
| Validation reveals fundamental persona misfit | §14 stop-the-line condition 6 — public launch holds until §9 messaging matrix is rewritten |
| Engine drift mid-cohort | Cohort comms cadence catches it early; engine config is locked during validation per Scoopy custom instructions ("No core engine changes" during validation) |
| Vendor outage during validation | Status page surfaces; cohort accepts as expected risk; not a launch-block |
| Cohort feedback contradicts assumptions in Phase 2 PACKAGING / PRICING | Pr2-1 / Pk-1 revision-trigger conditions fire; revisions documented in decision log |

---

## 4. P1 — Narrow Ship (Jun–Jul 2026)

### Entry criteria

All P0 → P1 exit criteria above met.

### GTM beat

- **Public launch day:** orchestrated per `Trust-First Launch Campaign Plan` (NEXT). Pricing page goes live; founder-cohort window opens.
- **Founder-cohort window: 60 days from public launch day.** Per `_pricing/03` §7. One-shot GTM event.
- **Founder-led distribution per `03-founder-led-distribution-plan.md`** — 5–10 hrs/week cadence; weekly long-form; founder direct outreach 3–5/week.
- **Validation-cohort → paying-customer migration.** P0 cohort gets founder-cohort pricing automatic; conversion offer per `_packaging/01-packaging.md` Pk-6 (NEXT).
- **Pricing page is the conversion surface.** Per `_packaging/03-plan-comparison-table-v1.md` — sticky header, single-toggle annual, mobile collapsed, no urgency mechanics.

### In-phase anti-actions

- **Don't run paid acquisition.** Per Phase 2 charter §2 + `01-go-to-market-strategy-v1.md` §5.
- **Don't extend founder-cohort window mid-launch.** Per `01-go-to-market-strategy-v1.md` §6 anti-pattern. Window is 60 days; extension reads as "we needed to bribe people" + violates time-bounded discipline.
- **Don't A/B test pricing page.** Per `_pricing/02-initial-pricing-philosophy.md` Principle 6 + `_packaging/00-readme.md` Pr2-1 revision discipline.
- **Don't open public Discord / Telegram community.** CANDIDATE-P3 only.
- **Don't accept signal-group / copy-trade / leverage-maximizer co-marketing.** Anti-channel per `02-initial-channel-strategy.md` §4.
- **Don't make founder-cohort comms drift to "lifetime."** §6.10 Flag 1 inherited.
- **Don't open international localization at P1.** UAE/MENA + global EN audience only.

### Exit criteria

P1 → P2 transition requires:

1. Founder-cohort window closed (T+60 days from public launch).
2. P1 paid customer count ≥100 (target: 100–200).
3. Activation funnel KPIs landing in or above downside per `_onboarding/02-activation-milestones-definition.md` §4.
4. Founder time on GTM steady at 5–10 hrs/week (per `03-founder-led-distribution-plan.md` §9 KPI; >12 hrs sustained 2 weeks = §9 falsifier fires).
5. Support load steady at <10 hrs/week (per `_support/01` §2; >10 hrs/week trigger fires).
6. Vendor-outage incident count documented; trust-load through incidents intact.
7. Phase 3 charter opens; Phase 3 channel-mix evaluation begins.

### Risks

| Risk | Mitigation |
|---|---|
| Public launch produces <50 signups in first 30 days | `01-go-to-market-strategy-v1.md` §9 falsifier — accelerate Phase 3 channel-mix decision; consider paid testing |
| Founder-cohort uptake <40% in window | `_pricing/01` revision trigger #4 — reopen Pr2-4 (founder-cohort discount magnitude) |
| Trader → DP conversion <4% by mid-P1 | `_pricing/01` revision trigger #2 — investigate DP positioning |
| Vendor outage with >10% user impact during launch window | `_support/03` Escalation A fires; status page + active push per Su-5 |
| US user signup attempts breaking region-block | `_onboarding/03` Step 1 audit re-runs; Eng remediation immediate |
| Founder-cohort comms drift detected | Stop launch comms; rerun anti-overclaim audit per `Messaging Risk Review for Public Claims` (NEXT QA) |

---

## 5. P2 — Vendor expansion (Aug–Sep 2026)

### Entry criteria

All P1 → P2 exit criteria met.

### GTM beat

- **Steady-state founder-led + organic** continues from P1 cadence.
- **Bybit integration ships.** Multi-venue is unlocked at DP+ per `_packaging/02-free-vs-paid-boundary.md` row F. Pricing-page tier comparison updates to "Bybit (Aug-Sep 2026)" → "Bybit (live)" per launch.
- **Cohort retention focus.** First 12-month retention cohort data lands during P2; KPI dashboard surfaces retention per tier per cohort.
- **Phase 3 channel-mix evaluation begins.** CANDIDATE-P3 channels reviewed against §9 KPI baseline. Phase 3 charter opens by P2 close.

### In-phase anti-actions

- **Don't ship Bybit integration without anti-overclaim audit on multi-venue messaging.** Pricing page + onboarding + methodology docs all need Bybit-aware language without overclaiming "all venues now."
- **Don't accelerate Phase 3 paid acquisition into P2.** Phase 3 charter is Phase 3, not late-Phase-2.
- **Don't open community at P2.** Phase 3 channel-mix decision precondition is support coverage scaled (per `_support/04-support.md` Su-8 + `02-initial-channel-strategy.md` Public Discord / Telegram row). Support hire is Phase 3 trigger; community follows hire.
- **Don't break founder-cohort discipline post-window.** Window-closed = standard pricing applies. No "extension promo" or "surprise discount" violating §6.7.

### Exit criteria

P2 → P3 transition (Phase 3 charter opens) requires:

1. Bybit integration live + anti-overclaim audit clean on multi-venue surfaces.
2. P2 customer count ≥300 (target: 300–500 cumulative).
3. First 12-month cohort retention numbers landed; trends visible.
4. Phase 3 channel-mix evaluation criteria built (consumes `02-initial-channel-strategy.md` §6 CANDIDATE-P3 set).
5. Founder time + support load sustainable; if Su-8 trigger fired during P2, first hire onboarded.
6. Phase 4 §11 financial model build can begin (Phase 4 charter opens with Phase 2 inputs locked).

### Risks

| Risk | Mitigation |
|---|---|
| Bybit integration delays past P2 window | Phase map slip is a trust event; status page + cohort comms transparent; don't promise compensation, accept reality |
| Cohort retention <50% at 12 months | `01-go-to-market-strategy-v1.md` §9 falsifier — strategy revision trigger; Phase 3 channel-mix decision pauses pending root-cause analysis |
| Phase 3 channel-mix decision premature | Hold the line; Phase 3 charter opens only when entry criteria 1–6 met |
| Founder time over-loading on multi-venue support | Su-8 first hire trigger; per `_support/01` §2 |

---

## 6. P5 — Desk Full v2 launch (Mar–May 2027)

### Entry criteria (anticipated; locked at Phase 5 charter)

- DF v2 platform ready: audit-grade partner reporting (LP-style), per-seat infrastructure, custom Telegram routing.
- DP → DF v2 migration mechanics locked.
- Founder-cohort window for DF v2 launch designed (separate from P1 founder-cohort).
- Phase 5 charter opens with Phase 4 §11 financial model + Phase 4 fundraising posture inputs.
- Layla cohort retention ≥80% through P3 / P4 (per `_pricing/05` §6.9 base case).

### GTM beat (anticipated)

- **DF v2 launch is its own one-shot GTM event.** Separate from P1 founder-cohort.
- **Existing DP customers are the conversion target.** DP → DF v2 migration rate target ≥70% per §6.9 base.
- **New Layla recruits enter at DF v2 directly OR via DP discovery step.** Per `_onboarding/01-first-time-user-journey.md` Layla swim-lane.
- **Per-seat motion launches.** Partner read-only seats + analyst seats become available; per-seat density target ≥1.5 per `_onboarding/02-activation-milestones-definition.md` DF-3.
- **Audit-grade partner reporting becomes available.** Methodology + reporting docs publish; LP-aware Solo PMs get the report-as-evidence demand surface.

### In-phase anti-actions (anticipated)

- **Don't repeat P1 founder-cohort phrasing.** Different cohort, different window, different mechanics. Canonical phrasing form inherited but window-specific.
- **Don't promise audit-grade reporting beyond v2 spec.** "v2 covers X; v3 might cover Y" — qualifications inherit.
- **Don't open international localization at P5.** Still UAE/MENA + global EN unless Phase 5 charter explicitly amends.

### Exit criteria (anticipated)

(To be locked in Phase 5 charter.)

---

## 7. Cross-phase capacity reservation

The framework reserves capacity for Phase 5 by ensuring P1/P2 GTM doesn't lock channel mix in a direction incompatible with DF v2:

| P1/P2 commitment | Phase 5 compatibility |
|---|---|
| Founder-led + organic | Compatible — DF v2 launch can be founder-led intensified |
| Methodology-as-demand-surface | Compatible — DF v2 audit-grade reporting extends the methodology surface |
| Anti-channel list (signal groups, copy-trade, leverage maximizers, mass affiliates) | Compatible — Phase 5 inherits |
| No paid acquisition | (Phase 3 may unlock) |
| No public community | (Phase 3 may unlock with support coverage) |
| 12-week content rotation | Compatible — Phase 5 likely accelerates rotation during DF v2 launch window |
| Founder direct outreach to Karim / Layla profiles | Compatible — Layla outreach intensifies for DF v2 |

If a P1/P2 GTM action would create a Phase 5 incompatibility (e.g., burning credibility with Layla audience for short-term P1 conversion), the action is anti-pattern by sequencing principle.

---

## 8. Per-phase KPI summary

| KPI | P0 target | P1 target | P2 target | P5 target |
|---|---|---|---|---|
| Customer count (cumulative) | 40 cohort | 100–200 paid | 300–500 paid | DP→DF v2 ≥70% migration |
| Founder time on GTM | ~5 hrs/week (cohort comms) | 5–10 hrs/week | 5–10 hrs/week | (Phase 5 charter) |
| Founder-cohort uptake | (auto for cohort) | ≥40% in 60-day window | (closed) | (DF v2 cohort separate) |
| Methodology-page → signup | (cohort-recruited) | ≥1% conversion | ≥1% sustained | (Phase 5 charter) |
| Cohort retention (12-mo) | (validation only) | (early signal) | First retention data | ≥80% Layla cohort |
| Support load | (cohort-managed) | <10 hrs/week | <10 hrs/week (or hire) | (Phase 5 charter) |

---

## 9. The "what changes per phase" register

Documenting what's allowed to change per phase prevents accidental scope-creep:

| Item | P0 | P1 | P2 | P5 |
|---|---|---|---|---|
| Pricing | Track B (cohort-priced) | Track B (LOCKED through P0 exit memo, then standard) | Standard | DF v2 separate launch pricing |
| Founder-cohort window | Cohort-auto | 60-day window post-public-launch | (closed) | DF v2-specific window (separate) |
| Public sign-up | Closed | Open | Open | Open |
| Channel mix | Founder direct outreach only | IN-V1 channel set | IN-V1 + Phase 3 evaluation begins | Phase 3 lock active + DF v2 motion |
| Paid acquisition | None | None | None (Phase 3 evaluates) | (Phase 3 lock) |
| Community | None (cohort Telegram only) | None | None (Phase 3 evaluates with support coverage) | (Phase 3 lock) |
| Bybit | None | None | Live (mid-P2) | Live |
| Audit-grade partner reporting | None | None | None | Live (DF v2) |
| International localization | None | None | None | None at v1 (Phase 5 charter may amend) |

---

## 10. Failure modes specific to sequencing

- **Phase compression.** Founder skips P0 validation cohort to "save time." Trust posture broken; PCC v2 §8 gate-status undocumented; positioning risks invalidation. **Validation phase is non-negotiable.**
- **P1 → P2 transition before exit criteria met.** "Let's just open Bybit early" without P1 lock cleanly closed = disorderly state. Hold transitions strict.
- **Founder-cohort window extension.** "Just two more weeks" — once. Then becomes standing extension. Anti-pattern.
- **Phase 3 paid acquisition test snuck into P2.** Even "small budget test" violates Phase 2 charter §2; produces noisy data + pre-anchors Phase 3 decision.
- **Phase 5 capacity not reserved.** P1/P2 over-commits to channel mix that won't carry Layla buyers. Per §7 — sequencing principle is the prevention.
- **Validation cohort cap relaxed.** "We have 50 great applicants" — accept all. Cohort mechanics break, validation signal noisy. **Cap is 40.**
- **P0 documentation skipped.** "We'll write it up later." Later is now never. Validation Phase Exit Memo is a hard exit gate.
- **Public launch date pre-promised.** "Launching June 15!" announced in P0. Then validation reveals issues. Either ship broken or break promise; both bad.
- **Phase order swap.** "Let's do Phase 5 DF v2 launch before Phase 2 founder-cohort." Strategic incoherence; revenue dependency violations; cohort confusion.
- **Channel-mix lock during P1.** "Twitter is working, lock it in." Phase 3 charter is for channel-mix lock; P1 is for organic + founder-led discovery.
- **Cohort comms drift to public launch comms style.** P0 cohort comms are validation-focused; P1 launch comms are conversion-focused. Mixing the two erodes both.

---

## 11. What this unlocks

- Phase sequence is canonical for Phase 2 → Phase 5 GTM planning.
- `Trust-First Launch Campaign Plan` (NEXT) consumes the P0 → P1 transition as the launch trigger.
- `Waitlist and Early Access Motion` (NEXT) consumes the founder-cohort window mechanics + P0 → P1 transition.
- `Funnel Structure from Content to Demo to Paid` (NEXT) consumes per-phase KPI targets.
- `Acquisition KPI Dashboard Definition` (NEXT METRICS) consumes per-phase KPI targets as dashboard data model.
- Phase 3 charter has explicit P2 → P3 entry criteria.
- Phase 4 charter has explicit Phase 4 entry-criteria placeholder.
- Phase 5 charter has explicit P4 → P5 entry-criteria placeholder + capacity reservation.
- Cross-workstream coordination has explicit sequencing dependencies (Pk-1 / Pr2-1 lock waits for P0 exit memo; ONBOARDING P0 remediation precedes P1 launch; SUPPORT Su-* locks before P1 launch).
