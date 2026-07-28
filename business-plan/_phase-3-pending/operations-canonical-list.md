# OPERATIONS — Canonical Task List (Phase 3 staging)

**Status:** **ABSORBED 2026-05-05.** Canonical list now lives in `_phase-3/01-operations.md` Section 8. Scaffold sections 3 / 4 / 6 / 7 adjusted to align with new task surface. This file is retained as a record of the user-supplied canonical list and the prior-draft → canonical-list transition.
**Source of truth:** user-supplied canonical list 2026-05-05, reproduced verbatim.
**Format:** `[TYPE] [AREA] — Action / Deliverable`. Per-task fields (Objective · Why · Dependency · Output) expanded in `_phase-3/01-operations.md` during absorption.

---

## Why this exists

Per the Phase 1 / Phase 2 precedent (`_phase-1/_phase-1-pending/brand-canonical-list.md`, `_phase-2-pending/packaging-canonical-list.md`), user-supplied canonical lists are reproduced verbatim in a `pending/` record file before being absorbed into the phase scaffold. The record file:

- Preserves the verbatim list as authored.
- Documents what changed in the scaffold during absorption.
- Anchors any future de-dup or re-sequencing decisions.

---

## A. OPERATIONS — canonical list (verbatim)

### NOW

- `[OPS] OPERATIONS — Business Operating Cadence`
- `[DOC] OPERATIONS — Weekly Planning and Review Workflow`
- `[DOC] OPERATIONS — Decision Log System`
- `[DOC] OPERATIONS — Cross-Functional Handshake Rules`
- `[OPS] OPERATIONS — Workstream Ownership Map`

### NEXT

- `[DOC] OPERATIONS — Incident Response Escalation Model`
- `[DOC] OPERATIONS — Vendor Review Cadence`
- `[DOC] OPERATIONS — Launch Readiness Checklist`
- `[QA] OPERATIONS — Current Workflow Friction Audit`
- `[OPS] OPERATIONS — Documentation Maintenance Rhythm`

### LATER

- `[DOC] OPERATIONS — Scale-Stage Operating System`
- `[DOC] OPERATIONS — Internal Governance Framework`

---

## B. What changed in the scaffold during absorption

| Prior-draft task (`_phase-3/01-operations.md` 2026-05-05 first pass) | Canonical task it maps to | Action |
|---|---|---|
| `[DOC] OPERATIONS — Operating Cadence Document v1` | `[OPS] OPERATIONS — Business Operating Cadence` | Renamed; same intent |
| `[DOC] OPERATIONS — Engine Release Runbook` | (no direct map) | **Moved out of Phase 3 scope** — engine release runbook is a §10 / PCC v2 operational artifact, not an OPERATIONS-workstream Phase 3 deliverable. Re-staged as `_phase-3-pending/engine-release-runbook-followup.md` for Phase 3.5 / Phase 4 placement |
| `[DOC] OPERATIONS — Founder-Unavailable Protocol (§16 Cont. C)` | (no direct map) | **Moved to COMPLIANCE workstream** — §16 Cont. C is a contingency-protocol operationalization, fits COMPLIANCE more than OPERATIONS |
| `[OPS] OPERATIONS — Cadence Calendar v1` | Sub-deliverable of `[OPS] OPERATIONS — Business Operating Cadence` | Absorbed; calendar artifact lives under cadence task |
| `[DOC] OPERATIONS — Tooling Sync Discipline SOP` | `[OPS] OPERATIONS — Documentation Maintenance Rhythm` | Renamed; broader scope (rhythm, not just sync) |
| 5× `[DOC] OPERATIONS — Vendor Swap Runbook (X)` | `[DOC] OPERATIONS — Vendor Review Cadence` | **Compressed** — single cadence doc covers vendor review (which includes swap drills as a sub-event), instead of five separate runbooks. Per-vendor runbooks become sub-artifacts under the cadence |
| `[DOC] OPERATIONS — Incident Review / Postmortem Template` | `[DOC] OPERATIONS — Incident Response Escalation Model` | Renamed; broader scope (escalation model includes postmortem template as a downstream artifact) |
| `[OPS] OPERATIONS — Weekly Ops Review (run for 4 weeks)` | Sub-deliverable of `[DOC] OPERATIONS — Weekly Planning and Review Workflow` | Absorbed; "run for 4 weeks" is the quality-by-execution sub-step under the workflow design |
| `[OPS] OPERATIONS — Monthly Ops Review (run once)` | Sub-deliverable of `[OPS] OPERATIONS — Business Operating Cadence` | Absorbed |
| `[DOC] OPERATIONS — Quarterly Ops Review Template` | Sub-deliverable of `[OPS] OPERATIONS — Business Operating Cadence` | Absorbed |
| `[BUILD] OPERATIONS — Vendor Swap Hardening (post-drill)` | Sub-deliverable of `[DOC] OPERATIONS — Vendor Review Cadence` | Absorbed |
| `[OPS] OPERATIONS — Cadence Audit (after consecutive lapses)` | Sub-deliverable of `[OPS] OPERATIONS — Business Operating Cadence` | Absorbed |

