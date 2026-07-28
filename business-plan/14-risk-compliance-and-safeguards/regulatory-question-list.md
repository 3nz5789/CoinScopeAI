# Regulatory Question List

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_data/legal/Counsel_Brief_v2.md`; `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`; `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`; `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`

---

## 1. How to use this file

This file is the **structured question set for counsel and compliance review**. Questions are organized by area and priority.

- Questions marked **[P1]** must be answered before P1 launch (2026-06-01).
- Questions marked **[P2]** must be answered before P2 public launch (Aug–Sep 2026).
- Questions marked **[P5]** must be answered before P5 Desk Full v2 launch (Mar–May 2027).
- Questions marked **[Continuous]** are quarterly review items.

Each question carries the **CA-#** that depends on it (per `compliance-assumptions.md`) and the **business decision** the answer unblocks.

This is not legal advice. It is the request set the company will send to counsel.

---

## 2. Positioning questions

Counsel must opine on whether CoinScopeAI's positioning is defensible given the operating posture and target jurisdictions.

### 2.1 [P1] Tools-not-advice positioning (CA-5, CA-7)

> The product produces signals (long/short with entry, regime label, confidence score, gate result, position-sizing rationale) that are descriptive engine outputs displayed to the user. The user decides whether to act. We do not personalize recommendations to the user's portfolio, financial situation, or investment objectives.

**Question for counsel:**

Q-Pos-1. **Is the "tools, not advice" positioning defensible across our target jurisdictions (UAE primary, MENA secondary, EU/UK read-across)?** Specifically, does the structure of our signal output (regime + confidence + gate + sizing rationale, displayed to the user without personalized recommendation) cross the line into regulated investment advice in any of these jurisdictions?

Q-Pos-2. **What surface-level disclaimers do you require in addition to the validation-phase footer to support the tools-not-advice posture?**

Q-Pos-3. **At what point would the addition of personalization features (e.g., per-user trade suggestions tuned to their portfolio) shift the positioning from tools to regulated advice?**

**Unblocks:** Pricing page tier descriptions; methodology page; support reply templates; finalization of `No_Investment_Advice_Memo_v0_DRAFT.md`.

### 2.2 [P1] "Institutional-grade" usage (CA-6)

> The phrase "institutional-grade, AI-driven crypto futures trading" appears in CoinScopeAI's positioning. We use it for capability and audience-bridging value descriptions, not for status / certification / regulation / track record.

**Question for counsel:**

Q-Pos-4. **Is "institutional-grade" usage in our positioning defensible given (a) our sole-prop status, (b) our validation-phase posture, and (c) the lack of regulatory certification?**

Q-Pos-5. **What contextual framing (around the phrase) reduces legal exposure to the minimum?**

Q-Pos-6. **Are there alternative terms (e.g., "professional-grade", "operator-grade") that carry less regulatory implication?**

**Unblocks:** Hero copy; pitch deck; about page; pricing-page tier descriptions.

### 2.3 [P1] "Custody-free by structural choice" (CA-8)

> CoinScopeAI never custodies user capital. Capital remains in the user's exchange account at all times. The product enforces user-defined risk gates and surfaces signals; execution is user-authorized.

**Question for counsel:**

Q-Pos-7. **Does the custody-free posture, combined with risk-gate enforcement, constitute a "managed account" or "discretionary advisor" service in any of our target jurisdictions?**

Q-Pos-8. **Does the multi-account view in Desk Preview, or the per-seat partner-reporting in Desk Full v2, alter this characterization?**

**Unblocks:** Desk Preview multi-account framing; Desk Full v2 audit-grade reporting language; positioning across all surfaces.

### 2.4 [P5] Solo PM positioning at Desk Full v2 (R-002)

> Desk Full v2 is positioned for solo portfolio managers running $200k–$1M aggregate books. Per-seat scaling captures partner read-only and analyst seats.

**Question for counsel:**

Q-Pos-9. **Does the solo-PM positioning, combined with partner-reporting capability at Desk Full v2, drift toward "fund infrastructure" or "fund administration" service framing?**

Q-Pos-10. **What language and structural commitments preserve the tools-not-advice posture at the Desk Full v2 tier?**

**Unblocks:** Desk Full v2 audit-grade reporting language; pre-P5 launch announcement.

---

## 3. Automation questions

Counsel must opine on whether the engine's enforcement and execution patterns are defensible given the validation-phase posture.

### 3.1 [P1] Risk-gate enforcement (CA-8)

> The risk gate runs **before** trade arming. If the user's configured thresholds (within the locked floors) are breached, the proposed trade is rejected with explicit gate-result reasoning. The user does not execute the rejected trade.

**Question for counsel:**

Q-Auto-1. **Does pre-trade risk-gate enforcement constitute "trading on behalf of the user" or "discretionary execution" in any target jurisdiction?**

Q-Auto-2. **Does the user-configurable threshold model (within locked floors) sufficiently establish that the user, not the engine, is the decision-maker?**

Q-Auto-3. **What surface-level disclosures are required to make this clear to users at signup, exchange-connection, and during operation?**

**Unblocks:** Risk-gate UI copy; engine documentation; Risk Disclosure finalization.

### 3.2 [P1] Locked risk-gate floors (P-S4)

> The locked floors are: 10% drawdown / 5% daily loss / 10x leverage / 5 max positions / 80% heat. Users can configure tighter thresholds; they cannot relax below the floors.

**Question for counsel:**

Q-Auto-4. **Are the locked floors a "fiduciary commitment" or a "product feature" from a regulatory perspective?**

Q-Auto-5. **Could the locked floors create implicit regulatory expectations (e.g., that we have analyzed each user's suitability)?**

**Unblocks:** Risk-gate UI copy; methodology page; Risk Disclosure finalization.

### 3.3 [P1] §8 Capital Cap and phased ramp

> Real-capital deployment is gated by code-level enforcement until PCC v2 §8 Capital Cap criteria pass. Even after pass, deployment opens through a phased ramp.

**Question for counsel:**

Q-Auto-6. **Does the §8 Capital Cap framework's existence (and its public publication) create regulatory expectations or carry legal implications we should be aware of?**

Q-Auto-7. **Does publishing the phased-ramp schedule constitute a "performance projection" or "track-record commitment" in any jurisdiction?**

Q-Auto-8. **At the moment §8 passes and real-capital deployment opens through phased ramp, what counsel review pass is required?**

**Unblocks:** PCC v2 page; Validation_Phase_Exit_Memo language; first phased-ramp comms.

### 3.4 [P1] User-authorized execution

> The product does not execute autonomously. The user authorizes each trade. The engine outputs are decision-support, not orders.

**Question for counsel:**

Q-Auto-9. **What language explicitly confirms the user-authorized model in pricing, ToS, and risk disclosure?**

Q-Auto-10. **At what point would adding any auto-execution feature (e.g., user-authorized standing rules that fire automatically) require regulatory review?**

**Unblocks:** Engine API descriptions; Telegram alert templates; finalization of ToS.

---

## 4. Signals and decision support questions

Counsel must opine on the regulatory characterization of signal output formats and surfaces.

### 4.1 [P1] Signal output format (CA-7)

> Each signal carries: symbol, direction, entry, regime label (Trending / Mean-Reverting / Volatile / Quiet), confidence score, gate result (pass / rejected), position-sizing rationale.

**Question for counsel:**

Q-Sig-1. **Is the signal output format a "personalized investment recommendation" given that it is calibrated to the user's risk-gate configuration?**

Q-Sig-2. **Does the inclusion of confidence scores or sizing rationale make the output more or less likely to be characterized as advice?**

Q-Sig-3. **Are there alternative signal-output framings that reduce regulatory characterization risk while preserving the product's value?**

**Unblocks:** Signal payload schema; Telegram alert template; in-product signal cards.

### 4.2 [P1] Free vs. paid signal differentiation

> Free tier shows top-5 delayed signals (daily refresh) with regime label only (no confidence). Paid tiers show full-fidelity real-time signal feed with full output.

**Question for counsel:**

Q-Sig-4. **Does providing a curated signal subset on the Free tier change the product's regulatory characterization (e.g., shifting from "tools" to "signal service")?**

Q-Sig-5. **Does the "delayed daily refresh" mechanism reduce regulatory exposure compared to real-time delivery?**

**Unblocks:** Free tier Scope B implementation; tier comparison copy.

### 4.3 [P1] Methodology page disclosure

> `coinscope.ai/methodology` documents the engine logic, regime classifier, position-sizing math, and vendor stack reasoning. It is publicly accessible regardless of tier.

**Question for counsel:**

Q-Sig-6. **Does educational disclosure of the engine's logic constitute "investment education" with associated regulatory implications, or is it product methodology disclosure?**

Q-Sig-7. **What surface-level disclaimers are required on the methodology page?**

**Unblocks:** Methodology page finalization; Substack content cadence.

---

## 5. Billing and subscription questions

Counsel must opine on billing, refund, founder-cohort, and discount mechanics.

### 5.1 [P1] Refund policy (CA-10)

> 14-day money-back guarantee on first paid charge, single-use per account/email/payment method. After 14 days, no refunds; cancel-at-renewal applies.

**Question for counsel:**

Q-Bill-1. **Is the 14-day money-back, single-use enforcement mechanism (account/email/payment method, whichever more restrictive) defensible against UAE consumer-protection standards and EU/UK consumer-rights baseline?**

Q-Bill-2. **Are there jurisdictions where a 14-day window is insufficient (e.g., 30-day legal minimum)?**

Q-Bill-3. **Does the anti-stacking enforcement (one promo code per subscription) raise consumer-protection concerns?**

**Unblocks:** Pricing page refund language; ToS finalization.

### 5.2 [P1] Founder-cohort framing (CA-11)

> Founder-cohort pricing applies to first 60 days post-public-launch (P2). Discount is ≈25–30%. Locks through one renewal cycle, then standard pricing applies.

**Question for counsel:**

Q-Bill-4. **Is "founding-member pricing — locked through your first renewal cycle, then standard pricing applies" defensible against permanent-discount-implication claims?**

Q-Bill-5. **Are there jurisdictions where the time-bounded promo language is required to be more explicit (e.g., "promotional pricing valid until [DATE]; standard pricing of $X applies thereafter" disclosed at signup)?**

Q-Bill-6. **What protections exist for the first-renewal user who is surprised by the standard price (despite the time-bounded language)?**

**Unblocks:** Founder-cohort messaging; pricing page; renewal email language.

### 5.3 [P1] Annual prepay (CA-12)

> Annual prepay carries ≈17% discount. Refunds pro-rated only within the 14-day window; locked for the term thereafter.

**Question for counsel:**

Q-Bill-7. **Does annual prepay locking after the 14-day window comply with consumer-protection norms in our target jurisdictions?**

Q-Bill-8. **Are mid-term cancellation requests handled defensibly given the locked-term posture?**

**Unblocks:** Annual prepay marketing; ToS finalization.

### 5.4 [P1] Stripe billing posture (CA-9)

> Stripe handles billing for all tiers in P1 with UAE entity support. Promo codes implement founder-cohort time-bounding. Per-seat invoicing supported via Stripe quantity-based subscriptions at Desk Full v2.

**Question for counsel:**

Q-Bill-9. **Is Stripe ToS coverage adequate for our jurisdictional mix (UAE / MENA / global EN, US blocked)?**

Q-Bill-10. **What additional billing-platform considerations apply when we cross the VAT threshold or expand jurisdictionally?**

Q-Bill-11. **Does Paddle (merchant-of-record) or another platform offer more compliance-favorable handling for our model post-threshold?**

**Unblocks:** Pre-P1 payment flow; per-seat invoicing implementation; post-VAT-threshold migration evaluation.

---

## 6. Claims and marketing questions

Counsel must opine on what we can and cannot say in public-facing surfaces.

### 6.1 [P1] Anti-overclaim discipline (CA-13)

> No performance language, no leaderboards, no testimonials presented as endorsement, no urgency theatre. Locked phrasing per `13-support-and-trust-ops/public-claims-guardrails.md`.

**Question for counsel:**

Q-Claim-1. **Does the anti-overclaim discipline provide legal cover against advisory / promissory claims, or is the discipline a marketing-restraint that does not affect regulatory characterization?**

Q-Claim-2. **What additional language or surface-level disclaimers reduce regulatory exposure beyond what the anti-overclaim discipline provides?**

Q-Claim-3. **Are there phrases on the approved-claim list that you would flag for revision?**

**Unblocks:** Brand-voice enforcement skill calibration; pricing-page polish; launch announcement language.

### 6.2 [P2] Cohort observation summaries (CA-14)

> Quarterly anonymized cohort summaries describe usage patterns (rule-respect, retention bands, edge cases). No per-user numbers, no aggregate return figures, no performance language.

**Question for counsel:**

Q-Claim-4. **Are cohort observation summaries (anonymized, structural, no performance numbers) operational disclosures or regulated marketing claims?**

Q-Claim-5. **What anonymization standard is required for cohort data to qualify as operational disclosure?**

Q-Claim-6. **Is publishing usage patterns ("P1 cohort users configure custom risk-gate thresholds in Week 1") a marketing claim that requires substantiation?**

**Unblocks:** Quarterly cohort summary template; first publication.

### 6.3 [P1] AI claims (CA-13 sub-area)

> The product uses a v3 ML regime classifier and minimal Claude API integration. AI claims describe engine capability (regime labels, confidence scores) without overclaiming autonomous decision-making or alpha generation.

**Question for counsel:**

Q-Claim-7. **What AI claims are safe to make in our target jurisdictions?**

Q-Claim-8. **Does mentioning specific model providers (e.g., "Claude API for narrow analytical tasks") create vendor-relationship implications we should be careful of?**

Q-Claim-9. **At what point would AI claims drift toward "automated decision-making" framing that triggers EU AI Act / similar regulatory exposure?**

**Unblocks:** Methodology page; Substack content; pitch deck AI claims.

### 6.4 [P2] Press / op-ed placements

> One press placement at P2 launch; founder POV op-eds at quarterly cadence in methodology-aligned outlets.

**Question for counsel:**

Q-Claim-10. **What review cadence for press placements is required given the product's regulatory sensitivity?**

Q-Claim-11. **Does naming the founder (Mohammed) in press coverage create individual-liability exposure beyond company-level?**

**Unblocks:** P2 launch press placement; founder POV cadence.

---

## 7. Jurisdiction-sensitive questions

Counsel must opine on jurisdiction-specific risks and obligations.

### 7.1 [P1] UAE primary posture (CA-1)

> CoinScopeAI is operated as a UAE sole prop by the founder. Target users include UAE/MENA + global EN.

**Question for counsel:**

Q-Jur-1. **Is sole-prop operating posture sufficient for the validation phase (P0–P1) given our target user mix?**

Q-Jur-2. **Are there UAE virtual-asset regulatory developments (VARA, ADGM, DFSA) we should be tracking that could classify CoinScopeAI as advisory or broker?**

Q-Jur-3. **Should we engage with VARA or ADGM proactively, or maintain a "tools, not advice" posture without sandbox engagement?**

**Unblocks:** P1 launch; pre-P2 entity decision sequencing.

### 7.2 [P1] Post-validation entity restructure (CA-2)

> Strategic Priority 6: counsel-recommended entity (DMCC FZE / mainland LLC / other) before any structured raise.

**Question for counsel:**

Q-Jur-4. **What entity formation jurisdiction (DMCC, ADGM, mainland, other) best fits our operating posture, target users, and post-validation roadmap?**

Q-Jur-5. **What is the cost and timeline for entity formation, and what triggers a cost spike (e.g., licensing-required entity)?**

Q-Jur-6. **Does the entity decision affect our advisory-line characterization (e.g., a regulated entity might force advisory licensing)?**

**Unblocks:** Post-P0 entity decision; pre-fundraise structure; vendor master-services contracts.

### 7.3 [P1] US-block enforcement (CA-18)

> US-residents blocked at signup via multi-layer geo-detection (IP + KYC declaration + ban-and-refund flow).

**Question for counsel:**

Q-Jur-7. **Is the multi-layer US-block enforcement sufficient pre-licensure?**

Q-Jur-8. **What additional enforcement measures (e.g., periodic re-verification, sanctions-list screening) are required?**

Q-Jur-9. **What is the proper response if a US-resident bypasses the block (e.g., via VPN)?**

**Unblocks:** Pre-P1 signup flow; ban-and-refund SOP; ongoing US-block discipline.

### 7.4 [P1] EU/UK exposure (CA-1 sub-area)

> Some target users are EU/UK residents (global EN-fluent). MiFID, MAR, EU AI Act, GDPR are relevant.

**Question for counsel:**

Q-Jur-10. **Does the EU/UK user mix create any specific regulatory exposure beyond the UAE primary posture?**

Q-Jur-11. **What GDPR-specific obligations apply (DPA, data-subject rights, cross-border transfer mechanisms)?**

Q-Jur-12. **Does MiFID II or similar regimes create characterization risk for our signal output?**

**Unblocks:** Privacy Policy finalization; DPA scope; pre-P2 EU/UK posture.

### 7.5 [P2] GCC cross-border VAT (CA-3, CA-4)

> KSA, Bahrain, Oman have separate VAT regimes. We are below UAE VAT threshold at v1; cross-border GCC obligations apply only if specifically registered there.

**Question for counsel:**

Q-Jur-13. **At what revenue / user-mix threshold does GCC cross-border VAT registration become operationally required?**

Q-Jur-14. **Are there enforcement risks from GCC users without specific in-jurisdiction registration?**

**Unblocks:** Post-P2 MENA expansion sequencing; AED display copy; cross-border revenue tracking.

### 7.6 [P5] Multi-jurisdiction expansion at Desk Full v2

> Desk Full v2 may attract small-fund and family-office buyers in jurisdictions beyond UAE/MENA (e.g., Singapore, Switzerland, Malta).

**Question for counsel:**

Q-Jur-15. **Does the Desk Full v2 audit-grade reporting capability create jurisdictional exposure in any of these markets?**

Q-Jur-16. **What jurisdictional expansion review is required pre-P5?**

**Unblocks:** Pre-P5 launch readiness; Desk Full v2 audit-grade reporting language.

---

## 8. Launch-timing questions

Counsel must opine on what is required for each launch event.

### 8.1 [P1] Pre-P1 launch readiness

**Question for counsel:**

Q-Launch-1. **What is the minimum counsel-cleared documentation set required before P1 cohort opens (2026-06-01)?**

Q-Launch-2. **Is the Counsel Brief Phase A scope (ToS, Privacy Policy, Risk Disclosure, No-Investment-Advice memo, entity-formation recommendation) the correct minimum, or should additional items be added?**

Q-Launch-3. **What ongoing counsel-review SLA applies during P1 cohort observation?**

**Unblocks:** P1 launch; pre-P1 readiness review meeting.

### 8.2 [P2] Pre-P2 public launch readiness

**Question for counsel:**

Q-Launch-4. **What additional counsel review is required before public launch (Aug–Sep 2026)?**

Q-Launch-5. **Does the public launch announcement require counsel review?**

Q-Launch-6. **At what point does P2 public launch trigger jurisdictional-specific marketing review?**

**Unblocks:** P2 launch; launch announcement; one optional ≤25%/≤30-day promo language.

### 8.3 [P5] Pre-P5 Desk Full v2 launch readiness

**Question for counsel:**

Q-Launch-7. **What audit-grade reporting language is defensible at Desk Full v2?**

Q-Launch-8. **Does per-seat partner read-only / analyst seat structure require additional terms or addenda?**

Q-Launch-9. **Does Desk Full v2's positioning toward solo PMs trigger any new advisory characterization questions?**

**Unblocks:** Pre-P5 launch readiness; Desk Full v2 marketing.

### 8.4 [Continuous] Post-launch counsel touch points

**Question for counsel:**

Q-Launch-10. **What incidents require immediate counsel notification (security; refund disputes; regulator inquiries; brand-voice violations)?**

Q-Launch-11. **What quarterly review cadence is reasonable for ongoing counsel oversight?**

**Unblocks:** Ongoing operations; incident-comms templates finalization.

---

## 9. Question priority summary

| Priority | Count | Where to find |
|---|---|---|
| **[P1]** Pre-P1 launch (by mid-May 2026) | ~30 questions | §§ 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 5.1, 5.2, 5.3, 5.4, 6.1, 6.3, 7.1, 7.2, 7.3, 7.4, 8.1 |
| **[P2]** Pre-P2 public launch (by Aug–Sep 2026) | ~6 questions | §§ 6.2, 6.4, 7.5, 8.2 |
| **[P5]** Pre-P5 Desk Full v2 launch (by Mar–May 2027) | ~4 questions | §§ 2.4, 7.6, 8.3 |
| **[Continuous]** Quarterly review | ~2 questions | § 8.4 |

---

## 10. How to send to counsel

When the engagement starts:

1. **Send `Counsel_Brief_v2.md`** as the primary engagement document.
2. **Attach this file** as the structured question list.
3. **Attach `compliance-assumptions.md`** as the assumption tracking.
4. **Attach `No_Investment_Advice_Memo_v0_DRAFT.md` and `Risk_Disclosure_v0_DRAFT.md`** as draft documents for review.
5. **Confirm Phase A scope** (ToS, Privacy Policy, Risk Disclosure, No-Investment-Advice memo, entity-formation recommendation) and 4–6 week target delivery.
6. **Schedule pre-P1 readiness review meeting** within 30 days of engagement start.

The engagement budget per Counsel Brief: **USD $10,000–$15,000 mid-tier UAE / regional firm** for Phase A.

---

## 11. Cross-references

- Counsel Brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- No Investment Advice memo (DRAFT): `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`
- Risk Disclosure (DRAFT): `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- Compliance assumptions: `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`
- Business risk register: `business-plan/14-risk-compliance-and-safeguards/business-risk-register.md`
- Safeguards framework: `business-plan/14-risk-compliance-and-safeguards/safeguards-framework.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Strategic Priority 6 (entity decision): `business-plan/01-executive-summary/strategic-priorities.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
