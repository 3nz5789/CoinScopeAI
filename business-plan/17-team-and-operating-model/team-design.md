# Team Design

## 1. Stated posture

The smallest viable team for CoinScopeAI through P3 is:

- **Founder (full-time)** — single-threaded across product, engineering, GTM, trust, and ops.
- **Trust Ops contractor (part-time, P2 trigger)** — owns first-line support, incident triage, KB maintenance, gate-confusion ticket review.
- **Engineering contractor (project-based, P2 trigger)** — vendor integrations (Bybit at P2, additional data feeds), engine reliability work, scoped SOWs only.
- **Optional advisor (informal/paid, P1+ trigger)** — monthly review participant for outside perspective; not in the operating loop.

Full-time hire #2 is **not before P3** and is **dictated by where the bottleneck actually is at that moment**, not by a pre-defined org chart.

## 2. Core functions needed (and where they live now)

A trust-sensitive trading product has more functions than a generic SaaS. We list them honestly, then specify who currently carries them.

| Function | Current owner | Future owner trigger |
|---|---|---|
| Product strategy | Founder | Founder (durable) |
| Engineering — engine + scanner | Founder | + Engineering contractor (P2 vendor work) |
| Engineering — dashboard / web app | Founder | + Engineering contractor (selective, P3+) |
| ML / regime classification | Founder | Specialist contractor (P3+) — not before |
| Risk + safeguards ownership | Founder | Founder (durable; non-delegable) |
| Trust posture + public claims | Founder | Founder (durable; non-delegable) |
| Customer support — first line | Founder | Trust Ops contractor (P2) |
| Customer support — escalations | Founder | Founder (durable) |
| Incident management | Founder | Trust Ops contractor for triage; Founder for resolution |
| Onboarding flow design | Founder | + UX contractor (P3+) — only if activation rate plateaus |
| Content / GTM | Founder | Founder (founder voice is the channel; not delegable until brand is established) |
| Sales (Desk Full v2 cycle) | Founder | Founder, then sales contractor (P5+) |
| Finance / billing ops | Founder | Bookkeeping contractor (P2+, low cost, low overhead) |
| Legal / compliance | External counsel project basis | External counsel + retainer (P2+) |
| HR / hiring ops | Founder | Founder (durable until ≥3 hires) |
| Vendor management | Founder | Founder (durable; concentration risk requires single-threading) |

**Functions explicitly NOT yet needed:** Marketing manager, BDR/AE, Customer Success Manager, Data Analyst, DevRel, Community Manager. Each of these is the wrong hire at our stage.

## 3. Founder-heavy vs distributed execution — the tradeoffs

| Dimension | Founder-heavy (current) | Distributed earlier |
|---|---|---|
| **Speed of decision** | Highest — no coordination cost | Slower — alignment overhead |
| **Trust posture coherence** | Strong — single voice | Risk of fragmentation in early days |
| **Coverage during incidents** | Brittle — single point of failure | Better — but only if delegate is capable |
| **Cost** | Lowest — founder time only | Higher cash + coordination cost |
| **Bus factor** | 1 (highest risk) | 2+ (better) |
| **Scaling ceiling** | Hard ceiling at founder bandwidth | Higher, with cost |
| **Founder burnout risk** | High during incident weeks | Lower with right delegate |

**Verdict for current stage:** founder-heavy is correct for P0–P1. The bus-factor risk is real and is mitigated by:

- Documented runbooks (`13-support-and-trust-ops`).
- A nominated stand-in for incident communication (advisor or one trusted contact) — DECISION NEEDED.
- Operating cadence that surfaces brittleness before it becomes a crisis.

The cost of distributing earlier (P0–P1) is higher than the bus-factor it removes, *unless* the founder is genuinely incident-incapacitated, which is itself a risk to mitigate, not a hiring trigger.

## 4. Current-stage team design principles

1. **Single-threaded ownership over RACI matrices.** Every important thing has one owner. The owner can ask for help; they cannot share the accountability.

2. **Roles are activated by triggers, not by calendar.** "Hire when X" is a real plan; "hire in Q3" is a wish. Triggers live in `role-priorities.md`.

3. **Contractors before employees.** Through P3, every "team expansion" is a contractor first. Contractors test the role; employees lock the cost.

4. **Trust Ops is the first non-founder function to activate.** Not engineering. Founder can usually do another sprint of code; founder cannot scale to 4-hour incident response and 30-min ticket TTFR alone.

5. **Don't hire to a job description; hire to a bottleneck.** When a function consistently doesn't get done, that is a hiring trigger. When it gets done but slower than ideal, that is not.

6. **Geographic constraints are strategy, not preference.** UAE / MENA / global EN coverage matters for support timezone and trust signal — first contractor decisions should reflect this. (DECISION NEEDED.)

7. **No "chief of staff" hire.** A chief of staff at our stage compounds founder workload by adding alignment overhead without removing operational load. Reconsider only post-Series A or equivalent scale.

