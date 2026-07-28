# 01 — OPERATIONS

**Workstream:** OPERATIONS
**Phase:** 3 — Operating System
**Status:** Canonical list ABSORBED 2026-05-05 from user-supplied list (record retained at `_phase-3-pending/operations-canonical-list.md`).
**Canonical authorities:** v1 framework `10-operations-support.md`; `_data/operations/Production_Candidate_Criteria_v2.md`; `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`; `_data/operations/OPS_Linear_Tickets_v1.md`; project memory `coinscopeai-platform-sync`, `feedback_session_start_protocol`, `reference_automation`.

---

## 1. Purpose

Lock the **operating cadence, decision discipline, and ownership clarity** that holds CoinScopeAI together while it ships under load. OPERATIONS extends the Phase 2 SUPPORT runbooks (severity, triage, escalation, vendor-outage comms) into the broader operating rhythm: how the founder + P4 contractors actually run the company day to day, week to week, month to month — *and* the governing artifacts (decision log, workstream ownership map, handshake rules, friction audit) that make the cadence durable rather than personality-dependent.

## 2. Why this matters specifically for CoinScopeAI

- **Solo founder posture is the discipline, not a constraint to apologize for.** Per §10 SLA defensibility — we don't promise enterprise-grade ops we can't meet. The cadence is the thing that makes solo+P4 defensible.
- **Capital-preservation extends to operations.** Per §5.3.1 — the kill switch operates regardless of tier. The operating cadence is the system that ensures the discipline *holds* across release, vendor change, and §16 contingency events.
- **Decision-log discipline is the cheapest moat.** `_decisions/decision-log.md` already exists; without a *system* (entry rules, review cadence, archival rules) it drifts to "the founder remembers." Phase 3 codifies the system.
- **Cross-functional handshakes invisible until they fail.** METRICS surfaces a `A` → `O` reclassification → FINANCE owns variance → OPERATIONS owns cadence to land both. Without explicit handshake rules, the boundary is freelance.
- **Workstream ownership map is the remediation surface.** When something goes wrong (overclaim leak, missed audit, lapsed cadence), "who owns this" is the first question. Implicit ownership = no remediation.
- **Tooling-sync drift is silent** — Linear / Notion / GitHub / Drive all maintain their own state, and the cost of drift compounds invisibly. Documentation maintenance rhythm closes the loop.
- **Workflow friction compounds.** New SOPs without a friction audit on the existing flow are SOPs piled on top of bad flow. Audit-first discipline.

## 3. Required subsections

