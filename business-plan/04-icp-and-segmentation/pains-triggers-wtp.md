# Pains, Triggers, and Willingness-to-Pay

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file maps **pain points**, **buying / activation triggers**, **trust triggers**, **willingness-to-pay indicators**, and **anti-fit signals** by segment. It is the input to messaging (`09-brand-messaging.md`), packaging (`_phase-2/_packaging/`), pricing (`_phase-2/_pricing/`), and channel strategy (`_phase-2/_gtm/`).

The voice across this file is **buyer-side**, not product-side. We capture what each segment feels, what causes them to evaluate, what causes them to commit, and what they reveal in their language about how much they will pay.

---

## 1. Pain points by segment

### P1 Omar — Self-Taught Methodist (primary)

| Pain | Severity | Frequency | Where it lives today |
|---|---|---|---|
| Manual gating is tiring and error-prone at edge cases (multiple positions, after-hours, news) | High | Weekly | Spreadsheets, mental rules |
| Journal lives in spreadsheets/Notion; performance attribution is painful | High | Monthly | Notion, Sheets |
| Tools either replace their methodology or ignore it | High | Per-tool | Existing crypto SaaS |
| Plenty of products exist for chart-pattern traders; few for *risk-first methodology* traders | High | Persistent | Underserved-segment feeling |
| Sleep loss during volatile sessions because monitoring is manual | Medium-High | Cyclical | Personal time |
| Doubt about whether they followed their own rules | Medium | Per-trade | Self-assessment |
| Cognitive load of remembering thresholds across multiple positions | Medium | Daily | Working memory |

### P2 Karim — Engineer Trader

| Pain | Severity | Frequency | Where it lives today |
|---|---|---|---|
| Wants programmable risk + clean APIs; offered black boxes and signal feeds | High | Per-tool | Existing crypto SaaS |
| Build-vs-buy math: "I could spend six months building this myself" | High | Per-decision | Self-debate |
| Engineering hobby trading takes time away from day job; cost of part-time discipline is high | Medium-High | Continuous | Personal time |
| Lack of well-documented APIs in the crypto-tooling category | High | Per-evaluation | Documentation reading |
| Existing tools assume they want a UI; they want a CLI / SDK / read API | Medium | Per-tool | Workflow friction |
| Hard to integrate exchange-native tools with their own indicators / scripts | Medium | Per-strategy | Glue code |

### P3 Layla — Solo PM

| Pain | Severity | Frequency | Where it lives today |
|---|---|---|---|
| Toolchain is a spreadsheet; audit trail is an inbox | Critical | Daily | Sheets, email |
| Multi-account juggling across personal book and partner book is error-prone | High | Daily | Exchange dashboards |
| Bloomberg / Aladdin / institutional risk vendors are overspecified and overpriced for $200k–$1M | High | Per-evaluation | Procurement context |
| Partner expects clean reports; current process is 90% manual | High | Monthly | Spreadsheet pain |
| Regulatory ambiguity for informal partner-book operations creates documentation pressure | Medium-High | Continuous | Legal anxiety |
| Time taxonomy: too much time on operations, not enough on decisions | High | Daily | Calendar reality |
| No clean separation between rules-engine and reporting-engine | Medium | Per-process | Tool fragmentation |

---

## 2. Buying / activation triggers

What causes a prospect to start evaluating, and what causes them to commit. Triggers are *external events*, not preferences.

### P1 Omar — Buying triggers

| Trigger | Likelihood to convert | Pattern |
|---|---|---|
| Peer in a methodology-focused closed community recommends | High | Word-of-mouth in cohort |
| A long-form explainer demonstrates the team understands position-sizing math | High | Substack / blog / explainer post |
| Account size inflection — typically ~$50k across multiple positions | Medium-High | Manual processes break |
| A drawdown they handled correctly that nonetheless cost them sleep | Medium-High | "I should automate this" moment |
| Reading the canon (Van Tharp, Schwager) again and noticing the gap between book and tools | Medium | Spontaneous |

