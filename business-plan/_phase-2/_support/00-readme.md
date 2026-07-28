# SUPPORT — Workstream Index

**Phase:** 2 — Monetization
**Status:** All five NOW deliverables drafted at v0.1. Workstream-NOW complete pending decisions Su-1 through Su-8, and REQUIRED INPUT items (current support tooling state, monitoring stack, status page presence).
**Closed:** 2026-05-04

---

## Files

| # | File | Type | Status | Feeds decision |
|---|---|---|---|---|
| 0 | `00-readme.md` | Index | DONE | — |
| 1 | `01-support-operating-model.md` | DOC NOW | DRAFT v0.1 | **Su-1**, **Su-2**, **Su-3**, **Su-8** |
| 2 | `02-support-sla-framework.md` | DOC NOW | DRAFT v0.1 | **Su-4**, locks input to **Pr2-5** |
| 3 | `03-ticket-routing-and-escalation-rules.md` | DOC NOW | DRAFT v0.1 | (consumed by 04 + 05) |
| 4 | `04-user-issue-taxonomy.md` | DOC NOW | DRAFT v0.1 | (consumed by 05 + KB + templates) |
| 5 | `05-support-inbox-and-response-workflow.md` | OPS NOW | DRAFT v0.1 | (operational SOP) |

---

## NEXT (queued, not started)

- `[DOC] SUPPORT — Help Center Structure` · consumes deflection priorities from `04` §4
- `[DOC] SUPPORT — Standard Response Templates` · 10 priority templates per `05` §6
- `[DOC] SUPPORT — Billing Support Playbook` · §6.7 + Pr2-5 + Escalations C/D from `03` + `05`
- `[DOC] SUPPORT — Exchange Connectivity Support Playbook` · per-vendor flows from `Vendor_Failure_Mode_Mapping_v1.md`
- `[METRICS] SUPPORT — Support KPI Dashboard` · `05` §9 metrics → Cowork artifact

## LATER (queued, not started)

- `[DOC] SUPPORT — Premium Support Offer Design` · Phase 5 input, concept-only
- `[DOC] SUPPORT — Community-to-Support Deflection Strategy` · Phase 3+ input, concept-only

---

## Decisions surfaced (consolidated)

| ID | Decision | Recommendation | Locks at |
|---|---|---|---|
| **Su-1** | Support coverage model at v1 | **Founder-only, defined hours** | Before P1 Narrow Ship public launch |
| **Su-2** | Support tooling stack | **Email + in-product ticketing only** (no Help Scout / Intercom at v1) | Before P1 Narrow Ship |
| **Su-3** | Coverage hours canonical | **Sun–Thu 09:00–15:00 GMT+4** (UAE workweek) | Before SLA publication |
| **Su-4** | Per-tier SLA differentiation | **Uniform first-response, tier-stratified resolution** | Before SLA publication |
| **Su-5** | Status page presence | **Public status page from launch** | Before P1 launch |
| **Su-6** | Vendor-outage comms channel | **Email + status page + Telegram bot** | Before P1 launch |
| **Su-7** | Refund authorization | **Founder-approved per case at v1** | Before P1 launch |
| **Su-8** | First support hire trigger | **Sustained >25 hrs/week founder support load for 3+ weeks** OR sustained >10 hrs/week for 2+ weeks (escalation trigger to invest in deflection first) | Phase 2 close |

### Cross-workstream decision unlock

| Decision (other workstream) | What SUPPORT contributes |
|---|---|
| **Pr2-5** (Refund SLA per tier) | `02-support-sla-framework.md` §6 recommends **uniform 14d eligibility + tier-stratified processing time + DF v2 first-30-days seat-return carve-out**. Resolves Pr2-5 input. |

---

## Open questions surfaced (consolidated)

