# Master Backlog

Grouped by workstream, with **NOW / NEXT / LATER** filters across all groups.

- **NOW** = next 30 days from 2026-05-08.
- **NEXT** = days 31–90.
- **LATER** = beyond 90 days.

Every task uses `[TYPE] [AREA] — Action / Deliverable`, followed by a metadata line and four required fields:

```
**[TYPE] AREA — Action / Deliverable**
*Status | Owner | Deadline | Blocked by | Cross-ref*
- Objective: ...
- Why it matters: ...
- Dependency: ...
- Output: ...
```

**Phased subsets** of this backlog live in `phase-1-backlog.md` (strategic foundation), `phase-2-backlog.md` (packaging/pricing/GTM), `phase-3-backlog.md` (finance/KPIs/team), and `phase-4-backlog.md` (later-stage). Phase 1 is the active subset for the next ~30 days.

**Loggable threshold (cross-ref `21-decision-log/README.md`):** tasks that close a decision-register row must update both this backlog (Status → `Completed`) and the decision-register row (Status → `DECIDED`) in the same change-set.

**Status taxonomy:** `Not started` / `In progress` / `Blocked` / `Completed` / `Cancelled`.

---

## What's deliberately NOT in this backlog

- Sales-cycle metrics work (deal size, pipeline coverage) — defer to P5.
- Paid acquisition execution — forbidden until P3+ per E-02; only design-phase tasks before then.
- Full-time hires — none before P3.
- ARR / fundraising-deck modeling — defer until ≥60 days paid cohort data exists.
- White-label / dedicated-infrastructure customer work — not before P5.
- Performance attribution metrics — explicitly excluded.
- ML / regime specialist work — defer to P5+ contingent.

Reference `99-task-backlog/README.md` for the full exclusion list.

---

## 1. Product / Risk / Trust readiness

### NOW

**[RISK] RISK — Audit PCC v2 G3 stability for 30-day clock**
*Status: In progress | Owner: Founder | Deadline: Trigger: G3 30 days reached | Blocked by: — | Cross-ref: QA-01, H-01*
- Objective: confirm G3 readiness criteria are met with consecutive day-count visible.
- Why it matters: gates P1 narrow-ship; anchors entire 30-60-90 plan.
- Dependency: engine telemetry trailing 30 days.
- Output: dated G3-state log with consecutive-day count, in `21-decision-log` row QA-01.

**[BUILD] PRODUCT — Expand replay days corpus to ≥20 historical days**
*Status: In progress | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: M2 launch readiness, QA-03*
- Objective: ensure regression-test coverage at the launch-readiness threshold.
- Why it matters: launch-readiness gate for M2.
- Dependency: existing replay tooling; engine repo CI.
- Output: 20+ replay days passing in CI; manifest committed to engine repo.

**[DOC] TRUST — Audit runbook coverage to ≥80% of likely incident classes**
*Status: In progress | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: M2 trust readiness, QA-04*
- Objective: identify runbook gaps; close the top 5.
- Why it matters: trust-readiness gate for M2.
- Dependency: incident-class taxonomy from `13-support-and-trust-ops`.
- Output: coverage % logged in `kpi-map.md` §7; gap list with named owners and target dates.

**[QA] PRODUCT — Run pre-mortem on P1 narrow-ship plan**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: H-01, pre-mortem skill*
- Objective: surface failure modes before commitment.
- Why it matters: pre-mortem is mandatory before any canonical risk/PCC change per `decision-rights.md` §0 principle 5.
- Dependency: pre-mortem skill memory; `30-60-90-plan.md`.
- Output: pre-mortem document committed to repo; top-5 risks captured in `21-decision-log` H-01 context.

**[OPS] OPERATIONS — Verify connector-health 100% green for trailing 14 days**
*Status: In progress | Owner: Founder | Deadline: Daily check; 14-day window completes Trigger: G3 stability period | Blocked by: — | Cross-ref: M2 launch readiness, kpi-map.md §7*
- Objective: confirm operational readiness before monetization decision.
- Why it matters: launch-readiness criterion.
- Dependency: `coinscope-connector-health` Cowork artifact.
- Output: 14-day green log captured in weekly review.

### NEXT

**[QA] RISK — Confirm 30-day G3 stability and publish formal P1 readiness sign-off**
*Status: Blocked | Owner: Founder | Deadline: Trigger: G3 30d clock complete | Blocked by: G3 stability NOW task | Cross-ref: H-01, M2*
- Objective: produce the dated, criteria-met log entry.
- Why it matters: H-01 P1 ship-date decision input.
- Dependency: NOW G3 audit task; uninterrupted clock.
- Output: signed-off entry in `21-decision-log` H-01 with criteria validation evidence.

### LATER

**[BUILD] PRODUCT — Scope Bybit integration SOW (draft only, do not sign)**
*Status: Not started | Owner: Founder | Deadline: Trigger: M3 stabilization | Blocked by: M3 milestone | Cross-ref: H-02, G-03*
- Objective: define vendor-integration scope at engineering-contractor depth.
- Why it matters: P2 vendor expansion pre-work.
- Dependency: P1 stabilization (M3); engineering-contractor shortlist.
- Output: SOW v1 draft, not signed; reviewed ahead of P2 entry.

---

## 2. Pricing / Packaging

