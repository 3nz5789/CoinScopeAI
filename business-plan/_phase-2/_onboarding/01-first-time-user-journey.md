# ONBOARDING — First-Time User Journey

**Task:** `[DOC] ONBOARDING — First-Time User Journey`
**Type:** NOW
**Owner:** Strategy CoS + Design
**Status:** DRAFT v0.1 — per-persona swim-lane map, end-to-end first-30-days
**Anchored to:** §6.5 Free Scope B (LOCKED); PACKAGING `_packaging/02-free-vs-paid-boundary.md`; PRICING `_pricing/04-trial-and-intro-offer-options.md` (no free trial); §3 personas Omar / Karim / Layla; PCC v2 §8 Capital Cap; Scoopy custom instructions (regime tokens, Telegram bot, validation disclaimer).

---

## 1. Journey shape (all personas)

The journey has six gates. Every user passes through them in order; persona variants change the *content* at each gate, not the sequence.

| # | Gate | What happens | Failure = drop-off |
|---|---|---|---|
| 0 | Pre-signup | Landing page → pricing page → "Verify Account" CTA | User leaves; no account created |
| 1 | Region check | US blocked at signup before any other friction | User sees "Not currently available in your region"; no account |
| 2 | Signup + email verify | Email + password; verify email link | Email link not clicked; account inactive |
| 3 | Exchange connect | Binance USDT-M API key (read-only); testnet-first | API key entry abandoned; account verified-but-unconnected |
| 4 | First value (Free) | Top-5 signals + regime label + demo-trade gate decision visible within 5 minutes | User sees the page but doesn't engage; bounce |
| 5 | First conversion event | Either Free → Trader upgrade OR Free retention to first weekly digest | Neither happens; cohort moves to "dormant" segment |

Gate 4 (first value) is the load-bearing trust moment. Gate 3 (exchange connect) is the highest-friction conversion step. Gate 5 (first conversion event) is the §13 KPI handoff.

---

## 2. Per-persona swim-lanes

Personas: Omar (P1 Self-Taught Methodist), Karim (P2 Engineer Trader), Layla (P3 Solo PM, $200k–$1M aggregate book).

### Swim-lane A — Omar (P1 Methodist)

**Profile reminder:** Account size $20k–$150k typical; cobbling TradingView + Tradervue + Edgewonk + occasional CoinGlass (~$200/mo cobbled bundle); buying frame is "does this respect my framework and replace what I'm cobbling?"

| Gate | What Omar sees | What Omar does | Time |
|---|---|---|---|
| 0 | Pricing page; Trader $79 anchor; "stabilizing in cohort" status visible | Reads tier comparison, lands on Trader card | 3–5 min |
| 1 | Region OK (assume MENA / global EN) | Continues to signup | <30s |
| 2 | Signup form: email + password; methodology link visible | Signs up; clicks verify-email link | 2 min |
| 3 | Exchange connect: Binance USDT-M, read-only API key, testnet-first explanation | Enters API key; confirms account at $30k mainnet (or $1k testnet for trial-runners) | 5–10 min |
| 4 | First-value page: top-5 signals + regime label per signal + demo-trade gate decision; "Testnet only" badge prominent | Reads top-5; hovers regime labels; reviews one demo-trade gate decision in detail | 10–15 min |
| 5 | Free retention; weekly digest opt-in confirmed | Returns within 7 days for second look at signals; reviews methodology docs | T+7d |
| Conversion path | After 14–30 days of Free use, upgrade prompt for Trader appears (single, quiet, inline) on attempted journal action | Upgrades to Trader on day 30–60 if methodology proves credible | T+30–60d |

**Omar's "aha" moment:** seeing a gate decision rejection on a demo trade with explicit reasoning — "the system is not just a signal generator; it's a discipline enforcer."

### Swim-lane B — Karim (P2 Engineer Trader)

**Profile reminder:** Account size $50k–$200k typical; cobbling TradingView + QuantConnect + Nansen + CryptoQuant (~$300/mo + opportunity cost on personal backtest framework); buying frame is "is the methodology credible? is the API depth sufficient? is this cheaper than building it myself?"

