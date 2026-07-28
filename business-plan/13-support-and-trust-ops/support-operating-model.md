# Support Operating Model

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_support/01-support-operating-model.md`; `_phase-2/_support/02-support-sla-framework.md`; `_phase-2/_support/03-ticket-routing-and-escalation-rules.md`

---

## 1. Support philosophy

Five operating beliefs.

1. **Support is value delivery, not a cost center.** Disciplined-trader cohorts judge a trading product on its incident response inside the first 90 days. That judgment is irrevocable.
2. **Honest constraints beat inflated promises.** A published "Sun–Thu 09:00–15:00 GMT+4" coverage that is consistently met builds more trust than a "24/7 priority support" claim that breaks under load.
3. **Severity outranks tier for safety-critical issues.** A Free user reporting a possible auth bypass gets the same P1 response as a Desk Full v2 customer reporting the same. Money does not buy faster help on safety.
4. **Support is product-tier voice.** Terse, technical, declarative, anti-overclaim. No "Hi friend! Sorry to hear that 😔". Per Scoopy custom instructions and `09-brand-messaging.md`.
5. **Founder-led until evidence justifies hiring.** Founder runs support through P1 (Jun–Jul 2026). First support hire triggers at a pre-defined volume / hour threshold, not at a calendar date.

---

## 2. Recommended support model for current stage

**Founder-led, defined coverage hours, narrow channel set, lightweight tooling, scaling trigger explicit.**

### 2.1 At v1 (P0–P1 — through Jul 2026)

- **Owner:** Founder (Mohammed)
- **Coverage:** Sun–Thu 09:00–15:00 GMT+4 (UAE time) — ~30 hours/week standard
- **Out-of-coverage:** P1 severity (vendor outage, security, data integrity) covered 24/7 via engine monitoring + on-call
- **Tooling:** Email inbox + in-product contact form + status page; lightweight ticketing (e.g., simple inbox tagging, not full Zendesk)
- **Scaling trigger:** First support hire when ticket volume sustained ≥ X tickets/day or coverage hours strain ≥ Y hours/week (specific thresholds in `_phase-2/_support/01-support-operating-model.md` §6)

### 2.2 At v2 (P2 onwards — Aug 2026 onwards)

- **Owner:** Founder + 1 support contractor (PT or FT depending on volume)
- **Coverage:** Extension to Mon–Fri standard, with weekend P1 coverage by founder/on-call
- **Tooling upgrade:** Real ticketing (Zendesk / Front / Help Scout) — depending on cost vs. capability evaluation
- **Brand-voice review:** Every customer-facing reply by contractor passes brand-voice skill audit at v2

### 2.3 At v3+ (post-P3 — Q1 2027 onwards)

- **Owner:** Founder + 1 FT support lead + 1 specialist (if volume justifies)
- **Coverage:** UAE business hours + EN-fluent overlap into US morning (without unblocking US signups)
- **Tooling:** Full ticketing + knowledge base + status page integration
- **Quarterly support metrics review:** Per `business-plan/13-kpi-okr.md`

The model **does not** jump from "founder-led" to "enterprise CS team" — the intermediate steps (1 contractor, 1 lead) are deliberate. Skipping them produces tier-mismatched support that the cohort notices.

---

## 3. Support channels

### 3.1 v1 channels — supported

| Channel | Purpose | Audit trail | Status at v1 |
|---|---|---|---|
| **Email** (`support@coinscope.ai` — REQUIRED INPUT confirm) | Primary inbound; first-response for all tiers and severities | Yes (mailbox) | LIVE |
| **In-product help menu / contact form** | Inbound for logged-in users; auto-attaches account context (tier, signup date, tier-relevant config) | Yes (DB record + email mirror) | TBD pre-P1 |
| **Status page** | Outbound only — vendor outage + incident comms; uptime history | Public history | TBD pre-P1 |
| **`@ScoopyAI_bot` Telegram** | Alerts only (per Scoopy custom instructions). NOT a support channel | n/a | LIVE for alerts |

### 3.2 v1 channels — not supported

| Channel | Why not |
|---|---|
| **Live chat / chatbot** | Sets expectation of <1-min response; founder-bandwidth incompatible; voice-discipline fragile under chat pressure |
| **Phone / voice** | Asynchronous-text-first reduces context loss + creates audit trail; voice support adds disproportionate ops cost |
| **Twitter / X / LinkedIn DM** | Cannot guarantee delivery; lacks audit trail; founder-DM channels stay personal, not support |
| **Discord / Slack community** | Open community deferred to LATER per `_phase-2/_support/`; cohort-only Discord at P3+ at earliest |
| **WhatsApp** | UAE-region cultural default but lacks audit trail; not a support channel |
| **Telegram replies to `@ScoopyAI_bot`** | Bot is alerts-only; if a user replies, auto-response routes them to email |

### 3.3 The narrow-channel discipline

- Single founder cannot multi-channel without quality drop.
- Email + in-product form covers ~95% of inbound (industry-norm INFERENCE; validate at P1 close).
- Status page covers proactive comms.
- Adding channels later is cheap; removing them after users learn to use them is expensive.

---

## 4. Escalation logic

### 4.1 Severity matrix (locked)

Every ticket assigned one of four severity levels at triage. Severity drives SLA.

| Severity | Definition | Response window (within coverage hours) |
|---|---|---|
| **P1 — Critical** | Real-capital risk, security/auth failure, data integrity at risk, full engine outage, vendor outage affecting majority of users | <30 min from detection; 24/7 |
| **P2 — High** | Significant feature broken; partial vendor outage; billing failure blocking conversion; refund within 14d window | <4 hours from receipt |
| **P3 — Standard** | Single-user feature issue, billing question, account/exchange-connection question, non-blocking confusion | <24 hours from receipt |
| **P4 — Low** | Feature request, future-roadmap question, anti-ICP outreach, marketing-style inquiry, brand-voice / copy feedback | <72 hours from receipt |

Internal targets are ~30% tighter than published SLAs. Per `_phase-2/_support/02-support-sla-framework.md` §3.

### 4.2 Auto-escalation triggers

Tickets containing any of the following **auto-flag P1 for founder review** at intake:

- "real money" / "real capital" / "live trading"
- "unauthorized access" / "breach" / "hacked"
- "wrong balance" / "missing funds" / "incorrect position"
- "executed without my permission" / "rogue trade"
- "withdrawal" / "withdrawn" (in any context — even anti-ICP confusion)
- "security issue" / "vulnerability"

The user may be misunderstanding (e.g., demo-trade context confused with real money). The intake severity is set by content, not by the founder's eventual interpretation. Reclassification happens after triage; reclassification logged.

### 4.3 Escalation paths

| Escalation type | Trigger | Path |
|---|---|---|
| **Within support** | P3 ticket reveals P2 facts during investigation | Reclassify; log; meet new SLA |
| **To product / engineering** | Ticket reveals a real bug | Open issue in repo; SLA pauses pending fix; user informed of timeline |
| **To counsel** | Ticket touches legal posture (refund disputes outside policy; jurisdictional questions; data-deletion requests) | Counsel reviewed; user informed of timeline |
| **To founder** | Any P1; any P2 outside founder coverage hours; any escalation by user request | Founder takes the ticket; on-call alert if out-of-hours |
| **To incident comms** | Vendor outage detected; engine bug confirmed at scale | `incident-communications.md` flow activates |

### 4.4 What cannot be auto-resolved

- Refund decisions outside the 14-day money-back window — founder review only
- Account access disputes (inheritance, partner access) — counsel review
- Anti-ICP signal-group bundling requests — declined per `09-brand-messaging.md`
- Real-capital deployment requests outside §8 phased ramp — declined; gate is structural

---

## 5. Support boundaries

### 5.1 What support **does**

- Answer product / configuration / billing / exchange-connection questions
- Triage incidents and route per severity
- Process refunds within 14-day money-back window per `07-packaging-and-pricing/trial-and-discount-policy.md` §5
- Surface bug reports to engineering with reproducible context
- Communicate vendor incidents transparently
- Escalate to founder / counsel / engineering per matrix

### 5.2 What support **does not do**

- **Provide investment advice, trade ideas, or signal interpretation.** Per `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`. If a user asks "should I take this trade?", the response is "We don't provide trade advice; here's how the regime label / gate result is calculated, and here's the methodology page link."
- **Offer alpha-source content or bypass anti-ICP guardrails.** A request to "add Bybit copy-trade" or "let me share my signals with friends" is declined per `09-brand-messaging.md`.
- **Modify cohort caps or extend founder-cohort pricing past the eligibility window.** §6.7 + §5.3.5 are locked policy.
- **Disclose other users' data, configurations, or any personally identifying information.** Per privacy commitments.
- **Promise a roadmap date.** Roadmap is gate-driven, not calendar-driven. Support can confirm "on the roadmap" or "deferred" with reference to public roadmap; cannot promise dates.
- **Process real-capital deployment outside the §8 phased ramp.** The gate is structural; no support escalation path bypasses it.

### 5.3 Why these boundaries are explicit

The boundaries are positioning surfaces. A support reply that says "I can't promise a date but let me check with the team" is voice-incongruent; product-tier says "Bybit is on the roadmap, scheduled for P2 vendor expansion (Aug–Sep 2026). The PR/decision-log entry is at [link]." Calibration in support carries through to retention.

---

## 6. Billing / support separation where relevant

### 6.1 Default — billing handled inside support

For v1, billing tickets are handled inside the same support inbox. Reasons:

- Volume too low to justify a separate billing queue.
- Most billing tickets are simple (refund within 14d, tier-change confirmation, invoice request).
- Founder context speeds resolution.

### 6.2 Where separation matters

- **Refund decisions** — founder-only. Support contractors (when added at v2+) cannot independently grant refunds outside the 14-day window.
- **Chargeback handling** — founder-only; counsel briefed if pattern emerges.
- **Per-seat invoicing for Desk Full v2** — at P5+, may need a billing-specific contractor or a dedicated workflow tag.
- **Tax / VAT-registration touch points** — flagged at thresholds per `business-plan/06-pricing-monetization.md` §6.8; not a support concern at v1.
- **Stripe disputes** — handled at the Stripe layer; support copies the user; counsel notified for any escalation.

### 6.3 Privacy of billing data

Billing data (card last-4, transaction history) is **never** discussed across channels other than email-with-account-verification. A Telegram or in-app message asking "Why was I charged $79?" gets routed to email with a verification step. This is a security stance, not just a procedure.

---

## 7. Exchange / provider issue handling expectations

### 7.1 Exchange (Binance USDT-M; +Bybit at P2) issues

When a Binance API issue affects users:

| Issue | Detection | Action |
|---|---|---|
| **Binance full outage** | Engine monitoring auto-flags; vendor status page check | P1 incident; status page updated within 15 min; user-facing copy uses approved phrasing (`incident-communications.md` §4) |
| **Binance partial outage** (specific endpoints down) | Engine logs; user reports converging | P2 incident; status page note; affected users notified |
| **User's API key expired / IP-restricted / wrong scopes** | User reports inability to connect | P3 ticket; troubleshooting doc linked; user resolves via Binance |
| **Rate-limiting on Binance side affecting our scanner** | Engine monitoring detects request weight saturation | P2 incident; `scanner-engine-optimizer` runbook entry |

### 7.2 Other vendor issues (CoinGlass, Tradefeeds, CoinGecko, Stripe, Telegram, Claude API)

| Vendor | Failure mode | User-facing impact |
|---|---|---|
| **CoinGlass** | OI / liquidation feed down or stale | Signal quality degrades; surface via status page |
| **Tradefeeds** | Adjacent data degraded | Limited impact; surface if signals affected |
| **CoinGecko** | Price reference degraded | Limited impact; surface if signals affected |
| **Stripe** | Billing failure | P2 incident; user-facing copy explicit; retry logic per `07-packaging-and-pricing/trial-and-discount-policy.md` §5 |
| **Telegram Bot API** | Alerts undelivered | P2 incident; dashboard remains primary; user-facing notice |
| **Claude API** | Optional analytical assist degraded | Minimal impact (used minimally during P1); status page entry |

Vendor failure-mode mapping is detailed in `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`.

### 7.3 Handling expectations published to users

Published on `coinscope.ai/status` or equivalent:

- Live engine status (green / yellow / red)
- Vendor incident history (90-day rolling window)
- Active incidents with last-update timestamp
- Subscribe-by-email for vendor incident notifications (opt-in)

Per `incident-communications.md` § templates, vendor incidents are user-facing within minutes of detection. Concealing a vendor incident from users is a brand-voice violation.

---

## 8. Who needs higher-touch support first

### 8.1 P1 cohort users (40 P1 users — Jun–Jul 2026)

Optional founder kickoff call within first 7 days of signup; cohort observation cadence weekly; founder reach-out on stuck-state indicators per `12-onboarding-and-activation/activation-milestones.md` §5.

This is **not** a different SLA — it is a different observation cadence. The SLA is what's published.

### 8.2 P3 Layla candidates (Desk Preview during P1–P2)

- Mandatory founder kickoff call (capacity ≤10 per cohort window per `12-onboarding-and-activation/onboarding-strategy.md` §6.2).
- "Talk to founder" CTA on the Desk Preview pricing card per `_phase-2/_onboarding/01-first-time-user-journey.md` Swim-lane C.
- Cohort observation per Desk Preview activation criteria.

### 8.3 Desk Full v2 customers (P5+)

- Named ops contact per `07-packaging-and-pricing/plan-matrix.md` §5.
- Priority routing on tickets; SLA target ≤4 business hours first-response.
- Per-seat onboarding for partner / analyst seats invited by the PM.

### 8.4 Trader users at scale (P2+)

- Self-serve default. Founder kickoff is offered only at edge-case high-account-size signups during P1; not a general benefit.
- Best-effort SLA per the published matrix; ≤2 business days first-response at P1; tightens at P2 onwards.

### 8.5 Free users

- Public docs + community; no individual support obligation.
- Severity supersedes — a Free user reporting a P1 issue gets P1 response.

---

## 9. Support maturity progression over time

Five stages mapped to the locked phase plan.

| Stage | Window | Support shape | Tooling | Brand-voice review |
|---|---|---|---|---|
| **v1** | P0–P1 (May–Jul 2026) | 1 founder; defined coverage hours; email + in-product form | Email inbox + lightweight tagging; basic status page | Founder runs every reply through brand-voice skill |
| **v1.5** | P2 (Aug–Sep 2026) | 1 founder + 1 PT contractor (if volume justifies) | Status-page upgrade; consider real ticketing (Front / Help Scout) | Contractor replies pre-checked by skill; founder approves until quality bar holds |
| **v2** | P3 (Oct–Dec 2026) | 1 founder + 1 FT contractor; coverage extension | Real ticketing; knowledge base v0; status-page integration | Contractor independent; spot-check audit weekly |
| **v2.5** | P4 (Jan–Feb 2027) | Founder + 1 FT support lead | KB v1; cross-team escalation matrix | Audit cadence quarterly |
| **v3** | P5+ (Mar 2027+) | Founder + 1 lead + 1 specialist (if Desk Full v2 volume justifies) | Full SaaS support stack | Audit cadence quarterly + per-incident review |

**The rule:** **support hires after evidence accumulates, not before.** A premature contractor hire at v1 produces voice-incongruent replies that the cohort notices. A delayed v2 hire produces SLA breach and trust damage. The trigger is volume / hours strain, not calendar.

---

## 10. Cross-references

- Support operating model canonical: `business-plan/_phase-2/_support/01-support-operating-model.md`
- Support SLA framework: `business-plan/_phase-2/_support/02-support-sla-framework.md`
- Ticket routing + escalation rules: `business-plan/_phase-2/_support/03-ticket-routing-and-escalation-rules.md`
- User issue taxonomy: `business-plan/_phase-2/_support/04-user-issue-taxonomy.md`
- Support inbox + response workflow: `business-plan/_phase-2/_support/05-support-inbox-and-response-workflow.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications: `business-plan/13-support-and-trust-ops/incident-communications.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
