# Revenue Model

## 1. Revenue model overview

CoinScopeAI's revenue model is **subscription-led with phased SKU activation**. Revenue ambition rises only as Production Candidate Criteria (PCC v2 G1–G4) and §8 Capital Cap milestones are met. The model deliberately separates **revenue capacity** (what tiers exist) from **revenue authorization** (which tiers are safe to sell at the current product phase).

| Layer | Description |
|---|---|
| Revenue capacity | The full Track B tier matrix (Free / Trader / Desk Preview / Desk Full v2). |
| Revenue authorization | Which tiers are operationally safe to monetize given the current PCC state. |
| Revenue quality | Whether revenue is durable (paid retention, low refund risk) vs fragile (early cohort, single-vendor dependency). |

**Current state (P0, May 2026)**: zero revenue assumed. Validation cohort is invitation-only, capped at 40, no monetization pressure. Any revenue collected at this phase would be incidental, not load-bearing.

**Near-term (P1, Jun–Jul 2026)**: narrow-ship begins. **Trader $79/mo** is the only tier we should treat as monetization-ready, and only after G3 of PCC v2 has been demonstrated for ≥30 days.

**Medium-term (P2–P3, Aug 2026–early 2027)**: Trader at scale + **Desk Preview $399/mo** for advanced solo operators. Vendor expansion (Bybit, additional feeds) widens addressable use cases.

**Long-term (P5, Mar–May 2027)**: **Desk Full v2 $1,199/mo + per-seat ($149 or $249)** launches for small fund / multi-seat operators. This is the highest-revenue SKU but explicitly **not launchable earlier** — it requires per-seat audit, role-based access, and stronger compliance posture.

## 2. Likely monetization structure

**Primary revenue streams (in priority order):**

1. **Recurring subscription** — Trader, Desk Preview, Desk Full v2.
2. **Per-seat add-ons** — only on Desk Full v2 ($149 or $249/seat/month). DECISION NEEDED on the rate.
3. **Annual prepay discount** — 2 months free on annual (DECISION NEEDED on whether to offer pre-G4).

**Explicitly NOT in the near-term revenue model:**

- Performance fees, profit share, or AUM-based revenue. Regulatory and trust posture do not support these in any P0–P3 jurisdiction we operate in. (Cross-ref: `14-risk-compliance-and-safeguards`.)
- Brokerage / order routing rebates from exchanges. We do not route customer orders; users connect their own exchange API keys.
- Affiliate revenue tied to referral signups on exchanges. Excluded by trust posture and US-blocked policy.
- Paid signal selling outside the subscription. The signal layer is part of the subscription, not a standalone marketplace.

## 3. Subscription logic

### Tier matrix (Track B canonical, locked 2026-05-01)

| Tier | Price | Audience | Activation phase |
|---|---|---|---|
| Free | $0 | Discovery, light users, persona P1 (Omar) entry | P0+ (always available) |
| Trader | $79/mo | P1 Omar / P2 Karim — solo retail-sized operators | P1 (post G3 for ≥30 days) |
| Desk Preview | $399/mo | Advanced solo / pre-fund operators | P2 (post G4 + vendor expansion validated) |
| Desk Full v2 | $1,199/mo + per-seat ($149 or $249) | P3 Layla — small fund / multi-seat ($200k–$1M aggregate book) | P5 (Mar–May 2027) |

### Key subscription dynamics

- **Free is a trust-builder, not a funnel filler.** It exists so prospects can verify regime labels, gate decisions, and journal output before paying — *not* to maximize signup volume.
- **Trader is the workhorse.** It is the tier we expect to validate monetization first. Pricing is high enough to filter casual signups, low enough to be a defensible upgrade from Free.
- **Desk Preview is a bridge SKU.** It exists to capture operators who outgrow Trader but cannot yet justify Desk Full v2. It must NOT cannibalize Desk Full v2 once that launches.
- **Desk Full v2 is the lever.** Per-seat structure is what makes it economically meaningful at small fund scale; without per-seat, the SKU doesn't carry.

## 4. Possible annual vs monthly revenue mix

| Mix scenario | Description | Cash impact | Refund risk |
|---|---|---|---|
| Monthly-only (default through P1) | Cleanest, lowest commitment, lowest cash | Low cash, smooth | Low — refunds are 1 month max |
| Annual prepay introduced at P1 (with 2mo discount) | Improves cash, increases liability | Strong cash | Material — engine rollback could trigger refund waves |
| Annual prepay only post-G4 | Conservative, defers cash benefit | Delayed cash | Lowest — only sold once gates are stable |

**Recommendation (ASSUMPTION):** monthly-only through P1. Introduce annual prepay only after PCC v2 G4 is demonstrably stable for ≥60 days. Rationale: a refund wave triggered by a rolled-back engine release would damage trust posture more than the cash benefit is worth. (Cross-ref: `14-risk-compliance-and-safeguards`.)

**DECISION NEEDED:** lock annual-policy decision before P2.

