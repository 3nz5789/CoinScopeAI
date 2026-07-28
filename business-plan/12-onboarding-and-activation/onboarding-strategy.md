# Onboarding Strategy

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md`; `business-plan/_phase-2/_onboarding/05-friction-audit-across-current-flow.md`

---

## 1. Onboarding philosophy

Five operating beliefs, in order of weight.

1. **Onboarding is a trust transition, not a UX flow.** The buyer is not learning to use a tool; they are deciding whether to extend trust to a product that will sit between them and their capital. Every step is judged on whether it earns or spends that trust.
2. **Friction is a filter, not a defect.** Some steps that would be removed at a typical SaaS product (account verification, exchange-connection at signup, US-block enforcement) are the cohort filter at CoinScopeAI. Removing them attracts anti-ICP signups; keeping them earns the right to address P1 Omar's pattern.
3. **First value precedes commitment.** A user must see something useful before they pay, configure, or invite others. The Free tier's job is to deliver that. Onboarding's job is to surface it cleanly.
4. **Speed and trust are not opposites — but speed is a function of trust.** A buyer evaluating CoinScopeAI moves fast when they understand what they're seeing and slow when they don't. Adding "engagement" mechanics (countdown timers, urgency CTAs) does not accelerate genuine evaluation; it triggers skepticism and stalls it.
5. **The onboarding voice is the brand voice.** Product-tier (terse, technical, declarative, anti-overclaim) — not social-tier. Onboarding copy passes the same brand-voice review as any other surface. No emoji parade, no "Welcome aboard! 🚀", no "You're in!" theatre.

The synthesis: **onboarding is the product's first promise about itself**. If the product later behaves more disciplined than the onboarding implied, that's wasted trust. If it behaves less disciplined, that's broken trust. Onboarding sets the calibration.

---

## 2. Who onboarding is designed for first

**P1 Omar (Self-Taught Methodist) is the primary onboarding archetype.** Inheriting `04-icp-and-segmentation/primary-icp.md` and `_phase-2/_onboarding/01-first-time-user-journey.md` Swim-lane A.

| Persona | Onboarding shape | Time-to-first-value | Conversion path |
|---|---|---|---|
| **P1 Omar** (primary) | Self-serve, methodology-rich, no kickoff call required (cohort kickoff offered) | <15 min from signup to first-value page | Free → Trader on day 30–60 after methodology proves credible |
| **P3 Layla** (strategic secondary) | Self-serve OR assisted via "Talk to founder" CTA on Desk Preview pricing card | 20–30 min on first-value page; founder kickoff call optional | Free → Desk Preview within 3–7 days |
| **P2 Karim** (watch-list) | Self-serve, methodology-deep evaluation, API docs visible early | <60 min on first-value page; methodology re-read often | Free → Trader within 7–14 days; Trader → Desk Preview when API limit binds |
| **Sub-$5k disciplined** (pre-ICP) | Self-serve, identical Free Scope B, "we'll be back" routing instead of upgrade pressure | Variable; depends on account size growth | "Notify me at $5k" subscription opt-in; convert when threshold crosses |
| **US-resident** | Blocked at Gate 1 with copy explanation | n/a | n/a (until US licensure decision) |
| **Anti-ICP (signal-seekers, copy-trade audience)** | Self-deselect via the Free Scope B (no signals delivered as recommendations; no copy-trade affordances; "what we don't do" page visible) | n/a | n/a |

The anchor: **design the Trader-bound P1 Omar journey first; verify it works for P3 Layla and sub-$5k handling; verify P2 Karim reads it as credible.** The Trader-bound flow is the canonical journey; everything else is a deliberate variant.

---

## 3. Recommended onboarding flow

Inherits the locked six-gate journey from `_phase-2/_onboarding/01-first-time-user-journey.md` §1, restated here with operator-level commentary.

### 3.1 Six gates

```
Gate 0 — Pre-signup
       Landing page → pricing page → "Verify Account" CTA
                  ↓
Gate 1 — Region check
       US-resident → blocked with copy → END
                  ↓ (allowed)
Gate 2 — Signup + email verify
       Email + password; verify-email link click
                  ↓
Gate 3 — Exchange connect
       Binance USDT-M API key (read-only); testnet-first explanation visible
                  ↓
Gate 4 — First value
       Top-5 signals + regime label + demo-trade gate decision
       (the load-bearing trust moment)
                  ↓
Gate 5 — First conversion event
       Either Free → Trader upgrade OR Free retention to first weekly digest
