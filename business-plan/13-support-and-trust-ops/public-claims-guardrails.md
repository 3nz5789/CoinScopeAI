# Public Claims Guardrails

**Status:** Wave 2 · v1.1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/09-brand-messaging.md`; `business-plan/06-pricing-monetization.md` §6.10 (anti-overclaim audit)
**Canonical for:** `07-packaging-and-pricing/pricing-strategy.md` §9; `08-go-to-market/trust-first-growth.md` §2; `12-onboarding-and-activation/first-value-design.md` §10
**Changelog v1 → v1.1:** Inheritance loop with `trust-first-growth.md` §2 removed (this file is canonical, not a downstream of it); §2.2 Trader stability includes the $79/mo price anchor per §6.10 Flag 2; §2.3 annual prepay phrasing matches `pricing-strategy.md` §3; §2.3 refund row includes full anti-abuse enforcement form; §3 + §4–§7 overlap resolved (Option B — §3 master short-list, deep-dives below; §3 expanded with Institutional, Automation, Model-evaluation categories; "Set it and forget it" consolidated to §5.2 only); permanently-vs-conditionally-forbidden distinction added at §3 header; §1 single-sentence rule promoted to callout; new §1.1 Scope, §1.2 Legacy surfaces, §1.3 User-generated content; new §3.7 Institutional misuse, §3.8 Automation overclaim, §3.9 Model-evaluation metrics; new §8.5 Brand-voice review log artifact, §8.6 Contractor audit cadence; surface-mapping column added to §2.4 hero variants; §6.4 path made explicit; §7.1 / §9.4 bracket-placeholder convention; §9.5 calendar example reframed gate-driven; cross-references updated.

---

## 1. Purpose

This file is the **operational discipline document for what CoinScopeAI is and is not allowed to say in public**. Every external surface — pricing page, about page, methodology docs, support replies, launch announcements, Substack posts, Twitter, Telegram alerts, conference talks, op-eds — is governed by these guardrails.

> **Single-sentence rule:** **A claim is allowed only if it is on the approved list (§2) or has passed brand-voice review; anything else is "needs review" by default.**

That is the discipline. Everything below is a refinement of that rule.

### 1.1 Scope

**Product-tier surfaces are governed by these guardrails.** Product-tier surfaces include: pricing page, about page, methodology docs, support replies, launch announcements, Substack longform, X/Twitter methodology threads, Telegram alerts, conference talks, op-eds, dashboard copy, onboarding email sequences, in-product banners. All approved canonical phrasings (§2) are product-tier voice.

**Social-tier surfaces inherit forbidden claims (§3) but may use different positive phrasings.** Social-tier surfaces (Instagram, X social posts, Threads, Facebook) are **never** used for the product-tier canonical phrasings. Copy passes brand-voice review against the social-tier register, not against the product-tier canonical. If CoinScopeAI publishes nothing on a social-tier surface (the recommended posture pre-P5), this scope question is moot.

**English-only at v1.** All approved canonical phrasings are English. Arabic and other-language content requires brand-voice + counsel review of each translation; canonical equivalents are not yet locked. Pre-v1 launch, defer non-English content. Arabic UI is deferred D8 per `01-executive-summary/strategic-priorities.md`.

### 1.2 Legacy surfaces

These guardrails apply to **all currently-accessible public surfaces, regardless of when they were authored**. A Substack draft from earlier in 2026 that's still publicly readable is a current claim by virtue of being live.

- Legacy surfaces with non-compliant claims get amended or pulled
- For substantive edits, an archive note is acceptable per `incident-communications.md` §4.7
- Pre-Wave-2 surfaces are audited at the next quarterly review and brought into compliance

### 1.3 User-generated content

Quoted user content is allowed when **all three** conditions hold:

- (a) The user has given explicit consent for the specific quote in the specific surface
- (b) The quote does not contain performance language (per §3.1 + §4)
- (c) Surrounding text does not frame the quote as endorsement

Pure attributed praise is testimonial-as-endorsement → forbidden (per §3.6).

Attributed question-being-answered is allowed under brand-voice review (the user asks "Why does the gate use 80% heat as the default?"; the founder's reply quotes the question and answers).

Anonymized quoted content ("one cohort user asked us...") follows §4.3 cohort observation rules — same anonymization standard.

---

## 2. Approved claim categories

Five categories of claims that are pre-approved when used in their canonical form. Each maps to a Wave 1 source.

### 2.1 Methodology claims — APPROVED

| Claim category | Canonical phrasing | Source |
|---|---|---|
| Risk-gate timing | "The risk gate runs before trade arming, not as a post-hoc audit." | `05-positioning/positioning-statement.md` |
| Regime classification | "Every signal carries a regime label and a confidence score." | Scoopy custom instructions |
| Position-sizing transparency | "Position sizing math is shown, not hidden." | `04-icp-and-segmentation/primary-icp.md` §4 |
| User-defined thresholds | "You configure your own thresholds above our locked floors." | `06-product-strategy/core-product-pillars.md` |
| Journal capability | "R-multiple and rule-violation reporting in the journal." | `04-icp-and-segmentation/primary-icp.md` §4 |
| Locked thresholds | "Drawdown 10% / daily loss 5% / leverage 10x / max positions 5 / heat 80%." | Scoopy custom instructions |

### 2.2 Operational claims — APPROVED

| Claim category | Canonical phrasing | Source |
|---|---|---|
| Custody | "UAE-built, custody-free by structural choice." | `01-executive-summary/business-model-summary.md` |
| Capital location | "Capital stays in your exchange account." | Locked positioning |
| Validation status | "Testnet only. 30-day validation phase. No real capital." | Scoopy custom instructions |
| Real-capital path | "Real-capital deployment opens through a phased ramp once §8 Capital Cap evidence accumulates." | PCC v2 |
| PCC reference | "We publish our Production Candidate Criteria; you can read them before signing up." | TS-C trust signal in `13-support-and-trust-ops/trust-framework.md` §3 |
| Founder identification | "Founder is named and contactable: Mohammed." | `02-company-overview/strategic-constraints.md` |
| US posture (signup form) | "Not currently available in your region." | `12-onboarding-and-activation/onboarding-strategy.md` Gate 1 |

> **Surface-mapping note (US posture):** The signup form Gate 1 uses "Not currently available in your region" (above). The `coinscope.ai/what-we-dont-do` page uses the longer "We don't operate in the US until our licensure path is decided" (per §2.5). Two phrasings for two surfaces; mapping is intentional.

### 2.3 Pricing claims — APPROVED

| Claim category | Canonical phrasing | Source |
|---|---|---|
| Founder cohort | "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies." | §6.10 Flag 1 (`06-pricing-monetization.md`) |
| Annual prepay | "Pay for 10 months, get 12 (≈17% off) — annual prepay discount." | `07-packaging-and-pricing/pricing-strategy.md` §3 |
| Currency | "USD-billed; AED equivalent shown for MENA users at the standard peg." | `06-pricing-monetization.md` §6.8 |
| Trader stability | "**Trader — $79/mo.** Includes engine API + dashboard (stabilizing in cohort during validation phase)." | `06-pricing-monetization.md` §6.10 Flag 2 |
| AED courtesy | "Approximate AED equivalent — billed in USD. UAE sole prop (Mohammed). Other GCC users responsible for any local tax obligations." | `06-pricing-monetization.md` §6.10 Flag 3 |
| Refund | "14-day money-back guarantee on first paid charge, single-use per account/email/payment method, whichever more restrictive." | `07-packaging-and-pricing/trial-and-discount-policy.md` §5 |

### 2.4 Positioning claims — APPROVED

| Claim category | Canonical phrasing | Surface mapping |
|---|---|---|
| Hero (operator-grade) | "AI-driven capital-preservation infrastructure that enforces the discipline you've already built." | Website hero (operator-grade) |
| Hero (primary marketing) | "Trade smarter with AI." | Marketing campaigns; product hero (consumer-facing) |
| Hero (compact) | "Trade smarter." | Compact lockups; bios; sub-headlines |
| Hero (B2B / formal) | "Your trusted partner in cryptocurrency trading." | B2B / formal contexts; investor materials |
| Long form | See `05-positioning/positioning-statement.md` §1 | About page; pitch deck; recruiting |
| Paragraph form | See `05-positioning/positioning-statement.md` §2 | Hero sub-section; sales follow-up; content intros |

Other one-line variants must pass brand-voice review before publication.

### 2.5 Anti-claim disclosures — APPROVED (and required where context implies)

| Anti-claim | Where it must surface |
|---|---|
| "We don't generate alpha." | `coinscope.ai/what-we-dont-do` |
| "We don't deliver signals as recommendations to act on." | Same |
| "We don't custody capital." | Same |
| "We don't execute autonomously without authorization." | Same |
| "We don't make performance promises." | Same |
| "We don't operate in the US until our licensure path is decided." | `coinscope.ai/what-we-dont-do` (long form). Signup form Gate 1 uses the shorter "Not currently available in your region" per §2.2 surface-mapping note. |

These claims are the load-bearing trust signals. They are required, not optional, on the surface that lists product non-claims.

---

## 3. Forbidden categories — master short-list

Use of any of these in any external surface is a brand-voice violation triggering a stop-the-line review.

> **Permanently forbidden vs. conditionally forbidden:**
> §3.1 Performance, §3.3 Discount/urgency, §3.4 Adjacency/bundling, §3.5 Black-box, §3.6 Authority/endorsement, §3.7 Institutional misuse, §3.8 Automation overclaim — **permanently forbidden** (no path to allowed).
> §3.2 Readiness — **conditionally forbidden** (unblocked post-§8 pass + counsel review).
> §3.9 Model-evaluation metrics — **counsel-review-pending** (partial allowance possible at counsel engagement; default forbidden until resolved).

§4–§7 are the deep-dives on the highest-risk categories (Performance, Automation, Institutional-grade, AI). §3 is the master short-list copywriters consult first.

### 3.1 Performance claims — FORBIDDEN (deep-dive in §4)

- ~~"Win rate of X%."~~
- ~~"Average user makes Y."~~
- ~~"Returned X% over the past Y days."~~
- ~~"Backtested at X% return."~~ (testnet data does not justify production claims)
- ~~"ROI guaranteed."~~
- ~~"100x your account."~~
- ~~"Outperform [benchmark]."~~
- ~~"Top traders use CoinScopeAI."~~
- ~~"Beat the market."~~
- ~~"Profitable on N out of M trades."~~

Restated rule: **no performance language anywhere on any external surface, regardless of how flattering the underlying data might be**. Cohort observation summaries are anonymized and structural — they describe usage patterns, not outcomes.

### 3.2 Readiness claims — CONDITIONALLY FORBIDDEN (until §8 passes + counsel)

- ~~"Production-ready."~~
- ~~"Battle-tested."~~ (implies real-capital tests we have not run)
- ~~"Going live next week / soon / imminently."~~
- ~~"Beta = production once you trust it."~~
- ~~"Coming soon: live trading."~~
- ~~"Now with [feature] — fully tested!"~~ (unless brand-voice-reviewed)
- ~~"Stable and ready for real capital."~~

After §8 passes AND counsel reviews, the language can shift. The transition is itself a major event and gets a brand-voice + counsel review pass.

### 3.3 Discount / urgency theatre — FORBIDDEN

- ~~"Founder discount — locked in forever."~~
- ~~"Limited-time forever pricing."~~
- ~~"Last chance!"~~
- ~~"Going up tomorrow!"~~
- ~~"Lock in this rate forever."~~
- ~~"Refer 3 friends, get free Pro."~~ — **doubly-forbidden:** urgency framing + locked anti-tier-name "Pro" per `07-packaging-and-pricing/plan-matrix.md` §2

### 3.4 Adjacency / bundling claims — FORBIDDEN

- ~~"Bundled with [signal group / copy-trade / leverage maximizer]."~~
- ~~"Powered by [influencer]."~~
- ~~"As featured by [crypto Twitter handle]."~~
- ~~"Used by top trading communities."~~

### 3.5 Black-box claims — FORBIDDEN

- ~~"Our proprietary algorithm picks winners."~~
- ~~"AI does the work for you."~~
- ~~"Trust the system; it knows."~~
- ~~"Our models are too sophisticated to explain in detail."~~

(Note: "Set it and forget it" is forbidden under §3.8 Automation overclaim — single-source canonical home in §5.2.)

The rule: **if the public claim hides the engine, it is forbidden**. The product's positioning is methodology disclosure; black-box framing is structurally incompatible.

### 3.6 Authority / endorsement implication — FORBIDDEN

- ~~"Trusted by [vague authority]."~~ (unless an explicit, named, consenting endorsement that has passed brand + legal review)
- ~~"Used by professionals at [unspecified firms]."~~
- ~~"As seen on [unverified press]."~~
- ~~"5-star rated."~~ (unverified)

### 3.7 Institutional misuse — FORBIDDEN (deep-dive in §6)

- ~~"Institutional-grade returns."~~ (performance claim disguised)
- ~~"Used by institutional traders."~~ (false endorsement)
- ~~"Institutional-grade compliance."~~ (overclaim — we are sole-prop, validation-phase)
- ~~"Institutional-grade custody."~~ (we are explicitly custody-free)
- ~~"Institutional-grade audit-ready."~~ (audit-grade reporting is a P5 deliverable, not current)

See §6 for approved usages of "institutional-grade" in capability and audience-bridging contexts.

### 3.8 Automation overclaim — FORBIDDEN (deep-dive in §5)

- ~~"Autonomous trading."~~
- ~~"Trades for you while you sleep."~~
- ~~"Set it and forget it."~~
- ~~"Hands-free trading."~~
- ~~"Robo-trading bot."~~
- ~~"Algorithmic trading service."~~
- ~~"Automated profits."~~
- ~~"Fully autonomous AI trader."~~

See §5 for approved automation phrasings and the rationale.

### 3.9 Model-evaluation metrics scope — COUNSEL-REVIEW-PENDING

Performance claims about the v3 ML regime classifier itself (test-set accuracy, backtest model-output statistics) are a gray area between acceptable methodology disclosure and forbidden performance language. Counsel review at engagement start (per `14-risk-compliance-and-safeguards/regulatory-question-list.md` §4 and `compliance-assumptions.md` CA-13/CA-14) must address this category.

**Default state pending counsel:** forbidden as a marketing claim; allowed in methodology-page context only when **all four** anchors hold:

- (a) The test set is named (e.g., "OOS validation set, BTC-USDT 2024 Q1")
- (b) The metric definition is named (e.g., "regime-classification accuracy = correctly-labeled-bars ÷ total-bars")
- (c) The temporal window is named
- (d) No implication is drawn about user trading outcomes

**Forbidden regardless of counsel resolution:**

- ~~"Our model achieved 78% accuracy"~~ (without context anchors)
- ~~"Backtested model returns of [X]"~~ (drifts from model-eval to user-outcome)
- ~~Sharpe / Sortino / drawdown levels of model output presented as model performance~~ (covered in §4.4)

**Counsel question carried in `14-risk-compliance-and-safeguards/regulatory-question-list.md` §6.3 Q-Claim-7 / Q-Claim-8.**

---

## 4. Performance language guardrails

This category is so risk-heavy it gets its own section.

### 4.1 The cardinal rule

**No external surface contains any number, range, or percentage that describes user trading outcomes.** Not from cohort data. Not from testnet data. Not from "what users have reported." Not from anonymized aggregates. Not from "real-money simulation."

The rationale: **the line between "informational" and "promotional" performance language is finer than it looks**, and counsel exposure compounds. A safe rule is the bright line.

### 4.2 What is allowed in place of performance language

- **Methodology descriptions:** "The risk gate fires when daily loss exceeds your configured threshold. The locked floor is 5%."
- **Cohort observation patterns (anonymized, structural, no outcome numbers):** "P1 cohort users configure custom risk-gate thresholds in Week 1 of their evaluation."
- **Capability statements:** "The position sizer surfaces inputs, outputs, and rationale on every trade decision."
- **Operational metrics:** "Engine availability over the past 90 days: [X%]" (uptime is operational, not performance)

### 4.3 What is allowed with explicit caveat (brand-voice review required)

- Public quarterly cohort summary: must be anonymized, no per-user numbers, no aggregate return figures, no "average" anything related to outcomes
- Vendor incident summaries: operational language only

### 4.4 What is forbidden even with caveats

This list **extends §6.10 with quantitative-finance-specific anti-claims** that the upstream did not name explicitly:

- Win rates, expected values, risk-adjusted returns, Sharpe / Sortino numbers, drawdown levels achieved by any user, "average gain", "best month", "biggest winning trade"
- Even framed as "cohort observation" — these are performance language and are not mitigated by framing

---

## 5. Automation language guardrails

The product enforces user-defined risk gates and surfaces signals; it does not autonomously trade. Automation language must reflect that exactly. This is the canonical home for "Set it and forget it" and similar autonomous-execution framings.

### 5.1 Approved automation phrasing

- "Configurable risk gates that run before trade arming."
- "Pre-arming gate evaluation across the locked five thresholds."
- "User-authorized execution against the user's exchange account."
- "24/7 market surveillance across the configured Binance USDT-M perpetual universe." (specific scope, not "many pairs")
- "Telegram alerts via @ScoopyAI_bot."
- "The buyer decides whether the signal fits their framework."

### 5.2 Forbidden automation phrasing

- ~~"Autonomous trading."~~
- ~~"Trades for you while you sleep."~~
- ~~"Set it and forget it."~~ ← canonical home for this phrase
- ~~"Hands-free trading."~~
- ~~"Robo-trading bot."~~
- ~~"Algorithmic trading service."~~
- ~~"Automated profits."~~
- ~~"Fully autonomous AI trader."~~

### 5.3 Why these are forbidden

- They imply autonomous execution beyond what the product does (and beyond what counsel-approved posture allows)
- They are structurally incompatible with capital-preservation positioning
- They attract anti-ICP audience (alpha-seekers, autonomous-bot buyers)
- They expose CoinScopeAI to advisory-status / robo-advisor regulatory questions

The product is **a configurable risk-and-discipline tool that the user operates against their own exchange account**. Automation language must reflect that exactly.

---

## 6. "Institutional-grade" usage guidance

The phrase appears in CoinScopeAI's positioning ("institutional-grade, AI-driven crypto futures trading"). It is allowed but **with caveats**.

### 6.1 Approved usage

- "Institutional-grade risk management primitives" — describes capability
- "Institutional-grade infrastructure for individual traders and small portfolio managers" — describes audience-bridging positioning
- "We're building institutional-grade tooling at retail price points" — describes value prop

### 6.2 Forbidden usage

See §3.7 for the master short-list. Repeated here for the deep-dive context:

- ~~"Institutional-grade returns."~~ (performance claim disguised)
- ~~"Used by institutional traders."~~ (false endorsement)
- ~~"Institutional-grade compliance."~~ (overclaim — we are sole-prop, validation-phase)
- ~~"Institutional-grade custody."~~ (we are explicitly custody-free)
- ~~"Institutional-grade audit-ready."~~ (audit-grade reporting is a P5 deliverable, not current)

### 6.3 The required caveat

Whenever "institutional-grade" appears, the surrounding context must make clear what is being claimed:

- **Capability** — what the engine does (acceptable)
- **Audience-bridging value** — that retail / small-PM buyers get tools previously reserved for funds (acceptable)

Not what is being claimed:

- **Status / certification / regulation** (forbidden — we are not regulated as institutional)
- **Track record** (forbidden — performance)
- **Endorsement** (forbidden unless named + counsel-cleared)

### 6.4 REQUIRED INPUT

**Counsel sign-off on "institutional-grade" usage** is needed before P1 launch (per `business-plan/13-support-and-trust-ops/README.md` §6 question 7 and `14-risk-compliance-and-safeguards/regulatory-question-list.md` §2.2 Q-Pos-4 through Q-Pos-6). The phrase is core to positioning; counsel must confirm legal exposure is acceptable in the approved usages.

---

## 7. How to discuss AI without overclaiming

The product uses AI (v3 ML regime classifier; minimal Claude API integration). AI claims are a category-risk because the genre is overclaim-heavy.

### 7.1 Approved AI phrasing

- "AI-driven regime classification (v3 ML)."
- "AI-assisted signal context — every signal carries a regime label and confidence score."
- "Machine-learning regime classifier trained on historical OHLCV / OI / funding / liquidation data."
- "Minimal LLM use during P1 validation; we use Claude for [`task-name`]." (template — see placeholder convention below)
- "AI augmentation of human discipline, not replacement of human discipline."

> **Bracket-placeholder convention:** [`task-name`] / [`link`] / [`X%`] / [`Y`] etc. in this file are template placeholders. The placeholder itself is not approved phrasing. At surface instantiation, the bracket is replaced with the surface-specific value, which then passes brand-voice review like any other claim. For the LLM-use phrasing above, the founder fills in the actual narrow task (e.g., "Claude for vendor-stack reasoning summarization in methodology longform") at publication.

### 7.2 Forbidden AI phrasing

- ~~"AI predicts the market."~~
- ~~"Our AI knows what to trade."~~
- ~~"GPT-powered alpha."~~ (or any model brand-flexing)
- ~~"AI eliminates emotion from your trades."~~ (overclaim)
- ~~"Smart AI that thinks like a hedge-fund quant."~~
- ~~"AI trader that does the work for you."~~
- ~~"Machine learning that beats the market."~~

### 7.3 The discipline

- Be **specific** about what the model does (regime classification) and does not do (does not predict price; does not make trade decisions; does not autonomously execute)
- Be **specific** about confidence (every signal carries a confidence score; we do not hide it)
- Be **specific** about the engine's limitations (testnet only; validation phase; gated)

The principle: **AI is a feature of the engine, not a marketing veneer**. Treat it like the position-sizer — describe what it does, show the inputs, surface the outputs. No mystique.

---

## 8. Review process for public-facing claims

### 8.1 Mandatory review surfaces

Every external surface passes brand-voice review before publication:

- Pricing page (and any change to it)
- About page (and any change)
- Methodology page edits
- "What we don't do" page edits
- PCC v2 page edits
- Status page incident notes (templated, but each instance reviewed when severity ≥ medium)
- Substack posts (every one)
- X/Twitter methodology threads (defined as: founder-authored thread of ≥3 tweets advancing a methodology argument)
- Launch announcements (every one)
- Press placements / op-eds (every one)
- Conference talks / decks (every one)
- Onboarding email sequences (every one)
- Telegram alert template changes (each template change reviewed)
- Support reply templates (each template change reviewed)
- Any new claim outside the approved list

**Routine engagement does NOT need review:** single-tweet replies, likes, simple acknowledgments that don't introduce a new claim. When uncertain about the boundary, route to review.

### 8.2 Review process

1. **Author drafts the surface** with the approved-claim list (§2) open and the forbidden-claim list (§3) visible.
2. **Brand-voice skill audit** runs against the draft. Any flagged claim returns to author for revision.
3. **Founder approves** the surface (founder is the named approver during P0–P2; may delegate to a vetted brand-voice contractor at P3+ — see §8.6 audit cadence).
4. **For high-risk claims** (legal posture, financial promises, performance-adjacent language, "institutional-grade" usage, AI claims, model-evaluation metrics): **counsel review in addition** before publication.
5. **Surface ships** with a brand-voice review log entry recorded (see §8.5).

### 8.3 Review SLA

- Routine surfaces: <24h review turnaround
- Launch / press surfaces: <72h review turnaround
- Counsel-required surfaces: per counsel's response time + brand-voice pass

### 8.4 Review failure handling

If a claim ships unreviewed and is later flagged:

1. **Immediate:** the surface is amended or pulled.
2. **Postmortem:** brand-voice review log entry; what failed, what to fix.
3. **Comms:** if the claim was visible publicly long enough to matter, an honest correction note is published per `incident-communications.md` §4.7.
4. **Pattern check:** if more than one such failure occurs in a quarter, the review process is hardened (e.g., automated content scanning before publish; second-author review; contractor audit cadence resets per §8.6).

The principle: **a single overclaim is recoverable; a pattern is not**.

### 8.5 Brand-voice review log artifact

The brand-voice review log is the per-surface record of every brand-voice review pass that a public surface received before publication. It is a load-bearing operational artifact.

**Location:** `business-plan/_data/brand-voice-review-log.md` (REQUIRED INPUT — file to be created pre-P1 launch as part of pre-launch checklist closeout per `08-go-to-market/launch-plan.md` §4.3).

**Fields per entry:**

- Surface name (e.g., "Pricing page hero, 2026-05-30 update")
- Author
- Date submitted for review
- Brand-voice skill audit output (flagged claims, if any)
- Author response / revision summary (if applicable)
- Founder approver
- Approval date
- Surface ship date
- Edit history if amended post-publication
- Counsel review status (if applicable)

**Access:**

- Founder: read-write
- Brand-voice contractor (P3+): read-write within their scope
- Counsel: read-only on request

**Cadence of audit:**

- Weekly during P1 (founder reviews each prior-week entry)
- Monthly thereafter
- Quarterly external audit at v2.5+ (single contractor reviewing the full log)

The log is a trust signal in its own right — its existence and its discipline are evidence of operational integrity per `trust-framework.md` §3.

### 8.6 Contractor audit cadence

When a vetted brand-voice contractor takes on first-pass review at P3+ (per `support-operating-model.md` §9 v1.5/v2 transitions), the audit cadence enforces quality:

- **Weeks 1–4 (initial):** founder reviews **100%** of contractor-approved surfaces post-hoc; any flagged miss returns to 100% review for an additional 4 weeks
- **Weeks 5–12 (ramp):** drops to **25% spot-check** if quality holds (zero pattern failures in weeks 1–4)
- **v2.5+ (Jan 2027+):** drops to **10% spot-check + monthly audit** of the full review log
- **Any flagged miss at any cadence:** returns to 100% review for 4 weeks

Same shape as `support-operating-model.md` §9 — the discipline is consistent across functional contractor onboarding.

---

## 9. Example good vs. bad phrasing

Real examples, organized by category. Use these as the calibration set.

### 9.1 Pricing page — examples

| Bad | Good |
|---|---|
| "Trader — $79/mo. Full dashboard access." | "Trader — $79/mo. Includes engine API + dashboard (stabilizing in cohort during validation phase)." |
| "Founding member — discount locked in forever!" | "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies." |
| "Save 30% off — limited time only!" | "Pay for 10 months, get 12 (≈17% off) — annual prepay discount." |
| "Get started today — no risk, full refund anytime!" | "14-day money-back guarantee on first paid charge, single-use per account/email/payment method, whichever more restrictive." |

### 9.2 Methodology / capability — examples

| Bad | Good |
|---|---|
| "Our AI predicts market moves with high accuracy." | "Our v3 ML regime classifier labels each market state as Trending, Mean-Reverting, Volatile, or Quiet, with a confidence score on every signal." |
| "Set it and forget it — the system trades for you." | "Configurable risk gates that run before trade arming; user-authorized execution against the user's exchange account." |
| "Battle-tested algorithms with proven returns." | "Engine running on Binance USDT-M Testnet during a 30-day validation phase. Real-capital deployment opens through a phased ramp once §8 Capital Cap evidence accumulates." |

### 9.3 Cohort / observation — examples

| Bad | Good |
|---|---|
| "Our cohort has seen returns of [X%] in their first month." | "Our P1 cohort is observing engine behavior over a 30-day validation window. We do not publish per-user performance figures." |
| "Top users in our cohort have profited consistently." | "Cohort observation focuses on rule-respect, retention, and edge-case behavior. Performance language is not used." |
| "Beta users say it's life-changing." | (Do not publish testimonials presented as endorsement. If a user gives explicit permission for an attributed quote, it must pass brand-voice + counsel review and may not contain performance language.) |

### 9.4 Incident / status — examples

| Bad | Good |
|---|---|
| "Minor blip earlier — all good now!" | "Status: Binance USDT-M API experienced elevated latency 14:32–14:47 GMT+4. Scanner refresh delayed during this window. Resolved at 14:47. Postmortem to follow within 7 days." |
| "We're investigating an issue." | "Issue confirmed at 14:32 GMT+4: Binance USDT-M scan endpoint returning stale data. Engine fallback active. Next update at 15:00." |
| "Apologies for the inconvenience!" | "Incident root cause: vendor API change without prior notice. Mitigation deployed at 14:47. Runbook updated. Postmortem published [`postmortem-link`]." |

(The `[postmortem-link]` is a bracket-placeholder per the convention in §7.1 — replace with the actual URL at instantiation.)

### 9.5 Support reply — examples

| Bad | Good |
|---|---|
| "Hi friend! 👋 Thanks for reaching out! 😊" | "Hi [`Name`] — thanks for the report. Looking into this now." |
| "Sorry to hear that! We'll get back to you ASAP!" | "Acknowledged. Severity P3 — first-response SLA <24h within coverage hours (Sun–Thu 09:00–15:00 GMT+4)." |
| "We can definitely add Bybit copy-trade — let us know your thoughts!" | "Bybit is on the public roadmap, scheduled for P2 vendor expansion (target Aug–Sep 2026, gate-driven per `14-launch-roadmap.md` §14.1). Copy-trade is not on the roadmap; per our positioning, we don't offer copy-trade. The 'what we don't do' reference is at [`what-we-dont-do-link`]." |

---

## 10. Cross-references

- Brand messaging canonical: `business-plan/09-brand-messaging.md`
- Anti-overclaim audit (pricing): `business-plan/06-pricing-monetization.md` §6.10
- Primary ICP (methodology + journal claim sources): `business-plan/04-icp-and-segmentation/primary-icp.md`
- Positioning statement (hero variant sources): `business-plan/05-positioning/positioning-statement.md`
- Pricing strategy (annual prepay framing canonical): `business-plan/07-packaging-and-pricing/pricing-strategy.md`
- Trial / discount policy (refund language source): `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Plan matrix (locked tier names): `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Trust-first growth: `business-plan/08-go-to-market/trust-first-growth.md`
- Launch plan (pre-launch checklist for §8.5 log file creation): `business-plan/08-go-to-market/launch-plan.md`
- Onboarding strategy (US Gate 1 surface): `business-plan/12-onboarding-and-activation/onboarding-strategy.md`
- First-value design (downstream consumer of this canonical): `business-plan/12-onboarding-and-activation/first-value-design.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Support operating model (contractor audit cadence reference): `business-plan/13-support-and-trust-ops/support-operating-model.md`
- Incident communications: `business-plan/13-support-and-trust-ops/incident-communications.md`
- Compliance assumptions (CA-13/CA-14 model-evaluation pending): `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`
- Regulatory question list (Q-Pos-4..6 institutional-grade; Q-Claim-7..8 AI claims): `business-plan/14-risk-compliance-and-safeguards/regulatory-question-list.md`
- Strategic priorities (D8 Arabic deferral): `business-plan/01-executive-summary/strategic-priorities.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- No Investment Advice memo: `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`
- Risk Disclosure: `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- Brand-voice review log artifact (REQUIRED INPUT pre-P1): `business-plan/_data/brand-voice-review-log.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
