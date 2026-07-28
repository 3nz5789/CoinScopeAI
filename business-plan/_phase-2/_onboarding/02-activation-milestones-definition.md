# ONBOARDING — Activation Milestones Definition

**Task:** `[DOC] ONBOARDING — Activation Milestones Definition`
**Type:** NOW
**Owner:** Strategy CoS + Eng
**Status:** DRAFT v0.1 — operational definitions + instrumentation spec
**Anchored to:** `01-first-time-user-journey.md` 6-gate sequence; engine API endpoints (/scan, /risk-gate, /position-size, /regime/{symbol}, /performance, /journal); §6.5 Free Scope B; §13 KPI framework input; PRICING `_pricing/05-price-to-margin-sensitivity-model.md` (§6.9 conversion benchmarks).

---

## 1. Definition of "activated"

**Activated = a user has crossed the threshold where they have seen enough of the product to make an informed decision about retention or conversion.**

For Free, that's seeing the trust demo (gate 4). For Trader, it's seeing a real-capital-context signal + at least one journal entry. For Desk Preview, it's seeing multi-account aggregation. For Desk Full v2 (post-launch), it's seeing the audit-grade reporting surface + adding at least one partner seat.

Activation is **not** the same as conversion. Activation is *prerequisite* to conversion. A user who activates and never converts is informative (suggests product-fit gap); a user who converts without activating is a billing event without product engagement (suggests false-positive conversion or accidental signup).

---

## 2. Per-tier milestone table

### Free milestones (5 ordered events)

| # | Milestone | Operational definition | Instrumentation event | Target time | Activation criterion |
|---|---|---|---|---|---|
| F-1 | Account verified | Email verified + record created | `signup.email_verified` | <5 min post-signup | Required |
| F-2 | Exchange connected | Binance USDT-M API key validated, account-balance read | `signup.exchange_connected` { exchange, account_size_band, testnet_or_mainnet } | <15 min post-email-verify | Required |
| F-3 | First signal seen | User session has rendered the top-5 signal list at least once | `value.first_signal_seen` { signal_count, time_since_connect } | <5 min post-exchange-connect | Required for activation |
| F-4 | First gate decision seen | User session has rendered the demo-trade gate decision view at least once | `value.first_gate_decision_seen` { gate_result, regime_at_decision } | <10 min post-exchange-connect | Required for activation |
| F-5 | Methodology page viewed | User session has navigated to engine methodology docs | `value.methodology_viewed` | Within 7 days | Optional; trust-confidence indicator |

**Activation condition (Free):** F-1 + F-2 + F-3 + F-4 within 24 hours of signup.

### Trader milestones (5 ordered events)

| # | Milestone | Operational definition | Instrumentation event | Target time | Activation criterion |
|---|---|---|---|---|---|
| T-1 | Trader subscription activated | Stripe subscription state = active for Trader tier | `billing.tier_activated` { tier: "trader", billing_cadence, founder_cohort: bool } | At conversion | Required |
| T-2 | First real-time signal seen | User has rendered at least one full-fidelity (non-delayed) signal | `value.realtime_signal_seen` | <5 min post-Trader-activation | Required for activation |
| T-3 | Risk gate configured | User has set at least one custom threshold within Capital Cap | `value.risk_gate_configured` { params_changed } | <30 days post-Trader-activation | Strong activation indicator |
| T-4 | First journal entry | User has added or auto-imported at least one trade entry | `value.first_journal_entry` { source: manual_or_imported } | <30 days | Strong activation indicator |
| T-5 | Telegram bot connected | User has linked Telegram bot (per **On-3** post-first-signal nudge) | `value.telegram_connected` | <14 days | Optional; engagement amplifier |

**Activation condition (Trader):** T-1 + T-2 + (T-3 OR T-4) within 14 days of subscription activation.

### Desk Preview milestones (5 ordered events)

| # | Milestone | Operational definition | Instrumentation event | Target time | Activation criterion |
|---|---|---|---|---|---|
| DP-1 | Desk Preview subscription activated | Stripe subscription state = active for DP tier | `billing.tier_activated` { tier: "desk_preview", ... } | At conversion | Required |
| DP-2 | Multi-account connected | User has connected ≥2 exchange accounts (or ≥1 multi-account view) | `value.multi_account_connected` { account_count } | <14 days post-DP-activation | Strong activation indicator |
| DP-3 | First cross-account view rendered | Multi-account heat or aggregation view rendered in user session | `value.multi_account_view_seen` | <14 days | Required for activation |
| DP-4 | First monthly PDF report generated | Static monthly performance PDF generated and downloaded | `value.first_pdf_report` | First month-end after DP-activation | Required for activation |
| DP-5 | Backtest sandbox used | User has run at least one backtest session | `value.first_backtest_run` | <30 days | Optional; engagement amplifier |