### NOW

**[DOC] PRICING — Lock discount policy posture pre-P2**
*Status: Not started | Owner: Founder | Deadline: 2026-06-30 | Blocked by: — | Cross-ref: B-03, decision-rights.md §4*
- Objective: decide and document discount stance before Trader live.
- Why it matters: protects tier-ladder defensibility; "a single ad-hoc discount resets the floor."
- Dependency: B-03 in decision register.
- Output: B-03 row moved from `OPEN — High` to `DECIDED` with rationale; discount-policy memo in `15-financial-framework/`. Recommendation: no discounts pre-P2.

**[DOC] TRUST — Author refund/credit playbook v1**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: C-05, decision-rights.md §7*
- Objective: produce the playbook with explicit dollar thresholds (1 month tier value; Desk Full v2 always escalates) and Trust Ops scope.
- Why it matters: gates Trader monetization; Trust Ops scope clarity.
- Dependency: tier matrix (A-03); `decision-rights.md` §7 dollar threshold table.
- Output: playbook published internally; C-05 row moved from `OPEN — High` to `DECIDED`.

### NEXT

**[DOC] PRICING — Lock annual prepay policy timing**
*Status: Blocked | Owner: Founder | Deadline: 2026-07-31 | Blocked by: PCC v2 G4 stability data | Cross-ref: B-01, financial-assumptions.md Row 4*
- Objective: decide whether annual launches at P2 or post-G4.
- Why it matters: cash vs refund-wave tradeoff; annual prepay before G4 stable creates refund-wave exposure.
- Dependency: B-01; PCC v2 G4 stability data when available.
- Output: B-01 moved from `OPEN — High` to `DECIDED`; Stripe configuration impact documented.

**[DOC] PRICING — Lock trial model**
*Status: Not started | Owner: Founder | Deadline: 2026-06-30 | Blocked by: — | Cross-ref: B-04, financial-assumptions.md Row 28*
- Objective: confirm Free tier as trial vs introducing time-boxed paid trial.
- Why it matters: shapes onboarding flow and conversion path.
- Dependency: B-04; first cohort feedback.
- Output: B-04 moved from `OPEN` to `DECIDED`; trial-model memo; onboarding flow impact noted.

### LATER

**[DOC] PRICING — Lock Desk Full v2 per-seat rate ($149 vs $249)**
*Status: Blocked | Owner: Founder | Deadline: 2026-12-31 | Blocked by: First fund-tier conversations | Cross-ref: B-02, financial-assumptions.md Row 3*
- Objective: choose per-seat anchor.
- Why it matters: Desk Full v2 economics; M8 launch readiness.
- Dependency: B-02; first fund-tier conversations.
- Output: B-02 moved to `DECIDED`; tier matrix updated; per-seat rate memo.

---

## 3. GTM / Brand / Content

### NOW

**[DOC] BRAND — Audit disclosure language consistency across surfaces**
*Status: Not started | Owner: Founder | Deadline: 2026-06-15 | Blocked by: — | Cross-ref: C-04 (DECIDED — execution task), QD-04*
- Objective: confirm "Testnet only. 30-day validation phase. No real capital." appears on every prospect-reachable surface.
- Why it matters: drift here is invisible until incident; C-04 approach is locked at "both" (manual quarterly audit + embedded into deploy checklist).
- Dependency: list of public surfaces; deploy-checklist updates.
- Output: surface-by-surface checklist; corrections applied; deploy-checklist updated to embed disclosure-language verification.

**[GTM] GTM — Establish founder content cadence (1–2 substantive pieces/week)**
*Status: Not started | Owner: Founder | Deadline: Trigger: P1 narrow ship | Blocked by: — | Cross-ref: E-01, E-03, 08-go-to-market*
- Objective: lock cadence and topic backlog.
- Why it matters: only acquisition channel pre-P3.
- Dependency: founder time allocation.
- Output: 8-week content plan committed; first piece shipped; E-01 moved to `DECIDED` with cadence locked.

### NEXT

**[RESEARCH] MARKET — Test MENA-targeted vs global EN content performance**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 4 weeks of attributed content | Blocked by: Founder content cadence task | Cross-ref: E-03, QC-02*
- Objective: measure side-by-side performance on equivalent content.
- Why it matters: anchors E-03 channel decision.
- Dependency: 4 weeks of content with attribution.
- Output: comparison memo; channel-investment recommendation; E-03 moved to `DECIDED`.

**[METRICS] GTM — Quantify founder-hour CAC for activated free + paid signups**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 90 days content + signup data | Blocked by: Founder time-by-category log + signup attribution | Cross-ref: QC-04, F-01*
- Objective: produce honest CAC framing.
- Why it matters: required before any paid-acquisition discussion.
- Dependency: founder time log; signup attribution.
- Output: CAC memo with founder-hour conversion at $100/hr placeholder (per F-01).

### LATER

**[GTM] GTM — Design paid-acquisition trigger criteria for P3+**
*Status: Blocked | Owner: Founder | Deadline: Trigger: P3 entry approaching | Blocked by: Cohort retention data, refund rate measurement | Cross-ref: E-02, decision-rights.md §5*
- Objective: define what must be true before paid spend activates.
- Why it matters: prevents premature acquisition that buys low-quality cohorts; paid acquisition is **forbidden, not deferred** until criteria met.
- Dependency: defensible cohort retention; refund rate <2%; trust posture publicly defensible.
- Output: trigger document; explicit go/no-go criteria; E-02 stays `DEFERRED` until criteria met.

