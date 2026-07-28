# METRICS — Canonical Task List (Phase 3 staging)

**Status:** **ABSORBED 2026-05-05.** Canonical list now lives in `_phase-3/02-metrics.md` Section 8. Scaffold sections 3 / 4 / 6 / 7 adjusted to align with new task surface. This file is retained as a record of the user-supplied canonical list and the prior-draft → canonical-list transition.
**Source of truth:** user-supplied canonical list 2026-05-05, reproduced verbatim.
**Format:** `[TYPE] [AREA] — Action / Deliverable`. Per-task fields (Objective · Why · Dependency · Output) expanded in `_phase-3/02-metrics.md` during absorption.

---

## A. METRICS — canonical list (verbatim)

### NOW

- `[METRICS] METRICS — North Star Metric Recommendation`
- `[METRICS] METRICS — Leading vs Lagging KPI Map`
- `[DOC] METRICS — KPI Definitions and Owners`
- `[METRICS] METRICS — Activation and Retention Measurement Framework`
- `[METRICS] METRICS — GTM and Revenue Dashboard Spec`

### NEXT

- `[METRICS] METRICS — Trust and Reliability KPI Set`
- `[METRICS] METRICS — Support and Onboarding KPI Set`
- `[DOC] METRICS — Weekly Business Review Template`
- `[DOC] METRICS — Monthly Executive Review Template`
- `[QA] METRICS — Metric Instrumentation Gap Review`

### LATER

- `[METRICS] METRICS — Fundraising KPI Pack`
- `[METRICS] METRICS — Scale-Stage Executive Scorecard`

---

## B. What changed in the scaffold during absorption

| Prior-draft task (`_phase-3/02-metrics.md` 2026-05-05 first pass) | Canonical task it maps to | Action |
|---|---|---|
| `[DOC] METRICS — MAVT + VCSE Definition Doc v1.1` | `[METRICS] METRICS — North Star Metric Recommendation` + `[DOC] METRICS — KPI Definitions and Owners` | Absorbed; MAVT/VCSE definition lives inside the North Star recommendation + KPI definitions doc |
| `[DOC] METRICS — Weekly Internal Report Template v1` | `[DOC] METRICS — Weekly Business Review Template` | Renamed; repositioned NOW → NEXT (per canonical sequencing — KPI structure NOW, review templates NEXT) |
| `[BUILD] METRICS — §13 Conditional Red-Line Monitor` | (no direct map — sub-task of `[METRICS] METRICS — Trust and Reliability KPI Set` or `[QA] METRICS — Metric Instrumentation Gap Review`) | **Absorbed** into Trust and Reliability KPI Set as instrumentation sub-deliverable; alert wiring covered there |
| `[QA] METRICS — §14 Stop-the-Line Instrumentation Audit` | `[QA] METRICS — Metric Instrumentation Gap Review` | Renamed; broader scope (gap review covers §14 stop-the-line + all KPI instrumentation gaps) |
| `[DOC] METRICS — Public Metric Surface Inventory` | (no direct map) | **Re-staged** — moved to Phase 3 GTM follow-up (Phase 3.5) under public-roadmap / public-surface scope. Anti-overclaim audit cadence absorbed into Monthly Executive Review Template |
| `[DOC] METRICS — Monthly Stakeholder Report Template v1 (light + full)` | `[DOC] METRICS — Monthly Executive Review Template` | Renamed; light/full variants become sub-deliverables under the canonical task |
| `[OPS] METRICS — Anti-Overclaim Audit (run on every public surface)` | (no direct map) | **Re-staged** — covered under Monthly Executive Review Template (audit cadence) + Phase 3.5 public-surface scope |
| `[DOC] METRICS — Anti-Overclaim Audit Pre-Publish Checklist` | (no direct map) | **Re-staged** — moved to Phase 1 BRAND `[DOC] BRAND — Brand Do/Don't Examples` follow-up or POSITIONING `[DOC] POSITIONING — Claim Language Guardrails` (closer fit) |
| `[DOC] METRICS — OKR Quarterly Review SOP` | (no direct map) | **Moved to OPERATIONS** — quarterly OKR review is a cadence sub-deliverable under `[OPS] OPERATIONS — Business Operating Cadence` |
| `[DOC] METRICS — §11 Feedback Loop Surfacing Doc` | (no direct map) | **Moved to FINANCE** — A→O reclassification feedback loop is a §11 variance-review concern |
| `[OPS] METRICS — Weekly Report (run for 4 consecutive weeks)` | Sub-deliverable of `[DOC] METRICS — Weekly Business Review Template` | Absorbed |
| `[OPS] METRICS — Monthly Report (run once)` | Sub-deliverable of `[DOC] METRICS — Monthly Executive Review Template` | Absorbed |
| `[DOC] METRICS — Persona-Segmented Metric Reads (Omar / Karim / Layla)` | Sub-deliverable of `[METRICS] METRICS — Activation and Retention Measurement Framework` | Absorbed |
| `[DOC] METRICS — Cohort-Behavioral Grid Review Template` | Sub-deliverable of `[METRICS] METRICS — Activation and Retention Measurement Framework` | Absorbed |
| `[BUILD] METRICS — Investor Variant Monthly Report` | `[METRICS] METRICS — Fundraising KPI Pack` | Renamed/expanded; canonical task is the Phase 4 raise-grade KPI pack, of which investor monthly is a deliverable |
| `[QA] METRICS — Quarterly Anti-Overclaim Re-Audit` | Sub-deliverable of `[QA] METRICS — Metric Instrumentation Gap Review` (recurring trigger) | Absorbed |

