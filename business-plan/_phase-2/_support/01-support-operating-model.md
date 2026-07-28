# SUPPORT — Support Operating Model

**Task:** `[DOC] SUPPORT — Support Operating Model`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — founder-led at v1; team-scaling triggers defined
**Anchored to:** §10 ops-support framework; current support tooling REQUIRED INPUT; Scoopy custom instructions (product-tier register); ONBOARDING `_onboarding/05-friction-audit-across-current-flow.md` (predicted support load).
**Feeds decisions:** **Su-1**, **Su-2**, **Su-3**, **Su-8**.

---

## 1. The model in one paragraph

**Founder-led at v1, with explicit defined hours, lightweight tooling, and a documented scaling trigger.** Support is one founder for the duration of P1 Narrow Ship (Jun-Jul 2026). At a defined load threshold, the first support hire is triggered. The model trades response speed for direct-founder context; the trade is explicit in the SLA framework (`02-support-sla-framework.md`) and disclosed honestly to users at signup ("Support is provided by the founder during defined hours").

---

## 2. Coverage

### Coverage hours (per **Su-3** option a — recommended)

| Day | Hours (GMT+4 / UAE time) | Coverage type |
|---|---|---|
| Sunday | 09:00–15:00 | Standard (UAE/MENA work-week start) |
| Monday | 09:00–15:00 | Standard |
| Tuesday | 09:00–15:00 | Standard |
| Wednesday | 09:00–15:00 | Standard |
| Thursday | 09:00–15:00 | Standard |
| Friday | (no standard coverage; weekend) | Incident response only (P1 severity, see SLA framework) |
| Saturday | (no standard coverage; weekend) | Incident response only |

**Total standard coverage:** ~30 hours/week, 5 days.
**Out-of-hours:** P1 severity (vendor outage, critical incident, security) only.
**Holidays:** UAE national holidays observed; published in advance on status page.

### Coverage commitments published at customer-facing surfaces

- Pricing page footer: link to "Support hours" page.
- Account dashboard help menu: "Support hours: Sun–Thu 09:00–15:00 GMT+4. P1 incidents covered 24/7."
- Email signature: "Support hours: Sun–Thu 09:00–15:00 GMT+4 (UAE)."

### What "covered" means

- **First-response SLA holds within coverage hours** (per `02-support-sla-framework.md`).
- **Out-of-hours tickets queue.** Auto-acknowledgement fires immediately ("Received outside coverage hours; first response by [next-coverage-window-start-time + SLA window]").
- **P1 severity bypasses coverage hours** via on-call / monitoring alerts.

---

## 3. Channels

### v1 channels (per **Su-2** option a — recommended)

| Channel | Purpose | Status at v1 |
|---|---|---|
| **Email** (`support@coinscope.ai` — REQUIRED INPUT confirm) | Primary inbound; all tier first-response | LIVE (assumed) |
| **In-product help menu / contact form** (REQUIRED INPUT — confirm dashboard has contact form) | Inbound for logged-in users; auto-attaches account context | TBD |
| **Status page** (REQUIRED INPUT — confirm exists or create) | Outbound: vendor-outage + incident comms; uptime history | TBD per **Su-5** |
| **Telegram bot @ScoopyAI_bot** | Alerts only (per Scoopy custom instructions); NOT support | Existing for alerts |
| **Founder direct DM (X / LinkedIn / personal email)** | Out-of-band founder relationships only; NOT a published support channel | Discouraged at v1 |

### Channels we do NOT support at v1

- **Live chat / chatbot.** Adds expectation of <1 min response; founder-bandwidth-incompatible.
- **Phone / voice.** Asynchronous-text-first reduces context-loss + creates audit trail.
- **Twitter / X DM as support channel.** Cannot guarantee delivery + lacks audit trail.
- **Community forum support.** Discord / Slack community deferred to LATER per `04-support.md` §8 LATER.

### Why narrow channel set

- Single founder cannot multi-channel without quality drop.
- Email + in-product form covers ~95% of inbound (INFERENCE — category norm).
- Status page covers proactive comms.
- Adding channels is cheap; removing them after users learn to use them is expensive.

---

## 4. Tooling (per **Su-2**)

### Recommended at v1: email + in-product ticketing

**Why not Help Scout / Intercom / Zendesk at v1:**

