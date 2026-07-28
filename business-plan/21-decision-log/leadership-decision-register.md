# Leadership Decision Register

## How to read this register

- **Append-only.** A `DECIDED` row, once revised, becomes `SUPERSEDED`; a new row is added.
- **Status taxonomy (strict — no bespoke values):** `OPEN` / `IN REVIEW` / `DECIDED` / `DEFERRED` / `SUPERSEDED`. A status grade may be appended (`OPEN — High`) but the base value must be one of the five.
- **Owner column:** role labels per `17-team-and-operating-model/decision-rights.md`. Most rows are `Founder`; some are `Founder + counsel` where decision-rights.md mandates counsel involvement.
- **Deadline format:** absolute date (`YYYY-MM-DD`) OR `Trigger: <event>`. No relative descriptions.
- **Blocked by:** upstream decision ID or trigger that must clear before this decision can be made. `—` if not blocked.
- **Cross-ref format:** `<folder>/<file>.md` or `<folder>/<file>.md §X` for section anchors.

Today's date for deadline anchoring: **2026-05-08**.

## Section index

- **A.** Strategic identity (locked) — 7 rows
- **B.** Pricing and packaging — 5 rows
- **C.** Trust, claims, and safeguards — 9 rows
- **D.** Onboarding and activation — 3 rows
- **E.** GTM — 5 rows
- **F.** Financial assumption decisions — 5 rows
- **G.** Hiring and team — 7 rows
- **H.** Roadmap and gating — 5 rows
- **I.** Decision-system meta-decisions — 5 rows
- Status summary, urgent watchlist, cross-references, version history below.

---

## A. Strategic identity (largely locked, listed for visibility)

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| A-01 | Primary ICP | Drives every persona-tied surface | (a) Solo Methodist (Omar), (b) Engineer Trader (Karim), (c) Solo PM (Layla) | (a) Omar primary; Karim secondary; Layla deferred to P5 | Founder | 2026-05-01 (locked) | — | All persona-driven surfaces | DECIDED | `04-icp-and-segmentation/` |
| A-02 | Category / positioning | Anchors price defensibility and trust framing | (a) AI trading intelligence, (b) Automated futures system, (c) Trader OS, (d) Institutional-grade quant trading for individuals + funds | (d) — locked | Founder | 2026-05-01 (locked) | — | Brand voice, all messaging | DECIDED | `05-positioning/` |
| A-03 | Tier matrix (Track B canonical) | Drives revenue model + sequencing | Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + per-seat | Locked Track B | Founder | 2026-05-01 (locked) | — | Pricing, GTM, financial framework | DECIDED | `07-packaging-and-pricing/` |
| A-04 | Phase map | Drives every roadmap and KPI activation | P0 May 2026 → P1 Jun-Jul → P2 Aug-Sep → P5 Mar-May 2027 | Locked phase map | Founder | 2026-05-01 (locked) | — | Roadmap, KPI activation, hiring | DECIDED | `06-product-strategy/` |
| A-05 | Risk thresholds | Capital-preservation backbone | 10x leverage / 10% MDD / 5% daily / 3 max positions / 80% heat | Locked via PCC v2 §8 Capital Cap | Founder | 2026-05-01 (locked) | — | Engine config, all monetization tiers | DECIDED | `14-risk-compliance-and-safeguards/` |
| A-06 | Jurisdictional posture | Drives signup gating + compliance scope | UAE founder, sole prop, target UAE/MENA + global EN, US blocked at signup | Locked posture | Founder + counsel | 2026-05-01 (locked) | — | Auth flow, compliance, GTM | DECIDED | `02-company-overview/` |
| A-07 | NSM definition | Single number to be judged by | (a) MRR, (b) WAU, (c) Activated Paying, (d) TRAS, (e) VCE for P0 only | (e) VCE during P0; (d) TRAS from P1 narrow ship — operationally adopted in `kpi-map.md` §0a | Founder | 2026-05-01 (locked); confirmation note at P1 narrow ship | — | Weekly + monthly reviews | DECIDED | `16-kpi-okr-system/kpi-map.md` §0a, `16-kpi-okr-system/north-star-metric.md` |

