# Decision Rights

## §0. Decision-rights principles

Five rules that govern how the rest of this file is read. They override individual row interpretations.

1. **Single-threaded accountability.** Co-owners are visibility, not accountability. One named role owns each decision. Layered ownership (e.g., Trust Ops within a playbook; Founder of the playbook) is acceptable; shared accountability is not.
2. **Fail-safe defaults.** When in doubt, the default is the safer position: no real capital, no discount, no public claim, no rollback-forward. The default is the *non-action* state.
3. **Escalate when uncertain.** Over-escalation costs less than under-escalation at our stage. The bias is intentional and correct.
4. **Irreversibility weighting.** Decisions that compound (claims, prices, real-capital authorization) get more authority guardrails than reversible ones (KPI band tweaks, content cadence). The §2 `Reversibility` column makes this explicit.
5. **Pre-mortem for canonical changes.** Risk thresholds, PCC v2 gates, NSM definition, and TRAS knobs require a pre-mortem (per `pre-mortem` skill memory) before the first edit. Skipping pre-mortem is a process violation, not a stylistic preference.

---

## 1. Why this file exists

Vague ownership is how trust posture quietly degrades. At our stage, **almost everything is decided by the founder** — but "the founder decides everything" is not a useful operating model. Some decisions are non-delegable; some can be delegated to contractors today; some will move as the team grows.

This file makes the boundaries explicit so that:

- Contractors know what they can and cannot decide unilaterally.
- The founder doesn't accidentally delegate a non-delegable decision under time pressure.
- Every category has a documented escalation path.
- Decisions that are made get logged in `21-decision-log` consistently.

The file is the **moment-of-decision artifact**: an operator at 9pm during a stress event reads this row, knows whether to act or escalate, and acts.

---

## 2. Decision categories at a glance

**Loggable threshold:** decisions that affect pricing, claims, refunds, hiring, vendor concentration, risk thresholds, or roadmap dates are loggable in `21-decision-log` per its README. Everything else is an operational note.