- Cost: $20–$50/user/month; founder is the only user; bills $240–$600/yr for tooling that solves problems we don't yet have.
- Complexity: each tool is a learning curve + a support-data lock-in if we switch.
- Premature optimization: workflows we'd build before we know the actual ticket-shape distribution.

**Trigger to add ticketing tool:**

- Sustained >15 hrs/week founder support load AND
- Ticket volume >20/week AND
- Founder identifies specific tooling-driven friction (e.g., losing track of ticket states, missing follow-ups)

If trigger fires: evaluate Help Scout (lightweight, email-native) first. Intercom / Zendesk only if customer-facing chat or self-serve KB needs converge.

### v1 minimum tool stack

| Need | Tool at v1 | Notes |
|---|---|---|
| Inbound email | Personal/business email | REQUIRED INPUT — confirm `support@coinscope.ai` configured |
| In-product contact form | Dashboard form → email | REQUIRED INPUT — confirm or build |
| Ticket tracking | Email folders + manual labels | Workable up to ~20 tickets/week |
| Response templates | Saved drafts in email client | Per `Standard Response Templates` (NEXT) |
| Status page | TBD per **Su-5** (recommend StatusPage / Atlassian or simple custom) | Public; auto-update on engine monitoring alerts |
| Knowledge base | TBD per Help Center Structure (NEXT) | Phase 3 build; v1 = pricing-page FAQ + scattered docs |
| Refund processing | Stripe dashboard | Founder-approved per case at v1 (Su-7 option a) |
| Vendor-outage detection | Engine monitoring (REQUIRED INPUT — confirm what's instrumented) | Auto-trigger comms when detected |

---

## 5. Roles + responsibilities at v1

| Role | Holder at v1 | Responsibilities |
|---|---|---|
| **Support owner** | Founder | All inbound triage, response, resolution, follow-up, refund decisions |
| **Vendor escalation** | Founder | Binance / CoinGlass / Tradefeeds / CoinGecko / Claude support relationships |
| **Engine incident response** | Founder + Eng (same person at v1 — REQUIRED INPUT confirm) | PCC v2 §8 incident handling |
| **PCC v2 §8 communication owner** | Founder | Single canonical answer to "is it production-ready" / "real capital" questions |
| **Regulatory / counsel coordination** | Founder | Routes regulatory questions to UAE counsel (Phase 4 trigger) |
| **Billing / refund authorizer** | Founder | Per **Su-7** option a — founder-approved per case |
| **Status-page updates** | Founder (auto-augmented by engine monitoring) | Per **Su-6** |

When team scales: split support owner first (recommended first hire), then engine incident response (likely existing Eng), then specialized billing role at higher scale.

---

## 6. Scaling triggers

### Trigger 1 — First support hire (per **Su-8** option a — recommended)

**Trigger condition:** sustained >25 hrs/week founder support load for 3+ consecutive weeks.

**Why this trigger:**

- Founder bandwidth at >25 hrs/week is unsustainable; product / strategy / Eng work degrades.
- 3-week sustained measurement filters out one-off spikes (e.g., post-launch).
- Ties to capacity, not revenue or cohort size — capacity is the binding constraint.

**What to hire:**

- Profile: technical contractor, 20–30 hrs/week, async-first, English-fluent.
- Geography: GMT+0 to GMT+5 timezone overlap to extend coverage hours; non-UAE acceptable.
- Comp: contractor rate per HR comp benchmark (Phase 4 input).
- Onboarding: 2-week shadowing + canonical SOPs (this workstream's deliverables).

**Backup triggers (any one fires):**

- Single P1 incident requiring >8 hrs continuous founder attention with concurrent ticket queue >20.
- Founder identifies specific support-driven product / strategy task slip ≥2 weeks.

### Trigger 2 — Support tooling upgrade

**Trigger condition:** see §4 above.

### Trigger 3 — Coverage hours expansion

**Trigger condition:** support load distribution shows >15% of tickets arriving Friday/Saturday + first-response SLA misses on >10% of those.

**Action:** add weekend partial coverage (~3 hrs/day, P2-severity-and-above).

### Trigger 4 — Live chat / chatbot consideration

**Trigger condition:** sustained >100 tickets/week AND deflection-eligible (FAQ / KB-answerable) tickets >40% of volume.

**Action:** evaluate chat (Intercom or Crisp) with chatbot-first KB lookup; live chat only after support team scales to ≥2.

---

## 7. Region / language posture

### Languages

- **English at v1.** Primary support language; all customer-facing surfaces in English.
- **Arabic deferred.** Founder bilingual capacity reserved for high-touch P3 conversations + UAE-government / counsel work; not exposed as a support channel.
- **Other languages.** Out-of-scope at v1.

### Region

- **UAE / MENA + global EN markets.** Per memory `project_jurisdictional`.
- **US-blocked.** Per memory `project_jurisdictional`. Support does not field US-region inquiries; pre-signup region check (per ONBOARDING `_onboarding/03` Step 1) prevents most.
- **EU users.** Standard support; founder may need GDPR-data-request handling (Phase 4 trigger).

---

## 8. Founder time budget

Founder's total weekly time budget: ~40–50 hours (assumed; REQUIRED INPUT confirm).

### Allocation at v1 (target):

| Category | Hours/week target | Notes |
|---|---|---|
| Product / strategy / Eng work | 25–30 | Primary value creation |
| Support | 10–15 | Within scaling-trigger threshold |
| Founder relationships (P3 prospects, partners) | 3–5 | Out-of-band, not in support inbox |
| Operations / admin / planning | 3–5 | Including this Phase 2 work |

If support exceeds 15 hrs/week sustained → re-evaluate scaling trigger weighting.

---

## 9. Honesty in customer-facing comms

Per `_pricing/02-initial-pricing-philosophy.md` Principle 4 (predictable, anti-surprise) — coverage and operating model are disclosed honestly:

| Surface | Copy |
|---|---|
| Pricing page footer | "Support hours: Sun–Thu 09:00–15:00 GMT+4 (UAE). Support is provided by the founder during these hours. P1 incidents covered 24/7." |
| Dashboard help menu | "Support response targets: Free <48h, Trader <24h, Desk Preview <8h, Desk Full v2 <4h, all within coverage hours. P1 incidents <30 min from detection." (Per SLA framework `02`.) |
| Out-of-hours auto-ack | "Received outside coverage hours. First response by [next-coverage-window-start + SLA window]." |
| Vendor outage comms | "We are seeing [vendor] degradation. Status updates at [status page URL]. Engine impact: [specific impact]." |
| First support hire announcement (when triggered) | Honest, brief: "Welcoming [name] to support." |

No "24/7 support" claim. No "instant response" claim. No "Premium support" claim until Premium Support Offer Design (LATER) is shipped.

---

## 10. Failure modes specific to this operating model

- **Founder skips coverage hours.** Without disciplined hours, support load creeps to "always" and product / strategy slip silently. Time-block calendar; respect the boundaries.
- **Support tooling drift.** "Just temporarily using personal email for this one ticket" → audit trail gone. Single inbox per channel from the start.
- **Vendor escalation through public channels.** Tweeting at Binance support is a category-norm anti-pattern. Use vendor enterprise support; document contacts.
- **Out-of-band founder DM as support.** Friend asks via WhatsApp; gets faster response than ticketed user. Two-tier reality. Either route to ticketing or accept founder-relationship is ad-hoc.
- **Team-scaling trigger ignored.** Founder powers through 30 hrs/week support indefinitely; product roadmap slips multiple sprints; first support hire happens reactively in crisis. Trigger is a contract.
- **Tooling upgrade without taxonomy.** Adding Help Scout before User Issue Taxonomy is locked = misconfigured tags + KPI drift. Sequence matters: taxonomy first, tooling later.

---

## 11. What this unlocks

- **Su-1** can be marked recommended at "Founder-only, defined hours" for v1.
- **Su-2** can be marked recommended at "Email + in-product ticketing" for v1.
- **Su-3** can be marked recommended at "Sun–Thu 09:00–15:00 GMT+4."
- **Su-8** can be marked recommended at "Sustained >25 hrs/week for 3+ consecutive weeks" trigger.
- `02-support-sla-framework.md` consumes coverage hours + tooling assumptions.
- `03-ticket-routing-and-escalation-rules.md` consumes role/responsibility table.
- `05-support-inbox-and-response-workflow.md` consumes tooling + coverage assumptions.
- Phase 4 §11 financial model has support cost-line at v1 (founder time only) + scaling trigger ($X for first hire post-trigger).
