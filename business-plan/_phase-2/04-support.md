# 04 — SUPPORT

**Workstream:** SUPPORT
**Phase:** 2 — Monetization
**Status:** Canonical task list absorbed verbatim 2026-05-04. Source of truth for the Phase 2 SUPPORT workstream.
**Canonical authorities:** v1 framework `10-operations-support.md`, `12-risk-compliance-trust.md`; `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`; `_data/operations/Production_Candidate_Criteria_v2.md` §8 Capital Cap; §6.7 refund + dunning + chargeback; PRICING `_pricing/04-trial-and-intro-offer-options.md`; ONBOARDING `_onboarding/05-friction-audit-across-current-flow.md` (audit findings → support load); Scoopy custom instructions (register, regime tokens, validation disclaimer).

---

## 1. Purpose

Lock the **support operating system** for P1 Narrow Ship and into P2: how user issues are received, triaged, routed, resolved, and learned from. SUPPORT is the operational form of the trust posture committed in §12 — it is also the surface where vendor-outage, billing-dispute, and real-capital-question issues land. Done well, it is the highest-leverage trust signal post-onboarding; done badly, it erases every gain Phase 1 + Phase 2 PACKAGING / PRICING / ONBOARDING produced.

## 2. Why this matters specifically for CoinScopeAI

- **Support is a trust-load surface in a low-trust category.** Crypto-trading-tool category averages on response time and resolution quality are poor (INFERENCE — observable in public forums). CSAI's anti-overclaim, capital-preservation positioning is incoherent if support response is opaque or dismissive.
- **Vendor dependency is structural.** Binance, CoinGlass, Tradefeeds, CoinGecko, Claude — every vendor is an outage source we can't fix. Support's job during a vendor outage is comms + escalation, not resolution. Getting comms right is the entire deliverable.
- **PCC v2 §8 governs real-capital communication.** Any user question that touches "should I trade real money" or "is the system production-ready" routes to a single canonical answer. Support cannot improvise here.
- **Refund handling is operational, not policy.** §6.7 sets the policy; support executes it. Misexecution (missed 14-day window, over-refunding to abuse pattern, under-refunding to legitimate request) erodes trust both ways.
- **Per-tier SLA differentiation is a packaging signal.** Desk Full v2 buyers paying $1,199/mo + per-seat expect a different response than Free users — but Free users are future-ICP and cannot be ignored. SLAs encode the expectation.
- **Support load is finite and founder-bottlenecked at v1.** Single-founder support means triage discipline + template library + deflection through documentation are non-negotiable. Phase 2 designs the system that scales without breaking.
- **Friction-audit findings will create a support backlog.** ONBOARDING `05-friction-audit` flagged 11 P0 + 13 P1 items; many of these will surface as support tickets if shipped without remediation. Support workstream coordinates with ONBOARDING fixes.

## 3. Required subsections

1. **Support operating model** — who, when, where, with what tools; founder-led at v1; team-scaling triggers.
2. **Support SLA framework** — first-response + resolution targets per tier per severity; weekly coverage hours; refund SLA (Pr2-5).
3. **Ticket routing and escalation rules** — issue category → owner → escalation path; vendor-outage routing; PCC v2 §8 routing.
4. **User issue taxonomy** — exhaustive issue categories with severity defaults and resolution-path notes.
5. **Support inbox and response workflow** — operational SOP for inbox triage, response, status, resolution, follow-up.
6. **Help center structure** (NEXT) — knowledge-base organization for self-serve deflection.
7. **Standard response templates** (NEXT) — canonical responses for top-N issues with brand-voice register lock.
8. **Billing support playbook** (NEXT) — refund / past-due / chargeback / per-seat dispute handling.
9. **Exchange connectivity support playbook** (NEXT) — Binance API key issues, IP allowlist questions, testnet/mainnet confusion.
10. **Support KPI dashboard** (NEXT METRICS) — first-response time, resolution time, deflection rate, CSAT (if measured), per-tier breakdown.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Support operating model | MD; founder + scaling triggers | Founder + Strategy CoS |
| Support SLA framework | MD per-tier × per-severity matrix | Founder |
| Ticket routing + escalation rules | MD with routing table + escalation tree | Founder + Strategy CoS |
| User issue taxonomy | MD canonical issue catalogue | Strategy CoS |
| Support inbox + response workflow | MD SOP + state-machine spec | Strategy CoS + FinOps |
| Help center structure | MD KB structure spec → live KB (Phase 3) | Strategy CoS |
| Standard response templates | MD template library; brand-voice tagged | Founder + Strategy CoS |
| Billing support playbook | MD with §6.7 operationalized | FinOps + Founder |
| Exchange connectivity playbook | MD with Binance + per-vendor flows | Eng + Strategy CoS |
| Support KPI dashboard | MD spec → Cowork artifact | FinOps + Strategy CoS |