| # | Category | Decider (current) | Reason / failure mode prevented | Reversibility | Delegation / Escalation | Logging | Decision-log ID |
|---|---|---|---|---|---|---|---|
| 1 | Product strategy + roadmap | Founder | Strategic coherence; phase-gate integrity | Costly to reverse | Never delegated | Logged at phase transition | A-04 |
| 2 | Engineering architecture | Founder | Architectural drift compounds | Costly to reverse | Engineering contractor: implementation choices within approved SOW | ADR per `business-plan/06-product-strategy/` | — |
| 3 | Risk + safeguard rules (PCC v2, gates, kill-switch logic) | Founder | Catastrophic + irreversible if wrong | Effectively irreversible | **Never delegated** | Logged immediately | A-05 |
| 4 | Real-capital authorization (§8 Capital Cap) | Founder | Single most consequential decision | Effectively irreversible | **Never delegated. Cannot be made in founder absence.** | Logged immediately + cross-ref §14 | C-01 |
| 5 | Pricing — list prices for any tier | Founder | A single ad-hoc discount resets the floor | Costly to reverse | Never delegated | Logged + monthly review | A-03 |
| 6 | Pricing — discount precedents | Founder | Floor-reset risk per §4 below | Costly to reverse | **No discount may be granted by anyone other than founder, ever** | Logged | B-03 |
| 7 | Pricing — annual prepay policy | Founder | Cash vs refund-wave exposure | Costly to reverse | Never delegated | Logged | B-01 |
| 8 | Pricing — per-seat rate (Desk Full v2) | Founder | Anchors fund-tier economics | Costly to reverse | Never delegated | Logged at lock | B-02 |
| 9 | Pricing — trial model | Founder | Shapes onboarding + conversion | Reversible | Never delegated | Logged at lock | B-04 |
| 10 | Public-facing claims (marketing, social, brand voice, press) | Founder | Wrong claim compounds permanently | Effectively irreversible | **Never delegated** | Logged for material claims | C-03 |
| 11 | Disclosure language ("Testnet only…") | Founder | Surface drift = trust drift | Reversible (but easy to miss the drift) | Never delegated | Logged | C-04 |
| 12 | Transparency artifact publication (validation cohort summary) | Founder | Trust signal vs disclosure-risk tradeoff | Costly to reverse | Never delegated | Logged when published | C-02 |
| 13 | Refund — standard (within playbook) | Trust Ops contractor (when active) | Routine support hygiene | Reversible | Within published rules; otherwise → Founder | Auto-logged | C-05 |
| 14 | Refund — non-standard (>1 month tier, or incident-tagged, or Desk Full v2) | Founder | Trust-event coupling; refund-wave risk | Costly to reverse | Never delegated | Logged immediately | C-05 |
| 15 | Support response within playbook | Trust Ops contractor (when active) | Operational throughput | Reversible | Within playbook; Founder owns playbook itself | Per ticket | — |
| 16 | Support playbook authorship + revisions | Founder | Playbook drift = trust drift | Costly to reverse | Never delegated | Logged at revision | C-05 |
| 17 | Incident triage (severity, ack, paging) | Trust Ops contractor (when active) | Per runbook | Reversible | Per runbook; escalates per §10 | Auto-logged | — |
| 18 | Incident resolution + postmortem | Founder | Engine-behavior interpretation | Costly to reverse | Never delegated | Logged per incident | — |
| 19 | Security incident response (data exposure, key leak, account compromise) | Founder + external counsel | Different escalation path; legal exposure | Effectively irreversible if mishandled | **Never delegated.** Counsel involvement within 1 hour of detection | Logged immediately + counsel record | (open category) |
| 20 | Vendor selection + concentration | Founder | Concentration risk needs single-threaded ownership | Costly to reverse | Never delegated | Logged | — |
| 21 | Vendor day-to-day (renewals within budget, normal usage) | Founder | Operational | Reversible | Bookkeeping for billing only | Bookkeeping logs | — |
| 22 | GTM channel selection | Founder | Channel choice shapes brand | Reversible | Never delegated | Logged when new channel activates | E-01, E-03 |
| 23 | Paid acquisition activation | Founder | Premature paid spend = low-quality cohort | Costly to reverse | Forbidden until P3+ AND criteria in E-02 met. Activation is loggable | Logged at activation | E-02 |
| 24 | Content publication (founder voice) | Founder | Founder voice is the channel | Reversible | Production / scheduling logistics may be delegated; final-call stays with founder | Logged for material claims | — |
| 25 | KPI definition changes (NSM, TRAS knobs, KPI map row revisions) | Founder | Definition drift = silent metric tampering | Costly to reverse | Never delegated. **Phase-transition or quarterly cadence only**, not weekly | Logged immediately | A-07, H-04 |
| 26 | Validation gate rule application (using unvalidated assumption in a model) | Founder | Fictional precision in models compounds | Reversible | Never delegated | Logged with assumption row reference | — |
| 27 | Hiring decisions (any role) | Founder | First-hire stakes are highest in company history | Costly to reverse | Never delegated | Logged at offer | G-01–G-06 |
| 28 | Compensation decisions | Founder | Sets internal precedent | Costly to reverse | Never delegated | Logged at offer | G-06 |
| 29 | Contractor SOW approval | Founder | Scope discipline | Reversible | Never delegated | Logged at SOW signing | G-02, G-03 |
| 30 | Termination decisions | Founder | Cultural + legal weight | Effectively irreversible | Never delegated | Logged with reason | — |
| 31 | Legal / compliance posture | Founder + external counsel | Regulatory exposure | Costly to reverse | Counsel for technical drafting; Founder retains call | Logged | QE-01, QE-03 |
| 32 | Compliance posture changes (jurisdictional) | Founder + external counsel | Material regulatory exposure | Effectively irreversible | Counsel involvement mandatory | Logged immediately | A-06 |
| 33 | US-blocked enforcement-bypass incident | Founder | Regulatory exposure if leaked | Costly to reverse | Treated as a security incident; per §10A escalation | Logged immediately | A-06, QE-02 |
| 34 | Decision-log curation (status updates, supersession entries, register hygiene) | Founder | Register integrity | Reversible | Never delegated | Auto-logged via the register | I-01 |

