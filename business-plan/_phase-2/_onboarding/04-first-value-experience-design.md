# ONBOARDING — First Value Experience Design

**Task:** `[DOC] ONBOARDING — First Value Experience Design`
**Type:** NOW
**Owner:** Strategy CoS + Design
**Status:** DRAFT v0.1 — first-30-minutes script per persona
**Anchored to:** `01-first-time-user-journey.md` gate 4; `02-activation-milestones-definition.md` F-3 + F-4 milestones; engine API endpoints (/scan, /risk-gate, /position-size, /regime/{symbol}); Scoopy custom instructions (regime tokens, risk thresholds canonical 5, validation disclaimer); §6.5 Free Scope B locked features.
**Feeds decision:** **On-2**.

---

## 1. The first-value moment

**Definition:** The first 5–30 minutes of a user's first dashboard session, immediately after Step 9 (post exchange-connect). This is the trust demo. It determines whether the user comes back.

**On-2 recommendation:** Option (c) — *both* top-5 signals + regime label visible AND demo-trade gate decision shown, sequentially, within 5 minutes.

**Why both, sequentially:**

- Signals + regime is the *what*: "the system is doing this, classifying the market like this."
- Demo gate decision is the *why-this-matters*: "the system would have either let you take this trade or stopped you, with reasoning."
- Either alone is half the trust signal. Together, they demonstrate the methodical, evidence-led BRAND voice that distinguishes CSAI from signal-services and bot platforms.

---

## 2. The first-value page (universal layout)

All personas land on the same page after Step 9. Persona-specific framing comes from in-line tour overlays (optional, dismissible) and the persistent `Methodology` link in the nav.

