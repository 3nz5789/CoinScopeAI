# Dependency Map

## 1. Why dependencies need a dedicated map

A roadmap that names milestones without naming dependencies is an opinion. A roadmap that names dependencies forces decisions to be honest. This map exists so:

- No workstream silently outruns its prerequisite.
- Pulling a milestone forward becomes visible: it forces another milestone to move with it.
- A bottleneck can be identified before it becomes a crisis.

## 2. Core dependency principles for CoinScopeAI

1. **Trust gates monetization.** A monetization milestone (M2, M5, M8) cannot reach "complete" without the corresponding trust readiness criteria being met first. This is not a soft preference — it is the structural backbone of the business plan.

2. **Stability gates expansion.** P2 vendor expansion does not start until P1 has stabilized. Expanding before stability multiplies risk, doesn't average it.

3. **Validation data gates KPI calibration.** TRAS knobs cannot be locked before real cohort data exists. Any KPI calibration on synthetic or assumed data is fictional precision.

4. **Decisions gate execution.** Several execution items wait on a decision-log entry, not on more work. Identifying decision blockers is half the value of this map.

5. **Founder time is itself a dependency.** A workstream where founder is the only contributor cannot run in parallel with another founder-only workstream of equal intensity. The map must reflect this.

---

## 3. Cross-workstream dependency table

Reads as: **Workstream X (row) depends on Workstream Y (column) being at state Z.**

