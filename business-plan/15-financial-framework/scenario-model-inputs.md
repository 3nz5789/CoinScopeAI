# Scenario Model Inputs

This file defines **what to track**, not **what to forecast**. It exists so that when leadership eventually builds a 3-statement model or fundraising spreadsheet, the inputs are pre-defined, sourced, and graded — not invented.

We deliberately do not present scenario *outputs* (no ARR forecasts, no margin tables). Scenario outputs at this stage are vapor; the discipline is in the inputs.

## 1. Best / base / worst input categories

For each category we describe **what changes** between scenarios, not what value to use. Values come from `financial-assumptions.md` once validated.

### Revenue inputs

| Input | Best case driver | Base case driver | Worst case driver |
|---|---|---|---|
| Free-tier signup velocity | Founder content + organic compounding strongly | Steady, modest organic | Activation friction or trust event suppresses signups |
| Free → Trader conversion | Upper end of band (#6) | Mid-band | Lower end or below band |
| Trader churn | Lower end of band (#9) | Mid-band | Above band, drawdown-correlated waves |
| Tier mix | Desk Preview adopted earlier than expected post-P2 | Trader dominates through P3 | Trader cap stalls; Desk Preview deferred |
| Desk Full v2 ramp (P5+) | Multi-seat expansion at first cohort | Single-seat first, expansion gradual | Launch slipped to mid-2027 or beyond |
| Refund rate | <2% MRR/mo | 2–4% MRR/mo | 5%+ MRR/mo, incident-driven |
| Geographic mix | MENA + global EN balanced | MENA-heavy with global EN trickle | MENA-only (global EN fails to land) |

### Cost inputs

| Input | Best case driver | Base case driver | Worst case driver |
|---|---|---|---|
| Vendor cost / revenue | <15% | 15–25% | >25%, with overage events |
| LLM cost / active user | Cache + throttle keep it flat | Slightly superlinear, manageable | Superlinear, margin-eroding |
| Support time / Trader user | <20 min/mo | 20–30 min/mo | >30 min/mo, with incident bursts |
| First hire timing | Deferred to late P2 | Mid-P2 | Forced early at P1 due to overload |
| Compute step-up | Avoided through P2 | One step-up at P2 | Multiple step-ups, cost discontinuities |
| Compliance / legal | Project-based, light | Recurring + ToS/DPA refresh | Audit-driven scope expansion |

### Trust / risk / ops inputs (frequently underweighted)

| Input | Best case driver | Base case driver | Worst case driver |
|---|---|---|---|
| Incident frequency | <1 P1 incident / quarter | 1–2 P1 incidents / quarter | Multiple P1s, public-facing |
| Vendor outage exposure | Quick fail-soft, no user impact | Brief fail-soft, minor impact | Cascading vendor outage, paid-customer impact |
| Regulatory pressure | Stable jurisdictional posture | Minor clarification work | Forced jurisdiction change or feature suspension |
| Engine rollback events | None | One rollback, fast recovery | Multi-day rollback, refund wave |
| Public trust event | None | Minor public discussion handled with transparency | Major public incident requiring response posture |

## 2. Inputs leadership should track

A short list of **always-on** inputs (weekly or monthly review):

- **Revenue side:** active paying users, MRR, refund rate, churn cohort, upgrade rate Free → Trader.
- **Cost side:** total vendor cost, top-3 vendor concentration %, LLM $/active user, infrastructure $/MRR.
- **Trust/ops side:** incident count + severity, kill-switch trips, gate-decline rate, user-reported gate confusion (`13-support-and-trust-ops`), engine rollbacks.
- **Phase progress:** PCC v2 gate status (G1–G4 + §8 Capital Cap), days since last gate transition.
- **Cohort health:** activation rate, day-7 retention, day-30 retention, day-90 retention.

Anything not on this list is a vanity metric for our stage.

## 3. What triggers scenario revision

Revise scenarios — meaning re-run the input table, not just tweak a number — when **any** of the following occur:

| Trigger | Why it forces revision |
|---|---|
| PCC v2 gate transition (forward or backward) | Changes which SKUs are authorized to monetize. |
| Vendor pricing change >10% on any line >5% of cost | Resets cost-side inputs. |
| Single P1 incident with paid-customer impact | Resets trust/ops inputs and refund risk. |
| New jurisdictional restriction (or relaxation) | Resets geographic mix and possibly compliance cost. |
| Real-capital authorization decision | Fundamentally changes revenue ceiling and risk posture. |
| Successful 60-day cohort with paid users | First moment we can replace assumption bands with measured numbers. |
| Founder hiring decision (first hire, role, timing) | Resets cost-side and operating-model inputs. |
| Any material engine architecture change | May change compute and vendor cost shape. |

**Avoid quarterly scenario revision purely on calendar.** Triggers should be event-driven, not date-driven. Calendar-revising creates motion without insight.

## 4. Revenue-side input list (full)

For each, name the input and where the data lives once it exists:

| Input | Source |
|---|---|
| Free signups (count, weekly) | Auth/onboarding analytics |
| Free activations (defined: completed onboarding + first scan + first journal entry) | Product analytics |
| Free → Trader upgrade events | Stripe + product DB |
| Trader signups (count, weekly) | Stripe |
| Trader MRR | Stripe |
| Trader churn events (count + reason) | Stripe + cancellation form |
| Refund events (count + amount + reason) | Stripe + support log |
| Tier mix (Free / Trader / Preview / Full) | Product DB |
| Effective ARPU per tier | Stripe net of discounts/refunds |
| Annual vs monthly mix (when annual launches) | Stripe |
| Geographic mix | Stripe + signup country |
| Cohort retention curves (D7, D30, D90, D180) | Product analytics |
| Reactivation events (churned → returned) | Stripe + product DB |

## 5. Cost-side input list (full)

| Input | Source |
|---|---|
| Per-vendor monthly spend | Vendor invoices + connector-health artifact |
| Per-vendor call/usage volume | Vendor dashboards + internal counters |
| LLM token spend (Claude, OpenAI separately) | Provider dashboards |
| Compute (engine VPS, app, PG, Redis) | Hosting bill |
| Email/Telegram delivery costs | Provider bill |
| Stripe processing fees | Stripe |
| Domain / DNS / monitoring fixed | Vendor bills |
| Founder time by category (build, support, ops, GTM) | Manual log; reviewed weekly |
| Contractor spend (when activated) | Invoices |
| Legal / compliance spend | Invoices |
| One-off vs recurring breakdown | Internal tagging |

## 6. Trust / risk / ops inputs that affect financial performance

These are often left out of financial models, which is a mistake for a trust-sensitive product:

- **Kill-switch trip count and reasons** — a kill-switch that trips often is correctly working but creates user-experience cost and may suppress upgrade intent.
- **Gate-decline rate** — high decline rate is the gate doing its job, but if users don't understand it, churn rises.
- **Incident count + severity + duration** — drives refund risk and reputational tail.
- **Engine rollback events** — direct refund risk.
- **Provider outage exposure (minutes/month)** — drives both cost (fail-soft compute) and trust (visible degradation).
- **Public sentiment events** — track separately; correlate with churn and refunds.

The financial model should explicitly include lines for **incident-driven refunds** and **trust-event-driven churn delta**, even if zero in baseline.

## 7. Metrics that should feed a future model

When the time comes to build a real 3-statement or unit-economics model, these are the inputs that matter most:

1. **Cohort-based retention curves**, not flat churn rates.
2. **Tier-mix evolution over cohort age** — users upgrade or downgrade over time, not at a single point.
3. **Cost-per-active-user** broken into infrastructure / LLM / vendor / support.
4. **Refund rate by cause** (incident, dissatisfaction, accidental signup, drawdown-period).
5. **Per-vendor sensitivity** — what happens to margin if vendor X goes up 25%?
6. **Trust-event impact distribution** — if an incident occurs, what's the typical churn + refund + support time delta?
7. **Real-capital revenue gate** — when (if ever) and what it does to the ceiling.
8. **Founder time as cost** at internal rate (post-DECISION).
9. **Hiring decision tree** — first hire, second hire, role, timing, cost.
10. **Phase-gated SKU activation timing**.

A model that treats CoinScopeAI like generic SaaS — flat churn, smooth growth, fixed CAC — will be wrong in the first stress event. The inputs above force the model to encode the right shape.

## 8. What NOT to pretend to know yet

This list is as important as anything else in the folder.

- **We do not know our paid conversion rate.** Bands are directional only.
- **We do not know our true CAC.** No paid acquisition has been run; founder-time CAC is real but not benchmarkable yet.
- **We do not know LTV.** Without 6+ months of paid data, LTV is a story.
- **We do not know vendor cost slopes at scale.** P0 volumes are tiny; pricing curves bend at higher tiers.
- **We do not know what the Desk Full v2 sales cycle looks like.** Zero validated B2B sales motion to fund customers.
- **We do not know our refund rate under stress.** Baseline can be modeled; incident-driven cannot.
- **We do not know how regulatory posture evolves** in any of our target jurisdictions over the next 12 months.
- **We do not know which of our high-risk assumptions will fail first** — only that some will.

A scenario model that pretends to know any of the above is **less useful than no model at all**, because it converts uncertainty into false precision and lets leadership over-commit on the back of it. The discipline is to track the inputs, mark them as `not-yet-validated`, and revise on triggers — not to fabricate numbers to fill a spreadsheet.

---

*Inputs to be revisited at every PCC v2 gate transition and at every cohort-health checkpoint.*
