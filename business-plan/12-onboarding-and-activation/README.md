# 12 — Onboarding and Activation

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_phase-2/_onboarding/` (six-gate journey, per-persona swim-lanes, activation milestones, friction audit) — this folder operationalizes that work, it does not supersede it.

---

## 1. Folder purpose

This folder defines **how a new CoinScopeAI user moves from first signup to first meaningful value** in a way that is trustworthy, low-friction, and aligned with the product's current maturity.

It answers four operator questions:

1. **What's the onboarding philosophy and flow?** — `onboarding-strategy.md`
2. **What does "activated" mean and how do we measure it?** — `activation-milestones.md`
3. **What does "first value" actually look like, and how do we deliver it without overpromising?** — `first-value-design.md`
4. **How do all of these line up against the personas and the validation-phase posture?** — answered across all three files

It is **operator-grade**, not UX-spec-grade. The detailed gate-by-gate UX (signup form fields, exchange-connection screen layout, Telegram bot link flow) lives in `_phase-2/_onboarding/`. This folder gives a strategy-tier owner what they need to make decisions, set priorities, and reject anti-pattern asks.

---

## 2. File list

| File | What it contains |
|---|---|
| `README.md` | This file — folder map, dependencies, reading order, open questions |
| `onboarding-strategy.md` | Philosophy, flow, sell-to-first, balancing speed/trust/education, exchange-connection placement, self-serve vs. assisted, risks, current-app clarity gaps |
| `activation-milestones.md` | Activation definition, per-tier milestones, ordering, progression indicators, stuck indicators, ICP differences, what activation is not |
| `first-value-design.md` | First-value definition, early-proof patterns, best workflows to showcase, trust-building interactions, what to explain clearly, what not to force, retention/monetization linkage |

---

## 3. Why this folder matters

Onboarding is **the most important brand-voice surface in the product**. By the time a buyer reaches the dashboard, they have read the pricing page, the methodology docs, and at least one Substack post. Onboarding is where the product either confirms or contradicts the brand promise.

For a trust-sensitive trading product, three failure modes destroy this transition:

- **Friction failure** — exchange connection is too painful; user abandons before seeing value.
- **Trust failure** — the product over-promises in onboarding copy; the buyer notices the contradiction and churns or stays cynical.
- **Value-blindness failure** — the user reaches the dashboard but cannot tell what they're supposed to see; they bounce without understanding what just happened.

Each is independently fatal. Each is also **structurally avoidable** if onboarding is treated as a deliberate sequence of trust-building gates rather than a UX checklist. This folder treats it that way.

---

## 4. Dependencies on prior folders

| Source | What we inherit |
|---|---|
| `01-executive-summary/business-model-summary.md` | Track B tier matrix; custody-free posture; testnet-first |
| `02-company-overview/strategic-constraints.md` | US blocked at signup; UAE/MENA + global EN; founder-led ops |
| `03-market-thesis/` | Buyer behavior — slow, reading-heavy, skeptical-by-default |
| `04-icp-and-segmentation/primary-icp.md` | P1 Omar conversion path (slow, methodology-driven) |
| `04-icp-and-segmentation/secondary-icps.md` | P3 Layla pattern (faster conversion, higher WTP); sub-$5k "we'll be back" handling |
| `05-positioning/positioning-statement.md` | Locked positioning; "trader operating system" frame |
| `05-positioning/messaging-hierarchy.md` | Tier-by-tier messaging; onboarding copy must match |
| `06-product-strategy/core-product-pillars.md` | What the product enforces; configurability of gates is non-negotiable |
| `06-product-strategy/feature-prioritization.md` | What ships in MVP / Beta / Scale |
| `07-packaging-and-pricing/plan-matrix.md` | Free is account-verified evaluation; Trader is the default offer; tier upgrade mechanics |
| `07-packaging-and-pricing/trial-and-discount-policy.md` | Free-as-evergreen + 14-day money-back; sub-$5k "we'll be back" routing |
| `08-go-to-market/launch-plan.md` § 4.4 | Onboarding readiness is a P1 launch dependency |
| `08-go-to-market/trust-first-growth.md` | Anti-overclaim rules apply to onboarding copy too |
| `business-plan/_phase-2/_onboarding/` | Six-gate journey, per-persona swim-lanes, activation milestones, friction audit, signup-to-exchange flow |

This folder is a Wave 2 **operator restatement** of `_phase-2/_onboarding/` plus inheritance from Wave 1 ICP, positioning, packaging, and GTM commitments. Where the working notes give the gate-by-gate detail, this folder gives the strategic shape.

---

## 5. Recommended reading order

For a founder reviewing onboarding readiness pre-P1:

1. `README.md` (this file) — orientation
2. `onboarding-strategy.md` — philosophy, flow, what self-serve vs. assisted
3. `first-value-design.md` — what the buyer should see in the first 15 minutes
4. `activation-milestones.md` — what's measured to know it worked
5. `_phase-2/_onboarding/01-first-time-user-journey.md` — gate-by-gate detail when implementing

For a designer / engineer building the signup-to-first-value flow:

1. `_phase-2/_onboarding/03-signup-to-exchange-connection-flow.md` (Wave 1 detail)
2. `first-value-design.md` (this folder) § 2–4
3. `activation-milestones.md` (this folder) § instrumentation references
4. `08-go-to-market/trust-first-growth.md` § 2 (allowed/forbidden claims) before any copy ships

For a support / cohort-onboarding owner during P1:

1. `onboarding-strategy.md` § self-serve vs. assisted
2. `activation-milestones.md` § stuck indicators
3. `_phase-2/_onboarding/05-friction-audit-across-current-flow.md` (Wave 1 friction inventory)

---

## 6. Open questions

Carried forward from `_phase-2/_onboarding/` plus introduced by Wave 2.

1. **DECISION NEEDED — Assisted-onboarding eligibility.** Which P1 cohort users get a founder-led kickoff call vs. self-serve? Recommendation in `onboarding-strategy.md` §5: all P1 cohort users get an optional founder kickoff in the first 7 days; mandatory only for P3 candidates.
2. **DECISION NEEDED — Sub-$5k threshold-watcher.** "Notify me when account crosses $5k" mechanism — opt-in checkbox at signup or proactive offer at first-value page? Pre-P1 lock.
3. **DECISION NEEDED — Real-time vs. delayed signal on Free.** Locked v1 says delayed (top-5 daily refresh). Confirm latency target.
4. **DECISION NEEDED — Demo-mode for Desk Preview at P2.** Whether to ship a 14-day Desk-Preview demo experience for P3 candidates evaluating multi-account view. Inherited from `07-packaging-and-pricing/trial-and-discount-policy.md` §10.
5. **REQUIRED INPUT — Exchange-connection failure-mode coverage.** Documented failure modes for Binance API key entry (wrong permissions, expired key, IP-restricted key) — needs SOP in `13-support-and-trust-ops/`.
6. **REQUIRED INPUT — Brand-voice audit on every onboarding copy surface.** Must clear before P1 launch.
7. **ASSUMPTION — Activation criteria thresholds (e.g., F-activation = F-1 + F-2 + F-3 + F-4 within 24h).** Validate against P1 cohort data; revisit at P1 close.
8. **ASSUMPTION — Telegram bot link is a strong activation amplifier.** Currently optional; cohort data may suggest making it a primary or secondary activation milestone.
9. **OPEN — In-product education depth.** How much methodology context to embed inline vs. link-out to `coinscope.ai/methodology`. Trade-off: clarity vs. interface clutter.
10. **OPEN — Onboarding for re-activated accounts.** §6.7 allows reactivation within 90 days at prior tier and pricing. The flow for a returning user is different from a first-time user; needs explicit design.

---

## 7. Cross-references

- Phase 2 onboarding canonical: `business-plan/_phase-2/_onboarding/`
- First-time user journey: `business-plan/_phase-2/_onboarding/01-first-time-user-journey.md`
- Activation milestones (instrumentation): `business-plan/_phase-2/_onboarding/02-activation-milestones-definition.md`
- Signup-to-exchange flow: `business-plan/_phase-2/_onboarding/03-signup-to-exchange-connection-flow.md`
- First-value experience design: `business-plan/_phase-2/_onboarding/04-first-value-experience-design.md`
- Friction audit: `business-plan/_phase-2/_onboarding/05-friction-audit-across-current-flow.md`
- Plan matrix: `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Trial / discount policy: `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Trust-first growth: `business-plan/08-go-to-market/trust-first-growth.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
