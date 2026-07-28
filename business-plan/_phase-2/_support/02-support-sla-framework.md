# SUPPORT — Support SLA Framework

**Task:** `[DOC] SUPPORT — Support SLA Framework`
**Type:** NOW
**Owner:** Founder
**Status:** DRAFT v0.1 — per-tier × per-severity SLA matrix; refund SLA per tier resolves Pr2-5
**Anchored to:** `01-support-operating-model.md` coverage hours; PRICING `_pricing/02-pricing.md` Pr2-5; §6.7 refund policy; PCC v2 §8 incident criteria; §6.6 tier prices.
**Feeds decisions:** **Su-4**, locks input to **Pr2-5**.

---

## 1. SLA design philosophy

Three principles, derived from `_pricing/02-initial-pricing-philosophy.md` Principle 4 (predictable, anti-surprise) + Principle 7 (pricing page is a trust-load surface):

1. **Publish realistic SLAs, beat them consistently.** Inflated SLAs that get missed erode trust faster than honest SLAs that get met. Internal targets are ~30% tighter than published.
2. **Per-tier differentiation in resolution targets, not first-response.** Per **Su-4** option (a) — every paying customer (and Free user during coverage hours) gets prompt acknowledgement; resolution depth and prioritization differ by tier.
3. **Severity supersedes tier for safety-critical issues.** A Free user reporting a P1 incident (e.g., system showing wrong account balance, auth bypass risk) gets P1 response regardless of tier.

---

## 2. Severity matrix

Every ticket is assigned one of four severity levels at triage. Severity drives SLA, not tier alone.

| Severity | Definition | Examples |
|---|---|---|
| **P1 — Critical** | Real-capital risk, security/auth failure, data integrity at risk, full outage of core engine surface, vendor outage affecting majority of users | System showing incorrect balance; unauthorized account access suspected; full /scan or /risk-gate endpoint down; Binance outage rendering signals stale; demo gate decision returning wrong reasoning |
| **P2 — High** | Significant feature broken for tier; partial vendor outage; billing failure blocking conversion; refund within 14d window | Telegram bot not delivering alerts; Stripe payment processing failing; multi-account view broken on DP; user inside 14d refund window |
| **P3 — Standard** | Single-user feature issue, billing question, account/exchange-connection question, content-moderation, non-blocking confusion | "How do I read the regime label?"; "Where do I download my journal?"; per-seat invoicing question; password reset; single user's exchange API key issue |
| **P4 — Low** | Feature request, future-roadmap question, anti-ICP outreach, marketing-style inquiry, brand voice / copy feedback | "Will you add Bybit?" (already on roadmap); "Can you do crypto payments?"; partnership pitch; cosmetic feedback |

### Severity assignment rules

- **Default at triage:** P3 unless flagged by ticket content for higher severity.
- **Auto-escalation triggers:** any ticket mentioning "real money," "unauthorized access," "wrong balance," "missing funds," "executed without my permission" → auto-flag P1 for founder review (the user may be misunderstanding, but content drives initial severity).
- **Vendor-outage detection (engine monitoring):** auto-flag P1 if confirmed; auto-creates broadcast comms ticket.
- **Reclassification:** founder may re-classify after triage; reclassification logged.

---

## 3. SLA matrix — first-response (within coverage hours)

First-response = founder has acknowledged the ticket with a substantive reply (not just an auto-ack).

Per **Su-4** option (a) — first-response is uniform across tiers; severity drives the difference.

| Severity | First-response SLA (within coverage hours) | Out-of-coverage behavior |
|---|---|---|
| P1 | **<30 minutes from detection** | 24/7 — bypasses coverage hours; founder on-call via engine monitoring + status-page-driven alerts |
| P2 | **<4 hours from receipt** | Queued; first-response by [next coverage-window start + 4h] |
| P3 | **<24 hours from receipt** | Queued; first-response by [next coverage-window start + 24h] |
| P4 | **<72 hours from receipt** | Queued; first-response by [next coverage-window start + 72h] |

**Internal targets** (~30% tighter): P1 <20min, P2 <3h, P3 <16h, P4 <48h.

---

## 4. SLA matrix — resolution

Resolution = the user's reported issue is fully addressed (resolved, refunded, escalated to known fix ETA, or closed with explanation).

Per **Su-4** option (a) — resolution targets are tier-stratified, recognizing per-tier expectation differences and pricing-power asymmetry.

| Severity | Free | Trader ($79) | Desk Preview ($399) | Desk Full v2 ($1,199) |
|---|---|---|---|---|
| P1 | **<8 hours** | **<6 hours** | **<4 hours** | **<2 hours** |
| P2 | **<48 hours** | **<24 hours** | **<12 hours** | **<8 hours** |
| P3 | **<5 business days** | **<3 business days** | **<2 business days** | **<1 business day** |
| P4 | **Best-effort, no SLA** | **<10 business days** | **<7 business days** | **<5 business days** |