1. **Business operating cadence (D / W / M / Q)** — what happens daily, weekly, monthly, quarterly; who attends; what artifacts are produced; cadence calendar with hard-blocked slots.
2. **Weekly planning and review workflow** — explicit agenda, KPI feeds, decision triggers, output artifacts. Run for ≥4 consecutive weeks before signed.
3. **Decision log system** — entry rules (what constitutes a decision), schema (date / decision / options / chosen / rationale / impact), review cadence, archival rules. Operationalizes `_decisions/decision-log.md`.
4. **Cross-functional handshake rules** — METRICS↔FINANCE (A→O reclassification), OPS↔COMPLIANCE (risk transitions), OPS↔ROADMAP (phase-gate readiness), founder↔contractor (P4 onboarding + handoff).
5. **Workstream ownership map** — RACI across all 7 Phase 1 + 5 Phase 2 + 5 Phase 3 workstreams. Single canonical artifact.
6. **Incident response escalation model** — when a Sev-1/Sev-2 fires, who's notified when, what the escalation chain is, when comms go out, when postmortem happens. Postmortem template is a downstream artifact.
7. **Vendor review cadence** — recurring review (quarterly minimum) of every P1 vendor. Includes swap-drill scheduling, SLA review, pricing review, relationship review. Per-vendor runbooks live as sub-artifacts under the cadence.
8. **Launch readiness checklist** — operational variant of the ROADMAP phase-gate review. Per phase boundary (P2→P3, P3→P4, P4→P5): runbook readiness, vendor SLA stable, support staffing, comms drafted.
9. **Workflow friction audit** — current-state audit of existing operating flow (Linear pipeline, code review, deploy, support, billing). What's slow / brittle / personality-dependent / undocumented.
10. **Documentation maintenance rhythm** — Linear ↔ Notion ↔ GitHub ↔ Drive ↔ MemPalace sync rules; drift-detector audit cadence; CLAUDE.md snapshot policy; design-system manifest sync.
11. **Scale-stage operating system** (LATER) — what changes at headcount > 3, geography > 1, venue > 1.
12. **Internal governance framework** (LATER) — board / advisor / contractor governance posture, decision rights, escalation authority.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Business Operating Cadence v1 | MD + calendar artifact (hard-blocked recurring slots) | Founder + Strategy CoS |
| Weekly Planning and Review Workflow | MD template + 4-week run record | Founder |
| Decision Log System SOP | MD; operationalizes `_decisions/decision-log.md` | Founder + Strategy CoS |
| Cross-Functional Handshake Rules | MD with handshake diagram per pair | Founder + Strategy CoS |
| Workstream Ownership Map (RACI) | MD table (workstream × role × R/A/C/I) | Founder |
| Incident Response Escalation Model | MD + postmortem template + completed-review index | Founder |
| Vendor Review Cadence | MD + per-vendor sub-artifacts (CCXT / CoinGlass / Tradefeeds / CoinGecko / Claude) | Founder + ops contractor (P4) |
| Launch Readiness Checklist (per phase) | MD checklist (P2→P3, P3→P4, P4→P5) | Founder |
| Workflow Friction Audit Report | MD audit + remediation backlog | Strategy CoS |
| Documentation Maintenance Rhythm SOP | MD; pairs with `reference_automation` memory | Founder |
| Scale-Stage Operating System (concept) | MD; *no commitments* tag | Founder |
| Internal Governance Framework (concept) | MD; *no commitments* tag | Founder |

## 5. Assumptions to validate

1. **ASSUMPTION** — Solo founder + 1–2 P4 contractors (per §5.4.7) is the right ops shape through P5. Phase 3 cadence is sized for this; if Phase 4 raise changes the shape, cadence redesigns.
2. **ASSUMPTION** — Linear remains the canonical task surface; Notion the canonical doc surface; GitHub the canonical code surface; Drive the curated mirror; MemPalace the agentic memory layer. No tool consolidation in Phase 3.
3. **ASSUMPTION** — Decision log already at `_decisions/decision-log.md` is the canonical surface. Phase 3 codifies the *system*, not relocates the file.
4. **ASSUMPTION** — Workstream Ownership Map can be built RACI-style with role-shorthand (Founder, Strategy CoS, Eng, Design, P4 Ops, P4 Eng) — explicit named-individual map is Phase 4+.
5. **ASSUMPTION** — Vendor review cadence is quarterly minimum; ad-hoc trigger on §12 register status transition (Monitoring → Active or Active → Triggered).
6. **ASSUMPTION** — Workflow friction audit can be self-served by Strategy CoS using shadowing + log review; external auditor is Phase 4+ if at all.
7. **ASSUMPTION** — Scale-stage and Internal Governance Framework are *concept-only* in Phase 3 — no commitments. Both activate at Phase 4 raise opening or Phase 5 Desk Full launch, whichever comes first.

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **Op-1** | Weekly review day + duration | (a) Sunday 90 min (UAE business-week start). (b) Thursday 60 min (UAE business-week end). (c) Both — Sunday plan + Thursday review. | Founder | Phase 3 week 1 | All cadence anchors hang off this |
| **Op-2** | Decision-log entry threshold | (a) Every named decision with downstream impact. (b) Only decisions affecting locked artifacts (framework, PCC, risk thresholds). (c) Decisions + locked-artifact reversals only. | Founder + Strategy CoS | Phase 3 week 1 | Log volume; review burden; audit coverage |
| **Op-3** | Workstream Ownership Map granularity | (a) Workstream-level only. (b) Workstream + sub-workstream (e.g., METRICS → MAVT, FINANCE → close, etc.). (c) Workstream + artifact-level. | Founder | Phase 3 week 2 | Map size; remediation precision |
| **Op-4** | Vendor review cadence frequency | (a) Quarterly all vendors. (b) Quarterly P1 critical (CCXT, CoinGlass) + bi-annual rest. (c) Monthly status only + quarterly deep review. | Founder | Phase 3 week 2 | Review burden; signal latency |
| **Op-5** | Incident escalation chain | (a) Founder direct on Sev-1 always. (b) Founder direct on Sev-1; designated contractor on Sev-2; founder on confirmation. (c) Tier-aware (Free / Trader / Desk Preview / Desk Full v2 escalation differs). | Founder | Phase 3 week 3 | Escalation latency; tier SLA defensibility |
| **Op-6** | Launch readiness checklist version per phase | (a) Single shared checklist with phase-specific addenda. (b) Per-phase checklist (P2→P3, P3→P4, P4→P5 each separate). | Founder + Strategy CoS | Phase 3 week 3 | Maintenance burden; per-phase precision |
| **Op-7** | Workflow friction audit scope | (a) All operating flow (Linear, code review, deploy, support, billing). (b) Top-3 highest-leverage only (operator-time-weighted). (c) Only flows with reported friction. | Strategy CoS | Phase 3 week 2 | Audit duration; remediation backlog size |
| **Op-8** | Documentation maintenance rhythm cadence | (a) Weekly drift-detector review. (b) Bi-weekly. (c) Daily detector emit + weekly human review. | Founder | Phase 3 week 1 | Drift latency; review burden |

