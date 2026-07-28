# Operating Cadence

## 1. Why a cadence is the operating system

The CoinScopeAI cadence has one job: **make sure the right things get reviewed, decided, and logged on a schedule that survives incident weeks.** Cadence beats willpower. A trust-sensitive product cannot rely on the founder remembering to think about trust posture this week.

The cadence below is sized for current stage (founder + occasional contractors). Rhythms scale — they don't multiply — as the team grows.

## 2. The cadence layers

| Layer | Frequency | Time investment | Output |
|---|---|---|---|
| **Daily** | Every business day | 10–20 min | Inbox/incident sweep + day-shape |
| **Weekly review** | Once / week | 30–45 min | `weekly-review-template.md` filled in |
| **Monthly exec review** | Once / month | 90 min | `monthly-exec-review-template.md` filled in + decisions logged |
| **Phase-transition review** | Per phase boundary (P0→P1, etc.) | Half day | Decision-log refresh + PCC gate audit |
| **Quarterly strategy** | Once / quarter | 1 day | Roadmap revision + strategic-priority refresh |

That's it. Five layers. Anything else is optional.

## 3. Daily cadence

Not a meeting. A 10–20 minute solo discipline.

| Time | What |
|---|---|
| First 5 min | Connector-health artifact glance + incident inbox |
| Next 5 min | Support queue glance (TTFR, any P1/P2 tickets) |
| Next 5 min | Engine logs glance (kill-switch trips, gate-decline shape) |
| Optional | Ship-of-the-day or write-of-the-day intent |

**Triggers that interrupt daily cadence:**

- Any P1 incident → switch to incident runbook.
- Any kill-switch trip with unexplained reason → investigate before normal work.
- Any vendor budget at 80%+ alarm → investigate same-day.
- Any external trust event → response posture before normal work.

**What's NOT in daily cadence:**

- Email triage as a discipline (handle email when you handle email; not a ritual).
- Standups for self.
- KPI reviews (those are weekly).
- Roadmap edits (those are monthly+).

## 4. Weekly cadence

Anchored on the `weekly-review-template.md` from `16-kpi-okr-system`.

**When:** Same day, same time, every week. Recommended: Monday morning (review prior week) OR Friday afternoon (review current week). Pick one and stick with it.

**Duration:** 30–45 minutes.

**Participants:**

- P0–P1: Founder solo, with shared written log.
- P2+: Founder + Trust Ops contractor + Engineering contractor (async-first; 30-min sync if needed).

**Required pre-work (before the live discussion):**

- Pull all KPI data per `weekly-review-template.md` §"Required data inputs."
- Fill in the template *before* the live segment.
- Note any triggers from `weekly-review-template.md` §"What must trigger action."

**Live segment (when it happens):**

- 5 min — NSM trend and any "for the right reason?" check.
- 10 min — exceptions only (yellows, reds, triggers fired).
- 10 min — blockers and decisions.
- 5 min — postmortem (if any P1 incident).
- 5 min — open questions for the monthly review.

**Post-review action:**

- Decisions made → log in `21-decision-log`.
- Tasks created → use `[TYPE] [AREA] — Action / Deliverable` format.
- Deferred items → noted with reason.

**Anti-pattern:** filling the template with green checkmarks. Note exceptions only. Empty rows are fine.

## 5. Monthly cadence

Anchored on `monthly-exec-review-template.md`.

**When:** Last week of the month. Recommended: same day-of-week each month (e.g., last Friday).

**Duration:** 90 minutes.

**Participants:**

- P0–P1: Founder, optionally + advisor.
- P2+: Founder + Trust Ops + Engineering contractor + advisor.

**Required pre-work (assembled in advance):**

- Last 4 weekly reviews compiled.
- KPI map populated with month-end values.
- Financial assumptions table reviewed for invalidations.
- Decision-log delta for the month.
- Roadmap status with any slippage notes.
- Top 5 open risks.
- PCC v2 gate status snapshot.

**Live segment structure:** see `monthly-exec-review-template.md` — 11 numbered sections, with the trust + risk section (§6) explicitly non-summarizable.

**Post-review action:**

- Top 3 priorities for next month → these are the operating output of the review.
- Decisions made → logged.
- Decisions deferred → with reason and re-review date.
- One-paragraph "what changed this month" summary → goes into `01-executive-summary` if external comms needed.

## 6. Planning rhythm

Planning is not a separate cadence; it is the **output** of monthly and phase-transition reviews.

| Planning horizon | Where it gets done |
|---|---|
| Next week | Output of the weekly review |
| Next month | Output of the monthly exec review |
| Next phase | Output of the phase-transition review |
| Next quarter | Output of the quarterly strategy review |

There is no separate "planning meeting." Planning emerges from review. This avoids the failure mode where planning meetings exist independent of data and produce wishful priorities.

## 7. KPI review rhythm

| Cadence | KPI focus |
|---|---|
| Weekly | All metrics in `kpi-map.md` filtered to the active phase + trigger checks |
| Monthly | NSM trend, quality-of-growth questions, KPI deep-dive on 3–5 most-moved metrics |
| Phase-transition | Full KPI map audit — which KPIs activate, which deprecate, which deferred metrics become live |
| Quarterly | NSM definition review (only revise with explicit decision-log entry) |

