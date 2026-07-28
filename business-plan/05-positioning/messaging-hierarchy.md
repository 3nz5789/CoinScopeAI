# Messaging Hierarchy

**Status:** Wave 1 · v1 · 2026-05-07 · pending category-decision ratification (W1-Q1)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **operator-grade messaging hierarchy** — recommended pending ratification of the category decision (W1-Q1 in `_wave-1-closeout.md`). It declares the master message, the supporting messages, the proof points, the trust language, and the claims guardrails — and then translates the hierarchy into surface-specific direction for the homepage, product pages, sales conversations, onboarding, and content.

The rule: every external surface inherits from this file. If a surface has language that is not derivable from this hierarchy, it is drift, and the brand-voice review skill should catch it before publication.

---

## 0. Voice taxonomy

Locked v1 (`CLAUDE.md` register) defines two voice tiers:

- **Product tier** (app, coinscope.ai, docs): technical, terse, declarative, data-led. No emoji. No marketing fluff. Numbers monospaced / tabular.
- **Social tier** (IG, X, Threads, FB): aspirational, meme-fluent — never used inside the product.

This file uses two **additional working tiers** to cover homepage / sales / long-form surfaces that fit neither locked tier cleanly. Both are tagged `DECISION NEEDED` pending ratification in `business-plan/09-brand-messaging.md`:

| Working tier | Surfaces | Register | Status |
|---|---|---|---|
| Product (locked) | Dashboard chrome, in-product copy, Telegram payloads, status pages, documentation | Terse, declarative, data-led, no emoji | Locked v1 |
| **Brand** (working) | Homepage, about, pricing, tier landings, recruiting, investor leave-behind | Product-tier voice extended for marketing context — may use "AI-driven" as modifier; never marketing fluff | DECISION NEEDED |
| **Founder voice** (working) | Sales conversation, long-form blog, founder posts, recruiting paragraphs | First-person, methodical, anti-overclaim; the founder's own voice on the page | DECISION NEEDED |
| Social (locked) | IG, X, Threads, FB | Aspirational, meme-fluent | Locked v1 |

**Brand-tier vs product-tier reconciliation rule:** Brand-tier surfaces may use "AI-driven" as a modifier. Product-tier surfaces do not — AI is implied by features (regime classifier, signal confluence), not branded as a feature. Per CLAUDE.md register and this file §8.

If §3.7 / §3.8 cohort feedback or a brand-voice review pass produces evidence that the four-tier system is over-specified, collapse to two tiers (product + social) and treat homepage / sales / blog as marketing surfaces under product-tier discipline. Working assumption is the four-tier system holds; ratification gates the lock.

---

## 1. Master message

> **AI-driven capital-preservation infrastructure that enforces the discipline you've already built.**

This is the locked v1 line from `business-plan/01-executive-summary.md`. It is the canonical one-sentence message. Every other piece of copy is downstream of this sentence.

### Why this sentence holds

- **"AI-driven"** acknowledges Force 2 (AI cost-collapse) without making AI the hook
- **"capital-preservation infrastructure"** locks Vision A in the noun phrase
- **"enforces"** carries the operating-system frame (Option C from `category-decision.md`)
- **"the discipline you've already built"** signals respect for primary ICP's framework — and excludes anyone who hasn't built one
- The sentence does not promise performance, returns, or autonomy — anti-overclaim by construction

### When to use it

- Homepage hero
- Investor leave-behind
- Single-line bio / signature
- Whenever the available context is exactly one sentence

### When not to use it

- Inside-product surfaces (use product-tier voice; this is brand layer)
- Telegram alerts (use canonical payload schema)
- Technical documentation (use feature-named, terse phrasing)

---

## 2. Supporting messages

Three supporting messages, each carrying a distinct buyer-perspective truth. They expand the master message; they do not replace it.

### S1 — On *what we are*

> **A trader operating system that runs configurable risk gates before trades arm.**

Carries: Option C category lock + D1 (gate before arming) + D2 (regime context).
Use on: Hero sub, sales open, content intros.

### S2 — On *what makes us different*