---

## B. Pricing and packaging decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| B-01 | Annual prepay policy timing | Cash vs refund-wave exposure | (a) At P1 narrow ship, (b) At P2, (c) At PCC v2 G4 + 60 days stable | (c) — refund exposure too high earlier | Founder | 2026-07-31 | PCC v2 G4 stability data | Stripe config, GTM messaging, revenue model | OPEN — High | `15-financial-framework/financial-assumptions.md` Row 4 |
| B-02 | Desk Full v2 per-seat rate | Anchors fund-tier economics | (a) $149/seat, (b) $249/seat | Lean (b) for institutional posture; lock pending fund-tier conversation input | Founder | 2026-12-31 | First fund-tier conversations | Desk Full v2 SKU launch | OPEN | `15-financial-framework/financial-assumptions.md` Row 3, `07-packaging-and-pricing/` |
| B-03 | Discount policy posture | Defensibility of tier ladder | (a) No discounts pre-P2, (b) Founder-discretion case-by-case, (c) Published rules at P1 | (a) — protect tier defensibility | Founder | 2026-06-30 | — | Pricing integrity, refund playbook | OPEN — High | `17-team-and-operating-model/decision-rights.md` §4 |
| B-04 | Trial model | Filters for serious users vs broadens funnel | (a) Free tier as trial, (b) Time-boxed paid trial, (c) Both | (a) — Free is trust-builder, time-boxed creates churn pressure | Founder | 2026-06-30 | — | Onboarding flow, conversion path | OPEN | `15-financial-framework/financial-assumptions.md` Row 28, `12-onboarding-and-activation/` |
| B-05 | Regional pricing variants | MENA purchasing power vs global EN | (a) Single global price, (b) MENA discount, (c) Defer to P3+ | (c) — defer; not enough data to price regionally | Founder | Trigger: P3 entry | — | Pricing structure | DEFERRED | `15-financial-framework/financial-assumptions.md` Row 5 |

---

## C. Trust, claims, and safeguards

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | Real-capital authorization default | Single most consequential decision in the framework | (a) Default NO until §8 fully met, (b) Default YES with caveats | (a) — default NO; non-delegable; criteria-driven only | Founder | Locked default; review at every monthly exec | — | All monetization, all marketing claims, all roadmap | DECIDED | `14-risk-compliance-and-safeguards/`, `17-team-and-operating-model/decision-rights.md` §8 |
| C-02 | Public-facing transparency artifact (validation cohort summary) | Trust signal vs disclosure risk | (a) Publish at P1, (b) Publish at P2, (c) Defer indefinitely | Lean (b) once P1 cohort is large enough to anonymize | Founder | 2026-08-31 | M3 stabilization | Brand trust, content strategy | OPEN | `13-support-and-trust-ops/`, `18-roadmap/` |
| C-03 | Public claims about engine performance | Regulatory + reputational tail | (a) Allow with disclaimer, (b) Forbid in public marketing, (c) Allow only in private fund-tier conversations | (b) — forbid in public marketing; revisit at P5 with counsel | Founder | Locked posture | — | Brand voice, content guardrails | DECIDED | `13-support-and-trust-ops/`, `17-team-and-operating-model/decision-rights.md` §6 |
| C-04 | Disclosure language consistency check (approach) | Surface drift = trust drift | (a) Manual quarterly audit, (b) Embedded into deploy checklist, (c) Both | (c) — both — locked. Activation date for the deploy-checklist embed is in `99-task-backlog/master-backlog.md` (NOW task) | Founder | Approach locked; activation 2026-06-15 | — | Every public surface | DECIDED (approach); execution task tracked separately | `18-roadmap/`, `17-team-and-operating-model/decision-rights.md` §6 |
| C-05 | Refund/credit playbook publication (internal) | Trust Ops scope; refund consistency | Author + publish v1 with explicit thresholds (1 month tier value; Desk Full v2 always escalates) | Author by 2026-06-07 | Founder | 2026-06-07 | — | Trust Ops activation, Stripe behavior | OPEN — High | `17-team-and-operating-model/decision-rights.md` §7 |
| C-06 | Incident comms stand-in (phased decision) | Founder unavailability risk | (a) Advisor, (b) Trusted contact, (c) Trust Ops contractor, (d) None | **Phased:** Phase 1 = (b) Trusted contact identified by 2026-06-30; Phase 2 = (c) Trust Ops contractor at P2 activation; transition trigger = G-01 closure | Founder | Phase 1: 2026-06-30; Phase 2: Trigger G-01 closure | — | Incident posture, bus-factor | OPEN — High | `13-support-and-trust-ops/`, `17-team-and-operating-model/decision-rights.md` §10 |
| C-07 | Security incident response posture | Different escalation than operational incidents; legal exposure | Posture defined: containment in-band; Founder + counsel notified within 1 hour; no public/customer comms until concur; postmortem within 7 days | Posture locked per decision-rights.md §10A | Founder + counsel | Locked posture | — | Incident escalation, regulatory disclosure timing | DECIDED | `17-team-and-operating-model/decision-rights.md` §10A |
| C-08 | Compliance posture changes (jurisdictional) | Material regulatory exposure | All changes require counsel involvement; never delegated | Locked: Founder + counsel for all jurisdictional changes | Founder + counsel | Locked posture; review at every phase transition | — | Auth flow, compliance scope, US-blocked enforcement | DECIDED | `02-company-overview/`, `17-team-and-operating-model/decision-rights.md` §2 row 32 |
| C-09 | Engine rollback authority (with carve-out) | Operational vs capital-preservation tradeoff | (a) Founder always; (b) Founder normally with engineering carve-out during incident | (b) — Founder normally; engineering may roll back to last known-good during active incident if capital-preservation risk AND founder unreachable. Forward deploys NOT permitted under same conditions | Founder | Locked posture | — | Incident response; deploy authority | DECIDED | `17-team-and-operating-model/decision-rights.md` §8 |

