# North-Star Metric

## 1. What a North-Star Metric is for here

A North-Star Metric (NSM) is the **single number** the company is willing to be judged by quarter-over-quarter. It is not the only metric — it is the one whose movement most reliably indicates that the business is working **as intended**, with all of CoinScopeAI's intent (capital preservation + trust + revenue) included.

For a trust-sensitive trading product, the NSM must satisfy four tests:

1. **Aligns with capital-preservation default.** It cannot be a metric that rises when users override the Risk Gate or take excessive leverage.
2. **Resists vanity inflation.** Cannot be gamed by signups, free signups, or one-off paid campaigns.
3. **Is observable at the current stage.** Must produce a non-zero reading in P0–P1, not require P5 to be meaningful.
4. **Compresses the most failure modes into one number.** Trust degradation, churn, refund waves, and incident frequency should all show up.

## 2. Candidate NSMs

### Option A — Monthly Recurring Revenue (MRR)

| Pro | Con |
|---|---|
| Universally understood. | Hostile to capital-preservation: a refund wave from an incident can hide behind a single big monthly signup. |
| Direct to fundraising narrative. | Has near-zero signal at P0 (no paying users), and fragile signal at P1. |
| | Rewards growth without weighting trust quality. |

**Verdict:** wrong NSM at our stage. Tracked as a first-class lagging KPI in `kpi-map.md`, not as the NSM.

### Option B — Weekly Active Users (WAU)

| Pro | Con |
|---|---|
| Easy to compute, low instrumentation overhead. | Vanity metric — high WAU with degraded trust is exactly the failure mode we're trying to avoid. |
| Smooths over single-day volatility. | Doesn't distinguish gate-aligned use from override-heavy use. |
| | Weighted equally for free vs paying, which doesn't reflect commercial intent. |

**Verdict:** rejected as NSM.

### Option C — Activated Paying Users

| Pro | Con |
|---|---|
| Filters out signups that never engaged. | Still doesn't weight gate-aligned vs override-heavy behavior. |
| Aligned with conversion thesis. | Empty in P0 (no paying users); awkward through P1 ramp. |

**Verdict:** strong, but doesn't yet capture trust dimension.

### Option D — Trust-Retained Active Subscribers (TRAS) — RECOMMENDED

Defined as: **paid subscribers (Trader / Desk Preview / Desk Full v2) who are simultaneously past day 30 of paid use, have not initiated a refund, have completed ≥N gate-aware sessions in the trailing 30 days, AND have an override rate below a defined threshold.**

| Pro | Con |
|---|---|
| Captures revenue, retention, AND trust posture in one number. | Higher instrumentation cost than MRR alone (need session, gate-decline, override telemetry). |
| Cannot be inflated by free signups or one-off marketing pushes. | Empty at P0 (validation cohort, no paid). Needs a stage-aware sibling metric. |
| Penalizes both incidents (refunds) and trust drift (override rate, dormancy). | Definition has knobs (N sessions, override threshold) — must be locked once and not tweaked to chase a number. |
| Forces revenue and trust discipline to compete for the same headline. | Requires honest cancellation reason capture to be fully meaningful. |

**Verdict:** strongest NSM for CoinScopeAI's stated mission and stage.

### Option E — Validated Cohort Engagement (VCE) — for P0 ONLY

Used during P0 validation phase (no paying users by design). Defined as: **validation-cohort users who completed a 30-day window with (a) consistent product use, (b) ≤X overrides of the Risk Gate, (c) zero incident-driven termination, (d) submitted at least one substantive feedback artifact.**

| Pro | Con |
|---|---|
| Non-zero in P0 when paid metrics aren't yet meaningful. | Becomes obsolete after P1 launch. |
| Validates the same underlying behaviors that TRAS will later measure on paying users. | Smaller absolute numbers (cohort cap 40) — one user moves the percentage materially. |

**Verdict:** strong stage-bridge metric. Use as NSM during P0; transition to TRAS at P1 narrow ship.

### Option F — Capital-Preservation Score (gross drawdown across cohort, capped)

| Pro | Con |
|---|---|
| Most direct expression of the "capital preservation first" promise. | Heavily distorted by individual user behavior; one over-leveraged user can dominate. |
| Speaks the language of the institutional persona (Layla). | Hard to interpret cleanly until cohort is large. |
| | Better as a watch metric / public transparency artifact than as the operating NSM. |

