# 18 — Roadmap

## Purpose

Convert CoinScopeAI's strategy into a **staged, dependency-aware execution roadmap**. The folder answers three operational questions:

1. **What should happen first?** — the 30-60-90 day window starting from today.
2. **What must happen before launch or scaling?** — milestone definitions and gate criteria.
3. **How do business, product, trust, and ops milestones depend on one another?** — explicit dependency mapping so no workstream silently outruns another.

The roadmap is **honest, not aspirational**. CoinScopeAI is in P0 (validation phase, May 2026, cohort cap 40), Binance Testnet only, with real-capital trading gated by PCC v2 §8 Capital Cap. Roadmap items that pretend any of those constraints don't exist are misleading and excluded by design.

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, reading order, dependencies, open questions. |
| `30-60-90-plan.md` | 30/60/90-day priorities from today (2026-05-08), categorized as discovery vs execution vs hardening, with what NOT to force into the window. |
| `milestone-framework.md` | Strategic milestones, launch / trust / monetization / ops readiness criteria, gate logic, milestone-inflation antipatterns. |
| `dependency-map.md` | Cross-workstream dependencies, decision unlock chains, sequencing bottlenecks, operator-grade summary. |

## Why this folder matters

The single most common way trust-sensitive trading products fail is by **collapsing the dependency graph** — pulling launch forward, monetization forward, or scale forward before the trust and safeguard work that should precede them is complete. That collapse is rarely intentional. It's usually the cumulative effect of small "we can do this in parallel" decisions that, in aggregate, force the engine to be sold before it's ready.

This folder exists to make that collapse impossible to do silently. Every time a milestone is pulled forward, the dependency map names what must move with it. That makes the trade-off visible, not invisible.

## Dependencies on prior folders

| Upstream folder | What this folder reuses |
|---|---|
| `01-executive-summary` | Strategic posture (capital-preservation default). |
| `02-company-overview` | UAE / sole-prop / US-blocked operating context. |
| `06-product-strategy` | Phase map P0 → P5; this roadmap is the operational version. |
| `07-packaging-and-pricing` | Track B tier matrix; SKU activation timing. |
| `08-go-to-market` | Channel selection; founder-led content posture. |
| `12-onboarding-and-activation` | Activation flow definitions; D7/D30 retention targets. |
| `13-support-and-trust-ops` | Runbook coverage as a hard prerequisite for monetization. |
| `14-risk-compliance-and-safeguards` | PCC v2 G1–G4 + §8 Capital Cap as the canonical gate logic. |
| `15-financial-framework` | Hiring pace assumptions; vendor cost discipline; revenue authorization timing. |
| `16-kpi-okr-system` | NSM (VCE → TRAS at P1); weekly/monthly review cadence. |
| `17-team-and-operating-model` | Role activation triggers; decision rights; operating cadence. |

## Recommended reading order

1. `README.md` (this file).
2. `30-60-90-plan.md` — what's next, organized by horizon.
3. `milestone-framework.md` — what counts as "done" at each major step.
4. `dependency-map.md` — what cannot proceed before what.

If you only have 10 minutes: read the **30-day section** in `30-60-90-plan.md` plus the **gate criteria** section in `milestone-framework.md`.

## Open questions (carried into `21-decision-log`)

- **DECISION NEEDED** — P1 narrow-ship date target. Earliest defensible: 30 days after PCC v2 G3 stabilization. Today's date is 2026-05-08; G3 status is REQUIRED INPUT.
- **DECISION NEEDED** — P2 vendor expansion sequencing: Bybit first, additional data feeds first, or in parallel.
- **DECISION NEEDED** — P5 Desk Full v2 launch criteria — is the canonical Mar–May 2027 window contingent on a specific revenue threshold from Trader/Desk Preview, or a product-readiness threshold only?
- **REQUIRED INPUT** — Current PCC v2 gate state (G1, G2, G3, G4) to anchor the 30-60-90 plan to reality.
- **REQUIRED INPUT** — Validation cohort progress: how many of the cohort cap of 40 have completed the 30-day window with no incident-driven termination.
- **DECISION NEEDED** — Whether the optional advisor (`17-team-and-operating-model`) is activated within this 90-day window.
- **DECISION NEEDED** — Real-capital authorization stays at default NO; review checkpoints are at every monthly exec review. Confirm this default is communicated to any external party who might apply pressure.

## What this folder is NOT

- Not a Gantt chart with confidence intervals it can't honor.
- Not a launch announcement plan.
- Not a fundraising timeline.
- Not a marketing calendar.

It is the **execution contract** that makes phase progression honest. Every milestone in this folder either moves CoinScopeAI forward through PCC v2 / §8 Capital Cap, or directly serves a workstream that supports that progression.

---

*Folder owner: Founder. Reviewed at every weekly review (slippage), monthly exec review (full), and phase transition (re-baseline). Last reviewed: 2026-05-08.*