---

## D. Onboarding and activation decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | Activation definition lock | KPI calibration + cohort definitions | Define exact step-set that counts as "activated" | Lock current proposed definition | Founder | 2026-06-07 | — | KPI map, weekly review, NSM, Free → Trader conversion measurement | OPEN — High | `12-onboarding-and-activation/`, `16-kpi-okr-system/kpi-map.md` §2 |
| D-02 | Onboarding flow first-iteration trigger | When to revisit | (a) D7 retention <60%, (b) D7 retention <50%, (c) Drop-off >20% at any step | (a) + (c) | Founder | 2026-06-07 | D-01 | Activation iteration | OPEN | `12-onboarding-and-activation/` |
| D-03 | Exchange-connection gating | Block users without exchange creds vs allow Free without | (a) Require exchange connection, (b) Allow Free without, gate Trader on connection | (b) | Founder | 2026-06-07 | D-01 (partial) | Free-tier UX, conversion path | OPEN | `12-onboarding-and-activation/` |

---

## E. GTM decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| E-01 | Founder content cadence | Only acquisition channel pre-P3 | (a) 1 piece/week, (b) 2 pieces/week, (c) Variable | (b) at P1 entry; flex to (a) under load | Founder | Trigger: P1 narrow ship | H-01 | GTM motion, founder time allocation | OPEN | `08-go-to-market/` |
| E-02 | Paid acquisition trigger | Premature paid spend = low-quality cohort. **Forbidden until P3+ at earliest with explicit criteria** | (a) Activate at P3 if cohort retention defensible + refund rate <2% + trust posture publicly defensible, (b) Defer to P5 | (a) with explicit trigger criteria | Founder | Trigger: P3 entry | Cohort defensibility data | Marketing budget, CAC modeling | DEFERRED | `08-go-to-market/`, `17-team-and-operating-model/decision-rights.md` §5 |
| E-03 | MENA-specific channel investment | Founder geographic posture | (a) MENA-first content, (b) global EN-first, (c) parallel | (c) — both, with founder voice unifying | Founder | Trigger: P1 narrow ship | — | Content strategy, distribution | OPEN | `08-go-to-market/` |
| E-04a | Exchange affiliate program | Excluded by jurisdictional posture | (a) Activate, (b) Forbid | (b) — forbidden by jurisdictional posture | Founder | Locked posture | — | GTM motion | DECIDED | `08-go-to-market/`, `15-financial-framework/revenue-model.md` §2 |
| E-04b | User referral incentive program | Tempting but trust-fragile | (a) Activate, (b) Defer | (b) — defer; revisit at P3 | Founder | Trigger: P3 entry | — | GTM motion | DEFERRED | `08-go-to-market/`, `15-financial-framework/revenue-model.md` §2 |

