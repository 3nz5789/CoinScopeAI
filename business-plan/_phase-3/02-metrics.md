# 02 — METRICS

**Workstream:** METRICS
**Phase:** 3 — Operating System
**Status:** Scaffold initialized 2026-05-05.
**Canonical authorities:** v1 framework `13-kpi-okr.md` (north-star MAVT + VCSE; 5-layer metric tree; persona segmentation; Q1 OKRs; risk KPIs paired with §14 stop-the-line; weekly + monthly reporting templates; §11 feedback loops; anti-overclaim audit); Phase 2 `05-gtm.md` (funnel instrumentation: signup → first-signal → first-gate-decision → first-billing); §14 stop-the-line conditions; §16 anti-probability framing.

---

## 1. Purpose

Operationalize the §13 v1 KPI / OKR framework into **living instruments**: the weekly internal report, the monthly stakeholder report, the OKR quarterly review, the §13 conditional-escalation red-line monitor, and the anti-overclaim audit on every public metric surface. METRICS is the workstream that converts a *framework document* into a *running discipline*.

## 2. Why this matters specifically for CoinScopeAI

- **§13 v1 locked the framework but not the cadence.** A north-star metric (MAVT) and a 5-layer tree without a weekly running report is reference material, not an operating instrument. Phase 3 is where it becomes muscle memory.
- **Anti-overclaim discipline is metric discipline.** Every public surface — pricing page, status page, public roadmap, monthly stakeholder report, due-diligence pack — that touches a number is an overclaim risk. Per §13 final audit + §6.10 Flag 2 — stabilizing-status visibility is non-negotiable.
- **Vanity metric drift is the post-launch failure mode.** At P3 stabilization (Oct–Dec 2026) users + revenue exist; the temptation to substitute MAU / signup count / Twitter reach for MAVT compounds quickly. Vanity metrics misroute capital and break §15 due diligence.
- **§13 conditional-escalation red-line** (cohort gate-rejection acceptance <50%) is the first non-§14 red-line in the framework. It needs an alert, not a quarterly check. Phase 3 wires it.
- **§14 stop-the-line conditions feed off METRICS instrumentation.** Six §14 conditions + the §13 conditional all require *measured* signals. If the measurement is absent or noisy, stop-the-line either fails to fire (false-negative) or fires on noise (false-positive); both erode discipline.
- **§11 feedback loops** depend on observed-vs-assumed reconciliation. Per §11 source taxonomy `A`/`O`/`B` — every assumed input that reaches `O` must be flagged. METRICS owns the surfacing.
- **§15 investor narrative inherits the format** — Phase 4 raise discipline starts here. Sloppy weekly reporting in Phase 3 = sloppy narrative in Phase 4.

## 3. Required subsections

1. **Weekly internal report template** — agenda, sections, KPI feeds, decision triggers. Run for ≥4 consecutive weeks before signed.
2. **Monthly stakeholder report template** — investor / advisor / founder-cohort variants; light + full versions per §13.7.
3. **OKR quarterly review SOP** — review → reset cycle; KR closure criteria; carried-over KR rules.
4. **§13 conditional-escalation red-line monitor** — alert wiring on cohort gate-rejection acceptance <50%; escalation path; investigation runbook.
5. **§14 stop-the-line metric instrumentation audit** — every of the six §14 conditions + the one §13 conditional has an instrumented signal with defined source and threshold.
6. **Public metric surface inventory + anti-overclaim audit** — pricing page numbers, status page, public roadmap, blog content if any. Each surface audited against §13.8 audit + §9 messaging matrix.
7. **MAVT + VCSE primacy enforcement** — every internal report leads with MAVT; vanity metrics tagged as such or excluded.
8. **§11 model-vs-actuals feedback loop instrumentation** — `A` → `O` reclassification surfacing in monthly report.
9. **Persona-segmented metric reads** (NEXT) — Omar / Karim / Layla cuts on activation, retention, gate-acceptance.
10. **Cohort-behavioral grid review cadence** (NEXT) — §3.8 grid (gate-rejection acceptance, multi-account setup, journal review frequency, tier-upgrade trigger pattern, NPS) reviewed monthly.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Weekly Internal Report Template v1 | MD template + dashboard pointer | Founder + Strategy CoS |
| Monthly Stakeholder Report Template v1 | MD template (light + full variants) | Founder + Strategy CoS |
| OKR Quarterly Review SOP | MD; owned cycle | Founder |
| §13 Red-Line Monitor SOP | MD + alert wiring spec | Founder + Eng |
| §14 Stop-the-Line Instrumentation Audit | MD audit table, condition × signal × threshold × source | Founder + Eng |
| Public Metric Surface Inventory | MD inventory + per-surface audit | Strategy CoS |
| Anti-Overclaim Audit Pre-Publish Checklist | MD checklist | Strategy CoS |
| MAVT + VCSE Definition Doc v1.1 | MD operationalizing definitions tighter than §13 v1 | Founder + Eng |
| §11 Feedback Loop Surfacing Doc | MD; pairs with FINANCE variance review | Founder + Strategy CoS |
| Cohort-Behavioral Grid Review Template | MD; pairs with §3.8 | Strategy CoS |

