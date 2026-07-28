# Plan Matrix

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** §6 v1 LOCKED (`business-plan/06-pricing-monetization.md`); `01-executive-summary/business-model-summary.md` §3 (Track B canonical)

---

## 1. Plan matrix at a glance

| | **Free** | **Trader** | **Desk Preview** | **Desk Full v2** |
|---|---|---|---|---|
| **Standard price** | $0 | **$79/mo** · $790/yr | **$399/mo** · $3,990/yr | **$1,199/mo** · $11,990/yr + per-seat |
| **Founder cohort (60-day window)** | $0 | $59/mo | $299/mo | $899/mo |
| **Per-seat add-ons** | — | — | — | $149/mo partner read-only · $249/mo analyst |
| **Intended buyer** | Sub-$5k disciplined; evaluating P1 Omar; methodology-curious | P1 Omar (primary); P2 Karim (early evaluation) | P2 Karim (mature); P3 Layla (early / pre-v2) | P3 Layla; small funds (P5+) |
| **Internal persona match** | Pre-P1 / sub-$5k disciplined | P1 (anchor); some P2 | P2 (anchor); some P3 | P3 (anchor) |
| **Operating shape** | Account-verified, evaluation-only | 1 user · 1 account | 1 user · 2+ accounts · API | 1 PM + N partner / analyst seats · audit-grade |
| **Ships when** | Live now | P1 (Jun 2026 soft-launch) | P1 close → P2 | **P5 (Mar–May 2027)** |
| **Default offer first?** | No (entry, not target) | **Yes — primary** | Opportunistic | No — deferred |

---

## 2. Plan names

Locked per §5.3.3. No renames without brand-voice review.

| Internal name | External name | Why this name |
|---|---|---|
| Free | **Free** | Self-evident; matches comp-set norms |
| Trader | **Trader** | Matches the buyer's self-description; avoids "Pro/Premium" claims |
| Desk Preview | **Desk Preview** | "Preview" labeling protects against premature audit-grade claims |
| Desk Full v2 | **Desk Full v2** | "v2" labeling makes the deferred status explicit; "Full" only when the audit-grade capability ships |

**Rejected alternatives:**

- ~~Pro / Premium / Enterprise~~ — implies maturity claim PCC v2 has not certified
- ~~Starter / Plus / Ultimate~~ — generic SaaS pattern; says nothing about operating shape
- ~~Solo / Team / Fund~~ — "Fund" creates regulatory ambiguity (CoinScopeAI is not a fund)

---

## 3. Intended buyer by plan

### Free — "Account-verified evaluation"

- **Who buys (or signs up):** Disciplined retail traders evaluating CoinScopeAI; sub-$5k disciplined users we treat as future ICP, not current customers; methodology-curious P2 Karims doing a buy-vs-build evaluation.
- **Who should not sign up:** Casual retail looking for free signals; copy-trade audience; alpha-seekers; anti-ICP per `04-icp-and-segmentation/secondary-icps.md` §6.
- **What we expect from them:** Account verification at signup. Engagement with the demo-trade view of risk-gate behavior. Clicking through the engine methodology documentation.

### Trader — "Personal risk infrastructure"

- **Who buys:** P1 Omar — disciplined retail crypto-perp trader, account size $20k–$150k, has a written trading plan they have followed 12+ months. Predominantly UAE/MENA + global EN. Pays for tools that respect their framework.
- **Secondary buyer:** P2 Karim — engineer-trader doing a buy-vs-build evaluation; will upgrade if API depth becomes binding.
- **Who should not buy:** Sub-$5k accounts; copy-trading audience; users seeking signals or autonomous execution; users who reject testnet-first / validation-phase posture.
- **Operating shape served:** 1 user, 1 exchange account (Binance USDT-M perp at P1; +Bybit at P2).

### Desk Preview — "Programmable risk + multi-account view"