> **Your capital stays in your exchange account. We don't trade for you. We enforce the rules you've written.**

Carries: D3 (custody-free) + D1 (gate enforcement) + custody / authorization framing.
Use on: About-page section heads, FAQ leads, sales pivot when comparison-pressure arrives.

### S3 — On *posture and trust*

> **UAE-built. Custody-free by structural choice. Gated against real-capital deployment until our Production Candidate Criteria pass.**

Carries: D5 (UAE-built) + D3 (custody-free as posture) + D4 (anti-overclaim, validation-phase honesty).
Use on: About page, footer language, investor introductions, recruiting page.

---

## 3. Proof / support points

Each support point pairs with a master or supporting message. Each is **observable** (not asserted) — a buyer can verify it without taking our word.

| Proof point | What it supports | Where it shows |
|---|---|---|
| Risk gate fires *before* trade arms; rejected trades return the explicit gate | D1, S1, S2 | Homepage feature section; gate UI; refusal patterns |
| Regime label (Trending / Mean-Reverting / Volatile / Quiet) + confidence on every signal | D2, S1 | Homepage; regime page; signal payloads |
| API-key scope copy: "least privilege, no withdrawal scope, ever" | D3, S2, S3 | Exchange-connection step; documentation |
| Production Candidate Criteria v2 — published, gated G1–G4 + §8 | D4, S3 | Dedicated PCC page; about page; footer link |
| Founder named, contactable, UAE-resident; consistent voice across surfaces | D5, S3 | About page; founder posts; recruiting page |
| Locked thresholds: 10% drawdown · 5% daily loss · 10x leverage · 5 max positions · 80% heat | D1 | Hero risk-numbers strip; gate UI; documentation |
| Position-sizing formula transparency (formula + inputs + output visible when composing) | D1 | Position-sizing UI; documentation |
| R-multiple + rule-violation tagging in journal | D1, S1 | Journal UI; sample journal artifact |
| Testnet-only honesty; visible disclaimer above the fold | D4, S3 | Hero footer; product surfaces; documentation |
| Decision log openness | D4 | Linked from about page (post-validation; **DECISION NEEDED** W1-Q26) |

---

## 4. Trust-supporting language

Specific phrasing that carries trust without overclaiming. Each is approved across surfaces.

| Phrase | When to use | Why it carries trust |
|---|---|---|
| "Validated on testnet" | Anywhere the product's state is described | Honest about state |
| "30-day validation phase" | Footer, disclaimers, status descriptions | Specific, time-bound, falsifiable |
| "No real capital deployed" | Footer, validation copy | Posture statement |
| "Capital stays in your exchange account" | Custody / authorization sections | Verifiable feature |
| "Rule-respected" | Gate-result descriptions | Process-led, not performance-led |
| "Evidence-led" | Methodology / about copy | Anti-overclaim signaling |
| "Methodical" | Brand voice descriptions | Brand-voice rule |
| "Risk-gated" | Replaces "risk-free" | Honest substitute |
| "Configurable to your thresholds" | Product description | Framework-respect signal |
| "Your authorization required" | Order-arming descriptions | Custody-free signal |
| "Founder named: [Mohammed]" | About / contact | Accountability signal |
| "UAE-built" | Geography copy | Specific, verifiable |
| "Custody-free by structural choice" | Posture copy | Specific, verifiable |
| "Gated against real-capital deployment" | Status copy | Falsifiable posture |

---

## 5. Claims guardrails (the disallowed list)

Carried from `02-company-overview/strategic-constraints.md` §2 and `05-positioning/positioning-statement.md` §7. Disallowed across all surfaces.

