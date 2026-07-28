# Phase 3 Backlog — Finance, KPIs, Team, Roadmap, Decision Discipline

## Phase 3 scope

**Operating discipline at scale.** Phase 3 turns the now-monetized product into a measurable, instrumented, reviewable business. Heavy emphasis on the financial reality (vendor costs, LLM scaling, cohort economics), KPI calibration with real data, team stabilization, and the cadence that prevents drift as activity grows.

**Time horizon:** ~60–90 days post Phase 2 exit.

**Phase exit criteria:**

- TRAS knob calibrated against real cohort data.
- Vendor cost / revenue measured; concentration shape visible.
- LLM cost per active user characterized.
- Trust Ops contractor formally activated or explicitly deferred.
- First quarterly strategy review held.
- Roadmap re-baselined for P2 entry.

---

## Section A — Financial discipline activation

**[FINANCE] FINANCE — Set founder internal rate at $100/hr placeholder**
- Objective: codify cost-recognition rate in `15-financial-framework`.
- Why it matters: honest margin framing; opportunity-cost discipline.
- Dependency: F-01.
- Expected output: assumption-table update.

**[FINANCE] FINANCE — Activate bookkeeping contractor at first paid customer**
- Objective: low-cost time-saver.
- Why it matters: unlocks F-04; frees founder hours.
- Dependency: first paid Trader.
- Expected output: contractor engaged; first month reconciled.

**[METRICS] FINANCE — Measure first-month vendor cost / revenue + top-3 concentration**
- Objective: produce first defensible cost-shape reading.
- Why it matters: anchors F-02 threshold.
- Dependency: first paid month elapsed.
- Expected output: cost-shape memo.

**[METRICS] FINANCE — Measure LLM cost per active user + identify scaling shape**
- Objective: detect linear vs superlinear early.
- Why it matters: margin erosion risk on Trader.
- Dependency: 30 days of paid usage.
- Expected output: cost-per-user trend; scaling-shape memo.

**[METRICS] FINANCE — Measure Stripe blended take-rate (MENA + global EN)**
- Objective: produce real take-rate vs assumption.
- Why it matters: F-05 honesty; QB-04.
- Dependency: 30 days of paid transactions.
- Expected output: take-rate memo.

**[QA] FINANCE — Run first vendor-concentration review (top 3 as % of total)**
- Objective: surface concentration risk before it bites.
- Why it matters: structural fragility check.
- Dependency: first month bills.
- Expected output: concentration report.

---

## Section B — KPI map activation and calibration

**[METRICS] METRICS — Run first weekly review per `weekly-review-template.md`**
- Objective: establish cadence; surface data gaps.
- Why it matters: discipline through repetition.
- Dependency: required-data inputs.
- Expected output: filled template committed.

**[METRICS] METRICS — Run first monthly exec review per `monthly-exec-review-template.md`**
- Objective: establish monthly cadence; surface decisions for register.
- Why it matters: operating-cadence stability.
- Dependency: 4 weekly reviews.
- Expected output: filled monthly template.

**[METRICS] METRICS — Transition NSM from VCE to TRAS at P1 narrow ship**
- Objective: smooth handoff in dashboards + templates.
- Why it matters: prevents ragged transition.
- Dependency: H-01 P1 narrow-ship decision.
- Expected output: transition checklist executed.

**[METRICS] METRICS — Lock TRAS knob calibration (N sessions, override threshold)**
- Objective: lock NSM operating definition.
- Why it matters: NSM credibility.
- Dependency: first paid cohort D30 data.
- Expected output: locked definition; KPI map + weekly template updated.

**[METRICS] METRICS — Activate KPI ownership transitions per `kpi-map.md`**
- Objective: name owners as roles activate (Trust Ops, Engineering contractors).
- Why it matters: avoids vague shared ownership.
- Dependency: contractor activations.
- Expected output: ownership-row updates.

---

## Section C — Team stabilization

**[OPS] TEAM — Activate Trust Ops contractor formally if trial succeeded**
- Objective: convert trial to ongoing engagement.
- Why it matters: founder time relief; trust posture coverage.
- Dependency: trial completion + go/no-go decision.
- Expected output: SOW v2 signed or explicit deferral logged.