1. **SuQ-1** — At what active-paid-customer count does support load reliably exceed founder capacity? (Validate via P0 cohort actual time spent.)
2. **SuQ-2** — Does email-only inbound channel produce measurable conversion-loss vs adding in-app chat? (Cohort feedback.)
3. **SuQ-3** — Vendor-outage comms latency target (30 min status-page update) — is this achievable with current Eng-side monitoring stack? (REQUIRED INPUT.)
4. **SuQ-4** — Refund volume tracking 3–8% baseline — does P0 cohort confirm? If higher, what's the dominant driver (onboarding, product-fit, value-delivery)?
5. **SuQ-5** — Sub-$5k Free user support volume — is it materially higher than $5k+ Free, or comparable?
6. **SuQ-6** — Telegram bot question-deflection — do users accept "support is via email" auto-redirect or expect bot triage?
7. **SuQ-7** — DF v2 customers paying $1,199/mo + per-seat — does the published 4-hour resolution target on P3 hold credible vs their expectation?
8. **SuQ-8** — Counsel review cadence on `REG.*` tickets — quarterly sufficient, or specific cases need accelerated review?
9. **SuQ-9** — Quarterly template review — who owns? (Strategy CoS at v1; first hire when scaled.)

---

## REQUIRED INPUT items (consolidated)

| Item | Source | Affects |
|---|---|---|
| Confirm current support tooling state (email setup, in-product ticketing form existence) | Eng / Founder | `01` §3 (tooling stack) |
| Confirm engine monitoring stack capabilities (vendor-outage detection, P1 alert paging) | Eng | `03` Escalation A; `05` Escalation A |
| Confirm public status page exists OR is buildable for P1 launch | Eng | Su-5 lock |
| Confirm Stripe webhook → entitlement pipeline + chargeback flow + refund execution capability | Eng / FinOps | `05` Escalation C/D |
| Confirm engine status / uptime page is public + accurate | Eng | `04-first-value-experience-design.md` (ONBOARDING) + this workstream |
| Confirm Telegram bot @ScoopyAI_bot has user-affected-segment broadcast capability | Eng | Su-6 lock |
| UAE national holidays calendar for SLA auto-extension comms | Founder | `02` §8 holiday extension |
| Counsel selection for Phase 4 engagement | Founder | `03` Escalation E |
| Time-tracking method for founder support time (KPI input) | Founder | `01` §2 + `05` §9 |
| Initial template authoring (10 priority templates per `05` §6) | Founder + Strategy CoS | NEXT phase |

---

## Anti-overclaim audit roll-up

Every NOW draft was authored against the §6.10 anti-overclaim flags + Scoopy custom instructions canonical phrasings. Six canonical responses are codified in `05` §7 — verbatim, never modified, founder + Strategy CoS sign-off required for revision.

- **Validation disclaimer** ("Testnet only · 30-day validation phase · No real capital.") — surfaced in `01` §2 auto-responder; `05` Canonical 1 + 5; daily anti-overclaim checklist (`05` §5).
- **PCC v2 §8 reference** — Canonical 1 (`05` §7) is the single canonical response for real-capital questions; Escalation B (`05` §8) routes all such tickets to it verbatim.
- **Founder-cohort canonical phrasing** ("Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies.") — Canonical 2 (`05` §7); inherited from `_pricing/03` §6.
- **"v2" / "v3" qualifiers on roadmap features** — surfaced in Canonical 4 (anti-ICP decline) + daily anti-overclaim checklist.
- **Sub-$5k disciplined respect** ("we'll be back" framing) — Canonical 5 (`05` §7) explicit; Escalation F (`05` §8) anti-ICP filtration distinct from sub-$5k respect.
- **Region-block (US) honest posture** — Canonical 6 (`05` §7) — "Not on our roadmap at this time" verbatim from `_onboarding/03` §5.

No new overclaim risks introduced. SUPPORT contributes a clean baseline pending live walk-through of current support flow + tooling.

---

## Cross-workstream linkages

SUPPORT produces inputs consumed by + depends on inputs from:

