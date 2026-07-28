# Business Model Summary

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file summarizes how CoinScopeAI creates, captures, and delivers value. It is operator-facing — built for execution clarity, vendor decisions, and fundraising honesty — not for marketing.

---

## 1. Business model overview

CoinScopeAI sells **AI-driven capital-preservation infrastructure** to disciplined crypto-perpetuals traders and small portfolio managers via a tiered SaaS subscription. The product runs on top of the user's existing exchange account — capital and execution stay with the user; CoinScopeAI provides the analytical engine, regime classification, risk gates, and surfaces (dashboard + Telegram) that wrap them.

| Element | CoinScopeAI's choice | Alternative considered | Why our choice |
|---|---|---|---|
| Revenue model | Tiered monthly + annual subscription | Performance-based fees, signal subscription, fund formation | Predictable, custody-free, regulatory-aligned, anti-overclaim |
| Custody | None — capital stays in user's exchange account | Pooled / managed account | Removes regulatory burden + trust friction; aligns with disciplined-trader values |
| Execution | User-authorized only | Full autonomous | Anti-overclaim discipline + regulatory posture |
| Distribution | Founder-led + content-driven; no paid acquisition before CAC validation | Paid-first growth | Capital-efficient + trust-building during validation |
| Geography | UAE/MENA + global EN; US blocked at signup | Global from day one | Regulatory clarity + structural geographic credibility |

---

## 2. How CoinScopeAI monetizes

Three monetization levers, in order of weight:

1. **Subscription seat revenue** — primary. Monthly or annual subscriptions across Free / Trader / Desk Preview / Desk Full tiers. This is the durable revenue line.
2. **Per-seat scaling at Desk Full v2** — additional seats inside small-fund or solo-PM accounts at $149 or $249/seat (DECISION NEEDED — pricing locked at the band, exact per-seat tier still under v1 review).
3. **Annual prepay discount** — discount in exchange for cash-flow timing and commitment signal (rate **DECISION NEEDED**; conventional range 15–20%, founder-cohort may differ).

**Not monetized in P0–P2:** add-ons, usage-based overages, marketplace listings, alpha resale, performance fees, custody fees, copy-trading take rate. All deferred or explicitly out of scope.

**ASSUMPTION:** Stripe handles billing for all tiers in P1; tax handling and VAT compliance for UAE/EU/MENA transactions still REQUIRES INPUT from counsel.

---

## 3. Likely plan structure direction

Tier matrix locked v1 (Track B canonical):

| Tier | Price | Audience | Core promise | Includes (high-level) |
|---|---|---|---|---|
| **Free** | $0 | Curious traders, evaluation | "See the engine work" | Read-only scanner sample; limited regime view; no risk-gate output |
| **Trader** | $79/mo | P1 Omar, P2 Karim (early) | "Personal risk infrastructure" | Full scanner, risk gates, regime, journal, Telegram alerts; single-user |
| **Desk Preview** | $399/mo | P2 Karim (mature), P3 Layla (early) | "Programmable risk + multi-account view" | Trader features + multi-account · advanced gates · API access (read) · Desk-grade analytics |
| **Desk Full v2** | $1,199/mo + per-seat ($149 or $249) | P3 Layla, small funds | "Institutional-grade risk surface for solo PMs and small desks" | Desk Preview features + seat scaling · audit-grade journal · advanced reporting · DECISION NEEDED on additional v2 deltas |

**Transitions and deferrals:**

- Desk Full v2 launches in the **P5 window (Mar–May 2027)**. Until then, "Desk" is sold as Desk Preview only.
- Annual plans live alongside monthly from P1; trial/intro mechanics are still **DECISION NEEDED** (free-tier-as-trial vs. time-bounded trial).
- Founder-cohort (40 users in P1) may price below sticker — terms locked per cohort document, not generally available.

---

## 4. Value-delivery chain

Linear chain from raw market data to user-actionable surface:

```
Exchange APIs (Binance USDT-perp; Bybit deferred to P2)
        │
        ▼
Vendor stack (P1 narrow): CCXT · CoinGlass · Tradefeeds · CoinGecko · Claude (minimal)
        │
        ▼
Ingestion layer (Python 3.11, Pydantic, Redis cache, PostgreSQL persistence)
        │
        ▼
Engine modules:
  - Scanner (multi-pair confluence, OHLCV + OI + funding + CVD)
  - Regime classifier (v3 ML — Trending / Mean-Reverting / Volatile / Quiet)
  - Risk gate (drawdown · daily loss · leverage · heat · max positions)
  - Position sizer (per-account thresholds)
        │
        ▼
FastAPI surface: /scan · /risk-gate · /position-size · /regime/{symbol} · /performance · /journal
        │
        ▼
User surfaces:
  - Dashboard at coinscope.ai (React 18, TypeScript, Vite, Tailwind)
  - Telegram alerts via @ScoopyAI_bot
        │
        ▼
User decision + user-authorized execution against user's exchange account
        │
        ▼
Journal + performance feedback loop (back into engine for cohort observation)
```

**Where value is captured:** Subscription gates access to engine endpoints and user surfaces. The engine itself, the regime classifier, and the risk-gate logic are the differentiators. Vendor data is commodity; the differentiation is in *how* it's classified, gated, and surfaced.

---

## 5. Key cost drivers

| Cost driver | Category | P0–P1 monthly order-of-magnitude (USD) | Sensitivity | Notes |
|---|---|---|---|---|
| Vendor data fees (CoinGlass, Tradefeeds, CoinGecko paid tiers) | Variable / step-up | Low–medium 3-figure to low 4-figure | High at P2 expansion | Step-up at P2 when more pairs/venues added |
| Inference / LLM (Claude) | Variable | Low; minimal use during validation | Medium — scales with feature use | Held to "minimal" deliberately during P1 |
| Cloud + infra (Postgres, Redis, hosting, Stripe fees) | Mostly fixed | Low–medium 3-figure | Low at P0–P1 scale | Stripe fees are revenue-linked |
| Engineering capacity | Fixed (founder) + step-up at P4 contractor | Founder-funded; contractor budget at v2 build (~3 months) | Highest single sensitivity | Solo-founder bus factor is structural risk |
| Counsel + compliance | Lumpy | Variable; brief work + entity restructure cost | Medium | Pre-validation: minimal; post-validation: step-up |
| Support tooling | Fixed-low | Low 3-figure | Low at <50 users | Scales modestly into P2 |
| Telegram + dashboard hosting | Fixed-low | Low 3-figure | Low | Vercel/Cloudflare/equivalent |

**REQUIRED INPUT:** Specific vendor-fee schedules and Stripe fee math belong in `11-financial-model.md` (already locked v1). This file references; it does not duplicate.

**ASSUMPTION:** Gross margin ~76% at base case (per locked §15 narrative). Revisit after P1 cohort, especially if vendor expansion changes the cost mix at P2.

---

## 6. Key dependencies

External dependencies that, if degraded or removed, change the business materially:

| Dependency | Type | Risk if degraded | Mitigation |
|---|---|---|---|
| Binance USDT-perp API + WebSocket | Critical exchange | Engine becomes inert for primary venue | P1 narrow stack; Bybit at P2 adds redundancy |
| Stripe | Critical billing | Cannot collect revenue | No alternative selected pre-P2; ASSUMPTION: Stripe coverage adequate for UAE/MENA/EU |
| CoinGlass | Important market-data | Loss of OI/liquidation feed quality | Tradefeeds adjacency partial; full mitigation requires P2 redundancy |
| Telegram Bot API | Important surface | Alerts surface degrades; dashboard remains | Dashboard is primary; Telegram is companion |
| Claude API | Optional | Loses one analytical assist; engine still works | Minimal use by design during P1 |
| UAE regulatory posture | Macro | Forces entity restructure or geography pivot | Counsel brief v2 + jurisdictional posture documented |
| Founder availability | Internal-critical | Solo-founder bus factor | P4 contractor support at v2 build; documentation discipline |

