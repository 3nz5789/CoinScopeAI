# 15 — Financial Framework

## Purpose

Define the **financial logic** of CoinScopeAI before any full financial model is built. This folder is **assumption-driven, not forecast-driven**. It tells leadership:

- how the business is expected to make money,
- what it will cost to operate at each phase,
- which assumptions are load-bearing,
- and what inputs to track before committing to a 3-statement model or fundraising spreadsheet.

We are deliberately **not** publishing pro-forma revenue, ARR, or margin figures. CoinScopeAI is in the **30-day validation phase (P0, May 2026)** with a cohort cap of 40, on Binance Testnet only. Real-capital trading is gated by Production Candidate Criteria v2 (G1–G4 + §8 Capital Cap). Any financial output that pretends to know more than that is misleading.

## File list

| File | What it covers |
|---|---|
| `README.md` | This file — purpose, reading order, dependencies, open questions. |
| `revenue-model.md` | How CoinScopeAI monetizes: subscription logic, mix, retention quality, what to defer. |
| `cost-structure.md` | Cost categories, fixed vs variable, vendor exposure, infra and support cost drivers. |
| `financial-assumptions.md` | Explicit assumption table — pricing, conversion, churn, support, vendor, hiring, readiness — with risk grading. |
| `scenario-model-inputs.md` | Best/base/worst input categories, triggers for scenario revision, what NOT to pretend to know yet. |

## Why this folder matters

CoinScopeAI is a **trust-sensitive trading product**. Monetization maturity will lag product ambition because:

1. The Risk Gate, regime classifier, and exchange integrations need 30+ days of validated behavior before any P1 narrow-ship is defensible.
2. The Desk Full v2 tier (the highest-revenue SKU at $1,199/mo + per-seat) is **not launchable until P5 (Mar–May 2027)** per the canonical phase map.
3. Real-capital trading is gated; we cannot price like a P&L SaaS while we are still validating capital preservation behavior.

Premature financial fabrication ("we'll do $1.2M ARR in 12 months") would directly contradict §14 Risk/Compliance and §8 Capital Cap. So this folder establishes a **disciplined, transparent assumption layer** instead.

## Dependencies on prior folders

| Upstream folder | What this folder reuses |
|---|---|
| `01-executive-summary` | Strategic framing — why we're trust-first, capital-preservation default. |
| `02-company-overview` | Operating posture (UAE founder, sole prop, US blocked at signup). |
| `03-market-thesis` | TAM/SAM commentary feeding revenue ceiling logic. |
| `04-icp-and-segmentation` | Personas P1 Omar / P2 Karim / P3 Layla — drives ARPU and conversion assumptions. |
| `05-positioning` | "Institutional-grade for individuals + funds" — anchors price defensibility. |
| `06-product-strategy` | Phase map (P0 → P5) — drives revenue-readiness timing. |
| `07-packaging-and-pricing` | Track B tier matrix — direct input to revenue model. |
| `08-go-to-market` | Acquisition channels and CAC structure. |
| `12-onboarding-and-activation` | Activation friction → conversion assumption. |
| `13-support-and-trust-ops` | Support load → variable cost. |
| `14-risk-compliance-and-safeguards` | Capital cap / kill-switch logic — caps how aggressive the revenue plan can be. |

## Recommended reading order

1. `README.md` (this file) — frame the discipline.
2. `financial-assumptions.md` — the load-bearing layer; everything else depends on it.
3. `revenue-model.md` — read against `07-packaging-and-pricing` and `04-icp-and-segmentation`.
4. `cost-structure.md` — read against `13-support-and-trust-ops` and `14-risk-compliance-and-safeguards`.
5. `scenario-model-inputs.md` — turns the assumptions into watch-items for leadership.

Do not skip to scenarios before reading the assumptions; out-of-context scenario numbers are how trust-sensitive companies get their financial framing wrong.

## Open questions (carried into `21-decision-log`)

- **DECISION NEEDED** — Do we accept annual prepay at P1 narrow-ship, or only monthly until G4 is met? Annual prepay improves cash but creates refund exposure if the engine is rolled back.
- **DECISION NEEDED** — Per-seat pricing for Desk Full v2 ($149 vs $249) — when do we lock the choice? Currently both are canonical placeholders.
- **REQUIRED INPUT** — Vendor cost commitments at P2 vendor expansion (Bybit, additional data feeds): we need 3 written quotes per vendor before assumptions can be tightened.
- **REQUIRED INPUT** — Stripe/processor fee modeling for MENA + global EN — actual blended take-rate including FX.
- **DECISION NEEDED** — Founder-only stage cost recognition: do we book founder time at zero, market rate, or a discounted internal rate? This drives cost-structure honesty.
- **ASSUMPTION** — Trader $79/mo is the default conversion target from Free; this needs cohort validation before being treated as load-bearing.

## What this folder is NOT

- Not a forecast.
- Not a fundraising deck spreadsheet.
- Not a unit-economics claim.
- Not a margin promise.

It is the **assumption contract** that any future financial model must trace back to. If a number shows up in a future model and isn't grounded here, the model is wrong.

---

*Folder owner: Founder / Strategy Chief of Staff. Last reviewed: 2026-05-08.*
