# Packaging Strategy

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** §6 v1 LOCKED (`business-plan/06-pricing-monetization.md`); `_phase-2/_packaging/` working notes

---

## 1. Packaging philosophy

CoinScopeAI packages **discipline enforcement**, not feature lists. The product is bought because it forces a user's own framework on themselves at scale; it is not bought because it has more checkboxes than a competitor's pricing page.

Five principles, in order of weight:

1. **Trust gates packaging, not the other way around.** A capability is in a tier only if its quality bar matches what that tier's buyer will pay for. "Stabilizing in cohort" features can ship in Trader at $79 because the price already signals "this is a tool, not a finished system" — but they cannot ship in Desk Preview at $399 without compromising P3 Layla's audit posture.
2. **Capital-preservation primitives are universal.** The risk gate, regime classifier, and testnet hard-gate are present in every paid tier. They are not premium features. They are the product.
3. **Tiers map to operating shape, not feature counts.** Trader = single-user, single-account. Desk Preview = multi-account, programmable, API. Desk Full v2 = multi-seat, audit-grade, partner reporting. The tier name describes the buyer's operating context, not the SKU's feature density.
4. **No anti-ICP bundling.** Per §5.3.3, no tier ever includes signal-group access, copy-trading, leverage maximization, or "trade more to win more" framing. Packaging is structurally aligned with positioning.
5. **No lifetime, no grandfather, no permanent founder discount.** Per §5.3.5, all preferential pricing is time-bounded. Packaging respects the future repackaging right.

---

## 2. Recommended offer structure for CoinScopeAI

Track B canonical, locked v1 — four tiers, one upsell axis:

```
                        ┌──────────────────────────────┐
                        │   FREE — $0                   │
                        │   "See the engine work"       │
                        │   Account-verified entry      │
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │   TRADER — $79/mo             │
                        │   "Personal risk infra"       │
                        │   Single user · single acct   │
                        └──────────────┬───────────────┘
                                       │  (account scale + multi-account need)
                                       ▼
                        ┌──────────────────────────────┐
                        │   DESK PREVIEW — $399/mo      │
                        │   "Programmable risk + API"   │
                        │   Multi-account · read API    │
                        └──────────────┬───────────────┘
                                       │  (P5 — Mar–May 2027)
                                       ▼
                        ┌──────────────────────────────┐
                        │   DESK FULL v2 — $1,199/mo    │
                        │   + per-seat $149 / $249      │
                        │   "Solo PM + small desk"       │
                        │   Audit-grade reporting        │
                        └──────────────────────────────┘
```

**Why this shape works:**

- One linear ladder, no parallel SKUs. P1 Omar evaluates Trader; if he scales, he upgrades. P3 Layla skips Trader and lands on Desk Preview today, then upgrades to Desk Full at P5. There is no pricing-page maze.
- Per-seat charge sits **only** at Desk Full v2 — the tier where partner count is the actual scale dimension. No per-seat at Trader or Desk Preview because those tiers serve single-operator personas.
- The `Free → Trader` step is a **discipline-gate**, not a feature-gate. Free is account-verified; sub-$5k disciplined users get "we'll be back" messaging rather than journal-access-as-trial.
- The `Desk Preview → Desk Full v2` step is **temporally gated** to P5. Until then, "Desk" is sold only as Preview, with explicit "Preview" framing in every surface.

---

## 3. What the initial paid product should be

**Trader at $79/mo is the initial paid product.** Concretely, this is the SKU CoinScopeAI commercializes during P1 (Jun–Jul 2026) and through P2 public launch.

Reasons:

- It is the only tier whose ICP (P1 Omar) is reachable through founder-led distribution at the scale a 40-user cohort cap supports.
- Its capability set (engine API + dashboard + journal + Telegram + risk gate at user-defined thresholds) is what the MVP definition in `06-product-strategy/mvp-vs-beta-vs-scale.md` already commits to building at validation quality.
- Its price ($79) sits inside the $40–$150 band that Wave 1 §6.2 locked for P1 Omar's WTP, and is clean against the ~$200/mo cobbled bundle P1 currently spends on TradingView + Tradervue + Edgewonk + occasional CoinGlass.
- It can ship before Desk Preview is at quality bar — Desk Preview is targeted to reach quality bar at P1 close, but is not required for soft-launch.