---

## 4. Onboarding / Activation

### NOW

**[DOC] ONBOARDING — Lock activation definition for KPI use**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: D-01, kpi-map.md §2, financial-assumptions.md Rows 33–35*
- Objective: define exact step-set that counts as activated.
- Why it matters: NSM (TRAS) and weekly KPI review depend on it; multiple downstream tasks blocked.
- Dependency: D-01; cohort analytics.
- Output: D-01 moved from `OPEN — High` to `DECIDED`; definition memo committed; KPI map §2 + financial-assumptions Rows 33–35 status updated to reflect lock.

**[BUILD] ONBOARDING — Decide exchange-connection gating for Free tier**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: D-01 (partial) | Cross-ref: D-03*
- Objective: choose whether Free can be used without exchange creds.
- Why it matters: shapes Free-tier UX and conversion path.
- Dependency: D-03; activation flow design.
- Output: D-03 moved to `DECIDED`; UX adjusted accordingly; recommendation: allow Free without, gate Trader on connection.

### NEXT

**[BUILD] ONBOARDING — Iterate on worst-performing onboarding step (round 1)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 4 weeks activation analytics post-D-01 lock | Blocked by: D-01 lock + activation analytics | Cross-ref: D-02, kpi-map.md §2*
- Objective: ship targeted fix to the highest drop-off step.
- Why it matters: D7 retention compounds across cohorts; feeds NSM band.
- Dependency: activation analytics; D-01 lock.
- Output: shipped change + before/after measurement; kpi-map.md §2 row updated.

### LATER

**[BUILD] ONBOARDING — Iterate on activation flow (round 2)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: D7 retention <60% after round 1 | Blocked by: Round 1 measurement | Cross-ref: D-02, kpi-map.md §2*
- Objective: only fires if D7 retention <60% after round 1; otherwise explicit "no further iteration needed" memo.
- Why it matters: avoids treating activation as "done" too early.
- Dependency: round 1 measurement.
- Output: round-2 change set OR explicit "no further iteration needed" memo committed.

---

## 5. Support / Trust Ops

### NOW

**[DOC] SUPPORT — Seed KB with ≥10 articles on common gate-confusion patterns**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: 13-support-and-trust-ops, kpi-map.md §4 user-reported gate confusion*
- Objective: pre-stock self-serve content before paid traffic.
- Why it matters: reduces founder support load at launch; first line of defense against gate-confusion ticket waves.
- Dependency: ticket-class taxonomy; gate-decision examples from engine.
- Output: 10+ KB articles published; categorized; tagged for the support tagging schema below.

**[OPS] SUPPORT — Tag all support tickets with category + severity + gate-confusion flag**
*Status: Not started | Owner: Founder | Deadline: 2026-05-31 | Blocked by: — | Cross-ref: QF-03, kpi-map.md §4*
- Objective: build the dataset that informs Trust Ops scope.
- Why it matters: required input for QF-03 (ticket-share by class) and Trust Ops SOW sizing.
- Dependency: support tool tagging schema.
- Output: tagging schema documented; tagging in place; first-week sample reviewed and posted in weekly review.

### NEXT

**[OPS] TEAM — Source Trust Ops contractor shortlist (2–3 candidates)**
*Status: Not started | Owner: Founder | Deadline: 2026-07-15 | Blocked by: G-04 lock | Cross-ref: G-01, G-04, QH-01*
- Objective: have candidates ready 30 days before activation trigger.
- Why it matters: avoids reactive sourcing under stress.
- Dependency: G-04 geographic constraints locked.
- Output: shortlist with introductions completed; documented in QH-01.

**[DOC] SUPPORT — Define Trust Ops contractor SOW v1**
*Status: Blocked | Owner: Founder | Deadline: 2026-08-01 | Blocked by: G-02 engagement model | Cross-ref: G-01, G-02, role-priorities.md*
- Objective: scope hours, responsibilities, and refund authority per dollar threshold table in `decision-rights.md` §7.
- Why it matters: clean activation when trigger fires.
- Dependency: G-02 engagement model decision.
- Output: SOW v1 draft.

### LATER

**[OPS] SUPPORT — Activate Trust Ops contractor via 1–2 week trial project**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 2026-08-15 expected | Blocked by: Shortlist + first paid customer + G-01 trigger | Cross-ref: G-01, G-02*
- Objective: validate fit before retainer commitment.
- Why it matters: cheapest validation method available.
- Dependency: shortlist; first paid customer in system; founder hiring decision.
- Output: trial complete; go/no-go decision logged; G-01 moved to `DECIDED` either way.

---

## 6. Risk / Compliance / Safeguards

### NOW

**[DOC] TRUST — Codify public-claims posture in brand-voice document**
*Status: Not started | Owner: Founder | Deadline: 2026-05-31 | Blocked by: — | Cross-ref: C-03 (DECIDED — execution task), decision-rights.md §6*
- Objective: codify the rule and rationale in one document for future hires/contractors.
- Why it matters: regulatory and reputational tail; C-03 is `DECIDED` (forbid in public marketing) but the codification is execution.
- Dependency: C-03 in decision register.
- Output: brand-voice memo; cross-ref to `decision-rights.md` §6 forbidden-content list.