### Why these stratifications

- **P1 across tiers:** Free at 8 hours acknowledges Free is permanent (not a tier we can ignore in safety contexts); DF v2 at 2 hours acknowledges per-seat, partner-money obligation context.
- **P2 across tiers:** 6x ratio Free → DF v2 reflects feature-broken impact differential ($1,199/mo with multi-account view broken vs Free with delayed-feed broken).
- **P3 across tiers:** 5d → 1d ratio reflects accumulated standard-question backlog tolerance.
- **P4 across tiers:** Free has no SLA on feature requests (best-effort); paid tiers get response time.

### Resolution conditions

A ticket is "resolved" when one of:

1. The user-reported issue is fixed and confirmed by the user.
2. A workaround has been provided and the user accepts.
3. The issue is escalated to a known engineering fix with a published ETA, and the user has been informed.
4. The issue is identified as user-misunderstanding and explained, and the user has acknowledged.
5. The issue is non-actionable (e.g., feature request not on roadmap, anti-ICP request) and the user has been told with reason.
6. The user has been unresponsive for 7 days after the most recent founder reply requesting information.

---

## 5. Refund SLA per tier (resolves **Pr2-5**)

Per `_pricing/02-pricing.md` Pr2-5 — recommend uniform 14-day refund window per §6.7 with **tier-stratified processing time within the window**:

| Tier | Refund eligibility window | Processing time (founder-approved per case) |
|---|---|---|
| Free | N/A | N/A |
| Trader | 14 days from first-time payment | <3 business days from approval |
| Desk Preview | 14 days from first-time payment | <2 business days from approval |
| Desk Full v2 | 14 days from first-time payment + tier-specific carve-out: first 30 days, any added partner/analyst seat is refundable on removal | <1 business day from approval; seat-removal refund <12 hours |
| Per-seat (any tier) | First-time-seat-add: 14 days | <2 business days |

### Recommended Pr2-5 lock: option (c) — uniform 14d eligibility, with DF v2 first-30-days seat-return carve-out

**Why (c) over (a) uniform 14d:** DF v2 customers add seats in trial-and-error patterns (test partner workflow with one seat, decide to remove). 14d window for seat-removal is tight given partner onboarding is multi-week; 30-day seat-return window for first 30 days reduces friction without opening abuse vector.

**Why (c) over (b) tier-tiered eligibility (e.g., 14d Trader, 30d DP/DF):** asymmetric eligibility windows are a refund-policy complication; abuse pattern: subscribe DF, downgrade to Trader, claim "I was promised 30d" — explicit per-tier eligibility creates this dispute. Uniform 14d + DF-specific seat carve-out is cleaner.

### Refund authorization (per **Su-7** option a — founder-approved)

- All refunds founder-approved at v1 to learn the patterns.
- Anti-abuse: per §6.7, max 1 refund per account lifetime. Stripe-side flag enforced.
- Anti-abuse: refund-then-resubscribe-within-90-days = no second refund window (per §6.7 reactivation policy).
- Phase 3 evaluation: self-serve in-product refund within 14d window once abuse patterns are characterized.

---

## 6. Coverage-hour adjustments + holidays

### Coverage hours (per `01-support-operating-model.md` §2)

| Day | Coverage |
|---|---|
| Sun-Thu | 09:00–15:00 GMT+4 |
| Fri-Sat | P1 only |

### Holiday handling

- **UAE national holidays:** observed; published in advance on status page + dashboard banner ≥7 days before.
- **Holiday-impact SLA:** P1 unchanged (24/7); P2/P3/P4 SLAs extend by holiday-day count.
- **Holiday auto-ack:** "Received during UAE national holiday observance. Standard coverage resumes [date + time]. P1 incidents covered."

### Out-of-coverage auto-ack (canonical)

For out-of-coverage tickets:

```
Subject: Received: [original subject]

Your message reached us outside our standard support hours 
(Sun–Thu 09:00–15:00 GMT+4 / UAE).

We'll respond by [computed: next coverage window start + applicable SLA window].

If this is a P1 incident (real-capital risk, security/auth failure, full outage), 
mark the message [P1] in the subject and we'll page on-call.

— CoinScopeAI Support
```

### P1 escalation path out of coverage

- Engine monitoring auto-trigger on detected outage → status page update + email broadcast + founder paged via [REQUIRED INPUT — confirm paging tooling: PagerDuty? Phone? Telegram?].
- User-flagged P1 in subject line → email parsing routes to founder-pager.
- Status page is the authoritative "is the system up" reference; users should check it before submitting P1 tickets.