## 7. Failure modes to avoid

- **Cadence calendar that's never on the calendar.** A weekly review doc that lives in `_phase-3/` but doesn't have a hard-blocked recurring slot is theatre. The calendar event *is* the SOP.
- **Decision log that's append-only and never read.** A log without a review cadence (per Decision **Op-2**) is filing, not discipline. Decisions need recall and audit, not just record.
- **Workstream Ownership Map at the wrong granularity.** Too coarse → "who owns this?" remains unanswered. Too fine → maintenance burden kills the artifact. Decision **Op-3** picks the right level.
- **Cross-functional handshake assumed.** The METRICS↔FINANCE handshake (A→O reclassification) happens silently or doesn't happen. Explicit rules + named owner per handshake.
- **Incident escalation chain untested.** Escalation that's never been exercised under load fails when it has to. Per Decision **Op-5**, dry-run escalation as part of incident-review onboarding for any new contractor.
- **Vendor review cadence that's just a status check.** Quarterly review must include relationship review, pricing review, swap-drill schedule, SLA review — not just "are we still up?"
- **Launch readiness checklist that's a wish list.** Each item must be binary (Done / Not done) with evidence pointer. Subjective items ("we feel ready") get killed.
- **Friction audit that becomes a redesign.** Audit surfaces friction; remediation is bounded backlog work, not a rewrite. Per Decision **Op-7** scope discipline.
- **Documentation maintenance rhythm that adds steps faster than it removes them.** Sync discipline is a tax on velocity if not curated. Per memory `feedback_drive_git_incompatibility` — repos cannot live in Drive.
- **Scale-stage / governance concepts written as commitments.** Both LATER tasks are *concepts* — `*no commitments*` tag enforces this. Concepts now reduce Phase 4 / Phase 5 ramp time without locking decisions prematurely.
- **Solo-founder cadence drift to "I know what's on my plate."** The discipline is the moat. Cadence cannot be optional.
- **Postmortem becoming a blame surface.** Postmortems must be blameless or they don't surface causes. Template enforces structure: timeline → contributing factors → corrective actions → owner → due date.

## 8. Tasks (canonical list — verbatim, absorbed 2026-05-05)

### NOW

**`[OPS] OPERATIONS — Business Operating Cadence`**
- **Objective:** Define and instate the daily / weekly / monthly / quarterly operating cadence — what happens, who attends, what artifacts are produced, what triggers an exception. Includes hard-blocked calendar slots, rollover policy, and lapse-handling rule.
- **Why:** Without a single cadence document plus calendar event, every cadence event is reinvented from memory. The cadence *is* the discipline that makes solo+P4 posture defensible (per §10 SLA framing). Cadence calendar + monthly + quarterly review templates are sub-deliverables.
- **Dependency:** v1 framework `10-operations-support.md`; Phase 2 SUPPORT runbooks; project memory `feedback_session_start_protocol`.
- **Output:** Cadence MD signed; calendar artifact wired with hard-blocked recurring slots; rollover policy documented; first weekly + monthly + quarterly slot scheduled. Feeds Decision **Op-1**.