**[OPS] RISK — Confirm real-capital authorization default = NO across all surfaces**
*Status: In progress | Owner: Founder | Deadline: Weekly check; ongoing | Blocked by: — | Cross-ref: C-01 (DECIDED), decision-rights.md §8*
- Objective: ensure no surface implies otherwise.
- Why it matters: single most consequential default; per `decision-rights.md` §10 step 3, cannot be made in founder absence.
- Dependency: surface audit.
- Output: confirmation log per weekly review; corrections applied if any drift detected.

### NEXT

**[DOC] COMPLIANCE — Engage external counsel for UAE crypto-software posture review**
*Status: Not started | Owner: Founder + counsel | Deadline: 2026-07-31 | Blocked by: Counsel availability | Cross-ref: C-08 (DECIDED — execution task), QE-01, A-06*
- Objective: confirm or correct current operating posture.
- Why it matters: anchors A-06 enforcement; informs P2 scope; required before any compliance-sensitive expansion.
- Dependency: counsel availability.
- Output: counsel memo; any recommended adjustments logged in `21-decision-log` (potentially as new C-section row).

**[QA] COMPLIANCE — Audit US-blocked-at-signup enforcement (IP, attestation, payment)**
*Status: Not started | Owner: Founder + counsel | Deadline: 2026-06-30 | Blocked by: — | Cross-ref: A-06, QE-02, kpi-map.md §1 Geographic mix*
- Objective: confirm enforcement is actually robust.
- Why it matters: regulatory exposure if it leaks; KPI map §1 alarms on any US signup.
- Dependency: signup-flow review.
- Output: audit memo; remediation tasks if gaps; QE-02 moved from open question to closed.

**[DOC] OPERATIONS — Document security incident response runbook**
*Status: Not started | Owner: Founder + counsel | Deadline: 2026-07-31 | Blocked by: — | Cross-ref: C-07 (DECIDED — execution task), decision-rights.md §10A*
- Objective: codify the security-incident protocol per `decision-rights.md` §10A: containment in-band, Founder + counsel within 1 hour, no public/customer comms until concur, postmortem within 7 days.
- Why it matters: security incidents have a separate escalation path from operational incidents; runbook absence at moment of need is the failure mode.
- Dependency: counsel input.
- Output: runbook published in `13-support-and-trust-ops/`; cross-referenced from `decision-rights.md` §10A.

### LATER

**[DOC] COMPLIANCE — Scope compliance posture upgrade for Desk Full v2 fund tier**
*Status: Blocked | Owner: Founder + counsel | Deadline: Trigger: P3 entry or first fund-prospect conversation | Blocked by: First fund-prospect conversation | Cross-ref: M7, C-08, phase-4-backlog.md*
- Objective: define what DPA / SOC 2 lite / audit-grade exports look like.
- Why it matters: M7 milestone definition.
- Dependency: first fund-prospect conversations.
- Output: scope memo; legal retainer scope.

**[DOC] OPERATIONS — Document engine rollback carve-out for engineering contractor onboarding**
*Status: Blocked | Owner: Founder | Deadline: Trigger: Engineering contractor onboarding | Blocked by: G-03 contractor activation | Cross-ref: C-09 (DECIDED — execution task), decision-rights.md §8*
- Objective: codify the rollback carve-out rules for the engineering contractor onboarding pack.
- Why it matters: contractor needs to know in advance: rollback OK during incident if capital-preservation risk + founder unreachable; forward deploys never permitted under same conditions.
- Dependency: G-03 contractor activation; deploy runbook updated.
- Output: rollback carve-out doc included in contractor onboarding pack; cross-ref `decision-rights.md` §8.

---

## 7. Finance / Cost discipline

### NOW

**[FINANCE] FINANCE — Set founder internal rate at $100/hr placeholder**
*Status: Not started | Owner: Founder | Deadline: 2026-05-31 | Blocked by: — | Cross-ref: F-01, financial-assumptions.md Row 19, cost-structure.md §9*
- Objective: codify cost-recognition rate in `15-financial-framework`.
- Why it matters: honest margin framing; opportunity-cost discipline; cosmetic until fundraise then suddenly load-bearing.
- Dependency: F-01 decision.
- Output: F-01 moved to `DECIDED`; assumption-table Row 19 status updated; founder-hours-by-category log started.

**[OPS] FINANCE — Activate vendor budget alarms at 50/80/100% for vendors >5% of total monthly cost**
*Status: Not started | Owner: Founder | Deadline: 2026-06-15 | Blocked by: — | Cross-ref: F-02, kpi-map.md §6, cost-structure.md §3*
- Objective: monitor before overage occurs.
- Why it matters: vendor-overage explosion is the dominant cost shape risk per `cost-structure.md` §8.
- Dependency: vendor dashboards; spend baseline.
- Output: alarms live for every vendor >5% of total monthly cost; weekly review surfaces breaches; cross-ref `kpi-map.md` §6 vendor-concentration KPIs.

