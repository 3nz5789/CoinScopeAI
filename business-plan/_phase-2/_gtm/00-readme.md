# GTM — Workstream Index

**Phase:** 2 — Monetization
**Status:** All five NOW deliverables drafted at v0.1. Workstream-NOW complete pending decisions G-1 through G-7. **Channel-mix lock remains deferred to Phase 3 per Phase 2 charter §2 + §8** — Phase 2 GTM commits to *posture* and *anti-channels*, not channel mix.
**Closed:** 2026-05-05

---

## Files

| # | File | Type | Status | Feeds decision |
|---|---|---|---|---|
| 0 | `00-readme.md` | Index | DONE | — |
| 1 | `01-go-to-market-strategy-v1.md` | DOC NOW | DRAFT v0.1 | **G-1**, **G-6** |
| 2 | `02-initial-channel-strategy.md` | DOC NOW | DRAFT v0.1 | **G-1**, **G-5** |
| 3 | `03-founder-led-distribution-plan.md` | DOC NOW | DRAFT v0.1 | **G-3** |
| 4 | `04-launch-sequencing-framework.md` | DOC NOW | DRAFT v0.1 | (sequencing canon) |
| 5 | `05-lowest-risk-demand-channels.md` | RESEARCH NOW | DRAFT v0.1 | **G-5** |

---

## NEXT (queued, not started)

- `[DOC] GTM — Trust-First Launch Campaign Plan`
- `[DOC] GTM — Waitlist and Early Access Motion` → **G-2**
- `[DOC] GTM — Funnel Structure from Content to Demo to Paid`
- `[METRICS] GTM — Acquisition KPI Dashboard Definition` · Cowork artifact target
- `[QA] GTM — Messaging Risk Review for Public Claims` → **G-4**

## LATER (queued, not started)

- `[DOC] GTM — Scalable Growth Engine Hypotheses` · Phase 3+/4+ input
- `[DOC] GTM — International GTM Expansion Notes` → **G-7** · Phase 5+ input

---

## Decisions surfaced (consolidated)

| ID | Decision | Recommendation | Locks at |
|---|---|---|---|
| **G-1** | Phase 2 GTM commitment posture | **Founder-led + organic + content-light; defer paid + community to Phase 3** | Before P1 Narrow Ship public launch |
| **G-2** | Pre-launch waitlist motion | TBD — recommend public waitlist with cohort comms | Before P0 → P1 transition |
| **G-3** | Founder writing cadence at P1 | **Weekly long-form (1 piece/week, methodology / case-study / process notes)** | Before P1 Narrow Ship public launch |
| **G-4** | Public claims register | **Single canonical register of allowed claims with PCC v2 §8 cross-references** | Before any public claim ships |
| **G-5** | Anti-channel explicit list | **Publish internal anti-channel list with reasoning** | Before Phase 3 channel-mix decision |
| **G-6** | Methodology / docs as demand surface | **Treat methodology + docs as primary demand surface** (Karim + Layla) | Before P1 launch |
| **G-7** | International expansion at v1 | **UAE/MENA + global EN audience, no specific localization** | Phase 2 close |

---

## Open questions surfaced (consolidated)