**Notation:** `[seq]` = strict sequential gate (Y must be complete before X starts). `[par]` = parallel-allowed once Y is in flight (X can begin once Y is underway, doesn't need Y to be done).

| ↓ X depends on Y → | Product | Risk / Safeguards | Trust Ops | Onboarding | Pricing | GTM | Finance | Compliance | Team / Bandwidth |
|---|---|---|---|---|---|---|---|---|---|
| **Product (P1 narrow ship — M2)** | — | PCC v2 G3 ≥30 days stable [seq] | Runbook ≥80% (C-05) [seq] | Activation definition locked (D-01) [seq] | Tier matrix locked (A-03) [seq] | Disclosure language locked (C-04) [seq] | Stripe configured (F-05) [seq] | n/a | Founder bandwidth [par] |
| **Risk / Safeguards (G3 → G4)** | Engine telemetry stable [seq] | — | Incident postmortem cadence [par] | n/a | n/a | n/a | n/a | n/a | Founder authority (always present) |
| **Trust Ops (contractor active — G-01)** | Engine stability [seq] | Risk runbooks ready [seq] | — | n/a | Refund playbook published (C-05) [seq] | Disclosure language consistent (C-04) [seq] | Bookkeeping for refund audit (F-04) [par] | n/a | First paid customer in Pricing column |
| **Onboarding (D7 ≥60%, D30 ≥40%)** | Engine + signal pipeline stable [seq] | n/a | KB seeded (≥10 articles) [par] | — | Tier matrix locked (A-03) [seq] | Disclosure language locked (C-04) [seq] | n/a | n/a | Founder UX iteration cycles [par] |
| **Pricing (Trader live — M2)** | P1 narrow ship complete [seq] | All trust readiness criteria [seq] | Refund playbook (C-05) [seq] | Activation definition locked (D-01) [seq] | — | n/a | Stripe configured (F-05) [seq] | n/a | n/a |
| **GTM (founder content cadence)** | Honest claims posture (C-03 forbidden list) [seq] | n/a | n/a | n/a | Tier matrix as messaging (A-03) [par] | — | n/a | n/a | Founder bandwidth [par] |
| **Finance (vendor cost / revenue measured)** | First paid cohort exists [seq] | n/a | n/a | n/a | Trader live (M2) [seq] | n/a | — | n/a | Bookkeeping contractor active (F-04) [seq] |
| **Compliance (M7 posture upgrade)** | Per-seat features scoped [seq] | n/a | n/a | n/a | First Desk Preview customer or P3 entry [seq] | n/a | Counsel retainer active (legal — Role #6) [seq] | — | Founder + counsel calendar [seq] |
| **Team (Trust Ops contractor — G-01)** | Stable engine [seq] | Runbooks ready [seq] | — | n/a | First paid customer in system [seq] | n/a | Cash runway ≥9mo (Row 31) [seq] | n/a | Founder hiring authority (always present) |

**Read each row across to its dependencies.** A row's milestone cannot complete until every cell along its row reads "met."

**Founder bandwidth is itself a tracked KPI** (`kpi-map.md` §6 "Founder hours by category"). When in doubt, look at the log; don't estimate.

---

## 4. Major dependency chains

### Chain A+B — Product readiness AND Trust readiness → Trader monetization gate (AND-merge)

```
[Chain A: Product readiness]
PCC v2 G3 ≥30 days stable
+ Engine telemetry stable
+ Replay corpus ≥20
+ Connector-health 100% green ≥14d
                        \
                         \
                          → P1 narrow-ship decision (H-01)
                          /
                         /
[Chain B: Trust readiness]
Runbook coverage ≥80%
+ Disclosure language locked (C-04)
+ Refund playbook published (C-05)
+ Trust events: zero unresolved
                                ↓
                         AND-merge required
                                ↓
                  Trader $79/mo activated (M2)
                                ↓
                  NSM transition VCE → TRAS (H-04)
```

**Bottleneck:** PCC v2 G3 stability AND runbook coverage. Both must clear; ANDed, not ORed. Pulling either forward without the other is the most common monetization-readiness failure mode.

### Chain C — Cohort → KPI calibration → Phase transition

```
First paid cohort  →  D30 retention measured  →  TRAS knobs locked (H-04)
                                                         ↓
                                          P1 → P2 transition criteria reviewable
                                                         ↓
                                         If criteria met: P2 vendor expansion begins
```

**Bottleneck:** time. D30 retention requires 30 days of elapsed paid use. There is no shortcut.

### Chain D — Trust Ops activation

```
Engineering stable  +  Runbooks ready  +  First paid customer in system
                                ↓
                        Trial project (1–2 weeks) [G-01, G-02]
                                ↓
                   Trust Ops contractor activated
                                ↓
                    Founder time freed for:
            - P2 scope work
            - Strategic priorities
            - Quarterly review
```

**Bottleneck:** finding the right contractor. Sourcing should be in flight 30 days before the activation trigger. Founder hiring authority is always present (per `decision-rights.md` §9), so it is not listed as an input.

### Chain E — P5 Desk Full v2 launch (long-horizon)

```
P3 first FT hire activated
            ↓
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  ↓                                                     ↓
Compliance posture upgrade (M7)        Per-seat features built
  + DPA template                       + Audit-grade exports
  + Role-based access scaffolding      + Compliance-tested UI
  ↓                                                     ↓
  └────────────────────┬────────────────────────────────┘
                       ↓
            Desk Full v2 launch readiness (M8)
                       ↓
                First multi-seat customer
```

**Bottleneck:** compliance work, not engineering. Compliance posture upgrade is a documentation + legal workstream that runs in parallel with per-seat features but has independent counsel-availability dependencies.

---

## 5. Decisions that unblock other decisions

| Decision | Decision-log ID | What it unblocks | Cross-ref |
|---|---|---|---|
| Activation definition lock | **D-01** | KPI calibration; onboarding iteration; D7/D30 measurement; Free → Trader conversion measurement | `kpi-map.md` §2; `15-financial-framework` Row 6, 33–35 |
| Refund/credit playbook authoring | **C-05** | Trader monetization; Trust Ops scope; Stripe behavior; M2 trust readiness | `decision-rights.md` §7 |
| TRAS knob lock (N sessions, override threshold) | **H-04** | Weekly review interpretation; phase-transition criteria; NSM operating definition | `north-star-metric.md`; `kpi-map.md` §0a |
| Annual prepay policy | **B-01** | Stripe configuration; revenue model wording in GTM; refund exposure framing | `revenue-model.md` §4 |
| Per-seat rate ($149 vs $249) | **B-02** | Desk Full v2 economics; M8 milestone definition | `revenue-model.md` §3 |
| Discount policy posture | **B-03** | Tier-ladder integrity; refund playbook completeness; Trust Ops authority bounds | `decision-rights.md` §4 |
| Trial model (Free vs time-boxed paid) | **B-04** | Onboarding flow design; conversion path; Stripe configuration | `revenue-model.md` §3 |
| Founder internal rate (placeholder $100/hr) | **F-01** | Cost-recognition discipline; opportunity-cost framing of role decisions | `cost-structure.md` §9 |
| Disclosure language consistency check | **C-04** | Every public surface; M2 trust readiness; brand-voice integrity | `decision-rights.md` §6 |
| Incident comms stand-in | **C-06** | Bus-factor mitigation; escalation logic in `decision-rights.md` §10 step 4 | `decision-rights.md` §10 |
| Trust Ops engagement model (hourly vs project) | **G-02** | Contractor sourcing posture; cash exposure shape | `role-priorities.md` |
| Geographic constraints on hiring | **G-04** | Trust Ops sourcing radius; first-FT-hire pool | `team-design.md` §4 |
| First contractor activation timing | **G-01** | When founder time gets freed; Trust Ops scope expansion | `role-priorities.md` |
| Public transparency artifact yes/no | **C-02** | Trust messaging posture; what gets published when | `13-support-and-trust-ops` |
| Advisor activation | **G-05** | Monthly review participation; outside-perspective input | `team-design.md` |
| Validation status update on a load-bearing assumption | (per assumption row) | Assumption moves from "directional only" to "load-bearing in models" | `15-financial-framework/financial-assumptions.md` Validation Gate Rule |
| **Real-capital authorization** | **C-01** | **Not a decision; a defended posture.** Default firm NO. Communicated as a constraint, not a question. Pressure-resistant. | `decision-rights.md` §8 |

**Pattern:** decisions cluster. One unlocked decision often clears 2–3 others. Reviewing the decision log weekly catches stuck dependencies.

---

## 6. Likely sequencing bottlenecks

| Bottleneck | Why it bites | Mitigation |
|---|---|---|
| **Founder bandwidth** | Engine work, support work, content work, and hiring sourcing all compete for the same calendar | Use the cadence in `operating-cadence.md`; protect mornings for build, afternoons for ops; track via `kpi-map.md` §6 founder-hours-by-category |
| **PCC v2 G3 30-day clock** | No way to compress; calendar time is the cost | Begin the 30-day clock as early as possible; don't reset it on minor changes |
| **First cohort D30 retention measurement** | Cannot be measured before 30 days have passed since first paid customer | Don't promise stakeholders P1→P2 transition before D30+ has elapsed |
| **Trust Ops sourcing** | Right candidate not on demand; relationship-driven | Source 30 days ahead of activation trigger (QH-01) |
| **Vendor cost data** | First defensible measurement requires a full billing cycle of paid usage | Plan vendor-cost reviews to land at month-end after first paid customer, not earlier |
| **Runbook coverage** | Documentation feels low-priority until incident week, then catastrophic | Use weekly cadence to track coverage %, not as a project that's "done" |
| **Stripe + tax / regional posture** | UAE + MENA + global EN payment configuration has edge cases | Test transactions in real currencies before claiming Stripe-ready (F-05) |
| **Decision laundering between weekly reviews** | Slow drift in pricing, refund policy, or messaging without explicit log entry | Decision-log discipline is the only mitigation |
| **Cash runway <9 months** | When triggered, hiring + GTM spend pause; constrains all forward expansion | Track via `kpi-map.md` §6; alarm at 9-month floor (Row 31) |
| **External counsel availability** | Compliance work waits on counsel calendar; M7 posture upgrade gated | Engage counsel ahead of P3 entry, not at P3 entry |
| **Stale decision register entries** | OPEN-High decision >30 days old becomes a blocker on multiple downstream items | Monthly exec review forces stale-entry sweep (per `21-decision-log/README.md`) |
| **Notion mirror configuration** | If markdown and Notion drift, decisions land in inconsistent places | Lock I-01 (decision-log home) early; weekly verify |

---

## 7. What should NOT proceed before what

A short, blunt list of "do not start X before Y is complete." `Gate type` distinguishes whether the gate is **Time** (calendar elapsed, uncompressible), **State** (measurable threshold), or **Decision** (leadership choice required).

| Do not start | Until | Gate type | Cross-ref |
|---|---|---|---|
| Trader $79/mo activation | PCC v2 G3 ≥30 days stable + runbook ≥80% + refund playbook published | Time + State + Decision | M2; H-01; C-05 |
| NSM transition to TRAS | Trader is live AND first paid customer past activation | State | H-04 |
| TRAS knob lock | First paid cohort has D30 retention data | Time | H-04 |
| Bybit integration execution | P1 stabilization criteria met (M3) | State | H-02; M3 |
| Desk Preview $399/mo activation | P1 cohort D60 retention defensible AND vendor cost / revenue measured | Time + State | M5 |
| Trust Ops contractor activation | Engineering stable AND first paid customer in system AND trial project completed | State + Decision | G-01 |
| First full-time hire | Contractor has been binding constraint for ≥3 months | Time + State | G-06 |
| Paid acquisition spend | Cohort retention defensible AND refund rate <2% AND trust posture publicly defensible | State | E-02 |
| Annual prepay launch | PCC v2 G4 ≥60 days stable | Time + State | B-01 |
| Desk Full v2 launch | Per-seat features built + compliance posture upgraded + first multi-seat customer in pipeline | State + Decision | M8 |
| Real-capital authorization | §8 Capital Cap criteria fully met (no calendar substitute) | State | C-01 |
| Compliance posture upgrade | First Desk Preview customer with B2B contract requirements OR explicit P3 entry | State + Decision | M7 |

This list is **the inversion** of the dependency table — same content, blunter language. When in doubt, read this list.

**Reading the gate type:**

- **Time gates** are uncompressible. Calendar time is the cost.
- **State gates** can be accelerated by hardening work.
- **Decision gates** can be unblocked by a single founder action.

Identifying the gate type tells you which lever to pull.

---

## 8. Practical dependency summary for operators

If you only remember four things from this map:

1. **PCC v2 G3 stability gates everything in the next 90 days.** Not "should gate" — gates. If G3 is not stable, the calendar moves but the milestones do not.

2. **Trust readiness is a separate gate from launch readiness.** A product can ship and still not be trust-ready. Both gates must clear before any monetization milestone is declared complete.

3. **Founder time is a finite, non-fungible resource.** If two founder-only workstreams are in flight simultaneously, one is implicitly being de-prioritized. Naming which one is honest planning; ignoring the conflict is wishful planning.

4. **Security incidents have a separate dependency chain.** Containment is in-band; counsel + Founder concur is the gate before any other action. See `decision-rights.md` §10A. Operational incident runbooks do NOT apply to security incidents.

---

## 9. How to use this map

- At every weekly review: scan §7 to confirm nothing has been silently violated.
- At every monthly exec review: walk through §4 dependency chains and identify the binding constraint of the moment.
- At every phase transition: full re-baseline of §3 dependency table; update if any cells have changed state.
- At every decision-log entry: cross-check whether the decision unblocks anything in §5. If yes, propagate.
- At every contractor role activation (Trust Ops, Engineering, Bookkeeping, etc.): update §3 cells to reflect new ownership; remove activation as a dependency in chains where it appeared.

**Loggable threshold:** dependency-state changes that affect pricing, claims, refunds, hiring, vendor concentration, risk thresholds, or roadmap dates are loggable per `21-decision-log/README.md`. Cell changes in §3 are auto-logged via §12 version history below.

---

## 10. The dependency rule that overrides all others

**A pulled-forward milestone forces an equally pulled-forward dependency.** If a stakeholder, deadline, or impulse pulls M2 (P1 narrow-ship) forward by 2 weeks, every dependency in §3 row "Product" must also move forward by 2 weeks. If any dependency cannot move (e.g., PCC v2 G3 30-day clock — a Time gate), the milestone cannot move either.

**Worked example:** an advisor recommends moving Trader live two weeks earlier to capture a market window. Reading §3 row "Pricing": Trader live depends on `P1 narrow ship complete`, `All trust readiness criteria`, `Refund playbook (C-05)`, `Activation definition locked (D-01)`, and `Stripe configured (F-05)`. Each must move 2 weeks earlier. PCC v2 G3 stability is a Time gate — uncompressible. Therefore the milestone cannot move. The right answer is to maintain the original date and decline the recommendation, or to start the G3 clock earlier (which can be done now), not to compromise the dependency.

This rule is the structural protection against the most common failure pattern in trust-sensitive trading products: collapsing dependencies under pressure and then discovering at first incident that the trust posture was never actually validated. The dependency map exists so that the collapse cannot happen quietly.

---

## 11. Cross-references

| Topic | Where to look |
|---|---|
| Decision-log register (active decisions, IDs in §5 and §7) | `21-decision-log/leadership-decision-register.md` |
| Open questions register (IDs prefixed QA, QD, QE, QF, QG, QH, QI) | `21-decision-log/open-questions-register.md` |
| Financial assumptions (Row references in §3 and §6) | `15-financial-framework/financial-assumptions.md` |
| KPI map (KPIs that measure dependency state) | `16-kpi-okr-system/kpi-map.md` |
| Decision rights (decisions that unblock dependencies) | `17-team-and-operating-model/decision-rights.md` |
| Milestone definitions (M1–M9 referenced in §4 and §7) | `18-roadmap/milestone-framework.md` |
| Operating cadence (review frequencies referenced in §9) | `17-team-and-operating-model/operating-cadence.md` |
| Pre-mortem skill (required for canonical changes) | Memory: `reference_skill_risk_pcc_pre_flight.md` |
| Validation Gate Rule (governs unvalidated assumption use) | `15-financial-framework/financial-assumptions.md` §"Validation Gate Rule" |

---

## 12. Version history

Append-only log of changes to this file. Format: `YYYY-MM-DD — change summary — Decision-log ID (if applicable)`.

| Date | Change | Decision-log ID |
|---|---|---|
| 2026-05-08 | Initial version published as part of Wave 3 generation | — |
| 2026-05-08 | Cleanup pass: added decision-log IDs to §5; expanded §5 from 10 to 17 rows; reframed real-capital row as defended posture; standardized §3 cell semantics (added D-01, C-04, C-05, F-04, F-05 IDs); added Compliance as workstream row + column; added [seq]/[par] notation; merged Chain A+B with explicit AND-merge; removed "Founder hiring authority" from Chain D; expanded §6 from 8 to 12 bottlenecks; added Gate type + Cross-ref columns to §7; added 4th security-incident principle to §8; added §11 Cross-references; added §12 Version history; added contractor activation as 5th cadence trigger in §9; added worked example to §10 | — |

---

*Last reviewed: 2026-05-08. Reviewed at every weekly review (§7 scan), monthly exec review (§4 chain walk-through), phase transition (full re-baseline), decision-log entry (§5 propagation check), and contractor role activation (§3 ownership update).*
