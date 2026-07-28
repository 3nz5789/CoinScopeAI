# First-Value Design

**Status:** Wave 2 · v1.1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_onboarding/04-first-value-experience-design.md`; `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md` Gate 4 (the load-bearing trust moment); `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
**Changelog v1 → v1.1:** Free-tier-vs-demo-trade confidence display ambiguity resolved (demo gate decision shows full output regardless of tier as a one-time trust demo; real signal feed shows regime label only on Free per locked Phase 1 §6.5); §1/§2/§3/§4 restructured to remove four-way enumeration overlap (each surface now described once); CA-5/CA-7 counsel-review flag added to the "Action:" line in the demo format; §3.3 persona-cute cadence replaced with operational implication; §4.6 cite corrected; §5 row 4 slogan flagged as DECISION NEEDED; activation-milestones cites added; new §8 failure-mode first-value, §9 mobile-responsive, §10 A/B test discipline, §11 accessibility / readability; cross-references updated.

---

## 1. What first value is

**First value = the moment a new user has seen enough of CoinScopeAI to understand what makes it different and to extend trust to the product.**

For CoinScopeAI specifically, this is **Gate 4 of the onboarding journey** (per `_phase-2/_onboarding/01-first-time-user-journey.md`): a buyer who has signed up, verified email, connected an exchange (read-only), and now sees the surfaces enumerated in §2.

The cardinal property: **a P1 Omar reaching first-value should think "these people understand what they are and aren't"** — same test that applies to the pricing page (per `07-packaging-and-pricing/pricing-strategy.md` §5). Calibration is the message; the surfaces in §2 are how that calibration becomes visible.

---

## 2. What proof looks like — the surfaces

Seven surfaces compose the first-value experience. Each is described once here; design constraints on rendering each surface live in §4.

### 2.1 Top-5 signal feed (real)

The signal feed is the surface most analogous to what the buyer is currently used to (TradingView watchlists, CoinGlass dashboards). Familiar entry point; the differentiator is layered on top.

**On Free:** delayed top-5 (daily refresh) with **regime label only** — no confidence score (per locked Phase 1 §6.5 Free Scope B).

**On paid (Trader and above):** full-fidelity real-time feed with **regime label + confidence score** on every signal.

The regime tokens (Trending / Mean-Reverting / Volatile / Quiet) carry both color and semantic label per the design-system standards in §11.

### 2.2 Demo gate decision (full output, all tiers)

Pre-rendered demo trade exists on every account at first-value, **regardless of tier**. Unlike the real signal feed, the demo gate decision shows the **full output (including confidence) on Free as well as paid** — as a one-time trust-demo carve-out from the locked Free Scope B.

This is a deliberate exception: the locked §6.5 specifies regime-label-only for the *real signal feed*, but the demo trade is explicitly a "demo-trade view of risk gate behavior" (per locked §6.5 wording) — its purpose is showing the buyer what enforcement looks like, which requires the full payload.

Canonical demo format (per Scoopy custom instructions):

```
Demo trade — long BTC @ 67,420
Regime: Trending
Confidence: 0.72
Gate result: REJECTED — exposure cap 4.0x reached
Action: Close a leg or wait for gate to relax
Testnet only. 30-day validation phase.
```

The buyer reads the rejection, sees the reason, and recognizes that the product is doing the gating their methodology already requires. That recognition is the "aha".

> ⚠ **CA-5 / CA-7 counsel-review pending on the "Action:" line.** Per `14-risk-compliance-and-safeguards/compliance-assumptions.md` CA-5 (tools-not-advice) and CA-7 (signals are descriptive engine outputs, not personalized recommendations), the "Action: Close a leg or wait for gate to relax" phrasing reads as borderline-recommendation language. Counsel review may require restating as a non-directive observation (e.g., "Gate relaxes when exposure < 4.0x"). The canonical Scoopy format is locked at engine level; the first-value implementation must match counsel's resolution before public surface ships.