- **Who buys:** P2 Karim mature — API rate limits became binding on Trader; or P3 Layla early — running 2–3 accounts pre-v2, treats Preview as a transitional bundle replacement.
- **Who should not buy:** P1 Omar with a single account (no value over Trader); P3 Layla with formal partner-reporting obligations (audit-grade reporting is v2, not Preview); anyone expecting write-API capability.
- **Operating shape served:** 1 user, 2+ accounts, read-only API at ~1 req/sec/endpoint, static monthly performance PDF.

### Desk Full v2 — "Solo PM + small desk infrastructure"

- **Who buys:** P3 Layla — solo portfolio manager running $200k–$1M aggregate book with partner reporting obligations; small funds with similar shape.
- **Who should not buy:** Any single-account operator (use Trader); any pre-validated user who wants real-capital deployment beyond the §8 phased ramp (gated regardless of tier); regulated funds expecting custody (CoinScopeAI is custody-free, structurally).
- **Operating shape served:** 1 PM seat included; partner read-only and analyst seats added per-seat; audit-grade reporting; full API depth; multi-venue.
- **Ship date:** P5 (Mar–May 2027). Not in market before then.

---

## 4. Feature access by plan

Linear ladder — capabilities only **add** as you go up; never subtract.

| Capability | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| **Account verification at signup** | ✅ Required | ✅ Required | ✅ Required | ✅ Required |
| **Public engine methodology docs** | ✅ | ✅ | ✅ | ✅ |
| **Validation-phase status disclosure** | ✅ | ✅ | ✅ | ✅ |
| **"What CoinScopeAI does not do" reference** | ✅ | ✅ | ✅ | ✅ |
| **Read-only top-5 signal list (delayed, daily refresh)** | ✅ | — (full feed) | — (full feed) | — (full feed) |
| **Per-symbol regime label without confidence** | ✅ | — (with confidence) | — (with confidence) | — (with confidence) |
| **Demo-trade view of risk-gate behavior** | ✅ | — (live) | — (live) | — (live) |
| **Capital-preservation primitives on demo trades** | ✅ | — (on real config) | — (on real config) | — (on real config) |
| **"We'll be back" sub-$5k messaging** | ✅ | — | — | — |
| **Multi-pair scanner — full feed** | ❌ | ✅ | ✅ | ✅ |
| **Regime classifier with confidence — every signal** | ❌ | ✅ | ✅ | ✅ |
| **Risk gate at locked thresholds (10% DD / 5% daily / 10x lev / 5 max pos / 80% heat)** | ❌ | ✅ | ✅ | ✅ |
| **Position sizer with math transparency** | ❌ | ✅ | ✅ | ✅ |
| **Per-account user-configurable thresholds (above floors)** | ❌ | ✅ | ✅ | ✅ |
| **Personal performance journal (R-multiple + rule-violation tagging)** | ❌ | ✅ | ✅ | ✅ |
| **Telegram alerts via @ScoopyAI_bot (canonical payload)** | ❌ | ✅ | ✅ | ✅ |
| **Single-account workflow end-to-end** | ❌ | ✅ | — (multi) | — (multi) |
| **Multi-account view (≥2 accounts)** | ❌ | ❌ | ✅ | ✅ |
| **Programmable risk gates (composition above locked thresholds)** | ❌ | ❌ | ✅ | ✅ |
| **Read API (≈1 req/sec/endpoint)** | ❌ | ❌ | ✅ | ✅ (higher rate limits) |
| **Static monthly performance PDF** | ❌ | ❌ | ✅ | — (audit-grade) |
| **Cross-account journal aggregation** | ❌ | ❌ | ✅ | ✅ |
| **Partner read-only seats** | ❌ | ❌ | ❌ | ✅ ($149 / seat) |
| **Analyst seats with write privileges** | ❌ | ❌ | ❌ | ✅ ($249 / seat) |
| **Audit-grade reporting (P5 deliverable)** | ❌ | ❌ | ❌ | ✅ |
| **Higher API rate limits / write endpoints** | ❌ | ❌ | ❌ | ✅ |
| **Real-capital deployment beyond §8 Capital Cap phased ramp** | ❌ | ❌ | ❌ | ❌ (gated by code, regardless of tier) |
| **Custody, pooling, copy-trade, performance fees** | ❌ | ❌ | ❌ | ❌ (structural — never) |