| Gate | What Karim sees | What Karim does | Time |
|---|---|---|---|
| 0 | Pricing page; reads Trader card → flips to engine methodology docs (public per §5.3.1) | Reads methodology fully; checks API rate limits in tier comparison | 10–20 min |
| 1 | Region OK | Continues to signup | <30s |
| 2 | Signup form; clicks methodology link first to re-confirm before signup | Signs up; verifies email | 2 min |
| 3 | Exchange connect: Binance USDT-M, read-only API key | Enters API key; confirms account at $80k mainnet | 5 min |
| 4 | First-value page: top-5 signals + regime + confidence scores (Karim is on Free, sees label only); per-signal trace visible (T+ feature, but Karim previews via methodology page) | Reads regime classifications; mentally tests the regime classifier against a recent market move he remembers | 15–20 min |
| 5 | Free retention; reviews engine status / uptime page; bookmarks API docs | Returns within 3 days to check methodology updates and engine status | T+3d |
| Conversion path | Hits API rate limit on Trader-tier API testing → upgrade prompt to Desk Preview triggers | Upgrades to Trader on day 7–14 (faster than Omar — engineer mindset converts on credibility, not gradual trust); upgrades to Desk Preview when API limit binds | T+7–14d Trader, T+90–180d DP |

**Karim's "aha" moment:** confirming the regime classifier matches his own read of a recent market regime + seeing per-signal trace (regime + confidence + gate result + sizing rationale) on a Trader-tier signal.

### Swim-lane C — Layla (P3 Solo PM)

**Profile reminder:** Account size $200k–$1M aggregate (own + close-circle partners); cobbling TradingView + Tradervue + Nansen Pro + CoinGlass Hyper + research-tier (~$2,100/mo + manual effort); buying frame is "does this look professional to my partners? does it justify cost as % of book? does it scale with me?"

| Gate | What Layla sees | What Layla does | Time |
|---|---|---|---|
| 0 | Pricing page; reads DP card; clicks "Talk to founder" CTA OR self-serves to signup | If self-serve: continues. If "Talk to founder": assisted onboarding (NEXT, **On-7**). | Variable |
| 1 | Region OK | Continues | <30s |
| 2 | Signup form; reviews engine methodology + risk-gate documentation | Signs up; verifies email | 5 min |
| 3 | Exchange connect: Binance USDT-M, read-only API key for primary account ($300k mainnet) | Enters API key; (multi-account is DP+ — only first account at signup) | 5–10 min |
| 4 | First-value page (Free initially): top-5 signals + regime label + demo-trade gate decision; founder-cohort window comms surface | Reads top-5; reviews demo gate; clicks "Founder-cohort pricing — locked through your first renewal cycle" link | 20–30 min |
| 5 | Free retention: 1–3 days. P3 typically converts faster than P1 (higher pain, higher WTP) | Reviews methodology + LP-style reporting roadmap (v2-flagged); converts to Desk Preview within 7 days | T+3–7d DP |
| Conversion path | DP for 6–12 months → Desk Full v2 at v2 launch (Mar–May 2027) with partner seats | Adds 1–3 partner read-only seats at DF v2 launch | T+12–18m DF v2 |

**Layla's "aha" moment:** seeing the multi-account heat visualization preview on the DP card + understanding partner read-only seats are on the v2 roadmap. She doesn't need v2 today; she needs to know it's coming.

### Sub-$5k disciplined branch (cross-persona)

Some users — possibly Omar-aligned, possibly genuine future-ICP rather than current-ICP — sign up with sub-$5k accounts. Per §3.5 + §6.5 + `_packaging/02` §3:

| Gate | What sub-$5k user sees | What sub-$5k user does |
|---|---|---|
| 0–3 | Identical to other personas | Signs up, verifies email, connects Binance account at <$5k |
| 4 | First-value page: identical Free Scope B; persistent in-product copy frames Trader as the destination, not a paywall | Reads top-5; reviews demo gate; sees "we'll be back" framing as future-ICP message |
| 5 | Optional "notify me when account crosses $5k" subscription opt-in | Opts in; returns when account reaches $5k threshold |
| Conversion path | Account-balance event triggers notification → in-product CTA shifts to Trader entry | Converts to Trader within 30 days of $5k threshold (ASSUMPTION — validate via cohort data) |

**Anti-pattern guard reaffirmed:** sub-$5k users do NOT see different (tighter) Free features. NO upgrade-pressure prompts. NO "you're a casual trader" copy. Same Free Scope B; different conversion-trigger mechanics.

---

## 3. Time-to-value targets

| Milestone | Target time post-signup | Anti-target |
|---|---|---|
| Email verified | <5 minutes | >24 hours = lost |
| Exchange account connected | <15 minutes | >24 hours = abandoned signup |
| First signal seen | <5 minutes after exchange-connect | >24 hours = inactive |
| First gate decision seen | <10 minutes after exchange-connect | Never seen = trust demo failed |
| First conversion event (paid OR retention) | Free→Trader: 14–60 days; Free retention: 7-day digest opt-in | >30 days dormant after first signal = at-risk |