### 2.3 Position-sizing math, hover-revealed

When the buyer hovers the demo gate decision, the position-sizing inputs are visible: account size, risk-per-trade %, stop distance, position size in units, leverage, heat contribution. No hidden math. No black box. The numbers are tabular/monospaced per §11.

### 2.4 Methodology link inline ("How this is calculated")

Every signal surface has a discreet "How this is calculated" link that opens the relevant methodology page section (`coinscope.ai/methodology`). The buyer can dig in if they want; they are not forced to.

Methodology-link click-through correlates with trust-confidence — `12-onboarding-and-activation/activation-milestones.md` §2.1 captures this as F-5 (methodology page viewed), an optional but strong activation indicator.

### 2.5 Validation-phase footer

The footer renders **before** the signal feed loads (per §4.1 ordering). Copy: *"Testnet only. 30-day validation phase. No real capital."* Not a deep-footer note — visible on the surface itself, as a calibration anchor. The buyer who reads this learns that this product means what it says.

### 2.6 "What we don't do" link

A discreet link surfaces from first-value to `coinscope.ai/what-we-dont-do` (one of the five canonical surfaces per `08-go-to-market/trust-first-growth.md` §3.2). The buyer can confirm explicitly that the product they are evaluating is the product they thought they were evaluating. Anti-claim disclosure as continuous trust signal.

### 2.7 Founder-named about page

The about page link is in the footer of every dashboard page; clicking it surfaces the founder named (Mohammed), the sole-prop status disclosed honestly, and the UAE-resident posture stated. A black-box product hides authorship; CoinScopeAI puts a human at every claim.

### 2.8 Exchange-connection scope language (rendered at Gate 3, not Gate 4)

Strictly speaking the exchange-connection screen is upstream of first-value (Gate 3, not Gate 4). It is included here because the trust-establishing copy at this gate calibrates everything that follows. When the buyer enters their Binance API key, the screen states explicitly:

- *"We require **read-only** scopes. Withdrawal scope is never requested."*
- *"We connect to your exchange account; capital stays in your account at all times."*
- *"Testnet first is recommended; real-capital deployment is gated by our published Production Candidate Criteria."*

Inline links to the Binance API key documentation and to `coinscope.ai/methodology`. The buyer is not asked to trust on faith.

---

## 3. What to show vs not show

The first-value page does not show every workflow. It shows what the buyer's tier actually delivers — surfaces from higher tiers do not appear at lower-tier first-value, because doing so creates either a paywall reveal moment (anti-fit) or a confusion moment (anti-fit).

### 3.1 Showcased on first-value, understated

| Workflow | Why understated |
|---|---|
| **Telegram bot link** | Strong amplifier, but post-first-value setup. Shown discreetly in dashboard sidebar (desktop) or settings panel (mobile per §9), not pushed during first-value |
| **Risk-gate configuration UI** | Visible (with sensible defaults pre-populated); not blocked-on; not forced before the buyer has seen the demo gate decision |
| **Journal entry-creation** | Available in dashboard; not forced into first-value |
| **API docs** | Linked from Trader+ tier description on pricing; not surfaced in first-value page itself |

### 3.2 Not showcased at first-value (deliberately deferred)

| Workflow | Why deferred |
|---|---|
| **Multi-account view** | Desk Preview and above; do not show on Free first-value (would surface paid-tier feature without context — anti-pattern per `07-packaging-and-pricing/packaging-strategy.md`) |
| **Programmable / composed risk gates** | Same — Desk Preview+; not part of Trader-tier first-value |
| **Audit-grade reporting** | P5 — does not exist yet; do not preview |
| **Backtest sandbox** | Desk Preview; do not preview at Free first-value |
| **Real-capital deployment** | Gated by §8 Capital Cap; not part of first-value at any tier currently |

### 3.3 The discipline rule