**Activation condition (Desk Preview):** DP-1 + (DP-2 OR DP-3) + DP-4 within 60 days of subscription activation.

### Desk Full v2 milestones (5 ordered events, v2 launch March-May 2027)

| # | Milestone | Operational definition | Instrumentation event | Target time | Activation criterion |
|---|---|---|---|---|---|
| DF-1 | Desk Full v2 subscription activated | Stripe subscription state = active for DF v2 tier | `billing.tier_activated` { tier: "desk_full_v2", ... } | At conversion | Required |
| DF-2 | First audit-grade report generated | Partner-reporting (LP-style) report generated | `value.first_audit_report` | <30 days post-DF-activation | Required for activation |
| DF-3 | First partner seat added | At least one partner read-only seat added to subscription | `billing.first_partner_seat_added` | <60 days | Strong activation indicator (per-seat density) |
| DF-4 | Custom Telegram routing configured | Multi-channel Telegram routing set | `value.custom_telegram_configured` | <30 days | Optional |
| DF-5 | First analyst seat added | At least one analyst seat added | `billing.first_analyst_seat_added` | <90 days | Optional; per-seat density upside |

**Activation condition (Desk Full v2):** DF-1 + DF-2 + DF-3 within 90 days of subscription activation.

---

## 3. Per-persona activation expectations

| Persona | Expected activation path | Expected time to activation | Conversion likelihood post-activation |
|---|---|---|---|
| Omar (P1) | F-1 → F-2 → F-3 → F-4 → (Free retention 14–60 days) → T-1 → T-2 → T-4 | F-activation: <30 min; T-activation: 14d–14m | Free→Trader: 5% base case (per §6.9) |
| Karim (P2) | F-1 → F-2 → F-3 → F-4 → F-5 (methodology) → (Free retention 3–14 days) → T-1 → T-2 → T-3 → (DP trigger when API limit binds) → DP-1 | F-activation: <60 min; T-activation: 3–14d; DP-activation: 90–180d | Free→Trader: ~10%; Trader→DP: ~15% |
| Layla (P3) | F-1 → F-2 → F-3 → F-4 → (Free retention 1–3 days) → DP-1 (skip Trader) → DP-2 → DP-3 → DP-4 | F-activation: <30 min; DP-activation: <60d | Free→DP: ~15–25% (higher pain, higher WTP); DP→DF v2 at v2 launch: 70% base case |
| Sub-$5k disciplined | F-1 → F-2 → F-3 → F-4 → (Free retention indefinite) → ($5k threshold trigger) → T-1 | F-activation: <30 min; T-activation: variable, dependent on account growth | Conversion at $5k threshold: ASSUMPTION pending cohort data |

---

## 4. Activation funnel KPIs

Per `_pricing/05-price-to-margin-sensitivity-model.md` §3 sensitivity ranks. The following KPIs feed §13:

| KPI | Definition | Base | Upside | Downside | Falsifier |
|---|---|---|---|---|---|
| **Signup → F-2 (exchange-connected) rate** | % of email-verified accounts that complete exchange connection within 24h | 70% | 85% | 50% | <40% = signup-flow broken |
| **F-2 → F-4 (first gate decision) rate** | % of exchange-connected accounts that see the demo gate decision | 90% | 95% | 75% | <60% = gate decision UI broken |
| **F-activated → Free retention 7d** | % of F-activated users who return within 7 days | 60% | 75% | 40% | <30% = first value insufficient |
| **F-activated → Trader (90 days)** | Free → Trader conversion (per §6.9) | 5% | 10% | 2% | <2% = Pk-2 reopens |
| **T-1 → T-2 (real-time signal seen) rate** | % of Trader subscriptions that see a real-time signal within 5 min of activation | 95% | 99% | 80% | <80% = Trader onboarding broken |
| **T-1 → (T-3 OR T-4) within 14d** | % of Trader subscriptions that activate (per §2 Trader activation) | 70% | 85% | 50% | <50% = Trader value gap |
| **DP-1 → DP-2 (multi-account) rate** | % of DP subscriptions that connect ≥2 accounts within 14d | 75% | 90% | 50% | <50% = DP positioning gap |
| **DF-1 → DF-3 (first partner seat) rate** | % of DF subscriptions that add ≥1 partner seat within 60d | 60% | 80% | 30% | <30% = per-seat density assumption broken (Pk-3 + Pr2-1 implications) |
| **Sub-$5k Free → Trader at $5k threshold** | % of sub-$5k Free users who upgrade within 30 days of crossing $5k | 25% | 40% | 10% | <10% = "we'll be back" mechanism not working |

---

## 5. Instrumentation requirements

For Eng. Defines what must be instrumented before any activation KPI can be tracked.

### Event schema (canonical)

