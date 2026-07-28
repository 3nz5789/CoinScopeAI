# Role Priorities

## 1. Highest-priority roles (in sequence)

The list below is **ordered by activation sequence**, not by org-chart importance. Every role activates only when its trigger fires. No role activates by calendar.

| # | Role | Engagement | Activation trigger | Phase ETA |
|---|---|---|---|---|
| 1 | **Founder** | Full-time | Already active | P0+ |
| 2 | **Bookkeeping contractor** | Project / monthly batched | First paid customer (any tier) | Late P1 |
| 3 | **Trust Ops contractor** | Part-time hourly | First of: 30 days post-P1 narrow ship, OR support tickets >X/week, OR P95 TTFR breached for 2 consecutive weeks | P2 |
| 4 | **Engineering contractor — vendor integrations** | Project SOWs | P2 vendor expansion scope locked | P2 |
| 5 | **Optional advisor** | Informal / paid retainer | Founder identifies trusted candidate; mutual fit | P1+ |
| 6 | **Legal counsel — recurring** | Light retainer | First Desk Preview customer with B2B contract requirements | P2–P3 |
| 7 | **First full-time hire** | Full-time | Contractor #3 OR #4 has been the binding constraint for ≥3 months | P3 |
| 8 | **Customer Operations / Sales Lead** | Full-time | Desk Full v2 launch + first 3 fund-tier conversations | P5 |
| 9 | **ML / regime specialist** | Contractor first, FT later | Desk Full v2 monetization validated AND regime model upgrade roadmap requires specialist depth | P5+ |
| 10 | **UX / design contractor** | Project | Activation rate plateaus despite 2 consecutive flow iterations | P3+ |

## 2. Role detail — what each role owns

### Founder

**Owns (durable, non-delegable through P3):**

- Product strategy, roadmap, prioritization.
- Engine + scanner + ML core (until specialist activation).
- Risk Ownership and PCC v2 gate authority.
- Public-claims authority and brand voice.
- Pricing decisions and tier activations.
- Vendor relationships and concentration management.
- All legal/compliance authority (with external counsel input).
- Hiring decisions for every role on this list.
- Real-capital authorization decision (cross-ref `14-risk-compliance-and-safeguards` §8).

**Why durable:** every item above is either a single-source-of-truth issue (brand, claims, risk) or a strategic ownership issue (pricing, hiring) that delegation at our stage would weaken, not strengthen.

### Bookkeeping contractor (Role #2)

**Owns:**

- Monthly reconciliation of Stripe, vendor invoices, founder time log, cash position.
- Quarterly tax-relevant filings prep (UAE sole prop posture; coordinate with founder + counsel).
- Producing the monthly financial deck slot for the exec review (`16-kpi-okr-system`).

**Why this is role #2 and not later:** it's the lowest-cost time-saver available. A bookkeeping contractor at $100–500/month replaces 10–20 founder hours/month at a far higher implicit rate. Activate as soon as there is *any* paid customer to reconcile.

**Why this is role #2 and not first:** with zero paid customers, there's nothing to reconcile beyond founder cash flow, which the founder can do in 30 min/month.

### Trust Ops contractor (Role #3)

**Owns:**

- First-line support for Free + Trader tiers.
- Ticket triage, severity tagging, gate-confusion classification.
- KB article maintenance per `13-support-and-trust-ops`.
- Incident triage (acknowledge, gather data, page founder for resolution).
- Weekly support metrics input to `weekly-review-template.md`.
- Refund processing (under explicit approval rules — does NOT have unilateral refund authority).

**Why this is the most important non-founder hire:**

1. Trust Ops is the only role whose absence creates a *brand* failure mode at our stage. A slow ticket response or a confusing gate explanation lands directly on trust posture.
2. It's the role that protects founder time during incident weeks. Without it, founder cannot run the weekly/monthly reviews under stress.
3. It's the role that *cannot* be a generic SaaS support contractor — they need to understand regime labels, gate decisions, override events, and the exact language of `13-support-and-trust-ops`.

