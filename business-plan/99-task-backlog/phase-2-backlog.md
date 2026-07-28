# Phase 2 Backlog — Packaging, Pricing, GTM, Onboarding, Support, Safeguards

## Phase 2 scope

**Monetization readiness with discipline.** Phase 2 turns the validated foundation into a defensible Trader-tier monetization path. Heavy emphasis on the playbooks, configurations, and operational hooks that must be in place before charging the first user.

**Time horizon:** ~30–60 days (post Phase 1 exit).

**Phase exit criteria:**

- Refund/credit playbook published; Stripe configured; Trader $79/mo SKU activated.
- First paid customer flow validated end-to-end.
- Onboarding flow first-iteration shipped against real cohort signal.
- Trust Ops contractor sourcing complete; trial project initiated.
- US-blocked enforcement audited.

---

## Section A — Pricing and packaging configuration

**[DOC] PRICING — Lock discount policy posture pre-P2**
- Objective: decide discount stance before Trader live.
- Why it matters: protects tier-ladder defensibility.
- Dependency: B-03; Phase 1 complete.
- Expected output: policy memo; register update.

**[DOC] PRICING — Lock trial model (Free as trial vs time-boxed)**
- Objective: confirm Free tier as trial.
- Why it matters: shapes onboarding flow + conversion path.
- Dependency: B-04; first cohort feedback.
- Expected output: trial-model memo.

**[DOC] TRUST — Author refund/credit playbook v1**
- Objective: produce playbook with explicit thresholds + Trust Ops scope.
- Why it matters: gates Trader monetization.
- Dependency: tier matrix; `decision-rights.md` §7.
- Expected output: playbook published internally.

**[BUILD] PRICING — Configure Trader $79/mo SKU in Stripe**
- Objective: production-ready Stripe configuration.
- Why it matters: required for Trader live.
- Dependency: refund playbook; Stripe testing.
- Expected output: Trader SKU live in Stripe.

**[QA] FINANCE — Test Stripe end-to-end (signup, billing, refund) in MENA + global EN currencies**
- Objective: confirm monetization mechanics work cleanly.
- Why it matters: F-05 readiness.
- Dependency: Stripe sandbox + test accounts.
- Expected output: test-transaction log; sign-off.

---

## Section B — GTM activation

**[GTM] GTM — Establish founder content cadence (1–2 substantive pieces/week)**
- Objective: lock cadence + topic backlog.
- Why it matters: only acquisition channel pre-P3.
- Dependency: founder time allocation.
- Expected output: 8-week content plan; first piece shipped.

**[RESEARCH] MARKET — Test MENA-targeted vs global EN content performance**
- Objective: side-by-side performance measurement.
- Why it matters: anchors E-03 channel decision.
- Dependency: 4 weeks of attributed content.
- Expected output: comparison memo.

**[GTM] BRAND — Audit messaging consistency across landing surfaces**
- Objective: confirm brand voice + tier framing aligned to `05-positioning`.
- Why it matters: trust-aligned conversion.
- Dependency: surface inventory.
- Expected output: corrections applied.

---

## Section C — Onboarding and activation iteration

**[DOC] ONBOARDING — Lock activation definition for KPI use**
- Objective: define exact step-set that counts as activated.
- Why it matters: NSM and weekly KPI reviews depend on it.
- Dependency: D-01; cohort analytics.
- Expected output: definition memo committed.

**[BUILD] ONBOARDING — Decide and ship exchange-connection gating for Free tier**
- Objective: choose whether Free can be used without exchange creds.
- Why it matters: shapes Free-tier UX + conversion.
- Dependency: D-03.
- Expected output: decision logged; UX adjusted.

**[BUILD] ONBOARDING — Iterate on worst-performing onboarding step (round 1)**
- Objective: ship targeted fix to highest drop-off step.
- Why it matters: D7 retention compounds across cohorts.
- Dependency: activation analytics; D-01 lock.
- Expected output: shipped change + measurement.

**[METRICS] ONBOARDING — Measure D7 + D30 retention for first paid cohort**
- Objective: produce defensible cohort-retention numbers.
- Why it matters: P1 stabilization criterion.
- Dependency: 30 days post first paid customer.
- Expected output: retention curves committed.