## 5. Assumptions to validate

1. **ASSUMPTION** — MAVT (Monthly Active Validated Traders) as defined in §13.1 is the right north-star through P5. Phase 3 instruments and runs it; if Phase 4 raise narrative finds investor-legibility issues, definition tightens but primacy holds.
2. **ASSUMPTION** — VCSE (Validated Cohort Signal Effectiveness) companion metric is computable from existing engine instrumentation by P3 mid-point. If not, METRICS Phase 3 ships MAVT-only and VCSE rolls to Phase 4.
3. **ASSUMPTION** — Weekly internal report cadence (founder + any contractor) lands at the same anchor as Op-1 weekly ops review — not a separate meeting. METRICS feeds the agenda, not creates a second one.
4. **ASSUMPTION** — Monthly stakeholder report has two live variants in Phase 3: light (founder-cohort users) + full (advisors). Investor variant lands in Phase 4 once Phase 4 narrative posture is set.
5. **ASSUMPTION** — §13 conditional red-line alert can be wired through existing notification infra (Telegram + email) without new tooling. If not, decision needed (M-3 below).
6. **ASSUMPTION** — Anti-overclaim audit can run at publish-time as a checklist; it does not require automated linting in Phase 3. Automation is Phase 4+ if audit-volume justifies.

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **M-1** | MAVT operational definition tightening | (a) Ratify §13.1 v1 (≥1 engine-scored signal evaluated in last 30 days). (b) Tighten — require ≥1 gate decision *acted on* (accept or override). (c) Loosen — any signal viewed in dashboard counts. | Founder | Phase 3 week 2 | Internal report semantics, §15 narrative |
| **M-2** | VCSE Phase 3 ship vs Phase 4 ship | (a) Ship in Phase 3 alongside MAVT. (b) Defer to Phase 4 — MAVT-only weekly. (c) Ship VCSE as monthly-only in Phase 3, weekly in Phase 4. | Founder + Eng | Phase 3 week 3 | Weekly report scope; §15 narrative readiness |
| **M-3** | §13 conditional red-line alert delivery | (a) Telegram + email to founder. (b) PagerDuty-equivalent (BetterStack already wired per §10.4). (c) Linear ticket auto-create at threshold. | Founder + Eng | Phase 3 week 2 | Alert latency, response discipline |
| **M-4** | Investor-variant monthly report timing | (a) Ship in Phase 3 (early discipline). (b) Ship at Phase 4 raise opening. (c) Ship at first investor conversation, whichever comes first. | Founder | Phase 3 week 4 | Phase 4 narrative readiness |
| **M-5** | Public metric surface scope | (a) Pricing page only. (b) Pricing page + status page. (c) Pricing page + status page + public roadmap teaser + monthly public update. | Founder + Strategy CoS | Phase 3 week 3 | Audit surface area; trust signal scope |
| **M-6** | Vanity-metric handling rule | (a) Exclude entirely from internal reports. (b) Tag and include with explicit "vanity" label. (c) Include in marketing-only reports; exclude from operating reports. | Founder + Strategy CoS | Phase 3 week 2 | Discipline against drift |

## 7. Failure modes to avoid