8. **Equity is reserved for full-time hires only.** Contractors get cash. Mixing equity into contractor relationships at this stage creates legal and motivational complications that aren't worth it.

9. **No advisor board.** A single trusted advisor with monthly time is plenty. A 5-person advisor board at our stage is theatre.

10. **Founder does GTM until brand is independent.** Founder voice is the channel. Hiring marketing before the brand has its own gravity is the most common early-stage mistake.

## 5. What can remain part-time / contractor-led

| Function | Why part-time/contractor is correct |
|---|---|
| Trust Ops (first line) | Predictable hours; can be capacity-flexed for incidents; doesn't require equity stake. |
| Engineering — vendor integrations | Project-shaped work, well-defined SOW, ends when integration ships. |
| Bookkeeping / finance ops | Low complexity, monthly batched, $100–500/mo replaces founder hours at much higher implicit rate. |
| Legal / compliance | Project basis until P2; light retainer at P2; never full-time at our stage. |
| Design / UX | Project basis only; no in-house designer through P3. |
| Content production polish | Optional editor / production contractor; founder still owns voice. |

## 6. What likely needs stronger ownership (sooner than feels comfortable)

| Function | Why this is the one to over-invest in |
|---|---|
| **Trust Ops contractor** | The only function whose absence creates a *brand* failure mode, not a *speed* failure mode. Activate at first sign of P1 monetization. |
| **Risk + Safeguards** | Non-delegable. Founder owns this through P5 unless deliberately re-decided. |
| **Public claims authority** | Single source of truth for what we say externally. Drift here is irreversible. |
| **Vendor management** | Concentration risk needs single-threaded ownership. A "shared" vendor relationship is how surprise invoices happen. |

## 7. Team risks to monitor

| Risk | Why it matters | Detection signal |
|---|---|---|
| **Founder bottleneck during incidents** | A 4-hour P1 incident with founder unavailable is an existential risk to trust posture. | Any P1 incident where MTTA exceeds threshold; founder availability gaps. |
| **Premature hire** | Locks 6–9 months of cash; creates coordination overhead before product is ready. | Hiring discussion driven by FOMO or external pressure rather than a documented bottleneck. |
| **Wrong first hire** | The first non-founder sets culture and signals priority. Wrong choice (e.g., growth marketer before Trust Ops) sends wrong signal internally and externally. | Hiring discussion that doesn't start from the actual bottleneck. |
| **Contractor → employee transition skipped** | Hiring full-time without contractor trial period removes the cheapest validation. | Pressure to "lock in" a contractor with equity instead of keeping them on cash for 3+ months. |
| **Single-point-of-failure on knowledge** | Founder is the only person who knows how the engine works. | No documentation in `13-support-and-trust-ops` runbooks; no nominated incident-comms stand-in. |
| **Vague trust ownership** | "We all care about trust" → no one owns trust → trust degrades. | Any trust-relevant decision (refund, public claim, gate change) made without a clear owner of record. |
| **Founder burnout** | Quiet, slow, hard to detect early; recovery is slow and expensive. | Founder hours by category drifting toward "support / ops" and away from "build / strategy." |
| **Geographic mismatch** | First hire in wrong timezone makes incident coverage worse, not better. | Hiring shortlist that doesn't optimize for coverage of MENA + global EN business hours. |

## 8. Near-term vs later-stage team design

### Near-term (P0–P2, May 2026 → Sep 2026)

- Founder + 1 Trust Ops contractor (P2 trigger) + 1 Engineering contractor (project basis, P2 trigger).
- Optional: 1 advisor in monthly reviews (P1+).
- Optional: bookkeeping contractor.

**Total non-founder cash exposure:** small. Most of the spend is still vendor + infra, not headcount.

### Medium-term (P3, late 2026 → early 2027)

- Founder + first full-time hire (role TBD by bottleneck — most likely candidates: Trust Ops Lead, Engineering generalist, or Customer Operations).
- Contractors retained selectively.
- Advisor relationship formalized.

**Decision rule:** the first full-time hire is whichever role has been a contractor for ≥3 months and consistently been the binding constraint.

### Later-stage (P5, Mar–May 2027 onward)

- Founder + 2–4 full-time staff covering: Engineering, Trust Ops, Customer Operations / Sales for Desk Full v2.
- Advisor or board structure if a fundraise occurs.
- ML / regime specialist: contractor first, full-time only if Desk Full v2 monetization validates.

**This is still a small team by SaaS standards.** That is intentional. CoinScopeAI's defensibility is built on engine quality, trust posture, and capital discipline — none of which scale linearly with headcount. Adding people faster than the product can absorb them dilutes both quality and culture.

## 9. The single team-design rule that matters most

**Hire to remove a documented bottleneck. Never hire to fill a role title.**

Every other rule in this folder follows from that one.
