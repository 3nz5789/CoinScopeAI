# 03 — ONBOARDING

**Workstream:** ONBOARDING
**Phase:** 2 — Monetization
**Status:** Canonical task list absorbed verbatim 2026-05-04. Source of truth for the Phase 2 ONBOARDING workstream.
**Canonical authorities:** v1 framework `06-pricing-monetization.md` §6.5 Free Scope B; `10-operations-support.md`; `12-risk-compliance-trust.md`; `_data/operations/Production_Candidate_Criteria_v2.md` §8 Capital Cap; Scoopy custom instructions (validation disclaimer, regime tokens, Telegram bot); memory `project_jurisdictional` (US-blocked, UAE sole prop); PACKAGING `_packaging/02-free-vs-paid-boundary.md`; PRICING `_pricing/04-trial-and-intro-offer-options.md`.

---

## 1. Purpose

Lock the **first 30 minutes** through the **first 30 days** of a CoinScopeAI user's relationship with the product: how they sign up, prove out an exchange account, see their first signal, see their first gate decision, and either convert or stay productive on Free. ONBOARDING is the operational form of §6.5 Free Scope B + §3.5 "we'll be back" + the no-free-trial posture (per Pr2-3); it is also where PCC v2 §8 ("Testnet only. No real capital.") becomes real to the user, not just a footer disclaimer.

## 2. Why this matters specifically for CoinScopeAI

- **The first signal a user sees is the trust load surface.** If the first signal arrives without regime label + confidence + gate result, we lose the methodical, evidence-led BRAND voice in the user's first impression. If it arrives over-promising live-capital readiness, we credibly mislead them about what the product does today.
- **Account verification at signup is load-bearing for §6.5 Scope B.** Free includes an exchange-account-verified entry tier; verification is what unlocks the demo-trade gate behavior view + the sub-$5k "we'll be back" branch. Skipping or weakening verification breaks both.
- **Sub-$5k branch is the §3.5 anti-persona stance made operational.** Wrong here = either second-class treatment of future-ICP (anti-pattern) or premature funnel collapse (no path to $5k → Trader conversion).
- **Exchange connection is the only execution-adjacent step in onboarding.** Binance USDT-M only at P1; Bybit deferred to P2 (Aug-Sep 2026) per phase map; venue selection at signup must not promise venues we don't ship.
- **Real-capital boundary lives here.** PCC v2 §8 governs when the system permits any real-capital path. Onboarding copy must trace every "live trading" reference to the gate, not the marketing surface.
- **Telegram is the primary alert channel** (@ScoopyAI_bot per Scoopy custom instructions). Telegram-connection step is paid (Trader+ per `_packaging/02`); onboarding Free users to a paid feature path requires the gating to be transparent.
- **Founder-cohort window comms surface in onboarding.** If a user signs up during the 60-day window, they must see the founder-cohort offer at the conversion moment — not buried in pricing-page copy they've already left.

## 3. Required subsections

1. **First-time user journey** — end-to-end map from landing page → signup → verification → first signal → first gate decision → first billing event (or staying on Free).
2. **Activation milestones definition** — operational definitions of "activated" per persona + per tier; instrumented events.
3. **Signup-to-exchange-connection flow** — spec for the most critical conversion sequence; sub-$5k branch + region check + API key flow.
4. **First value experience design** — the "aha" moment per persona / per tier; concrete first-30-minutes script.
5. **Friction audit across current flow** — QA pass on documented surfaces; surfaces drift from anti-overclaim discipline + Pr2-3 no-trial posture.
6. **New user education sequence** (NEXT) — methodology + risk-gate + regime-label education in the right cadence and channel.
7. **Onboarding copy pack** (NEXT) — every onboarding string tied to the BRAND voice and anti-overclaim audit.
8. **Activation KPI dashboard** (NEXT METRICS) — the KPIs that confirm onboarding works.
9. **Assisted onboarding for high-value users** (NEXT) — light-touch concierge for prospective Desk Preview / Desk Full v2 buyers.
10. **Billing and trial entry experience review** (NEXT QA) — verifies no trial mechanic exists in production per Pr2-3.