**First-value showcases what the buyer's tier actually delivers.** This rule applies at every tier, not just Free. A Desk Preview first-value should not preview Desk Full v2 audit-grade reporting; a Desk Full v2 first-value should not preview deferred capabilities. Surfaces from higher tiers (or future versions) belong on the public roadmap (`coinscope.ai/roadmap`), not in the dashboard.

---

## 4. Design constraints on each surface

How the surfaces in §2 are rendered. Six constraints apply across the page; surface-specific notes added where relevant.

### 4.1 Order of attention — footer first, signal feed second

When first-value renders, the validation-phase footer must render visibly **before** the signal feed loads. The order matters: the buyer reads "this is testnet" before they read "this is a signal." This is enforced by render order, not by polite copy ordering.

### 4.2 The first demo gate decision is deliberately a rejection

This is a stated design opinion, not a derived claim: a rejection with explicit reasoning is a stronger signal of *enforcement* than a pass is of *capability*. The first-time buyer needs to see the system refuse an action with a reason; that recognition produces the "aha" faster than seeing a successful trade arm.

A second pre-rendered demo (a *pass* example with explicit gate-result reasoning) is acceptable to ship alongside the rejection demo. Both pre-rendered, both showing the canonical full-output format.

### 4.3 No urgency, no scarcity, no theatre

- No countdown timers
- No "X spots left" copy
- No "limited founder pricing — last day!"
- No "act now" CTAs
- No "Welcome aboard! 🚀" or social-tier voice

The pricing page is single-sticker (per `07-packaging-and-pricing/pricing-strategy.md` § 6 M3 / M6 + canonical anti-overclaim in `13-support-and-trust-ops/public-claims-guardrails.md` §3.3); the first-value page inherits that calibration. **Trust is the conversion mechanism; urgency is not.**

### 4.4 Embedded education only — no tutorial overlays

Tooltips and inline explanations are good. Modal popups, tutorial overlays, "click here next" arrow guides, and forced video tutorials are all anti-pattern (per §6 AP4 / AP9 / AP10). The buyer reads carefully and understands; the buyer who skims sees the right calibration. Either path lands inside the trust band.

### 4.5 No card-on-file, no paywall popups during Free first-value

Card capture is at intent-moment (Gate 5), never at first-value (per §6 AP5 / AP6). Paywall popups during Free first-value are forbidden; tier-comparison information surfaces only as a calm "What's in Free / What unlocks at Trader" panel — single, inline, anti-pressure.

### 4.6 CA-5 / CA-7 counsel-review pending on the demo "Action:" line

The canonical Scoopy demo format includes "Action: Close a leg or wait for gate to relax" (see §2.2). Per `14-risk-compliance-and-safeguards/compliance-assumptions.md` CA-5 (tools-not-advice) and CA-7 (signals are descriptive engine outputs, not personalized recommendations), counsel review may determine this language reads as borderline-recommendation and require revision.

The first-value implementation MUST track counsel resolution. If counsel determines the "Action:" line is non-recommendation language, ship as-is. If counsel requires revision, the canonical Scoopy format updates and this surface implements the revised format. **The first-value page does not ship the unrevised format publicly until counsel has resolved CA-5/CA-7.**

---

## 5. What must be clearly understood by the end of first session

Five things the buyer must understand. Each has a corresponding surface or copy element.

| # | What must be clear | How it's surfaced |
|---|---|---|
| **1** | What CoinScopeAI **does** (gates, classifies, sizes, journals, alerts) | Top-5 + demo gate decision + journal sidebar visibility |
| **2** | What CoinScopeAI **does not do** (no signals as recommendations to act on; no autonomous execution; no custody; no performance promises) | `coinscope.ai/what-we-dont-do` link from first-value; validation-phase footer |
| **3** | What is **gated by validation phase** (real-capital deployment is gated; testnet is the current operating mode) | Validation-phase footer; PCC v2 link from pricing/about |
| **4** | What the **buyer's role** is (configure your own thresholds; bring your own framework; the system enforces what the buyer has already decided) | Risk-gate configuration UI default state with framing copy. **DECISION NEEDED** — the working slogan "your framework, our enforcement" requires brand-voice review and lock in `09-brand-messaging.md` before P1 ship. Until then, use the descriptive form: "user-defined thresholds enforced above locked floors" |
| **5** | Where to **get help** (founder named, support inbox documented, methodology page available) | Footer with support inbox link; about page; methodology link inline |

