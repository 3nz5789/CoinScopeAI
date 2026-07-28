# Monthly Executive Review — Template

## Purpose

A monthly review that does what the weekly review cannot: **see the trend, not the data point**. Decide what stays, what goes, what changes posture. This is the meeting where roadmap, hiring, pricing, and risk-posture decisions are made or formally deferred.

## Cadence and participants

- **Cadence:** monthly, last week of the month, 90 minutes.
- **Participants (P0–P1):** Founder solo with written log committed to Notion `21-decision-log`. Optional: one trusted advisor.
- **Participants (P2+):** Founder + Trust Ops + Engineering contractor + (when activated) advisors / first hires.
- **Format:** review pack assembled before the meeting; the meeting is for **decisions and disagreements**, not for filling the template.

## Required inputs (assembled in advance)

- Last 4 weekly review logs.
- Current month's NSM trend chart (4–8 weeks).
- KPI map (`kpi-map.md`) populated with month-end values.
- Financial assumptions table (`15-financial-framework/financial-assumptions.md`) — flag any assumption whose risk grade changed.
- Decision-log delta (`21-decision-log`) — what was opened, decided, deferred this month.
- Roadmap (`18-roadmap`) — current phase, milestones, slippage notes.
- Top 5 open risks from `14-risk-compliance-and-safeguards`.
- Latest Production Candidate Criteria v2 status (G1–G4 + §8 Capital Cap).

---

## Template

> **Month of:** _YYYY-MM_  
> **Phase:** _P0 / P1 / P2 / P3 / P5_  
> **Reviewer(s):** _name(s)_  
> **PCC v2 gate state:** _G1 / G2 / G3 / G4 + §8 Capital Cap status_  
> **Real-capital authorization:** _N (default) / Y (with date and decision-log link)_

### 1. NSM and Quality-of-Growth

| | Month-end | M-1 | M-3 trend | Notes |
|---|---|---|---|---|
| NSM (VCE or TRAS) | | | | |
| NSM as % of paid (TRAS only, P1+) | | | | |
| New cohort time-to-NSM-eligibility | | | | |

**Headline question:** Is growth this month *trust-aligned*? If NSM rises only because of headline signups, that is a quality-of-growth red flag, not a green light.

### 2. Business health by category

For each category, mark **🟢 / 🟡 / 🔴** with one sentence justification.

| Category | Status | One-line justification |
|---|---|---|
| Growth | | |
| Activation | | |
| Retention | | |
| Trust posture | | |
| Risk + safeguards | | |
| Support quality | | |
| Operational readiness | | |
| Financial discipline | | |

**Rule:** No category may be silently green. Every green requires a sentence. Yellows and reds require an action item or an explicit "monitor only" decision.

### 3. KPI deep-dive — what changed this month

Pick the **3–5 KPIs** that moved most meaningfully. For each:

- Metric, value, M-o-M delta.
- What we think caused the move.
- Whether the cause is a one-off, a trend, or a structural change.
- Action: keep watching / investigate / commit.

### 4. Financial review

| | Value | M-o-M | Notes |
|---|---|---|---|
| MRR (P1+) | | | |
| ARPU by tier | | | |
| Refund rate | | | |
| Vendor cost ($) | | | |
| Vendor cost / MRR | | | |
| LLM cost / active user | | | |
| Cash burn (month) | | | |
| Cash runway (months) | | | |

**Mandatory checks:**

- Any assumption in `financial-assumptions.md` invalidated this month? List + log.
- Any vendor cost line change >10%? Triage.
- Any refund event uncovered after weekly review? Backfill + investigate root cause.
- Founder time category breakdown — does it match priorities?

### 5. Roadmap review

- **Current phase:** _P0/P1/P2/P3/P5_
- **Active milestones:** _list_
- **Milestones completed this month:** _list_
- **Milestones slipped this month:** _list, with revised dates_
- **Phase transition criteria status:** _which gates are met, which are pending_

**Headline question:** Has the phase transition date moved? If yes — does it affect SKU activation, monetization timing, or hiring decisions? Cross-ref `15-financial-framework`.

### 6. Trust and risk review

This section is **mandatory and non-summarizable**. It must list specifics, not just status colors.