**[QA] FINANCE — Test Stripe end-to-end (signup, billing, refund) in MENA + global EN currencies**
*Status: Not started | Owner: Founder | Deadline: 2026-06-07 | Blocked by: — | Cross-ref: F-05, M2 launch readiness*
- Objective: confirm monetization mechanics before Trader live.
- Why it matters: F-05 readiness; gates Trader monetization activation.
- Dependency: Stripe sandbox.
- Output: F-05 moved from `OPEN — High` to `DECIDED`; test-transaction log; sign-off committed.

### NEXT

**[FINANCE] FINANCE — Activate bookkeeping contractor at first paid customer**
*Status: Blocked | Owner: Founder | Deadline: Trigger: First paid Trader | Blocked by: First paid customer | Cross-ref: F-04, role-priorities.md Role #2*
- Objective: low-cost time-saver to free founder hours.
- Why it matters: unlocks F-04; replaces 10–20 founder hours/month at higher implicit rate.
- Dependency: first paid Trader.
- Output: contractor engaged; first month reconciled; F-04 moved to `DECIDED`.

**[METRICS] FINANCE — Vendor cost / revenue first reading and top-3 concentration**
*Status: Blocked | Owner: Founder | Deadline: Trigger: First paid month elapsed | Blocked by: First paid month | Cross-ref: F-02, financial-assumptions.md Rows 36–37, kpi-map.md §6*
- Objective: produce the first defensible cost-shape reading.
- Why it matters: anchors F-02 threshold; first validation of Rows 36–37 assumptions.
- Dependency: first paid month elapsed; bookkeeping contractor active.
- Output: cost-shape memo; vendor-concentration percentage; financial-assumptions Rows 36–37 status updated to `Validating`.

**[METRICS] FINANCE — LLM cost per active user trend and scaling shape**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 30 days paid usage | Blocked by: 30 days paid usage data | Cross-ref: financial-assumptions.md Row 17, QG-02, kpi-map.md §6*
- Objective: detect linear vs superlinear scaling early.
- Why it matters: margin erosion risk on Trader if superlinear.
- Dependency: 30 days of paid usage; provider dashboards.
- Output: cost-per-user trend; scaling-shape memo; QG-02 moved to closed.

### LATER

**[FINANCE] FINANCE — Build first scenario model spreadsheet from `scenario-model-inputs.md`**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 60 days paid cohort data + TRAS calibration | Blocked by: H-04 closure + 60 days paid cohort | Cross-ref: scenario-model-inputs.md, phase-4-backlog.md §F*
- Objective: turn input categories into a working model.
- Why it matters: required for any fundraising or strategic-planning conversation; without it, scenario-revision triggers can't be operationalized.
- Dependency: ≥60 days of paid cohort data; locked TRAS calibration (H-04).
- Output: model v1; clearly assumption-tagged with row references back to financial-assumptions.md.

---

## 8. KPIs / Reviews

### NOW

**[METRICS] METRICS — Run first weekly review per `weekly-review-template.md`**
*Status: In progress | Owner: Founder | Deadline: Weekly cadence | Blocked by: — | Cross-ref: weekly-review-template.md, operating-cadence.md*
- Objective: establish cadence and discover data gaps.
- Why it matters: discipline is set by repetition; weekly review is the moment-of-decision artifact.
- Dependency: required-data inputs per template.
- Output: filled template committed; data-gap list captured for follow-up tasks.

**[METRICS] METRICS — Run first monthly exec review per `monthly-exec-review-template.md`**
*Status: Not started | Owner: Founder | Deadline: 2026-05-31 (month-end) | Blocked by: 4 weekly reviews of data | Cross-ref: monthly-exec-review-template.md, operating-cadence.md*
- Objective: establish monthly cadence; surface decisions for register.
- Why it matters: operating-cadence stability.
- Dependency: 4 weekly reviews.
- Output: filled monthly template; decision-log delta committed; "what changed this month" paragraph drafted.

### NEXT

**[METRICS] METRICS — Lock TRAS knob calibration (N sessions, override threshold)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: First paid cohort D30 + 30 | Blocked by: H-01 closure + first paid cohort D30 | Cross-ref: H-04, north-star-metric.md, kpi-map.md §0a*
- Objective: lock NSM operating definition based on real cohort data.
- Why it matters: NSM credibility; without locked knobs, TRAS is directional only.
- Dependency: first paid cohort D30 data.
- Output: H-04 moved to `DECIDED`; locked definition; KPI map §0a + weekly template updated.

**[METRICS] METRICS — Transition NSM from VCE to TRAS at P1 narrow ship**
*Status: Blocked | Owner: Founder | Deadline: Trigger: P1 narrow ship (H-01) | Blocked by: H-01 closure | Cross-ref: H-01, north-star-metric.md, kpi-map.md §0a*
- Objective: smooth handoff in operating dashboards and templates.
- Why it matters: prevents ragged NSM transition.
- Dependency: H-01 P1 narrow-ship decision.
- Output: transition checklist executed; weekly template updated; kpi-map §0a "Status" column updated.

### LATER

**[METRICS] METRICS — First quarterly strategy review held**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 3 months of monthly reviews | Blocked by: 3 monthly reviews completed | Cross-ref: operating-cadence.md*
- Objective: revisit strategic horizon.
- Why it matters: roadmap discipline; quarterly is the right cadence for NSM-definition revision review.
- Dependency: 3 months of monthly reviews.
- Output: quarterly memo; roadmap re-baselined per `dependency-map.md` §9.

