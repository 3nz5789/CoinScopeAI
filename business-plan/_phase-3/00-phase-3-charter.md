# Phase 3 Charter — Operating System

**Owner:** Founder / Strategy Chief of Staff
**Phase window:** Oct 2026 – Jan 2027 (overlaps tail of P2 v1 Public Launch, full P3 v1 Stabilization, opening of P4 Desk Full Prep)
**Sits on top of:** Phase 1 strategic-foundation lock (`_phase-1/00-phase-1-charter.md`), Phase 2 monetization lock (`_phase-2/00-phase-2-charter.md`), v1 framework LOCKED 2026-05-01 (`00-framework.md` + `_decisions/decision-log.md`)
**Last updated:** 2026-05-05

---

## 1. Goal

Convert the Phase 1 strategic foundation and Phase 2 commercial system into a **working operating system**: the cadences, instruments, and review loops that hold the business together while it ships under load. Five workstreams determine *how the founder + P4 contractors actually run the company day to day, week to week, and quarter to quarter*:

1. **OPERATIONS** — operating cadence (daily / weekly / monthly / quarterly), runbooks beyond support (engine release, vendor swap, incident review, founder-unavailable protocol), tooling discipline (Linear / Notion / GitHub / Drive sync), §16 contingency operationalization.
2. **METRICS** — operationalize §13 KPI / OKR framework into living instruments: weekly internal report, monthly stakeholder report, OKR review cadence, anti-overclaim audit on every metric surface, §13 conditional-escalation red-line monitor.
3. **FINANCE** — operationalize §11 financial-model assumptions into a working close + reconciliation loop: monthly close, vendor cost reconciliation, Stripe revenue reconciliation, cash runway dashboard, §11 model-vs-actuals variance review, P0 cohort exit memo financial inputs.
4. **ROADMAP** — operationalize §14 launch roadmap into a functioning gate-review system: phase-gate readiness reviews (P2→P3, P3→P4, P4→P5), §5 capability flow tracking (IB↔VTN↔STN↔RM), public roadmap surface (anti-overclaim audited), launch comms plan execution.
5. **COMPLIANCE** — operationalize §12 risk register + §16 contingency protocols into an audit-able discipline: monitoring → active → triggered review cadence, regulatory-news monitor runbook, US-resident leak audit, AED display audit, vendor-relationship review (CoinGlass dual-relationship especially), counsel engagement cadence, geo-fence integrity check.

Phase 3 is **not** about: writing new strategy, repricing, repackaging, channel-mix selection (deferred — see §8), content calendar (deferred — see §8), fundraising posture, license filings, or building the §11 financial model from scratch (it exists at v1; Phase 3 *operates* it; Phase 4 *raises against* it).

---

## 2. Scope (in / out)

| In scope (Phase 3) | Out of scope (defer) |
|---|---|
| Operating cadence: daily standup-of-one, weekly ops review, monthly close, quarterly OKR review | Channel-mix selection (founder-led vs content vs partnerships vs paid) — Phase 3.5 / Phase 4 |
| Engine release runbook (testnet promotion, rollback, kill-switch test cadence) | Content calendar / publishing rhythm — Phase 3.5 |
| Vendor swap drill (CoinGlass / Tradefeeds / CoinGecko / Claude / CCXT) | Fundraising narrative + raise posture — Phase 4 |
| Incident review / postmortem template | Compliance counsel engagement *outcome* (cadence is in scope; advisory output is Phase 4) |
| Founder-unavailable protocol (§16 Contingency C operationalization) | License filings / regulated-entity restructure — Phase 4 (or §16 Contingency A trigger) |
| Linear / Notion / GitHub / Drive sync discipline + drift-detector cadence | New §11 model build-out (xlsx is a §11 v1 deliverable, not Phase 3) |
| §13 weekly internal report template + monthly stakeholder report template | Layla Phase-5 Desk Full v2 ops surface — Phase 5 input only |
| OKR quarterly review SOP | High-touch white-glove ops — Phase 5 |
| §13 conditional-escalation red-line monitor (gate-rejection acceptance <50%) | Bybit ops integration — P2 design-only; Phase 3 covers stack-as-shipped |
| §13 anti-overclaim audit applied to public dashboards / status page | Sales pipeline / Desk Full enterprise-buyer ops — Phase 5 |
| Monthly financial close SOP (revenue + cost reconciliation, runway) | API / data-product ops surface — Phase 3 concept only |
| §11 model-vs-actuals variance review (quarterly) | |
| P0 cohort exit memo financial inputs (consumed into §11 v1.1) | |
| §6.8 VAT threshold monitor + AED-display audit | |
| Stripe revenue reconciliation SOP, dunning + chargeback ops loop | |
| Phase-gate readiness reviews (P2→P3, P3→P4, P4→P5) | |
| §14 launch comms plan execution surface | |
| Public roadmap surface (status-page index + roadmap teaser, anti-overclaim audited) | |
| §5 capability flow tracking (IB↔VTN↔STN↔RM monthly) | |
| §12 risk register monthly review (status transitions) | |
| §16 contingency drill cadence (regulatory shock / vendor outage / founder unavailable) | |
| Regulatory-news monitor runbook (UAE / GCC / US-relevance scan) | |
| US-resident geo-fence integrity audit (signup + KYC declaration) | |
| AED-display footer-text audit | |
| CoinGlass dual-relationship quarterly review | |
| Counsel engagement cadence (quarterly check-in; ad-hoc on triggered risks) | |

