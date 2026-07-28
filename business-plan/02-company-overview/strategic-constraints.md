# Strategic Constraints

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **operating contract**. Each constraint is one of three classes:

- **HARD** — code-level or policy-level binding; cannot be changed without explicit decision-log entry and pre-mortem review
- **OPERATIONAL** — strongly-binding default; can be changed only with named owner, documented rationale, and downstream impact statement
- **SOFT** — current default for capital-efficiency or focus reasons; revisable as the situation changes

Constraints in this file extend — they do not contradict — the 10 hard constraints in `01-executive-summary/business-model-summary.md` §7.

---

## 1. Risk-related constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| R1 | Max drawdown 10% (account, hard stop) | HARD | PCC v2 §8 Capital Cap; locked 2026-05-01 |
| R2 | Daily loss limit 5% (24h rolling, halts trading) | HARD | PCC v2 §8 |
| R3 | Max leverage 10x per position (locked, supersedes earlier 20x) | HARD | PCC v2 §8 Capital Cap, 2026-05-01 |
| R4 | Max open positions 3 concurrent | HARD | Engine threshold; locked |
| R5 | Position heat cap 80% (per position, blocks new entries) | HARD | Engine threshold; locked |
| R6 | All risk numbers surfaced first-class in UI when composing a position | HARD | Brand-voice rule; trust observable in 30 seconds |
| R7 | All risk numbers paired with the disclaimer "Testnet only. 30-day validation phase. No real capital." | HARD | Anti-overclaim discipline |
| R8 | Risk-gate refusal includes the explicit gate that fired | HARD | Trust through transparency |
| R9 | Threshold changes require pre-mortem skill invocation before first edit | OPERATIONAL | `feedback_premortem_required.md` + skill `risk-pcc-pre-flight` |
| R10 | Threshold changes require simultaneous patch of CLAUDE.md, docs/, .env*, master prompt paste — same pass | OPERATIONAL | `feedback_risk_threshold_reconciliation.md` |

> Note: the canonical 5 tokens (10x / 10% / 5% / 5 pos / 80%) appear identically in `01-executive-summary/`, `00-framework.md`, the decision log, PCC v2, and CLAUDE.md. Drift in any one location is a guardrail violation.

---

## 2. Trust-related constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| T1 | Anti-overclaim across product, brand, marketing, fundraising, and recruiting | HARD | The trust moat |
| T2 | "Production-ready" claim disallowed until PCC v2 §8 passes | HARD | Locked phrasing rule |
| T3 | Product-tier voice (terse, declarative, data-led, no emoji) inside product surfaces | HARD | Voice posture; never marketing-tier voice in-product |
| T4 | Social-tier voice (aspirational, meme-fluent) only on social channels | HARD | Voice posture |
| T5 | Scoopy speaks in product tier only | HARD | In-product agent + Telegram companion |
| T6 | Every claim links to its data, model, or rule (regime label, confidence, gate result) | HARD | Methodical and evidence-led principle |
| T7 | No fabricated benchmarks, leaderboards, or "track record" pages while on testnet | HARD | Anti-overclaim |
| T8 | Any external claim passes a brand-voice review pass before publishing | OPERATIONAL | Brand-voice enforcement skill |
| T9 | No paid-promotion language ("boost", "10x your account", "guaranteed") under any cohort condition | HARD | Anti-overclaim |
| T10 | Trust signals (incident transparency, postmortems, decision-log openness) preferred over conventional marketing trust signals | OPERATIONAL | Brand differentiation |

---

## 3. Provider / exchange dependency constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| P1 | P1 vendor stack is narrow (CCXT, CoinGlass, Tradefeeds, CoinGecko, Claude minimal) | OPERATIONAL | Capital efficiency + cohort safety |
| P2 | Bybit and additional venues deferred to P2 | OPERATIONAL | Engine stability on Binance USDT-perp first |
| P3 | Engine designed to detect drift between local state and exchange truth | HARD | `binance-bybit-integration-guard` skill |
| P4 | WebSocket reconnect, signing, ping/pong handling reviewed before any new venue | HARD | Same skill |
| P5 | Vendor outage falls back to graceful degradation; never to silent stale data | HARD | Trust posture |
| P6 | Stripe is sole billing provider through P2; alternative gated on entity decision | OPERATIONAL | Tax / VAT alignment with entity |
| P7 | Telegram Bot API is companion surface, not primary; outage degrades alerts only | OPERATIONAL | Dashboard-first design |
| P8 | Claude API use is minimal during P1; not on the critical path for risk-gate decisions | HARD | Capital safety; deterministic gates only |
| P9 | Vendor master-services agreements gated on entity restructure | OPERATIONAL | Sole prop has limited contracting capacity |
| P10 | Vendor cost step-up evaluated at P2 charter, not before | OPERATIONAL | Avoid optimizing capacity that does not exist yet |