The discipline: **explanation is embedded in the surfaces, not interruptive.** The buyer who reads carefully understands; the buyer who skims sees the right calibration.

---

## 6. What should not be forced too early

Patterns that compress the trust transition by demanding action before the buyer is ready.

| # | Anti-pattern | Why it kills first-value | Guard |
|---|---|---|---|
| **AP1** | Forcing risk-gate configuration before showing the demo gate decision | The buyer doesn't yet know what they're configuring | Sensible defaults pre-populated; configuration UI visible but not blocking |
| **AP2** | Forcing journal setup before first signal seen | Journal makes sense after the buyer has decided to use the product | Journal available post-first-value; never blocking |
| **AP3** | Forcing Telegram bot link in first session | Telegram is an amplifier, not a gate | Post-first-value; persistent (not pushy) link |
| **AP4** | Forcing video tutorial completion to proceed | Treats the buyer as if they don't read | Optional video; never gates progress |
| **AP5** | Forcing card-on-file at signup or first-value | Anti-ICP filter inversion | No card before intent moment (Gate 5) |
| **AP6** | Forcing tier upgrade with paywall popups during Free first-value | Burns the trust transition | "What's in Free / What unlocks at Trader" panel — single, calm, anti-pressure |
| **AP7** | Forcing "Schedule onboarding call" CTA modal | Self-serve is the rule; assistance is by invitation | Founder kickoff offered to P1 cohort users only; not a forced modal |
| **AP8** | Forcing referral / invite-friends CTA | Anti-ICP affiliate adjacency | No referral program at P1–P2 |
| **AP9** | Forcing "rate your experience" feedback popup at first-value | Interrupts the trust demo | Feedback request post-session, by email, brand-voice reviewed |
| **AP10** | Forcing notification permission grants pre-first-value | Trust before action | Notifications request only when Telegram is being linked |

The combined rule: **a first-value page that demands actions to proceed is broken.** The buyer should be able to read the page, understand the product, and leave — and come back tomorrow at their own pace.

---

## 7. How first value connects to retention and monetization

First value is one event in a longer arc: first-value → engagement → activation → retention → conversion → expansion.

### 7.1 First-value → engagement (Free retention)

The buyer has seen the trust demo. The product earns the next session by:

- Sending a single, brand-voice-reviewed welcome email within 24 hours of first-value (not before; not multiple)
- A weekly digest opt-in CTA on the dashboard, anti-pressure
- Methodology page deep-link options surfaced contextually
- No gameification, no badges, no streak counters

### 7.2 Engagement → activation (Free)

The Free user comes back, reads the methodology, hits the gate decision view a few more times, opens the weekly digest. Activation criterion **F-1 + F-2 + F-3 + F-4 within 24 hours** is met early (per `12-onboarding-and-activation/activation-milestones.md` §2.1); F-5 (methodology viewed) is the strong-engagement signal that follows.

### 7.3 Activation → conversion

Conversion happens at an **intent moment**, not on a timer:

- The buyer attempts a journal entry → upgrade prompt for Trader appears (single, quiet, inline)
- The buyer hits the API rate limit → upgrade prompt for Desk Preview appears
- The buyer clicks "Talk to founder" on Desk Preview pricing card (P3 Layla path)

These are **discrete, contextual** triggers. They do not surface unless the buyer has signaled intent. They are not surfaced as countdown urgency; they are surfaced as natural next steps.

### 7.4 Conversion → retention (paid tier)