**Desk Preview at $399/mo ships alongside Trader at P1 close**, with explicit "Preview" labeling. P3 Layla can sign up at P1 if she finds us, but the funnel is not optimized for her until P2 vendor expansion completes.

**Desk Full v2 ships at P5.** No Desk Full SKU appears on the pricing page, in copy, or in sales conversation before then. (See §7 below.)

---

## 4. Core vs. Premium vs. Deferred capability separation

| Layer | What it is | Where it appears | Source of truth |
|---|---|---|---|
| **Core** | Capabilities every paid tier has, because they are the product itself | Trader, Desk Preview, Desk Full v2 | `06-product-strategy/core-product-pillars.md` |
| **Premium** | Capabilities that scale with operating shape (multi-account, API depth, partner seats, audit reporting) | Desk Preview and above | `06-product-strategy/feature-prioritization.md` |
| **Deferred** | Capabilities not yet built, not yet trustworthy, or out of scope until a later phase | Not in any tier; absent from pricing page | `06-product-strategy/mvp-vs-beta-vs-scale.md` |

### Core (in every paid tier)

- Multi-pair scanner across Binance USDT-M (Bybit at P2)
- Regime classifier (v3 ML — Trending / Mean-Reverting / Volatile / Quiet) with confidence
- Risk gate at the locked five thresholds (10% drawdown / 5% daily loss / 10x leverage / 5 max positions / 80% heat) — user-configurable above floors
- Position sizer with math transparency
- Single-account workflow end-to-end
- Canonical Telegram alerts (@ScoopyAI_bot) and dashboard payload at coinscope.ai
- Journal capture with R-multiple + rule-violation tagging
- Code-level testnet hard-gate (until §8 Capital Cap passes; then PCC v2 phased ramp)
- Engine methodology documentation (public regardless of tier — per §5.3.1)

### Premium (Desk Preview and above)

- Multi-account view (≥2 accounts; specific cap **DECISION NEEDED**)
- Programmable risk gates (rule composition above the locked five thresholds)
- Read API access at target ~1 req/sec/endpoint (rate limits widen at Desk Full v2)
- Static monthly performance PDF (Desk Preview); audit-grade reporting (Desk Full v2)
- Cross-account journal aggregation
- Partner / analyst seats (Desk Full v2 only — $149 / $249 per seat)
- Priority support routing (see `13-support-and-trust-ops/`)

### Deferred (not in any current tier)

- LP-style capital-preservation gates (post-v2)
- Tax-ready exports (post-v2; counsel input required)
- Mobile app (post-v2)
- Bybit and additional venues (P2 vendor expansion)
- Real-capital deployment beyond the §8 Capital Cap phased ramp (gated)
- Fund-grade product (deferred indefinitely; CoinScopeAI is not a fund — see `01-executive-summary/business-model-summary.md` §9)
- Custody, pooling, mirroring, copy-trading, performance fees (structural — never)

---

## 5. Packaging logic — advanced solo traders vs. more professional users

The packaging splits along a **single operating-shape axis**: how many accounts and how many people the buyer operates against.

| Axis dimension | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|
| Accounts under management | 1 | 2+ | 2+ with audit |
| People operating the system | 1 (the trader) | 1 (the trader, with deeper API) | 1 PM + N partner / analyst seats |
| Reporting obligation | None / personal | Personal + light external | Audit-grade external |
| API depth needed | Low (occasional) | Moderate (daily) | Moderate–high (daily, multi-seat) |
| WTP frame (§6.2) | 1–3% of account/mo | Buy-vs-build at engineering rates | 0.3–1% of book/mo |

**Implication for advanced solo traders (P1 Omar):**

- Trader at $79/mo is sufficient. There is no upgrade pressure unless their account scales past where manual cross-account work breaks (per `04-icp-and-segmentation/primary-icp.md` §2.5, around the multi-position ~$50k threshold).
- They do not need API depth, multi-account, or partner seats to get the discipline-enforcement value the product promises.
- The pricing page must not push P1 Omar toward Desk Preview unless their actual operating shape needs it. Manufactured upgrade pressure is anti-ICP.