1. **GQ-1** — Does founder-led + organic recruit 100–200 paid customers in P1 Narrow Ship 8-week window without paid acquisition? (`01-go-to-market-strategy-v1.md` §9 falsifier — Phase 3 decision accelerator if no.)
2. **GQ-2** — Methodology page → signup conversion ≥1% for Karim + Layla cohorts? (Falsifier for G-6.)
3. **GQ-3** — Founder time on GTM stays at 5–10 hrs/week steady-state? (`03-founder-led-distribution-plan.md` §9 KPI; >12 hrs sustained = §9 falsifier.)
4. **GQ-4** — Direct outreach response rate ≥20% to Karim / Layla profiles? (Targeting / message-form validity.)
5. **GQ-5** — Founder-cohort window uptake ≥40% in 60-day window? (Per `_pricing/01` revision trigger #4.)
6. **GQ-6** — Validation cohort retention ≥70% through P0 → P1 transition? (P0 → P1 exit criterion #4.)
7. **GQ-7** — Persona-fit segmentation in cohort: ≤50% casual-retail mix? (Anti-ICP filter validation.)
8. **GQ-8** — Long-form publishing cadence: 8 pieces in 8-week P1 window? (G-3 KPI.)
9. **GQ-9** — Phase 3 channel-mix evaluation criteria framework finalized by P1 close? (Phase 3 charter readiness.)
10. **GQ-10** — Phase 5 DF v2 launch capacity reserved through P1/P2 sequencing? (`04-launch-sequencing-framework.md` §7 cross-phase compatibility.)

---

## REQUIRED INPUT items (consolidated)

| Item | Source | Affects |
|---|---|---|
| Founder time-cost basis (for CAC modeling) | Founder + FinOps | `01-go-to-market-strategy-v1.md` §8 |
| Methodology-page → signup conversion instrumentation | Eng / product analytics | `01` §9 G-6 falsifier; `03` §9 KPI |
| Direct-outreach tracking method (Notion or similar) | Founder | `03-founder-led-distribution-plan.md` §5 + §9 |
| Founder-cohort window start date (anchored to P1 public launch day) | Founder | `04-launch-sequencing-framework.md` P1 entry; PRICING `_pricing/03` §7 |
| Phase 1 BRAND patternbook — final form | Phase 1 charter | `03` §8 voice register guards; cross-doc consistency |
| Phase 1 POSITIONING anti-claim list — final form | Phase 1 charter | `01` §4; `Messaging Risk Review` (NEXT QA) |
| Phase 1 ICP `Persona Fit Scoring Model` — final form | Phase 1 charter | KPI persona-fit segmentation; direct-outreach targeting |
| Validation Phase Exit Memo — actual completion at P0 close | Founder + Strategy CoS | All P0 → P1 exit criteria |
| Engine-side instrumentation: methodology-page traffic + funnel events | Eng | KPI dashboard data model (NEXT) |
| Stripe + entitlement webhook latency baseline | Eng | Funnel structure (NEXT) conversion-event timing |

---

## Anti-overclaim audit roll-up

Every NOW draft was authored against the §6.10 anti-overclaim flags + Scoopy custom instructions canonical phrasings:

- **Validation disclaimer** ("Testnet only · 30-day validation phase · No real capital.") — surfaced in `01` §4 trust commitments table; `03` §6 cohort comms; `04` §3 P0 GTM beat; `05` §3.6 trust amplifier.
- **PCC v2 §8 reference** — surfaced in `01` §4 + §5; `04` §3 P0 entry; canonical-claim register (G-4 NEXT) inherits.
- **Founder-cohort canonical phrasing** — `03` §6 + `04` §4. Inherited from `_pricing/03` §6.
- **"v2" / "v3" qualifiers on roadmap features** — `03` §10 (anti-pattern guard); `04` §6 P5 anti-actions.
- **Anti-channel register** — `02` §4 + `05` §7 maximum-risk register; G-5 publishes internally.
- **"Trade Smarter With AI" tagline usage** — `03` §8 explicit register: marketing-tier surfaces only, never product-tier.
- **No "Most popular" / urgency mechanics** — `01` §5 explicit decline; cross-references `_packaging/05` design rule 4 + `_pricing/02` Principle 5.
- **No paid acquisition at v1** — `01` §5 + `02` §2 + `04` §4 + `05` §5.1 explicit decline; Phase 3 deferral consistent across docs.
- **No co-marketing with anti-ICP** — `01` §5 + `02` §4 + `05` §5.5 explicit decline.

No new overclaim risks introduced. GTM contributes a clean baseline pending NEXT-phase `Messaging Risk Review for Public Claims` audit.

---

## Cross-workstream linkages

GTM produces inputs consumed by + depends on inputs from:

| Direction | Workstream | What | Where |
|---|---|---|---|
| GTM ← PACKAGING | `_packaging/03-plan-comparison-table-v1.md` | Pricing-page surface (gate 0 of funnel) | `01` §3; `04` P1 GTM beat |
| GTM ← PACKAGING | `_packaging/05-packaging-friction-review.md` | Class F anti-channel reasoning + design rules | `01` §5; `02` §5; `05` §5 |
| GTM ← PRICING | `_pricing/02-initial-pricing-philosophy.md` | Anti-pressure principles (4–7) inherited | `01` §5; `02` §6; `03` §10; `05` §1 |
| GTM ← PRICING | `_pricing/03-monthly-vs-annual-offer-structure.md` §6–§7 | Founder-cohort window mechanics + canonical phrasing | `01` §6; `03` §6; `04` §4 P1 GTM beat |
| GTM ← PRICING | `_pricing/04-trial-and-intro-offer-options.md` | Pr2-3 no-free-trial (constrains GTM offer space) | `01` §5; `03` §10 anti-pattern guard |
| GTM ← PRICING | `_pricing/05-price-to-margin-sensitivity-model.md` §7 | LTV/CAC tolerance per tier (CAC ceilings for Phase 3 channel-mix) | `01` §8 |
| GTM ← ONBOARDING | `_onboarding/01-first-time-user-journey.md` | 6-gate funnel structure (gate 0 → gate 5 = GTM scope) | `01` §3; `Funnel Structure` (NEXT) |
| GTM ← ONBOARDING | `_onboarding/02-activation-milestones-definition.md` | Activation funnel KPIs as GTM tracking metrics | `Acquisition KPI Dashboard` (NEXT) |
| GTM ← SUPPORT | `_support/01-support-operating-model.md` §3 | Founder time budget ceiling (GTM ≤ 10 hrs/week) | `03-founder-led-distribution-plan.md` §2 |
| GTM ← SUPPORT | `_support/05-support-inbox-and-response-workflow.md` §7 | Canonical responses inform canonical-claim register | G-4 (NEXT) inherits |
| GTM → §13 KPI | Per-phase KPI targets per `04-launch-sequencing-framework.md` §8 | KPI framework inputs | Phase 4 |
| GTM → §11 financial model | CAC tolerance + organic-recruit feasibility | §11 unit economics inputs | Phase 4 |
| GTM → §15 fundraising narrative | Trust-first GTM thesis + anti-channel discipline + organic-recruit story | Phase 4 fundraising deck | Phase 4 |
| GTM → Phase 3 charter | CANDIDATE-P3 channel set + 5 evaluation criteria + sequencing P2 → P3 entry | Phase 3 GTM scope | Phase 3 |
| GTM → Phase 5 charter | DF v2 launch capacity reservation + Layla-aligned channel posture | Phase 5 GTM scope | Phase 5 |

---

## Linkage to Phase 2 charter exit criteria

Phase 2 charter §4 requires (GTM row):

> **GTM** — Pricing page v1 spec; founder-cohort recruiting pack; beta-cohort conversion offer; anti-overclaim audit on every monetization surface; one-pager for the Narrow Ship offer. **No channel selection.** Documented in `_phase-2/05-gtm.md`.

Status against exit criteria:

- ✓ Pricing page v1 spec — owned by PACKAGING `_packaging/03-plan-comparison-table-v1.md`; GTM consumes as gate 0.
- ⏳ Founder-cohort recruiting pack — `Trust-First Launch Campaign Plan` (NEXT) + `Waitlist and Early Access Motion` (NEXT) deliver this.
- ⏳ Beta-cohort conversion offer — owned by PACKAGING `[DOC] PACKAGING — Beta Access Offer Design` (NEXT); GTM coordinates.
- ⏳ Anti-overclaim audit on every monetization surface — `Messaging Risk Review for Public Claims` (NEXT QA, G-4) delivers this; GTM workstream contributes the canonical-claim register.
- ⏳ Narrow Ship one-pager — derivable from `01-go-to-market-strategy-v1.md` + `04-launch-sequencing-framework.md`; produced as part of `Trust-First Launch Campaign Plan` (NEXT).
- ✓ No channel selection — GTM Phase 2 docs commit to *posture* (`01` §6, `02` §3) and *anti-channels* (`02` §4, `05` §7), explicitly defer channel-mix lock to Phase 3 (`01` §7, `04` §6).

GTM workstream NOW work is **draft-complete**. Lock requires the seven **G-*** decisions + REQUIRED INPUT items + execution of Phase 2 NEXT items (especially `Trust-First Launch Campaign Plan` + `Waitlist and Early Access Motion` + `Messaging Risk Review for Public Claims` before P1 Narrow Ship public launch).

---

## Phase 2 → Phase 3 handoff

GTM contributes the following to the Phase 2 → Phase 3 handoff (per Phase 2 charter §10):

- ✓ Pricing page v1 (live surface) — Phase 3 distributes traffic to it.
- ⏳ Founder-cohort offer fully operationalized — pending NEXT phase delivery.
- ⏳ Conversion-event instrumentation (signup → first-signal → first-gate-decision → first-billing) — pending `Funnel Structure` NEXT delivery + ONBOARDING `_onboarding/05` REQUIRED INPUT items.
- ✓ Anti-channel register canonical (`02` §4, `05` §7) — Phase 3 channel-mix decision inherits.
- ✓ CANDIDATE-P3 channel set (`02` §6) — Phase 3 channel-mix evaluation queue ready.
- ✓ 5 channel evaluation criteria (`02` §6) — Phase 3 acceptance criteria framework ready.
- ✓ LTV/CAC tolerance per tier (`01` §8) — Phase 3 per-channel acceptance criteria input ready.
- ⏳ Anti-overclaim audit clean across every monetization surface — pending `Messaging Risk Review for Public Claims` NEXT delivery.

Phase 3 cannot open without all ⏳ items cleared.

---

## Phase 2 GTM workstream sealed

PACKAGING / PRICING / ONBOARDING / SUPPORT / GTM — all five Phase 2 workstreams are now NOW-complete at draft v0.1. Phase 2 lock requires:

1. All five workstreams' decisions locked (Pk-* / Pr2-* / On-* / Su-* / G-* — total 35 decisions).
2. All five workstreams' REQUIRED INPUT items cleared.
3. Phase 2 NEXT-tier deliverables delivered (Help Center, Templates, Billing Playbook, Connectivity Playbook, KPI Dashboards across workstreams; Trust-First Launch Campaign Plan; Waitlist Motion; Funnel Structure; Messaging Risk Review).
4. P0 cohort exit memo signed (triggers Pk-1, Pr2-1, On-* lock confirmation).
5. P1 Narrow Ship public launch executed.

Phase 3 charter opens at P2 close (Aug-Sep 2026 window) per `04-launch-sequencing-framework.md` §5.