---

## 3. Entry criteria

All four must be true before Phase 3 activates:

1. **Phase 2 PACKAGING + PRICING outputs locked** — Tier structure final, Free vs Paid boundary signed, Plan Comparison Table v1 live, gating rules shipped, Track B ratified-or-revised, founder-cohort policy operational. Phase 3 FINANCE close SOP and METRICS revenue dashboard depend on these.
2. **Phase 2 ONBOARDING + SUPPORT outputs locked** — End-to-end onboarding flow specified, severity matrix + triage SOP + vendor-outage runbooks live. Phase 3 OPERATIONS extends these into the broader operating cadence.
3. **Phase 2 GTM Pricing-page v1 live** — Funnel-conversion instrumentation (signup → first-signal → first-gate-decision → first-billing) wired so METRICS workstream has signal to operate against.
4. **§11 v1 financial model + §13 v1 KPI framework + §14 v1 launch roadmap + §12 v1 risk register + §16 v1 contingency protocols** all available as canonical references. Phase 3 *operationalizes* — it does not re-author.

If entry criteria #1–#2 are not met when Phase 3 opens, Phase 3 starts with OPERATIONS NOW tasks and COMPLIANCE NOW tasks (which do not depend on Phase 2 commercial outputs) and METRICS / FINANCE / ROADMAP NOW tasks hold until #1–#3 clear.

---

## 4. Exit criteria

Phase 3 is *complete* when **all five** are true:

1. **OPERATIONS** — Operating cadence document signed (daily / weekly / monthly / quarterly rhythm). Engine release runbook live. Vendor swap drill executed once per P1 vendor (CCXT, CoinGlass, Tradefeeds, CoinGecko, Claude). Incident-review template signed. Founder-unavailable protocol signed and dry-run executed. Tooling sync discipline codified with drift-detector active. Documented in `_phase-3/01-operations.md`.
2. **METRICS** — §13 weekly internal report template live and run for ≥4 consecutive weeks. Monthly stakeholder report template live and run once. OKR quarterly review SOP signed. §13 conditional-escalation red-line monitor active (alert wired). Anti-overclaim audit run on every public metric surface. Documented in `_phase-3/02-metrics.md`.
3. **FINANCE** — Monthly close SOP signed and executed once. Vendor cost reconciliation SOP live (per-vendor monthly). Stripe revenue reconciliation SOP live. Cash runway dashboard live. §11 model-vs-actuals variance review run once at P3 mid-point. P0 cohort exit memo financial inputs landed into §11 v1.1. Documented in `_phase-3/03-finance.md`.
4. **ROADMAP** — Phase-gate readiness review SOP signed; P2→P3 review executed; P3→P4 review scheduled. §5 capability flow tracker live (monthly cadence). Public roadmap surface (status-page index + roadmap teaser) live and anti-overclaim audited. §14 launch comms plan execution surface live (audience × channel × phase). Documented in `_phase-3/04-roadmap.md`.
5. **COMPLIANCE** — §12 risk register monthly review SOP signed; first review executed. §16 contingency drill executed once for each of the three protocols (regulatory shock, vendor outage, founder unavailable). Regulatory-news monitor runbook signed. US-resident geo-fence integrity audit run once. AED-display footer-text audit run once. CoinGlass quarterly review executed. Counsel engagement cadence signed and first quarterly check-in executed. Documented in `_phase-3/05-compliance.md`.

Plus: Phase 3 backlog (`06-task-backlog.md` when added) has every NOW task either Done or moved to Phase 3.5 / Phase 4 backlog with reason.

---

