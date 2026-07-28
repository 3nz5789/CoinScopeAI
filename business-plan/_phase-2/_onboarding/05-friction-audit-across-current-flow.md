# ONBOARDING — Friction Audit Across Current Flow

**Task:** `[QA] ONBOARDING — Friction Audit Across Current Flow`
**Type:** NOW
**Owner:** Strategy CoS + Design
**Status:** DRAFT v0.1 — surface-by-surface audit; remediation backlog. **Several findings flagged REQUIRED INPUT pending Eng walk-through of current production flow** (audit performed against documented architecture + Phase 2 specs, not against live product walk-through).
**Anchored to:** `01-first-time-user-journey.md` 6-gate sequence; `02-activation-milestones-definition.md` instrumentation requirements; `03-signup-to-exchange-connection-flow.md` 9-step + 4-rule spec; `04-first-value-experience-design.md` first-value layout; PRICING `_pricing/04-trial-and-intro-offer-options.md` (no free trial, Pr2-3); PACKAGING `_packaging/05-packaging-friction-review.md` design rules; §6.5 Free Scope B; PCC v2 §8.

---

## 1. Audit method

The audit checks the documented current architecture (per memory `project_state_2026-05-02` + Scoopy custom instructions + project repo `3nz5789/coinscope-ai`) and the documented product surfaces (dashboard at coinscope.ai, Telegram bot @ScoopyAI_bot, engine API endpoints) against the Phase 2 specs in this workstream. Findings are categorized:

- **PASS** — current behavior matches Phase 2 spec.
- **GAP** — current behavior is missing or insufficient vs. spec.
- **DRIFT** — current behavior contradicts the spec or anti-overclaim discipline.
- **REQUIRED INPUT** — cannot be assessed without live product walk-through; flagged for Eng confirmation.

Each finding has a severity rating (P0 ship-blocker / P1 lock-blocker / P2 quality / P3 polish) and a remediation row.

---

## 2. Audit findings — gate by gate

### Gate 0 — Pre-signup (landing → pricing → CTA)

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 0.1 | Pricing page tier comparison | 4-tier horizontal grid + per-seat sub-section per `_packaging/03` | REQUIRED INPUT — current pricing page structure | P1 | REQUIRED INPUT |
| 0.2 | Validation badge on pricing page | "Testnet only · 30-day validation · No real capital" prominent on every paid tier card | REQUIRED INPUT | P0 | REQUIRED INPUT |
| 0.3 | Founder-cohort window comms | Sub-header: "Founder-cohort pricing available through [LAUNCH DATE + 60 days]." | REQUIRED INPUT — does pricing page surface this today? | P1 | REQUIRED INPUT |
| 0.4 | "Stabilizing in cohort" status on Trader card | Per §6.10 Flag 2 | REQUIRED INPUT | P1 | REQUIRED INPUT |
| 0.5 | AED courtesy display footer | Per `_packaging/03` §1 footer + §6.8 mitigation | REQUIRED INPUT | P2 | REQUIRED INPUT |

### Gate 1 — Region check

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 1.1 | Pre-signup region check | IP-based geolocation hint at landing-page CTA click; US blocked before signup form | REQUIRED INPUT — does current flow check region pre-signup or post-signup? | P0 | REQUIRED INPUT |
| 1.2 | Region-block copy | "CoinScopeAI is not currently available in your region. We're a UAE-based sole prop with global English-language reach in MENA, Europe, and other markets. US availability is not on our roadmap at this time." | REQUIRED INPUT | P1 | REQUIRED INPUT |
| 1.3 | Server-side region enforcement | Signup endpoint validates region on submit | REQUIRED INPUT — Eng confirm | P0 | REQUIRED INPUT |