```

### 3.2 What each gate does — and what it does not

| Gate | What it does | What it does NOT do |
|---|---|---|
| **0 Pre-signup** | Sets pricing/positioning expectation; surfaces validation-phase status | Does not gate or bind the user; no commitment yet |
| **1 Region check** | Enforces US-block at signup; honors strategic constraint | Does not collect any data from blocked users beyond the IP/region hint |
| **2 Signup + email verify** | Establishes account-level identity; standard auth pattern | Does not require credit card; does not require API keys yet |
| **3 Exchange connect** | Captures account size band, exchange context, testnet-or-mainnet selection | Does not require **write** scopes; never requests withdrawal scopes; least-privilege only |
| **4 First value** | Renders the trust demo: top-5 signals, regime label per signal, demo-trade gate decision; validation-phase footer prominent | Does not surface paid-tier features; does not nag for upgrade; does not show fake performance numbers |
| **5 First conversion event** | Either the Free retention loop completes (weekly digest opt-in) or the Free → Trader upgrade fires on a discrete intent moment (e.g., attempted journal action) | Does not auto-charge; does not surface countdown timers; does not lock the buyer in |

### 3.3 Time-to-value targets (from `_phase-2/_onboarding/01-first-time-user-journey.md` §3)

| Milestone | Target time post-signup | Anti-target (drop-off signal) |
|---|---|---|
| Email verified | <5 min | >24 h = lost |
| Exchange account connected | <15 min | >24 h = abandoned signup |
| First signal seen | <5 min after exchange-connect | >24 h = inactive |
| First gate decision seen | <10 min after exchange-connect | Never seen = trust demo failed |
| First conversion event | Free → Trader: 14–60 days; Free retention: 7-day digest opt-in | >30 days dormant after first signal = at-risk |

These are **observation targets**, not gameification levers. The dashboard shows them in the cohort observation deck; ops uses them to spot stuck users; we do not surface them as "you haven't activated yet" prompts to the buyer.

---

## 4. Balancing speed vs. trust vs. education

Three forces in tension at every gate. The balance differs by gate.

| Gate | Speed weight | Trust weight | Education weight | What this looks like |
|---|---|---|---|---|
| **0 Pre-signup** | Low | High | Medium | Pricing page is allowed to take 5 min to read; methodology page available alongside |
| **1 Region check** | High | Medium | Low | <30s; copy is honest, not adversarial |
| **2 Signup + email verify** | High | Medium | Low | Standard form; methodology link visible; no in-form education clutter |
| **3 Exchange connect** | Medium | **Highest** | Medium | Take time to explain testnet-first, least-privilege scopes, "no withdrawal scope ever"; do not rush this gate |
| **4 First value** | Medium | High | High | Render fast, but show enough that the buyer can read regime + confidence + gate result and understand what they're seeing |
| **5 First conversion event** | Low | High | Low | No urgency; conversion happens on a discrete intent moment (attempted journal action), not on a timer |

**The cardinal rule:** **trust outranks speed at the high-stakes gates** (3 and 4). A buyer who connects an exchange in 3 minutes but doesn't trust why we asked for read-only is more likely to churn than one who took 12 minutes and feels confident.

Education is **embedded, not interruptive**. Tooltips and inline explanations are good; modal popups, tutorial overlays, and "click here next" arrows are anti-pattern for a P1-Omar-shaped buyer.

---

## 5. Where exchange connection, scanner discovery, billing, and setup belong in the flow

### 5.1 Exchange connection — Gate 3 (mandatory pre-first-value)

- **Why here:** First-value cannot be rendered without an exchange context. The top-5 signals + regime + demo-gate-decision view is account-aware (even on Free, it shows the user's actual account size band so the demo-trade is contextualized).
- **What's required:** Binance USDT-M API key, read-only scopes, testnet-or-mainnet selection.
- **What's not required:** Withdrawal scopes (never requested). Funding addresses (never requested). Personal financial data beyond what the exchange API exposes via read scope.
- **Failure handling:** If exchange-connection fails (wrong permissions, expired key, IP-restricted), inline error explains the specific cause and links to the troubleshooting doc. **REQUIRED INPUT** — the troubleshooting doc must be live by P1 launch.
- **Why not deferred:** A "skip exchange connection for now" path was considered and rejected. It produces accounts with no first-value possibility, which then need a re-entry flow that doubles complexity without solving the underlying problem.

### 5.2 Scanner discovery — Gate 4 (the load-bearing trust moment)

- **Why here:** This is where the buyer learns what the product actually does. The top-5 signals + regime + confidence + demo-gate-decision is the trust demo.
- **What it shows:** Read-only top-5 (Free) or full feed (paid); regime label on every signal; confidence score (paid) or label-only (Free); demo-trade gate result with explicit gate-that-fired explanation.
- **What it does not show:** Performance claims; aggregated user PnL; "popular" or "most-traded" signals; leaderboard-style rankings.
- **Validation-phase footer:** Visible on this surface. "Testnet only. 30-day validation phase. No real capital." stays visible during scanner discovery; it is not optional copy.

### 5.3 Billing — Gate 5 (only at intent moment, never forced)

- **Why here:** The first conversion event happens when the user has an explicit intent (e.g., attempted journal action requires Trader). Billing is **never** forced before first-value.
- **What's enforced:** Trial mechanism is the 14-day money-back guarantee on first paid charge, paired with the Free tier as evergreen evaluation. No card on file at signup.
- **What's not done:** Card-on-file with auto-charge after a free trial period. Pre-loaded credit. "Start your free trial" framing — Free is the trial.
- **Founder-cohort window:** If the user signed up during the founder-cohort 60-day window, that pricing applies automatically at Gate 5; the buyer does not have to "remember" or "redeem" anything.

### 5.4 Setup (risk-gate configuration, journal start, Telegram link) — post-first-value, on intent

- **Why here:** Setup tasks (configuring custom risk-gate thresholds above the locked floors, starting a journal, linking Telegram) require the buyer to have **already understood** the trust demo. Forcing setup pre-first-value would compress the trust transition.
- **What ships in the first session post-payment:**
  - Risk-gate configuration UI is visible (with sensible defaults pre-populated)
  - Journal entry-creation is available
  - Telegram bot link is a single-click setup
- **What's not forced:** None of these are blocking. The buyer can use Trader without configuring custom thresholds (locked floors apply by default), without journaling (auto-import covers most flows), and without Telegram (dashboard works standalone).

---

## 6. What should be self-serve vs. assisted

### 6.1 Self-serve (default for all personas)

- Pre-signup, signup, email-verify, region-check (Gates 0–2)
- Exchange connection (Gate 3) — with inline troubleshooting and a documented self-help path
- First-value rendering (Gate 4) — fully automated from exchange-connection completion
- Free-tier ongoing engagement (Gate 5 retention path)
- Trader subscription activation, billing changes, journal use, Telegram setup
- Tier upgrade (Trader → Desk Preview) at intent moment
- Free → Trader conversion at intent moment

### 6.2 Assisted (founder-led, by invitation)

- **All P1 cohort users (40 P1 users)** — optional founder kickoff call within the first 7 days post-signup. ~10–15 minutes; founder-led; structured (not ad-hoc); covers configuration, expectations, and cohort observation cadence.
- **P3 Layla candidates** — "Talk to founder" CTA on the Desk Preview pricing card; founder-led kickoff is mandatory for P3 candidates evaluating during P1 (capacity-constrained; offered to ≤10 P3 candidates per cohort).
- **Edge-case high-account-size signups** during P1 — at founder discretion, a kickoff call may be offered for users at the upper bands ($150k+ Trader-tier signups).

### 6.3 Why this split

- Self-serve is the rule because P1 Omar's buying pattern is **slow, reading-heavy, evaluation-on-their-own-time**. Forcing a sales call breaks this pattern.
- Assisted is the exception because P1 cohort users earn extra attention (the cohort is the marketing) and P3 Layla's WTP justifies the founder-time investment.
- Beyond P1, assisted onboarding scales only if/when a vetted contractor takes over the kickoff function under brand-voice review. Founder time is the binding constraint until then.

### 6.4 What never becomes assisted

- Anti-ICP signups (signal-seekers, copy-trade audience) — they self-deselect via the Free tier; we do not assist their conversion.
- Sub-$5k signups — handled by the "we'll be back" mechanism; no assisted onboarding.
- US-residents — blocked at Gate 1; no assistance offered.

---

## 7. Onboarding risks to avoid

Eleven failure modes with specific guards.

| # | Risk | Why it kills CoinScopeAI specifically | Guard |
|---|---|---|---|
| **OR1** | **Forcing card-on-file at signup** | Anti-ICP filter inversion; pulls extraction-minded users; conflicts with "Free is the trial" mechanism | No card at signup; billing only at intent moment (Gate 5) |
| **OR2** | **Skipping exchange-connection at signup** | Account with no first-value possibility; doubled complexity in re-entry flow | Exchange-connect is mandatory at Gate 3 |
| **OR3** | **Requesting withdrawal scopes in the API key** | Trust collapse; brand contamination; existential | Read-only scopes only; never requested otherwise |
| **OR4** | **Onboarding copy with marketing language** ("You're in! 🚀", "Welcome aboard!") | Voice incongruence; signals social-tier on a product-tier surface | Brand-voice review on every onboarding string |
| **OR5** | **Tutorial overlays / forced walkthroughs at first-value** | Interrupts the trust demo; treats the buyer as if they need entertainment | Embedded education only; tooltips okay; modal walkthroughs forbidden |
| **OR6** | **Performance numbers in onboarding** ("see how our users gained X%") | Anti-overclaim violation; testnet data does not justify performance claims | Locked — no performance language in onboarding |
| **OR7** | **Urgency theatre** ("Founder-cohort spots are filling fast!") | Manufactured pressure; signals desperation; triggers buyer skepticism | No urgency timers, no "spots filling" copy, no Black Friday patterns |
| **OR8** | **Forced setup before first-value** (configure risk thresholds before showing scanner) | Compresses the trust transition; buyer doesn't know enough to configure intelligently | Sensible defaults pre-populated; setup is post-first-value, on intent |
| **OR9** | **Sub-$5k upgrade pressure** ("Upgrade to unlock journal!") | Anti-ICP; future-ICP routing breaks; cohort signal pollution | "We'll be back" routing per `07-packaging-and-pricing/trial-and-discount-policy.md` §4 |
| **OR10** | **Hidden validation-phase status during onboarding** | Contradicts every other trust surface; cohort buyers notice | Validation-phase disclaimer visible at signup, exchange-connect, and first-value gates |
| **OR11** | **Tutorial videos / "watch this 5-minute intro" gating first-value** | Interruptive; treats the buyer as if they don't read | Optional video; never gates progress; never auto-plays |

The combined rule: **an onboarding pattern that feels normal at a typical SaaS product is often anti-fit at CoinScopeAI**. When in doubt, the test is: *"Does this pattern increase the buyer's trust, or just engagement?"* Engagement-only patterns are rejected.

---

## 8. Where the current app likely needs clarity or support

Wave 1 friction audit (`_phase-2/_onboarding/05-friction-audit-across-current-flow.md`) is the canonical source. Wave 2 highlights the strategic clarity gaps that need attention before P1.

### 8.1 Likely high-priority clarity gaps

| Gap | Why it matters strategically | Recommended action |
|---|---|---|
| **Exchange-connection error states are sparse** | Largest abandonment risk at Gate 3; a confused buyer at this gate is a lost buyer | Documented error states for each Binance API failure mode; inline troubleshooting per error |
| **Validation-phase status visible only in footer** | Onboarding surfaces should restate it at exchange-connect and first-value gates, not just footer | Surface-by-surface anti-overclaim audit before P1 |
| **Free vs. Trader differentiation in first-value page is implicit** | A P1 Omar evaluating Free needs to understand what they're seeing vs. what's behind the upgrade gate, without the page becoming an upgrade ad | Clear, calm "What's in Free / What unlocks at Trader" panel — single, inline, anti-pressure |
| **Sub-$5k "we'll be back" experience design is undocumented in current app** | Without explicit design, default behavior is "show empty paid features" which is anti-ICP | Design pass before P1 launch; copy reviewed via brand voice |
| **Telegram bot link is post-first-value but discovery path may be unclear** | Telegram is a strong activation amplifier; if discovery is broken, amplification is lost | Persistent (but not pushy) link in dashboard sidebar after first-value |
| **Cohort kickoff scheduling lives outside the app** | If founder kickoff calls are routed through email-only, scheduling friction can stretch days | Lightweight in-app booking link for cohort users; founder approval per slot |
| **Reactivation flow** (90-day window) | Locked policy says reactivation restores prior tier and pricing; current flow likely does not differentiate reactivation from new signup | Design pass before P2; document what's preserved vs. reset |

### 8.2 Likely lower-priority clarity gaps

- Methodology page navigation from inside the app (link visibility)
- Risk-gate configuration default-vs-custom labeling
- Journal entry-creation discoverability
- Telegram alert-rate-limit transparency (when alerts are throttled, is that visible to the user?)

These are documented in `_phase-2/_onboarding/05-friction-audit-across-current-flow.md` for design follow-up; they are not P1-launch-blocking.

### 8.3 What is **not** a clarity gap (do not fix)

- The fact that Free is account-verified — this is a feature, not a bug
- The fact that exchange-connection is required at Gate 3 — feature, not bug
- The fact that paid-tier features are not previewed in detail on Free — feature, not bug
- The fact that there is no "free trial of Trader" — feature, not bug

The friction-audit discipline: **distinguish "users are confused because the UX is unclear" (fix) from "users are confused because they wanted a different product" (do not fix; their confusion is the filter working).**

---

## 9. Cross-references

- First-time user journey: `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md`
- Activation milestones: `business-plan/_phase-2/_onboarding/02-activation-milestones-definition.md`
- Signup-to-exchange-connection flow: `business-plan/_phase-2/_onboarding/03-signup-to-exchange-connection-flow.md`
- First-value experience design: `business-plan/_phase-2/_onboarding/04-first-value-experience-design.md`
- Friction audit: `business-plan/_phase-2/_onboarding/05-friction-audit-across-current-flow.md`
- Plan matrix: `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Trial / discount policy: `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Trust-first growth: `business-plan/08-go-to-market/trust-first-growth.md`
- Activation milestones (this folder): `business-plan/12-onboarding-and-activation/activation-milestones.md`
- First-value design (this folder): `business-plan/12-onboarding-and-activation/first-value-design.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