---

## 3. Product decisions

**Decided by:** Founder.

**What's in scope:**

- Roadmap **prioritization within a phase** (which features ship in P1 narrow scope, etc.).
- **Phase transitions** — gated per `18-roadmap/milestone-framework.md`. Forward-only by default; backward movement requires explicit decision-log entry per H-05.
- Feature inclusion / exclusion.
- Engine architecture changes (Architecture Decision Record filed in `business-plan/06-product-strategy/` per the engineering ADR convention).
- ML model revisions.
- Activation flow design (`12-onboarding-and-activation`); cross-ref D-01 (activation definition lock).
- API surface changes.

**What's NOT delegable:** any decision that affects the engine's capital-preservation behavior. These touch §14 risk-compliance and §8 Capital Cap.

**What CAN be delegated when applicable contractor active:**

- Engineering contractor: implementation choices within an approved SOW (e.g., specific library version, internal API shape) — provided architectural posture is preserved.
- UX contractor (P3+ contingent — activation requires D-02 trigger): visual / interaction details within an agreed flow.

**Logging:** roadmap and architecture decisions are logged at phase transitions and at any material change. Material = anything affecting an active milestone, a §14 risk threshold, or a public-facing claim.

---

## 4. Pricing decisions

**Decided by:** Founder. Not delegable through P5.

**The discount-floor rule (load-bearing):**

> Discount precedents are list-price implications. A single discount granted to one customer becomes the de facto floor for the next 5 customers asking. Therefore: **no discount is approved without an explicit policy entry in `21-decision-log`. Trust Ops cannot grant a discount under any circumstance — only published refunds and credits per §7 below.**

**What's in scope:**

- List prices for any tier (`21-decision-log` A-03).
- Discount policy (whether to offer; what magnitude; for whom — B-03).
- Annual prepay policy and timing (B-01; cross-ref `15-financial-framework/revenue-model.md` §4).
- Per-seat rates for Desk Full v2 ($149 or $249 — B-02, deadline 2026-12-31).
- Trial model (B-04, deadline 2026-06-30).
- Regional pricing variants (B-05 — deferred to P3+).

**What's NOT delegable:** anything that touches list price or that creates a precedent for discounting.

**What CAN be delegated:**