### Layout (top to bottom)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ [Header — fixed]                                                        │
│  CoinScopeAI · Free · Connected: Binance USDT-M (Testnet)              │
│  [Testnet only · 30-day validation · No real capital] (badge)          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Welcome, [Name].                                                       │
│                                                                         │
│  Below: top-5 signals from the engine, refreshed daily, 15-min          │
│  delayed on Free. Each signal includes the regime classification.       │
│                                                                         │
│  Click any signal to see the demo-trade gate decision the engine would  │
│  apply if you were trading it.                                          │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ TOP 5 SIGNALS  ·  Last refresh: [timestamp, 15-min delayed]            │
│                                                                         │
│  1. BTCUSDT      Long      Regime: Trending     [Click to inspect]     │
│  2. ETHUSDT      Short     Regime: Mean-Reverting                       │
│  3. SOLUSDT      Long      Regime: Volatile                             │
│  4. AVAXUSDT     Long      Regime: Trending                             │
│  5. DOGEUSDT     —         Regime: Quiet — most signals suppressed      │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ DEMO-TRADE GATE DECISION  ·  Latest demo trade on your account context │
│                                                                         │
│  Symbol: BTCUSDT      Direction: Long                                   │
│  Regime: Trending     Confidence: [shown to T+ only on Free]            │
│                                                                         │
│  Gate result: REJECTED                                                  │
│                                                                         │
│  Reasoning:                                                             │
│   • Position heat would exceed cap (current 78%, attempt would push    │
│     to 85%, cap is 80%).                                                │
│   • Open positions: 3 of 5 limit.                                       │
│   • Daily loss: 2.1% of cap (5%).                                       │
│   • Account drawdown: 4.2% of cap (10%).                                │
│                                                                         │
│  This is a demo trade. No real order was placed.                        │
│                                                                         │
│  [Why these limits?] → links to engine methodology + risk-gate docs    │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ [Footer — fixed]                                                        │
│  Capital Cap: 10x leverage · 10% drawdown · 5% daily loss               │
│  · 5 open positions · 80% position heat                                 │
│                                                                         │
│  Production Candidate Criteria v2 §8 enforces all caps.                 │
│  [Engine status]   [Methodology]   [What we don't do]                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why this layout

- **Top:** validation badge is unmissable. Per Scoopy custom instructions — risk surface pairs with the canonical disclaimer.
- **Welcome paragraph:** one short, declarative paragraph. Not "Welcome to your trading future!" — "Below: top-5 signals..." Functional, methodical, BRAND-voice-compliant.
- **Top-5 signals section:** delivers F-3 (`value.first_signal_seen`). Regime label is the load-bearing methodology disclosure.
- **Demo-trade gate decision section:** delivers F-4 (`value.first_gate_decision_seen`). Reasoning bullets are the trust load — they show the system thinking, not just deciding.
- **Footer:** canonical 5 risk tokens reproduced verbatim. PCC v2 §8 referenced. Engine status + methodology + "what we don't do" are public links.

---

## 3. Per-persona framing (optional in-line tour overlays)

Each persona has a 3-step in-line tour overlay (dismissible at any step) that lands on persona-relevant elements. Persona is inferred from signup behavior or explicitly chosen via "What kind of trader are you?" optional self-select post-Step 9.

If persona is unknown, no tour overlay shows; user explores the layout self-directed.

### Persona overlay — Omar (P1 Methodist)

**Step 1 (anchor: regime label on signal #1):**
> "Each signal carries a regime label: Trending, Mean-Reverting, Volatile, or Quiet. The regime classifier is part of why a signal exists at all — Quiet regimes suppress most signals."

**Step 2 (anchor: demo gate decision section):**
> "Below the signals, a demo-trade gate decision shows what the engine would do with a hypothetical trade on your account. Notice the reasoning: position heat, open positions, drawdown, daily loss. The system enforces discipline before generating a trade idea."

**Step 3 (anchor: methodology link):**
> "The methodology page documents how the regime classifier and risk gate work. Read it. The system isn't a black box."

**Why this framing for Omar:** Omar's buying frame is "does this respect my framework?" The overlay surfaces the methodology + the discipline-enforcer behavior, which is what Omar is evaluating.

### Persona overlay — Karim (P2 Engineer Trader)

**Step 1 (anchor: regime label):**
> "Regime classifier is v3 ML — Trending / Mean-Reverting / Volatile / Quiet. Confidence score is included on Trader+. Methodology page documents the classifier."

**Step 2 (anchor: demo gate decision section):**
> "Risk gate is rule-based, deterministic, exposed via the `/risk-gate` API endpoint on Trader+. Gate decision logs are auditable per signal."

**Step 3 (anchor: API docs link in nav):**
> "API access is rate-limited on Trader (~1 req/sec/endpoint), standard rate on Desk Preview. The `/scan`, `/risk-gate`, `/position-size`, `/regime/{symbol}` endpoints are the surface. Backtest sandbox is on Desk Preview."

**Why this framing for Karim:** Karim's buying frame is "is the methodology credible? is the API depth sufficient?" The overlay surfaces the engine surface + API depth + the "deterministic, auditable" framing that signals build-quality.

### Persona overlay — Layla (P3 Solo PM)

**Step 1 (anchor: connected exchange in header):**
> "You've connected one Binance account. Multi-account aggregation across exchanges is on Desk Preview — useful when you're tracking your own book + close-circle partner accounts."

**Step 2 (anchor: demo gate decision section):**
> "The demo-trade gate decision shows what the engine would enforce on this account. Multi-account heat visualization (Desk Preview) shows the same gate logic across your full book."

**Step 3 (anchor: roadmap / "Talk to founder" CTA):**
> "Audit-grade partner reporting (LP-style) is on the v2 roadmap (Mar–May 2027). For Desk Preview onboarding or to talk through your book setup, [Talk to founder]."

**Why this framing for Layla:** Layla's buying frame is "does this look professional? does it scale with me?" The overlay surfaces the multi-account view (DP-tier) + v2 roadmap + the "Talk to founder" path that her cohort expects.

### Persona overlay — sub-$5k disciplined

**No persona overlay.** Persistent in-product banner at top: "We'll be back for you when your account crosses $5k. Trader unlocks then." Per `_packaging/02` §3.

The first-value page itself is identical to standard onboarding — sub-$5k user sees top-5 signals + demo gate decision in full Free Scope B form. The only difference is the persistent banner + opt-in "Notify me at $5k."

---

## 4. The first 30 minutes — script

Approximate user behavior on the first-value page, by persona. Used to validate UX flow + spec the in-line tour timing.

### Omar (P1) — first 30 minutes

| Time | Behavior | What he learns |
|---|---|---|
| 0–2 min | Reads welcome paragraph; scans top-5 list; notices regime labels | The system classifies regime + ranks signals |
| 2–5 min | Clicks top signal (BTCUSDT) → demo gate decision view | The system would have stopped him from this trade because of position heat — this is the discipline demo |
| 5–10 min | Reads gate decision reasoning + clicks "Why these limits?" | Risk gate rules are documented + traceable to PCC v2 §8 |
| 10–20 min | Returns to top-5 list; explores 2–3 more signals + their regimes | The regime classifier is consistent + interpretable |
| 20–30 min | Clicks Methodology link; reads engine documentation | The system is methodologically transparent — no black box |

**Activation:** F-1 + F-2 + F-3 + F-4 cleared by minute 5. F-5 (methodology viewed) cleared by minute 30. Trader-conversion intent forms over next 14–60 days as Omar returns.

### Karim (P2) — first 30 minutes

| Time | Behavior | What he learns |
|---|---|---|
| 0–2 min | Skims welcome; clicks Methodology link in nav before exploring signals | Methodology depth is the gate to engagement |
| 2–10 min | Reads engine methodology end-to-end; checks regime classifier specifics | Classifier is v3 ML, deterministic risk gate, documented |
| 10–15 min | Returns to first-value page; clicks demo gate decision | Risk gate produces auditable, parameterizable decisions |
| 15–25 min | Tests `/scan` endpoint (Trader API surface); checks rate limits | API depth meets buy-vs-build threshold |
| 25–30 min | Reviews engine status / uptime page in footer | Operational maturity signal |

**Activation:** F-1 + F-2 + F-3 + F-4 + F-5 cleared by minute 15. Trader-conversion intent forms within 7–14 days (faster than Omar — engineer mindset converts on credibility, not gradual trust).

### Layla (P3) — first 30 minutes

| Time | Behavior | What he learns |
|---|---|---|
| 0–3 min | Reads welcome; notices "single account connected" framing | Multi-account is a differentiated tier (DP) — explicit |
| 3–10 min | Reviews top-5 signals; clicks demo gate decision | Risk gate is structured, professional in tone — signals to her partners |
| 10–20 min | Reads gate decision reasoning + clicks "Why these limits?" + reviews "what we don't do" | The product is positioned conservatively — defensible to partners |
| 20–30 min | Clicks "Talk to founder" CTA on Desk Preview tier OR self-serves to DP signup | Professional onboarding path available |

**Activation:** F-1 + F-2 + F-3 + F-4 cleared by minute 10. F-5 + DP intent forms by minute 30. Conversion to DP within 3–7 days.

### Sub-$5k disciplined — first 30 minutes

| Time | Behavior | What they learn |
|---|---|---|
| 0–2 min | Reads welcome + persistent "we'll be back" banner | They are recognized as future-ICP, not as second-class |
| 2–10 min | Explores top-5 signals + demo gate decision | Same trust demo as $5k+ users |
| 10–20 min | Sees "Notify me at $5k" opt-in CTA; opts in | Path to Trader is structured + low-effort |
| 20–30 min | Bookmarks the dashboard; closes session | Comes back when account approaches $5k |

**Activation:** F-1 + F-2 + F-3 + F-4 cleared. Conversion deferred until account-size event triggers $5k threshold.

---

## 5. The five "no-overclaim" guardrails on first-value

The first-value page is the highest-leverage trust surface. Five anti-overclaim guardrails enforced:

1. **Validation badge in header.** Always visible during validation phase.
2. **Demo-trade gate decision shows reasoning.** Pass/fail without reasoning is theatre. Bullets show position heat, open positions, drawdown, daily loss values vs caps.
3. **Canonical 5 risk tokens in footer.** Reproduced verbatim from Scoopy custom instructions: 10x / 10% / 5% / 5 positions / 80% heat.
4. **PCC v2 §8 referenced explicitly.** Footer ties caps to the canonical document.
5. **No "execute live" or "trade real money" copy.** PCC v2 §8 governs that path; until gates pass, the language is "demo-trade" or "testnet."

---

## 6. The two "trust amplifier" elements

Two elements amplify the trust signal beyond the minimum:

1. **Engine status / uptime page link.** Public, unauthenticated, real-time. Per BRAND voice — operational transparency. A signal that we know our engine has uptime obligations + we publish them.
2. **"What we don't do" reference page link.** Per §5.3.4 + Scoopy custom instructions. Pre-emptively addresses: "we don't promise returns, we don't trade for you, we don't custody funds, we don't replace your judgment."

Both are linked from the footer of every page including the first-value page.

---

## 7. Failure modes specific to first-value

- **Top-5 signals empty on first load.** First impression failure. If the engine has no signals to surface (e.g., all symbols in Quiet regime), show explicit "All symbols currently in Quiet regime — most signals suppressed. The system surfaces signals when conditions warrant; sometimes that's no signals." Frame the absence as evidence of discipline.
- **Demo gate decision unavailable on first load.** Can't render F-4 = trust demo failure. If account-context isn't yet processable (race condition with Step 8 validation), show "Generating your first demo gate decision — this takes up to 30 seconds." Auto-poll.
- **Regime label without explanation.** New user sees "Trending" / "Mean-Reverting" / "Volatile" / "Quiet" with no context. Hover-reveal definitions — at minimum, the regime token color (per Scoopy custom instructions) helps but text definition is required for accessibility.
- **Confidence score visible on Free.** Per `_packaging/02` row A — confidence is T+ only. If confidence leaks into Free, gating violation.
- **"Welcome to your trading future!" copy.** Social-tier register. Violation of Scoopy product-tier rule.
- **In-line tour overlay non-dismissible.** Anti-pattern. Tour must be dismissible at every step.
- **Conversion prompts on first-value page.** Per `01-first-time-user-journey.md` §5 — gate 4 is sacred for trust demo. No "Upgrade to Trader" copy on this page. Conversion comes at gate 5.

---

## 8. What this unlocks

- **On-2** can be marked recommended at "both top-5 signals + regime label AND demo-trade gate decision shown sequentially within 5 minutes."
- `[QA] ONBOARDING — Friction Audit Across Current Flow` has the canonical first-value layout to audit against.
- ONBOARDING NEXT `Onboarding Copy Pack` consumes every text block in §2 + §3 as canonical.
- ONBOARDING NEXT `New User Education Sequence` has the persona-overlay content as the seed for the in-app education cadence.
- §13 KPI framework gets explicit F-3 + F-4 + F-5 timing targets per persona for activation funnel monitoring.
- Eng has a deterministic spec including: demo-gate-decision rendering within 30s, regime-label hover-reveal, persona-overlay infrastructure, footer-link inventory.