## 5. Assumptions to validate

1. **ASSUMPTION** — Founder is sole support resource at v1 through P1 Narrow Ship (Jun-Jul 2026). First support hire triggered at P2 (Aug-Sep 2026) only if support load exceeds founder capacity per defined trigger. (REQUIRED INPUT — confirm.)
2. **ASSUMPTION** — Support tooling is plain email + dashboard ticketing (or equivalent lightweight system). No Help Scout / Intercom / Zendesk at v1. (REQUIRED INPUT — confirm current state.)
3. **ASSUMPTION** — Coverage hours: 5 days/week, ~6 hours/day in UAE/MENA timezone (GMT+4). Weekend coverage minimum: incident response only. (REQUIRED INPUT — confirm.)
4. **ASSUMPTION** — Languages: English only at v1. Arabic deferred. Founder's bilingual capacity reserved for high-touch P3 conversations.
5. **ASSUMPTION** — Vendor outage comms posture: pro-active to all affected users within 30 minutes of detection; status page (REQUIRED INPUT — confirm exists) updated continuously.
6. **ASSUMPTION** — Refund handling is founder-approved per case for v1; Stripe-portal self-serve refund deferred to Phase 3 (avoids abuse-pattern risk while founder learns the patterns).

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **Su-1** | Support coverage model at v1 | (a) Founder-only, defined hours (recommended at v1). (b) Founder + 1 part-time contractor. (c) Outsourced ticket-triage with founder escalation. | Founder | Before P1 Narrow Ship public launch | Support load capacity, response time |
| **Su-2** | Support tooling stack | (a) Email + dashboard ticketing only (recommended at v1). (b) Help Scout. (c) Intercom (heavier, marketing-overlap). (d) Custom in-app ticketing. | Founder + Eng | Before P1 Narrow Ship | Cost, audit trail, deflection |
| **Su-3** | Coverage hours canonical | (a) 5d/wk, 6h/day, GMT+4 (recommended). (b) 7d/wk reduced hours. (c) 5d/wk extended hours, +on-call weekend incidents. | Founder | Before SLA publication | SLA expectations, founder bandwidth |
| **Su-4** | Per-tier SLA differentiation | (a) Same first-response across tiers, different resolution targets (recommended). (b) Tier-stratified first-response. (c) Free best-effort, paid tiers SLA-bound. | Founder | Before SLA publication | Trust signal, packaging differentiation |
| **Su-5** | Status page presence | (a) Public status page from launch (recommended). (b) Internal-only at v1, public at P2. (c) Embedded in dashboard, no separate page. | Founder + Eng | Before P1 launch | Trust signal, vendor-outage comms |
| **Su-6** | Vendor-outage comms channel | (a) Email + status page + Telegram bot (recommended). (b) Email + status page only. (c) In-app banner only. | Founder + Eng | Before P1 launch | Vendor-outage trust load |
| **Su-7** | Refund authorization | (a) Founder-approved per case at v1 (recommended). (b) Self-serve in-product within 14d window. (c) Hybrid: under-$X self-serve, over-$X founder-approved. | Founder | Before P1 launch | Abuse-pattern risk, support load |
| **Su-8** | First support hire trigger | (a) Sustained >25 hrs/week founder support load for 3+ weeks (recommended). (b) Specific revenue threshold ($X MRR). (c) Specific cohort size threshold. | Founder | Phase 2 close | Phase 3 hiring, headcount budget |

## 7. Failure modes to avoid