### Gate 2 — Signup form

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 2.1 | Form fields | Email + password + ToS checkbox; optional country self-select | REQUIRED INPUT | P2 | REQUIRED INPUT |
| 2.2 | Marketing opt-in checkbox at signup | NOT present per `_pricing/02` Principle 4 | REQUIRED INPUT — verify no marketing-opt-in at signup | P1 | REQUIRED INPUT |
| 2.3 | Persona self-classification | NOT at signup (deferred to scoring elsewhere per Phase 1 ICP) | REQUIRED INPUT — verify no persona-quiz at signup | P2 | REQUIRED INPUT |
| 2.4 | Brand voice register | Product-tier — terse, technical, declarative; not "Join the community!" social-tier | REQUIRED INPUT — copy review | P2 | REQUIRED INPUT |
| 2.5 | Password baseline | Min 12 chars (REQUIRED INPUT — confirm baseline) | REQUIRED INPUT | P2 | REQUIRED INPUT |

### Gate 3 — Exchange connect (Steps 4–9 of `03`)

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 3.1 | Welcome page + exchange-connect intro | Single-screen explainer with "We use this to / We never" trust block | REQUIRED INPUT — does Step 4 welcome screen exist? | P0 | REQUIRED INPUT |
| 3.2 | Exchange selection UI | Binance USDT-M only; other venues shown as "coming [date]" not "available" | REQUIRED INPUT | P1 | REQUIRED INPUT |
| 3.3 | Testnet vs mainnet toggle | Default: Testnet. Both paths valid. PCC v2 §8 reasoning copy. | REQUIRED INPUT — does toggle exist? | P0 | REQUIRED INPUT |
| 3.4 | API key entry — read-only checkbox | Required for mainnet path; auto-checked for testnet | REQUIRED INPUT | P1 | REQUIRED INPUT |
| 3.5 | API key validation — write-permission rejection | Block, not silently accept | REQUIRED INPUT — Eng confirm | P0 | REQUIRED INPUT |
| 3.6 | Account-balance read at validation | Read account balance for sub-$5k branch evaluation | REQUIRED INPUT — Eng confirm | P0 | REQUIRED INPUT |
| 3.7 | IP-restriction recommendation | Static IP allowlist published for Eng outbound API calls | REQUIRED INPUT — confirm we publish this | P2 | REQUIRED INPUT |

### Gate 4 — First value

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 4.1 | Validation badge in header | "Testnet only · 30-day validation · No real capital" | REQUIRED INPUT | P0 | REQUIRED INPUT |
| 4.2 | Top-5 signals visible | Top-5 curated signals, 15-min delayed on Free | Likely instrumented (engine /scan endpoint exists) | P1 | LIKELY PASS — REQUIRED INPUT |
| 4.3 | Regime label on each signal | Trending / Mean-Reverting / Volatile / Quiet with canonical regime tokens (color per Scoopy) | REQUIRED INPUT — does dashboard render regime label? | P0 | REQUIRED INPUT |
| 4.4 | Confidence score on Free | Hidden on Free per `_packaging/02` row A. T+ only. | REQUIRED INPUT — verify Free does NOT show confidence | P1 | REQUIRED INPUT — gating leak risk |
| 4.5 | Demo-trade gate decision section | Latest demo decision rendered with reasoning bullets within 5 min of exchange-connect | REQUIRED INPUT — does this section exist? | P0 | REQUIRED INPUT |
| 4.6 | Gate decision reasoning bullets | Position heat / open positions / drawdown / daily loss values vs caps | Engine /risk-gate endpoint provides this; UI rendering REQUIRED INPUT | P0 | REQUIRED INPUT |
| 4.7 | Canonical 5 risk tokens in footer | "10x leverage · 10% drawdown · 5% daily loss · 5 open positions · 80% position heat" verbatim | REQUIRED INPUT | P0 | REQUIRED INPUT |
| 4.8 | PCC v2 §8 reference in footer | "Production Candidate Criteria v2 §8 enforces all caps." | REQUIRED INPUT | P1 | REQUIRED INPUT |
| 4.9 | Engine status / methodology / "what we don't do" links in footer | All three public, linked from every page | REQUIRED INPUT — confirm public + linked | P1 | REQUIRED INPUT |
| 4.10 | Persona-overlay infrastructure | In-line tour overlays per persona (Omar / Karim / Layla); dismissible | NOT present (new spec) | P2 | GAP — Phase 2 build |
| 4.11 | Sub-$5k persistent banner | "We'll be back for you when your account crosses $5k. Trader unlocks then." | REQUIRED INPUT — does sub-$5k branch UI exist? | P0 | REQUIRED INPUT |
| 4.12 | Conversion prompts on first-value page | NONE — gate 4 is sacred for trust demo | REQUIRED INPUT — verify no upgrade prompts on first-value | P1 | REQUIRED INPUT — anti-pattern risk |