## 4. Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| First-time user journey map | MD; per-persona swim-lane | Strategy CoS + Design |
| Activation milestones definition | MD; per-persona milestone table + instrumentation spec | Strategy CoS + Eng |
| Signup-to-exchange-connection flow | MD; step-by-step spec + branching rules | Design + Eng + Founder |
| First value experience design | MD; per-persona 30-min script | Strategy CoS + Design |
| Friction audit | MD; surface-by-surface audit + remediation backlog | Strategy CoS + Design |
| New user education sequence | MD; in-app + email + Telegram cadence spec | Strategy CoS + Design |
| Onboarding copy pack | MD; every string tagged tier + brand-voice register | Founder + Strategy CoS |
| Activation KPI dashboard | MD KPI spec → Cowork artifact (Phase 2/3 boundary) | FinOps + Strategy CoS |
| Assisted onboarding playbook | MD; high-value triage rules + concierge SOP | Founder |
| Billing/trial entry review | MD audit; failure-mode list | FinOps + Eng |

## 5. Assumptions to validate

1. **ASSUMPTION** — Account verification at signup (exchange API key, read-only) is acceptable signup friction for the §3.5 personas. Cohort feedback validates.
2. **ASSUMPTION** — First-signal-seen + first-gate-decision-seen are the load-bearing activation milestones for Free. Cohort engagement metrics validate.
3. **ASSUMPTION** — Telegram bot connection is the Trader-tier "aha" moment. Validate via Trader cohort behavior in first 7 days.
4. **ASSUMPTION** — Sub-$5k Free users behave differently from $5k+ Free users in conversion mechanics. KPI separation per `_packaging/02` confirms.
5. **ASSUMPTION** — Single-exchange (Binance USDT-M) at P1 is sufficient for onboarding any P1/P2 persona; multi-exchange is DP+ feature, not an onboarding blocker.
6. **ASSUMPTION** — Founder-cohort window comms in onboarding lift cohort uptake by ≥10pp vs pricing-page-only surfacing.

## 6. Decisions required

| ID | Decision | Options | Owner | Deadline | Downstream impact |
|---|---|---|---|---|---|
| **On-1** | Verification depth at signup | (a) Email + read-only Binance API key (recommended; locks §6.5 Scope B). (b) Email only; exchange-connect at first signal interaction. (c) Email + KYC-style identity verify. | Founder + Eng | Before signup-flow ships | §6.5 Scope B integrity, drop-off rate |
| **On-2** | First-value definition for Free | (a) Top-5 signals + regime label visible within 5 min (recommended). (b) Demo-trade gate decision shown within 5 min. (c) Both — sequential. | Founder + Design | Before first-value spec ships | Activation rate, Free → Trader conversion |
| **On-3** | Telegram connection moment | (a) Optional during signup; nudged after first signal (recommended for Trader). (b) Required at signup for Trader. (c) Deferred to first dashboard session. | Founder + Design | Before Trader signup-flow ships | Trader retention, alert engagement |
| **On-4** | Sub-$5k branch UX | (a) Same Free UI + persistent "we'll be back" copy (recommended per §3.5). (b) Modified UI with explicit waitlist. (c) Same as $5k+ Free, no special copy. | Founder | Before signup-flow ships | §3.5 anti-persona stance, conversion at $5k threshold |
| **On-5** | Region-block UX | (a) Pre-signup region check with copy (recommended). (b) Block at exchange-connect step. (c) Allow signup, block at first signal. | Founder + Eng | Before signup-flow ships | Wasted onboarding, trust-load |
| **On-6** | Founder-cohort surface in onboarding | (a) Visible during signup + at conversion moment (recommended). (b) Visible only at conversion moment. (c) Visible only on pricing page (not in onboarding). | Founder | Before P1 Narrow Ship public launch | Founder-cohort uptake (Pr2Q-9) |
| **On-7** | Assisted onboarding trigger | (a) Self-serve only at v1; assisted is NEXT (recommended). (b) All DP/DF signups get founder concierge. (c) Self-serve with optional founder-call CTA. | Founder | Before DP/DF signups go live | Support load at DP/DF entry |

## 7. Failure modes to avoid