**Implication for more professional users (P3 Layla):**

- They skip Trader. The Trader tier does not solve their multi-account or partner-reporting problem; offering it as a "starter" would be a packaging mistake.
- They land on Desk Preview at $399 as a transitional commitment that buys them the bundle replacement (Nansen + CoinGlass + journal) while the audit-grade Desk Full v2 is still pre-launch.
- They convert to Desk Full v2 at P5 with per-seat scaling that finally captures the partner-count dimension that drives their actual cost-of-operations.

**Implication for engineer-traders (P2 Karim):**

- They start at Trader to evaluate. The buy-vs-build math at $79/mo (~$948/year ≈ ~10 hours of senior engineering time) is favorable, so the test is whether the methodology is credible enough.
- If credible, they upgrade to Desk Preview at $399 when API rate limits become binding (this is the §6.2 documented upgrade trigger).
- They are watch-list secondary, not a primary acquisition target during P1.

---

## 6. What should remain intentionally limited early on

The discipline of packaging at validation phase is **constraining the shippable scope on purpose**, even where capability technically exists. Five concrete limits:

1. **Free tier is account-verified, not feature-rich.** No journal access on Free, no real-time signals, no Telegram bot, no API. Per §6.5 locked Scope B. The "we'll be back" messaging is the product for sub-$5k users, not free journal access.
2. **Trader is single-user, single-account.** Even if the engine technically supports two accounts, packaging enforces a one-account ceiling to preserve the Trader → Desk Preview upgrade path. (Implementation: account-count check at exchange-connection step.)
3. **Desk Preview API is read-only.** No write endpoints during P1 or P2. Write-API capability is a Desk Full v2 deliverable, not a Preview feature. This protects the trust posture: buyers cannot delegate execution authority to a Preview-tier product.
4. **No leaderboards, no public performance dashboards, no testimonials presented as endorsement** — at any tier. These are anti-overclaim violations regardless of what they would do for conversion.
5. **No "founder discount forever" copy** — at any tier. Founder cohort is time-bounded per §6.7 and §5.3.5; copy must say so explicitly. ("Founding-member pricing — locked through your first renewal cycle, then standard pricing applies.")

These limits cost short-term conversion. They protect long-term trust. P1 Omar specifically rewards companies that exhibit this kind of restraint.

---

## 7. What should not be packaged yet

Capabilities that are deliberately **not** packaged into any tier today, with the trigger that would unlock them:

| Capability | Why not packaged yet | Trigger to revisit |
|---|---|---|
| **Real-capital deployment beyond §8 Capital Cap** | PCC v2 §8 is the gate; until it passes, real capital stays gated by code | PCC v2 G1–G4 + §8 pass — `Validation_Phase_Exit_Memo` filed |
| **Desk Full v2 (audit-grade, multi-seat)** | Audit-grade reporting requires v2 build; preview-quality is not the same product | P5 (Mar–May 2027) |
| **Bybit and additional venues** | P1 vendor stack is narrow; reliability is not yet verified | P2 vendor expansion (Aug–Sep 2026) |
| **Performance fees, custody, pooling, mirroring, copy-trading** | Structural anti-claims per `business-model-summary.md` §9 | Never |
| **Tax-ready exports** | Counsel input required; jurisdictional complexity | Post-v2 |
| **LP-style capital-preservation gates** | v3 capability; not in current engine | Post-v2 |
| **Mobile app** | Post-v2 priority; current dashboard is responsive web | Post-v2 |
| **Bundled crypto payments** | UAE sole-prop posture; Stripe-only at P1; not worth complexity at validation phase | Revisit post-v2 if MENA users request |
| **Affiliate / referral revenue share** | Anti-overclaim risk with affiliate-driven copy; structural channel-misalignment | Post-P5, with brand-voice review gate |
| **White-label / OEM SKU** | Out of scope; would dilute the canonical brand and complicate trust posture | Not on roadmap |
| **Fund / accelerator / incubator add-on** | Out of scope; CoinScopeAI is not a fund | Not on roadmap |