| New canonical task | Prior coverage | Action |
|---|---|---|
| `[DOC] OPERATIONS — Decision Log System` | partial — `_decisions/decision-log.md` exists but not as a *system* | **NET-NEW scaffold expansion** — formalize log discipline, entry rules, review cadence, archival rules |
| `[DOC] OPERATIONS — Cross-Functional Handshake Rules` | not covered | **NET-NEW** — METRICS↔FINANCE, OPS↔COMPLIANCE, founder↔contractor handshakes |
| `[OPS] OPERATIONS — Workstream Ownership Map` | not covered | **NET-NEW** — explicit RACI across all workstreams |
| `[DOC] OPERATIONS — Launch Readiness Checklist` | partially covered by ROADMAP phase-gate readiness review | **NET-NEW** — operational variant; complements ROADMAP phase-gate review |
| `[QA] OPERATIONS — Current Workflow Friction Audit` | not covered | **NET-NEW** — audit existing flow before designing new SOPs |
| `[DOC] OPERATIONS — Scale-Stage Operating System` | LATER scope | **NET-NEW LATER** — Phase 5+ design |
| `[DOC] OPERATIONS — Internal Governance Framework` | LATER scope | **NET-NEW LATER** — Phase 4+ design |

---

## C. Re-staged out of Phase 3 scope

These prior-draft items did not map cleanly to the canonical list and have been re-staged for later placement:

- `[DOC] OPERATIONS — Engine Release Runbook` → re-stage as `_phase-3-pending/engine-release-runbook-followup.md`. This is a §10 / PCC v2 artifact; it deserves a home but not under the OPERATIONS workstream Phase 3 scaffold per the canonical list.
- `[DOC] OPERATIONS — Founder-Unavailable Protocol (§16 Cont. C)` → moved to COMPLIANCE workstream task list (closer to the §16 contingency operationalization scope).

---

## D. Open de-dup decisions

Two overlap surfaces flagged for de-dup at the appropriate phase:

| Canonical task | Overlapping work | De-dup recommendation |
|---|---|---|
| `[DOC] OPERATIONS — Vendor Review Cadence` | `[OPS] COMPLIANCE — CoinGlass Quarterly Review` (likely Phase 3 COMPLIANCE NOW); §10.3 vendor SLA matrix | OPERATIONS owns the cadence *mechanism*; COMPLIANCE owns the *risk-relationship review* (CoinGlass dual relationship per R-007). Same calendar slot, two complementary outputs |
| `[DOC] OPERATIONS — Launch Readiness Checklist` | `[DOC] ROADMAP — Phase-Gate Readiness Review SOP` | Strict overlap risk — checklist is the *artifact*, SOP is the *protocol*. Recommend: Phase 3 ROADMAP owns SOP, Phase 3 OPERATIONS owns checklist; merge if redundant after first run |

---

## E. What I did NOT do

- Did **not** re-author Sections 1, 2, 5 of `_phase-3/01-operations.md` (purpose / why / assumptions are stable).
- Did **not** delete prior-draft Section 8 content — it was overwritten with the canonical list, with mapping recorded above.
- Did **not** modify `_phase-3/00-phase-3-charter.md` Section 6 outputs status — `01-operations.md` remains DONE.
- Did **not** change Phase 3 charter §2 in/out-of-scope; the canonical list fits within the existing scope envelope.

Phase 3 OPERATIONS scaffold is now aligned with the user-supplied canonical list. Awaiting canonical lists for METRICS, FINANCE, ROADMAP, COMPLIANCE.
