# 17 — Team and Operating Model

## Purpose

Define how CoinScopeAI should be staffed, operated, and coordinated in its current and next stages. The folder answers four questions in sequence:

1. **What roles matter most** at our actual stage (not at the org chart we'd want at scale).
2. **What sequence** roles should be added in, and what triggers each addition.
3. **Who decides what** — explicit decision rights, not implied ones.
4. **How the team runs the business operationally** — cadence, rhythm, sync structure.

This is **not** an aspirational org chart. CoinScopeAI is currently a founder-only operation in the 30-day validation phase (P0). The smallest viable team for the next 6–12 months is **founder + a small number of phase-triggered contractors**, with full-time hiring deferred until product readiness and revenue patterns justify it.

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, reading order, dependencies, open questions. |
| `team-design.md` | Current-stage team structure, core functions, founder-heavy vs distributed tradeoffs, near-term vs later-stage. |
| `role-priorities.md` | Highest-priority roles, what each owns, hiring sequence, what NOT to hire too early. |
| `decision-rights.md` | Who decides what across product, pricing, GTM, trust, support, risk, hiring, with escalation logic. |
| `operating-cadence.md` | Weekly + monthly + quarterly rhythm; KPI / risk / roadmap / docs review cadence; what must happen reliably vs optionally. |

## Why this folder matters

CoinScopeAI is a **trust-sensitive, gated trading product** built by one founder at present. That fact is not a problem to be solved by hiring — it is a constraint to be respected until the product earns the right to scale headcount. This folder exists to:

1. **Prevent premature hiring.** A wrong-timed hire at P1 burns 6–9 months of runway and creates coordination overhead that founder-mode would have avoided. The first hire is the highest-stakes hire.

2. **Make trust and risk ownership explicit, not assumed.** A vague "we all care about trust" is how trust posture quietly degrades. Trust Ops, Risk Ownership, and Public-Claims authority must each have a single named owner.

3. **Avoid org-chart vapor.** Public-company-style RACI matrices applied to a one-person company waste cycles. The right model here is "who decides X, escalation if disputed, log the decision" — that's it.

4. **Make the operating cadence sustainable.** Weekly and monthly reviews defined in `16-kpi-okr-system` need a team-and-cadence model that doesn't collapse under incident weeks.

## Dependencies on prior folders

| Upstream folder | What this folder reuses |
|---|---|
| `01-executive-summary` | Strategic posture (capital-preservation default, trust-first). |
| `02-company-overview` | Founder posture (UAE, sole prop, US-blocked). |
| `06-product-strategy` | Phase map P0 → P5; drives hiring triggers. |
| `08-go-to-market` | GTM ownership (founder-led content for the foreseeable future). |
| `12-onboarding-and-activation` | Activation ownership and handoffs. |
| `13-support-and-trust-ops` | Trust Ops role definition; incident management responsibilities. |
| `14-risk-compliance-and-safeguards` | Risk Ownership; PCC v2 gate authority; real-capital decision authority. |
| `15-financial-framework` | Hiring pace assumptions (#20–#22); cost discipline rules. |
| `16-kpi-okr-system` | KPI ownership transitions; weekly/monthly review participants. |

## Recommended reading order

1. `README.md` (this file).
2. `team-design.md` — establishes the smallest-viable-team posture for each phase.
3. `role-priorities.md` — translates posture into actual hiring sequence.
4. `decision-rights.md` — clarifies who decides what, especially around trust, risk, and pricing.
5. `operating-cadence.md` — turns it all into a weekly and monthly rhythm.

## Open questions (carried into `21-decision-log`)

- **DECISION NEEDED** — First contractor activation date: is it triggered by P2 phase entry, or by a specific support-load threshold being crossed before P2?
- **DECISION NEEDED** — Trust Ops contractor: hourly engagement vs project retainer.
- **DECISION NEEDED** — Engineering contractor scoping model: per-project SOWs vs monthly retainer for vendor integration work.
- **DECISION NEEDED** — Founder internal rate (placeholder $100/hr from `15-financial-framework`#19) — used here for opportunity-cost framing of role decisions.
- **REQUIRED INPUT** — Whether one trusted advisor will participate in monthly reviews from P1, and the engagement model (informal, paid-advisor, or equity).
- **REQUIRED INPUT** — Specific contractor candidates — none assumed, sourcing is itself a near-term task.
- **DECISION NEEDED** — Geographic constraints on hiring (UAE residency, MENA timezones, EN proficiency). Locks search radius for first hire.
- **DECISION NEEDED** — Equity policy for first full-time hire (P3+). Even placeholder posture is better than no posture.

## What this folder is NOT

- Not an org chart for the company we want to be in 2 years.
- Not an HR policy manual.
- Not a job-description library (those live in hiring artifacts when each role activates).
- Not a comp framework (deferred to first FT hire decision).

It is the **smallest team-and-operating contract** that makes CoinScopeAI runnable at its actual stage without collapsing under incident weeks or losing trust posture to coordination drift.

---

*Folder owner: Founder. Reviewed at every phase transition (P0→P1, etc.). Last reviewed: 2026-05-08.*