---

## 7. Major business constraints

Constraints that cannot be relaxed without explicit decision:

1. **Testnet-only during validation.** No real capital deployed until PCC v2 §8 Capital Cap gates pass. Hard code-level gate.
2. **US users blocked at signup.** Until US licensure path is decided, US is not a target market.
3. **No paid acquisition before Trader CAC validates** (target: M5+).
4. **40-user cap in P1 cohort.** Soft launch is deliberately throttled.
5. **No production-ready claim** until PCC v2 criteria met. Brand-voice rule.
6. **No fund-grade product at P1 or P2.** Desk Full v2 is a P5 deliverable.
7. **Anti-overclaim discipline applies to all external claims**, including investor conversations.
8. **Custody-free posture is structural**, not negotiable. CoinScopeAI does not custody capital under any P0–P5 plan.
9. **Solo-founder + contractor team** through v2 build; no full-time engineering hire pre-validation.
10. **One canonical decision log + decision register**; no parallel decisions outside it.

---

## 8. Business-model assumptions requiring validation

These are bets — explicit and tagged. Each one must be tested by a specific data point during P0–P2.

| # | Assumption | Validation source | Window | Outcome if false |
|---|---|---|---|---|
| BMA1 | $79/mo Trader pricing matches P1 Omar's willingness-to-pay | P1 cohort retention/churn at M1–M3 | P1 (Jun–Jul 2026) | Reprice or repackage Trader |
| BMA2 | $399/mo Desk Preview matches P3 Layla's willingness-to-pay | P1 + P2 Desk Preview signups | P1–P2 | Reposition Desk Preview |
| BMA3 | $1,199/mo + per-seat is the right Desk Full v2 anchor | Solo-PM interviews + intent letters by P5 | P5 (Mar–May 2027) | Restructure Desk Full pricing |
| BMA4 | Annual prepay rate of [DECISION NEEDED]% materially shifts cohort cash flow | P1 cohort prepay attach rate | P1 | Adjust prepay discount or remove |
| BMA5 | Founder-led distribution carries to ~500 paid users without paid acquisition | Pipeline + signup-source attribution | P1–P2 | Trigger paid acquisition (M5+) |
| BMA6 | UAE/MENA + global EN demand mix is sufficient at sticker | P1 cohort geo-mix | P1 | Add or shift geographies |
| BMA7 | Vendor stack at P1-narrow is durable through 40 users | Engine stability + vendor incident rate | P0–P1 | P2 vendor expansion accelerated |
| BMA8 | Custody-free posture reduces (not removes) regulatory burden enough to defer licensure | Counsel brief v2 + jurisdictional review | Pre-P5 | Licensure path forced earlier |
| BMA9 | Anti-overclaim posture compounds trust faster than aggressive marketing would | Cohort referral rate + brand-mention sentiment | P1–P2 | Revisit voice posture |
| BMA10 | Gross margin ~76% holds through P2 vendor expansion | Financial model recheck post-P2 | Aug–Sep 2026 | Reprice or renegotiate vendors |

---

## 9. What this model is not

To stay anti-overclaim-honest:

- It is not a hedge fund. CoinScopeAI does not pool, custody, or trade user capital.
- It is not a signal service. CoinScopeAI does not sell trade ideas; it gates and contextualizes the user's process.
- It is not a copy-trading platform. No mirroring, no following, no leader-follower economics.
- It is not a regulated investment adviser. Counsel-confirmed posture is "tools, not advice." `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` documents the framing.
- It is not yet production-ready. Validation phase is active and ongoing.

---

## 10. Cross-references

- Pricing canonical: `business-plan/06-pricing-monetization.md` + `business-plan/_phase-2/_pricing/`
- Packaging canonical: `business-plan/_phase-2/_packaging/`
- Financial model: `business-plan/11-financial-model.md`
- Vendor failure mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Counsel brief: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
