# SUPPORT — Support Inbox and Response Workflow

**Task:** `[OPS] SUPPORT — Support Inbox and Response Workflow`
**Type:** NOW
**Owner:** Strategy CoS + FinOps
**Status:** DRAFT v0.1 — daily SOP for the founder running the inbox at v1
**Anchored to:** `01-support-operating-model.md` coverage hours + tooling; `02-support-sla-framework.md` severity matrix + first-response targets; `03-ticket-routing-and-escalation-rules.md` routing table + escalation tree; `04-user-issue-taxonomy.md` category catalogue; Scoopy custom instructions (product-tier register).

---

## 1. The inbox in one paragraph

Single email inbox at `support@coinscope.ai` mirrored into the in-product "Contact support" form. Every inbound is a ticket. Every ticket gets a single state at any time. Founder works the inbox in two scheduled blocks per coverage day — morning triage + late-coverage closeout. P1 tickets break the schedule; P3/P4 wait. Templates handle ~60% of volume; canonical responses handle ~25%; ad-hoc replies handle ~15% (with founder authoring).

---

## 2. Ticket lifecycle (state machine)

Every ticket moves through these states:

```
NEW
  ↓ (founder triages within first-response SLA window)
TRIAGED (severity assigned, category assigned, owner = founder)
  ↓ (founder begins response)
IN_PROGRESS
  ↓ (founder sends response)
WAITING_USER
  ├─ (user replies) → IN_PROGRESS
  ├─ (user resolves themselves) → RESOLVED
  └─ (no user reply within auto-close window) → AUTO_CLOSED
        ↓
RESOLVED
  ↓ (auto-close after retention window)
ARCHIVED
```

### State definitions + targets

| State | Definition | Target time-in-state | Anti-target |
|---|---|---|---|
| NEW | Inbound received, not yet triaged | <30 min coverage hours; <12h overnight | >first-response SLA window |
| TRIAGED | Severity + category assigned, ticket queued | <60 min from NEW for P3+ during coverage | (Should pass through quickly) |
| IN_PROGRESS | Founder actively drafting response | Bounded by SLA per severity per `02` §3 matrix | Stalled in IN_PROGRESS = SLA breach |
| WAITING_USER | Reply sent, awaiting user feedback | Auto-close 7 days; resolution-final 14 days | Indefinite WAITING_USER means failed-resolution check |
| RESOLVED | User confirmed resolution OR resolution-final logic | Static state | (None) |
| AUTO_CLOSED | No user reply within auto-close window | Static state | Re-opens if user replies post-close |
| ARCHIVED | Auto-archived 90 days post-RESOLVED for retention | Static | (None) |

### Re-open logic

- A user reply on a RESOLVED or AUTO_CLOSED ticket re-opens the ticket as NEW with a "Re-opened from previous ticket" tag.
- Re-opens within 7 days of RESOLVED inherit the original ticket's category + severity.
- Re-opens older than 7 days are triaged fresh.

---

## 3. Daily inbox SOP for founder

### Coverage day structure (Sun–Thu, GMT+4)

| Time block | Activity | Estimated time |
|---|---|---|
| 09:00–09:30 | **Morning triage** — open inbox, scan for P1, triage all NEW tickets, draft auto-acks if P1 escalation needed | 30 min |
| 09:30–11:30 | **Deep-work block** (product / strategy) — inbox closed; P1 alerts only via separate paging channel | 2 hours |
| 11:30–12:30 | **Late-morning support block** — work P1 + P2 IN_PROGRESS tickets; finish drafts | 1 hour |
| 12:30–13:30 | Lunch + non-support founder work | 1 hour |
| 13:30–14:30 | **Mid-afternoon support block** — P3 + P4 tickets + KB article authoring + template review | 1 hour |
| 14:30–15:00 | **End-of-day closeout** — final inbox sweep, set WAITING_USER status, draft any escalations to Eng/FinOps for next day | 30 min |

**Total support time per coverage day target:** ~3 hours. Steady-state with 50–100 paid customers should land here. If exceeded for 2 weeks, **Su-3** trigger fires (per `01-support-operating-model.md` §2 scaling triggers).

### Friday/Saturday (UAE weekend)

- Inbox auto-responder per `01` §2 sends out-of-hours reply.
- P1 monitoring runs (Eng-side); founder paged only if P1 incident detected by monitoring or if ticket explicitly tagged [URGENT] in subject.
- Best-effort response on P1 only; P2/P3/P4 wait for Sunday morning triage.

