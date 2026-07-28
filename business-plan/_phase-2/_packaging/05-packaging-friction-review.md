# PACKAGING — Packaging Friction Review

**Task:** `[RESEARCH] PACKAGING — Packaging Friction Review`
**Type:** NOW
**Owner:** Strategy CoS
**Status:** DRAFT v0.1 — anti-pattern catalogue + design rules. Inferences on competitor behavior labeled as such.
**Anchored to:** v1 framework `06-pricing-monetization.md` §6.1 comp landscape; Phase 1 BRAND voice (anti-overclaim, methodical); §5.3.3 packaging principles (no lifetime, no grandfather, no "Premium/Pro," no anti-ICP bundling).

---

## 1. Why a friction review is itself a packaging decision

Crypto trading tools and adjacent SaaS routinely engineer friction into pricing and packaging — surprise charges, downgrade restrictions, opaque billing, lifetime-deal entrapment, withholding of basic data. The category trains buyers to expect adversarial packaging. Codifying anti-patterns up-front is a positioning act: CoinScopeAI's "anti-overclaim, capital-preservation-first" stance is incoherent if it ships with industry-standard packaging hostility.

This review catalogues the friction patterns observed across the §6.1 comp set, marks each as **disallowed / disallowed-conditional / allowed**, and translates the disallowed list into design rules.

**Method:** scanned the §6.1 comp set (TradingView, 3Commas, Cryptohopper, Glassnode, Nansen, CoinGlass, CryptoQuant, vectorbt PRO, Tradervue, prop-firm subs). Patterns are inference from public pricing pages, terms-of-service excerpts, and user-reported behavior in public forums. Where I cannot directly verify, I mark **INFERENCE** rather than asserting.

---

## 2. Anti-pattern catalogue

### Class A — Pricing-page deception

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| "Starting at" / "as low as" pricing without showing the actual common-case price | Common across crypto bot platforms | User has to commit before the real price surfaces | **Disallowed.** Single-number pricing per tier, monthly + annual + founder-cohort all visible. |
| Usage-based pricing without an estimator | Some quant / data tools | User cannot predict their bill | **Disallowed for v1.** Track B is flat subscription + per-seat. Per-seat is a single deterministic number, not metered usage. |
| Annual price displayed as monthly equivalent without the actual annual figure | Common across SaaS | Anchors the smaller number; obscures the commitment | **Disallowed.** Both monthly and total annual visible. "$790/yr ($66/mo equivalent)." |
| "Most popular" / "Best value" badges driving toward higher tier | Common across SaaS | Pressure-driven selection rather than fit-driven | **Disallowed** (per `03-plan-comparison-table-v1.md` §6 visual rules). User picks tier that fits their trading. |
| Hidden enterprise pricing requiring a sales call | Crypto on-chain analytics tier-3 (Nansen Alpha, Arkham Ultra) | Forces friction-rich procurement | **Disallowed for Track B.** Desk Full v2 publishes its base price ($1,199) and per-seat add-ons ($149/$249) openly. "Talk to founder" is the CTA, not a price-discovery gate. |
| Strikethrough "regular price" anchoring (e.g., "~$199~ $99 today!") | Crypto bot platforms; some signal services | Manufactured discount theater | **Disallowed.** No strikethrough pricing. Founder-cohort is shown as a separate row, not a discount on the main price. |
| Currency switching without exchange-rate transparency | Common globally | Hides FX margin | **Allowed-conditional.** AED courtesy display is at fixed peg (USD/AED 3.673); footer states "Approximate AED equivalent — billed in USD." Per §6.8 + §6.10 Flag 3. |

### Class B — Lock-in mechanics

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| "Lifetime" / "founder forever" deals | Crypto bot platforms; signal-group tier | Sets unsustainable obligations; cannibalizes future revenue; produces legacy-customer friction at every pricing change | **Disallowed.** Per §5.3.3 packaging principle + §6.10 Flag 1. Founder-cohort is **time-bounded**, locked through one renewal cycle. |
| Non-cancellable annual subscriptions | Common across SaaS | Forces full-term billing even after dissatisfaction | **Disallowed.** Cancel anytime; effective at end of current billing period. 14-day refund window for first-time annual per §6.7. |
| Pro-rated refunds disallowed even within 14 days | Some SaaS | Punishes early dissatisfaction | **Disallowed.** 14-day money-back guarantee for first-time paid customers (§6.7), pro-rated within window. |
| Auto-renewal without notification | Common across SaaS | Surprise billing | **Disallowed.** Pre-renewal notification 7 days prior for monthly, 30 days prior for annual. (REQUIRED INPUT — confirm Stripe configuration supports.) |
| Reactivation requires re-signup at new pricing within short window | Common across SaaS | Punishes brief lapses | **Allowed-conditional.** Per §6.7: 90-day window restores prior tier and pricing. After 90 days → standard pricing (founder-cohort not re-extended). 90 days is generous by category norms. |
| Data export gated by active subscription | Some SaaS | Holds user data hostage | **Disallowed.** Journal export and account data export remain available for 30 days post-cancellation per §6.7 + `04-premium-feature-gating-rules.md` §4. |