- **Real-capital language in onboarding copy.** Per PCC v2 §8 — testnet only at validation phase. Onboarding cannot say "trade live," "execute orders," "go live with real capital" anywhere. Every reference to live trading traces to the gate, not the marketing surface.
- **Account verification skipped.** Breaks §6.5 Scope B (account-verified Free) and removes the sub-$5k branch instrumentation. **On-1 default is required at signup.**
- **Trial-creep.** "Try Trader for 7 days" surfaces in onboarding without explicit Pr2-3 reopen → Pr2-3 violation. `[QA] ONBOARDING — Billing and Trial Entry Experience Review` (NEXT) catches this.
- **Sub-$5k pressure copy.** "Upgrade to Trader to unlock" copy on a sub-$5k Free user violates §3.5 + `_packaging/02-free-vs-paid-boundary.md` §3. Sub-$5k gets persistent "we'll be back" framing, never paywall pressure.
- **Region-block discovered late.** US user onboarded to exchange-connect step before being told they can't use the product wastes signup time and trust. **On-5 default is pre-signup check.**
- **First signal arrives without regime + confidence + gate result.** Drops the methodical BRAND voice on the user's first impression. Every signal — especially first — surfaces regime label, confidence (T+), and gate result.
- **Telegram connect required at Trader signup.** Conflates billing with channel preference. Trader users may want web-only initially; nudge after first signal, don't block at signup.
- **Onboarding promises features that are v2 / v3.** Audit-grade reporting, tax-ready export, Bybit, multi-channel Telegram routing — none of these can appear in v1 onboarding without "v2" or "v3" qualifier.
- **Founder-cohort comms drift to "lifetime."** §6.10 Flag 1. Onboarding inherits the canonical phrasing from `_pricing/03-monthly-vs-annual-offer-structure.md` §6.
- **Dashboard / Telegram drift in tone.** Per Scoopy custom instructions — product tier is technical, terse, declarative. Onboarding copy that drifts into social-tier language ("Let's go!" "Nice trade!") violates the register.
- **First gate decision not shown.** Even if a user signs up and never trades, the demo-trade gate decision view is the §6.5 trust demo. Onboarding must surface it within first 5 minutes.

## 8. Tasks (canonical list — verbatim)

### NOW

**`[DOC] ONBOARDING — First-Time User Journey`**
- **Objective:** Map the end-to-end first-time user journey from landing page → signup → verification → first signal → first gate decision → first billing event (or staying on Free). Per-persona swim-lanes for Omar / Karim / Layla.
- **Why:** Without an explicit map, every other onboarding deliverable optimizes a step in isolation. The journey map is the source of truth for sequence and dependency.
- **Dependency:** §6.5 Free Scope B; PACKAGING `02-free-vs-paid-boundary.md`; PRICING `04-trial-and-intro-offer-options.md`; ICP definitions.
- **Output:** Journey map MD; per-persona swim-lane.

**`[DOC] ONBOARDING — Activation Milestones Definition`**
- **Objective:** Define "activated" operationally per persona + per tier. Instrumentation spec for each milestone event.
- **Why:** Activation rate is the primary onboarding KPI. Without explicit milestone definition, "activation" drifts in dashboard language and §13 KPIs lose meaning.
- **Dependency:** First-Time User Journey; engine API endpoints; current event-instrumentation surface.
- **Output:** Milestones MD with per-persona table + instrumentation spec.

**`[DOC] ONBOARDING — Signup-to-Exchange-Connection Flow`**
- **Objective:** Step-by-step spec for the most critical conversion sequence. Branching rules: region check, sub-$5k branch, API key entry, testnet/mainnet toggle.
- **Why:** Signup-to-exchange-connection is where the highest drop-off lives in fintech / crypto onboarding (INFERENCE — typical industry pattern). Spec discipline here is high-leverage.
- **Dependency:** §6.5 Scope B; memory `project_jurisdictional` (US-blocked); PCC v2 §8 (testnet-first).
- **Output:** Flow spec MD with step-by-step + branching rules. Feeds **On-1**, **On-4**, **On-5**.

**`[DOC] ONBOARDING — First Value Experience Design`**
- **Objective:** Design the first-30-minutes experience per persona. Concrete script: what they see, what they do, what they understand.
- **Why:** First-value moment determines Free → Trader conversion intent. Without explicit design, the first signal arrives in a context the user doesn't understand and the trust demo fails.
- **Dependency:** Activation Milestones; engine API endpoints (/scan, /risk-gate, /regime/{symbol}); regime tokens (per Scoopy custom instructions).
- **Output:** First-value design MD per persona. Feeds **On-2**.