**`[DOC] OPERATIONS — Weekly Planning and Review Workflow`**
- **Objective:** Codify the weekly review workflow — agenda, KPI feeds (from METRICS), §12 risk-register transitions (from COMPLIANCE), open-issue triage, decisions to log. Run for ≥4 consecutive weeks; iterate template based on what's actually useful.
- **Why:** Weekly cadence is the highest-frequency operating loop; quality compounds or degrades fastest here. Workflow without template = freelance. Quality from running, not from designing — 4-week run validates.
- **Dependency:** Business Operating Cadence; METRICS Weekly Internal Report Template (Phase 3 METRICS NOW); §12 risk register.
- **Output:** Workflow doc MD; 4 signed weekly review docs; agenda revisions logged.

**`[DOC] OPERATIONS — Decision Log System`**
- **Objective:** Operationalize `_decisions/decision-log.md` — entry rules (what constitutes a decision per Decision **Op-2**), schema (date / decision / options / chosen / rationale / impact / linked artifacts), review cadence (monthly), archival rules.
- **Why:** Log without system drifts to "the founder remembers." Per §15 due diligence and Phase 4 raise readiness, decision-log audit trail is a trust signal — not a filing exercise.
- **Dependency:** Existing `_decisions/decision-log.md`; project memory `feedback_premortem_required`, `reference_skill_risk_pcc_pre_flight`.
- **Output:** System SOP MD; entry-rule guide; first monthly review scheduled. Feeds Decision **Op-2**.

**`[DOC] OPERATIONS — Cross-Functional Handshake Rules`**
- **Objective:** Define the explicit handshakes between workstreams — METRICS↔FINANCE (A→O reclassification surfacing into variance review), OPS↔COMPLIANCE (risk-status transitions Monitoring→Active→Triggered), OPS↔ROADMAP (phase-gate readiness signal), founder↔contractor (P4 onboarding + handoff). Each handshake: trigger, owner, artifact, SLA.
- **Why:** Cross-functional boundaries are invisible until they fail. Handshakes assumed → handshakes lapsed. Explicit rules close the boundary risk.
- **Dependency:** Workstream Ownership Map; §11 source taxonomy (A/O/B); §12 status taxonomy (Monitoring/Active/Triggered/Resolved); §14 phase-gate criteria.
- **Output:** Handshake rules MD with handshake diagram per pair; named-owner per handshake; SLA per handshake.

**`[OPS] OPERATIONS — Workstream Ownership Map`**
- **Objective:** Build and sign the canonical RACI map across all CoinScopeAI workstreams — Phase 1 (MARKET, ICP, POSITIONING, PRODUCT, TRUST, RISK, BRAND), Phase 2 (PACKAGING, PRICING, ONBOARDING, SUPPORT, GTM), Phase 3 (OPERATIONS, METRICS, FINANCE, ROADMAP, COMPLIANCE).
- **Why:** When something goes wrong, "who owns this?" is the first question. Implicit ownership = no remediation. Granularity per Decision **Op-3**.
- **Dependency:** All Phase 1 + Phase 2 scaffolds; Phase 3 charter §7 crosswalk; role shorthand defined.
- **Output:** Ownership map MD (workstream × role × R/A/C/I); signed; pinned in Notion. Feeds Decision **Op-3**.

### NEXT

**`[DOC] OPERATIONS — Incident Response Escalation Model`**
- **Objective:** Codify the escalation chain when a Sev-1 / Sev-2 fires — who's notified when, comms timing, postmortem trigger, escalation timing. Includes blameless postmortem template as downstream sub-artifact + completed-review index.
- **Why:** §10.2 incident-response runbook covers *engine* incidents; escalation model covers the *organizational* response. Untested escalation chain fails when invoked.
- **Dependency:** §10.1 severity matrix; §10.2 incident-response runbook; Phase 2 SUPPORT vendor-outage runbooks; Cross-Functional Handshake Rules.
- **Output:** Escalation model MD; postmortem template MD; completed-review index. Feeds Decision **Op-5**.

