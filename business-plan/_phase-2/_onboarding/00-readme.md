# ONBOARDING — Workstream Index

**Phase:** 2 — Monetization
**Status:** All five NOW deliverables drafted at v0.1. Workstream-NOW complete pending decisions On-1 through On-7, Eng walk-through for Friction Audit REQUIRED INPUT items, and instrumentation gap closure.
**Closed:** 2026-05-04

---

## Files

| # | File | Type | Status | Feeds decision |
|---|---|---|---|---|
| 0 | `00-readme.md` | Index | DONE | — |
| 1 | `01-first-time-user-journey.md` | DOC NOW | DRAFT v0.1 | (foundational; consumed by all) |
| 2 | `02-activation-milestones-definition.md` | DOC NOW | DRAFT v0.1 | (feeds §13 KPI framework + activation funnel) |
| 3 | `03-signup-to-exchange-connection-flow.md` | DOC NOW | DRAFT v0.1 | **On-1**, **On-4**, **On-5** |
| 4 | `04-first-value-experience-design.md` | DOC NOW | DRAFT v0.1 | **On-2** |
| 5 | `05-friction-audit-across-current-flow.md` | QA NOW | DRAFT v0.1 | (audit; remediation backlog feeds Eng) |

---

## NEXT (queued, not started)

- `[DOC] ONBOARDING — New User Education Sequence`
- `[DOC] ONBOARDING — Onboarding Copy Pack`
- `[METRICS] ONBOARDING — Activation KPI Dashboard` · Cowork artifact target
- `[DOC] ONBOARDING — Assisted Onboarding for High-Value Users` → **On-7**
- `[QA] ONBOARDING — Billing and Trial Entry Experience Review` → cross-validates Pr2-3 lock

## LATER (queued, not started)

- `[DOC] ONBOARDING — Team/Fund Onboarding Playbook` · Phase 5 input, concept-only
- `[DOC] ONBOARDING — Multichannel Onboarding Automation Concept` · Phase 3+ input, concept-only

---

## Decisions surfaced (consolidated)

| ID | Decision | Recommendation | Locks at |
|---|---|---|---|
| **On-1** | Verification depth at signup | **Email + read-only Binance API key required at signup** | Before signup-flow ships |
| **On-2** | First-value definition for Free | **Both top-5 signals + regime label AND demo-trade gate decision shown sequentially within 5 min** | Before first-value spec ships |
| **On-3** | Telegram connection moment | **Optional during signup; nudged after first signal** | Before Trader signup-flow ships |
| **On-4** | Sub-$5k branch UX | **Same Free UI + persistent "we'll be back" copy** | Before signup-flow ships |
| **On-5** | Region-block UX | **Pre-signup region check with copy** | Before signup-flow ships |
| **On-6** | Founder-cohort surface in onboarding | **Visible during signup + at conversion moment** | Before P1 Narrow Ship public launch |
| **On-7** | Assisted onboarding trigger | **Self-serve only at v1; assisted is NEXT** | Before DP/DF signups go live |

---

## Open questions surfaced (consolidated)

1. **OnQ-1** — Does verification at signup depress signup-completion rate by >25% vs deferred-verify? (cohort A/B test in P0/P1)
2. **OnQ-2** — Is mainnet API-key entry at signup acceptable for sub-$5k disciplined users, or does it create disproportionate drop-off? (cohort feedback)
3. **OnQ-3** — Does the demo-trade gate decision view land within 5 min consistently, or do race conditions push it past target? (Eng confirm + load test)
4. **OnQ-4** — Does the founder-cohort window comm at signup lift uptake by ≥10pp vs pricing-page-only surfacing? (cohort A/B in P1)
5. **OnQ-5** — At what time-to-$5k-threshold does sub-$5k → Trader conversion stabilize? (cohort longitudinal)
6. **OnQ-6** — Telegram-nudge after first-signal — what timing maximizes Trader retention without feeling pushy? (cohort A/B)
7. **OnQ-7** — Persona-overlay engagement: do users complete the 3-step tour, or dismiss after step 1? (cohort behavioral)
8. **OnQ-8** — Does the pre-signup region check produce false-positives (legitimate non-US users blocked)? (support-ticket sampling)

---

## REQUIRED INPUT items (consolidated)

Pending Eng walk-through of live production flow + design + Stripe configuration. Drafts proceed; lock + remediation backlog wait.

| Item | Source | Affects |
|---|---|---|
| Live walk-through of current signup → first-value flow | Eng + Founder + Strategy CoS | All `05-friction-audit` REQUIRED INPUT rows |
| Read-only API key enforcement at engine-side | Eng | `03-signup-to-exchange-connection-flow.md` Step 8 + audit row 3.5 |
| Static IP allowlist for outbound API calls | Eng / DevOps | `03` Step 7 + audit row 3.7 |
| Password baseline policy | Eng / Security | `03` Step 2 + audit row 2.5 |
| Account-balance read at validation step | Eng / engine | `03` Step 8 + audit row 3.6 |
| Confidence-score gating: Free does NOT show confidence | Eng + design | Audit row 4.4 (gating leak risk) |
| `value.first_signal_seen` event at session-render level | Eng / product analytics | `02` §5 + audit rows I.3 + I.4 |
| `value.first_gate_decision_seen` event at session-render level | Eng / product analytics | `02` §5 + audit rows I.3 + I.4 |
| Cohort assignment logic instrumentation | Eng / product analytics | `02` §5 + audit row I.9 |
| Stripe webhook → entitlement YAML pipeline (<30s end-to-end) | Eng / Stripe | Audit row 5.4 |
| Verify no free trial mechanic in Stripe + product flow | Eng + FinOps | Audit row 5.3 (Pr2-3 cross-validation) |
| Persona-overlay infrastructure | Design + Eng | `04` §3 + audit row 4.10 |
| Brand voice copy review across onboarding surfaces | Founder + Strategy CoS | Audit rows V.1–V.5 |
| Tabular figures + regime token color application | Design | Audit rows V.2 + V.3 |

