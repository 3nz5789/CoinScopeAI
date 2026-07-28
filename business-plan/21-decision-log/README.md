# 21 — Decision Log

## Purpose

Serve as the **decision and ambiguity control center** for CoinScopeAI. The folder makes leadership decisions visible, tracks open questions across the business plan, and prevents the silent drift that kills trust-sensitive products.

Two registers live here:

1. **Leadership Decision Register** — the decisions that have been made, deferred, or are in flight. Each row names options, recommendation, owner, deadline, downstream impact, and status.
2. **Open Questions Register** — the questions that have not yet been turned into decisions, ranked by what they actually unblock.

Together, they answer the question that any operator should be able to ask in 60 seconds: **what is undecided, who owns it, what does it block, and when must it be resolved?**

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, reading order, dependencies, governance, open questions about the system itself. |
| `leadership-decision-register.md` | Structured table of leadership decisions, decided + deferred + in-flight, with options, recommendations, downstream impact, and status. |
| `open-questions-register.md` | Structured table of open questions across product maturity, pricing validation, GTM proof, trust readiness, compliance, support load, cost structure, hiring sequence, and roadmap gating. |

## Why this folder matters

Three failure modes that this folder exists to prevent:

1. **Decision laundering.** A decision that quietly changed between weekly reviews — without a log entry — is itself a trust-debt event. CoinScopeAI cannot afford pricing, refund-policy, public-claims, or risk-posture decisions to drift silently.

2. **Question stagnation.** Open questions that don't have a clear "who answers" or "what evidence is needed" tend to remain open indefinitely. Stagnant questions accumulate as hidden risk.

3. **Cross-folder drift.** Pricing in `07-packaging-and-pricing` says one thing; the financial framework in `15-financial-framework` assumes another; the roadmap in `18-roadmap` implies a third. Without one canonical decision-log, drift is invisible.

This folder is the canonical home. If a decision isn't here, it isn't made — it was guessed.

## Dependencies on prior folders

| Upstream folder | What this folder pulls from |
|---|---|
| `01-executive-summary` | Strategic posture (capital-preservation default). |
| `02-company-overview` | Operating posture (UAE, sole prop, US-blocked). |
| `04-icp-and-segmentation` | Primary ICP locked decisions (Omar / Karim / Layla). |
| `05-positioning` | Category and positioning lock. |
| `07-packaging-and-pricing` | Tier matrix (Track B canonical). |
| `08-go-to-market` | Channel selection and content posture. |
| `12-onboarding-and-activation` | Activation definition decision. |
| `13-support-and-trust-ops` | Refund/credit playbook + transparency artifact decisions. |
| `14-risk-compliance-and-safeguards` | PCC v2 gate authority + §8 Capital Cap state + real-capital authorization. |
| `15-financial-framework` | 8 explicit DECISION NEEDED items in §15 README + assumption-table risk grades. |
| `16-kpi-okr-system` | NSM lock + activation-definition lock + cadence-tooling decisions. |
| `17-team-and-operating-model` | 8 DECISION NEEDED items in §17 README + decision-rights boundaries. |
| `18-roadmap` | 7 DECISION NEEDED items in §18 README + gate-criteria decisions. |

Every "DECISION NEEDED" or "REQUIRED INPUT" tag flagged in any prior folder must have a row in `leadership-decision-register.md` or `open-questions-register.md`. If it doesn't appear here, the propagation step was missed.

## Recommended reading order

1. `README.md` (this file) — frame.
2. `leadership-decision-register.md` — what decisions exist and where they stand.
3. `open-questions-register.md` — what's still upstream of decisions.

If you only have 5 minutes: read the **status filter** of each register for `OPEN — High urgency`. That is the active risk surface.

## How the registers are governed

- **Source of truth.** This folder is canonical. If another folder references a decision, it must link back to a row here.
- **Update cadence.** Weekly review surfaces new decisions and updates statuses. Monthly exec review reviews the full register. Phase transitions force a register audit.
- **Status taxonomy.** Limited set: `OPEN` / `IN REVIEW` / `DECIDED` / `DEFERRED` / `SUPERSEDED`. No bespoke statuses.
- **Decision rows are append-only by intent.** A `DECIDED` row that is later revised becomes `SUPERSEDED` — a new row is added; the original stays for history.
- **Owners are single-threaded.** Per `decision-rights.md`, almost every row is owned by Founder. Co-ownership is documented for visibility, but accountability is single.
- **Deadlines are honest.** A row with `OPEN` status and no deadline is a defect. Either set a deadline or move to `DEFERRED` with a re-review trigger.

## Status placeholder definitions

| Status | Meaning |
|---|---|
| **OPEN** | Decision is needed; recommendation may exist; not yet decided |
| **IN REVIEW** | Decision being actively evaluated this week or this month |
| **DECIDED** | Resolved with documented decision; downstream propagation either complete or named |
| **DEFERRED** | Deliberately not decided yet; has a re-review trigger or date |
| **SUPERSEDED** | Replaced by a newer row; retained for history |

A row should never sit at `OPEN` indefinitely. If it has, it should move to `DEFERRED` with an explicit trigger.

## Open questions about the decision system itself

- **DECISION NEEDED** — Where does this register physically live alongside the markdown? Confirmed answer (working assumption): in this folder, with optional mirror to Notion via the configured workspace integration. **Need to confirm Notion mirror is set up.**
- **DECISION NEEDED** — Per-decision page vs single-table-row format. Single-table-row is faster to scan; per-page allows richer documentation. Recommendation: table here, with optional linked detail pages for high-impact decisions only.
- **DECISION NEEDED** — Public-facing decision-log subset. Some decisions (e.g., refund playbook) might be valuable to publish externally as a trust signal. Recommendation: defer until P2 with monthly re-review.
- **REQUIRED INPUT** — Confirm whether weekly reviews automatically surface new decisions, or whether the founder logs them. Working assumption: founder logs in real time; weekly review is a sweep, not a discovery exercise.
- **DECISION NEEDED** — Threshold for what qualifies as a "loggable decision." Working rule: if the decision affects pricing, claims, refunds, hiring, vendor concentration, risk thresholds, or roadmap dates, it is loggable. Anything else is operational and lives in tasks/notes.

## What this folder is NOT

- Not a brainstorming dump.
- Not an idea board.
- Not a risk register (those live in `14-risk-compliance-and-safeguards`).
- Not a task list (`99-task-backlog`).
- Not a meeting-notes archive.

It is the **canonical, low-overhead, append-only record** of decisions and the questions upstream of decisions. Every row earns its presence by either resolving ambiguity or naming the cost of leaving it unresolved.

---

*Folder owner: Founder. Reviewed weekly (status sweep), monthly (full register), and at every phase transition. Last reviewed: 2026-05-08.*