The first 14 days of paid tier are the trust window. The buyer can refund without arguing per `07-packaging-and-pricing/trial-and-discount-policy.md` §5. The product earns the next 14 days by hitting Trader milestones (per `12-onboarding-and-activation/activation-milestones.md` §2.2):

- T-2 (first real-time signal seen) within minutes of T-1
- T-3 (risk-gate configured) within first session if the buyer wants
- T-4 (first journal entry) within the first week
- Telegram bot connection (T-5) within first 14 days

If the trust window closes without these milestones, the user is at risk and triage applies (per `12-onboarding-and-activation/activation-milestones.md` §5).

### 7.5 Retention → expansion

Trader → Desk Preview happens on a binding constraint event (API rate limit, multi-account need, monthly PDF requirement). It is **not** a marketing-driven upsell.

Desk Preview → Desk Full v2 happens at P5 launch with a documented migration credit (per `07-packaging-and-pricing/pricing-strategy.md` §8 PD6).

The expansion arc respects the buyer's operating shape; we do not push tier upgrades that don't match their actual scale.

---

## 8. Failure-mode first-value

A buyer's first failure-state experience is also a first-value experience, just inverted. Calibrated honesty during failure compounds trust the same way calibrated honesty during success does.

### 8.1 Failure modes that affect first-value

| Failure mode | Source |
|---|---|
| Engine cold-start: exchange API connection succeeded but engine has no signal computed yet | Engine state |
| Vendor degradation (Tradefeeds STN per §12 R-010; CoinGlass partial outage; Binance rate-limit) | Vendor monitoring |
| Engine bug producing malformed signal output | Engine bug (P1 incident per §12 R-013) |
| API key wrong scopes / expired / IP-restricted | User-side configuration |
| Network failure between dashboard and engine | Infrastructure |

### 8.2 What clean degradation looks like

- **Status page banner visible at top of dashboard** if any vendor is at degraded state
- **"Signal feed initializing — typically <2 minutes after exchange-connection. Status: [link]"** placeholder during cold start, with a retry button visible
- **Signal cards that fail to render show:** "Signal data unavailable — engine status: [link]" (not blank state)
- **Demo gate decision is pre-rendered cached content** — must not depend on live engine; renders even when engine is degraded (this is a design requirement, not a coincidence)
- **API-key scope-error guidance inline:** "API key requires read-only scopes. [Documentation link]" — never generic "authentication failed"
- **Vendor-incident severity ≥ medium triggers in-product banner** per `13-support-and-trust-ops/incident-communications.md` §4

### 8.3 Anti-patterns at failure

- ~~Generic "Something went wrong" without actionable context~~
- ~~Silent failure (blank signal feed without explanation)~~
- ~~"Try again later" without status link~~
- ~~Hidden vendor outage (the buyer should not learn about it from a third party)~~
- ~~Apology-only error messages ("Sorry for the inconvenience!") without action information~~

The principle (per `13-support-and-trust-ops/incident-communications.md` §1): **silence is the worst incident response.** A buyer who sees a degraded surface with explicit, calibrated honesty about what's degraded and what's being done is less rattled than a buyer who sees a blank screen.

---

## 9. Mobile-responsive considerations

Dashboard is responsive web; mobile native app is deferred (D7 per `01-executive-summary/strategic-priorities.md`). UAE/MENA cohort skews mobile per regional norms — mobile first-value cannot be an afterthought.

### 9.1 Mobile first-value baseline

| Surface | Mobile rendering |
|---|---|
| Top-5 signal feed | Same content; vertical scroll; signal cards stacked |
| Demo gate decision | Full-width card; hover-revealed math becomes tap-to-expand |
| Methodology link | Tap-target ≥44px (iOS HIG); inline with signal cards |
| Validation-phase footer | Visible at top of viewport, not buried in mobile chrome |
| "What we don't do" link | Discreet but reachable in <2 taps |
| Telegram link | Single-tap deep-link to @ScoopyAI_bot |
| Risk-gate configuration UI | Scrollable, not blocking; collapsible sections |
| About-page link / founder name | Reachable in standard mobile footer pattern |
| AED conversion at signup | Visible without forced collapse |
| Sub-$5k "we'll be back" messaging | Readable inline, not behind a tap |