- **Promising what vendors can't deliver.** "We'll fix the Binance outage" is not a thing we can promise. Comms posture is "we are seeing X; here's our read on the cause; here's what to expect." Per §12 — vendor risk is acknowledged, not papered over.
- **Real-capital improvisation.** "Yes you can use real money, just be careful" is a PCC v2 §8 violation. Single canonical response routes through §8 gates language.
- **Refund-then-resubscribe abuse tolerated.** §6.7 caps refunds at one per account lifetime. Support must enforce; "the user keeps asking" is not a reason to grant a second.
- **Sub-$5k user treated as second-class.** Per §3.5 + ONBOARDING — sub-$5k is future-ICP. Support response register is identical to paid-tier register; no "this feature is paid" gate-keeping in tone.
- **First-response SLA inflated to look impressive then missed.** "We respond within 1 hour" published, actual median 6 hours = trust-load destroyed. Publish realistic SLA, beat it consistently.
- **Vendor-outage detection lag.** Founder learns about a Binance outage from a user ticket = comms is already late. Engine-side monitoring should detect + auto-trigger comms (REQUIRED INPUT — Eng confirm monitoring stack).
- **Per-tier SLA published but not enforced.** DF v2 user pays $1,199/mo + per-seat expecting differentiated response; gets standard response = packaging integrity broken.
- **Brand voice drift in support replies.** Per Scoopy product-tier — technical, terse, declarative. "So sorry for the trouble!" / "Thanks for your patience!" social-tier bleeds in easily under support pressure. Templates lock register.
- **Status page missing during outage.** Per `_packaging/05-packaging-friction-review.md` Class A — operational opacity is friction. Status page absent = users speculate publicly.
- **No deflection through documentation.** Founder answers the same Binance API key question 50 times = capacity drain. Help center + standard templates deflect early.
- **Incident comms after the fact.** Telling users "by the way, last Tuesday's gate decisions were wrong" *after* they discovered it = trust gone. Per §12 + PCC v2 — proactive disclosure is policy.
- **Refund SLA undefined per tier.** Pr2-5 deferred to TBD = support has no rule to apply. Phase 2 must lock per-tier refund response time.
- **Support inbox shared with sales / partnerships.** Cross-load means urgent support ticket gets buried under inbound sales. Separate inbox per function.
- **Telegram bot used for support questions.** Bot is for alerts only per Scoopy custom instructions; support questions via Telegram are a tooling gap. Either explicit "support is via email" or bot adds support-routing — not silent expectation mismatch.

## 8. Tasks (canonical list — verbatim)

### NOW

**`[DOC] SUPPORT — Support Operating Model`**
- **Objective:** Define who supports, when, with what tools, at what scale. Lock founder-led-at-v1 model + team-scaling triggers.
- **Why:** Without an explicit operating model, support load drifts to founder, founder bandwidth caps, support quality degrades silently. Operating model is the contract.
- **Dependency:** §10 ops-support framework; current support tooling REQUIRED INPUT.
- **Output:** Operating model MD; signed by founder. Feeds **Su-1**, **Su-2**, **Su-3**, **Su-8**.

**`[DOC] SUPPORT — Support SLA Framework`**
- **Objective:** Per-tier × per-severity SLA matrix: first-response + resolution targets; coverage hours; refund SLA per tier.
- **Why:** SLAs are a packaging signal + a trust signal + an internal capacity-planning tool. Without explicit SLAs, every ticket is best-effort and per-tier differentiation is theatre.
- **Dependency:** Support Operating Model; PRICING Pr2-5 (refund SLA per tier); §6.7 refund policy.
- **Output:** SLA matrix MD; published in customer-facing form. Feeds **Su-4**, locks **Pr2-5** input.

**`[DOC] SUPPORT — Ticket Routing and Escalation Rules`**
- **Objective:** Define how every issue category routes to its owner; escalation paths for vendor-outage, PCC v2 §8 real-capital questions, regulatory questions, billing disputes.
- **Why:** Routing discipline is what makes a single-founder support model survivable. Without explicit rules, founder context-switches across all issue types simultaneously.
- **Dependency:** User Issue Taxonomy; Support Operating Model; §12 vendor failure-mode mapping.
- **Output:** Routing table MD + escalation tree.

**`[DOC] SUPPORT — User Issue Taxonomy`**
- **Objective:** Exhaustive catalogue of user issue categories with default severity, resolution path, and common-cause notes.
- **Why:** Without a canonical taxonomy, ticket categorization drifts; KPI tracking is unreliable; templates can't be authored against unknowable categories.
- **Dependency:** ONBOARDING `05-friction-audit` audit findings (predicts support load); §12 vendor failure-mode mapping; current ticket history (REQUIRED INPUT if exists).
- **Output:** Issue taxonomy MD with severity + path per category.