- **MAU substitution.** "We had 5,000 visitors this week" is not MAVT and is not the north-star. Vanity metric drift is the highest-impact METRICS failure mode at P3 stabilization. Per Decision **M-6**, vanity is either excluded or explicitly tagged.
- **Pricing page implies actuals when it shows assumptions.** Per §6.10 Flag 2 + §13.8 audit — any number that's a *target* must read as a target; any number that's an *assumption* must read as an assumption. "Average drawdown 3.2%" without a "validation cohort, n=27" qualifier is overclaim.
- **§14 stop-the-line condition without measured signal.** A condition like "cohort drawdown exceeds §8 threshold" is *policy*; without an instrumented signal feeding §14 trigger logic, policy doesn't fire. Audit catches this.
- **Red-line alert that lapses without escalation.** §13 conditional red-line is the first non-§14 hard signal. If the alert fires and is silently muted, the discipline is gone. Escalation path: alert → 24h founder response → if no response, log to `_decisions/decision-log.md` automatically.
- **Weekly report that becomes a status update.** Status updates are passive ("here's what happened"). Weekly report is decision-forcing ("here's what we're going to do about it"). Template structure enforces this.
- **Monthly stakeholder report drifts to optimism.** Founder-cohort users and advisors deserve honest data, not curated. Anti-overclaim audit applies to monthly reports as much as pricing pages. Specific failure: omitting `Active` risks from §12 register because they "haven't triggered."
- **§11 feedback-loop surfacing missed.** If `A` (assumed) inputs reach `O` (observed) and §11 variance review doesn't catch it, model assumptions stay stale. METRICS owns the *surfacing*; FINANCE owns the *response*.
- **Persona-segmented reads collapsed to aggregate.** Omar / Karim / Layla behavior diverges meaningfully (per §3.8); aggregate reports hide persona-specific failures. Phase 3 NEXT task enforces segmentation in monthly report.
- **OKR review that just rolls forward.** Q review must close KRs (Done / Carried / Killed-with-reason) — rolling forward unmodified is a sign the OKR was wrong, not that the work is incomplete.

## 8. Tasks (canonical list)

### NOW

**`[DOC] METRICS — Weekly Internal Report Template v1`**
- **Objective:** Lock the weekly internal report template — agenda, sections (MAVT, funnel, gate health, vendor uptime, §12 risk transitions, decisions), KPI feeds, decision triggers.
- **Why:** Without a template, weekly review is freelance and the cadence quality is operator-dependent. Template is the contract.
- **Dependency:** §13 v1 framework (north-star, 5-layer tree, weekly section); Phase 3 OPERATIONS Op-1 (cadence anchor).
- **Output:** Template MD; first run scheduled.

**`[DOC] METRICS — MAVT + VCSE Definition Doc v1.1`**
- **Objective:** Tighten §13.1 MAVT operational definition (Decision **M-1**); operationalize VCSE companion metric or defer (Decision **M-2**).
- **Why:** §13 v1 defined MAVT semantically; instrumentation requires precision (what counts as "evaluated"? gate-decision acted on?). Without v1.1 the weekly report has definition ambiguity.
- **Dependency:** §13 v1; engine instrumentation inventory.
- **Output:** Definition doc MD; signed; feeds Decisions **M-1**, **M-2**.

**`[BUILD] METRICS — §13 Conditional Red-Line Monitor`**
- **Objective:** Wire alert on cohort gate-rejection acceptance <50% (the §13 conditional-escalation red-line).
- **Why:** This is the first non-§14 hard red-line; without an alert it's policy without enforcement. Per Decision **M-3** delivery channel.
- **Dependency:** §13.4 gate-rejection acceptance metric; notification infra; Decision **M-3**.
- **Output:** Alert wired; test fire executed; SOP doc.

**`[QA] METRICS — §14 Stop-the-Line Instrumentation Audit`**
- **Objective:** Audit every of the six §14 stop-the-line conditions + the §13 conditional — confirm each has an instrumented signal with defined source, threshold, owner.
- **Why:** §14 conditions without measurement are aspirational. The audit catches the gaps before a real fire.
- **Dependency:** §14 v1 conditions; §13 KPI feeds; engine + Stripe + vendor instrumentation.
- **Output:** Audit report MD with condition × signal × threshold × source × owner table; remediation backlog if any.

**`[DOC] METRICS — Public Metric Surface Inventory`**
- **Objective:** Catalogue every public surface that displays a number — pricing page, status page, public roadmap teaser, monthly update, social, blog.
- **Why:** Anti-overclaim audit needs an inventory. You can't audit what you haven't enumerated. Feeds Decision **M-5**.
- **Dependency:** Phase 1 anti-claim list; §6.10 Flag 2; §13.8 audit; §9 messaging matrix.
- **Output:** Inventory MD with per-surface audit status.

### NEXT

**`[DOC] METRICS — Monthly Stakeholder Report Template v1 (light + full)`**
- **Objective:** Lock the monthly report templates — light variant (founder-cohort users), full variant (advisors). Investor variant per Decision **M-4**.
- **Why:** Monthly cadence inherits weekly; explicit template avoids monthly drift to "longer weekly."
- **Dependency:** Weekly Internal Report Template v1; §13.7 reporting templates.
- **Output:** Two template MDs; first run scheduled.