---

## Anti-overclaim audit roll-up

Every NOW draft was authored against the §6.10 anti-overclaim flags + Scoopy custom instructions canonical phrasings:

- **Validation disclaimer** ("Testnet only. 30-day validation phase. No real capital.") — surfaced in `01` §6, `03` Steps 4 + 6, `04` §2 + §5, `05` audit rows 4.1 + X.1 + X.2.
- **Canonical 5 risk tokens** (10x / 10% / 5% / 5 / 80%) — surfaced in `04` §2 footer + §5 guardrail 3, `05` audit row 4.7.
- **PCC v2 §8 reference** — surfaced in `01` §6, `03` Steps 4 + 6, `04` §5 guardrail 4, `05` audit rows 4.8 + 5.4.
- **Founder-cohort canonical phrasing** ("Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies.") — surfaced in `01` §5 + §6, `05` audit row X.4. Inherited from `_pricing/03` §6.
- **"v2" / "v3" qualifiers on roadmap features** — surfaced in `01` §2 (Layla swim-lane), `04` §3 (Layla overlay), `05` audit row X.5.
- **Regime label color tokens** — surfaced in `04` §2, `05` audit row V.3. Per Scoopy custom instructions.

No new overclaim risks introduced. ONBOARDING contributes a clean baseline pending walk-through confirmation.

---

## Cross-workstream linkages

ONBOARDING produces inputs consumed by + depends on inputs from:

| Direction | Workstream | What | Where |
|---|---|---|---|
| ONBOARDING ← PACKAGING | `_packaging/02-free-vs-paid-boundary.md` | Free Scope B feature inventory + sub-$5k branch spec | `01-first-time-user-journey.md` §2; `04-first-value-experience-design.md` §3 |
| ONBOARDING ← PACKAGING | `_packaging/03-plan-comparison-table-v1.md` | Pricing page surface (gate 0) | `01` §1 gate 0; `05` audit rows 0.* |
| ONBOARDING ← PACKAGING | `_packaging/04-premium-feature-gating-rules.md` | Confidence-score gating + upgrade-prompt anti-pattern rules | `04` §7 failure modes; `05` audit row 4.4 |
| ONBOARDING ← PRICING | `_pricing/04-trial-and-intro-offer-options.md` | No-free-trial posture (Pr2-3) | `01` §1; `05` audit row 5.3 |
| ONBOARDING ← PRICING | `_pricing/03-monthly-vs-annual-offer-structure.md` §6 | Founder-cohort canonical phrasing + window comms | `01` §5; `05` audit row X.4 |
| ONBOARDING ← PRICING | `_pricing/02-initial-pricing-philosophy.md` | Anti-pressure principle (Principle 4 + 5) | `04` §1 first-value guardrails |
| ONBOARDING → SUPPORT | `02-activation-milestones-definition.md` § instrumentation | Cohort segmentation drives support triage | (forthcoming SUPPORT workstream) |
| ONBOARDING → SUPPORT | `05-friction-audit-across-current-flow.md` remediation backlog | Support runbook escalation criteria for onboarding-step failures | (forthcoming) |
| ONBOARDING → GTM | `01-first-time-user-journey.md` per-persona swim-lanes | Channel-mix decision (Phase 3) needs the persona-conversion-path map | (Phase 3) |
| ONBOARDING → GTM | `04-first-value-experience-design.md` first-value layout | Pricing-page CTA flow | (forthcoming GTM workstream) |
| ONBOARDING → §13 KPI | `02-activation-milestones-definition.md` §4 KPIs | Activation funnel KPIs feed §13 | Phase 4 |
| ONBOARDING → §11 financial model | Activation rates + sub-$5k → $5k conversion | Phase 4 §11 cohort modeling | Phase 4 |

---

## Linkage to Phase 2 charter exit criteria

Phase 2 charter §4 requires (ONBOARDING row):

> **ONBOARDING** — End-to-end flow specified: signup → email verification → exchange connection (Binance USDT-M, testnet-first) → first-signal-seen → first-gate-decision-seen → first-billing event. "We'll be back" sub-$5k branch defined. Documented in `_phase-2/03-onboarding.md`.

Status against exit criteria:

- ✓ End-to-end flow specified in `01-first-time-user-journey.md` (6 gates) + `03-signup-to-exchange-connection-flow.md` (9 steps + 4 rules).
- ✓ Email verification step defined (`03` Step 3).
- ✓ Exchange connection (Binance USDT-M, testnet-first) defined (`03` Steps 5–8 + On-1).
- ✓ First-signal-seen + first-gate-decision-seen defined (`02-activation-milestones-definition.md` F-3 + F-4; `04-first-value-experience-design.md`).
- ✓ First-billing event defined (`02` T-1 + DP-1 + DF-1).
- ✓ Sub-$5k branch defined (`03` Step 9 + branch §4 + On-4 + `04` §3).
- ⏳ Lock requires Eng walk-through (`05` REQUIRED INPUT) + decisions On-1 through On-7 + P0 remediation backlog cleared.

ONBOARDING workstream NOW work is **draft-complete**. Lock requires the seven **On-*** decisions, the live walk-through audit, and clearance of the eleven P0 remediation items.