---

## Section D — Support and Trust Ops

**[DOC] SUPPORT — Seed KB with ≥10 articles on common gate-confusion patterns**
- Objective: pre-stock self-serve content.
- Why it matters: reduces founder support load at launch.
- Dependency: ticket-class taxonomy.
- Expected output: 10+ KB articles published.

**[OPS] SUPPORT — Tag all support tickets with category + severity + gate-confusion flag**
- Objective: build dataset that informs Trust Ops scope.
- Why it matters: required input for QF-03.
- Dependency: support tool tagging schema.
- Expected output: tagging in place; first sample reviewed.

**[OPS] TEAM — Source Trust Ops contractor shortlist (2–3 candidates)**
- Objective: have candidates ready 30 days before activation trigger.
- Why it matters: avoids reactive sourcing.
- Dependency: G-04 geographic constraints.
- Expected output: shortlist with introductions.

**[DOC] SUPPORT — Define Trust Ops contractor SOW v1**
- Objective: scope hours, responsibilities, refund authority.
- Why it matters: clean activation when trigger fires.
- Dependency: G-02 engagement model.
- Expected output: SOW draft.

**[OPS] SUPPORT — Activate Trust Ops contractor via 1–2 week trial project**
- Objective: validate fit before retainer commitment.
- Why it matters: cheapest validation method available.
- Dependency: shortlist + first paid customer + founder hiring decision.
- Expected output: trial complete; go/no-go decision logged.

---

## Section E — Safeguards reinforcement

**[QA] COMPLIANCE — Audit US-blocked-at-signup enforcement (IP, attestation, payment)**
- Objective: confirm enforcement is robust.
- Why it matters: regulatory exposure if it leaks.
- Dependency: signup-flow review.
- Expected output: audit memo; remediation tasks.

**[OPS] OPERATIONS — Activate vendor budget alarms at 50/80/100% for top vendors**
- Objective: monitor before overage occurs.
- Why it matters: vendor-overage explosion risk.
- Dependency: vendor dashboards.
- Expected output: alarms live.

**[OPS] TEAM — Nominate incident comms stand-in for founder unavailability**
- Objective: name the person + the protocol.
- Why it matters: bus-factor mitigation.
- Dependency: C-06.
- Expected output: stand-in protocol document.

**[DOC] COMPLIANCE — Engage external counsel for UAE crypto-software posture review**
- Objective: confirm or correct current operating posture.
- Why it matters: anchors A-06 enforcement.
- Dependency: counsel availability.
- Expected output: counsel memo.

---

## Phase 2 sequencing

```
Section A (pricing config + refund playbook)
        │
        ▼
Section A (Stripe end-to-end test)  ──►  Trader $79 live
        │                                      │
        ▼                                      ▼
Section C (activation lock + onboarding iter)  Section B (content cadence)
        │
        ▼
Section D (KB seed + tagging + sourcing)
        │
        ▼
Section D (Trust Ops trial project)  ──►  Activation decision
        │
        ▼
Section E (US-blocked audit + budget alarms + counsel)
```

**Critical path:** Section A is the gating sequence. Trader cannot go live without refund playbook + Stripe end-to-end test + activation definition lock.

## Phase 2 exit gate

Phase 2 is complete when:

- [ ] Refund/credit playbook v1 published.
- [ ] Trader $79/mo SKU live in Stripe.
- [ ] First paid customer flow validated end-to-end.
- [ ] Activation definition locked.
- [ ] Onboarding round-1 iteration shipped.
- [ ] First paid cohort D7 + D30 retention measured.
- [ ] Founder content cadence stable for ≥4 weeks.
- [ ] KB ≥10 articles published.
- [ ] Trust Ops contractor sourcing complete; trial project initiated or activated.
- [ ] US-blocked enforcement audited.
- [ ] Vendor budget alarms live.
- [ ] Incident comms stand-in nominated.

If any of these fail, do not proceed to Phase 3 — re-baseline within Phase 2 or roll back to Phase 1.