| Disallowed phrase | Reason |
|---|---|
| `production-ready` | Until PCC v2 §8 passes |
| `guaranteed` (any form) | Anti-overclaim |
| `10x your account`, `boost`, `crush the market` | Anti-overclaim, brand voice |
| `autonomous trading`, `we trade for you`, `set it and forget it` | Custody-free + user-authorized posture |
| `our signals` (as deliverable) | Anti-signal-service positioning |
| `institutional-grade` (without surface evidence) | Reserved phrasing |
| `best-in-class`, `market-leading`, `world's first`, `industry-leading` | Anti-overclaim, unverifiable |
| `live performance`, `track record` | Until PCC v2 §8 Capital Cap passes + counsel review |
| `risk-free` (any context) | Anti-overclaim |
| `AI` as standalone hook | Use as modifier with feature evidence |
| `30-day money-back guarantee` | Anti-overclaim risk |
| Customer testimonials presented as endorsement of returns | Anti-overclaim |
| Fund-formation framing for Solo PM marketing | Counsel-line; locked v1 §3.0 |
| US-targeted user copy (until licensure) | Regulatory posture |
| `no-code` / `easy setup` (oversimplified) | Brand voice; primary ICP rewards depth |

---

## 6. Homepage headline direction

### Hero headline

> **AI-driven capital-preservation infrastructure that enforces the discipline you've already built.**

### Hero sub-headline

> A trader operating system for disciplined crypto-perp traders. Configurable risk gates run before trades arm. Regime, confidence, and gate result on every signal. Capital stays in your exchange account.

### Hero footer (above the fold)

> Testnet only. 30-day validation phase. No real capital. PCC v2 published.

### Hero CTA

> See how the gate works → (links to a live demo of a refused trade with explicit gate)
>
> **REQUIRED INPUT:** confirm "live demo of a refused trade" surface ships before homepage publication. In scope for P1 launch readiness; not yet a confirmed artifact in `02-company-overview/current-state-assessment.md`.

### Sub-hero proof strip (visible in hero region)

> 10% max drawdown · 5% daily loss · 10x max leverage · 5 max open positions · 80% heat — your thresholds, configurable.

The discipline: the buyer should be able to read the hero and disclaimer in 10 seconds and know:

