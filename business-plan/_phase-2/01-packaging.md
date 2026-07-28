# 01 — PACKAGING

**Workstream:** PACKAGING
**Phase:** 2 — Monetization
**Status:** Path A activated 2026-05-04. Canonical task list absorbed verbatim from `_phase-2-pending/packaging-canonical-list.md`.
**Canonical authorities:** v1 framework `06-pricing-monetization.md` (Track B, Free Scope B, Model C hybrid), `05-product-strategy.md`; Phase 1 PRODUCT outputs (Product Value Ladder, MVP/Beta/Scale Feature Matrix, Decision Pr-4).

---

## 1. Purpose

Lock the **commercial offer surface**: how the product is sliced into tiers, what is Free vs Paid, what gating rules apply per feature, and how the offer is communicated on the pricing page. PACKAGING translates §6 v1 monetization model + Phase 1 PRODUCT lifecycle into a buyer-facing structure.

## 2. Why this matters specifically for CoinScopeAI

- **Tier count is high-leverage.** Track B canonical (Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199) is committed at v1 but the *boundary lines* and *gating types* are not. Wrong boundaries kill conversion (too tight) or pricing power (too generous).
- **Anti-overclaim discipline is operational here.** Pricing-page tier descriptions must visually surface "stabilizing in cohort" status (per §6.10 Flag 2) — packaging is the surface where overclaim leaks first.
- **§3.5 sub-$5k "we'll be back" is a packaging decision dressed as a marketing decision.** Free Scope B (locked) sets up the funnel; gating rules + comparison-table copy execute it.
- **Per-seat structure on Desk Full v2 ($149 / $249) is the largest pricing-power asymmetry in the model** (§6.2 P3 carries 5–10x per-user revenue). Get gating right or leave revenue on the table.
- **Anti-friction packaging is a trust signal** in a category that engineers friction (lock-in, surprise charges, downgrade restrictions). Codifying anti-patterns up-front is positioning, not paperwork.

## 3. Required subsections

1. **Tier structure** — count, naming, gating, ratify-or-revise of Track B.
2. **Free vs Paid feature boundary** — every feature explicitly Free / Paid / Tier-specific. Operationalizes Phase 1 Decision Pr-4.
3. **Plan comparison table** — pricing-page surface, consistent with value ladder + feature matrix.
4. **Premium feature gating rules** — per-feature gating type: hard / soft / degraded / read-only.
5. **Packaging friction review** — competitive anti-pattern catalogue + packaging design rules.
6. **Beta-access offer design** (NEXT) — P0 → P1 cohort transition terms.
7. **Fund / Desk plan concept** (NEXT) — Phase 5 input, no commitments.
8. **Usage add-on concepts** (NEXT) — shape of add-ons to keep core tiers stable.
9. **Billing-to-entitlement logic review** (NEXT QA) — entitlement audit.
10. **Upgrade path design** (NEXT) — in-product flow + pro-rated billing + downgrade rules.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Tier Structure Recommendation | MD; signed by founder | Founder + Strategy CoS |
| Free vs Paid Feature Boundary | MD with feature-by-feature tag | Strategy CoS + Eng lead |
| Plan Comparison Table v1 | MD render-ready for pricing page | Strategy CoS + Design |
| Premium Feature Gating Rules | MD with hard/soft/degraded/read-only per feature | Eng lead + Strategy CoS |
| Packaging Friction Review | MD anti-pattern catalogue | Strategy CoS |
| Beta Access Offer Design | MD with eligibility + expiration | Founder |
| Fund / Desk Plan Concept | MD; *no commitments* tag | Founder |
| Usage Add-On Concepts | MD with pricing-model per add-on | Founder + Eng lead |
| Billing-to-Entitlement Audit Report | MD audit + remediation backlog | Eng lead |
| Upgrade Path Design | MD with flow diagrams + edge cases | Design + Eng lead |

## 5. Assumptions to validate