---

## F. Financial assumption decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| F-01 | Founder internal rate (cost recognition) | Honest margin; opportunity-cost framing | (a) $0, (b) $100/hr placeholder, (c) Market rate | (b) — $100/hr placeholder until fundraise/exit forces revision | Founder | 2026-05-31 | — | Cost-structure honesty, role decisions | OPEN | `15-financial-framework/financial-assumptions.md` Row 19 |
| F-02 | Vendor cost / revenue threshold | When to alarm | (a) 25%, (b) 30%, (c) 35% | (a) — 25% target | Founder | 2026-05-31 | — | Vendor management, cost discipline | OPEN | `15-financial-framework/financial-assumptions.md` Row 36 |
| F-03 | Cash runway floor | When to escalate | (a) 6 months, (b) 9 months, (c) 12 months | (b) — 9 months | Founder | 2026-05-01 (locked, operationally adopted) | — | Spend pacing | DECIDED | `15-financial-framework/financial-assumptions.md` Row 31, `15-financial-framework/cost-structure.md` §9 |
| F-04 | Bookkeeping contractor activation | Trigger-based engagement | Contract type: monthly retainer vs project | Monthly low-retainer ($100–500) | Founder | Trigger: first paid Trader | First paid customer (trigger) | Financial discipline, time savings | OPEN | `17-team-and-operating-model/role-priorities.md` Role #2 |
| F-05 | Stripe configuration scope | MENA + global EN edge cases | Currencies, refund flow, tax handling per region | Test all in sandbox before Trader live | Founder | 2026-06-07 | — | Monetization readiness | OPEN — High | `18-roadmap/30-60-90-plan.md` |

---

## G. Hiring and team decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| G-01 | Trust Ops contractor activation | First non-founder hire is the highest-stakes | (a) At P2 entry, (b) At first ticket-volume threshold, (c) After first paid customer + 30 days | (c) — wait for stress, then activate from pre-sourced shortlist | Founder | Trigger: 2026-08-15 expected | Stable engine + first paid customer + trial completion | Trust ops, support, founder time | OPEN | `17-team-and-operating-model/role-priorities.md` |
| G-02 | Trust Ops contractor engagement model | Cash exposure shape | (a) Hourly, (b) Project retainer, (c) Hybrid | (a) hourly initially | Founder | Trigger: G-01 activation | G-01 | Cash exposure | OPEN | `17-team-and-operating-model/role-priorities.md` |
| G-03 | Engineering contractor scoping | Scope drift vs flexibility | (a) Per-project SOWs, (b) Monthly retainer | (a) SOWs only — clean start/end | Founder | Trigger: P2 vendor expansion | P2 entry | Vendor integration cost | OPEN | `17-team-and-operating-model/role-priorities.md` |
| G-04 | Geographic constraints on hiring | Coverage of MENA + global EN business hours | (a) UAE-only, (b) MENA-broad, (c) global | (b) MENA-broad with global EN written-language fluency | Founder | 2026-06-15 (before sourcing closes) | — | Sourcing radius | OPEN | `17-team-and-operating-model/team-design.md` |
| G-05 | Optional advisor activation | Outside perspective vs theatre | (a) Activate now, (b) Activate at P1, (c) Defer | (b) at P1 if right candidate exists | Founder | Trigger: P1 narrow ship | H-01 | Monthly review participation | OPEN | `17-team-and-operating-model/role-priorities.md` |
| G-06 | Equity policy for first FT hire | Compensation framework | (a) No equity, (b) Standard early-stage equity, (c) Discretionary | Establish posture before role activates | Founder | Trigger: pre-P3 | First FT hire candidate identified | First FT hire offer | OPEN | `17-team-and-operating-model/team-design.md` §4 |
| G-07 | Chief of Staff posture | Stage appropriateness | (a) Hire, (b) Defer indefinitely | (b) — wrong stage; revisit only at venture-scale | Founder | Locked | — | Org-design discipline | DECIDED | `17-team-and-operating-model/team-design.md` |