**`[DOC] OPERATIONS — Vendor Review Cadence`**
- **Objective:** Recurring review (cadence per Decision **Op-4**) of every P1 vendor — CCXT, CoinGlass, Tradefeeds, CoinGecko, Claude. Includes swap-drill schedule, SLA review, pricing review, relationship review (CoinGlass dual-relationship per R-007), §12 register cross-check. Per-vendor runbooks live as sub-artifacts under the cadence.
- **Why:** Vendor risk is the highest-frequency external risk surface (§12 R-007 through R-012). Cadence converts policy into practice. Drills atrophy when stable; cadence forces practice.
- **Dependency:** §10.3 vendor SLA matrix; `Vendor_Failure_Mode_Mapping_v1.md`; §12 vendor risks; Cross-Functional Handshake Rules (OPS↔COMPLIANCE on R-007 review).
- **Output:** Cadence MD + 5 per-vendor sub-artifact runbooks; first review executed. Feeds Decision **Op-4**.

**`[DOC] OPERATIONS — Launch Readiness Checklist`**
- **Objective:** Operational variant of the ROADMAP phase-gate review — per phase boundary (P2→P3, P3→P4, P4→P5): runbook readiness, vendor SLA stable, support staffing adequate, comms drafted, billing tested, kill-switch validated. Binary items (Done / Not done) with evidence pointer.
- **Why:** Phase-gate readiness is a ROADMAP discipline at the *strategic* level; checklist is the *operational* surface. Both needed; OPS owns checklist, ROADMAP owns SOP.
- **Dependency:** ROADMAP phase-gate readiness SOP (Phase 3 ROADMAP NOW); §14 v1 phase progression; §13 OKR feeds.
- **Output:** Per-phase checklist MD (per Decision **Op-6** version structure); P2→P3 checklist signed and run.

**`[QA] OPERATIONS — Current Workflow Friction Audit`**
- **Objective:** Audit existing operating flow before designing new SOPs — Linear pipeline, code review, deploy flow, support flow, billing flow, sync flow. Identify what's slow / brittle / personality-dependent / undocumented. Bounded remediation backlog.
- **Why:** New SOPs without friction audit = SOPs piled on bad flow. Audit-first discipline. Per Decision **Op-7** scope.
- **Dependency:** Linear board access; deploy logs; support inbox; sync rules. Strategy CoS shadowing time.
- **Output:** Audit report MD; bounded remediation backlog (NOT a rewrite). Feeds Decision **Op-7**.

**`[OPS] OPERATIONS — Documentation Maintenance Rhythm`**
- **Objective:** Codify Linear ↔ Notion ↔ GitHub ↔ Drive ↔ MemPalace sync discipline — drift-detector cadence (per Decision **Op-8**), CLAUDE.md snapshot policy, design-system manifest sync, decision-log sync, framework-doc consolidation rules.
- **Why:** Tool drift compounds invisibly. Per memories `reference_automation`, `feedback_drive_git_incompatibility`, `feedback_design_system_sync`, `feedback_claude_md_safety` — discipline already exists in patches; rhythm consolidates.
- **Dependency:** project memories above; existing drift-detector; existing scheduled tasks (`reference_automation`).
- **Output:** Rhythm SOP MD; drift-detector emit destination wired into weekly ops review agenda. Feeds Decision **Op-8**.

### LATER

**`[DOC] OPERATIONS — Scale-Stage Operating System`**
- **Objective:** Concept-only sketch of what changes at headcount > 3, geography > 1, venue > 1 — cadence redesign, ownership-map regeneration, governance threshold triggers.
- **Why:** Phase 5+ input. Concept now reduces Phase 5 ramp time and pre-empts premature scale-stage commitments. *No commitments.*
- **Dependency:** Workstream Ownership Map; Internal Governance Framework concept; §5.4 phase map.
- **Output:** Concept MD; *no commitments* tag.

**`[DOC] OPERATIONS — Internal Governance Framework`**
- **Objective:** Concept-only sketch of board / advisor / contractor governance posture — decision rights, escalation authority, observer roles, advisory cadence.
- **Why:** Phase 4+ input. Bounds future raise-related governance discussion without committing. *No commitments* tag.
- **Dependency:** §15 raise posture (Phase 4); Decision Log System; Workstream Ownership Map.
- **Output:** Concept MD; *no commitments* tag.