### Gate 5 — First conversion event

| # | Surface | Spec | Current | Severity | Status |
|---|---|---|---|---|---|
| 5.1 | Free → Trader upgrade prompt mechanics | Single quiet prompt on first journal click attempt; no modal interstitial | REQUIRED INPUT — current prompt mechanics | P1 | REQUIRED INPUT |
| 5.2 | Trader signup → Stripe billing flow | Standard Stripe Checkout; founder-cohort promo code applied if in window | REQUIRED INPUT — confirm Stripe configured per Pr2-1 + Pr2-4 | P0 | REQUIRED INPUT |
| 5.3 | No free trial mechanic | Pr2-3 lock — no Trader trial in any form | REQUIRED INPUT — `[QA] PRICING — Stripe Plan Mapping Review` overlap | P0 | REQUIRED INPUT (cross-workstream) |
| 5.4 | Trader entitlement activation post-billing | Stripe webhook → entitlement YAML → tier check; <30s end-to-end | REQUIRED INPUT — Eng confirm | P0 | REQUIRED INPUT |
| 5.5 | First-real-time-signal post-Trader-activation | T-2 milestone within 5 min | REQUIRED INPUT — verify activation funnel | P1 | REQUIRED INPUT |

---

## 3. Audit findings — cross-cutting

### Anti-overclaim discipline

| # | Surface | Spec | Severity | Status |
|---|---|---|---|---|
| X.1 | Validation disclaimer pinned across all pages, not just pricing | Per Scoopy custom instructions — universal pairing with risk surfaces | P0 | REQUIRED INPUT |
| X.2 | "Testnet only / 30-day validation / no real capital" canonical phrasing | Single canonical string; never abbreviated to "testnet" alone | P1 | REQUIRED INPUT |
| X.3 | "Trade Smarter With AI" tagline usage | Allowed in marketing-tier surfaces (pricing page header per `_packaging/03`); never in product-tier signal/gate surfaces | P2 | REQUIRED INPUT |
| X.4 | Founder-cohort copy | Canonical: "Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies." Never "lifetime / forever / always / locked-in." | P1 | REQUIRED INPUT |
| X.5 | "v2" / "v3" qualifiers on roadmap features | Audit-grade reporting / tax-ready export / multi-channel Telegram routing / Bybit — all qualified | P1 | REQUIRED INPUT |

### Brand voice consistency

| # | Surface | Spec | Severity | Status |
|---|---|---|---|---|
| V.1 | Product-tier register on dashboard | Technical, terse, declarative, data-led; no emoji; no "Let's go!" social-tier copy | P2 | REQUIRED INPUT — copy review |
| V.2 | Numbers monospaced / tabular figures | Per Scoopy custom instructions | P3 | REQUIRED INPUT — design review |
| V.3 | Regime token colors used consistently | #00FFB8 / #A3ADBD / #F5A623 / #5B6472 per Scoopy | P2 | REQUIRED INPUT — design review |
| V.4 | Telegram bot copy matches dashboard register | Same product-tier language | P2 | REQUIRED INPUT — bot copy audit |
| V.5 | Email copy (verification, notifications) matches register | Same product-tier; not promotional | P2 | REQUIRED INPUT — email copy audit |

### Instrumentation