Notes:

- **Bybit and additional venues:** ship at P2 vendor expansion; available across all paid tiers thereafter, not gated by SKU.
- **LP-style gates, tax-ready exports, mobile app:** post-v2 deliverables; not in any current tier.
- **Free tier bias:** sub-$5k disciplined users see "we'll be back" messaging; sub-$5k anti-ICP users see no upgrade prompt.

---

## 5. Support and access differences by plan

Cross-reference `13-support-and-trust-ops/` (Wave 2 next folder). Pricing-page summary:

| Dimension | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| **Support channel** | Public docs + community | Email inbox; founder-handled during P1 | Email inbox; same-business-day response target | Email + named ops contact; priority routing |
| **Response SLA target** | None | Best-effort, ≤2 business days at P1 | Same business day, business hours | ≤4 business hours, business hours |
| **After-hours escalation** | None | None (incidents handled per `13-support-and-trust-ops/`) | None | Critical-incident path documented |
| **Onboarding** | Self-serve docs | Self-serve + onboarding email sequence | Self-serve + 1× founder kickoff call (P1–P2) | Self-serve + named-contact onboarding |
| **Status page access** | Public | Public | Public + per-account status | Public + per-account status + scheduled-window notice |
| **Brand-voice in support** | n/a | Product-tier (terse, technical) | Product-tier | Product-tier + named contact |
| **Partner / analyst seats** | n/a | n/a | n/a | Each seat has independent dashboard access; PM controls invite/revoke |
| **Refund SLA** | n/a | 14-day money-back, single-use | 14-day money-back, single-use | 14-day money-back, single-use |

**ASSUMPTION:** SLAs above are P1–P2 commitments. Post-P2 with paid acquisition active, Trader SLA may tighten to "next business day". Re-validate at P1 close.

---

## 6. Who should not buy each plan

Anti-fit signals at signup are filtered by the criteria below. Cohort quality depends on this filter being honest.

### Free — anti-fit

- US-residents (blocked at signup until US licensure path is decided)
- Casual retail seeking free signals (no signals are surfaced on Free)
- Copy-trade audience or alpha-seekers (anti-ICP per §3.5)
- Users explicitly looking for autonomous execution
- Users looking for "free trial of the full product" — Free is **not** a feature trial

### Trader — anti-fit

- Sub-$5k account holders (filtered; routed to Free with "we'll be back" messaging)
- US-residents
- Multi-account operators (Trader is single-account; should evaluate Desk Preview)
- Buyers expecting partner-reporting capability (not in Trader; not in Preview either)
- Anyone seeking real-capital deployment outside §8 Capital Cap phased ramp
- Buyers who reject testnet-first or validation-phase posture
- Buyers who request signals, autonomous execution, or copy-trading

### Desk Preview — anti-fit

- Single-account operators (Trader is the better fit)
- P3 Layla with formal audit-grade reporting obligations (the static PDF is not audit-grade; Desk Full v2 ships at P5)
- Buyers expecting write-API capability (not in Preview)
- Buyers who want partner seats (not in Preview)
- US-residents
- Anyone expecting "a Bloomberg terminal at $399"

### Desk Full v2 — anti-fit

- Single-account operators
- Regulated funds expecting custody, pooling, or fund administration
- Performance-fee-driven economic models
- Anyone who would have signed up before P5 (not in market before then)
- US-residents
- Buyers who reject custody-free posture as a structural choice

---

## 7. Default offer first

**The default offer at P1 (Jun–Jul 2026) and through P2 public launch (Aug–Sep 2026) is Trader at $79/mo.**

Reasons:

- **ICP match.** P1 Omar is the locked primary persona; Trader is his anchor tier. Founder-led distribution channels (methodology Substacks, applied-quant Twitter, closed Discords) reach P1 Omar most efficiently.
- **Capability readiness.** Trader's capability set is what MVP definition (`06-product-strategy/mvp-vs-beta-vs-scale.md`) commits to delivering at validation quality.
- **Cohort signal quality.** A 40-user P1 cohort heavy on Trader produces the cleanest retention, churn, and rule-respect signal — the data the next 6 months need.
- **Operational sustainability.** Founder-led ops can support Trader at the cohort cap without SLA promises that cannot be upheld.