1. **ASSUMPTION** — Track B four-tier structure (Free / Trader / Desk Preview / Desk Full v2) is the right shape. P0 cohort exit memo is the validation instrument.
2. **ASSUMPTION** — Free Scope B (account-verified, no paid-feature exceptions, "we'll be back" messaging for sub-$5k) drives Free → Trader conversion at the §6.9 base case of 5% over 90 days.
3. **ASSUMPTION** — Per-seat density at Desk Full v2 averages 2.5 seats per account (§6.9 base case). Sensitivity flagged as #1 most-impactful in financial model.
4. **ASSUMPTION** — Soft gating (graceful degradation + upgrade prompt) is the trust-aligned default; hard gating reserved for execution-adjacent features and risk-gate configurability.
5. **ASSUMPTION** — Plan comparison table reads cleanly with 4 tiers + 1 per-seat add-on row. If 4 tiers crowd the page, Desk Full per-seat moves to a "Team plans" sub-section.

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **Pk-1** | Tier structure ratify or revise Track B | (a) Ratify Track B as-is. (b) Collapse Desk Preview into Desk Full v2 (3-tier). (c) Add Trader Annual-only sub-tier. | Founder | After P0 cohort exit memo | §11 financial model, pricing page, §9 messaging |
| **Pk-2** | Free vs Paid boundary final form | (a) §6.5 Scope B as-locked (top-5 delayed signals + regime label, no journal). (b) Scope B + post-validation journal-read-only exception. (c) Tighter — drop the regime label. | Founder | Before pricing-page lock | Funnel conversion rate, §13 KPIs |
| **Pk-3** | Per-seat $149 / $249 split lock | (a) Ratify $149 partner read-only / $249 analyst. (b) Single $199 seat (no role split). (c) $99 / $199 (lower friction, higher per-seat density). | Founder | Phase 2 Q3 | §11 sensitivity #1 (per-seat density) |
| **Pk-4** | Gating type default | (a) Soft + upgrade-prompt (trust-aligned). (b) Hard gate (revenue-protective). (c) Degraded read-only on downgrade. | Founder + Design | Before gating rules ship | UX trust signal, churn rate |
| **Pk-5** | Plan comparison table form | (a) 4-tier horizontal grid. (b) 3-tier with Desk Full as "Team" sub-section. (c) 4-tier collapsed-feature-rows + expand-on-hover. | Design + Strategy CoS | Before pricing-page v1 | Pricing-page conversion |
| **Pk-6** | Beta-access offer form | (a) Founder-cohort pricing automatic for P0. (b) +30 days extension at P0 grandfathered Trader. (c) Free Trader for first 90 days of P1. | Founder | Before P0 → P1 transition | Cohort conversion, founder-cohort comms |

## 7. Failure modes to avoid

- **Tier sprawl.** Adding a fifth tier "to capture middle willingness-to-pay." Compresses pricing power and creates analysis paralysis at signup. Hold to 4 tiers + per-seat add-on.
- **Hidden gating.** Discovering on the dashboard that a feature is paid after the user already started using it. Read as bait-and-switch even if technically correct. Every gated feature must surface gating *before* the user touches it.
- **Pricing-page overclaim.** "Full dashboard access" copy on Trader while §5.2.3 IB items are "stabilizing in cohort." Per §6.10 Flag 2 — stabilizing status must be visible on the pricing page next to the price.
- **Free → Trader prompt fatigue.** Aggressive upgrade prompts on Free are user-hostile and counter-position the brand. Single quiet prompt per session, never blocking.
- **Founder-cohort drift to "lifetime."** Per §6.10 Flag 1 — never use "lifetime / forever / always / locked-in" language. "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies."
- **Per-seat invoicing surprise.** Adding a partner seat must show the pro-rated charge and next-renewal recurring charge before the user confirms. Stripe-native quantity-based subscription handles this; the UX must surface it.
- **Anti-ICP bundling leak.** Per §5.3.3 — no co-marketing or bundled promotions with signal groups, copy-trade products, or leverage maximizers. Even adjacent affiliate links read as endorsement.
- **Entitlement drift.** Stripe says Trader, feature flag says Desk Preview (or vice versa). Most-expensive packaging failure mode — revenue loss + support load + trust hit. `[QA] PACKAGING — Billing-to-Entitlement Logic Review` runs before any pricing change ships.