**Rule:** KPI definitions are not changed inside a weekly or monthly cycle. Definition changes happen only at phase-transition or quarterly cadence, and only via explicit decision-log entry. This prevents the failure mode of redefining a KPI to flatter a quarter.

## 8. Incident and risk review rhythm

| Cadence | Scope |
|---|---|
| Real-time | P1 incidents trigger immediate runbook (cross-ref `13-support-and-trust-ops`); not part of cadence |
| Within the week | Postmortem section in the weekly review for any P1 incident |
| Monthly | Incident pattern review + trust/risk section §6 of monthly exec |
| Phase-transition | Risk register full audit — which risks have evolved, which are retired, which are new |

**Specific triggers that escalate immediately (not held for next review):**

- Any backward PCC v2 gate transition.
- Any kill-switch trip with unexplained reason.
- Any public-facing trust event.
- Any vendor outage with paid-customer impact.
- Any refund event tagged `incident-related`.

The principle: **trust-relevant signals are escalated in the moment; KPI signals can wait for the next review.** Treating them with the same priority is how trust posture quietly degrades.

## 9. Roadmap review rhythm

| Cadence | Action |
|---|---|
| Weekly | Slippage check: did any milestone move? Note in weekly review §8 |
| Monthly | Full roadmap section in `monthly-exec-review-template.md` §5 |
| Phase-transition | Roadmap re-baseline: confirm phase exit criteria met before declaring transition |
| Quarterly | Strategic horizon review — what's still on the roadmap that shouldn't be, what's missing |

**Roadmap discipline:** dates only move backward, not forward, except at phase transitions or with explicit decision-log entry. Pulling milestones forward to chase revenue is the single most likely way the financial framework becomes a fiction (cross-ref `15-financial-framework`).

## 10. Documentation and update rhythm

| Cadence | Action |
|---|---|
| Per decision | Log in `21-decision-log` immediately |
| Weekly | Update KPI map values; refresh connector-health artifact |
| Monthly | Refresh assumption table in `15-financial-framework`; update KPI ownership if a role activated |
| Phase-transition | Refresh every business-plan README; refresh `02-company-overview` operating posture |
| Quarterly | Memory consolidation pass (cross-ref `consolidate-memory` skill); audit all open questions in every README |

**Rule:** documentation is the operating record, not an afterthought. A decision that wasn't logged in `21-decision-log` was not made — it was guessed. This rule survives the team scaling.

## 11. Leadership sync recommendations

At current stage there is no "leadership team." There is the founder. The relevant syncs are:

| Sync | Purpose | Cadence |
|---|---|---|
| Founder solo review | The weekly + monthly cadence above | Weekly + monthly |
| Founder + advisor (if active) | Strategic check-in, outside perspective | Monthly |
| Founder + Trust Ops contractor (when active) | Support metrics, incident review, KB updates | Weekly async; monthly sync |
| Founder + Engineering contractor (when active) | Project SOW progress, vendor-integration risk | Weekly async; ad-hoc sync per milestone |
| Founder + bookkeeping contractor | Monthly reconciliation | Monthly async; rare sync |
| Founder + external counsel | Quarterly review + ad-hoc per legal trigger | Quarterly + ad-hoc |

**No standing all-hands.** With this team size, all-hands meetings consume time without producing decisions. Async written communication is the default.

## 12. What must happen reliably (non-negotiable)

These rituals must occur even during incident weeks, even during travel, even when the founder is overloaded:

1. **Weekly review filled in.** May be abbreviated; cannot be skipped.
2. **Connector-health artifact glance.** Daily, every business day.
3. **Incident logging.** Every P1/P2 logged in real time.
4. **Decision logging.** Every material decision into `21-decision-log` within 48 hours.
5. **Monthly exec review.** May be deferred by ≤7 days; cannot be skipped for a calendar month.
6. **PCC v2 gate state check.** Whenever a deployment touches the engine or a risk threshold.
7. **§8 Capital Cap status.** Reviewed at every monthly cadence; firm default is "capped."

Skipping any of the above is itself a process incident and gets logged.

## 13. What is optional / can flex

- Daily cadence on weekends and holidays — flex freely.
- Advisor monthly call — flex by ±2 weeks if needed.
- Engineering contractor weekly sync — replaceable by async if no blockers.
- Quarterly strategy day — combinable with phase-transition review when they fall close together.
- Documentation polish (versus capture) — capture is required; polish is optional.

## 14. Cadence as a sustainability discipline

The point of the cadence is not coverage. The point is to make CoinScopeAI **sustainable** — runnable for years, not just months. Three rules support that:

1. **Sized for the current team.** A cadence designed for 10 people will collapse under a team of 1.
2. **Survives incidents.** If a cadence requires perfect conditions, it will not survive the first bad week.
3. **Forces trust to be reviewed at the same cadence as growth.** This is the single most important property — the one that a trust-sensitive product cannot afford to drop.

If any cadence layer becomes more burden than benefit for ≥2 consecutive months, log it in `21-decision-log` and revise. Cadence is a tool; it is not sacred.