---

## H. Roadmap and gating decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| H-01 | P1 narrow-ship date | Largest decision in 90-day plan | Triggered by: PCC v2 G3 ≥30 days stable | Date emerges from G3 stability — not chosen | Founder | Trigger: PCC v2 G3 30d stable | QA-01 (G3 state) | Trader monetization, NSM transition, all of M2 | OPEN — High | `18-roadmap/30-60-90-plan.md`, `18-roadmap/dependency-map.md` §4 Chain A+B |
| H-02 | P2 vendor expansion sequencing | Bybit vs additional feeds first | (a) Bybit first, (b) Feeds first, (c) Parallel | (a) Bybit first — single-venue dependency is the bigger risk | Founder | 2026-08-31 | M3 stabilization | P2 scope, contractor SOW shape | OPEN | `18-roadmap/`, `binance-bybit-integration-guard` (skill) |
| H-03 | P5 Desk Full v2 launch criteria | Time-locked vs criteria-locked | (a) Calendar Mar–May 2027, (b) Criteria-only | (b) — criteria-only; Mar–May 2027 is *target window*, not commitment | Founder | Locked posture | — | Desk Full v2 launch | DECIDED | `18-roadmap/milestone-framework.md` Milestone M8 |
| H-04 | TRAS knob calibration | NSM credibility | N-sessions threshold + override-rate threshold | Lock at 90-day mark from Trader live | Founder | Trigger: first paid cohort D30 + 30 | H-01, first paid cohort D30 | NSM operating definition | OPEN | `16-kpi-okr-system/north-star-metric.md`, `16-kpi-okr-system/kpi-map.md` §0a |
| H-05 | Forward-only gate transitions | PCC v2 process discipline | (a) Forward-only by default, (b) Allow ad-hoc | (a) — forward-only; backward requires explicit decision-log entry | Founder | Locked | — | Phase progression integrity | DECIDED | `18-roadmap/milestone-framework.md` §7 |

---

## I. Decision-system meta-decisions

| ID | Decision | Why it matters | Options | Recommendation | Owner | Deadline | Blocked by | Downstream impact | Status | Cross-ref |
|---|---|---|---|---|---|---|---|---|---|---|
| I-01 | Decision-log primary home | Avoid drift between markdown and other tools | (a) This folder canonical, (b) Notion canonical, (c) Both, mirrored | (c) — markdown canonical, Notion mirror for visibility (operationally adopted across Wave 3) | Founder | Markdown canonical posture locked; Notion mirror configuration pending | — | Process integrity | DECIDED | `21-decision-log/README.md` |
| I-02 | Per-decision detail page threshold | Richer doc vs scan-friendly | High-impact only get detail pages | High-impact = pricing, claims, risk, hiring | Founder | 2026-05-31 | — | Documentation overhead | OPEN | `21-decision-log/README.md` |
| I-03 | Loggable-decision threshold | Keep register from cluttering | Affects pricing/claims/refunds/hiring/vendor concentration/risk thresholds/roadmap dates → loggable | Working rule confirmed; codified in README | Founder | Locked | — | Register hygiene | DECIDED | `21-decision-log/README.md` |
| I-04 | Decision-log curation governance | Register integrity | Authority over status updates, supersession entries, register hygiene | Founder owns curation; never delegated; auto-logged via the register itself | Founder | Locked posture | — | Register integrity | DECIDED | `17-team-and-operating-model/decision-rights.md` §2 row 34 |
| I-05 | Validation gate rule application authority | Use of unvalidated assumption in load-bearing models | Authority over treating "directional only" assumption as load-bearing | Founder; applies whenever a financial-assumption row in `Status: Not validated` is used in a model | Founder | Locked posture | — | Model honesty; fictional-precision prevention | DECIDED | `15-financial-framework/financial-assumptions.md` Validation Gate Rule, `17-team-and-operating-model/decision-rights.md` §2 row 26 |