### P1 Omar — Activation triggers (post-signup)

| Trigger | What converts Free → Paid |
|---|---|
| First time the gate fires correctly during their evaluation | Direct conversion driver |
| First R-multiple report that matches their hand-calculation | Trust establishment |
| Telegram alert lands at exactly the right moment with canonical payload | Workflow displacement |
| Configurable thresholds save under their own values | Framework respect |
| Math transparency check passes (they verify the formula) | Hard requirement |

### P2 Karim — Buying triggers

| Trigger | Likelihood |
|---|---|
| Read API documented and shipping (P1 close target) | High |
| Architecture / decision-record content published | Medium-High |
| HN / applied-quant Twitter / GitHub presence | Medium |
| Direct cost comparison: $79/mo vs. ~6 months personal build time | Medium |

### P3 Layla — Buying triggers

| Trigger | Likelihood |
|---|---|
| Referral from a trusted P1 Omar in their network | High |
| Published cohort-data artifact (post-validation) | High |
| Audit-grade journal sample (anonymized) available to read | Medium-High |
| Counsel-aware Solo-PM marketing copy that does not over-position as fund-formation tool | Medium-High |
| Multi-account view at Desk Preview reaches quality bar | Direct conversion driver |

---

## 3. Trust triggers

The specific trust signals that move each segment from "interested" to "willing to pay." These compound — multiple signals are typically needed before commitment.

### P1 Omar — Trust triggers

- **Anti-overclaim posture observable in the first 30 seconds.** No "10x your account" copy; no leaderboards; no testimonials presented as endorsement.
- **PCC v2 published with G1–G4 + §8 criteria.** They will read it.
- **Position-sizing math shown with formula, inputs, output.** Not just claimed.
- **Founder named, contactable, consistent voice across surfaces.** No anonymous team page.
- **API-key scopes copy: "least privilege, no withdrawal scope, ever."** Explicit, not buried.
- **Free tier is genuinely useful, not a frustration funnel.** First-value pre-billing.
- **Documentation cadence visible.** Decision log openness, postmortems in product-tier voice.
- **Testnet-only honesty in the header disclaimer.** Not hidden.

### P2 Karim — Trust triggers

- **API documentation quality.** Schemas, error codes, rate limits documented.
- **Architecture decision records and engineering rationale posts.** Public reasoning.
- **GitHub presence** (when appropriate) showing the team ships and ships cleanly.
- **Open posts about what doesn't work and why.** Failure stories build trust faster than success stories.
- **Code-level testnet hard-gate evidence.** A line of code or a CI check, not just a policy.

### P3 Layla — Trust triggers

- **Cohort-data artifacts published post-validation.** P1 cohort retention, churn, gate-fire rates.
- **Audit-grade journal sample.** Anonymized, real, complete.
- **Counsel posture documented.** "Tools, not advice" memo references.
- **MENA-built credibility.** Founder context, entity intent, jurisdictional posture.
- **No fund-formation positioning.** Solo-PM marketing copy that respects the regulatory line.
- **Reporting samples that look like what their partner expects to read.**
- **Locked phrasing: "institutional-grade" reserved for evidenced cases.** Misuse is a fail signal.

---

## 4. Willingness-to-pay indicators

Signals that reveal what each segment actually pays — and what they will not pay. These are not surveys; they are **observable behaviors** in evaluation conversations.

### P1 Omar — WTP indicators

| Signal | Implication |
|---|---|
| Already paying for Edgewonk, Tradervue, prop-firm risk dashboards, or methodology coaching | $79/mo is well within their toolchain budget |
| Account size $50k+ across multiple positions | Tier matrix anchor matches; upgrade-pressure threshold approached |
| Frames cost as "% of one bad decision" rather than as monthly subscription line | $79 is rational against avoided-loss math |
| Comfortable with annual prepay if the discount is meaningful (15–20% range typical) | Prepay-attach feasibility |
| Will not pay if the product positions as performance promise | Anti-overclaim is *required* not *preferred* |
| Will not pay above $79 for a Trader tier without multi-account or read API | Tier matrix integrity |