| New canonical task | Prior coverage | Action |
|---|---|---|
| `[METRICS] METRICS — North Star Metric Recommendation` | partial — §13 v1 already locked MAVT + VCSE companion | **NET-NEW positioning** — Phase 3 task is to *recommend ratify-or-revise* of §13 v1 north-star against P0/P1 cohort observed data, not pick from scratch |
| `[METRICS] METRICS — Leading vs Lagging KPI Map` | not covered | **NET-NEW** — explicit lead/lag classification across §13 5-layer tree |
| `[DOC] METRICS — KPI Definitions and Owners` | partial — §13 v1 named KPIs without explicit per-KPI owner | **NET-NEW expansion** — every KPI has named owner (in addition to definition tightening) |
| `[METRICS] METRICS — Activation and Retention Measurement Framework` | partial — §13 funnel KPIs + §3.8 cohort grid exist | **NET-NEW consolidation** — single framework spanning Free → Trader activation, Trader retention, tier-up paths, persona-segmented |
| `[METRICS] METRICS — GTM and Revenue Dashboard Spec` | partial — Phase 2 GTM funnel instrumentation exists | **NET-NEW spec** — dashboard *spec* (what's surfaced where, refresh cadence, owner), not the dashboard build itself |
| `[METRICS] METRICS — Trust and Reliability KPI Set` | not covered as cohesive set — §13.4 risk KPIs scattered | **NET-NEW consolidation** — vendor uptime, gate health, kill-switch activation, SLA compliance, support response, drawdown discipline as one set |
| `[METRICS] METRICS — Support and Onboarding KPI Set` | partial — §10 SLA targets exist; Phase 2 ONBOARDING activation milestones exist | **NET-NEW consolidation** — single set for support response, resolution time, ticket volume by tier; onboarding signup→first-signal→first-gate-decision conversion |
| `[METRICS] METRICS — Scale-Stage Executive Scorecard` | LATER scope | **NET-NEW LATER** — Phase 5+ executive-level scorecard concept |

---

## C. Re-staged out of Phase 3 METRICS scope

These prior-draft items did not map cleanly to the canonical list and have been re-staged for placement elsewhere:

- `[DOC] METRICS — Public Metric Surface Inventory` → re-stage to Phase 3.5 (post-channel-mix-selection) under public-surface / content-surface scope.
- `[OPS] METRICS — Anti-Overclaim Audit (run on every public surface)` → cadence absorbed into Monthly Executive Review Template; full audit pass re-staged to Phase 3.5.
- `[DOC] METRICS — Anti-Overclaim Audit Pre-Publish Checklist` → re-stage to Phase 1 BRAND `[DOC] BRAND — Brand Do/Don't Examples` follow-up (closer brand-voice fit) or POSITIONING claim-guardrails follow-up.
- `[DOC] METRICS — OKR Quarterly Review SOP` → moved to OPERATIONS scaffold (cadence sub-deliverable).
- `[DOC] METRICS — §11 Feedback Loop Surfacing Doc` → moved to FINANCE scaffold (variance-review concern).

---

## D. Open de-dup decisions

| Canonical task | Overlapping work | De-dup recommendation |
|---|---|---|
| `[METRICS] METRICS — Trust and Reliability KPI Set` | §13.4 v1 risk KPIs; §14 stop-the-line conditions; Phase 3 COMPLIANCE risk-monitoring | METRICS owns the *KPI set* (definitions, instrumentation, dashboard surfacing); COMPLIANCE owns the *risk-register transitions*. Same numbers, different consumption surface |
| `[METRICS] METRICS — Support and Onboarding KPI Set` | §10.1 SLA matrix; Phase 2 ONBOARDING activation milestones; Phase 2 SUPPORT severity matrix | METRICS owns the *measurement framework*; OPERATIONS owns *cadence-of-review*; SUPPORT/ONBOARDING own the *target SLA values*. Three roles, one KPI set |
| `[DOC] METRICS — Weekly Business Review Template` | `[DOC] OPERATIONS — Weekly Planning and Review Workflow` | Strict overlap risk — METRICS owns the *KPI feed* into the workflow; OPERATIONS owns the *workflow agenda*. Single weekly meeting, two complementary artifacts. Confirm de-dup at Phase 3 mid-point |
| `[DOC] METRICS — Monthly Executive Review Template` | OPERATIONS monthly cadence (Op-1 → monthly slot) | Same handshake — METRICS feeds the agenda, OPERATIONS owns the cadence anchor |

---

## E. What I did NOT do

- Did **not** re-author Sections 1, 2, 5 of `_phase-3/02-metrics.md` (purpose / why / assumptions are stable, with light edits to align Section 5 assumptions to canonical task names).
- Did **not** delete prior-draft Section 8 content — it was overwritten with the canonical list, with mapping recorded above.
- Did **not** modify `_phase-3/00-phase-3-charter.md` Section 6 outputs status — `02-metrics.md` remains DONE.
- Did **not** change Phase 3 charter §2 in/out-of-scope; the canonical list fits within the existing scope envelope.

Phase 3 METRICS scaffold is now aligned with the user-supplied canonical list. Awaiting canonical lists for FINANCE, ROADMAP, COMPLIANCE.