---

## Status summary

| Status | Count |
|---|---|
| DECIDED | 22 |
| IN REVIEW | 0 |
| OPEN | 26 |
| DEFERRED | 3 |
| SUPERSEDED | 0 |
| **Total** | **51** |

The 26 OPEN rows are the active risk surface. Sort by deadline ascending to identify the next decision blocker.

---

## Urgent watchlist (OPEN — High, sorted by deadline)

| Deadline | ID | Decision |
|---|---|---|
| 2026-05-31 | F-01 | Founder internal rate (cost recognition) — currently OPEN |
| 2026-05-31 | F-02 | Vendor cost / revenue threshold — currently OPEN |
| 2026-06-07 | C-05 | Refund/credit playbook publication — **OPEN — High** |
| 2026-06-07 | D-01 | Activation definition lock — **OPEN — High** |
| 2026-06-07 | F-05 | Stripe configuration scope — **OPEN — High** |
| 2026-06-15 | C-04 | Disclosure language consistency activation (execution; decision DECIDED) |
| 2026-06-30 | B-03 | Discount policy posture — **OPEN — High** |
| 2026-06-30 | C-06 | Incident comms stand-in (Phase 1) — **OPEN — High** |
| 2026-07-31 | B-01 | Annual prepay policy timing — **OPEN — High** |
| Trigger: PCC v2 G3 30d stable | H-01 | P1 narrow-ship date — **OPEN — High** |

Other OPEN rows (non-High) are tracked but do not require immediate action this month.

---

## Cross-references

| Topic | Where to look |
|---|---|
| Open questions register (upstream of decisions) | `21-decision-log/open-questions-register.md` |
| Decision-log governance (loggable threshold, status taxonomy) | `21-decision-log/README.md` |
| Financial assumptions (F-section ↔ Row mapping) | `15-financial-framework/financial-assumptions.md` |
| KPI map (decisions referenced in `Linked` column) | `16-kpi-okr-system/kpi-map.md` |
| Decision-rights row mapping (each decision ↔ §2 row in decision-rights) | `17-team-and-operating-model/decision-rights.md` |
| Dependency map (§5 decisions-that-unblock; §7 do-not-start list) | `18-roadmap/dependency-map.md` |
| Milestone definitions (M1–M9 referenced in H-section and elsewhere) | `18-roadmap/milestone-framework.md` |
| Operating cadence (review frequencies that surface decisions) | `17-team-and-operating-model/operating-cadence.md` |

---

## Version history

Append-only log of changes to this file. Format: `YYYY-MM-DD — change summary — affected row IDs`.

| Date | Change | Affected IDs |
|---|---|---|
| 2026-05-08 | Initial register published as part of Wave 3 generation | A-01 through I-03 (45 rows) |
| 2026-05-08 | Cleanup pass: recounted status totals (now 22/0/26/3/0); eliminated bespoke status values; split E-04 into E-04a + E-04b; refreshed cross-refs to use post-cleanup row numbers (F-01 → Row 19, F-02 → Row 36, A-07 → kpi-map.md §0a); added 6 new rows (C-07 security incident posture, C-08 compliance posture changes, C-09 engine rollback, I-04 decision-log curation, I-05 validation gate rule); resolved F-03 to DECIDED; reframed I-01 to DECIDED; added Blocked by column; standardized Cross-ref column format; allowed Founder + counsel in Owner column where decision-rights.md mandates it; standardized Deadline format; added Urgent watchlist section; added Cross-references section; added Version history; added section index TOC; reframed C-04 to separate decision (DECIDED) from execution (task); reframed A-07 to DECIDED with confirmation note; codified C-06 as phased decision | All sections affected; new IDs C-07, C-08, C-09, E-04a, E-04b, I-04, I-05 |

---

*Last reviewed: 2026-05-08. Reviewed at every weekly review (status sweep), monthly exec review (full register), and phase transition (re-baseline). Status counts manually refreshed at every monthly exec review to prevent drift.*