---

## 4. Triage protocol per ticket

For each NEW ticket, founder runs this sequence:

### Step 1 — Read the ticket fully (≤2 minutes)

Read the entire body before acting. Skim leads to miscategorization. If user pasted log lines or screenshots, read those too.

### Step 2 — Assign severity per `02-support-sla-framework.md` §2

- P1 — Critical: real-capital risk, security/auth failure, data integrity at risk, full outage, vendor outage majority-affected.
- P2 — High: significant feature broken for tier; partial outage; billing failure; refund within 14d.
- P3 — Standard: single-user feature, billing question, account/exchange-connection question.
- P4 — Low / informational: roadmap inquiry, partnership inquiry, content / brand question.

If ambiguous, default upward (P3 → P2). Don't guess downward.

### Step 3 — Assign category per `04-user-issue-taxonomy.md`

Pick the most-specific subcategory. If none fits, use category-level catch-all. If category-level catch-all is needed repeatedly (>3 times in a week), the taxonomy is missing a subcategory — log for next quarterly review.

### Step 4 — Determine routing per `03-ticket-routing-and-escalation-rules.md` §2

Most v1 routes are "founder responds." Specific exceptions:

- `BIL.CHARGEBACK` → founder + FinOps joint
- `EXC.API_KEY_INVALID` with engine-side suspected fault → founder + Eng joint
- `INC.*` (incident-class) → founder + Eng joint via incident comms tree
- `REG.*` (regulatory) → founder; counsel flag for Phase 4 review

### Step 5 — Send first-response

Choose one of three response forms:

- **Template** (≥60% of cases) — pull from response template library; personalize with user-context fields; send.
- **Canonical response** (~25% of cases) — for PCC v2 §8 / regulatory / founder-cohort questions where canonical phrasing is locked. Copy verbatim from canonical-response register, never modify the canonical body.
- **Ad-hoc** (~15% of cases) — author from scratch when template + canonical don't fit. Always re-read for anti-overclaim audit before sending (§7 below).

### Step 6 — Update state to WAITING_USER (or RESOLVED if first-response is sufficient)

Some tickets resolve in first-response (e.g., "where's my journal?" → "Trader+ feature, here's the link"). Mark RESOLVED if resolution is unambiguous; mark WAITING_USER otherwise.

### Step 7 — Log the outcome

Tag the ticket with:
- Category + subcategory
- Severity
- Response form (template / canonical / ad-hoc)
- Resolution (resolved-on-first / N follow-ups)
- Time-in-state

Tags feed the KPI dashboard (NEXT).

---

## 5. Anti-overclaim audit checklist (per response, ≤30 seconds)

Before hitting send on any response, founder runs this 6-point check:

1. **Does the response avoid promising real-capital readiness?** No "you can trade live now / soon / when you're ready." PCC v2 §8 governs.
2. **If validation phase relevant, is the disclaimer present?** "Testnet only · 30-day validation phase · No real capital."
3. **Are roadmap features qualified with v2 / v3?** No "we'll have audit reporting" — yes "audit-grade partner reporting is on the v2 roadmap (Mar–May 2027)."
4. **Is founder-cohort phrasing canonical?** "Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies." Never "lifetime / forever / always / locked-in."
5. **Is brand voice product-tier?** Technical, terse, declarative. Not "Thanks so much for reaching out!" / "Hope this helps! 😊"
6. **Does the response avoid creating new policy?** "Per our policy, refunds are available within 14 days" — yes. "I can offer you a 30-day refund as a one-time exception" — only if §6.7 explicitly allows; otherwise founder approval logged + escalated.

If any check fails, revise. If revision is unclear, escalate to canonical-response register or async escalate to template-library review.

---

## 6. Response templates — usage protocol

Templates live in the response template library (`Standard Response Templates`, NEXT). At v1, founder maintains a working set in a Notion-mirror doc.

### Template categories (priority for NEXT authoring)

Per `04-user-issue-taxonomy.md` §4 deflection priorities, the top template categories are:

| # | Template | Triggered by |
|---|---|---|
| 1 | "Connecting Binance USDT-M with read-only API key" | `EXC.API_KEY_INVALID`, `EXC.TESTNET_VS_MAINNET_CONFUSION` |
| 2 | "Reading the engine: regime, signals, gate decisions" | `SIG.WHAT_IS_REGIME`, `SIG.WHY_NO_SIGNALS`, `RSK.DEMO_GATE_REJECTED_QUESTION` |
| 3 | "Validation phase and PCC v2 §8" | `PCC.IS_IT_PRODUCTION_READY`, `PCC.WHEN_REAL_CAPITAL`, `PCC.GATE_STATUS` |
| 4 | "Pricing, founder-cohort, refund" | `BIL.PRICING_QUESTION`, `BIL.FOUNDER_COHORT_QUESTION`, `BIL.REFUND_REQUEST_OUT_OF_WINDOW` |
| 5 | "Free vs Trader vs Desk Preview vs Desk Full v2" | `JRN.JOURNAL_NOT_VISIBLE_ON_FREE`, `EXC.MULTI_ACCOUNT_QUESTION`, `RPT.AUDIT_REPORTING_QUESTION` |
| 6 | "Email delivery troubleshooting" | `ACC.EMAIL_NOT_RECEIVED` |
| 7 | "Telegram bot connection" | `ALT.TELEGRAM_CONNECT_HELP` |
| 8 | "Anti-ICP feature decline (signal groups, copy-trade, leverage maximization)" | `FRQ.ANTI_ICP_FEATURE` |
| 9 | "Refund within 14d — auto-approved" | `BIL.REFUND_REQUEST_IN_WINDOW` |
| 10 | "Cancellation confirmation + 90-day reactivation window" | `BIL.CANCELLATION_REQUEST` |

### Personalization fields

Templates use `{{handlebars}}` for user-context insertion:

- `{{user_first_name}}` — from account record
- `{{tier}}` — Free / Trader / Desk Preview / Desk Full v2
- `{{cohort}}` — p0_validation / p1_narrow_ship / public / founder_cohort_in_window
- `{{exchange_account}}` — Binance Testnet / Binance Mainnet
- `{{ticket_subject}}` — original subject line
- `{{founder_signature}}` — Mohammed (founder) — single canonical signature

### Template review cadence

Quarterly review: walk through every template, audit against §5 anti-overclaim checklist, update for any new canonical phrasing changes (e.g., if §6.7 refund policy shifts, refund-related templates inherit).

---

## 7. Canonical responses — verbatim, never modified

Six canonical responses are reproduced **verbatim** with zero ad-hoc variation. Modification requires founder + Strategy CoS sign-off + decision-log entry. Per `_pricing/02-initial-pricing-philosophy.md` audit rules.

### Canonical 1 — Real-capital question (PCC v2 §8)

> Thanks for asking. We're currently in our 30-day validation phase. The system runs against real market data and executes only on testnet. Production Candidate Criteria v2 §8 — our public Capital Cap and Phased Ramp framework — governs when any real-capital path opens.
>
> Until §8 gates pass, the system does not place orders, execute trades, or move real capital. We will publish gate-pass status before any real-capital path becomes available.
>
> If you'd like to read the full Capital Cap framework, it's at [link to PCC v2 §8 published page].
>
> Testnet only · 30-day validation phase · No real capital.

### Canonical 2 — Founder-cohort window question

> Founder-cohort pricing applies to sign-ups during the first 60 days post-public-launch. The discount locks through your first renewal cycle (one cycle from sign-up date). After that first cycle, standard pricing applies.
>
> The cohort window is currently {{open / closed}}; it ends on [LAUNCH DATE + 60 days].
>
> We don't offer "founder discount locked in," "lifetime founder pricing," or any extension beyond the first renewal cycle. Standard pricing is what we publish on the pricing page.
>
> If you have a specific question about your renewal date or pricing, I can pull that up — just send your account email.

### Canonical 3 — Refund-out-of-window

> Refund-eligible window is 14 days from the first paid subscription per account. Per our published policy at [link to §6.7], we don't process refunds outside this window.
>
> You can cancel anytime — cancellation takes effect at the end of your current billing period, with no further charges. Your access continues until that period ends. Account data is retained for 90 days for reactivation; reactivation within that window restores your prior tier and pricing.
>
> If there's a specific issue you ran into that I should know about, I'm listening — feedback like this is how we improve.

### Canonical 4 — Anti-ICP feature decline