### Class C — Feature withholding

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| Basic features (e.g., dark mode, 2FA, basic alerts) gated behind paid tiers | Some SaaS | Treats baseline UX as upsell | **Disallowed.** UX baseline (theme, 2FA, password reset, account deletion) is universal. Paid features are functional differentiation, not UX. |
| Trial that auto-converts to paid without active opt-in | Common across SaaS | Surprise charge | **Disallowed by structure.** No free trial — Free is permanent at Scope B. Trader requires deliberate purchase, no card-on-file pre-purchase. |
| "Limited" Free tier with arbitrary low usage caps designed to force upgrade | Common across freemium SaaS | Free is theatre | **Disallowed.** Free Scope B is genuinely useful: top-5 delayed signals + regime label + demo-trade gate behavior + methodology docs. Permanent, not time-limited, not usage-capped. |
| Soft-disabled features shown as "available" but actually requiring upgrade clicks to discover | Common | Bait-and-switch | **Disallowed.** Per `04-premium-feature-gating-rules.md` §1: feature visibility matches feature accessibility. Hard-gated features don't render at all. Soft-gated features show their tier inline. |
| Region restrictions discovered after sign-up | Common across global SaaS | Wasted onboarding | **Disallowed.** US-blocked region check happens at signup (per memory `project_jurisdictional`); copy is "This region is not currently supported" before any account creation friction. |

### Class D — Per-seat / team-plan friction

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| Per-seat pricing without seat-removal flow | Some team SaaS | Adding is easy, removing is gated | **Disallowed.** Per-seat removal at next renewal per §6.7 mid-cycle changes; no special process. |
| Seat removal requires admin email to support | Some team SaaS | Friction-by-design | **Disallowed.** Self-serve seat management for DF account holders. |
| Per-seat charges continue after seat-holder leaves | Some team SaaS | Revenue from inactive seats | **Disallowed.** Seat removal effective at next renewal; no charge for removed seats post-removal date. |
| Different roles priced identically | Some team SaaS | Misprices both ends | **Avoided.** Per §6.6: partner read-only $149, analyst (write-privilege) $249. Role-priced. |
| Seat-tier minimums (e.g., "3-seat minimum") | Common in team SaaS | Forces over-purchase | **Disallowed.** 1 PM seat included; partner / analyst seats added one at a time. |

### Class E — Billing & dunning hostility

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| Failed-payment instant suspension with no retry | Some SaaS | Punishes transient card issues | **Disallowed.** Per §6.7 edge cases: 3 retries over 7 days; read-only "past due" state for 14 days before suspension. |
| Suspension deletes data immediately | Some SaaS | Hostage data | **Disallowed.** Suspension is read-only, not destructive. Data retained per cancellation policy (90 days). |
| Chargeback triggers permanent ban without review | Some SaaS | No due process for false-positive chargebacks | **Allowed-conditional.** Per §6.7: chargeback → immediate suspension *pending review*. Permanent ban requires review-confirmed abuse pattern. |
| Refund-then-resubscribe loop tolerated | Some SaaS | Revenue washing | **Disallowed.** Per §6.7: anti-abuse caps refunds at one per account lifetime. |
| Annual upgrade mid-cycle requires cancellation + new annual signup | Common across SaaS | Loses pro-ration benefit | **Disallowed.** Per §6.7: tier upgrades immediate with pro-rated charge. |

### Class F — Marketing / referral mechanics

| Anti-pattern | Where observed (INFERENCE) | Why it's friction | CSAI posture |
|---|---|---|---|
| Affiliate / referral programs that pay for any signup regardless of fit | Common across crypto | Drives anti-ICP traffic | **Disallowed for v1.** No referral / affiliate program until persona-fit screening can gate referral payouts. |
| Co-marketing with signal groups, copy-trade products, leverage maximizers | Common across crypto | Endorsement-by-association | **Disallowed.** Per §5.3.3 anti-ICP bundling rule. |
| "Influencer" pricing tier (free for X-followers ≥ N) | Common across crypto | Pays for adverse selection | **Disallowed.** Per §5.3.3 — no anti-ICP bundling, no influencer freebies. |
| Discount stacking across promotional channels | Common | Race-to-bottom | **Disallowed.** Per §6.7: maximum 25% discount, maximum 30-day promotional window, no stacking with founder-cohort or annual. |