## 8. Tasks (canonical list — verbatim)

### NOW

**`[DOC] PACKAGING — Tier Structure Recommendation`**
- **Objective:** Recommend the tier structure (count, gating, naming) for the P1+ commercial product, anchored to the locked Product Value Ladder. Ratifies or revises v1 Track B (Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199).
- **Why:** Tier count is a high-leverage decision. Too many tiers = analysis paralysis at signup; too few = pricing compression. The recommendation is the input to every other PACKAGING task.
- **Dependency:** Product Value Ladder (Phase 1 PRODUCT NOW); ICP Definitions v1; v1 framework `06-pricing-monetization.md` (Track B canonical).
- **Output:** Tier structure recommendation MD; signed; feeds Decision Register entry **Pk-1**.

**`[DOC] PACKAGING — Free vs Paid Feature Boundary`**
- **Objective:** Lock the precise boundary between Free and the lowest paid tier (Trader $79). Resolves Phase-1 open question PrQ-1 ("Free demonstrates the gate without substituting for Trader") at the operational level.
- **Why:** Free-tier shape is the funnel valve. Wrong shape kills either acquisition (too tight) or conversion (too generous). Phase 1 Decision Pr-4 is recommended at "top 10 + 15-min delay" — Phase 2 ratifies, revises, or A/B tests.
- **Dependency:** MVP vs Beta vs Scale Feature Matrix (Phase 1 PRODUCT NOW); Product Value Ladder; Phase 1 Decision Register entry Pr-4.
- **Output:** Free vs Paid boundary MD — every feature explicitly tagged Free / Paid / Tier-specific. Feeds **Pk-2**.

**`[DOC] PACKAGING — Plan Comparison Table v1`**
- **Objective:** External-facing plan comparison table for the pricing page (Free / Trader / Desk Preview / Desk Full v2 + per-seat).
- **Why:** Plan comparison is one of the highest-leverage conversion surfaces. Consistency with the value ladder and feature matrix is non-negotiable; drift here misrepresents the product.
- **Dependency:** Tier Structure Recommendation; Product Value Ladder; Free vs Paid Feature Boundary; Phase 1 POSITIONING Surface Variant Table.
- **Output:** Plan comparison table MD; ready to render on the pricing page; pairs with Phase 1 BRAND `Website Copy Structure` (NEXT). Feeds **Pk-5**.

**`[DOC] PACKAGING — Premium Feature Gating Rules`**
- **Objective:** Define the gating logic for premium features — what triggers an upgrade prompt, what gracefully degrades, what's hard-gated.
- **Why:** Soft vs hard gating is a UX trust signal. Aggressive gating reads as user-hostile (counter-positioning to anti-overclaim brand); soft gating leaves revenue on the table. Each feature needs an explicit gating type.
- **Dependency:** Free vs Paid Feature Boundary; Tier Structure Recommendation; Phase 1 Product Scope Guardrails (PRODUCT NEXT).
- **Output:** Gating rules MD with feature-by-feature gating type (hard / soft / degraded / read-only). Feeds **Pk-4**.

**`[RESEARCH] PACKAGING — Packaging Friction Review`**
- **Objective:** Review existing crypto-trading-tool packaging for the most common friction points (lock-in, surprise charges, feature withholding, downgrade restrictions, opaque billing).
- **Why:** Anti-friction packaging is itself a trust signal in a category that frequently engineers friction. Codifying anti-patterns up-front prevents drift toward category packaging debt.
- **Dependency:** v1 framework `06-pricing-monetization.md`; competitive intelligence pass.
- **Output:** Friction review MD — anti-pattern list + packaging design rules.

### NEXT