---

## 9. Team / Hiring / Cadence

### NOW

**[OPS] TEAM — Lock geographic hiring constraints (UAE / MENA / global EN)**
*Status: Not started | Owner: Founder | Deadline: 2026-06-15 | Blocked by: — | Cross-ref: G-04, team-design.md*
- Objective: set search radius for first contractors.
- Why it matters: timezone coverage and trust signal; gates Trust Ops sourcing.
- Dependency: G-04 decision.
- Output: G-04 moved to `DECIDED`; hiring policy memo; recommendation: MENA-broad with global EN written-language fluency.

**[OPS] TEAM — Nominate incident comms stand-in for founder unavailability (Phase 1)**
*Status: Not started | Owner: Founder | Deadline: 2026-06-30 | Blocked by: — | Cross-ref: C-06 (phased — Phase 1), decision-rights.md §10*
- Objective: name the trusted contact and the protocol for founder unavailability >24h.
- Why it matters: bus-factor mitigation; without this, founder unavailability >24h triggers a no-decision posture across all categories.
- Dependency: C-06 Phase 1 decision.
- Output: Phase 1 stand-in identified; protocol document committed; transitions to Phase 2 (Trust Ops contractor) at G-01 closure.

### NEXT

**[OPS] TEAM — Source Engineering contractor shortlist for vendor integrations**
*Status: Not started | Owner: Founder | Deadline: Trigger: P2 vendor expansion approaching | Blocked by: G-03 scoping model | Cross-ref: G-03, role-priorities.md Role #4, QH-02*
- Objective: have 2–3 candidates ready before P2 entry.
- Why it matters: prevents reactive sourcing.
- Dependency: G-03 scoping model.
- Output: shortlist with introductions; QH-02 closed.

**[OPS] TEAM — Identify optional advisor candidate; confirm engagement model**
*Status: Blocked | Owner: Founder | Deadline: Trigger: P1 narrow ship | Blocked by: H-01 | Cross-ref: G-05, role-priorities.md Role #5*
- Objective: activate advisor only if right candidate exists.
- Why it matters: monthly review value-add; "good advisors are unevenly available."
- Dependency: G-05 decision.
- Output: G-05 moved to `DECIDED`; candidate identified or role explicitly deferred with reason.

### LATER

**[DOC] TEAM — Define first FT hire role profile (driven by binding constraint)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: Pre-P3 with ≥3 months contractor data | Blocked by: 3 months contractor data | Cross-ref: G-06, team-design.md §8*
- Objective: write the role profile based on observed contractor utilization.
- Why it matters: G-06; first FT hire is the highest-stakes hire.
- Dependency: ≥3 months of contractor data.
- Output: role profile + activation criteria; G-06 progressing.

**[DOC] TEAM — Establish equity policy for first FT hire**
*Status: Blocked | Owner: Founder | Deadline: Trigger: Pre-P3 | Blocked by: First FT hire candidate identified | Cross-ref: G-06, team-design.md §4*
- Objective: set posture before role activates.
- Why it matters: G-06 unblocks offer terms.
- Dependency: counsel input; cap-table baseline.
- Output: equity-policy memo; G-06 moved to `DECIDED`.

---

## 10. Roadmap / Decision discipline

### NOW

**[OPS] ROADMAP — Re-baseline 30-60-90 plan against actual PCC v2 G3 state**
*Status: Blocked | Owner: Founder | Deadline: Trigger: QA-01 closes | Blocked by: QA-01 closure | Cross-ref: QA-01, 18-roadmap/30-60-90-plan.md*
- Objective: align plan with reality after QA-01 closes.
- Why it matters: plan is only as honest as its anchor.
- Dependency: QA-01 (G3 state).
- Output: revised plan; decision-log entry; affected items in master backlog updated.

**[OPS] OPERATIONS — Configure Notion mirror to match canonical markdown decision-log**
*Status: Not started | Owner: Founder | Deadline: 2026-05-31 | Blocked by: Notion workspace setup | Cross-ref: I-01 (DECIDED — execution task), 21-decision-log/README.md*
- Objective: operationalize the markdown-canonical + Notion-mirror posture per I-01.
- Why it matters: prevents drift between locations; I-01 is `DECIDED` but mirror configuration is pending.
- Dependency: Notion workspace setup.
- Output: Notion mirror configured and validated against canonical markdown; weekly verify added to weekly-review checklist.

### NEXT

**[OPS] ROADMAP — Hold P1 → P2 transition criteria review post-cohort D30**
*Status: Blocked | Owner: Founder | Deadline: Trigger: M3 D30 retention measurement | Blocked by: M3 cohort retention; vendor cost shape | Cross-ref: M3, milestone-framework.md §7*
- Objective: review whether P2 entry is warranted.
- Why it matters: gate discipline.
- Dependency: M3 cohort retention; vendor cost shape.
- Output: go/no-go memo; if go, P2 transition log entry; if no-go, revised baseline.

### LATER