> Thanks for the suggestion. {{specific feature}} is not on our roadmap.
>
> CoinScopeAI positions on capital preservation first, profit generation second. Features that integrate with signal-group products, copy-trade platforms, or leverage-maximization tools are anti-ICP for us — they don't fit how we want users trading with our system.
>
> What we do build for: regime-classified signals with explicit confidence + risk-gate enforcement. If that's the direction you're working in, here's the methodology page: [link]. If not, we're probably not the right fit, and that's fine.

### Canonical 5 — Sub-$5k disciplined inquiry

> Thanks for reaching out — and welcome.
>
> Free includes account verification, top-5 curated signals (15-min delayed), per-symbol regime labels, a demo-trade gate decision view, and full methodology documentation. There's no time limit on Free.
>
> Trader is the next step — it includes real-time signals, the configurable risk gate on your live account, the journal, and Telegram alerts. We position Trader as the destination when an account crosses the $5k threshold; that's the account size where the Trader-tier features start carrying their cost.
>
> If you want, opt into the "notify me when my account reaches $5k" subscription on the dashboard — we'll let you know when you're there. Until then, Free is yours.

### Canonical 6 — US user (region-block trip)

> Thanks for reaching out. CoinScopeAI is not currently available to US users.
>
> We're a UAE-based sole proprietorship with global English-language reach in MENA, Europe, and other markets. US availability is not on our roadmap at this time.
>
> If you'd like to be notified should our regional posture change, you can subscribe at [link]. Otherwise, no further action needed — your sign-up has been closed and any payment fully reversed.

---

## 8. Escalation execution

Per `03-ticket-routing-and-escalation-rules.md` §3, escalations follow named flows. Inbox SOP for triggering each:

### Escalation A — Vendor outage (per Su-5 active push)

When a vendor outage is detected (engine monitoring or via user ticket):

1. Open incident in `01-support-operating-model.md` §5 status-page tooling within 10 minutes.
2. Post canonical incident description to status page.
3. Trigger broadcast email to affected user segment.
4. Post Telegram alert if applicable.
5. Update status page every 30 min (P1) or 60 min (P2) until resolution.
6. Publish post-mortem within 7 days of resolution (per `03` §3).

### Escalation B — PCC v2 §8 question

1. Confirm question is in scope (real-capital, production-readiness, gate-pass status).
2. Send Canonical 1 verbatim.
3. If user follows up with substantive question (not addressable by canonical), escalate to founder personally for substantive reply.
4. Log follow-up volume; high follow-up volume = canonical 1 is insufficient and needs revision.

### Escalation C — Refund inside 14d window

1. Verify ticket is `BIL.REFUND_REQUEST_IN_WINDOW`.
2. Verify single-use anti-abuse: this is the user's first refund on this account.
3. Founder approval (Su-7 option a).
4. FinOps executes refund in Stripe within next coverage day (24h).
5. Send confirmation reply to user with refund-processed timestamp.
6. Log refund in monthly billing review.

### Escalation D — Refund outside 14d / abuse pattern

1. Verify out-of-window or abuse pattern (refund-resubscribe loop, ToS violation).
2. Send Canonical 3 verbatim.
3. If user disputes, escalate to founder for review.
4. If founder declines, send "appreciate your perspective; policy holds" follow-up; close ticket.
5. Log decline pattern; >5 declines per quarter = pricing/onboarding signal worth investigating.

### Escalation E — Regulatory / counsel flag

1. Flag ticket as `REG.*` per `04-user-issue-taxonomy.md`.
2. Founder responds with neutral acknowledgement (no policy commitments, no legal opinion).
3. Capture full ticket context + log to counsel-review file (Phase 4 trigger).
4. Counsel reviews quarterly; substantive cases get accelerated review.

### Escalation F — Persona-fit-failure (Su-7 anti-ICP retention)

1. Identify pattern: user demanding gate be turned off, complaining product enforces too much discipline, requesting features that violate §3.5 anti-ICP.
2. Founder sends Canonical 4 (anti-ICP decline) with personalized opening.
3. If user accepts: ticket closes, no churn-rescue attempt.
4. If user requests refund: process per Escalation C if in-window; per Canonical 3 if out-of-window.
5. Log pattern for §13 KPI: anti-ICP filtration rate.

---

## 9. Daily metrics tracked

Founder logs the following per coverage day; KPI dashboard (NEXT) consumes:

| Metric | Definition | Target |
|---|---|---|
| **Tickets received** | NEW count for the day | Trend metric |
| **First-response SLA hits** | % of NEW tickets receiving first-response within tier-appropriate window | ≥95% |
| **Tickets resolved on first response** | % of tickets moving NEW → RESOLVED in single reply | Target growth via deflection |
| **Tickets escalated to Eng / FinOps** | Count requiring cross-functional handoff | Trend metric |
| **P1 incident count** | Daily P1 ticket creation | Anti-target — should be near-zero |
| **Founder support time** | Self-reported time on inbox + escalations | <3 hrs/coverage day target; >5 hrs trigger investigation |
| **Auto-close count** | WAITING_USER → AUTO_CLOSED per day | Trend metric; high count = follow-up cadence broken |
| **Re-open count** | Resolved → re-opened by user reply | Trend metric; high count = first-response quality issue |

---

## 10. Failure modes specific to this workflow

- **Inbox check between scheduled blocks.** Founder breaks deep-work block to "just check support." Fragments product time. Discipline: P1 alerts page founder; everything else waits.
- **"Quick reply" without anti-overclaim audit.** Speed-trap. Even short replies run the §5 6-point check.
- **Template never updated.** Stale templates point to wrong policy or use outdated canonical phrasings. Quarterly template review is mandatory.
- **Canonical response modified ad-hoc.** Founder paraphrases Canonical 1 because "this user already knows the basics." Drift introduced. Canonical responses are verbatim or escalated, never paraphrased.
- **WAITING_USER tickets accumulating.** No follow-up cadence = ticket lost. Auto-close logic + 7-day retention is the safety valve.
- **Severity inflation.** Founder marks P3 as P2 to feel productive. KPI dashboard distorts. Severity is per the matrix.
- **Cross-function handoff dropped.** Ticket escalated to Eng; Eng forgets; user waits. Hand-off requires explicit ticket-state-change + Eng acknowledgement.
- **End-of-coverage-day inbox not closed.** Tickets in NEW state overnight = first-response SLA blown by morning. Closeout block is a hard stop.
- **Founder works support during weekend without monitoring trigger.** Slack creep — founder feels "always on." Discipline: weekend = best-effort P1 only. P2-P4 wait for Sunday morning.
- **No log of canonical-response usage.** If we don't track which canonical fired, we can't tell when to revise. Tag every send.

---

## 11. Workflow success criteria

The workflow is working when:

1. ≥95% of tickets meet first-response SLA per `02-support-sla-framework.md` §3.
2. Founder support time stays at <3 hrs/coverage day at 50–100 paid-customer scale.
3. Template coverage exceeds 60% of P3/P4 ticket volume by end of P1 Narrow Ship.
4. Canonical-response drift = zero (audit quarterly).
5. P1 incident comms hit status page within 10 minutes of detection.
6. Refund volume tracks 3–8% of new-paid-customers in 14d window.
7. No ticket sits in IN_PROGRESS > SLA window without escalation note.
8. KPI dashboard shows steady or improving deflection rate over time.

The workflow needs revision when:

- First-response SLA hit rate drops below 90% for 2 consecutive weeks (capacity issue or workflow drift).
- Auto-close rate exceeds 30% (follow-up cadence broken).
- Re-open rate exceeds 20% (first-response quality issue).
- Founder reports >5 hrs/coverage day for 1 week (capacity issue; **Su-3** trigger).
- Canonical-response drift detected (audit failure → retraining).

---

## 12. What this unlocks

- The 5 NOW SUPPORT deliverables form a complete day-1 operational system.
- `Help Center Structure` (NEXT) inherits the §6 deflection priorities as the KB article seed.
- `Standard Response Templates` (NEXT) inherits the §6 template categories + §7 canonical responses.
- `Billing Support Playbook` (NEXT) inherits Escalation C + D + Canonical 3 as base flow.
- `Exchange Connectivity Support Playbook` (NEXT) inherits Escalation A + the top-2 deflection priorities.
- `Support KPI Dashboard` (NEXT METRICS) consumes §9 daily metrics as the dashboard data model.
- ONBOARDING `_onboarding/05-friction-audit` P0 remediation backlog has explicit support coordination — items that ship with friction will produce inbound here.
- Phase 2 charter §4 SUPPORT exit criterion is met at draft-complete; lock requires the 7 Su-* decisions + REQUIRED INPUT items.