**`[OPS] SUPPORT — Support Inbox and Response Workflow`**
- **Objective:** Operational SOP for inbox triage, first-response, status states, resolution, follow-up. Single canonical workflow.
- **Why:** Workflow discipline lets the founder do support without re-deriving the process per ticket. State-machine clarity reduces dropped tickets.
- **Dependency:** Support Operating Model; SLA Framework; Routing Rules; Issue Taxonomy.
- **Output:** Workflow SOP MD + state-machine spec.

### NEXT

**`[DOC] SUPPORT — Help Center Structure`**
- **Objective:** Knowledge-base organization for self-serve deflection. Categories aligned with User Issue Taxonomy.
- **Why:** Deflection through documentation is the highest-leverage support investment. Each KB article that prevents a ticket is reusable founder bandwidth.
- **Dependency:** User Issue Taxonomy; pricing-page FAQ (per `_packaging/03` §4).
- **Output:** KB structure MD spec; live KB build is Phase 3 GTM dependency.

**`[DOC] SUPPORT — Standard Response Templates`**
- **Objective:** Canonical responses for top-N (estimated 20–30) issue categories. Brand-voice tagged. Editable per ticket but consistent in register.
- **Why:** Templates accelerate response without making it feel canned. They also lock anti-overclaim discipline + canonical phrasings (PCC v2 §8, founder-cohort, validation disclaimer).
- **Dependency:** User Issue Taxonomy; Phase 1 BRAND voice/tone; PRICING canonical phrasings.
- **Output:** Template library MD; integration with chosen support tooling.

**`[DOC] SUPPORT — Billing Support Playbook`**
- **Objective:** Refund / past-due / chargeback / per-seat dispute handling step-by-step. Operationalizes §6.7 + Pr2-5.
- **Why:** Billing issues are highest-trust-cost when mishandled. Playbook + clear authority levels prevent ad-hoc decisions.
- **Dependency:** SLA Framework (refund SLA); §6.7; Stripe configuration; PRICING `[QA] Stripe Plan Mapping Review`.
- **Output:** Billing playbook MD + decision-tree per scenario.

**`[DOC] SUPPORT — Exchange Connectivity Support Playbook`**
- **Objective:** Binance API key issues, IP allowlist questions, testnet/mainnet confusion, Bybit (P2) onboarding, vendor-outage triage. Per-vendor flows.
- **Why:** Exchange connectivity is the highest-volume technical-support category (INFERENCE based on category norms). Playbook + KB articles deflect majority.
- **Dependency:** ONBOARDING `03` Steps 5–8; vendor failure-mode mapping; Eng escalation contract.
- **Output:** Connectivity playbook MD with per-vendor flows + KB article seeds.

**`[METRICS] SUPPORT — Support KPI Dashboard`**
- **Objective:** Specify the dashboard for support KPIs: first-response time, resolution time, deflection rate, ticket volume per category, per-tier breakdown.
- **Why:** Without KPIs, support quality drifts and per-tier SLA enforcement is impossible to verify.
- **Dependency:** SLA Framework; Issue Taxonomy; instrumentation in chosen tooling.
- **Output:** KPI dashboard spec MD; Cowork artifact draft.

### LATER

**`[DOC] SUPPORT — Premium Support Offer Design`**
- **Objective:** Concept the premium / dedicated support offer for Desk Full v2 + per-seat customers. Phase 5 input.
- **Why:** P3 Layla scaling buyers expect dedicated support relationship; concept-only at Phase 2.
- **Dependency:** PACKAGING `Fund/Desk Plan Concept` (NEXT); Layla Phase-5 Pre-read.
- **Output:** Concept MD; *no commitments*.

**`[DOC] SUPPORT — Community-to-Support Deflection Strategy`**
- **Objective:** Concept for whether/how user community (forum, Discord, etc.) deflects support load. Phase 3+ input.
- **Why:** Community deflection works in some categories, fails in others. Concept-only at Phase 2 to avoid premature investment in community infrastructure.
- **Dependency:** Phase 3 channel mix; Phase 3 BRAND community posture.
- **Output:** Concept MD with deflection-vs-cost analysis.