| Direction | Workstream | What | Where |
|---|---|---|---|
| SUPPORT → PRICING (Pr2-5) | Refund SLA framework | Resolves Pr2-5 (refund SLA per tier) at uniform 14d eligibility + tier-stratified processing | `02` §6 |
| SUPPORT ← PACKAGING | Plan comparison table | Tier-tiered SLA published on pricing-page tier cards inherits from `02` §3 | `02` §3, `_packaging/03` |
| SUPPORT ← PACKAGING | Billing-to-entitlement audit (Pk-NEXT) | Stripe drift detection feeds support escalation criteria | `_packaging/04` §6 entitlement contract |
| SUPPORT ← PRICING | No free trial (Pr2-3) | Support inbox audit verifies no trial-related tickets indicate Stripe drift | `05` Escalation C; cross-validates Pr2-3 |
| SUPPORT ← PRICING | Founder-cohort canonical phrasing | Inherited verbatim into Canonical 2 + 5 | `_pricing/03` §6, `05` §7 |
| SUPPORT ← PRICING | Pricing philosophy (anti-pressure, anti-stack) | Inbox SOP §5 anti-overclaim checklist enforces | `_pricing/02` Principles 1–7 |
| SUPPORT ← ONBOARDING | Friction audit P0/P1 backlog | Pre-launch remediation prevents inbound spike | `_onboarding/05` |
| SUPPORT ← ONBOARDING | Activation milestones instrumentation | Cohort tags drive triage segmentation | `_onboarding/02` §5 |
| SUPPORT → §13 KPI | Support KPI dashboard | Per-category volume + resolution time + deflection rate | `05` §9 |
| SUPPORT → §11 financial model | Support cost line | Founder time + first-hire trigger ($X compensation) | `01` §6 SLA contract with founder time |
| SUPPORT → Phase 4 counsel | Regulatory ticket queue | Quarterly counsel review feeds Phase 4 legal posture | `03` Escalation E |
| SUPPORT → GTM | Status page + post-mortem publication | Trust-load surfaces Phase 3 GTM channel mix can reference | (forthcoming GTM) |

---

## Linkage to Phase 2 charter exit criteria

Phase 2 charter §4 requires (SUPPORT row):

> **SUPPORT** — Severity matrix (P1–P4), triage SOP, escalation paths, vendor-outage runbooks per vendor in P1 stack, refund-handling SOP, trust-load comms templates. Documented in `_phase-2/04-support.md`.

Status against exit criteria:

- ✓ Severity matrix (P1–P4) drafted in `02` §2.
- ✓ Triage SOP drafted in `05` §4.
- ✓ Escalation paths drafted in `03` §3 + `05` §8.
- ✓ Vendor-outage runbook framework drafted in `03` Escalation A + `05` Escalation A; per-vendor playbook detail is `Exchange Connectivity Support Playbook` (NEXT).
- ✓ Refund-handling SOP drafted in `05` Escalations C + D + Canonicals 3.
- ✓ Trust-load comms templates drafted as 6 canonical responses in `05` §7; full template library is `Standard Response Templates` (NEXT).
- ⏳ Lock requires the 8 **Su-*** decisions + 10 REQUIRED INPUT items + execution of Phase 2 NEXT items (Help Center Structure, Standard Response Templates, Billing Support Playbook, Exchange Connectivity Support Playbook, Support KPI Dashboard).

SUPPORT workstream NOW work is **draft-complete**. Lock requires the eight **Su-*** decisions + REQUIRED INPUT confirmations from Eng / FinOps / Founder + Phase 2 NEXT delivery (especially template library + per-vendor playbook detail before P1 Narrow Ship public launch).

---

## Phase 2 → Phase 3 handoff

SUPPORT contributes the following to the Phase 2 → Phase 3 handoff (per Phase 2 charter §10):

- ✓ Pricing-page SLA copy block ready for render (per `02` §10).
- ✓ Status page operational; vendor-outage comms tree live.
- ✓ Founder-cohort canonical phrasing enforced across all support replies.
- ✓ Anti-overclaim audit clean across all canonical responses.
- ⏳ Support KPI dashboard live (NEXT phase).
- ⏳ Help Center articles ≥10 published (NEXT phase).
- ⏳ Standard response templates ≥15 published (NEXT phase).
- ⏳ Billing + connectivity playbooks signed (NEXT phase).

Phase 3 cannot turn on paid acquisition without the ⏳ items cleared (per `_pricing/02` Principle 7 — pricing-page-area surfaces are trust load, including support comms).