**Recommended price point:** Trader $79/mo. Founder-cohort price (P1) per cohort document.
**Annual prepay discount:** **DECISION NEEDED**; carry to `06-pricing-monetization.md`. ASSUMPTION: 15–20% range typical for this segment.

### P2 Karim — WTP indicators

| Signal | Implication |
|---|---|
| Frames buy decision against six-month personal build time | $79–$399 must defeat opportunity cost |
| Wants the Desk Preview read API; willing to upgrade for it | Trader → Desk Preview pathway intact |
| Comfortable with monthly billing during evaluation; annual after 60–90 days | Prepay-attach feasibility delayed |
| Will not pay if API documentation is poor, regardless of features | Documentation is part of pricing |
| Will not pay for autonomous execution or signal-service framing | Voice posture matters here too |

**Recommended price points:** Trader $79 → Desk Preview $399. Read API documentation quality is part of the price proposition.

### P3 Layla — WTP indicators

| Signal | Implication |
|---|---|
| Comparing CoinScopeAI against Bloomberg / Aladdin / smaller institutional vendors | $399–$1,199 is well within their procurement frame |
| Asks about per-seat scaling unprompted | Desk Full v2 upgrade narrative resonates |
| Asks about audit-grade journal and reporting unprompted | Desk Preview surface is the right fit; Desk Full v2 confirmation |
| Will not pay sticker price for Desk Preview if multi-account view is partial | Quality bar gating; revisit after P1 close |
| Will pay annual prepay readily if procurement allows | High prepay-attach |
| Will not pay if marketing copy reads as fund-formation alternative | Counsel-line discipline matters at WTP layer |

**Recommended price points:** Desk Preview $399/mo → Desk Full v2 $1,199/mo + per-seat ($149 or $249) at P5.
**Per-seat tier:** **DECISION NEEDED** on which exact per-seat anchor ($149 or $249); carry to `06-pricing-monetization.md`.

---

## 5. Anti-fit signals — when a prospect is *not* a good fit

A consolidated list of signals that should cause the founder to deprioritize a prospect during P1, even if they are willing to pay. Each is observable in the first 1–2 conversations.

| Anti-fit signal | Source | Why it matters |
|---|---|---|
| Asks "what should I trade today?" rather than "how do I size what I'm trading?" | P1 anti-fit | Buyer wants signals, not process |
| Wants the product to override their rules and run autonomously | P1, P2, P3 anti-fit | Custody-free + user-authorized posture |
| US-resident retail | All anti-fit | Geofence + regulatory posture |
| Sub-$5k account | All anti-fit | Tier-matrix anchor; cohort signal |
| Talks in performance terms ("how much can I make") rather than process terms | P1 anti-fit | Vision A mismatch |
| Wants to copy-trade or follow leaders | All anti-fit | Custody-free + anti-overclaim posture |
| Wants CoinScopeAI to custody capital | All anti-fit | Structural posture |
| Asks for guarantees | All anti-fit | Anti-overclaim posture |
| Treats the validation-phase disclaimer as a deal-breaker | All anti-fit | Posture mismatch — not a buyer for our window |
| Pushes for paid promotion / referral payouts as a precondition | All anti-fit | Anti-overclaim risk |
| Frames CoinScopeAI as a fund or fund-formation tool | P3 anti-fit | Counsel line; cannot position as such |
| Wants white-label / private-label arrangement | All anti-fit | Out of scope; not on roadmap |

When any 2 of these signals appear in the first conversation, the founder should politely decline rather than pursue.

---

## 6. Implications for messaging

Direct readouts from the segment WTP and trust-trigger layers into messaging:

| Surface | Messaging direction |
|---|---|
| Headline / hero | "AI-driven capital-preservation infrastructure that enforces the discipline you've already built." (locked v1) |
| Sub-headline | Lead with *enforce your framework*; refer to *risk gates*, *regime*, *evidence*; never lead with *AI* in isolation |
| Body | Show formula transparency at least once; show a sample gate-refusal pattern; show the testnet-only disclaimer in-line, not in a footer |
| About / team | Founder named; UAE-resident; sole-prop-and-honest-about-it; voice consistency across surfaces |
| Pricing page | Tier matrix exposed; founder-cohort terms not advertised generally; annual prepay discount **DECISION NEEDED** |
| Onboarding copy | "Bring your own framework — configure these thresholds to your rules"; explicit API-key scope copy at exchange-connection step |
| Status / incidents | Postmortems in product-tier voice; cohort-data discipline |
| Community / content | Long-form over short-form; methodical over performative; closed-community channel preference for P1 Omar |
| Disallowed phrasing | "Production-ready" (until §8 passes); "guaranteed"; "10x your account"; "boost your returns"; "best-in-class"; "institutional-grade" used without evidence |

---

## 7. Implications for packaging

Direct readouts from the segment JTBD + WTP layers into packaging:

| Tier | Locked anchor | What it must include for its primary segment | What it must NOT include |
|---|---|---|---|
| **Free** | $0 | Read-only scanner sample; regime label; first-value pre-billing | Risk-gate output (a paid surface); journal; alerts |
| **Trader** | $79/mo | Full scanner; risk gates; regime; journal; canonical Telegram alerts; configurable thresholds; R-multiple reporting | Multi-account; read API; per-seat |
| **Desk Preview** | $399/mo | All Trader features + multi-account view + advanced gates + read API + Desk-grade analytics | Per-seat scaling (Desk Full v2 only); audit-grade reporting (Desk Full v2) |
| **Desk Full v2** | $1,199/mo + per-seat | All Desk Preview features + per-seat permissions + audit-grade journal + advanced reporting + partner read-only views | Custody, fund-formation features, autonomous execution |

Per-seat anchor ($149 vs $249): **DECISION NEEDED** before Desk Full v2 GA at P5.

---

## 8. Activation flow implications

What needs to be present at each evaluation stage by segment, derived from the trigger and trust-layer mappings:

| Stage | P1 Omar | P2 Karim | P3 Layla |
|---|---|---|---|
| Discovery | Substack / closed-Discord referral | HN / applied-quant Twitter / GitHub | Referral from P1 Omar in network |
| First-look | Long-form explainer; PCC v2 visible | API documentation; engineering posts | Cohort-data artifact (post-validation); audit-grade sample |
| Free-tier evaluation | Scanner + regime sample; framework-respect copy | API exploration; payload schemas | Light evaluation; mostly waiting for cohort-data signal |
| Trial / paid evaluation | 2–6 weeks; configurable gates; math transparency check | 4–8 weeks; read API verification | 2–4 months; multi-account quality bar; reporting sample |
| Commitment | Subscribes to Trader; eventually moves journal | Subscribes to Trader → upgrades to Desk Preview | Subscribes to Desk Preview; positions for Desk Full v2 at P5 |

---

## 9. Cross-references

- Locked v1 §3 persona cards: `business-plan/03-icp-segmentation.md`
- Locked v1 §4 problem and value prop: `business-plan/04-problem-value-prop.md`
- Locked v1 §6 pricing: `business-plan/06-pricing-monetization.md`
- Primary ICP: `04-icp-and-segmentation/primary-icp.md`
- Secondary ICPs: `04-icp-and-segmentation/secondary-icps.md`
- Jobs to be done: `04-icp-and-segmentation/jobs-to-be-done.md`
- Tier matrix: `01-executive-summary/business-model-summary.md` §3
- Brand voice rules: `business-plan/09-brand-messaging.md`
- Counsel brief: `business-plan/_data/legal/Counsel_Brief_v2.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