Desk Preview signups are **welcome and not discouraged**, but the funnel and content motion are not optimized for Desk Preview until P2 vendor expansion + brand depth in P3 fund-adjacent channels.

Free is the **entry**, not the **target**. Free's purpose is acquisition cost reduction (we get to verify and qualify before any paid step) and ICP filtering (the "we'll be back" messaging routes anti-ICP and pre-ICP users away from immediate conversion).

---

## 8. Which later-stage plans should be deferred

| Plan | Defer until | Why |
|---|---|---|
| **Desk Full v2** | **P5 (Mar–May 2027)** | Audit-grade reporting requires v2 build; per-seat ops requires §10 readiness; partner-reporting trust requires a track record we are still earning |
| **Real-capital tier (above §8 phased ramp)** | **PCC v2 §8 pass + counsel sign-off** | Code-level testnet hard-gate is a structural primitive; no SKU exists for unrestricted live-capital deployment |
| **Fund-grade SKU** | **Indefinite — not on roadmap** | CoinScopeAI is not a fund; structural (per `business-model-summary.md` §9) |
| **White-label / OEM tier** | **Indefinite — not on roadmap** | Dilutes canonical brand; complicates trust posture |
| **API-power-user tier between Trader and Desk Preview** | **Defer until P1 cohort signals demand** | Avoid SKU proliferation pre-validation; can be added post-P2 if cohort data justifies |
| **Mobile-only tier** | **Post-v2** | Mobile-first is a future product, not a future SKU |
| **Tax-ready exports tier** | **Post-v2 + counsel input** | Jurisdictional complexity exceeds current ops capacity |

The discipline: **a deferred plan is mentioned on the public roadmap, not on the pricing page.** Coming-soon copy on a pricing page degrades trust faster than it converts.

---

## 9. Plan transitions and upgrade paths

Mechanics inherited from §6.7 + §6.6, restated for operator clarity.

### Upgrade (Trader → Desk Preview, or any tier to a higher tier)

- Takes effect immediately.
- User is charged the pro-rated difference for the remainder of the current billing period.
- Founder-cohort discount, if active, transfers to the new tier at the founder-cohort price for that tier (within the original eligibility window).
- Annual prepay rolls forward — credit applied to the new tier's annual price.

### Downgrade (Desk Preview → Trader, or any tier to a lower tier)

- Takes effect at next renewal.
- No immediate refund of the price difference.
- Account access remains at the current tier until the renewal boundary.
- Per-seat removals follow the same rule.

### Per-seat additions / removals (Desk Full v2 only)

- Additions: immediate, pro-rated charge.
- Removals: take effect at next renewal.
- Founder-cohort per-seat pricing applies during the eligibility window only.

### Annual ↔ monthly switch

- Allowed only at renewal boundary, not mid-cycle.
- Founder-cohort and annual prepay discounts do not stack — the user picks one path per renewal.

### Reactivation after cancellation

- Within 90 days: prior tier and pricing restored. Journal and configuration retained.
- After 90 days: re-onboards as new account at current standard pricing. Founder-cohort is **not** re-extended.
- Account data permanently deleted at 90 days unless user requests longer hold (per §10 ops).

---

## 10. Cross-references

- §6 v1 LOCKED canonical: `business-plan/06-pricing-monetization.md`
- Phase 2 packaging notes: `business-plan/_phase-2/_packaging/03-plan-comparison-table-v1.md`
- Packaging strategy (rationale): `07-packaging-and-pricing/packaging-strategy.md`
- Pricing strategy (rationale): `07-packaging-and-pricing/pricing-strategy.md`
- Trial / discount / refund: `07-packaging-and-pricing/trial-and-discount-policy.md`
- Support tiers (forthcoming): `13-support-and-trust-ops/`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