---

## 4. Compliance / claims constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| C1 | US users blocked at signup until US licensure path is decided | HARD | Counsel brief v2 + jurisdictional posture |
| C2 | No claim of investment advice; counsel-confirmed posture is "tools, not advice" | HARD | `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` |
| C3 | Risk-disclosure surface present at signup and in product | HARD | `_data/legal/Risk_Disclosure_v0_DRAFT.md` |
| C4 | No "guaranteed" / "risk-free" / "double your account" language anywhere | HARD | Anti-overclaim |
| C5 | No customer testimonials presented as institutional / regulator endorsement | HARD | Anti-overclaim |
| C6 | UAE/MENA + global EN target; geographies outside this set are not actively pursued | OPERATIONAL | Capital efficiency + entity alignment |
| C7 | Founder cohort cohort-pricing terms documented; not generally advertised | OPERATIONAL | Cohort discipline |
| C8 | Tax / VAT handling for UAE/EU/MENA cross-border requires counsel input before scaling | OPERATIONAL | Compliance posture |
| C9 | KYC / AML posture inherited from exchange (capital stays in user's exchange account); CoinScopeAI is not the regulated entity | OPERATIONAL | Custody-free choice |
| C10 | Public benchmarks or "track record" only after §8 passes + counsel review | HARD | Anti-overclaim + regulatory posture |

---

## 5. Onboarding / support constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| O1 | Onboarding terminates at testnet sandbox during validation; no real-capital path | HARD | PCC v2 §8 |
| O2 | Exchange connection via API key (least-privilege scopes); no withdrawal scope ever | HARD | Custody-free posture |
| O3 | Onboarding completion measured against documented activation milestones | OPERATIONAL | `_phase-2/_onboarding/02-activation-milestones-definition.md` |
| O4 | First-value experience occurs before billing capture, not after | OPERATIONAL | `_phase-2/_onboarding/04-first-value-experience-design.md` |
| O5 | Support inbox response within published SLA; SLA framework v1 in production | OPERATIONAL | `_phase-2/_support/02-support-sla-framework.md` |
| O6 | All support replies follow product-tier voice | HARD | Brand consistency |
| O7 | Incident-class tickets escalate per documented severity matrix | OPERATIONAL | `_phase-2/_support/03-ticket-routing-and-escalation-rules.md` |
| O8 | Founder is sole on-call through P1; P4 contractor support around v2 build | OPERATIONAL | Bus-factor mitigation in highest-risk window |
| O9 | Cohort cap of 40 paid users in P1 is not exceeded for support-load reasons | HARD | Phase map locked; support discipline |
| O10 | KB articles (when introduced) follow customer-support skill conventions and pass brand-voice review | OPERATIONAL | Consistency |

---

## 6. Billing / ops constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| B1 | Tier matrix locked: Free / $79 / $399 / $1,199 + per-seat ($149 or $249) | HARD | Locked v1 |
| B2 | Founder-cohort pricing applied per cohort document; not generally advertised | OPERATIONAL | Cohort discipline |
| B3 | Annual prepay discount rate **DECISION NEEDED** before P1 billing live | OPERATIONAL | Open question |
| B4 | Trial mechanics (free-as-trial vs. time-bounded) **DECISION NEEDED** | OPERATIONAL | Open question |
| B5 | Stripe handles billing; alternative gated on entity decision | OPERATIONAL | Same as P6 above |
| B6 | Refunds within published policy; ad-hoc refunds documented in support log | OPERATIONAL | Trust posture |
| B7 | Plan changes are user-initiated and immediately reflected in entitlements | OPERATIONAL | Tier-matrix integrity |
| B8 | Billing failures trigger documented dunning; no silent suspension | OPERATIONAL | Trust posture |
| B9 | Billing data is not used for marketing personalization without explicit consent | HARD | Privacy posture |
| B10 | Per-seat scaling is a Desk Full v2 deliverable; not enabled at Trader or Desk Preview | OPERATIONAL | Tier-matrix integrity |

---

## 7. Growth constraints

| # | Constraint | Class | Rationale |
|---|---|---|---|
| G1 | No paid acquisition before Trader CAC validates (target M5+) | OPERATIONAL | Capital efficiency |
| G2 | Founder-led distribution is the primary GTM motion in P1 and P2 | OPERATIONAL | Trust through founder voice |
| G3 | Cohort cap of 40 in P1 is not exceeded for growth reasons | HARD | Same as O9 |
| G4 | Public launch (P2) opens only after P1 cohort observation passes its exit criteria | HARD | Phase map locked |
| G5 | Channel-mix decisions made post P1 cohort observation, not before | OPERATIONAL | Data-led GTM |
| G6 | No affiliate / referral program with payouts pre-validation | OPERATIONAL | Anti-overclaim risk |
| G7 | No copy-trading, leader-follower, or "follow the founder" mechanics ever | HARD | Custody-free + anti-overclaim |
| G8 | No PR push pre-validation; warm conversations only | OPERATIONAL | Anti-overclaim |
| G9 | Recruiting and hiring discussions follow the same anti-overclaim posture | HARD | Voice consistency |
| G10 | Geographic expansion outside UAE/MENA + global EN deferred until post-validation | OPERATIONAL | Capital efficiency |

---

## 8. What the company should avoid doing too early

A consolidated "do not yet" list. Each item is dangerous *not because it's wrong*, but because it's wrong *now*. Each links to where the trigger condition lives.

| # | Avoid | Trigger to revisit | Source |
|---|---|---|---|
| A1 | Real-capital deployment | PCC v2 §8 pass | `_data/operations/Production_Candidate_Criteria_v2.md` |
| A2 | Paid acquisition | Trader CAC validates (M5+) | `01-executive-summary/strategic-priorities.md` D1 |
| A3 | Public launch | P1 cohort exit criteria pass | Phase map (P2) |
| A4 | Bybit and additional venues | P2 charter | `_phase-2/00-phase-2-charter.md` (when written) |
| A5 | Desk Full v2 GA | P5 (Mar–May 2027) | Phase map |
| A6 | US user signup | US licensure path decided | `Counsel_Brief_v2.md` |
| A7 | Priced equity raise | Validation pass + entity restructure | `01-executive-summary/strategic-priorities.md` P10 |
| A8 | Hiring full-time engineers | Post-validation, post-raise | Capital efficiency |
| A9 | Native mobile app | P2+, only if cohort demands it | Web + Telegram cover the cohort |
| A10 | Custody, fund, exchange products | Not planned in any P0–P5 phase | Structural posture |
| A11 | Affiliate / referral payouts | Post-validation, with structured guardrails | Anti-overclaim risk |
| A12 | Copy-trading / leader-follower mechanics | Not planned | Anti-overclaim + custody-free |
| A13 | Public benchmarks / "track record" pages | §8 pass + counsel review | Anti-overclaim + regulatory |
| A14 | Multi-language UI beyond EN | Post-P5 | Capacity discipline |
| A15 | Aggressive content / viral marketing | Post-validation, with anti-overclaim guardrails | Brand discipline |

---

## 9. How constraints are amended

To change any constraint:

1. State the constraint, its class (HARD / OPERATIONAL / SOFT), and current rationale.
2. State the proposed change and the new rationale.
3. Run `risk-pcc-pre-flight` for any HARD constraint touching risk, PCC, regime labels, or persona.
4. Run a pre-mortem (`feedback_premortem_required.md`) before locking the new version.
5. Update in the same pass: this file, `01-executive-summary/business-model-summary.md` §7, decision log, master prompt paste (where applicable), CLAUDE.md (where applicable), `.env*` (if a numeric threshold).
6. Run the brand-voice / drift-detector guardrails to confirm no orphaned references.

A change that does not pass steps 1–5 is not a change. It is drift.

---

## 10. Cross-references

- 10 hard constraints (master): `01-executive-summary/business-model-summary.md` §7
- "Do not prioritize yet" list: `01-executive-summary/strategic-priorities.md` §3
- PCC v2 (gates + §8): `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Decision log: `business-plan/_decisions/decision-log.md`
- Brand-voice rules: `business-plan/09-brand-messaging.md`
- Counsel brief: `business-plan/_data/legal/Counsel_Brief_v2.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
