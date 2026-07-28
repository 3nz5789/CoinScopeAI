# 16 — KPI / OKR System

## Purpose

Define how CoinScopeAI measures success and operating health, balancing eight dimensions in roughly equal weight:

1. Growth
2. Activation
3. Retention
4. Trust
5. Risk
6. Support quality
7. Operational readiness
8. Financial discipline

The system is **stage-appropriate**: small, opinionated, low-overhead. It is not a public-company reporting framework. It is the smallest set of metrics, reviews, and triggers that lets a founder-led, trust-sensitive trading product avoid the two failure modes that kill products like ours:

- **Optimizing only for growth** while trust posture quietly degrades.
- **Vanity dashboards** that look healthy until a single incident exposes the fragility behind them.

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, reading order, dependencies, open questions. |
| `north-star-metric.md` | NSM candidates evaluated, recommended NSM, why it fits CoinScopeAI's current stage, how to interpret it, what NOT to use too early. |
| `kpi-map.md` | KPIs by workstream — growth, activation, retention, trust, support, risk, financial, ops, product-readiness — with leading/lagging tags and ownership. |
| `weekly-review-template.md` | Structure for the weekly business review: sections, required data, decision triggers, participants. |
| `monthly-exec-review-template.md` | Structure for monthly exec review: business health, financial review, roadmap, trust/risk, decision-log refresh, monthly-change rules. |

## Why this folder matters

CoinScopeAI cannot be measured like a generic SaaS. Three reasons:

1. **The Risk Gate sometimes prevents revenue-generating behavior.** A KPI system that rewards "more signals delivered" or "more positions opened" is structurally hostile to capital preservation. Our metrics must reward the gate doing its job, not punish it.

2. **A single trust event can erase weeks of growth.** Lagging financial metrics (MRR, churn) can look great while leading trust metrics (incident count, gate-decline confusion, kill-switch trips) are deteriorating. We need the leading indicators visible at the same cadence as the lagging ones.

3. **We are in the 30-day validation phase (P0).** Most "real" KPIs do not yet have data. The system must distinguish between metrics that are **load-bearing now**, **measurable but informational**, and **deferred to later phase**.

Without this discipline, the founder ends up running the business by gut feel and a single dashboard, neither of which catches a slow-rolling trust degradation in time.

## Dependencies on prior folders

| Upstream folder | What this folder reuses |
|---|---|
| `01-executive-summary` | Strategic framing — capital-preservation default, trust-first. |
| `02-company-overview` | Operating posture (UAE, US-blocked, sole prop). |
| `03-market-thesis` | TAM logic that bounds growth ambition. |
| `04-icp-and-segmentation` | Personas (Omar / Karim / Layla) — drive activation/retention metric definitions. |
| `05-positioning` | "Institutional-grade for individuals + funds" — anchors quality-of-revenue tracking. |
| `06-product-strategy` | Phase map (P0 → P5) — gates which KPIs are active when. |
| `07-packaging-and-pricing` | Tier matrix — drives MRR/ARPU breakdowns. |
| `08-go-to-market` | Acquisition channels — drives funnel-stage KPIs. |
| `12-onboarding-and-activation` | Activation definitions feed the leading retention indicators. |
| `13-support-and-trust-ops` | Support load + incident metrics directly map to the trust/support KPIs. |
| `14-risk-compliance-and-safeguards` | Kill-switch trips, gate-decline rate, PCC v2 gate progress are first-class KPIs, not side metrics. |
| `15-financial-framework` | The 30-row assumption table is the source of every financial KPI band. |

## Recommended reading order

1. `README.md` (this file).
2. `north-star-metric.md` — establishes the single most important number and why it isn't MRR.
3. `kpi-map.md` — the actual scorecard, organized so trust/risk are co-equal with growth.
4. `weekly-review-template.md` — operating cadence; what changes the week.
5. `monthly-exec-review-template.md` — strategic cadence; what changes the quarter.

## Open questions (carried into `21-decision-log`)

- **DECISION NEEDED** — Confirm the recommended North-Star Metric (Trust-Retained Active Subscribers, TRAS) or pick an alternative from `north-star-metric.md`.
- **DECISION NEEDED** — Activation definition lock. `12-onboarding-and-activation` proposes a multi-step activation; the KPI system needs the exact stop-conditions locked.
- **DECISION NEEDED** — Weekly review cadence: founder solo log vs founder + 1 advisor. Both are viable; the choice affects how the weekly template is filled in.
- **REQUIRED INPUT** — Tooling: do we instrument these KPIs in a dashboard now, or maintain a spreadsheet through P1? (Recommendation in `weekly-review-template.md` §6.)
- **REQUIRED INPUT** — Incident severity scale lock from `13-support-and-trust-ops` so KPI rows reference one canonical scale, not two.
- **DECISION NEEDED** — Whether to publish *any* KPIs externally during P0/P1 (e.g. validation-cohort transparency reports). Trust signal vs over-disclosure tradeoff.

## What this folder is NOT

- Not a board reporting pack.
- Not a complete OKR catalog. (OKRs at P0 are largely founder objectives; full team OKRs come at P3+ and live in `17-team-and-operating-model`.)
- Not a vanity dashboard.
- Not a complete-coverage scorecard. We deliberately defer metrics that cannot be honestly populated yet.

It is the **operating discipline** that surfaces both growth and trust deterioration at the same cadence, so neither is invisible.

---

*Folder owner: Founder. Reviewed at every phase transition (P0→P1, etc.). Last reviewed: 2026-05-08.*