---

## 3. Packaging design rules (derived from anti-pattern list)

The disallowed-list above translates into nine durable packaging design rules. These are the rules every PACKAGING decision should be tested against.

1. **Single-number pricing per tier.** Monthly, annual total, and founder-cohort visible. No "starting at." No strikethrough. No metered usage at v1.
2. **Permanent Free tier.** No time-limited trial. No usage caps that arbitrarily force conversion. Free Scope B is genuinely useful.
3. **No "lifetime," "forever," "always," "locked-in."** Founder-cohort is time-bounded and the time-bound is publicly stated.
4. **No pressure mechanics.** No "Most popular" badges. No "Limited time." No countdown timers. No upgrade interstitials between user action and result.
5. **Self-serve everything.** Cancel, refund (within 14d), upgrade, downgrade, add seat, remove seat, change billing cadence — all self-serve. Support assists, doesn't gatekeep.
6. **Data is the user's.** Export available during active subscription and for 30 days post-cancellation. Cancellation is read-only, not destructive.
7. **Region check at signup.** US-blocked check before account creation friction. No surprise restrictions discovered post-onboarding.
8. **Anti-ICP bundling forbidden.** No co-marketing with signal groups, copy-trade products, or leverage-maximizer content. No "influencer" pricing tiers. No referral / affiliate at v1.
9. **Visibility matches accessibility.** Hard-gated features don't render. Soft-gated features show their tier inline. No bait-and-switch UI.

---

## 4. Friction patterns we explicitly *allow* (with reason)

Three patterns appear superficially as friction but are load-bearing for trust or operational integrity. Documented here so they don't get re-flagged as bugs:

| Pattern | Why we allow it | Reference |
|---|---|---|
| 14-day refund cap (no refund after day 14) | Anti-abuse + anti refund-then-resubscribe loop. Cancel-anytime preserves user agency post-day-14. | §6.7 |
| 90-day reactivation window for prior tier + pricing (then standard pricing) | 90 days is generous; longer windows cannibalize founder-cohort discipline. | §6.7 |
| Region block (US blocked at signup) | Compliance posture per memory `project_jurisdictional`; UAE sole prop scope. | `project_jurisdictional` |
| Hard gate on configurable risk gate | Risk-config is execution-adjacent; misconfiguration on a real account is the highest-stakes user error. Hard gate forces deliberate tier purchase. | `04-premium-feature-gating-rules.md` §2.B |
| Validation-phase disclaimer pinned to every pricing surface | "Testnet only. 30-day validation phase. No real capital." reads as friction; it's actually an anti-overclaim trust signal. | Scoopy custom instructions; §6.10 |

---

## 5. Inference confidence and verification path

Patterns marked INFERENCE in §2 are derived from public pricing pages and user-reported behavior, not from internal documents I have access to. Confidence varies:

- **High confidence:** TradingView, Glassnode, Nansen, CoinGlass pricing-page mechanics — directly observable on their pricing pages as of late-2025.
- **Medium confidence:** Auto-renewal notification practices, refund handling — varies by region (US vs EU vs MENA) and changes over time.
- **Low confidence:** Specific chargeback / suspension behavior — inferred from forum reports and Stripe defaults; not verified per vendor.

If competitive friction posture matters for a specific PACKAGING decision (e.g., Pk-2 boundary form, Pk-6 beta-access offer), the recommended verification path is: (a) sign up for the named competitor at lowest paid tier, (b) walk the cancellation / refund / downgrade flow, (c) document actual behavior. This is a `[RESEARCH] PACKAGING — Competitive Friction Walk-throughs` follow-up that could be queued for Phase 3 if data quality becomes a blocker.

---

## 6. Open dependencies

- **REQUIRED INPUT** — Stripe pre-renewal notification configuration (7-day monthly / 30-day annual). Confirm Stripe Atlas account supports.
- **REQUIRED INPUT** — Region-block at signup implementation. Verify current product behavior matches the rule. (Eng confirm.)
- **REQUIRED INPUT** — Self-serve seat-removal flow exists in DF UX. (Eng confirm; if missing, queue under `[BUILD] PACKAGING — Self-serve Seat Management UI`.)

---

## 7. What this unlocks

- The nine design rules in §3 become the audit checklist for every PACKAGING and PRICING surface.
- `[QA] PACKAGING — Billing-to-Entitlement Logic Review` (NEXT) inherits Class B and Class E anti-patterns as failure-mode tests.
- §9 messaging matrix and pricing-page copy can be audited against §3 design rules.
- Phase 3 GTM (channel-mix selection, content) inherits §3 rules 8 (anti-ICP bundling) and 4 (no pressure mechanics) directly.
- §10 ops gets the Class E (billing & dunning) rules as the SOP baseline.