## 5. Phase 3 risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Operating-cadence drift in absence of formal pressure | Solo founder + 1–2 contractors at P4 — without codified cadence, weekly review collapses into ad-hoc work and §13 / §14 / §12 review loops silently lapse. The discipline is the moat. | Cadence calendar with hard-blocked recurring slots; one cadence event lapses → log to `_decisions/decision-log.md` with reason; two consecutive lapses → cadence redesign |
| Metric drift to vanity (post-public-launch) | At P3 stabilization users + revenue exist, and the temptation to substitute MAU / signup count / Twitter reach for the locked north-star (MAVT + VCSE) compounds quickly. Vanity metrics misroute capital and break §15 due diligence. | §13 v1 north-star binding; weekly internal report template enforces MAVT primacy; monthly anti-overclaim audit catches drift on public surfaces |
| Phase-3 financial close becomes a §11 v1.1 rebuild | A clean close discovers that v1 model assumptions (per-seat density, Stripe blended fee, vendor cost mid-points) are off — the temptation is to refactor §11 mid-flight. Phase 3 is *operate*, not rebuild; Phase 4 absorbs structural model work. | §11 v1 model-vs-actuals variance review is a *delta document*, not a §11 v1.2; structural changes hold for Phase 4 unless §16 Contingency A or §14 stop-the-line fires |
| Phase-gate review becomes a rubber stamp | If the founder owns build, sell, support, *and* the gate review, the gate review is the cheapest meeting to deprioritize — and the most expensive to skip (cohort drawdown, persona invalidation, etc. travel through it). | Gate-review SOP is a checklist, not a meeting; signed entry in `_decisions/decision-log.md` is the artifact; one skipped review fires `[OPS] OPERATIONS — Cadence Audit` |
| Compliance posture decays under load | At P3 stabilization the regulatory and vendor environment has six months more drift since §12 v1; the founder under shipping load forgets the monitoring loop and an `Active` risk drifts to `Triggered` without escalation | §12 v1 monthly review SOP is hard-cadence; status transitions logged; counsel quarterly check-in is calendar-locked |
| Vendor swap drill never executed because nothing's broken | Drills atrophy when the system is stable; the first time we *need* to swap is not when we should *learn* to swap. CoinGlass and Tradefeeds carry the highest swap risk per §12 R-007 / R-010 | One drill per P1 vendor scheduled in Phase 3 OPS calendar; drill outcome logged regardless of result; failed drill → `[BUILD] OPERATIONS — Vendor Swap Hardening` |
| Public roadmap drifts to overclaim | Public roadmap is a marketing surface; pressure to commit to a date / a feature precision that engineering can't honor is constant. Per §6.10 Flag 2 + Phase 1 anti-claim list: stabilizing-status visibility is non-negotiable | Public roadmap shows § stabilizing / VTN / IB tags with hover-explanations; anti-overclaim audit pre-publish; copy review through §9 messaging matrix |
| Founder-unavailable dry-run never run | Solo founder + critical-path posture means founder-unavailable is the highest-impact §16 contingency (Cont. C). Untested protocols fail when invoked | One dry-run executed in Phase 3; outcome logged; gaps fixed within 2 weeks of dry-run |
| Phase 3 scope creep into Phase 4 fundraising work | Cash runway dashboard and §11 variance review will surface cap-table / runway / raise questions; absorbing them blows Phase 3 timing | Phase 3 charter §2 out-of-scope is the contract; runway dashboard is operational instrument; raise narrative is Phase 4 |

---

## 6. Concrete outputs

| Output | File | Format | Status |
|---|---|---|---|
| Phase 3 charter (this doc) | `00-phase-3-charter.md` | MD | DONE |
| OPERATIONS scaffold | `01-operations.md` | MD | DONE |
| METRICS scaffold | `02-metrics.md` | MD | DONE |
| FINANCE scaffold | `03-finance.md` | MD | DONE |
| ROADMAP scaffold | `04-roadmap.md` | MD | DONE |
| COMPLIANCE scaffold | `05-compliance.md` | MD | DONE |
| Phase 3 task backlog | `06-task-backlog.md` | MD | NEXT |
| Phase 3 deliverable map | `07-deliverable-map.md` | MD | NEXT |
| Phase 3 decision register | `08-decision-register.md` | MD | NEXT |
| Phase 3 open questions | `09-open-questions.md` | MD | NEXT |

---

## 7. Workstream → v1 framework crosswalk