| # | Surface | Spec | Severity | Status |
|---|---|---|---|---|
| I.1 | `signup.email_verified` event | Per `02-activation-milestones-definition.md` §5 | P1 | LIKELY PASS — REQUIRED INPUT |
| I.2 | `signup.exchange_connected` event with full props | { exchange, account_size_band, testnet_or_mainnet } | P1 | PARTIAL — REQUIRED INPUT |
| I.3 | `value.first_signal_seen` event | Session-render-level, not API-call-level | P1 | LIKELY GAP — REQUIRED INPUT |
| I.4 | `value.first_gate_decision_seen` event | Session-render-level | P1 | LIKELY GAP — REQUIRED INPUT |
| I.5 | `value.risk_gate_configured` event | T+ only | P2 | REQUIRED INPUT |
| I.6 | `value.first_journal_entry` event | T+ only | P2 | REQUIRED INPUT |
| I.7 | `value.telegram_connected` event | Bot-side webhook | P2 | REQUIRED INPUT |
| I.8 | `billing.*` events from Stripe webhooks | All flow to product analytics | P1 | REQUIRED INPUT |
| I.9 | Cohort assignment logic | Per `02` §5 (p0_validation / p1_narrow_ship / sub_5k / etc.) | P2 | LIKELY GAP — REQUIRED INPUT |

---

## 4. Highest-priority remediation backlog

Sorted by severity. Each item assumed to require Eng confirmation first; status will move from REQUIRED INPUT → GAP/DRIFT/PASS after walk-through.

### P0 — ship-blockers (must clear before P1 Narrow Ship public launch)

1. **Pre-signup region check + server-side enforcement.** Without this, US users complete onboarding and discover region restriction late — Class C anti-pattern. Audit row 1.1 + 1.3.
2. **Validation badge in header on every page.** Universal disclaimer pairing per Scoopy. Audit row X.1 + 4.1.
3. **Welcome page + "We never trade / execute / withdraw" trust block at exchange-connect.** Trust-load-bearing surface. Audit row 3.1.
4. **Testnet vs mainnet toggle + PCC v2 §8 reasoning copy.** Anti-overclaim discipline at the most-execution-adjacent step. Audit row 3.3.
5. **Write-permission API key block.** Technical guarantee for "we never place orders." Audit row 3.5.
6. **Demo-trade gate decision section on first-value page within 5 min of exchange-connect.** Trust demo F-4; without this, gate 4 fails. Audit row 4.5 + 4.6.
7. **Canonical 5 risk tokens in footer.** Trust signal. Audit row 4.7.
8. **Sub-$5k persistent banner UI.** §3.5 anti-persona stance operational. Audit row 4.11.
9. **Stripe billing flow for Trader signup with founder-cohort promo code.** Required for Pr2-1 + Pr2-4. Audit row 5.2.
10. **Trader entitlement activation post-billing webhook.** Without this, T-1 → T-2 gap is permanent. Audit row 5.4.
11. **No free trial mechanic in Stripe or product flow.** Pr2-3 violation. Audit row 5.3.

### P1 — lock-blockers (must clear before Phase 2 close)

12. Founder-cohort window comms on pricing page (audit row 0.3).
13. "Stabilizing in cohort" status on Trader card (audit row 0.4).
14. Region-block copy text canonical (audit row 1.2).
15. Marketing opt-in checkbox NOT at signup (audit row 2.2).
16. Read-only-scope checkbox at API key entry (audit row 3.4).
17. Regime label rendered on each signal (audit row 4.3).
18. Confidence score gating — Free does NOT show confidence (audit row 4.4).
19. PCC v2 §8 reference in footer (audit row 4.8).
20. Engine status / methodology / "what we don't do" public links (audit row 4.9).
21. No conversion prompts on first-value page (audit row 4.12).
22. Free → Trader upgrade prompt mechanics — single quiet prompt, not modal (audit row 5.1).
23. Anti-overclaim canonical phrasings (audit rows X.2 + X.4 + X.5).
24. Instrumentation: `value.first_signal_seen`, `value.first_gate_decision_seen`, full `signup.exchange_connected` props (audit rows I.2 + I.3 + I.4).

### P2 — quality