Every milestone event has:

```
event_name:    string (snake_case, namespaced: signup.* / value.* / billing.*)
user_id:       UUID
session_id:    UUID
timestamp:     ISO 8601 UTC
tier:          enum { free, trader, desk_preview, desk_full_v2 }
cohort:        enum { p0_validation, p1_narrow_ship, p2_vendor_expansion, public, founder_cohort_in_window, founder_cohort_locked, sub_5k }
event_props:   object (event-specific; see milestone tables above)
```

### Required instrumentation surface

- **Web dashboard:** all `signup.*` and `value.*` events except `billing.*`.
- **Stripe webhooks:** all `billing.*` events.
- **Engine API:** must emit `value.first_signal_seen` and `value.first_gate_decision_seen` based on session-level rendering, not just API call count (a /scan call that returns no rendered UI does not count).
- **Telegram bot:** `value.telegram_connected` event from bot-side webhook.

### Cohort assignment logic

- `p0_validation` → assigned at signup if signup window is in P0 (May 2026).
- `p1_narrow_ship` → assigned if signup window is in P1 (Jun-Jul 2026).
- `founder_cohort_in_window` → assigned if signup is within 60 days of public launch.
- `founder_cohort_locked` → transitions to `founder_cohort_in_window` at end of first renewal cycle (then expires to `public`).
- `sub_5k` → assigned at F-2 if `account_size_band < $5k`; transitions out if `account_size_band` crosses $5k.

### REQUIRED INPUT — current instrumentation gap audit

Eng must confirm which of the events above are currently instrumented vs. need to be added:

| Event family | Likely status (REQUIRED INPUT — Eng confirm) |
|---|---|
| `signup.email_verified` | Likely instrumented (auth flow) |
| `signup.exchange_connected` | Partially instrumented (need account_size_band + testnet_or_mainnet props) |
| `value.first_signal_seen` | Likely not instrumented at session-render level |
| `value.first_gate_decision_seen` | Likely not instrumented |
| `value.risk_gate_configured` | REQUIRED INPUT |
| `value.first_journal_entry` | REQUIRED INPUT |
| `value.telegram_connected` | REQUIRED INPUT (Telegram bot side) |
| `billing.*` | Partial (Stripe webhooks may not all flow to product analytics) |

---

## 6. Activation cohort segmentation

Per `_pricing/03-monthly-vs-annual-offer-structure.md` §3 + §13 KPI framework: cohorts segmented by

1. **Tier at activation** — Free / Trader / DP / DF v2
2. **Persona-fit signal** (if scored at signup per Phase 1 ICP `Persona Fit Scoring Model`) — Omar / Karim / Layla / sub-$5k / unscored
3. **Signup window** — P0 validation / P1 narrow ship / P2 / public / founder-cohort-window
4. **Billing cadence** — monthly / annual
5. **Account size band** at exchange-connect — sub-$5k / $5k–$50k / $50k–$200k / $200k–$1M / >$1M

Cross-cuts that matter for §13:
- **Persona × Tier × Cadence** — does Layla on annual DP retain better than Layla on monthly DP?
- **Founder-cohort-window × Tier** — does founder-cohort uptake actually lift conversion or just compress price?
- **Sub-$5k × Time-to-$5k-threshold** — what's the median time for sub-$5k Free to cross $5k?

---

## 7. Anti-patterns flagged

| Anti-pattern | Why it matters | Mitigation |
|---|---|---|
| Counting "signup" as activation | Misleading; bills as growth metric what is actually intent metric | Use signup as funnel-entry, not activation |
| Counting "Stripe billing event" as activation for Trader | Misses users who pay but never see real-time signal (false-positive conversion) | T-1 alone is not Trader-activation; T-1 + T-2 + (T-3 or T-4) is |
| Aggregating activation across personas | Hides persona-specific drop-off | Per-persona activation rate is the load-bearing metric |
| Ignoring cohort dimension in activation rate | Validation cohort behaves differently than public cohort | Cohort segmentation required in every KPI cut |
| Re-defining activation post-hoc to make a KPI look better | KPI gaming | Activation definition is locked at this doc; revisions require explicit decision-log entry |

---

## 8. What this unlocks

- `[METRICS] ONBOARDING — Activation KPI Dashboard` (NEXT) consumes this doc directly.
- `[QA] ONBOARDING — Friction Audit Across Current Flow` consumes the funnel KPIs as the audit lens.
- §13 KPI/OKR framework gets the canonical activation-milestone definitions.
- §11 Phase 4 financial model has activation-rate inputs aligned with §6.9 conversion benchmarks.
- Eng has an instrumentation backlog (REQUIRED INPUT roll-up in §5).
- ONBOARDING NEXT `Education Sequence` knows the milestone-target-time windows for cadence design.
