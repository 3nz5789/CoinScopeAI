# Cost Structure

## 1. Major cost categories

CoinScopeAI's cost structure at P0–P1 is dominated by **vendor data costs and founder time**, not headcount. As we move toward P2 and beyond, the cost mix shifts: vendor expansion, support load, and selective hiring become the larger lines.

| Category | P0 (May 2026, validation) | P1 (narrow ship) | P2–P3 (vendor expansion) | P5 (Desk Full v2) |
|---|---|---|---|---|
| **Infrastructure** | Low | Low–Med | Med | Med–High |
| **Data / API vendors** | Med | Med | High | High |
| **Exchange integration cost** (sandbox, testnet) | Negligible | Low | Med | Med |
| **AI / LLM API costs** (Scoopy, regime, copy gen) | Low | Low–Med | Med | Med–High |
| **Support / trust ops** | Founder time only | Founder + part-time | Dedicated support | Tiered support |
| **GTM / acquisition** | $0 budget | Low (founder content) | Selective | Selective + paid |
| **Compliance / legal** | One-off | Recurring (ToS, DPA) | Recurring + audit prep | Audit + per-seat compliance |
| **Founder time** | High (recognized at internal rate, DECISION NEEDED) | High | Medium (offloaded to first hires) | Strategic only |

## 2. Likely fixed vs variable costs

### Fixed (or near-fixed at our scale)

- Domain, DNS, monitoring (Datadog/Sentry-equivalent) — small, but always-on.
- Base infrastructure floor (one app server, one PG, one Redis, one engine VPS).
- Core data subscriptions that are tier-flat (e.g. CoinGlass base tier, Tradefeeds base tier).
- Legal retainer (REQUIRED INPUT — currently project-based, not retainer).
- Stripe account fee floor.

### Variable (scale with users, signals, calls, or capital)

- LLM API costs (Claude / OpenAI) — scale with Scoopy interactions, signal explanation calls, regime classification frequency.
- Exchange API request budget — scales with active scanned pairs and update frequency.
- Data feed call volumes (CoinGecko, Tradefeeds endpoints) — scale with user-driven scanning.
- Stripe transaction fees — scale with revenue.
- Email / Telegram alert delivery — scales with active users × alert frequency.
- Support time — scales with active users (not signups).

### Hybrid / step-function

- Compute (engine VPS) — flat until throughput exceeds a threshold, then step-up to next tier.
- Database — flat until row volume / connection count crosses tier.
- Per-vendor minimums + overage — fixed floor with variable overage, the most dangerous shape if overage is not monitored.

## 3. Vendor cost exposure

CoinScopeAI is **highly vendor-exposed**. This is a structural feature of trading platforms, not a flaw, but it must be managed explicitly.

| Vendor type | Examples | Why exposure is high |
|---|---|---|
| **Exchanges** | Binance (P0–P1), Bybit (P2) | Rate limits, API changes, enforcement actions, regional restrictions. |
| **Market data aggregators** | CoinGecko, Tradefeeds | Pricing tier shifts, endpoint deprecation, latency. |
| **Derivatives data** | CoinGlass | Single-source dependency for funding/OI/liquidation features. |
| **AI providers** | Anthropic (Claude), OpenAI | Token pricing changes, rate limits, model deprecation. |
| **Infra** | Hosting provider, managed PG, Redis, Stripe | Regional outages, billing model changes. |
| **Comms** | Telegram (Scoopy bot), email provider | Account suspension risk, deliverability changes. |

**Vendor concentration tests we should be running monthly:**

- Top 3 vendors as % of monthly cost.
- Highest single-point-of-failure vendor (if it disappeared tomorrow, what stops working?).
- Vendor-cost-per-paying-user — early warning of cost slope outpacing revenue slope.

(Cross-ref: phased-vendor-rollout memory and `14-risk-compliance-and-safeguards`.)

## 4. Infrastructure cost drivers

| Driver | Description | Sensitivity |
|---|---|---|
| **Scanned pair count** | More pairs scanned at higher frequency = more API weight + more compute. | High |
| **Bar resolution** | 1m vs 5m vs 15m vs 1h scanning has dramatic cost differences. | High |
| **Active users** | Each active user adds Scoopy turns, dashboard loads, signal explanations. | Medium |
| **Alert volume** | Per-user × per-alert-type × per-pair. Easy to under-budget. | Medium |
| **Backtest / simulation** | Heavy reads of historical OHLCV during dev cycles. | Medium (controllable) |
| **Replay days corpus** | Stored data + replay compute. Bounded but real. | Low–Medium |
| **Logging / observability** | Trace volume scales with user activity + signal density. | Medium |

**Cost-engineering levers we should preserve:**

- Cache OHLCV aggressively (cross-ref: `scanner-engine-optimizer` skill).
- Batch exchange requests; never single-call when batchable.
- WebSocket where feasible to avoid REST weight.
- Tier scanning: high-priority pairs every 1m, lower-priority every 5–15m.
- Throttle Scoopy LLM calls per session; cache regime-explanation strings.

## 5. Exchange / data / API cost sensitivity

The riskiest cost shape is **a vendor with a low fixed floor + steep overage curve**. This pattern is common in crypto data:

- "Free up to 30 calls/sec, $X per 1k calls beyond."
- "$Y/mo includes 10 endpoints, $Z each additional."

Without monitoring, this scales smoothly until a single bad day (high volatility, more signals, more user activity) blows the budget.

**Mitigation discipline:**

- Hard budget alarms per vendor (50%, 80%, 100% of monthly budget).
- Per-vendor daily call counter, surfaced on the connector-health artifact.
- Defined fail-soft behavior — if a vendor budget is hit, scanner degrades gracefully (fewer pairs, longer interval) instead of erroring.
- Quarterly vendor cost review against revenue.

## 6. Support and ops costs

Support cost is dominated by **time, not seat licenses**, until we cross a threshold of active users that demands a dedicated headcount.

| Phase | Support model | Cost shape |
|---|---|---|
| P0 | Founder direct, async via email + Telegram | Time-only |
| P1 | Founder + canned responses + KB articles | Time + small KB platform fee |
| P2–P3 | Part-time support contractor + ticketing tool | Hourly + tool license |
| P5 | Tiered support, response SLAs by SKU, Desk Full v2 customers get priority | Headcount + tooling |

**The hidden support cost is incident response.** Cross-ref: `13-support-and-trust-ops`. A single 4-hour incident can consume more founder time than a week of normal support, and that time is invisible in any tooling spend.

**ASSUMPTION (load-bearing):** average support load per Trader-tier user at maturity is ≤30 min/month including incident overhead. This is the threshold above which we need dedicated support before adding more revenue.

## 7. GTM / customer acquisition costs

Cross-ref: `08-go-to-market`.

At P0–P1 the GTM budget is **effectively zero, paid in founder time and content**. We should not assume CAC numbers from generic SaaS benchmarks; they don't apply to a trust-sensitive crypto trading product where:

- Paid acquisition is structurally risky pre-G4 (we'd be acquiring users who can't be trusted with the gated promise).
- Affiliate / referral programs tied to exchanges are excluded by jurisdictional posture.
- The only acceptable acquisition motions are content, founder voice, and earned trust, none of which translate to a clean CAC number.

**What "CAC" actually looks like at our stage:**

- $0 paid acquisition.
- Time cost of producing trust-grade content (founder hours × internal rate).
- Time cost of community presence (founder hours × internal rate).
- Tool fees (analytics, scheduling) — small.

When we can credibly run paid acquisition (P3+ at earliest), CAC modeling should distinguish:

- **Trust-sensitive channels** (specialist newsletters, niche communities) — higher cost per click, higher conversion quality.
- **Broad channels** (X ads, Reddit ads) — lower cost, lower quality, often higher refund risk.

## 8. Cost risks to monitor early

| Risk | Why it matters | Watch metric |
|---|---|---|
| **Vendor overage explosion** | Volatile day → budget breach → hard cost spike. | Per-vendor daily spend, weekly. |
| **LLM cost slope > active-user slope** | If Scoopy usage scales superlinearly, margin collapses on Trader. | LLM cost / active user / month. |
| **Compute step-up triggered by inefficient scanning** | One bad query pattern can push us into the next tier prematurely. | Compute utilization weekly. |
| **Support load step-up** | First hire is a real commitment — under-shooting and over-shooting are both costly. | Avg minutes/user, p95 ticket time. |
| **Compliance creep** | A new jurisdiction or product feature pulls in legal/compliance fees we hadn't budgeted. | Open compliance items, $-flagged. |
| **Founder time as hidden cost** | Treating founder time as $0 makes early margins look better than they are. | Founder hours/week by category. |

## 9. Cost discipline recommendations for the current stage

1. **Treat founder time as a real cost.** Pick an internal rate (DECISION NEEDED — recommend $100/hr placeholder until a fundraise or exit values it differently). Apply it consistently in all internal cost reviews.

2. **Run a monthly vendor cost review.** Top 5 vendors by spend, % of total cost, % of revenue (when revenue exists). Cross-ref: `coinscope-connector-health` Cowork artifact.

3. **Budget alarms before they're needed.** Every vendor should have hard alarms at 50/80/100% of expected monthly spend, set up *before* the first paying customer.

4. **Defer all non-essential SaaS.** Until P2, refuse any tool that costs more than $50/mo unless it directly supports a PCC v2 gate or §14 safeguard.

5. **Prefer call-budget caps over feature-richness.** A vendor that lets you cap calls is safer than one that bills overage; even at higher list price.

6. **No headcount before P2.** Hires before the engine and revenue model are validated will burn cash and create coordination overhead. (Cross-ref: `17-team-and-operating-model` upcoming.)

7. **Document every contract's exit path.** Annual contracts at this stage are landmines. Prefer monthly with no minimums.

8. **Reserve a minimum 90-day runway for vendor + infra costs before any GTM spend.** A surprise vendor invoice should never threaten the engine itself.

9. **Track "cost per validated signal" as a watch metric.** Not for reporting — as a sanity check. If it climbs without a corresponding rise in customer-perceived value, the cost structure is drifting in the wrong direction.

10. **Review this folder quarterly.** Cost structure changes as fast as the product does.