1. What the product is (operating system, not signal service, not bot)
2. Who it's for (disciplined crypto-perp traders)
3. What state it's in (testnet, validation-phase)
4. What it enforces (the buyer's framework, gates first-class)

---

## 7. Sub-headline direction (other pages)

### About page

> CoinScopeAI is a UAE-built, AI-driven trader operating system for disciplined crypto-perp traders. We're in a 30-day validation phase against published Production Candidate Criteria. Founder: [Mohammed].

### Pricing page

> Three tiers: Free / Trader $79/mo / Desk Preview $399/mo. Desk Full v2 launches in P5 (Mar–May 2027) at $1,199/mo + per-seat. Founder-cohort terms available during P1 (June 2026).

### Trader-tier landing

> Personal risk infrastructure for the disciplined retail crypto-perp trader.

### Desk Preview-tier landing

> Multi-account discipline + programmable risk for engineer-traders and solo PMs.

### Desk Full v2-tier landing (post-P5)

> Institutional-grade signal/risk platform for solo portfolio managers and small funds.

### Documentation / API page

> Read API at Desk Preview. Documented payloads on /scan, /risk-gate, /position-size, /regime/{symbol}, /performance, /journal.

### Status / incident page

> Postmortems published in product-tier voice. Testnet status: live. Real-capital status: gated.

---

## 8. Product page / in-product message structure

In-product copy follows the **product-tier voice**: terse, declarative, data-led, no marketing fluff, no emoji.

### Voice rules in product

- Numbers are first-class, surfaced when relevant (e.g., "Drawdown: 4.2% / 10.0% threshold")
- Refusals show the gate, not generic "blocked" copy
- Regime + confidence + gate result on every signal payload (canonical)
- Telegram and dashboard share the canonical payload — never two different schemas
- Scoopy speaks in product-tier only; no marketing-tier voice in-product
- **AI is implied by features** (regime classifier, confluence scoring, signal context) — never branded as a feature in-product. "AI-driven" as a modifier is approved on brand-tier surfaces only (homepage, about, sales, recruiting). See §0 Voice taxonomy.

### Standard in-product patterns

| Pattern | Example |
|---|---|
| Signal | "Long BTC @ 67,420. Confidence 0.72. Regime: Trending. Gate: pass." |
| Refusal | "Rejected — exposure cap 4.0x reached. Close a leg or wait for gate relax." |
| Configuration nudge | "Drawdown: 8.4% / 10% threshold. Daily loss limit reset in 6h 12m." |
| Regime change | "Regime flip: Trending → Volatile. Confidence 0.81. Open positions affected: 2." |
| Onboarding step | "API key required. Read + trade scopes. **No withdrawal scope, ever.**" |

The opposite — what is **disallowed** in product:

- "🚀 Welcome to CoinScopeAI! Let's get you trading!"
- "Our intelligent AI is now monitoring your portfolio."
- "Boost your performance with our advanced regime classifier."

---

## 9. Sales / demo message translation

The translation from website → sales conversation. The voice is more direct; the substance is identical.

### Sales open

> "We're an AI-driven trader operating system. We sit between you and your exchange and enforce the discipline you've already built. We're in a 30-day validation phase, on testnet only, with our Production Candidate Criteria published."

### When asked "what makes you different"

> "Three things. One: our risk gates run *before* a trade arms — drawdown, daily loss, leverage, heat — at your thresholds. Two: every signal carries a regime label and a confidence score, paired with the gate result. Three: your capital stays in your exchange account. We never custody, never autonomously execute, never take orders for you."

### When asked "is this a signal service"

> "No. We surface setups, but your gates decide whether they can be armed. The buyer's framework is enforced, not replaced."

### When asked "is this a bot"

> "No. We don't trade for you. You authorize each trade against your own configured gates. We're tools, not advice, not custody, not autonomy."

### When asked "why aren't you production-ready"

> "We are gated against real-capital deployment until our published Production Candidate Criteria pass. The criteria are visible — G1 through G4 plus §8 Capital Cap. We don't claim production-ready until they're met. That's the trust posture."

### When asked "what should I expect from your trial"

> "Connect testnet, configure your thresholds, run alongside your manual workflow. Verify the gate fires when you'd expect; verify the math matches your hand-calculation. If both check, you'll know whether the product respects your framework. If they don't, you'll know to walk."

### When asked about institutional / fund use

> "We don't custody capital, and we're not a fund. At Desk Full v2 we offer institutional-grade signal/risk platform features — multi-account discipline, audit-grade journal, per-seat scaling — that fit a solo PM or small desk. We don't position as a fund-formation alternative."

### Disallowed sales lines

- "Trust me, the AI is amazing." (overclaim)
- "We've helped X traders get Y returns." (performance promise)
- "You'll make money faster than [competitor]." (anti-overclaim)
- "Just connect and we'll do the rest." (autonomy framing)
- "It's basically a hedge fund in your pocket." (custody / fund framing)

---

## 10. Onboarding message structure

The discipline: **first-value before billing**. Every onboarding step earns the next, and the buyer's framework is respected from the first screen.

### Onboarding step hierarchy

| Step | Message direction |
|---|---|
| Signup | "Geography: UAE / MENA / global EN. US: not yet supported." (geofence is honest, not buried) |
| Welcome | "Configure your thresholds. Defaults shown; your rules apply." |
| Exchange connection | "API key required. Read + trade scopes. **No withdrawal scope, ever.** Connect Binance Testnet to get started." |
| First scan | "Here are setups, ranked by confluence. Each carries regime + confidence + gate result against your current thresholds." |
| First gate test | "Try a low daily-loss threshold; attempt to arm a position that breaches it. Observe the refusal." |
| First journal entry | "Captured. Rule-respect: yes. R-multiple: pending close." |
| First Telegram alert (optional) | Canonical payload, rate-limited |
| Trial / paid transition | "First-value pre-billing. Subscribe when the product respects your framework." |

---

## 11. Content narrative themes

Long-form content motion in P1 and P2 should orbit five themes, in priority order. Each theme has multiple posts; each post follows brand-voice rules.

### Theme 1 — Methodology & math (carries D1 + D2)

Posts about position-sizing math, R-multiples, drawdown discipline, regime classification rationale. Example titles:

- "Why we run risk gates before trades arm — and why post-hoc audit isn't enough"
- "How v3 ML labels Trending vs. Mean-Reverting — and what the confidence number actually means"
- "R-multiples for crypto-perp: what changes when funding and OI matter"

### Theme 2 — Validation discipline & PCC (carries D4)

Posts about Production Candidate Criteria, validation-phase posture, anti-overclaim discipline. Example titles:

- "What 'production-ready' means at CoinScopeAI — and why we won't claim it until §8 passes"
- "Anti-overclaim writing: a posture, not a marketing strategy"
- "What our Validation Phase Exit Memo will actually contain"

### Theme 3 — Custody & authorization (carries D3)

Posts about custody-free posture, user authorization, API-key scopes. Example titles:

- "Why your capital stays in your exchange account — and why that's structural, not a feature"
- "Least-privilege API keys: what scopes we ask for, and why"
- "How we think about regulatory direction — UAE, EU, US"

### Theme 4 — UAE / MENA context (carries D5)

Posts about geographic posture, founder context, MENA family-office context, jurisdictional alignment. Example titles:

- "Why CoinScopeAI is built in the UAE — and what that means for our buyers"
- "MENA family-office crypto allocation: what we're seeing"
- "How a UAE entity restructure works — and why we're waiting"

### Theme 5 — Cohort & evidence (post-validation; carries D4)

Posts about cohort observation, retention, gate-fire patterns, cohort-data discipline. Example titles:

- "What our P1 cohort showed about gate-fire patterns"
- "Cohort retention by tier — what we did and didn't expect"
- "Anonymized journal samples: how the journal looks at scale"

The discipline across all themes: **show, don't tell. Every post links a claim to a model, rule, or data artifact. Every post passes brand-voice review before publication.**

---

## 12. Surface-by-surface message map

Voice labels match §0 taxonomy exactly: **Product / Brand / Founder voice / Social**. Register notes appear in parentheses only when material.

| Surface | Lead message | Voice | Disclaimer placement |
|---|---|---|---|
| Homepage hero | Master message + S1 | Brand | Visible above the fold |
| About page | S3 + founder context | Brand (founder section may shift to Founder voice) | Above the fold |
| Pricing | Tier matrix + Trader anchor | Brand | Footer |
| Trader landing | "Personal risk infrastructure" | Brand | Above the fold |
| Desk Preview landing | "Multi-account discipline + programmable risk" | Brand | Above the fold |
| Desk Full v2 landing (post-P5) | Option D language + per-seat | Brand | Above the fold |
| Documentation | Feature-named, terse | Product | Documentation header |
| Status / incidents | Postmortem / incident voice | Product (postmortem register) | Header banner |
| Sales conversation | S1 + S2 + S3 (in order) | Founder voice | Stated explicitly |
| Onboarding (in-product) | Per `onboarding message structure` above | Product | Header banner |
| Telegram alerts | Canonical payload only | Product | Per-message footer |
| In-product (Scoopy) | Per product-tier voice rules | Product | Stated when discussing risk numbers |
| Long-form blog | Per `content narrative themes` | Founder voice | Footer |
| Social (X / Threads) | Per locked v1 product/social separation | Social | Restated when claims approach the line |
| Investor leave-behind | S3 + S1 | Brand | On cover / first page |
| Recruiting page | S3 + founder context + recruiting paragraph from `02-company-overview/company-overview.md` | Brand (founder paragraph may shift to Founder voice) | Above the fold |

---

## 13. Cross-references

- Master message source: `business-plan/01-executive-summary.md`
- Locked v1 brand-voice rules: `business-plan/09-brand-messaging.md`
- Positioning statement: `05-positioning/positioning-statement.md`
- Category decision: `05-positioning/category-decision.md`
- Differentiation framework: `05-positioning/differentiation-framework.md`
- Strategic constraints (locked phrasing): `02-company-overview/strategic-constraints.md`
- Pains, triggers, WTP (messaging implications): `04-icp-and-segmentation/pains-triggers-wtp.md`
- Alerting design rules: `alerting-and-user-experience` skill
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