### 9.2 Anti-patterns on mobile

- ~~Tutorial overlays that block scrolling~~
- ~~Hidden validation-phase footer behind mobile chrome (e.g., collapsed in a hamburger menu)~~
- ~~Forced landscape orientation~~
- ~~Tap-targets <44px~~
- ~~Risk-gate UI that requires desktop screen real estate~~
- ~~Modal popups that prevent scrolling on small viewports~~

---

## 10. A/B test discipline on first-value copy

Most product organizations default to A/B testing onboarding copy. CoinScopeAI's anti-overclaim posture creates specific guardrails.

### 10.1 What is testable

- Secondary CTA placement (e.g., "View methodology" button position)
- Methodology-link wording variants ("How this is calculated" vs. "See the math")
- Exchange-connection instructions order
- Signal-card density (3-pair preview vs. 5-pair)
- Sub-$5k "we'll be back" copy variants — **DECISION NEEDED** brand-voice review of each variant before instrumentation
- Tier-comparison panel layout (table vs. side-by-side)

### 10.2 What is NOT testable

- Validation-phase footer presence (locked surface)
- Performance language (forbidden — per `13-support-and-trust-ops/public-claims-guardrails.md` §3.1; never test "X% wins" vs. "no claims")
- Anti-overclaim copy (forbidden — never test "production-ready" vs. "validation-phase")
- "What we don't do" link visibility (locked)
- Founder-named about page (locked)
- "Welcome aboard 🚀" vs. anything (only the calibrated honesty version is allowed)
- Card-on-file capture (forbidden anywhere)
- Founder-cohort framing ("founding-member pricing — locked through your first renewal cycle, then standard pricing applies" — locked language per `pricing-strategy.md` §9)
- Urgency theatre (forbidden — per §4.3 + canonical guardrails)

### 10.3 The guard

**Every test variant passes brand-voice review before instrumentation.** No "control vs. treatment" runs without both variants surviving brand-voice audit. A test that proposes a forbidden variant is rejected at review; a test that proposes only allowed variants ships with a documented hypothesis and a sample-size target.

### 10.4 Decision-log entry per test

Each A/B test on first-value gets a decision-log entry recording the hypothesis, the variants, the brand-voice review pass, and (after the test) the result and decision. A/B testing without decision-log discipline is anti-strategy at validation phase.

---

## 11. Accessibility and readability standards

First-value is information-dense by design. Accessibility considerations are not an afterthought.

### 11.1 Numbers

Risk-relevant values use **tabular / monospaced** numerals (per Scoopy custom instructions): drawdown %, daily loss %, leverage, position count, heat %, confidence score, exposure cap. Tabular numerals align vertically across cards and prevent the "is that 4.0x or 4.O x" misreading.

### 11.2 Regime tokens