**[OPS] ROADMAP — Hold first phase-transition review (P1 → P2)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: M3 milestone complete | Blocked by: M3 milestone | Cross-ref: milestone-framework.md §7, dependency-map.md §9*
- Objective: full re-baseline at phase boundary.
- Why it matters: keeps every folder synchronized; updates owner/state/cell in dependency-map §3.
- Dependency: M3 milestone complete.
- Output: phase-transition log; folder updates across `15-financial-framework/`, `16-kpi-okr-system/`, `17-team-and-operating-model/`, `18-roadmap/`, `21-decision-log/`.

---

## 11. Partnerships / Sales

### LATER

**[PARTNERSHIPS] PARTNERSHIPS — Identify 3 niche EN newsletters / communities for content placement**
*Status: Blocked | Owner: Founder | Deadline: Trigger: Founder content cadence stable ≥8 weeks | Blocked by: Content cadence stability | Cross-ref: phase-4-backlog.md §D*
- Objective: explore amplification options without paid spend.
- Why it matters: GTM amplification at low cost.
- Dependency: founder content cadence stable.
- Output: shortlist with outreach plan.

**[PARTNERSHIPS] PARTNERSHIPS — Explore data-vendor partnership tier with CoinGlass**
*Status: Blocked | Owner: Founder | Deadline: Trigger: P2 entry | Blocked by: P2 entry | Cross-ref: QG-04, financial-assumptions.md Row 16, phase-4-backlog.md §D*
- Objective: investigate whether single-source dependency can be eased via partnership.
- Why it matters: QG-04 single-source risk on derivatives data.
- Dependency: P2 entry.
- Output: conversation memo; pricing alternatives.

**[GTM] SALES — Scope Desk Full v2 first-customer sales motion (founder-led)**
*Status: Blocked | Owner: Founder | Deadline: Trigger: Per-seat features in scope + compliance posture upgrade in flight | Blocked by: M7 (compliance) + per-seat features scoped | Cross-ref: M8, phase-4-backlog.md §C*
- Objective: define what the first 5 fund-tier conversations look like.
- Why it matters: M8 launch readiness.
- Dependency: per-seat features; compliance posture upgrade in progress.
- Output: sales motion memo; first 5 prospect list.

---

## 12. Fundraising / Scenarios (deferred)

### LATER

**[DOC] FUNDRAISING — Decide bootstrap vs venture-track posture**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 6+ months of validated revenue patterns | Blocked by: 6+ months paid data | Cross-ref: phase-4-backlog.md §E*
- Objective: anchor narrative for any future capital conversation.
- Why it matters: shapes hiring pace, scenario modeling, milestone cadence.
- Dependency: 6+ months of validated revenue patterns.
- Output: posture memo with options + recommendation.

**[DOC] SCENARIOS — Build best/base/worst scenario models from `scenario-model-inputs.md`**
*Status: Blocked | Owner: Founder | Deadline: Trigger: 60+ days paid data + locked TRAS calibration | Blocked by: H-04 + 60 days paid cohort | Cross-ref: scenario-model-inputs.md, phase-4-backlog.md §F*
- Objective: convert input categories into 3 scenario models.
- Why it matters: leadership scenario-revision triggers depend on this existing.
- Dependency: ≥60 days paid data; locked TRAS calibration.
- Output: 3 model variants; clearly assumption-tagged with rows from financial-assumptions.md.

**[DOC] FUNDRAISING — Design milestone-gated fundraising trigger criteria**
*Status: Blocked | Owner: Founder | Deadline: Trigger: P2 stabilization | Blocked by: P2 stabilization | Cross-ref: phase-4-backlog.md §E*
- Objective: define what must be true before fundraising conversations begin.
- Why it matters: avoids fundraising on weak data.
- Dependency: P2 stabilization.
- Output: trigger memo.

---

## Master backlog summary

| Section | NOW | NEXT | LATER | Total |
|---|---|---|---|---|
| 1. Product / Risk / Trust readiness | 5 | 1 | 1 | 7 |
| 2. Pricing / Packaging | 2 | 2 | 1 | 5 |
| 3. GTM / Brand / Content | 2 | 2 | 1 | 5 |
| 4. Onboarding / Activation | 2 | 1 | 1 | 4 |
| 5. Support / Trust Ops | 2 | 2 | 1 | 5 |
| 6. Risk / Compliance / Safeguards | 2 | 3 | 2 | 7 |
| 7. Finance / Cost discipline | 3 | 3 | 1 | 7 |
| 8. KPIs / Reviews | 2 | 2 | 1 | 5 |
| 9. Team / Hiring / Cadence | 2 | 2 | 2 | 6 |
| 10. Roadmap / Decision discipline | 2 | 1 | 1 | 4 |
| 11. Partnerships / Sales | 0 | 0 | 3 | 3 |
| 12. Fundraising / Scenarios | 0 | 0 | 3 | 3 |
| **Totals** | **24** | **19** | **18** | **61** |

**61 active tasks total.** Lean by design. The phase backlogs (`phase-1-backlog.md` through `phase-4-backlog.md`) pull subsets into ordered execution sequences.

---

## Urgent watchlist (NOW tasks tied to OPEN — High decisions)

Sorted by deadline ascending. These are the next-to-act items.