**`[QA] ONBOARDING — Friction Audit Across Current Flow`**
- **Objective:** Audit the documented current flow against this workstream's principles. Surface drift from anti-overclaim, Pr2-3 no-trial, §6.5 Scope B, PCC v2 §8.
- **Why:** v1 framework + Phase 1 outputs assume a current flow that may not exist or may drift; audit before redesign so remediation is targeted.
- **Dependency:** Current product surface walkthrough (REQUIRED INPUT — Eng confirm); §6.5; Pr2-3; `_packaging/05-packaging-friction-review.md`.
- **Output:** Audit report MD with surface-by-surface findings + remediation backlog.

### NEXT

**`[DOC] ONBOARDING — New User Education Sequence`**
- **Objective:** Design the methodology + risk-gate + regime-label education cadence across in-app, email, and Telegram. Spans first 30 days post-signup.
- **Why:** Methodology disclosure is §5.3.1 (public) and a load-bearing trust signal. Education cadence is how it lands without overwhelming the new user.
- **Dependency:** First Value Experience Design; engine methodology docs; BRAND voice + tone guidelines.
- **Output:** Education sequence MD with cadence spec per channel.

**`[DOC] ONBOARDING — Onboarding Copy Pack`**
- **Objective:** Every onboarding string (signup, verification, first-signal, first-gate, conversion prompts, sub-$5k copy) tagged with tier + brand-voice register + anti-overclaim audit row.
- **Why:** Copy drift is the primary leak of brand voice and anti-overclaim discipline. Centralized copy pack with audit columns is the maintainable form.
- **Dependency:** First Value Experience Design; New User Education Sequence; Phase 1 BRAND patternbook + voice/tone guidelines.
- **Output:** Copy pack MD; every string in a single audit-ready table.

**`[METRICS] ONBOARDING — Activation KPI Dashboard`**
- **Objective:** Specify the dashboard for activation KPIs (signup, verification, first-signal, first-gate, first-billing) per persona + per tier. Build as Cowork artifact per memory `reference_automation`.
- **Why:** Real-time visibility into activation funnel is required for §13 KPI tracking and for catching cohort drift.
- **Dependency:** Activation Milestones Definition; instrumented events; existing connector-health artifact pattern.
- **Output:** KPI dashboard spec MD; Cowork artifact draft.

**`[DOC] ONBOARDING — Assisted Onboarding for High-Value Users`**
- **Objective:** Light-touch concierge for prospective Desk Preview / Desk Full v2 buyers. Triage rules: who qualifies, what's offered, who delivers, time-cap per session.
- **Why:** P3 buyers expect higher-touch onboarding. Without explicit playbook, founder time leaks unbounded.
- **Dependency:** ICP definitions; PACKAGING `Fund/Desk Plan Concept` (NEXT); SUPPORT (forthcoming).
- **Output:** Assisted onboarding playbook MD. Feeds **On-7**.

**`[QA] ONBOARDING — Billing and Trial Entry Experience Review`**
- **Objective:** Verify no trial mechanic exists in production per Pr2-3. Audit Stripe configuration + product flow + onboarding copy for any trial reference.
- **Why:** Trial-creep is a top failure mode. Periodic audit catches drift before launch.
- **Dependency:** Pr2-3 lock; PRICING `[QA] Stripe Plan Mapping Review`; current product surface.
- **Output:** Audit report MD; remediation backlog if any.

### LATER

**`[DOC] ONBOARDING — Team/Fund Onboarding Playbook`**
- **Objective:** Sketch the onboarding playbook for Desk Full v2 + per-seat customers (PM + partners + analysts). Phase 5 input.
- **Why:** Phase 5 readiness; concept-only at Phase 2.
- **Dependency:** PACKAGING `Fund/Desk Plan Concept` (NEXT); Layla Phase-5 Pre-read.
- **Output:** Concept MD; *no commitments*.

**`[DOC] ONBOARDING — Multichannel Onboarding Automation Concept`**
- **Objective:** Concept for cross-channel onboarding automation (in-app + email + Telegram + possibly SMS). Phase 3+ input.
- **Why:** Bounds Phase 3 GTM channel-mix discussion without committing to a specific automation stack.
- **Dependency:** Phase 3 channel mix; New User Education Sequence (NEXT).
- **Output:** Concept MD; *no commitments*.