- Trust Ops can apply *published* refund rules without escalation, within the dollar threshold defined in §7.
- Trust Ops can offer a *published* goodwill credit (up to 1 month of the customer's tier) under explicit playbook conditions.

**Escalation path:** any pricing-adjacent customer ask not covered by the published refund/credit playbook → Founder, same-day if possible.

**Logging:** every list-price change, discount precedent, and annual policy revision is logged in `21-decision-log` and revisited in the monthly exec review.

---

## 5. GTM decisions

**Decided by:** Founder.

**What's in scope:**

- Channel selection (content, founder voice, community presence, **eventual paid — gated**).
- Brand voice and message pillars.
- Content production cadence and formats (E-01).
- Partnership and co-marketing decisions (deferred to Phase 4 per `99-task-backlog/phase-4-backlog.md`).
- Any external-facing claims about the product.

**Paid acquisition specifically (E-02):** **forbidden until P3+ at earliest**, and only after explicit trigger criteria (cohort retention defensible, refund rate <2%, trust posture publicly defensible) are met. Activation is a Founder decision with explicit `21-decision-log` entry. Until activation, paid acquisition is **forbidden**, not deferred.

**What's NOT delegable:**

- Founder voice is not delegable. A ghostwriter or editor may polish, but final-call authority on what is published under founder name stays with the founder.
- Public claims about the product (cross-ref §6 below).
- Paid acquisition activation (per above).

**What CAN be delegated:**

- Production / scheduling logistics (when role activated).
- Editing / formatting polish.
- Distribution mechanics within an approved (Founder-signed-off) plan.

---

## 6. Trust and public-claims decisions

**Decided by:** Founder. Single-threaded. Non-delegable.

**Why this category gets its own section:**

A wrong claim in a marketing post, an oversold capability in a sales call, or a premature performance reference compounds permanently. Recovery costs orders of magnitude more than the upfront discipline.

**What requires founder sign-off, always:**

- Any claim about engine performance, signal quality, or risk-gate behavior.
- Any reference to backtest results in external materials.
- Any statement that could be read as performance attribution to user P&L.
- Any positioning claim about regulatory status or jurisdictional posture.
- Any public response to an incident or trust event (response speed is governed by the runbook in `13-support-and-trust-ops`).
- Any change to the disclosure language ("Testnet only. 30-day validation phase. No real capital.") — C-04.
- Any comparative claim about competitors.
- Any decision to publish (or not publish) a transparency artifact — C-02.

**What is explicitly forbidden, regardless of who proposes it:**

- Marketing language implying real-capital trading is approved when it isn't.
- Performance projections.
- Any wording that conflates the subscription with returns to the user.
- Any wording that minimizes or hides the §14 risk posture.
- Comparative claims that disparage competitors without substantiation.

**Logging:** any material public claim is logged with the source of authority.

---

## 7. Support and escalation decisions

**Decided by:** Trust Ops contractor (when active), within explicit playbook bounds. Founder above the playbook.

**Refund and credit dollar threshold (defined):**

| Tier | Trust Ops authority | Hard cap per ticket | Escalation trigger |
|---|---|---|---|
| Trader ($79/mo) | Refund up to 1 month ($79); goodwill credit up to 1 month | $79 | >1 month, or incident-tagged |
| Desk Preview ($399/mo) | Refund up to 1 month ($399); goodwill credit up to 1 month | $399 | >1 month, or incident-tagged |
| Desk Full v2 ($1,199/mo + per-seat) | **Always escalates**, regardless of amount | $0 (no Trust Ops authority) | All Desk Full v2 refunds → Founder |

**Within Trust Ops authority (when active, when published rules cover it):**

- Standard ticket responses per playbook.
- Refund within published threshold (table above).
- Goodwill credit within published rules (up to 1 month tier value).
- Severity-tagging and triage per runbook.
- KB article drafting (Founder reviews **material** updates — material = changes that touch gate behavior, refund policy wording, or any §14 risk reference).

**Requires founder authority:**

- Refund ≥ threshold or any Desk Full v2 refund.
- Refund tied to an incident or trust event (any incident-tagged ticket).
- Any response involving public-facing language about a trust event.
- Any escalation that involves engine behavior interpretation.
- Any compensation arrangement for a customer beyond standard refund/credit.
- Any KB article that touches §14 risk language.

**Escalation path:** Trust Ops → Founder (same-business-day for P1/P2 incidents; next-business-day for P3 routine). When Founder is unavailable, see §10.

**Logging:** every refund or non-standard credit is auto-logged with reason and amount; founder-authored responses get tagged separately.

---

## 8. Risk and safeguard decisions

**Decided by:** Founder. **This is the most non-delegable category in the entire framework.**

**What's in scope:**

- PCC v2 gate transitions (G1 → G2 → G3 → G4) — A-05.
- §8 Capital Cap state changes — C-01.
- Kill-switch logic changes.
- Risk threshold changes (10x leverage cap, 10% MDD, 5% daily loss, 3 max positions, 80% heat).
- Engine version rollback decisions (with the carve-out below).
- Real-capital authorization (default: NO; never delegated) — C-01.

**What is NOT delegable, ever:**

- Real-capital authorization. **Cannot be made in founder absence under any circumstance.** Default state is "no real capital" — that default is fail-safe.
- Backward gate movement decisions (the *decision* is non-delegable; the *process* is defined in `18-roadmap/milestone-framework.md` §7).
- Kill-switch override (manual disabling of a fired kill-switch).
- Risk threshold relaxation.

**Engine rollback — with explicit fail-safe carve-out:**

Engine rollback is normally a Founder decision. **Exception:** during a documented active incident where the engine's continued operation poses an active capital-preservation risk **AND** Founder is unreachable, Engineering may roll back to last known-good per the deployment runbook. The carve-out applies because rollback is reversible; a forward deploy under the same conditions is **NOT** permitted. Engineering must notify Founder same-day; the action is logged immediately; Founder reviews on availability.

**Pre-mortem requirement (cross-ref `pre-mortem` skill memory):** any change to canonical risk posture (thresholds, gates, NSM definition, TRAS knobs) must run a pre-mortem before the first edit. Skipping this is a process violation, not a stylistic preference.

**Logging:** every risk decision is logged immediately, in `21-decision-log` and the engine repo, with timestamp and rationale.

---

## 9. Hiring decisions

**Decided by:** Founder. Through P5.

**What's in scope:**

- Activation of any role on the priority list (`role-priorities.md`) — G-01 through G-06.
- Selection of specific contractors / hires.
- Offer terms (cash, hours, project scope).
- Termination decisions.
- Conversion of contractor to full-time.
- Compensation framework decisions (deferred per `team-design.md` §4 until first FT hire).
- Equity policy for first FT hire (G-06 — deferred decision; required before P3 hire).

**What CAN be delegated:**

- Sourcing logistics (e.g., a recruiter or referral channel) — but Founder still makes the offer.
- Reference checks (when a trusted advisor is willing to do them).

**Termination grounds:**

- Contractor: unmet deliverables per SOW, scope drift, communication breakdown, security/trust violation.
- Full-time (P3+): documented performance issues, trust violation, or strategic role-elimination. Process to be documented at first FT hire activation.

**Logging:** every offer and every termination is logged with date, role, terms, and reason.

---

## 10. Decision escalation logic

When decisions are unclear or contested:

1. **Check this file first.** If the category is named, the decider is named.
2. **If a contractor is uncertain about authority,** default to escalation to Founder. Better to over-escalate than to make a non-delegable decision (cross-ref §0 principle 3).
3. **If founder is unavailable during a P1/P2 incident:**
   - Trust Ops follows incident runbook (`13-support-and-trust-ops`) for triage and acknowledgment.
   - Engineering may roll back to last known-good version per the §8 fail-safe carve-out — only if the engine's behavior poses an active capital-preservation risk. Forward deploys are not permitted.
   - **Real-capital decisions cannot be made in founder absence.** Default state is "no real capital" — that default is fail-safe.
4. **If founder is unavailable >24 hours during a non-incident period:**
   - **Stand-in identity:** TBD per `21-decision-log` row **C-06** (deadline 2026-06-30). Until C-06 closes, founder unavailability >24h triggers a **no-decision posture** across all categories — Trust Ops continues triage per runbook, no escalations or commitments are made, no SOWs signed, no public communications issued.
   - When C-06 closes, the documented stand-in handles communication only. No operational, financial, or risk decisions are delegated even in extended absence.

---

## 10A. Security incident escalation (separate path)

Security incidents are categorically different from operational incidents and have their own escalation path.

**Trigger events:** discovered API key leak, customer data exposure, account compromise, exchange-credential exposure, signing-key exposure, vendor breach affecting CoinScopeAI data.

**Escalation:**

1. Detection → containment (no system change beyond containment without authority).
2. Founder + external counsel notified within **1 hour** of detection.
3. **No public communication, no customer communication, no system change beyond containment** until counsel and Founder concur.
4. Regulatory disclosure timing per counsel, per jurisdictional posture (UAE / MENA / global EN — A-06).
5. Postmortem + remediation plan within 7 days.

**Logging:** logged immediately in `21-decision-log` + counsel record. Cross-link to incident log.

**Why this is separate:** operational incidents have known runbooks. Security incidents have legal, customer-trust, and regulatory dimensions that can't be runbook-driven without counsel involvement.

---

## 11. What must NOT be left ambiguous

Listed here as a final checklist:

| Decision | Must have a single named decider |
|---|---|
| Real-capital authorization | ✓ Founder (cannot be made in absence) |
| PCC v2 gate transitions | ✓ Founder |
| Risk threshold changes | ✓ Founder |
| List-price changes | ✓ Founder |
| Discount precedents (any) | ✓ Founder |
| Public claims and brand voice | ✓ Founder |
| Disclosure language | ✓ Founder |
| Transparency artifact publication | ✓ Founder |
| Refund and credit playbook authorship | ✓ Founder |
| Refund non-standard / Desk Full v2 / incident-tagged | ✓ Founder |
| KPI definition changes (incl. NSM, TRAS knobs) | ✓ Founder |
| Validation gate rule application | ✓ Founder |
| Paid acquisition activation | ✓ Founder (forbidden until P3+ criteria met) |
| Hiring and termination | ✓ Founder |
| Vendor selection and concentration | ✓ Founder |
| Compliance posture changes | ✓ Founder + external counsel |
| Security incident response | ✓ Founder + external counsel (within 1 hour) |
| Incident communication external messaging | ✓ Founder |
| Engine rollback (with §8 fail-safe carve-out only) | ✓ Founder |
| Decision-log curation | ✓ Founder |

**Rule:** if a decision in any of these areas is being made *without* explicit founder sign-off (or, where applicable, without external counsel), that itself is the incident.

---

## 12. How this file evolves

- At every phase transition, review whether any decision categories should move from "Founder" to a new role.
- When a role activates (e.g., Trust Ops contractor at P2), add their authority bounds to this file in the same week.
- When a decision is contested in practice, log the contest itself in `21-decision-log` and update this file if the boundary needs to shift.
- This file is not a one-shot artifact; it is a living contract that should change as the team changes.
- All changes to this file are logged in §14 below.

The single rule that makes the rest of this file work: **any time a contractor or future hire is uncertain whether they have the authority to decide, the answer is escalate.** That bias is correct at our stage and erring toward over-escalation costs less than erring toward under-escalation.

---

## 13. Cross-references

| Topic | Where to look |
|---|---|
| Decision-log register (active decisions) | `21-decision-log/leadership-decision-register.md` |
| Open questions upstream of decisions | `21-decision-log/open-questions-register.md` |
| KPI ownership transitions | `16-kpi-okr-system/kpi-map.md` §11 |
| Phase-transition discipline | `18-roadmap/milestone-framework.md` §7 |
| Risk thresholds (10x leverage, 10% MDD, 5% daily loss, 3 max pos, 80% heat) | `14-risk-compliance-and-safeguards/` + memory |
| Pre-mortem skill | Memory: `reference_skill_risk_pcc_pre_flight.md` |
| Refund/credit playbook (when authored) | C-05 in decision register |
| Stand-in protocol | C-06 in decision register (currently OPEN) |
| Loggable threshold definition | `21-decision-log/README.md` §"Status placeholder" |
| Engineering ADR convention | `business-plan/06-product-strategy/` (when ADRs accumulate) |
| Validation gate rule (financial assumptions) | `15-financial-framework/financial-assumptions.md` §"Validation Gate Rule" |

**Decisions ↔ KPIs pairing:** decisions in this file set policy; KPIs in `kpi-map.md` measure adherence. §6 of this file (Trust + claims) is measured by §4 of the KPI map (Trust + Support KPIs). §8 of this file (Risk + safeguards) is measured by §5 of the KPI map (Risk + Safeguard KPIs). §4 of this file (Pricing) is measured by §6 of the KPI map (Financial KPIs).

---

## 14. Version history

Append-only log of changes to this file. Format: `YYYY-MM-DD — change summary — Decision-log ID (if applicable)`.

| Date | Change | Decision-log ID |
|---|---|---|
| 2026-05-08 | Initial version published as part of Wave 3 generation | — |
| 2026-05-08 | Cleanup pass: added §0 principles; defined refund dollar thresholds; eliminated co-ownership; reconciled §8/§10 engine rollback carve-out; added 8 missing decision categories; added cross-links to decision-log IDs; added §10A security incident path; expanded §11 checklist; added §13 cross-references; added §14 version history | — |

---

*Last reviewed: 2026-05-08. Reviewed at every phase transition, every contractor role activation, and every contested decision. Any change to this file is logged in §14.*