- **Incidents this month** (count by severity, with one-line summary each).
- **Engine rollbacks this month** (count + reason).
- **Kill-switch trips** (notable trips with explanation).
- **Override events** (count, distribution across users, any user with above-threshold override rate).
- **Public trust events** (count, response posture, current state).
- **Drawdown breach events** (count, average severity).
- **Vendor outages affecting users** (count, total minutes, fail-soft behavior).
- **Compliance / legal items opened or closed this month.**

**Output:** any items requiring leadership-level decision get logged in §9 below.

### 7. PCC v2 + §8 Capital Cap review

| Gate | Status M-o-M | Days in current state | Notes |
|---|---|---|---|
| G1 | | | |
| G2 | | | |
| G3 | | | |
| G4 | | | |
| §8 Capital Cap | | | |

**Headline question:** Is the gate progression on the trajectory implied by the roadmap? If a gate has moved backward, mandatory escalation in §9 below.

### 8. Decision-log update

- **Decisions made this month** (link to each).
- **Decisions deferred** (with reason and re-review date).
- **Decisions reopened** (with what changed).
- **Top 3 open decisions blocking next month** (cross-ref `21-decision-log`).

### 9. Leadership decisions and escalations

Items that require explicit leadership decision now:

- _List with options, recommendation, and decision target date._

Items escalated from §6 (trust/risk) or §7 (PCC):

- _List._

### 10. What changed this month — summary log

A short paragraph (3–5 sentences) capturing the month in plain language. This is the entry that goes into `01-executive-summary` if external communication is needed.

### 11. Forward-looking — what we expect next month

- **Top 3 priorities for next month:** _list, in order._
- **Top 3 risks for next month:** _list, with mitigations._
- **What would make this month a failure:** _one sentence — used as the ex-ante litmus test._

---

## Key questions leadership should answer monthly

These are the questions that, if answered honestly, surface the things a KPI dashboard alone cannot:

1. **Is the NSM moving for the right reason?**  
   If NSM rose because activation improved, that is durable. If it rose because of a one-time signup wave, that is fragile.

2. **Did any green KPI hide a degrading sub-metric?**  
   E.g. retention green while gate-confusion tickets rose 30%.

3. **Has any assumption in the financial framework been invalidated?**  
   If yes, what downstream models or commitments need to be rewritten?

4. **Has the PCC v2 gate state moved forward, stalled, or moved backward?**  
   Stalled or backward changes require explicit decision treatment.

5. **Did we have any incident, refund, or trust event whose root cause is still unclear?**  
   Unclear root causes are the highest-risk debt the company is carrying.

6. **What did founder time get spent on this month, and is that consistent with the priorities we set last month?**  
   This is the cheapest way to detect drift.

7. **What decisions did we defer — and is the reason for deferral still valid?**  
   Deferred decisions silently accumulate risk.

8. **What would we do differently if we re-ran this month with full information?**  
   The single most useful retrospective question.

9. **Is there any pressure (sales, revenue, advisor, founder ego) that wants to pull a phase transition forward?**  
   If yes, name it explicitly and check it against PCC criteria.

10. **What is the one thing that, if it broke next month, would hurt most?**  
    This becomes a top-3 risk in §11.

## What should change month-to-month (and what shouldn't)

**Should change:**

- The 3–5 KPIs in the deep-dive (§3) — the most-moved metrics, not a fixed list.
- Top priorities (§11) — these are the operating output of the review.
- Risk list (§11) — risks evolve as the product evolves.
- Specific incidents and root causes (§6).

**Should NOT change** (without an explicit decision-log entry):

- The North-Star Metric definition.
- The 8 business-health categories (§2).
- The list of mandatory financial checks (§4).
- The structure of the trust/risk section (§6).
- The set of 10 leadership questions above.

If the structure itself is changing every month, the framework is unstable, not the business.

## Anti-patterns (avoid)

- **All-green months.** A month where everything is fine and there's nothing to improve is almost certainly a month where the leading indicators weren't read carefully.
- **Roadmap optimism.** Don't move milestone dates forward without a corresponding gate transition. Don't defer dates silently.
- **Trust-section abbreviation.** §6 is the section that distinguishes a trust-sensitive product's review from a generic one. Cutting it short is the single most common mistake.
- **Decision laundering.** A decision that quietly changes between weekly reviews without being logged in `21-decision-log` is a trust-debt event in itself.
- **Reporting voice.** This template is internal. Don't write it for a future investor reader; write it for the founder's future-self decision-making.
