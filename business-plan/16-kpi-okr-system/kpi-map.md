# KPI Map

## How to read this map

Each KPI has: **definition**, **leading/lagging tag**, **owner**, **phase activation**, **source**, **target band**, **status**, and **linked decision or milestone**.

- **Lead/Lag:** Lead = changes first, Lag = confirms. A KPI may be Lead in one chain and Lag in another (e.g., D7 retention is Lead vs monthly churn, Lag vs activation). Tag reflects the dominant chain.
- **Phase activation:** `P0+` (active from P0 forward), `P0-only` (deprecates at next phase), `P1+` (informational before P1, load-bearing from P1), etc.
- **Owner:** role labels per `17-team-and-operating-model/decision-rights.md`. Most rows are Founder until contractor activations; co-owners listed for visibility, accountability remains single-threaded.
- **Target band:** defensible range or watch threshold. Cross-refs in this column point to specific assumption rows in `15-financial-framework/financial-assumptions.md`.
- **Status:** `Not measured` (no instrumentation) / `Measuring` (data accumulating, not yet at interpretation threshold) / `Active` (meaningful data, in operating use) / `Definitional` (blocked on a definition decision, e.g., D-01 lock) / `Deprecated` (scheduled for removal at phase transition).
- **Linked:** decision-log ID (e.g., D-01, H-04) or milestone reference (e.g., M1, M2) — what the KPI unblocks or depends on.

This map is opinionated and short. Adding metrics is easy; removing them is hard. Defer aggressively.

---

## §0. Reading principles (top-of-file callouts)

The four operating principles below override individual row interpretations. They are not section footers; they are the frame.

1. **The headline is *activated* signups, not raw signups.** Vanity inflation in the funnel is the easiest mistake to make.
2. **A high gate-decline rate is good news for capital preservation.** A KPI system that pressures it down is the wrong KPI system.
3. **Trust KPIs are co-equal to growth KPIs in every review.** §4 and §5 are not "side metrics" — they are read at the same cadence and weight as §1.
4. **NRR / LTV / NPS / CAC payback on a small base are stories, not metrics.** Defer them, don't hide them in a footer.

---

## §0a. North Star Metric

**Current NSM:** `VCE` (Validated Cohort Engagement) during P0; transitions to `TRAS` (Trust-Retained Active Subscribers) at P1 narrow ship. Definitions in `north-star-metric.md`.

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| **TRAS (absolute)** | Paid subs past D30, no refund initiated, ≥N gate-aware sessions in trailing 30d, override rate < threshold | Lag¹ | Founder | P1+ | Product DB + Stripe + engine telemetry | Track WoW delta; absolute rises monthly | Not measured (definitional) | A-07; H-04 |
| **TRAS as % of paid** | TRAS / total paid subscribers | Lag | Founder | P1+ | Product DB + Stripe | ≥60% floor (placeholder; lock with H-04) | Not measured | A-07; H-04 |
| **TRAS cohort curve** | TRAS-eligibility timing by signup cohort | Lag | Founder | P1+ | Product analytics | Later cohorts reach TRAS-eligibility faster | Not measured | A-07 |
| **VCE (P0-only)** | % of validation cohort completing 30-day window with gate-aligned behavior, ≤X overrides, zero incident-driven termination, ≥1 substantive feedback artifact | Lead | Founder | P0-only | Manual + product analytics | ≥70% (`15-financial-framework` Row 32) | Validating | A-07; M1 |
| **Time since NSM revision** | Months since the NSM definition or knobs last changed | Lead (process) | Founder | All | `21-decision-log` | Stability is good; alert on any revision <90d apart | Active | A-07 |