| Deadline | Task | Linked decision |
|---|---|---|
| 2026-05-31 | `[FINANCE] FINANCE — Set founder internal rate at $100/hr placeholder` | F-01 (OPEN) |
| 2026-05-31 | `[OPS] FINANCE — Activate vendor budget alarms at 50/80/100%...` (depends on F-02 lock) | F-02 (OPEN) |
| 2026-05-31 | `[OPS] SUPPORT — Tag all support tickets with category + severity + gate-confusion flag` | QF-03 |
| 2026-05-31 | `[DOC] TRUST — Codify public-claims posture in brand-voice document` | C-03 (DECIDED — execution) |
| 2026-05-31 | `[METRICS] METRICS — Run first monthly exec review per template` | operating-cadence |
| 2026-05-31 | `[OPS] OPERATIONS — Configure Notion mirror to match canonical markdown decision-log` | I-01 (DECIDED — execution) |
| 2026-06-07 | `[BUILD] PRODUCT — Expand replay days corpus to ≥20 historical days` | M2 launch readiness |
| 2026-06-07 | `[DOC] TRUST — Audit runbook coverage to ≥80% of likely incident classes` | M2 trust readiness |
| 2026-06-07 | `[QA] PRODUCT — Run pre-mortem on P1 narrow-ship plan` | H-01 |
| 2026-06-07 | `[DOC] TRUST — Author refund/credit playbook v1` | C-05 (OPEN — High) |
| 2026-06-07 | `[DOC] ONBOARDING — Lock activation definition for KPI use` | D-01 (OPEN — High) |
| 2026-06-07 | `[BUILD] ONBOARDING — Decide exchange-connection gating for Free tier` | D-03 |
| 2026-06-07 | `[DOC] SUPPORT — Seed KB with ≥10 articles on common gate-confusion patterns` | trust-ops |
| 2026-06-07 | `[QA] FINANCE — Test Stripe end-to-end (signup, billing, refund) in MENA + global EN` | F-05 (OPEN — High) |
| 2026-06-15 | `[DOC] BRAND — Audit disclosure language consistency across surfaces` | C-04 (DECIDED — execution) |
| 2026-06-15 | `[OPS] TEAM — Lock geographic hiring constraints` | G-04 |
| 2026-06-30 | `[OPS] TEAM — Nominate incident comms stand-in (Phase 1)` | C-06 (OPEN — High, Phase 1) |
| 2026-06-30 | `[DOC] PRICING — Lock discount policy posture pre-P2` | B-03 (OPEN — High) |
| 2026-06-30 | `[DOC] PRICING — Lock trial model` | B-04 |
| 2026-06-30 | `[QA] COMPLIANCE — Audit US-blocked-at-signup enforcement` | A-06, QE-02 |

---

## Cross-references

| Topic | Where to look |
|---|---|
| Backlog governance, naming rules | `99-task-backlog/README.md` |
| Phased subsets (active execution sequences) | `99-task-backlog/phase-1-backlog.md` through `phase-4-backlog.md` |
| Decision register (decision IDs in Cross-ref column) | `21-decision-log/leadership-decision-register.md` |
| Open questions register (Q* IDs in Cross-ref column) | `21-decision-log/open-questions-register.md` |
| 30-60-90 plan (origin of many NOW/NEXT tasks) | `18-roadmap/30-60-90-plan.md` |
| Dependency map (§7 do-not-start list — many tasks gated by dependencies there) | `18-roadmap/dependency-map.md` |
| Milestone framework (M1–M9 referenced in Cross-ref column) | `18-roadmap/milestone-framework.md` |
| KPI map (KPIs that measure task outcomes) | `16-kpi-okr-system/kpi-map.md` |
| Financial assumptions (Row references in Cross-ref column) | `15-financial-framework/financial-assumptions.md` |
| Decision rights (authority bounds for tasks) | `17-team-and-operating-model/decision-rights.md` |
| Operating cadence (review frequencies that surface tasks) | `17-team-and-operating-model/operating-cadence.md` |

---

## Version history

Append-only log of changes to this file. Format: `YYYY-MM-DD — change summary — affected sections / tasks`.

| Date | Change | Affected |
|---|---|---|
| 2026-05-08 | Initial backlog published as part of Wave 3 generation (60 tasks) | All sections |
| 2026-05-08 | Cleanup pass: deleted §1 NEXT duplicate onboarding-iteration task (already in §4); refreshed stale "lock" tasks for now-DECIDED rows (renamed §10 Notion-mirror task and §6 public-claims-posture task); added 2 new tasks for new DECIDED rows (§6 NEXT security incident runbook for C-07; §6 LATER engine rollback carve-out doc for C-09); added per-task metadata line with Status / Owner / Deadline / Blocked by / Cross-ref; tightened vague Output specifications; defined "top vendors" as >5% of total monthly cost; renamed §7 NEXT tasks for distinctness (Vendor cost / revenue first reading; LLM cost per active user trend); added Urgent watchlist section; added Cross-references section; added Version history; added phase-backlog reference in preamble; added What's NOT in this backlog framing; added Last reviewed footer; updated Master backlog summary (60 → 61 tasks: -1 deletion, +2 additions) | All sections; new tasks in §6 NEXT and §6 LATER; renamed tasks in §6 NOW, §7 NEXT, §10 NOW |

---

*Last reviewed: 2026-05-08. Reviewed at every weekly review (Status field updates), monthly exec review (full backlog), every contractor activation (Owner field updates), and at every phase transition (re-baseline).*
