# Weekly Business Review — Template

## Purpose

A 30–45 minute weekly review that surfaces the week's signal, decisions, and blockers. It is not a status update; it is **the place where the week's data forces or refuses to force action.**

The review is small by design. If it grows past 45 minutes regularly, the template is wrong, not the meeting.

## Cadence and participants

- **Cadence:** weekly, same day, same time. Recommended: Monday morning (review prior week) or Friday afternoon (review current week).
- **Participants (P0–P1):** Founder solo, with a written log shared into Notion / decision register.
- **Participants (P2+):** Founder + Trust Ops + Engineering contractor, async-first review with a 30-min sync.
- **Format:** the template below is filled in *before* the live discussion (or solo log). The discussion is for triggers and decisions only, not for filling the template.

## Required data inputs (gathered before the review)

The following are **must-haves** every week. If any are missing, the review is incomplete and a recurring task should be created to fix the data pipeline.

| Input | Source | Owner |
|---|---|---|
| Free signups, activation rate, day-7 retention (prior week) | Product analytics | Founder |
| Paid signups, churn events, refund events (prior week) | Stripe | Founder |
| Incident log (count, severity, MTTA, MTTR) | Incident tracker | Founder / Trust Ops |
| Support ticket volume, TTFR, gate-confusion tag count | Support tool | Founder / Trust Ops |
| Kill-switch trips, gate-decline rate, override events | Engine logs | Founder / Engineering |
| PCC v2 gate state, days since last transition | Engineering log | Founder / Engineering |
| Vendor cost weekly delta, top-3 concentration | Bills + connector-health | Founder |
| Connector-health artifact snapshot | `coinscope-connector-health` Cowork artifact | Founder |
| North-Star Metric (VCE in P0, TRAS from P1) | Product analytics | Founder |

If a metric isn't in this list, it doesn't belong in the weekly review.

---

## Template

> **Week of:** _YYYY-MM-DD_  
> **Phase:** _P0 / P1 / P2 / P3 / P5_  
> **Reviewer(s):** _name(s)_  
> **PCC v2 gate state:** _G1 / G2 / G3 / G4 / §8 Capital Cap status_  
> **Real-capital authorization:** _N (default) / Y (with date and decision-log link)_

### 1. North-Star Metric

| | Value | WoW delta | Notes |
|---|---|---|---|
| NSM (VCE or TRAS) | _value_ | _+/−_ | _trend interpretation in 1 sentence_ |
| NSM as % of paid (TRAS only) | _%_ | _+/−_ | _quality signal_ |

**Question:** Did the NSM move for a reason we understand? If no, that's the first investigation.

### 2. Growth + Activation

| Metric | This week | Last week | Trend | Notes |
|---|---|---|---|---|
| Free signups | | | | |
| Activation rate (D7) | | | | |
| Free → Trader upgrades | | | | |
| Paid signups (P1+) | | | | |
| Tier mix shift | | | | |

**Trigger:** if activation rate drops >5pp WoW with no product change, investigate before next review.

### 3. Retention + Refunds

| Metric | This week | Trailing 4w avg | Trend | Notes |
|---|---|---|---|---|
| Trader monthly churn (rolling 30d) | | | | |
| Refund events (count, $) | | | | |
| Refund rate (% MRR) | | | | |
| Reactivations | | | | |

**Trigger:** any single refund event with `incident-related` tag → triage with `13-support-and-trust-ops` runbook before next review.

### 4. Trust + Support

| Metric | This week | Notes |
|---|---|---|
| Incidents (P1 / P2 / P3) | | |
| MTTA (P1) | | |
| Support tickets (volume) | | |
| TTFR (median) | | |
| Gate-confusion tagged tickets | | |
| User-reported product confusion | | |
| Public trust events | | |

**Trigger:** any P1 incident → mandatory short postmortem section in this review (§9). Any public trust event → escalate to monthly exec review immediately.

### 5. Risk + Safeguards

| Metric | This week | Notes |
|---|---|---|
| Kill-switch trips (count + reasons) | | |
| Gate-decline rate | | |
| Override events (count, who, why) | | |
| Drawdown breach events | | |
| Engine rollbacks | | |
| Days since last PCC gate transition | | |

**Trigger:** any backward gate movement → freeze monetization decisions, escalate to monthly exec review immediately.

### 6. Financial + Vendor

| Metric | This week | Notes |
|---|---|---|
| MRR (P1+) | | |
| Vendor cost (weekly run-rate) | | |
| Vendor concentration top-3 | | |
| LLM cost / active user | | |
| Cash runway (months) | | |
| Founder hours (build / support / ops / GTM) | | |

**Trigger:** any vendor budget hitting 80% threshold mid-week → investigate before week-end. Cash runway dropping below 9 months → exec discussion.

### 7. Operations + Connector Health

| Metric | This week | Notes |
|---|---|---|
| Connector-health % | | |
| Deploy count | | |
| Deploy failures | | |
| Backup verification last test | | |
| Open ops blockers | | |

**Trigger:** connector-health <100% → fix before next review or document why deferred.

### 8. Blockers and decisions this week

- **Blockers:** _list, with what's needed to unblock_
- **Decisions made this week:** _bullet list, log links_
- **Decisions deferred to monthly:** _list with reason_

### 9. Postmortem (only if a P1 incident occurred)

- **What happened (one paragraph, factual):**
- **What the gate / kill-switch / runbook did vs should have done:**
- **User impact:**
- **Public-facing communication required? Y/N — if Y, status:**
- **Follow-up tasks created (use `[TYPE] [AREA] — Action / Deliverable`):**

### 10. Open questions for the monthly exec review

- _List items that need leadership-level discussion, decision authority, or cross-folder dependency resolution._

---

## What must trigger action (summary)

The review is the place where these conditions force a decision:

1. **NSM drops with no understood cause** → investigation task before next review.
2. **Activation rate drops >5pp WoW** → investigation task before next review.
3. **Any P1 incident** → §9 postmortem this week.
4. **Any public trust event** → escalate to monthly exec immediately.
5. **Backward PCC v2 gate movement** → freeze monetization changes; escalate.
6. **Vendor budget breach** (80%+) → mid-week investigation.
7. **Cash runway <9 months** → exec-level discussion this month.
8. **Connector-health <100%** → fix or document deferral with reason.
9. **Refund event with incident tag** → triage runbook before next review.
10. **Any backward override / kill-switch override** → review with engineering before next deploy.

If none of those triggers fire, the review can be a 20-minute scan. The discipline is consistency, not length.

## Anti-patterns (avoid)

- Filling the template with green checkmarks because nothing went wrong. **Note exceptions only.**
- Letting the review become a status update for a stakeholder. It is an internal forcing function.
- Adding more KPIs because a row is empty. Empty rows are fine.
- Optimizing for the prettiest dashboard. The dashboard is a side effect, not the goal.
- Skipping the review during incident-heavy weeks. *Especially* don't skip then.

## When the template needs to evolve

Update this template (and log in `21-decision-log`) when:

- A phase transition occurs (P0→P1, etc.).
- The NSM definition is locked or revised.
- A new role takes over a KPI block (e.g. Trust Ops contractor at P2).
- An incident class repeatedly fails to surface in the review — meaning the inputs are wrong.
- A KPI is consistently green for 90+ days — likely deferred or removed.
