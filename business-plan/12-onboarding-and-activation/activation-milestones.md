# Activation Milestones

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_onboarding/02-activation-milestones-definition.md` (instrumentation spec, per-tier milestones, per-persona expected paths)

---

## 1. What activation should mean for CoinScopeAI

**Activation = a user has crossed the threshold where they have seen enough of the product to make an informed decision about retention or conversion.**

Three implications baked into that definition:

- Activation is **prerequisite** to conversion, not synonymous with it. A user who activates and never converts is a useful signal (suggests product-fit gap or persona mismatch). A user who converts without activating is a billing event without product engagement — it is **not** a success.
- Activation is **per-tier**, not global. The activation criteria for a Free user (saw the trust demo) are different from a Trader user (saw a real-time signal + journal entry) and from a Desk Preview user (saw multi-account aggregation + a monthly PDF). Different tiers, different proof-of-value moments.
- Activation is **observable, not inferred**. Each milestone has an instrumentation event (`signup.email_verified`, `value.first_signal_seen`, `value.first_gate_decision_seen`, etc. — see `_phase-2/_onboarding/02-activation-milestones-definition.md` for the full event spec). The cohort observation deck reports against actuals; we do not guess at activation.

The product-side significance: **activation is the strongest leading indicator we have of cohort health**. Retention and conversion are lagging; activation funnel rates are leading. P1 cohort observation orbits around this metric.

---

## 2. Key activation milestones

Inherits the locked per-tier milestone tables from `_phase-2/_onboarding/02-activation-milestones-definition.md` §2. Restated here at strategy level.

### 2.1 Free milestones (5 ordered events)

| # | Milestone | What it proves | Required for activation? |
|---|---|---|---|
| **F-1** | Account verified (email confirmed) | The user is real and committed enough to confirm an email | ✅ Required |
| **F-2** | Exchange connected | The user is a trader (filter pass) and trusts the read-only API key request (trust pass) | ✅ Required |
| **F-3** | First signal seen | The product has rendered to a logged-in user; the trust demo has begun | ✅ Required |
| **F-4** | First gate decision seen | The user has seen the differentiator: gate result + regime + confidence on a demo trade | ✅ Required |
| **F-5** | Methodology page viewed | The user has invested reading time in the engine logic — strongest trust-confidence signal | Optional; trust amplifier |

**Activation condition (Free):** F-1 + F-2 + F-3 + F-4 within 24 hours of signup.

### 2.2 Trader milestones (5 ordered events)

| # | Milestone | What it proves | Required for activation? |
|---|---|---|---|
| **T-1** | Trader subscription activated | Stripe state = active; payment cleared | ✅ Required |
| **T-2** | First real-time signal seen | The user has rendered the full-fidelity signal feed (vs. delayed top-5 on Free) | ✅ Required |
| **T-3** | Risk gate configured (custom threshold above floor) | The user is operating their own framework, not just consuming defaults | Strong activation indicator |
| **T-4** | First journal entry | The user has begun the workflow shift away from their cobbled bundle | Strong activation indicator |
| **T-5** | Telegram bot connected | The user has wired up the canonical alert path | Optional; engagement amplifier |

**Activation condition (Trader):** T-1 + T-2 + (T-3 OR T-4) within 14 days of subscription activation.

### 2.3 Desk Preview milestones (5 ordered events)

| # | Milestone | What it proves | Required for activation? |
|---|---|---|---|
| **DP-1** | Desk Preview subscription activated | Stripe state = active for DP tier | ✅ Required |
| **DP-2** | Multi-account connected (≥2 accounts) | The buyer is using the multi-account differentiator | Strong activation indicator |
| **DP-3** | First cross-account view rendered | The aggregation surface has been used | ✅ Required |
| **DP-4** | First monthly PDF report generated | The reporting promise has been fulfilled — first month-end after DP-activation | ✅ Required |
| **DP-5** | Backtest sandbox used | The buyer is exploring the API/backtest surface | Optional; engagement amplifier |

**Activation condition (Desk Preview):** DP-1 + (DP-2 OR DP-3) + DP-4 within 60 days of subscription activation.

### 2.4 Desk Full v2 milestones (5 ordered events; v2 launch P5 — Mar–May 2027)

| # | Milestone | What it proves | Required for activation? |
|---|---|---|---|
| **DF-1** | Desk Full v2 subscription activated | Stripe state = active for DF v2 tier | ✅ Required |
| **DF-2** | First audit-grade report generated | The v2 audit-grade reporting promise has been fulfilled | ✅ Required |
| **DF-3** | First partner seat added | Per-seat scaling has begun (the Desk Full v2 pricing premise) | Strong activation indicator |
| **DF-4** | Custom Telegram routing configured | Multi-channel alert routing in use | Optional |
| **DF-5** | First analyst seat added | Per-seat density upside in motion | Optional; per-seat density amplifier |

**Activation condition (Desk Full v2):** DF-1 + DF-2 + DF-3 within 90 days of subscription activation.

---

## 3. Milestone ordering

The ordering is not arbitrary; each milestone unlocks the trust required for the next.

### 3.1 Why F-1 before F-2

A user who refuses to verify their email is not a candidate for the API-key step. Email verification is a basic-trust filter; without it, exchange-connection ask is premature.

### 3.2 Why F-2 before F-3

The first-value page is account-aware (account size band, account context). Rendering it without an exchange connection produces a degraded experience that misrepresents what the product actually does. F-2 is the gate, not just a step.

### 3.3 Why F-3 before F-4

A signal alone is not differentiating; CoinGlass shows liquidations, Nansen shows wallet flows. The differentiator is the **gate decision** that combines signal + regime + risk-gate result. F-3 (signal seen) is the surface; F-4 (gate decision seen) is the differentiator. Order matters because the buyer's mental model needs the signal context to interpret the gate.

### 3.4 Why F-5 is optional

Methodology page viewing is a strong trust amplifier — it correlates with conversion uplift — but it is **not** required for activation. A Trader-bound P1 Omar may activate without ever opening the methodology page during the F-window if the trust demo (F-4) was sufficient.

### 3.5 Why T-3 OR T-4 (not both required)

Trader activation requires evidence the user is **operating** (configuring risk-gate thresholds) **or** **journaling** (logging trade entries). Either is sufficient evidence of meaningful product use. Both is better, but requiring both delays the activation flag artificially.

### 3.6 Why DP-4 (first monthly PDF) requires waiting until first month-end

Activation for Desk Preview is intentionally slower than Trader because the **reporting capability** is the headline value, and the reporting cadence is monthly. A 60-day activation window allows for at least one full month-end cycle.

### 3.7 Why DF-3 (first partner seat) is included in activation

Desk Full v2's pricing premise is per-seat scaling. A Desk Full v2 user without partner seats is effectively a high-priced Desk Preview user — they have not used the differentiator. Activation requires at least one partner seat to confirm the product fits the operating shape.

---

## 4. Indicators that a user is progressing well

| Indicator | What it suggests | When to celebrate / observe |
|---|---|---|
| **Email verified within 5 minutes of signup** | High intent; good filter pass | All signups |
| **Exchange connected within 15 minutes** | The exchange-connection trust ask was accepted cleanly | All signups |
| **First gate decision seen within 10 minutes of exchange-connect** | The trust demo landed; the buyer understood what they saw | All Free users; activation criterion |
| **Methodology page viewed within 7 days of signup** | High trust-confidence; correlates with conversion | All Free users |
| **Free retention to first weekly digest opt-in** | The buyer is in genuine evaluation mode | All Free users |
| **Risk-gate threshold customized within 30 days of Trader activation** | Operating shape is being applied; product is becoming part of their workflow | All Trader users; strong activation indicator |
| **Journal entries logged consistently in first 30 days post-Trader-activation** | Workflow shift from cobbled bundle is occurring | All Trader users; strong retention predictor |
| **Telegram bot connected within 14 days of Trader activation** | Engagement amplifier wired up | Trader users |
| **Multi-account connected within 14 days of DP-activation** | Desk Preview value is being used | DP users |
| **Cohort cross-references the product in their network** | Word-of-mouth amplification beginning (per `04-icp-and-segmentation/primary-icp.md` §7) | Quarterly observation |

These are **observation signals**, not user-facing badges or progress bars. The cohort observation deck reports them; the user does not see "you have completed 4 of 5 activation steps" or similar gameification copy.

---

## 5. Indicators that a user is stuck

| Indicator | What it suggests | Triage action |
|---|---|---|
| **Email not verified after 24 hours** | Lost or not-serious signup; do not pursue | Auto-prune from active cohort observation; archive |
| **Account verified but exchange not connected after 24 hours** | Exchange-connection friction blocked them — most common stuck state | Inline help on the next session; if cohort user, founder reach-out within 48h |
| **Exchange connected but no first signal seen** | Engine rendered nothing — likely an instrumentation or product bug | Internal incident; check logs for engine errors |
| **First signal seen but no gate decision viewed** | The trust demo was incomplete; the buyer left mid-flow | Send a one-time, brand-voice-reviewed re-engagement email with a direct link to the gate decision view |
| **Free retention dies before the first weekly digest** | The buyer evaluated, didn't see fit, and moved on | Capture exit-survey reason if possible; do not pursue |
| **Trader subscription activated but T-2 not hit within 24 hours** | Likely billing-success-but-product-failure (auth issue, dashboard rendering failure) | Internal incident; founder reach-out within 24h |
| **Trader user not configuring risk-gate or journaling within 30 days** | Operating shape mismatch; user paid but is not using the differentiator | Cohort observation flag; founder check-in if P1 cohort user |
| **DP user not connecting multi-account within 14 days** | The DP differentiator is unused; user is effectively paying for Trader | Cohort observation flag; founder check-in if P1/P2 cohort user |
| **DP user not generating monthly PDF after first month-end** | Reporting capability unused; potential downgrade risk | Cohort observation; structured feedback request |
| **Refund requested within 14 days** | First-week trust failure; capture reason | Honor refund without arguing per `07-packaging-and-pricing/trial-and-discount-policy.md` §5; capture reason |

The triage discipline: **stuck-user indicators are observed and acted on by the founder during P1; they are not surfaced as in-product nags to the user.** A user who is stuck because the product confused them gets gentle help. A user who is stuck because the product is not for them gets distance, not pressure.

---

## 6. Activation differences by ICP

Inheriting expected activation paths from `_phase-2/_onboarding/02-activation-milestones-definition.md` §3.

| Persona | Expected activation path | Expected time to activation | Conversion likelihood post-activation (base case) |
|---|---|---|---|
| **P1 Omar** (Methodist) | F-1 → F-2 → F-3 → F-4 → (Free retention 14–60 days) → T-1 → T-2 → T-4 (journal) | F-activation: <30 min · T-activation: 14d–14m | Free → Trader: ~5% over 90 days |
| **P2 Karim** (Engineer Trader) | F-1 → F-2 → F-3 → F-4 → F-5 (methodology) → (Free retention 3–14 days) → T-1 → T-2 → T-3 (risk gate config) → eventual DP trigger when API rate-limit binds | F-activation: <60 min · T-activation: 3–14d · DP-activation: 90–180d | Free → Trader: ~10% · Trader → DP: ~15% |
| **P3 Layla** (Solo PM) | F-1 → F-2 → F-3 → F-4 → (Free retention 1–3 days) → DP-1 (skip Trader) → DP-2 → DP-3 → DP-4 (first PDF after first month-end) | F-activation: <30 min · DP-activation: <60d | Free → DP: ~15–25% (higher pain, higher WTP) · DP → DF v2 at v2 launch: 70% base case |
| **Sub-$5k disciplined** | F-1 → F-2 → F-3 → F-4 → (Free retention indefinite) → ($5k threshold trigger) → T-1 | F-activation: <30 min · T-activation: variable, dependent on account growth | Conversion at $5k threshold: **ASSUMPTION** pending cohort data |

### 6.1 What this means strategically

- **P1 Omar's activation is fast (Free side) but slow (paid side).** Don't mistake long Free retention for stuck-ness; that's the buying pattern.
- **P2 Karim activates fastest because they convert on credibility.** Methodology-page view (F-5) is more strongly correlated with paid conversion for Karim than for Omar.
- **P3 Layla activates faster on Free→DP than P1 does on Free→Trader.** Higher pain, higher WTP. But DP activation (DP-1 → DP-4) takes 60 days because of the monthly PDF cadence. That is structural, not a stuck signal.
- **Sub-$5k disciplined activation is intentionally indefinite.** The "we'll be back" mechanism does not push these users toward T-1; they move when their account grows.

### 6.2 What this means for cohort observation

- The 40-user P1 cohort target mix (~30 P1 / ~8 P3 / ~2 P2) implies mixed activation timelines. Cohort observation deck reports per-persona, not just aggregate.
- A P3 candidate stuck on Free past 7 days deserves more triage attention than a P1 candidate at the same point.
- Sub-$5k users are observed as a separate stream; their conversion-trigger metric (account size crosses $5k) is unique.

---

## 7. What activation should not be confused with

Eight common conflations that distort the metric.

| Conflated with | Why it's wrong | The discipline |
|---|---|---|
| **Conversion** | Activation is prerequisite to conversion; conversion can happen without activation (bad) or activation without conversion (informative) | Track separately; never collapse into one funnel metric |
| **Engagement** | A user can be highly engaged on the methodology page (high session time, multiple visits) without activating | Activation requires specific milestones; engagement is observed but not gated to activation |
| **Time spent in product** | Long session time with no F-4 hit means the user is searching for something they didn't find | Time-in-product is an input signal; it does not substitute for the milestone events |
| **Login count** | High login count without exchange-connection or first-value is a frustrated user, not an activated one | Login count is a stuck-indicator candidate, not an activation indicator |
| **Tutorial completion** | We don't have forced tutorials; if we did, completion would not equal activation | Activation is about the buyer seeing real product behavior, not artifacts of guided overlays |
| **Pricing-page visits** | Lots of pricing-page traffic from one user suggests they are evaluating; it is not yet activation | Pricing-page bounce is a top-of-funnel metric, not an activation signal |
| **Email-newsletter open rate** | A Free user who opens every weekly digest is engaged but may never have hit F-3 | Newsletter engagement is a Free-retention signal; activation requires the in-product milestones |
| **Word-of-mouth referrals** | A user who recommends the product without using it is not activated; their recommendation is brand affinity, which is positive but separate | Track referral signals separately; they correlate with activation but are not the same construct |

The cardinal rule: **activation is observable, defined, and per-tier**. Anything else is a related metric, not activation.

---

## 8. Activation as the leading indicator for cohort health

The reason all of this matters: **activation rate is the cleanest leading indicator of P1 cohort signal**.

| Metric | Lag | What it tells us |
|---|---|---|
| **Cohort retention at 30 days** | 30 days | Whether users stay |
| **Cohort retention at 90 days** | 90 days | Whether users meaningfully use the product |
| **Free → Trader conversion at 60 days** | 60 days | Whether the upgrade path works |
| **Activation rate (F + T) at 14 days** | 14 days | Whether the product reaches first-value reliably |

A 14-day activation signal landing 30+ days before retention data lets the founder steer the cohort. If F-activation is dropping below 70% during P1 weeks 1–3, ops/product can intervene **before** the 30-day retention metric confirms the problem.

This is why activation-milestone instrumentation (per `_phase-2/_onboarding/02-activation-milestones-definition.md`) is a P1-launch-blocking dependency.

---

## 9. Validation phase note

Activation thresholds (e.g., F-activation = F-1 + F-2 + F-3 + F-4 within 24 hours; Trader activation = T-1 + T-2 + (T-3 OR T-4) within 14 days) are **working assumptions, not locked truths**. P1 cohort data validates or revises them.

If P1 cohort data shows:

- F-activation consistently lands in <12 hours → tighten threshold to 12 hours (post-validation)
- T-activation requires both T-3 AND T-4 to predict retention → revise the OR to AND
- DP-activation 60-day window is too short for the monthly-PDF cadence in practice → extend to 75 days

These are post-validation revisions. **DECISION NEEDED — revisit thresholds at P1 close (Jul 2026).**

---

## 10. Cross-references

- Activation milestones canonical (instrumentation): `business-plan/_phase-2/_onboarding/02-activation-milestones-definition.md`
- First-time user journey: `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md`
- KPI / OKR framework: `business-plan/13-kpi-okr.md`
- Onboarding strategy (this folder): `business-plan/12-onboarding-and-activation/onboarding-strategy.md`
- First-value design (this folder): `business-plan/12-onboarding-and-activation/first-value-design.md`
- Plan matrix: `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