**Verdict:** rejected as NSM, but recommended as a quarterly published artifact in `13-support-and-trust-ops` later.

## 3. Recommendation

**P0 (now, May 2026 → first weeks of June):** NSM = **Validated Cohort Engagement (VCE)**.

**P1 onwards (post narrow-ship, Jun–Jul 2026):** NSM = **Trust-Retained Active Subscribers (TRAS)**.

This is one stage transition, in one direction, with a clearly defined trigger (P0→P1 narrow-ship moment). No further NSM rotation is anticipated through P3.

## 4. Why TRAS fits CoinScopeAI's current stage

- **It bakes the gate into the business model, not around it.** TRAS rises when the gate is being respected and the product is preserving capital — exactly the behavior we want compounding.
- **It penalizes incident-driven churn and refund waves automatically.** A trust event reduces TRAS even if topline MRR temporarily holds.
- **It penalizes signup-without-engagement.** No "trial bloating" — only durable, gate-aligned paid behavior counts.
- **It scales gracefully into P5.** When per-seat Desk Full v2 customers exist, each seat counts independently in TRAS, which correctly weights expansion within fund customers.
- **It doesn't pretend to be precise.** The N-sessions and override-threshold knobs are part of the definition, but locked after first calibration; not tweaked to flatter a quarter.

## 5. How TRAS should be interpreted

**TRAS is a level metric, read as a trend.** A single weekly value is noise. Use:

- **Week-over-week TRAS delta** — operational signal.
- **TRAS as % of paid subscribers** — quality signal. If absolute paid grows but TRAS-% drops, growth is trust-eroding.
- **TRAS retention curve by cohort** — strategic signal. New cohorts should reach TRAS-eligibility at a rising rate as activation flow improves.

**What a healthy TRAS pattern looks like (qualitatively):**

- Absolute TRAS rises monthly, with occasional flat months during volatility.
- TRAS-% of paid subscribers stays above a defined floor (e.g. 60%) — meaning most paying users are gate-aligned, retained, non-refunded.
- Cohort curves show *later* cohorts reaching TRAS-eligibility *faster* than *earlier* ones — proving onboarding/activation work is compounding.

**What an unhealthy TRAS pattern looks like:**

- Total paid users rising while TRAS-% drops — growth is buying low-quality customers.
- TRAS flat for ≥2 months despite signup growth — activation flow is leaking.
- TRAS drops sharply in a single week — likely a trust event; cross-check incidents and refunds immediately.

## 6. What should NOT be the NSM (and why)

| Tempting candidate | Why it's wrong, especially now |
|---|---|
| **MRR / ARR** | Premature, fragile, hides incident-driven refund risk under headline growth. |
| **Total signups (free + paid)** | Vanity. Easy to inflate, hostile to trust posture. |
| **Daily active users** | Too volatile; daily noise drowns weekly trust signal. Use as supporting metric, not NSM. |
| **Number of signals delivered** | Actively wrong direction — rewards quantity over quality, and conflicts with the gate. |
| **Number of trades placed** | Strongly wrong — rewards activity that the gate may correctly suppress. |
| **Customer satisfaction (CSAT)** | Useful, but a lagging single-survey metric is too easy to influence on a small base. |
| **Net Promoter Score (NPS)** | Same. Use as a watch metric, not NSM. |
| **Returns generated for users** | Catastrophic NSM — would conflate product value with market beta and create a regulatory and reputational problem. |

The last row matters most: **CoinScopeAI must never adopt user P&L as its operating success metric.** It would (a) imply performance attribution, (b) collide with `14-risk-compliance-and-safeguards`, and (c) reward leverage and override behavior the product exists to suppress.

## 7. Recommendation and rationale

**Adopt TRAS as the post-P1 NSM, with VCE as its P0 stage-bridge.** Lock the definition (N sessions, override threshold, refund window) before P1 narrow ship. Do not re-tune the definition to chase a quarter; if the definition needs revision, log it in `21-decision-log` first.

This NSM is harder to compute than MRR. It is also the only NSM whose movement reliably means that the business is doing what it says it does.