## 5. Later-stage team / fund revenue possibilities

Desk Full v2 unlocks revenue patterns unavailable at solo scale:

- **Per-seat expansion within an existing fund customer.** A 3-seat Desk Full v2 deployment is materially more valuable than a 1-seat one and is the simplest expansion lever.
- **Compliance-grade audit features.** Decision logs, per-seat permissions, and exportable journal records become saleable, not just operational. (Possible add-on, DECISION NEEDED.)
- **Dedicated infrastructure tier (LATER).** A fund customer that needs isolated rate-limit budget, separate Redis/PG, or VPC-scoped engine could justify a custom tier. **Not before P5.**

What we should NOT assume:

- That a fund customer will pay for white-label deployment. White-label introduces support and brand-risk burden disproportionate to revenue at our scale.
- That regulated funds will accept our stack without third-party security review (SOC 2 lite or equivalent). That is a P5+ workstream, not a P1 sales claim.

## 6. What revenue should and should not be assumed near-term

**Should be assumed (only as ranges, never as point forecasts):**

- A small, validation-grade Trader cohort emerging post-G3 — measured in low double digits, not hundreds. ASSUMPTION.
- Mostly monthly billing, MENA + global EN geographies, US blocked at signup.
- Single-tier monetization (Trader) as the only proof point for ≥90 days post-launch.

**Should NOT be assumed:**

- Desk Preview revenue before P2.
- Desk Full v2 revenue before P5.
- Any annual contract revenue before annual policy is decided.
- Performance-fee or AUM-based revenue at any phase in the current jurisdictional posture.
- Referral or affiliate revenue from exchanges.
- Enterprise deals via outbound sales — we have no outbound motion budgeted, and inbound from `08-go-to-market` is not yet validated.

## 7. Revenue quality considerations

| Quality dimension | What "good" looks like for CoinScopeAI |
|---|---|
| Durability | Paid >90 days, ≥2 active sessions/week, journal usage. |
| Refund exposure | <2% of MRR refunded per month; <5% in any single month. |
| Concentration | No single customer >10% of revenue (becomes meaningful at Desk Full v2 stage). |
| Vendor dependency | Revenue not contingent on a single exchange or data provider. |
| Trust signal correlation | Paid retention rises with kill-switch transparency, not despite it. |

Revenue from customers who churn after one billing cycle is **lower-quality than zero revenue** at this stage, because it (a) generates support load, (b) risks negative public commentary, and (c) wastes early cohort slots that should go to higher-fit users.

## 8. Retention and churn implications

**ASSUMPTION (load-bearing):** Trader monthly churn at maturity is in the 5–10% range, with early-cohort churn possibly higher (10–20%) until activation flow (`12-onboarding-and-activation`) is tuned.

Why churn is more dangerous here than in a generic SaaS:

- A churned user with a bad experience may publicly attribute losses to the product, even when losses came from their own override of the Risk Gate. The reputational tail is asymmetric.
- Crypto users are highly mobile and price-comparison-driven; absent a clear regime-aware differentiator, they will swap tools at low friction.
- Churn waves correlated with market drawdowns (BTC/ETH down 20%+ in a month) are likely. Model assumptions must allow for this volatility, not pretend monthly churn is smooth.

**Mitigation levers (already covered in upstream folders):**

- Activation flow that demonstrates the Risk Gate's value within the first 7 days (`12-onboarding-and-activation`).
- Trust-ops messaging that pre-frames drawdowns and gate behavior (`13-support-and-trust-ops`).
- Hard kill-switch transparency (`14-risk-compliance-and-safeguards`).

## 9. Risks in the revenue model

| Risk | Why it matters | Watch metric |
|---|---|---|
| **Price compression** | If Trader gets discounted to chase signups, defensibility of Desk Preview / Desk Full v2 collapses. | Trader effective ARPU vs list. |
| **Tier cannibalization** | Desk Preview eating Desk Full v2 demand once v2 launches. | Mix shift Preview → Full at P5 launch. |
| **Provider-driven SKU break** | If a vendor (e.g. CoinGlass) re-prices, our cost structure shifts and the tier may no longer support its margin. | Vendor cost as % of tier ARPU. |
| **Regulatory tightening** | A jurisdiction reclassifying us as advisory could force tier suspension. | Policy news in target jurisdictions. |
| **Trust event** | A public incident (e.g. miscalculated gate) triggers churn wave + refund wave simultaneously. | Refund-rate spike correlated with incident. |
| **Real-capital pressure too early** | Customers demand real-capital trading before PCC v2 is met; we either lose revenue or break the safety promise. | Sales pressure cases logged before G4. |
| **Performance-tied expectation** | Customers conflate subscription with returns; churn when their P&L is bad regardless of product behavior. | Churn correlation with BTC drawdown. |

The recurring theme: **revenue at this stage is fragile by design, and pretending otherwise is the actual risk**. The model is built to be honest about that.