25. Persona-overlay infrastructure on first-value (audit row 4.10) — Phase 2 build.
26. Brand voice consistency review (audit rows V.1 + V.4 + V.5).
27. Tabular figures + regime token colors design review (audit rows V.2 + V.3).
28. Optional country self-select on signup form (audit row 2.1).
29. Form fields baseline + password policy (audit rows 2.1 + 2.5).
30. Persona self-classification NOT at signup (audit row 2.3).
31. AED courtesy display footer (audit row 0.5).
32. IP-restriction recommendation at API key entry (audit row 3.7).
33. Cohort assignment logic (audit row I.9).
34. Remaining instrumentation (audit rows I.1 + I.5–I.8).

### P3 — polish

35. (None at v0.1; deferred until P0/P1/P2 clear.)

---

## 5. Cross-workstream remediation overlap

Several remediation items overlap with other Phase 2 workstreams. Documented to avoid duplicate work:

| Audit row | Overlaps with | Coordination |
|---|---|---|
| 0.1, 0.2, 0.4 (pricing page) | PACKAGING `_packaging/03-plan-comparison-table-v1.md` | PACKAGING owns pricing-page spec; ONBOARDING audit confirms current state vs spec |
| 5.3 (no free trial) | PRICING `[QA] Stripe Plan Mapping Review` (NEXT) | PRICING owns Stripe audit; ONBOARDING audit cross-references |
| 5.2, 5.4 (Stripe billing flow + entitlement) | PACKAGING `[QA] Billing-to-Entitlement Logic Review` (NEXT); PRICING `[QA] Stripe Plan Mapping Review` (NEXT) | Three workstream audits converge on Stripe + entitlement layer |
| 4.4 (confidence score gating leak) | PACKAGING `_packaging/04-premium-feature-gating-rules.md` | PACKAGING owns gating spec; ONBOARDING audit catches gating leaks |
| X.4 (founder-cohort copy) | PRICING `_pricing/03-monthly-vs-annual-offer-structure.md` §6 | PRICING owns copy; ONBOARDING audit confirms application |
| V.1–V.5 (brand voice) | Phase 1 BRAND patternbook + voice/tone | Phase 1 owns canonical; ONBOARDING audit confirms consistency in onboarding surfaces |

---

## 6. Audit findings — DRIFT (current behavior contradicts spec)

**None confirmed at v0.1 — REQUIRED INPUT for all surfaces.**

If the live walk-through surfaces DRIFT (e.g., a free trial is enabled in Stripe, or sub-$5k users see different features, or pricing page lacks validation badge), each finding moves to DRIFT classification with explicit anti-pattern callout. DRIFT findings are higher priority than GAP findings because they are *incorrect* behavior to be removed, not *missing* behavior to be added.

---

## 7. Audit findings — PASS (current matches spec)

Pending Eng walk-through, the following are *likely PASS* based on documented architecture:

- Engine API endpoints exist and serve `/scan`, `/risk-gate`, `/regime/{symbol}` (per `coinscopeai-engine-api` skill).
- Telegram bot @ScoopyAI_bot exists and is wired to alert flow (per Scoopy custom instructions).
- Dashboard at coinscope.ai serves the product surface (per `coinscopeai-architecture` skill).
- Stripe is the payment processor (per §6.8).

These are likely PASS but require explicit confirmation in walk-through.

---

## 8. Recommended next action

Schedule a **30-minute Eng + Founder + Strategy CoS walk-through of the live signup → first-value flow** with this audit document open. For each REQUIRED INPUT row:

1. Walk the surface live.
2. Mark PASS / GAP / DRIFT.
3. Capture screenshot or DOM evidence for any GAP / DRIFT.
4. Assign owner + estimate to remediation backlog.

Output: this document updated with PASS / GAP / DRIFT determinations and a sized remediation backlog. Phase 2 cannot exit ONBOARDING workstream until P0 backlog is cleared.

---

## 9. What this unlocks

- ONBOARDING workstream NOW deliverables cleared subject to walk-through.
- Eng has a deterministic audit checklist to walk against.
- Phase 2 charter §4 ONBOARDING exit criterion has a structured path: walk-through → backlog → P0 clear → lock.
- §13 KPI framework instrumentation gaps explicit (audit rows I.*).
- Cross-workstream coordination explicit (§5) — no duplicate audit work in PACKAGING / PRICING / SUPPORT.