¹ TRAS is technically lagging (it's a stock metric over a 30-day window), but the WoW delta is the operating signal; in practice it functions as both.

---

## §1. Growth KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| Free signups (weekly) | New free accounts / trailing 7 days | Lead | Founder | P0+ | Auth/onboarding | Track shape, not absolute | Measuring | — |
| Activated free users (weekly count) | Free users completing the activation definition | Lead | Founder | P0+ | Product analytics | ≥40% of weekly signups (`15-financial-framework` Row 33) | Definitional² | D-01 |
| Paid signups (weekly) | New paid subscriptions across all tiers | Lag | Founder | P1+ | Stripe | Track delta, not absolute | Not measured | H-01 |
| Free → Trader upgrade rate | % of activated free users upgrading within 30 days | Lead | Founder | P1+ | Product DB + Stripe | Early 1–4%; Mature 3–7% (`15-financial-framework` Row 6) | Not measured | D-01; H-01 |
| Tier mix | % distribution across SKUs (Free / Trader / Preview / Full) | Lag | Founder | P1+ | Stripe | Trader-dominant through P3 | Not measured | A-03 |
| Geographic mix | % by country / region | Lag | Founder | P0+ | Stripe + signup | MENA + global EN. **Alarm on any US signup — treat as enforcement-bypass incident, not a metric drift** | Active | A-06; QE-02 |

² Row depends on D-01 (activation definition lock) — directional only until D-01 closes.

**Headline rule (cross-link to §0 principle 1):** the headline is *activated* signups (Row above), not raw signups.

---

## §2. Activation KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| Time-to-first-meaningful-action | Median minutes from signup to first scan + first journal entry | Lead | Founder | P0+ | Product analytics | <60 min target | Definitional² | D-01 |
| Activation rate (%) | % of weekly signups completing activation definition within 7 days | Lead | Founder | P0+ | Product analytics | ≥40% (`15-financial-framework` Row 33) | Definitional² | D-01 |
| Day-7 retention | % of activated users still active on D7 | Lead vs churn / Lag vs activation | Founder | P0+ | Product analytics | ≥60% (`15-financial-framework` Row 34) | Measuring | D-01 |
| Day-30 retention | % of D7-retained users still active on D30 | Lead vs churn / Lag vs activation | Founder | P0+ | Product analytics | ≥40% (`15-financial-framework` Row 35) | Measuring | D-01; M3 |
| Onboarding drop-off step | First step where ≥X% of users abandon | Lead | Founder | P0+ | Product analytics | Drop-off >20% at any step → investigate (per D-02) | Measuring | D-02 |
| Exchange-connection success rate | % of users completing API key linking on first attempt | Lead | Founder | P0+ | Product analytics | ≥80% | Measuring | D-03 |

**Cross-link:** "Activation rate (%)" and §1's "Activated free users (count)" are two views of the same underlying measurement. The §1 row is the headline (used in growth chain); the §2 row is the operational ratio (used in activation chain).

---

## §3. Retention KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| Trader monthly churn | Trader subs cancelled / Trader subs at start of month | Lag | Founder | P1+ | Stripe | 5–10% mature; 10–20% early (`15-financial-framework` Rows 9/10) | Not measured | H-01 |
| Cohort retention curve (D7/D30/D90/D180) | Retention by signup cohort | Lag | Founder | P0+ | Product analytics | Later cohorts ≥ earlier cohorts | Measuring (D7/D30 only) | M3 |
| Reactivation rate | Churned → returned within 90 days | Lag | Founder | P1+ | Stripe + DB | Watch only, no target yet | Not measured | — |
| Tier downgrade rate | % moving to a lower tier in a month | Lag | Founder | P2+ | Stripe | Watch only | Not measured | — |
| Net revenue retention (NRR) | Standard NRR formula | Lag | Founder | P3+ | Stripe | **Deferred** until cohort large enough to interpret | Deprecated (until P3) | — |

**Note:** NRR on a small base tells you nothing. Listed here as deferred, NOT as actively tracked. Cross-link to §0 principle 4.

---

## §4. Trust and Support KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| Incident count by severity | P1 / P2 / P3 incidents per month | Lag | Founder / Trust Ops | P0+ | Incident log | <1 P1/quarter target | Active | — |
| Mean time to acknowledge (MTTA) | Avg minutes to acknowledge a P1 incident | Lead | Founder / Trust Ops | P0+ | Incident log | ≤15 min for P1 | Active | C-06 |
| Mean time to resolve (MTTR) | Avg minutes to resolve a P1 incident | Lag | Founder / Trust Ops | P0+ | Incident log | Track, no fixed target | Active | — |
| Incident postmortem completion | % of P1 incidents with postmortem completed within 7 days | Lag | Founder | P0+ | Incident log | 100% target | Active | — |
| Support ticket volume | Tickets per active user per month | Lag | Founder / Trust Ops | P0+ | Support tool | Trader ≤30 min/user/mo (`15-financial-framework` Row 12) | Active | G-01 |
| Time to first response (TTFR) | Median minutes to first human reply | Lead | Founder / Trust Ops | P0+ | Support tool | <4h business hours | Active | — |
| **Refund rate (CANONICAL)** | Refunds / MRR | Lag | Founder | P1+ | Stripe | <2% / mo, never >5% (`15-financial-framework` Row 11) | Not measured | C-05 |
| User-reported gate confusion | Tickets/comments where user misunderstood a gate decision | Lead | Founder / Trust Ops | P0+ | Support tagging | Trend down over time | Active | — |
| Trust events (public-facing) | External commentary requiring response posture | Lag | Founder | P0+ | Manual log | Zero target; investigate any | Active | C-02 |
| CSAT after support interaction | Avg score on post-ticket micro-survey | Lag | Founder / Trust Ops | P1+ | Support tool | Watch only — **NOT** the headline trust metric (see §10) | Not measured | — |

**Cross-link:** Refund rate is canonical here (trust-side ownership). §6 Financial section lists it as a reference only.

---

## §5. Risk and Safeguard KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| PCC v2 gate state | Current state of G1–G4 + §8 Capital Cap | Lead | Founder / Engineering | P0+ | Engineering log | Forward-only progress; backward = alert | Active | H-05; A-05 |
| Days since last gate transition | Days since most recent G-transition | Lead | Founder | P0+ | Engineering log | Stability is good; >60d watch | Active | — |
| Kill-switch trips | Count + reason per week | Lead | Founder / Engineering | P0+ | Engine logs | Trips are good; explained trips are great (cross-link §0 principle 2) | Active | — |
| Kill-switch halt minutes / month | Total minutes engine spent in halt state | Lag | Founder / Engineering | P0+ | Engine logs | Track shape; investigate spikes | Active | — |
| Gate-decline rate | % of candidate signals declined by Risk Gate | Lead | Founder / Engineering | P0+ | Engine logs | Track shape; alert on sudden drop. **DO NOT pressure downward** (§0 principle 2) | Active | — |
| Override events | User overrides of a gate decision (count + per-user distribution) | Lead | Founder | P1+ | Engine logs | Per-user override rate < threshold (locks at H-04) | Not measured | H-04 |
| Risk threshold breaches | Any of the 5 canonical thresholds breached: 10x leverage, 10% MDD, 5% daily loss, 3 max positions, 80% heat cap | Lead | Founder | P0+ | Engine logs | Investigate every event | Active | A-05 |
| Engine rollback events | Production engine rolled back to prior version | Lead | Founder / Engineering | P1+ | Deploy log | Zero is the target; ≥1 triggers refund risk review | Not measured | — |
| Vendor outage minutes | Provider-side outage minutes affecting users | Lag | Founder / Engineering | P0+ | Connector-health artifact | Track, not optimize | Measuring | — |
| Real-capital authorization status | Authorized? Y/N + last review date | Lead | Founder | All | Decision log | Default N until §8 conditions met | Active | C-01 |

**Cross-link to §0 principle 2:** A high gate-decline rate is good news. The KPI system tracks it as a *shape* metric, not a *minimize* metric.

---

## §6. Financial KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| MRR | Monthly recurring revenue (Stripe net of refunds) | Lag | Founder | P1+ | Stripe | Track delta, not absolute | Not measured | H-01 |
| ARPU by tier | Net revenue / paying users / tier | Lag | Founder | P1+ | Stripe | Match list price ±5% | Not measured | A-03 |
| Stripe blended take-rate | Effective Stripe fee % including FX | Lag | Founder | P1+ | Stripe | 3.0–3.9% MENA; 2.9–3.4% global EN (`15-financial-framework` Row 18) | Not measured | F-05 |
| Vendor cost % of revenue | Total vendor spend / MRR | Lag | Founder | P1+ | Bills + Stripe | ≤25% (`15-financial-framework` Row 36) | Not measured | F-02 |
| Top-3 vendor concentration | Sum of top 3 vendors / total cost | Lag | Founder | P0+ | Bills | <70% target; investigate at 80%+ | Measuring | — |
| Single-vendor concentration | Largest single vendor / total cost | Lag | Founder | P0+ | Bills | ≤40% (`15-financial-framework` Row 37) | Measuring | — |
| LLM cost per active user | LLM spend / monthly active user | Lead | Founder | P0+ | Provider dashboards | Flat-to-mild-growth target | Measuring | — |
| Cash runway (months) | Cash on hand / monthly burn | Lag | Founder | P0+ | Manual | ≥9 months at all times (`15-financial-framework` Row 31) | Active | F-03 |
| Refund rate (REFERENCE) | Refunds / MRR | Lag | Founder | P1+ | Stripe | Same as §4 canonical refund rate | Not measured | C-05 |
| Founder hours by category | build / support / ops / GTM hours/week | Lead | Founder | P0+ | Manual log | Visible, not optimized | Not measured | F-01; QH-04 |

**Note:** No ARR claims at this stage. ARR on a small monthly base is misleading framing.

---

## §7. Operations KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| Connector-health score | % of integrations with valid auth, no rate-limit hit, fresh data | Lead | Founder / Engineering | P0+ | Cowork artifact `coinscope-connector-health` | 100% target; <100% triggers fix | Active | — |
| Deploy frequency | Production deploys per week | Lead | Founder / Engineering | P0+ | CI logs | Steady is good; sudden drop = blocker | Active | — |
| Deploy failure rate | % of deploys requiring rollback or fix-forward | Lag | Founder / Engineering | P0+ | CI logs | <10% target | Active | — |
| Runbook coverage | % of likely incident types with documented runbook | Lead | Founder / Trust Ops | P0+ | Manual audit | ≥80% by P1 | Measuring | M2 |
| Backup verification | Last successful backup-restore test | Lead | Founder / Engineering | P0+ | Manual | Within trailing 30d | Active | M2 |
| Monitoring coverage | % of critical paths instrumented with alerts | Lead | Founder / Engineering | P0+ | Manual audit | ≥90% by P1 | Measuring | M2 |

---

## §8. Product-Readiness KPIs

| KPI | Definition | L/L | Owner | Phase | Source | Band / threshold | Status | Linked |
|---|---|---|---|---|---|---|---|---|
| PCC v2 gate progress | G1, G2, G3, G4 status | Lead | Founder / Engineering | P0+ | Engineering log | Forward-only | Active | A-05; H-05 |
| **PCC v2 G3 consecutive stable days** | Days with no unexplained kill-switch trip, no rollback, no drift event | Lead | Founder / Engineering | P0+ | Engine telemetry | ≥30 days for P1 ship (`15-financial-framework` Row 23) | Validating | H-01; QA-01 |
| §8 Capital Cap status | Current cap state + last review | Lead | Founder | P0+ | Decision log | Default capped until criteria | Active | C-01 |
| Replay days corpus size | Number of stress-tested historical days | Lead | Founder / Engineering | P0+ | Engine repo | ≥20 by P1 | Measuring | M2; QA-03 |
| Backtest coverage | % of signals with passing backtest | Lead | Founder / Engineering | P0+ | Engine repo | 100% target | Active | — |
| Validation cohort completion | % of cohort completing 30-day window with no incident-driven termination | Lead | Founder | P0-only | Manual | ≥70% (`15-financial-framework` Row 32) | Validating | M1; QD-01 |

---

## §9. Leading vs lagging mix

A healthy KPI map is roughly **60% leading, 40% lagging**. CoinScopeAI's current map is intentionally weighted that way. Leading metrics give time to act before lagging metrics confirm the trend.

**Decision rule:** when a KPI moves, it's the **leading metric pair** that should drive decisions. Lagging metrics confirm; they don't trigger.

**Chain-relativity caveat:** some KPIs (e.g., D7/D30 retention) are Lead in one chain and Lag in another. The tag in this map reflects the dominant chain; in operating use, the metric serves both.

---

## §10. Metrics to defer until later maturity

Do **not** track these as named KPIs yet. Reasons in parentheses.

- **NPS / Net Promoter Score** — too noisy at small base; vanity-prone.
- **Lifetime Value (LTV)** — needs ≥6 months of paid data; until then it's a story.
- **CAC payback period** — no paid acquisition yet; CAC is founder-time, not benchmarkable.
- **Magic Number / Bessemer Efficiency Score** — designed for venture-scale SaaS reporting.
- **Net Revenue Retention (NRR)** — requires meaningful expansion motion; defer to P3+.
- **Logo retention** — not meaningful at small N.
- **CSAT as the *headline* trust metric** — too easy to influence at small base. Use incident count + refund rate as the trust headline. CSAT remains a watch metric per §4 row, but should not move executive-review priorities.
- **Performance attribution metrics (user P&L)** — explicitly excluded for regulatory and trust reasons.
- **Sales-cycle metrics (deal size, pipeline coverage, win rate)** — defer to P5+ when Desk Full v2 sales motion exists.
- **Logo expansion / contraction rate** (separate from NRR) — defer to P3+.

---

## §11. Ownership summary

At current stage, the founder owns nearly every KPI. As `17-team-and-operating-model/role-priorities.md` activates roles, ownership transitions:

| Role activation | Takes over | Phase trigger |
|---|---|---|
| Trust Ops contractor | Trust + Support KPIs (§4 above) | P2 |
| Engineering contractor | Risk + Product-Readiness + Ops KPIs (§5, §7, §8) | P2 |
| Bookkeeping contractor | Financial KPI data assembly (§6) | First paid customer |
| First full-time hire | Driven by where the binding constraint sits at activation, not pre-decided | P3+ |

**Single-threaded accountability rule:** even when KPIs list multiple roles, accountability is single-threaded per `decision-rights.md`. Co-owners are visibility, not accountability.

**Handoff discipline:** when a role activates, KPI rows in this map are updated in the same week. The `Owner` column reflects current ownership; transitions are logged in `21-decision-log`.

---

## §12. Cross-references

| KPI block | Primary upstream folder |
|---|---|
| North Star (§0a) | `16-kpi-okr-system/north-star-metric.md` |
| Growth (§1) | `04-icp-and-segmentation`, `08-go-to-market` |
| Activation (§2) | `12-onboarding-and-activation` |
| Retention (§3) | `04-icp-and-segmentation`, `13-support-and-trust-ops` |
| Trust + Support (§4) | `13-support-and-trust-ops` |
| Risk + Safeguard (§5) | `14-risk-compliance-and-safeguards` |
| Financial (§6) | `15-financial-framework` (Row references throughout) |
| Ops (§7) | `13-support-and-trust-ops`, `14-risk-compliance-and-safeguards` |
| Product-Readiness (§8) | `06-product-strategy`, `14-risk-compliance-and-safeguards` |
| Decision references | `21-decision-log/leadership-decision-register.md` (IDs in `Linked` column) |
| Open question references | `21-decision-log/open-questions-register.md` (QA/QD/QE/QF/QG/QH IDs) |

---

*Last reviewed: 2026-05-08. Reviewed at every weekly review (KPI values), monthly exec review (full map), and phase transition (full re-baseline + ownership transitions).*
