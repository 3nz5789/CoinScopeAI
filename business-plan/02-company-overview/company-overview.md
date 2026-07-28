# Company Overview

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## 1. Company description (plain)

CoinScopeAI is a **UAE-built, validation-phase software company** that ships AI-driven capital-preservation infrastructure for disciplined crypto-perpetuals traders and small portfolio managers. The product is a tiered SaaS subscription that wraps the user's existing exchange account with regime classification, configurable risk gates, and a journaling and analytics surface. Capital remains in the user's exchange account.

The company is operated as a **sole-proprietorship** by a UAE-resident founder (Mohammed). Engineering is solo-founder-led with planned **P4 contractor support** at the highest-risk window (~3 months around the v2 build). There is no full-time team beyond the founder, and there is no priced equity raise before validation passes.

Today, the company is best described as a **product in active validation**, not a product at scale.

---

## 2. Vision

> **Capital preservation, by default — for traders disciplined enough to demand it, in tools honest enough to enforce it.**

This is **Vision A**, locked 2026-04-22 (`project_vision_mission.md`). It is intentionally non-grandiose: it commits the company to a specific orientation (capital preservation first, alpha second) rather than to a market-cap or category-leadership outcome.

What this vision rejects, deliberately:

- "Become the largest crypto trading platform"
- "Become the dominant signal provider"
- "Build the AI hedge fund of the future"

The vision does not preclude scale; it constrains the *shape* of scale.

---

## 3. Mission

> **Build the operational discipline software that surviving disciplined traders already wish existed.**

This is **Mission 1**, locked 2026-04-22 (`project_vision_mission.md`). Operational, not aspirational. Three commitments are embedded:

1. **Operational discipline software** — the product is process software, not signal software.
2. **Surviving disciplined traders** — we serve traders who have already learned, often the hard way, that discipline is what survives. We do not market to first-time traders or to traders who treat the product as a way to skip discipline.
3. **Already wish existed** — we are filling a known gap, not inventing a category. The product is recognizable on first use.

---

## 4. Intended users

Three locked personas (internal names; never used externally):

| ID | Name | Audience | Buying motivation | Default tier |
|---|---|---|---|---|
| **P1** | Omar — Self-Taught Methodist | Solo retail trader who has built his own discipline framework, often after a meaningful loss | Tools that *enforce* his framework rather than replace it | Trader $79/mo |
| **P2** | Karim — Engineer Trader | Quant-curious software engineer trading perps part-time | Programmable risk + clean APIs over signal feeds | Trader $79 → Desk Preview $399 over time |
| **P3** | Layla — Solo PM | Solo portfolio manager running $200k–$1M aggregate book, formal or informal | Institutional-grade risk surface without institutional overhead | Desk Preview $399 → Desk Full v2 $1,199 + per-seat |

**Deferred personas (post-P2 at earliest):** funds >$5M AUM, prop desks, signal resellers, US-domiciled traders, copy-trading audiences, beginner traders, day-trading-as-content audiences.

**REQUIRED INPUT:** §3.7 interview validation in flight; persona reconfirmation due before P1 mid-cohort review.

---

## 5. Product scope summary

In scope, today, on testnet:

- **Engine** — multi-pair scanner across USDT-perpetual venues (Binance USDT-M; Bybit deferred to P2)
- **Regime classifier** (v3 ML) — Trending / Mean-Reverting / Volatile / Quiet, with confidence
- **Risk gate** — drawdown, daily-loss, max leverage, position heat, max open positions, all configurable, all gating *before* trade arming
- **Position sizer** — per-account thresholds against the gate
- **Performance + journal** — cohort-grade observation surface
- **Surfaces** — web dashboard at coinscope.ai (React + TypeScript + Tailwind) and Telegram (@ScoopyAI_bot)
- **Auth, onboarding, billing** — Stripe-ready; tier matrix wired

In scope, design-level only, until earlier gates pass:

- Bybit integration (P2)
- Desk Preview multi-account view, advanced gates, read API (P1 close target)
- Desk Full v2 (P5 window: Mar–May 2027)
- Per-seat scaling at Desk Full

Explicitly **out of scope** at every horizon currently planned:

- Capital custody (no pooled capital, no managed accounts)
- Autonomous execution without user authorization
- Alpha generation as a product
- Signals-as-a-service
- Copy-trading / leader-follower economics
- Fund-formation tooling
- Native mobile app (web + Telegram cover the cohort)
- US-licensed retail flow (US is blocked at signup until licensure path is decided)

---

## 6. Current strategic posture

Five-line posture statement, suitable as the founder's verbal anchor:

1. **Validation-phase, not production-ready.** PCC v2 G1–G4 + §8 Capital Cap criteria gate that claim.
2. **Testnet only, no real capital.** A code-level hard gate enforces it; a policy-level claim alone is insufficient.
3. **Bootstrap-efficient, not bootstrap-forever.** Pre-validation: warm conversations only. Post-validation: structured raise opens with cohort data.
4. **Founder-led distribution; no paid acquisition before Trader CAC validates.** M5+ trigger only.
5. **UAE-built, MENA-rooted, global EN.** US blocked at signup; not a target market until licensure path is decided.

This posture is the operating contract. Anything that contradicts it should be flagged before action.

---

## 7. Business-model direction

Tiered SaaS, monthly + annual, on top of the user's exchange account. Monetization summary lives in `01-executive-summary/business-model-summary.md`; the directional view here is:

- **Primary line:** subscription seat revenue across Free / Trader / Desk Preview / Desk Full
- **Secondary line:** per-seat scaling at Desk Full v2
- **Tertiary line:** annual prepay discount (rate **DECISION NEEDED**)
- **Custody-free** by structural choice — capital and execution stay with the user
- **Anti-overclaim** by structural choice — pricing and packaging do not promise alpha or guaranteed returns

What we do not do as a business model: performance fees, custody fees, signal subscription, copy-trading take rate, alpha resale, marketplace listing fees.

---

## 8. Trust and risk orientation

Trust is the moat. The orientation is enforced at three layers:

| Layer | What it looks like | Why it exists |
|---|---|---|
| **Product** | Risk controls (drawdown, daily loss, leverage, heat, position count) are first-class UI; rejected trades show the explicit gate that fired; regime + confidence + gate-result on every signal | Disciplined traders calibrate quickly to whether tools respect their framework — observable in 30 seconds |
| **Brand and voice** | Anti-overclaim language; no "production-ready" claim until §8 passes; product-tier voice (terse, declarative, data-led) on all surfaces; never marketing-tier voice inside the product | One viral overclaim is enough to undo months of disciplined posture |
| **Operations** | Testnet-only enforcement at code level; PCC v2 gates documented; vendor failure-mode mapping; runbooks and incident playbook before P2 | Trust is judged on how we behave when things go wrong, not when things go well |

The risk numbers — **10% max drawdown · 5% daily loss · 10x max leverage · 5 max open positions · 80% position heat** — are **locked** (PCC v2 §8, 2026-05-01). They are not marketing copy. They are first-class numbers, surfaced when composing a position. The disclaimer that always pairs them: *"Testnet only. 30-day validation phase. No real capital."*

---

## 9. How CoinScopeAI should describe itself today

A short list of approved framings, ordered by audience. Each is consistent with anti-overclaim discipline and locked v1 messaging.

### One-line — primary
> AI-driven capital-preservation infrastructure that enforces the discipline you've already built.

### One-line — formal / B2B
> Your trusted partner in cryptocurrency trading.

### One-paragraph — investor / advisor
> CoinScopeAI is a UAE-built validation-phase software company building AI-driven capital-preservation infrastructure for disciplined crypto-perpetuals traders and small portfolio managers. The engine evaluates signals on USDT-perp venues, classifies market regime in real time, and runs configurable risk gates before any trade arms. Capital stays in the user's exchange account. We're operating under documented anti-overclaim discipline and gated against real-capital deployment until validation passes.

### One-paragraph — recruiting / contractor
> CoinScopeAI is a small, UAE-built software company in active validation. We ship AI-driven risk infrastructure for disciplined traders, with a heavy emphasis on operational discipline, anti-overclaim writing, and testnet-only safety. The engine, regime classifier, and risk gates are live on Binance Testnet; we open a 40-user soft launch on 2026-06-01 with a structured raise after validation passes.

### What we deliberately do not say (today)
- "Production-ready" — until PCC v2 §8 passes.
- "Live trading" — without "testnet" qualifier.
- "Fund / hedge fund" — we are not a fund.
- "Investment advice" — counsel-confirmed posture is "tools, not advice."
- "Guaranteed" — never. About anything.
- "Institutional" — only inside the locked phrase "institutional-grade", and only where supported by documented criteria.

---

## 10. Cross-references

- Strategic frame and priorities: `01-executive-summary/`
- Decision log (vision, mission, persona, tier-matrix locks): `business-plan/_decisions/decision-log.md`
- PCC v2 (gates + §8 Capital Cap): `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Locked v1 §1 narrative: `business-plan/01-executive-summary.md`
- Locked v1 §3 ICP: `business-plan/03-icp-segmentation.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