| Phase 3 workstream | Authoritative v1 file(s) | Phase 3 layer adds |
|---|---|---|
| OPERATIONS | `10-operations-support.md`, `_data/operations/Production_Candidate_Criteria_v2.md`, `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`, `_data/operations/OPS_Linear_Tickets_v1.md`, project memory `coinscopeai-platform-sync` | Operating cadence (D/W/M/Q); engine release runbook; vendor swap drill; incident-review template; founder-unavailable protocol; tooling sync discipline + drift-detector cadence |
| METRICS | `13-kpi-okr.md` (v1 north-star MAVT + VCSE; 5-layer tree; OKR Q1; risk KPIs paired with §14 stop-the-line), Phase 2 `05-gtm.md` (funnel instrumentation) | Weekly internal report template; monthly stakeholder report template; OKR quarterly SOP; §13 red-line alert wiring; anti-overclaim audit on every public metric surface |
| FINANCE | `11-financial-model.md` (v1 assumptions + sensitivity), `06-pricing-monetization.md` (revenue inputs), `10-operations-support.md` §10.3 (vendor stack costs), Phase 2 `02-pricing.md` (Stripe + dunning) | Monthly close SOP; vendor cost reconciliation; Stripe revenue reconciliation; cash runway dashboard; §11 model-vs-actuals variance; P0 cohort exit memo financial inputs |
| ROADMAP | `14-launch-roadmap.md` (v1 phase progression + stop-the-line), `05-product-strategy.md` §5.4 phase map + §5.4.4 phase-gate triggers, §13.3 OKR feeds | Phase-gate readiness SOP; §5 capability flow tracker; public roadmap surface (status-page index); §14 launch comms plan execution surface |
| COMPLIANCE | `12-risk-compliance-trust.md` (v1 41-entry register), `16-scenario-planning.md` (contingency protocols A/B/C), `_data/legal/Counsel_Brief_v2.md`, `_data/legal/Risk_Disclosure_v0_DRAFT.md`, `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` | §12 monthly review SOP; §16 contingency drill cadence; regulatory-news monitor runbook; US-resident geo-fence audit; AED display audit; CoinGlass quarterly review; counsel engagement cadence |

---

## 8. Decisions deferred *out* of Phase 3 (deliberate)

These are real decisions but belong to Phase 3.5+ or Phase 4. Recording them so they don't leak in:

- **Channel-mix selection** — founder-led vs content vs partnerships vs paid. Inherited from Phase 2 charter §8 deferral. **Phase 3.5** (lightweight scoping pass) **or Phase 4** (full activation).
- **Content calendar / publishing cadence.** Inherited from Phase 2 charter §8. **Phase 3.5** (cadence) **or Phase 4** (publishing).
- **Fundraising narrative + bootstrap-vs-venture posture.** **Phase 4.**
- **§11 financial-model build-out (xlsx + projections refresh).** Phase 3 *operates* §11 v1; Phase 4 builds the raise-grade model.
- **Compliance counsel engagement *outcome* (entity restructure / license filing).** Phase 3 sets the cadence; Phase 4 acts on the advisory output.
- **License filings.** Driven by §16 Contingency A trigger or Phase 4 raise-prep, whichever comes first. Not Phase 3.
- **Bybit and other venues integration.** P2 design-only; Phase 3 ops cover the stack-as-shipped.
- **Layla Phase-5 Desk Full v2 surface** — Phase 5; Phase 3 produces concept-only ops note.
- **High-touch white-glove ops** — Phase 5; concept only at Phase 3.
- **API / data-product ops surface** — Phase 3 concept only; Phase 4+ activation.
- **Sales pipeline / Desk Full enterprise-buyer ops** — Phase 5.

---

## 9. How to read Phase 3 docs

- Each workstream scaffold (`01–05`) follows the same eight-block structure: purpose → why for CSAI → required subsections → recommended artifacts → assumptions → decisions → failure modes → tasks.
- `06-task-backlog.md` (when added) is the **execution surface**. Tasks named `[TYPE] [AREA] — Action / Deliverable`. Grouped by area, ordered NOW / NEXT / LATER.
- `07-deliverable-map.md` rows include explicit Phase 1 / Phase 2 dependency where applicable.
- `08-decision-register.md` lists only the decisions that block Phase 3 exit (Op-* for OPERATIONS, M-* for METRICS, F-* for FINANCE, R-* for ROADMAP, C-* for COMPLIANCE).
- `09-open-questions.md` lists only the questions whose answers Phase 3 needs.

---

## 10. Phase 3 → Phase 4 handoff

Phase 3 produces these as inputs Phase 4 consumes:

- **§11 model-vs-actuals variance report** (quarterly cadence) — Phase 4 consumes one full quarter of variance to refit the raise-grade model.
- **P0 cohort exit memo financial inputs** landed into §11 v1.1 — Phase 4 model build inherits.
- **Cash runway dashboard live** — Phase 4 raise narrative quotes against actuals, not assumption.
- **§13 monthly stakeholder report run ≥3 times** — Phase 4 investor narrative inherits the format.
- **§12 risk register at v1.1** (post-monthly-review status transitions) — Phase 4 due-diligence pack inherits.
- **§16 contingency drills executed (3 protocols)** — Phase 4 due diligence cites operational evidence, not policy.
- **§14 phase-gate review SOP run for P2→P3 and P3→P4** — Phase 4 raise narrative anchors to phase-gate evidence, not phase-map calendar.
- **Counsel engagement first quarterly check-in done** — Phase 4 license / entity work has a relationship to draw on.
- **Anti-overclaim audit clean across public metric surfaces + public roadmap** — Phase 4 due diligence inherits same audit discipline.

If any of these is missing at Phase 3 exit, Phase 4 cannot open with a credible raise narrative.