**Hiring profile:**

- 5–15 hours/week to start, scaling to 20–25 by P3.
- Strong written EN; MENA timezone preferred for coverage.
- Trading or fintech context is a strong plus, but not a hard requirement — discipline and clarity matter more.
- Comfort with documentation-heavy work (KB maintenance is half the role).

### Engineering contractor — vendor integrations (Role #4)

**Owns:**

- Bybit integration (P2).
- Additional data feed integrations (CoinGecko enhancements, Tradefeeds expansions, etc.).
- Connector reliability work (reconnect logic, drift detection — cross-ref `binance-bybit-integration-guard` skill).
- Project-scoped reliability improvements to the engine.

**Why project SOW, not retainer:**

- Each vendor integration has a defined start, scope, and end.
- Retainer model encourages scope drift; project model forces clarity.
- Founder retains code-review and architectural authority.

**Hiring profile:**

- Strong Python (asyncio, FastAPI, ccxt familiarity).
- Track record on at least one production exchange or trading-data integration.
- Comfortable with the engine's testing posture (unit + replay days corpus).

### Optional advisor (Role #5)

**Owns:**

- Monthly review participation (1 of 12 monthly exec reviews).
- One scheduled call/month for strategic discussion outside the review.
- No operating role. No decision authority. No equity unless formalized later.

**Why optional:** good advisors are unevenly available. Forcing the role for the sake of having "an advisor" produces theatre. A genuine advisor with limited time beats a structured advisor board with availability.

**Engagement model options (DECISION NEEDED):**

- Informal (no comp, no formal agreement).
- Light cash retainer ($500–1500/month).
- Equity (defer until first FT hire and a real cap table exists).

### Legal counsel — recurring (Role #6)

**Owns:**

- Quarterly ToS/DPA review.
- Jurisdictional posture review (UAE, MENA, US-blocked enforcement).
- B2B contracts as Desk Preview / Desk Full v2 customers emerge.
- DPA and data-handling reviews when vendors change.

**Why P2–P3 and not earlier:** project-basis legal work is sufficient through P1. A recurring retainer becomes worth the cost when contracts and jurisdictional questions become recurring, not one-off.

### First full-time hire (Role #7)

**Owns:** TBD by bottleneck observed across P2.

**Most likely candidates** (in order of expected probability):

1. **Trust Ops Lead** — formalize what the contractor has been doing; expand to multi-tier support.
2. **Engineering Generalist** — cover vendor work + dashboard + on-call rotation.
3. **Customer Operations** — bridge support, onboarding, and early sales functions.

**Decision rule:** whichever contractor has been the binding constraint for ≥3 months becomes the FT candidate. Either offer the role to that contractor, or hire to that role's profile if the contractor is not the right long-term fit.

### Customer Operations / Sales Lead (Role #8)

**Owns:**

- Desk Full v2 sales cycle execution (founder still leads, this role supports + scales).
- Per-seat customer success.
- Compliance-grade onboarding for fund customers.

**Why P5+:** before Desk Full v2 launches, this role has nothing to operate. Hiring it earlier creates a sales motion in search of a product.

### ML / regime specialist (Role #9)

**Owns:**

- Regime model evolution.
- Backtest coverage and statistical rigor.
- Replay days corpus expansion.

**Why so late:** the v3 ML regime classifier exists and is locked through P0–P2. The decision to bring on a specialist is gated by Desk Full v2 economics validating the spend, not by ambition.

### UX / design contractor (Role #10)

**Owns:**

- Activation flow iteration when in-house attempts plateau.
- Visual design polish for marketing surfaces.

**Why contingent:** activation flow is a founder priority through P2. Bringing on a UX contractor before founder has tried 2 iterations is delegating before the problem is understood.

## 3. Suggested hiring / order-of-ops support

Pre-activation (do in advance, not when triggered):