The pricing page does not allude to any of the above. Surfaces that mention "coming soon" must point to a published roadmap section or be removed.

---

## 8. Packaging risks to avoid

Eight failure modes that have killed packaging at trust-sensitive trading products historically, mapped to specific guards.

| # | Risk | Why it kills CoinScopeAI specifically | Guard |
|---|---|---|---|
| **R1** | **Feature-stuffing the Free tier** | Sub-$5k users churn from "free was enough"; cohort signal degrades; support cost rises | §6.5 locked Scope B — no journal, no real-time, no API on Free |
| **R2** | **Naming a tier "Pro" or "Premium"** | Implies maturity that PCC v2 has not yet certified; anti-overclaim violation | §5.3.3 — locked tier names are Trader / Desk Preview / Desk Full v2 |
| **R3** | **Cross-tier feature spaghetti** ("Trader has X but Desk Preview doesn't") | Confuses buyers and signals incoherent operating shape | One linear ladder; capabilities only **add** as you go up — never subtract |
| **R4** | **Selling Desk Full v2 as if it ships now** | When the v2 ship slips, every customer who paid for "Full" feels misled | "Desk" is sold only as "Preview" until P5; "v2" labeling explicit on every Desk Full surface |
| **R5** | **Packaging a real-capital tier before §8 passes** | Trust collapse + regulatory exposure | Code-level testnet hard-gate; no SKU implies live trading; PCC v2 phased ramp is the only path |
| **R6** | **Over-packaging support / SLAs** | Promised SLAs at $79/mo that the founder-led ops team cannot uphold | SLAs match `13-support-and-trust-ops/` v1 — Trader is best-effort, not contractual |
| **R7** | **Per-trade pricing or volume-tied add-ons** | Adverse incentive — we win when the user trades more, which is anti-ICP | §6.3 — Model C explicitly rejects per-trade; no add-ons of this shape ever |
| **R8** | **Founder-cohort framing as "lifetime"** | Time-bounded discount marketed as permanent damages credibility on next renewal | §6.7 + §6.10 Flag 1 — "founding-member pricing — locked through your first renewal cycle" only |
| **R9** | **Performance-tier upcharges** ("Trader Plus — for traders who win more") | Positioning suicide; gambling adjacency | Never. No tier name, copy, or upsell is performance-conditioned |
| **R10** | **Anti-ICP cross-promotion** (signal groups, copy-trade, prop-firm offers) | Brand contamination; cohort signal pollution | §5.3.3 — no co-marketing or bundled promotions with anti-ICP products |

When in doubt, the test is: **does this packaging decision reduce the price the buyer pays in trust?** If yes, do it differently.

---

## 9. Operating implications for downstream folders

| Downstream folder | What this packaging strategy commits to |
|---|---|
| `08-go-to-market/` | Trader is the primary funnel target during P1; Desk Preview is opportunistic; Desk Full v2 is **not** in market until P5 |
| `12-onboarding-and-activation/` | Free-tier "we'll be back" messaging is a first-class onboarding path, not an afterthought |
| `13-support-and-trust-ops/` | SLA tiers must match: Trader = best-effort + business-hours; Desk Preview = same-business-day; Desk Full v2 = priority routing + named ops contact |
| `14-risk-compliance-and-safeguards/` | Code-level testnet hard-gate is a **packaging** primitive, not just an engineering detail — it must be visible in product copy |
| `business-plan/11-financial-model.md` | Per-seat density at Desk Full v2 is the highest-impact sensitivity; modeling assumptions inherit from §6.9 |
| `business-plan/13-kpi-okr.md` | Tier-conversion KPIs must be modeled separately: Free → Trader, Trader → Desk Preview, Desk Preview → Desk Full v2 |

---

## 10. Cross-references

- §6 v1 LOCKED canonical: `business-plan/06-pricing-monetization.md`
- Phase 2 packaging notes: `business-plan/_phase-2/_packaging/`
- Tier matrix detailed: `07-packaging-and-pricing/plan-matrix.md`
- Pricing rationale: `07-packaging-and-pricing/pricing-strategy.md`
- Trial / discount / refund: `07-packaging-and-pricing/trial-and-discount-policy.md`
- Decision log entries: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