Activation funnel KPIs (per `02-activation-milestones-definition.md`) measure these explicitly.

---

## 4. Sequence map

```
Landing page
    ↓
Pricing page (validation disclaimer + tier comparison + founder-cohort window)
    ↓
"Verify Account" CTA
    ↓
[Gate 1] Region check → US blocked → END (with copy)
    ↓ (allowed)
[Gate 2] Signup form (email + password)
    ↓
Verify email link
    ↓
[Gate 3] Exchange connect
    ├─ Binance USDT-M selected (only option at P1)
    ├─ Testnet vs mainnet toggle (testnet-first explanation)
    ├─ API key entry (read-only scope)
    └─ Account size detected
        ├─ ≥$5k → Standard onboarding
        └─ <$5k → Sub-$5k branch (same UI + "we'll be back" copy)
    ↓
[Gate 4] First value (within 5 min)
    ├─ Top-5 curated signals (15-min delayed)
    ├─ Regime label per signal (Trending / Mean-Reverting / Volatile / Quiet)
    ├─ Demo-trade gate decision view (latest decision, with reasoning)
    ├─ "Testnet only · 30-day validation" badge prominent
    └─ Methodology docs link in nav
    ↓
[Gate 5] First conversion event (varies)
    ├─ Free retention → 7-day digest (Free) or daily digest (T+)
    ├─ Free → Trader upgrade (within 14–60 days, single quiet prompt on first journal click)
    └─ Free → Desk Preview upgrade (Layla path; within 3–7 days, "Talk to founder" CTA OR self-serve)
```

---

## 5. Cross-persona patterns (load-bearing for design)

1. **Methodology link is in the nav from gate 0 onward.** Karim reads it twice; Omar references it post-signup; Layla checks it before "Talk to founder." Hiding it behind a conversion event breaks all three personas.
2. **Engine status / uptime page is publicly linked from the footer.** Trust signal per BRAND — operational transparency.
3. **Validation phase status visible on every page**, not just pricing. Per Scoopy custom instructions — disclaimer is universal.
4. **First gate decision must show reasoning**, not just a pass/fail. Reasoning is the discipline-enforcer demo.
5. **Founder-cohort window comms appear at gate 0 (pricing page) AND gate 5 (conversion moment), not in between.** Gate 4 is sacred for trust demo; injecting cohort sales pitch here breaks register.
6. **Telegram nudge is post-first-signal, not at signup.** Per **On-3** option (a) — optional during signup, nudged after first signal demonstrates value.
7. **"Talk to founder" CTA is reserved for Desk Preview / Desk Full v2 cards.** Pricing page never shows it on Trader (which is self-serve only).

---

## 6. Anti-overclaim audit on the journey

| Surface | Audit element | Pass condition |
|---|---|---|
| Pricing page (gate 0) | Validation disclaimer; "stabilizing in cohort" on Trader; founder-cohort window dated | All three present |
| Signup form (gate 2) | No "Trade Smarter — start now" social-tier copy; product-tier register | Verify with Phase 1 BRAND patternbook |
| Exchange connect (gate 3) | Testnet-first explanation; API key scope explicitly read-only; PCC v2 §8 referenced | Real-capital path explicitly gated |
| First value (gate 4) | "Testnet only" badge; first signal includes regime label; demo gate decision shows reasoning | All three present |
| Conversion prompts (gate 5) | Anti-pressure (per `_pricing/02` Principle 5); no "Most popular" badge; no countdown timers | No urgency mechanics |
| Sub-$5k copy | "We'll be back" framing; no paywall pressure | §3.5 + §6.5 alignment |

---

## 7. What this unlocks

- `[DOC] ONBOARDING — Activation Milestones Definition` consumes the 6 gates as instrumentation candidates.
- `[DOC] ONBOARDING — Signup-to-Exchange-Connection Flow` zooms in on gates 1–3.
- `[DOC] ONBOARDING — First Value Experience Design` zooms in on gate 4 per persona.
- `[QA] ONBOARDING — Friction Audit Across Current Flow` audits the documented current product against this journey map.
- ONBOARDING NEXT `Onboarding Copy Pack` consumes the per-gate, per-persona content as the copy inventory.
- ONBOARDING NEXT `New User Education Sequence` consumes gate 5's first-30-days as the cadence horizon.