Regime tokens carry both color (mint #00FFB8 / neutral #A3ADBD / amber #F5A623 / muted #5B6472 per Scoopy) and a **semantic label or icon**. Color is never the only carrier of meaning. A color-blind buyer or a screen-reader user must be able to read the regime label.

### 11.3 WCAG 2.1 AA contrast minimum

All text on the first-value surface meets WCAG 2.1 AA contrast ratios at minimum. Risk-relevant text (gate result, validation-phase footer, error states) meets AAA where feasible.

### 11.4 Screen-reader support

- Demo gate decision is structured data: regime label, confidence, gate result, position-sizing inputs are all readable as labeled fields
- Validation-phase footer is in the page's main landmark, not a footnote ARIA role
- Inline links ("How this is calculated", "What we don't do") have descriptive text (no "click here")
- Tooltips accessible via keyboard navigation (focus + show; not hover-only)

### 11.5 No information conveyed only by color

Gate result (pass / rejected) carries text in addition to any color treatment. Regime tokens carry semantic labels. Confidence-score color tints (if any) are paired with the numeric value.

### 11.6 Reference

- Design-system manifest (CoinScopeAI Design System; project memory)
- Brand-voice product-tier register (Scoopy custom instructions)
- WCAG 2.1 AA at minimum

---

## 12. Ship checklist

A checklist for the founder + designer to verify before P1 launch.

- [ ] First-value page renders within 5 minutes of exchange-connection (success path)
- [ ] Top-5 signals visible with regime label on every signal (Free: regime label only; paid: regime + confidence)
- [ ] At least one pre-rendered demo gate decision visible — full output regardless of tier (Free included)
- [ ] Demo gate decision shows: signal, entry, regime, confidence, gate result with explicit gate-that-fired explanation
- [ ] Validation-phase footer renders **before** signal feed loads
- [ ] "How this is calculated" inline link to methodology page on signals and gate decisions
- [ ] "What we don't do" link surfaced (discreet, not pushy)
- [ ] About page link in footer with founder named (Mohammed)
- [ ] No tutorial overlay; no forced walkthrough; no modal popups
- [ ] No countdown timers, no scarcity copy, no urgency CTAs
- [ ] No performance numbers anywhere on the surface
- [ ] No paywall popups during Free first-value
- [ ] No card-on-file capture pre-first-value
- [ ] No "Welcome aboard! 🚀" copy or social-tier voice
- [ ] Sub-$5k accounts see "we'll be back" framing, not upgrade pressure
- [ ] Telegram link visible (sidebar on desktop / settings panel on mobile), not pushed
- [ ] Risk-gate configuration UI visible with sensible defaults pre-populated, not blocking
- [ ] Brand-voice audit pass on every copy string
- [ ] Activation event instrumentation (F-3, F-4) firing correctly per `12-onboarding-and-activation/activation-milestones.md` § Free milestones (upstream: `_phase-2/_onboarding/02-activation-milestones-definition.md`)
- [ ] Failure-mode rendering tested (engine cold-start placeholder; vendor-degraded banner; scope-error guidance) per §8
- [ ] Mobile-responsive baseline verified per §9 (tap-targets ≥44px; footer visible; no forced landscape)
- [ ] Accessibility verified per §11 (tabular numerals; regime tokens with semantic labels; WCAG 2.1 AA contrast; screen-reader support)
- [ ] CA-5 / CA-7 counsel resolution applied to demo "Action:" line (per §2.2 + §4.6)
- [ ] **DECISION NEEDED — slogan "your framework, our enforcement" passes brand-voice review and locks in `09-brand-messaging.md`**, OR is replaced with the descriptive form (per §5 row 4)

Pass-through is the launch dependency; partial-pass is a P1 close gap.

---

## 13. Cross-references

- First-value experience design canonical (Phase 1): `business-plan/_phase-2/_onboarding/04-first-value-experience-design.md`
- First-time user journey: `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md`
- Activation milestones (instrumentation upstream): `business-plan/_phase-2/_onboarding/02-activation-milestones-definition.md`
- Activation milestones (Wave 2 sibling): `business-plan/12-onboarding-and-activation/activation-milestones.md`
- Friction audit: `business-plan/_phase-2/_onboarding/05-friction-audit-across-current-flow.md`
- Plan matrix: `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Pricing strategy (cardinal-test cross-document consistency): `business-plan/07-packaging-and-pricing/pricing-strategy.md`
- Trial / discount policy: `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Trust-first growth: `business-plan/08-go-to-market/trust-first-growth.md`
- Anti-overclaim canonical: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications (failure-mode templates): `business-plan/13-support-and-trust-ops/incident-communications.md`
- Onboarding strategy (this folder): `business-plan/12-onboarding-and-activation/onboarding-strategy.md`
- Compliance assumptions (CA-5 / CA-7): `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`
- Brand messaging: `business-plan/09-brand-messaging.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