**[OPS] TEAM — Source Engineering contractor shortlist for vendor integrations**
- Objective: 2–3 candidates ready before P2 entry.
- Why it matters: prevents reactive sourcing.
- Dependency: G-03 scoping model.
- Expected output: shortlist with introductions.

**[OPS] TEAM — Identify optional advisor candidate; confirm engagement model**
- Objective: activate advisor only if right candidate exists.
- Why it matters: monthly review value-add.
- Dependency: G-05.
- Expected output: candidate identified or role explicitly deferred.

**[METRICS] TEAM — Begin founder time-by-category log**
- Objective: weekly founder-hour breakdown into build / support / ops / GTM.
- Why it matters: bottleneck identification; first-FT-hire input.
- Dependency: simple time log.
- Expected output: weekly entries in operating cadence.

---

## Section D — Roadmap re-baselining

**[OPS] ROADMAP — Re-baseline 30-60-90 plan against actual PCC v2 G3 state**
- Objective: align plan with reality.
- Why it matters: plan honesty.
- Dependency: QA-01 closed.
- Expected output: revised plan; decision-log entry.

**[OPS] ROADMAP — Hold P1 → P2 transition criteria review post-cohort D30**
- Objective: review whether P2 entry is warranted.
- Why it matters: gate discipline.
- Dependency: M3 cohort retention; vendor cost shape.
- Expected output: go/no-go memo.

**[OPS] ROADMAP — First quarterly strategy review held**
- Objective: revisit strategic horizon.
- Why it matters: roadmap discipline.
- Dependency: 3 months of monthly reviews.
- Expected output: quarterly memo; roadmap re-baselined.

**[BUILD] PRODUCT — Scope Bybit integration SOW (draft only, do not sign)**
- Objective: define vendor-integration scope at engineering-contractor depth.
- Why it matters: P2 vendor expansion pre-work.
- Dependency: P1 stabilization (M3); engineering-contractor shortlist.
- Expected output: SOW v1 draft.

---

## Section E — Decision discipline

**[DOC] OPERATIONS — Lock decision-log home (markdown canonical + Notion mirror)**
- Objective: confirm I-01 + operationalize the mirror.
- Why it matters: prevents drift between locations.
- Dependency: Notion workspace setup.
- Expected output: confirmation; mirror configured.

**[DOC] OPERATIONS — Establish weekly decision-log delta as part of weekly review**
- Objective: surface decisions made / deferred / superseded each week.
- Why it matters: prevents decision laundering.
- Dependency: weekly review cadence stable.
- Expected output: standing review section.

**[QA] OPERATIONS — Audit `21-decision-log` registers for stale OPEN entries**
- Objective: move stale OPEN to DEFERRED with explicit triggers.
- Why it matters: prevents register rot.
- Dependency: 60 days of operation.
- Expected output: cleanup memo.

---

## Phase 3 sequencing

```
Phase 2 exit gate cleared
        │
        ▼
Section A (financial measurements roll out as paid data accumulates)
        │
        ▼
Section B (KPI cadence, NSM transition, TRAS calibration)
        │
        ▼
Section C (Trust Ops formalize, engineering contractor sourcing)
        │
        ▼
Section D (P1→P2 transition criteria review, quarterly strategy)
        │
        ▼
Section E (decision discipline cleanup)
```

**Critical path:** Section A → B (financial truth feeds KPI calibration). Section C runs in parallel. Section D depends on cohort data from Section B.

## Phase 3 exit gate

Phase 3 is complete when:

- [ ] Founder internal rate codified.
- [ ] Bookkeeping contractor active.
- [ ] Vendor cost / revenue measured and within target band.
- [ ] LLM cost per user characterized.
- [ ] Stripe take-rate measured.
- [ ] Vendor concentration review complete.
- [ ] Weekly + monthly reviews running for ≥6 consecutive cycles.
- [ ] NSM transitioned to TRAS.
- [ ] TRAS knobs locked.
- [ ] KPI ownership transitions reflect contractor activations.
- [ ] Trust Ops formally activated or deferred with reason.
- [ ] Engineering contractor shortlist current.
- [ ] Founder time-by-category log running.
- [ ] First quarterly strategy review held.
- [ ] P1 → P2 transition criteria reviewed.
- [ ] Decision-log register cleaned up.

If any of these fail, do not proceed to Phase 4 — re-baseline within Phase 3.