**`[DOC] PACKAGING — Beta Access Offer Design`**
- **Objective:** Design the offer for the P0 → P1 transition cohort (e.g., grandfathered Trader pricing, founder-cohort discount, free-extension).
- **Why:** Beta-access offers reward early users without setting bad pricing precedents. Needs explicit design — ad-hoc offers create entitlement disputes later.
- **Dependency:** Tier Structure Recommendation; Cohort exit memo; Phase 2 pricing direction.
- **Output:** Beta access offer MD — terms, eligibility criteria, expiration rules, prorated migration. Feeds **Pk-6**.

**`[DOC] PACKAGING — Fund/Desk Plan Concept`**
- **Objective:** Sketch the Fund / Desk plan concept (Desk Full v2 $1,199 + per-seat at $149 or $249) for Phase 5 ramp.
- **Why:** Concept-only in Phase 2; Phase 5 charter input. Concepts now reduce Phase-5 ramp time and pre-empt premature Desk Full sprawl.
- **Dependency:** Layla Phase-5 Pre-read (ICP LATER); Team and Fund Product Variant Concept (PRODUCT LATER).
- **Output:** Fund/Desk plan concept MD; *no commitments*.

**`[DOC] PACKAGING — Usage Add-On Concepts`**
- **Objective:** Catalogue usage-based add-on candidates (custom thresholds, API access tier, additional venues post-Bybit, extra Telegram routing, per-seat additions).
- **Why:** Usage add-ons let core tiers stay simple while power users pay more. Deciding the *shape* of add-ons in Phase 2 keeps the core tier matrix stable through Phase 3+.
- **Dependency:** Tier Structure Recommendation; Karim API Surface Scoping (deferred PRODUCT LATER).
- **Output:** Add-on concepts MD — each concept's pricing model (flat / metered / overage).

**`[QA] PACKAGING — Billing-to-Entitlement Logic Review`**
- **Objective:** Walk every entitlement (feature flag, tier check, upgrade prompt, downgrade revocation) and verify it correctly reflects the locked tier structure and gating rules.
- **Why:** Entitlement drift is the single most expensive packaging failure mode (revenue loss + support load + trust hit). Audit before any pricing change ships.
- **Dependency:** Premium Feature Gating Rules; Stripe integration; current product feature flags.
- **Output:** Audit report; remediation backlog if any.

**`[DOC] PACKAGING — Upgrade Path Design`**
- **Objective:** Design the in-product upgrade path — when prompts appear, how the upgrade flow works, prorated billing, downgrade rules, refund/credit policy.
- **Why:** Upgrade path UX shapes ARR. Ad-hoc designs leak conversions and create churn surface.
- **Dependency:** Premium Feature Gating Rules; Tier Structure Recommendation; Stripe billing flows.
- **Output:** Upgrade path design MD with flow diagrams + edge-case rules.

### LATER

**`[DOC] PACKAGING — High-Touch White-Glove Onboarding Offer`**
- **Objective:** Sketch a high-touch onboarding offer (e.g., for Desk Full v2 buyers or larger-book traders) — what it includes, what it costs, who delivers it.
- **Why:** Phase 5 input. Small books / funds expect high-touch, but it's a margin trap if mispriced or under-staffed.
- **Dependency:** Fund/Desk Plan Concept; Enterprise Buyer Readiness Notes (ICP LATER).
- **Output:** Concept MD; *no commitments*.

**`[DOC] PACKAGING — API/Data Product Packaging Concept`**
- **Objective:** Concept the API / data product as a separate packaged offering (e.g., Karim P2 API surface; risk-as-a-service).
- **Why:** Phase 3+ input. Bounds future scope discussion without committing. Keeps the core PACKAGING surface clean (API as a *separate* product, not a tier add-on, if that proves correct).
- **Dependency:** Karim API Surface Scoping (deferred); Expansion Opportunities Beyond Core Trading Intelligence (PRODUCT LATER).
- **Output:** Concept MD; *no commitments*.