- **For Trust Ops contractor:** maintain a 2–3 person shortlist sourced over P1. Don't post a role; ask the network.
- **For Engineering contractor:** maintain a 2–3 person shortlist of trusted Python/exchange-integration freelancers from P1.
- **For bookkeeping:** identify a UAE-savvy bookkeeping firm or contractor before the first paid customer.
- **For legal:** keep current project-basis counsel on a known relationship; warm conversation about retainer terms ahead of P2.

Activation flow when a trigger fires:

1. **Confirm the trigger has actually fired** (not just feels like it). Document in `21-decision-log`.
2. **Validate the bottleneck is the role you think it is.** Sometimes the bottleneck is process, not headcount.
3. **Run a 1–2 week paid trial project** before any retainer / ongoing engagement.
4. **Document the SOW** with clear deliverables and end-state.
5. **Revisit fit at 30 days** before extending.

## 4. What NOT to hire too early

| Role | Why not yet |
|---|---|
| **CTO / Engineering Manager** | Founder is the engineer; layering management above zero engineers is theatre. |
| **CFO / Head of Finance** | Bookkeeping covers it through P5. |
| **CMO / Marketing Manager** | Founder voice is the channel. Hiring marketing before brand independence dilutes the only acquisition motion that's working. |
| **Head of Product** | Founder owns product. Until headcount supports a product team, this hire creates parallel decision authority. |
| **Sales / BDR / AE** | No outbound motion budgeted; inbound from `08-go-to-market` not yet validated. Sales hires before product-market fit are runway destroyers. |
| **Customer Success Manager** | Trust Ops covers the function until Desk Full v2 customers exist. |
| **Community Manager** | Community is built by founder voice + content; a hired community manager creates a "voice" disconnected from the product. |
| **DevRel / Developer Advocate** | We are not a developer-product. Wrong category. |
| **Data Analyst** | KPIs in `16-kpi-okr-system` are deliberately small; founder + bookkeeping covers the analyst load through P5. |
| **HR / Recruiter** | No team to manage; no recruiting volume to support a role. Founder + lightweight ATS covers any P3 hiring. |
| **Chief of Staff** | At our stage, a chief of staff adds alignment cost without removing operational load. Wrong stage. |

## 5. Contractor vs full-time considerations

| Dimension | Contractor | Full-time |
|---|---|---|
| **Test fit** | Easy — 30/60/90 day check-ins | Hard — termination is costly emotionally and legally |
| **Cost shape** | Variable, capped by hours | Fixed, regardless of utilization |
| **Equity exposure** | None at our stage | Yes — and equity policy is a real decision |
| **Cultural impact** | Low | High |
| **Operational coverage** | Capacity-flexed | Always-on |
| **Coordination cost** | Low | Medium-to-high |
| **Speed of activation** | Days to weeks | Weeks to months |
| **Risk of premature commitment** | Low | High |

**Stage rule:** every role through P3 starts as a contractor. Full-time conversion happens only when the contractor has been the binding constraint for ≥3 months and the founder explicitly decides to lock the cost.

## 6. Role sequencing logic

The sequence in §1 is not arbitrary. It follows three rules:

1. **Lowest-cost time-saver first.** Bookkeeping returns founder hours at the cheapest rate.
2. **Trust before scale.** Trust Ops activates before any growth-oriented role because trust posture is the constraint, not lead generation.
3. **Specialists last.** Generalists (Trust Ops, generalist engineer) come before specialists (ML, sales, UX) because at our stage the bottleneck is breadth, not depth.

Inverting any of these rules — e.g., hiring a sales lead before Trust Ops — sends the wrong internal and external signal and makes the company look like it is optimizing for revenue ahead of trust. That's exactly the opposite of the positioning in `05-positioning`.

## 7. The hiring rule that overrides every other rule

If a hire would compromise capital-preservation default or trust posture — **don't make the hire**, even if the role is "needed." A vacancy is recoverable. A trust-eroding hire takes years to recover from.