---

## 7. SLA enforcement + measurement

### Measurement

Per `Support KPI Dashboard` (NEXT METRICS):

| KPI | Definition | Target | Falsifier |
|---|---|---|---|
| First-response SLA hit rate | % of tickets where first-response landed within published SLA | ≥95% | <85% triggers Su-1 / Su-3 reopen |
| Resolution SLA hit rate | % of tickets where resolution landed within published per-tier SLA | ≥90% | <75% triggers Su-1 / Su-8 reopen |
| Median first-response time | per severity | per internal target (~30% tighter than published) | sustained miss = SLA inflation risk |
| Per-tier resolution time distribution | p50 / p90 / p99 per tier per severity | meets targets at p90 | p99 outliers = process gap |
| P1 detection-to-comms time | time from engine-monitoring P1 alert to status-page update | <10 min | >15 min = monitoring/comms gap |

### Enforcement

- SLA misses logged in dashboard.
- Sustained miss (3+ weeks of <95% first-response or <90% resolution) triggers Su-1 / Su-3 / Su-8 reopen.
- Single P1 miss (>30 min first-response or >SLA resolution) triggers immediate post-mortem within 7 days.
- Customer-facing apology + remediation only for SLA-missed tickets where the user notices; no proactive apology for internal-target miss.

### Customer-facing visibility

- Published SLA on `coinscope.ai/support-sla` (or equivalent).
- KPI summary published quarterly on status-page or `coinscope.ai/operations` (REQUIRED INPUT — confirm willingness to publish quarterly support metrics).

---

## 8. Per-tier signals embedded in SLA

The SLA framework is itself a packaging signal. The differences below are intentional and load-bearing for tier perception:

| Signal | Free | Trader | DP | DF v2 |
|---|---|---|---|---|
| P1 resolution speed | 8h | 6h | 4h | 2h |
| P3 resolution speed | 5d | 3d | 2d | 1d |
| Refund processing speed (within window) | N/A | 3d | 2d | 1d |
| First-response speed (uniform) | per severity | per severity | per severity | per severity |
| P4 SLA exists | No | 10d | 7d | 5d |
| Status-page transparency | Same | Same | Same | Same |

The single "uniform first-response" combined with "tier-stratified resolution" is the explicit design — every customer is acknowledged promptly; resolution priority reflects pricing-power asymmetry.

---

## 9. Failure modes specific to SLA design

- **Inflating published SLA to look impressive.** "Free P1 resolution <2 hours" sounds good, won't be met at v1. Trust-cost > marketing-benefit. Hold realistic targets.
- **Missing P1 on Free.** A Free user reporting a real-capital risk is an existential trust event. P1 across all tiers, no exceptions.
- **DF v2 SLA missed silently.** $1,199/mo + per-seat customer expects differentiated response; missed SLA = packaging integrity broken. Per-tier KPI tracking required.
- **Refund SLA undefined per tier.** This was the Phase 2 Pr2-5 deferral. Fixed here at uniform 14d eligibility + tier-stratified processing + DF carve-out.
- **Out-of-coverage P1 missed because monitoring wasn't tripped.** Engine monitoring must reliably detect outage classes without relying on user reports. REQUIRED INPUT — Eng confirm monitoring coverage.
- **Holiday SLA extension claimed but not communicated.** UAE national holidays are knowable in advance; auto-extend SLAs + publish advance notice.
- **Quarterly KPI publication promised then abandoned.** Per `_pricing/02` Principle 7 — pricing-page-area surfaces are trust load. If we promise quarterly metrics, we publish them.
- **First-response uniform but acknowledgement quality drops at scale.** "Acknowledged" template-only first-response = ack ≠ substantive. Must be a substantive reply that engages with the ticket's content.

---

## 10. What this unlocks

- **Su-4** can be marked recommended at "uniform first-response, tier-stratified resolution."
- **Pr2-5** can be marked recommended at "uniform 14-day refund window + tier-stratified processing time + DF v2 first-30-days seat-return carve-out."
- `03-ticket-routing-and-escalation-rules.md` consumes severity matrix as routing input.
- `04-user-issue-taxonomy.md` consumes severity matrix as default-severity-per-category assignment.
- `05-support-inbox-and-response-workflow.md` consumes coverage hours + auto-ack copy + P1 escalation path.
- `Support KPI Dashboard` (NEXT) has the canonical KPI definitions + targets + falsifiers.
- `Billing Support Playbook` (NEXT) consumes refund SLA + authorization rule.
- Pricing-page footer has SLA copy block to render publicly.
- Phase 2 charter §4 SUPPORT exit criterion has explicit SLA published-form requirement met.