**`[OPS] METRICS — Anti-Overclaim Audit (run on every public surface)`**
- **Objective:** Run the audit checklist against each surface in the inventory. Patch overclaim language. Re-audit pre-publish.
- **Why:** Audit without execution is filing. The audit is the discipline.
- **Dependency:** Public Metric Surface Inventory; Anti-Overclaim Audit Pre-Publish Checklist.
- **Output:** Audit report; per-surface remediation; re-audit clean.

**`[DOC] METRICS — Anti-Overclaim Audit Pre-Publish Checklist`**
- **Objective:** Codify the checklist any new public surface must pass before publish — claim language, qualifier presence, stabilizing-status surfacing, source-citation discipline.
- **Why:** Process-isolating overclaim risk. Surface owners (eng, design, founder) inherit the checklist; audit becomes self-served.
- **Dependency:** Phase 1 anti-claim list; §6.10 Flag 2; §9 messaging matrix.
- **Output:** Checklist MD; pre-publish gate doc.

**`[DOC] METRICS — OKR Quarterly Review SOP`**
- **Objective:** Codify the Q-cycle — review existing KRs (Done / Carried / Killed-with-reason), reset for next Q, close cadence.
- **Why:** OKR quality is mostly review quality. SOP enforces close discipline.
- **Dependency:** §13.3 Q1 OKRs; §13 v1 cadence.
- **Output:** SOP MD; first cycle scheduled.

**`[DOC] METRICS — §11 Feedback Loop Surfacing Doc`**
- **Objective:** Define how `A` (assumed) inputs in §11 reach `O` (observed) status, where the reclassification is logged, and how it surfaces in the monthly report and FINANCE variance review.
- **Why:** Without explicit surfacing, model assumptions stay stale and §11 v1.1 never closes.
- **Dependency:** §11 source taxonomy; FINANCE variance review SOP.
- **Output:** Surfacing doc MD; sample reclassification logged.

**`[OPS] METRICS — Weekly Report (run for 4 consecutive weeks)`**
- **Objective:** Run the weekly report four consecutive weeks; iterate the template based on what's actually useful and what's noise.
- **Why:** Template quality from running, not from designing. Same logic as OPS weekly review.
- **Dependency:** Weekly Internal Report Template v1.
- **Output:** Four signed reports; template revisions logged.

**`[OPS] METRICS — Monthly Report (run once)`**
- **Objective:** Execute first monthly stakeholder report at end of Phase 3 month 1.
- **Why:** Same logic as weekly — discipline from running.
- **Dependency:** Monthly Stakeholder Report Template v1.
- **Output:** Signed monthly report; template revisions logged.

### LATER

**`[DOC] METRICS — Persona-Segmented Metric Reads (Omar / Karim / Layla)`**
- **Objective:** Define the persona cuts on activation, retention, gate-acceptance, NPS, tier migration. Add to monthly report.
- **Why:** §3.8 cohort grid only realizes value if surfaced segmented; aggregate hides persona-specific failures.
- **Dependency:** §3.8 cohort grid; user persona tagging in product; monthly report template.
- **Output:** Persona reads MD; monthly report extended.

**`[DOC] METRICS — Cohort-Behavioral Grid Review Template`**
- **Objective:** Monthly review template for §3.8 cohort grid — gate-rejection acceptance, multi-account setup, journal review frequency, tier-upgrade trigger pattern, NPS.
- **Why:** Grid is locked; review cadence is what makes it operational.
- **Dependency:** §3.8 grid; monthly report template.
- **Output:** Review template MD; monthly slot scheduled.

**`[BUILD] METRICS — Investor Variant Monthly Report`**
- **Objective:** Investor-facing variant of the monthly report. Activate per Decision **M-4** timing.
- **Why:** Phase 4 readiness; not Phase 3 commitment unless raise opens early.
- **Dependency:** Full-variant monthly report; Phase 4 raise posture decision.
- **Output:** Variant template MD.

**`[QA] METRICS — Quarterly Anti-Overclaim Re-Audit`**
- **Objective:** Re-audit every public metric surface quarterly; catch surfaces added since last audit.
- **Why:** Public surfaces grow; audit must be recurring, not one-time.
- **Dependency:** Anti-Overclaim Audit Pre-Publish Checklist; Public Metric Surface Inventory.
- **Output:** Quarterly audit report; remediation backlog.
