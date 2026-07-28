# 99 — Task Backlog

## Purpose

Convert the full CoinScopeAI business plan into an **execution-ready Claude Co-Work backlog**. The folder provides a master backlog grouped by workstream and four phased backlogs that sequence work in dependency-aware order. Tasks here are operational artifacts — not narrative — and they map cleanly to specific upstream folders, decisions, or open questions.

The backlog is **opinionated, lean, and traceable**. Every task either:

- closes a `DECISION NEEDED` from `21-decision-log`,
- gathers evidence for an open question,
- delivers a hard-dependency item from `18-roadmap`, or
- hardens a workstream against a known failure mode.

If a task doesn't do one of those four things, it doesn't belong here.

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, naming/sequencing rules, governance, open questions. |
| `master-backlog.md` | Full backlog by workstream, with NOW / NEXT / LATER grouping. |
| `phase-1-backlog.md` | Strategic foundation: market, ICP, positioning, product, trust, risk. |
| `phase-2-backlog.md` | Packaging, pricing, GTM, onboarding, support, safeguards. |
| `phase-3-backlog.md` | Finance, KPIs, team, roadmap, decision discipline. |
| `phase-4-backlog.md` | Later-stage: sales, partnerships, fundraising, scenarios, scale readiness. |

## Why this folder matters

Three failure modes this folder exists to prevent:

1. **Backlog bloat.** A 300-task backlog is unreadable. The discipline here is to keep the master backlog tight (~50–60 active tasks), with phase backlogs as the operational subset for the current quarter.

2. **Generic filler.** Tasks like "improve onboarding" or "do marketing" are not tasks; they are categories. Every entry below is sized to a clear deliverable that one person can close in days, not weeks.

3. **Lost dependencies.** A task that ships before its dependency is complete is wasted work. The sequencing in the phase backlogs encodes the dependency graph from `18-roadmap/dependency-map.md`.

## How backlog files should be used

| Use case | File to open |
|---|---|
| "What should I work on this week?" | `master-backlog.md` → NOW section |
| "What's the next 90 days?" | `master-backlog.md` → NEXT section + relevant phase file |
| "What's blocking what?" | Phase file (each task names its dependency) |
| "Where does this map to the plan?" | Each task includes a cross-ref to upstream folder |
| Pull into Claude Co-Work as actionable tasks | Any phase file — names follow `[TYPE] [AREA] — Action / Deliverable` exactly |

## Naming rules (mandatory)

Format: **`[TYPE] [AREA] — Action / Deliverable`**

**Allowed TYPE values:** `[RESEARCH]`, `[BUILD]`, `[DOC]`, `[OPS]`, `[RISK]`, `[GTM]`, `[FINANCE]`, `[LEGAL]`, `[PARTNERSHIPS]`, `[METRICS]`, `[QA]`.

**Allowed AREA values:** MARKET, ICP, POSITIONING, BRAND, PRODUCT, PACKAGING, PRICING, GTM, SALES, PARTNERSHIPS, ONBOARDING, SUPPORT, TRUST, RISK, COMPLIANCE, FINANCE, METRICS, OPERATIONS, TEAM, FUNDRAISING, ROADMAP, SCENARIOS.

**Distinctness rule:** task names must be distinct in the first 4–6 words so they remain readable when truncated in the Co-Work sidebar.

**Every task includes:**

- **Objective** — what is being delivered.
- **Why it matters** — what it unblocks or hardens.
- **Dependency** — what must be true or complete before it starts.
- **Expected output** — the artifact, decision, or measurement produced.

## Sequencing rules

1. **Dependencies are non-negotiable.** A task with an open dependency moves to NEXT or LATER, never NOW.
2. **Forward-only phase movement.** Tasks don't slide between phases without an explicit decision-log entry.
3. **NOW = this 30 days.** NEXT = 30–90 days. LATER = beyond 90 days.
4. **Hardening tasks precede expansion tasks.** Replay corpus before vendor expansion. Runbook coverage before Trust Ops contractor.
5. **Decision-closing tasks precede execution tasks that depend on them.** A `[DOC] PRICING — Lock annual prepay policy` precedes `[BUILD] PRICING — Configure annual prepay in Stripe`.

## Open questions (about the backlog itself)

- **DECISION NEEDED** — Is this backlog mirrored to a tool (Notion / Linear / Asana), or does it live in markdown only? Recommendation: markdown canonical, mirror to one tool only.
- **DECISION NEEDED** — Cadence for backlog grooming. Recommendation: weekly review surfaces new tasks, monthly exec review re-priorities, phase transition forces re-baseline.
- **DECISION NEEDED** — Who other than founder can mark a task complete? Recommendation: founder only through P3, with contractor "ready for review" status as the alternative.
- **REQUIRED INPUT** — Does Co-Work pull this backlog automatically, or does the founder copy tasks individually? Affects how granular task descriptions need to be.
- **DECISION NEEDED** — Whether to publish a sanitized version of NOW tasks externally as a transparency artifact (cross-ref `13-support-and-trust-ops`).

## What this folder is NOT

- Not a project management replacement for proper task tracking when the team scales.
- Not a wishlist.
- Not a sprint plan with story points.
- Not a roadmap (the roadmap is in `18-roadmap`).
- Not a decision register (decisions are in `21-decision-log`).

It is the **execution-grade list** of work to be done, sequenced honestly, with every entry traceable to a higher-order document.

---

*Folder owner: Founder. Reviewed weekly (status sweep), monthly (re-prioritization), at every phase transition (re-baseline). Last reviewed: 2026-05-08.*
