# PACKAGING — Premium Feature Gating Rules

**Task:** `[DOC] PACKAGING — Premium Feature Gating Rules`
**Type:** NOW
**Owner:** Eng lead + Strategy CoS
**Status:** DRAFT v0.1 — pending Phase 1 PRODUCT Scope Guardrails (NEXT) for final lock
**Feeds decision:** **Pk-4**
**Anchored to:** `02-free-vs-paid-boundary.md` matrix; §5.3.2 paid feature list; §6.5 Free Scope B; §6.10 anti-overclaim audit; Phase 1 BRAND voice (anti-pressure, methodical, evidence-led).

---

## 1. Gating taxonomy

Four gating types. Each feature in the boundary matrix gets exactly one type assigned.

| Type | Behavior | When to use | Anti-pattern to avoid |
|---|---|---|---|
| **Hard** | Feature is invisible or completely inaccessible to lower tiers. Click → upgrade modal. | Execution-adjacent (live orders); risk-config (real account); per-seat-only (DF). | Hard-gating informational features (reads as bait-and-switch). |
| **Soft** | Feature is visible but disabled. Hover/click reveals an inline upgrade prompt with the tier name + price. No modal. | Personalization features that are obviously useful but not execution-critical. | Pop-up modals that block the page. Multiple prompts per session. |
| **Degraded** | Lower tier gets a reduced form of the feature. Upgrade unlocks the full form. | Time-delayed signals (Free 15-min delay → T real-time); rate-limited API (T limited → DP standard); digest cadence (F weekly → T daily). | "Crippleware" framing — the degraded form must be genuinely useful, not just a tease. |
| **Read-only** | Lower tier gets read-only access; upgrade unlocks edit/write. | Cross-tier viewing (DF partner read-only seat); journal-as-teaser (post-validation candidate). | Withholding the *existence* of data. Read-only must show the actual data. |

**Default policy:** soft + degraded preferred over hard. Hard reserved for the five "no exceptions" features in the boundary doc.

---

## 2. Gating type per feature (full assignment)

### A. Signal output

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| Top-5 curated signals, 15-min delayed | Free | n/a | n/a | Free included. |
| Real-time signal feed | T | **Degraded** | F shows the 15-min-delayed list with a small "Real-time on Trader" inline link next to the timestamp | The delay itself is the gating signal — visible, honest, no modal. |
| Per-symbol regime label | Free | n/a | n/a | Free included (label only, no confidence). |
| Regime confidence score | T | **Degraded** | F shows label without confidence; T shows label + confidence (0.00–1.00). Inline "+ confidence on Trader" link next to label on F. | Confidence is the upgrade trigger — visible methodology improvement. |
| Multi-timeframe confirmation | T | **Soft** | F sees the row in the signal panel disabled with "Trader" badge. Click → inline copy: "Multi-timeframe confirmation is included in Trader ($79/mo)." | Single-click reveal. No modal. |
| Custom watchlist | T | **Hard** | F sees no watchlist UI element. Settings page shows "Watchlists are included in Trader and above" copy. | Feature is personalization — not visible until paid. |

### B. Risk gate

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| Demo-trade gate behavior view | Free | n/a | n/a | Free included. Trust demo. |
| Configurable risk gate | T | **Hard** | F sees the demo-trade gate working with default thresholds; "Configure your gate on your real account → Trader" link below the demo widget. | Hard because configuring a gate on a real account is execution-adjacent. |
| Live gate decisions on user account | T | **Hard** | F has no live-account binding (only demo-trade view). | Hard because it requires authenticated, billed exchange-account binding. |
| Multi-account portfolio heat | DP | **Soft** | T sees a single-account heat widget with "Multi-account portfolio heat in Desk Preview" link. | Soft — Trader users see what's missing. |
| Cross-exchange risk aggregation | DP | **Soft** | T sees the per-exchange row with disabled rollup; "Cross-exchange aggregation in Desk Preview" inline. | Soft — Trader users see what's missing. |

### C. Journal & analytics

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| Personal performance journal | T | **Hard** | F has no journal UI. Settings page shows "Journal is part of Trader ($79/mo)." | Hard per §5.3.2 + §6.5 explicit exclusion. *No exception for sub-$5k.* Post-validation candidate to soften → read-only teaser (per `02-free-vs-paid-boundary.md` §5). |
| Journal export (CSV) | T | n/a | n/a | T included. |
| Custom tags | T | n/a | n/a | T included. |
| Cohort comparison | DP | **Soft** | T sees a "Compare to cohort" CTA in journal that opens an inline upgrade prompt. | Soft — visible feature-presence without modal. |
| Static monthly PDF report | DP | **Hard** | T has no PDF generation UI. Settings page shows "Monthly performance reports are part of Desk Preview." | Hard per DP positioning. |
| Audit-grade partner reporting | DF (v2) | **Hard** | DP sees no partner reporting UI. Roadmap page references v2 launch window. | Hard + v2-flagged. |
| Tax-ready export | DF (v3) | **Hard** | All tiers see no tax-export UI. v3-deferred per §6.10 Flag-clean inventory. | Hard + v3-flagged. |

### D. Alerts & integration

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| In-app alerts | Free (read-only, delayed) | **Degraded** | F sees alerts feed, delayed; T+ sees real-time. Inline "Real-time on Trader" link in feed header. | Degraded — visible product-presence with honest cadence label. |
| Telegram bot routing | T | **Hard** | F has no Telegram-connect UI. Settings page shows "Telegram alerts are part of Trader." | Hard per §5.3.2. |
| Custom Telegram routing (multi-channel) | DF +seat | **Hard** | T / DP have single-channel only. DF settings shows "Multi-channel routing — add seats to enable." | Hard + seat-aware. |
| Email digest | Free (weekly) | **Degraded** | F gets weekly; T+ gets daily. Email footer reads "On Trader and above, this digest arrives daily." | Degraded. (ASSUMPTION — confirm Pk-2.) |
| Webhook egress | DP | **Hard** | T has no webhook UI. | Hard per DP positioning. |

### E. API & power-user

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| API access | T | **Degraded** | F has no API UI. T = limited rate; DP+ = standard rate. T users hitting the limit see "Upgrade to Desk Preview for standard rate" inline. | Degraded between T and DP — explicit Karim P2 trigger per §6.2. |
| Backtest sandbox | DP | **Hard** | T has no sandbox UI. Roadmap page references DP availability. | Hard per DP positioning. |

### F. Account

| Feature | Lowest paid tier | Gating type | Upgrade trigger | Notes |
|---|---|---|---|---|
| Multi-account / multi-exchange | DP | **Hard** | F / T have single-account UI. Settings page shows "Multi-account view — Desk Preview." | Hard per DP positioning. |
| Per-seat invoicing | DF | **Hard** | DP / T have no seat-management UI. DF settings shows "Add partner / analyst seats." | Hard + seat-only. |

---

## 3. Upgrade-prompt rules (anti-pressure)

Per Phase 1 BRAND voice (anti-overclaim, methodical, evidence-led) and §6.10 Flag 1 (no "lifetime" framing): upgrade prompts are quiet, honest, and rare.

### Frequency rules

- **Maximum one upgrade prompt visible per page.** No stacked prompts. No prompts on the dashboard hero.
- **Maximum one full-screen upgrade modal per session.** Triggered only on a deliberate user action that requires a paid feature (e.g., "Add to watchlist" click on Free).
- **No interstitial upgrade page** between any user action and its result. The result of a click on a soft-gated feature is the inline prompt, not a redirect.
- **No re-prompt within 24 hours** for the same feature. Once a user has dismissed the inline prompt for "Multi-timeframe confirmation," that prompt does not re-render until the next day.
- **No prompt during a signal arrival or a gate decision.** Trust-critical moments are sacred.
- **No prompt during a billing event** (renewal, payment failure, refund). Billing surface is not an upsell surface.

### Copy rules

- **Lead with the feature's function**, not the price. "Configure your gate on your real account" before "Trader $79/mo."
- **State the price plainly.** Never "starting at," never "as low as." Single number, single tier.
- **Never use "upgrade now," "limited time," "act fast."** Per BRAND voice — methodical, anti-pressure.
- **Acceptable verbs:** "available in," "included in," "part of," "unlocks." Never "exclusive," "premium," "elite."
- **For founder-cohort:** "Founder-cohort pricing — locked through your first renewal cycle, then standard pricing applies." Never abbreviate to "founder discount."
- **For sub-$5k Free users:** no upgrade prompts at all. Persistent in-product copy frames Trader as the destination per §6.5 (`02-free-vs-paid-boundary.md` §3). The notification fires when the account crosses $5k, not before.

### Visual rules (handoff to Design)

- **Inline prompts:** subtle muted background (#5B6472 fill, body text color), tier name + price as a single clickable text. No buttons. No icons. No badges.
- **Soft-gated rows:** disabled state uses 50% opacity + lock icon (lucide-react `Lock`, 12px, color `#A3ADBD`). Hover reveals inline prompt below the row.
- **Hard-gated UI absence:** the feature simply does not render. No grayed-out icons in nav. No "Locked" labels in menus. The user discovers the feature when they cross into the tier where it lives.
- **Modals:** plain. Single sentence describing the feature. Single price line. Single "Start [Tier]" button. Single "Maybe later" link. No imagery.

---

## 4. Downgrade rules

Per §6.7 mid-cycle changes: downgrades take effect at next renewal. Gating implications:

| At downgrade event | Behavior | Reasoning |
|---|---|---|
| User's exit-tier features (e.g., journal on T → F downgrade) become inaccessible at next renewal | Read-only access for 30 days post-downgrade | Allows export. Avoids data-hostage perception. |
| Multi-account user downgrades from DP → T | At next renewal, only first-connected account remains active. Other accounts disconnect (data retained 30 days for re-connection if user re-upgrades). | Avoids surprise data deletion. |
| DF customer removes a partner seat | Seat access ends at next renewal. Seat-holder receives 7-day-prior notice email. | Per §10 ops; avoids interpersonal friction within DF customer's team. |
| DF customer downgrades to DP | All seats end at next renewal. Per-seat charges stop pro-rated next billing cycle. | Hard cliff is acceptable here — the customer initiated the downgrade. |
| Any downgrade | Founder-cohort pricing does **not** carry forward. Re-upgrading after downgrade goes to standard pricing. | Per §6.7 cancellation policy + §6.10 Flag 1. |

---

## 5. Exception register

Two exceptions to the default rules above. Both documented for audit clarity.

1. **Validation cohort (P0) gating override.** P0 cohort members (cap 40 per §14) get full Trader-tier feature access during the validation phase regardless of billing state. Gating reverts to standard at P0 → P1 transition (`[DOC] PACKAGING — Beta Access Offer Design` defines the conversion offer per **Pk-6**).
2. **Compliance-driven gating override.** If a feature is region-blocked (e.g., US blocked at signup per memory `project_jurisdictional`), gating type is **Hard + region-message** regardless of feature category. Copy: "This feature is not available in your region." No upgrade prompt; no tier mention.

---

## 6. Engineering implementation contract

For Eng lead. Defines the entitlement contract feature flags must satisfy.

### Entitlement schema (canonical)

Every gated feature has a single entitlement key. Format: `feature.<area>.<name>`. Example: `feature.signal.realtime`, `feature.risk.configure`, `feature.journal.read`, `feature.journal.edit`, `feature.alerts.telegram`.

Each entitlement key resolves to one of:
- `enabled` (full access)
- `degraded:<form>` (e.g., `degraded:delayed-15m`, `degraded:rate-limited-1rps`)
- `readonly`
- `disabled`
- `region-blocked`

Tier → entitlement-key mapping is a single config file: `_data/entitlements/tier-matrix.yaml` (REQUIRED INPUT — Eng to create).

### Resolution rules

- Tier check must be **server-side authoritative**. Client-side feature flags are UX optimization only.
- Stripe subscription state is the source of truth for tier. Any drift between Stripe and entitlement = incident (P2 per `04-support.md` severity matrix).
- P0 cohort override is a separate flag (`cohort.p0.member`) that overlays Trader entitlements on top of Free billing state.
- Region-blocked is a separate flag (`region.blocked`) that supersedes all tier-driven entitlements.

### `[QA] PACKAGING — Billing-to-Entitlement Logic Review` (NEXT) consumes this contract.

---

## 7. Anti-overclaim audit on gating surfaces

| Surface | Audit pass? | Notes |
|---|---|---|
| Upgrade prompt copy ("available in," "included in") | ✓ | Anti-overclaim: no "premium," "exclusive," "elite" language. |
| Validation badge on Trader card | ✓ | "Stabilizing in cohort" status surfaces per §6.10 Flag 2. |
| Founder-cohort upgrade prompts | ✓ | "Locked through your first renewal cycle, then standard pricing applies" — no "lifetime," no "always." |
| v2 / v3-flagged features | ✓ | Roadmap-flagged inline; never sold as v1. |
| Sub-$5k user behavior (no upgrade prompts) | ✓ | Per §3.5 anti-persona "we'll be back" stance. |
| Region-blocked copy | ✓ | "Not available in your region" — no tier mention, no workaround suggestion. |

---

## 8. Open dependencies

- **Pk-4** decision (gating-type default) — currently drafted as soft + degraded preferred over hard. Hard reserved for execution-adjacent + 5 "no exceptions" features.
- **Phase 1 PRODUCT Scope Guardrails (NEXT)** — defines "execution-adjacent" / "personalization" precisely. Required to lock the boundary policy.
- **REQUIRED INPUT** — Eng to create `_data/entitlements/tier-matrix.yaml`.
- **REQUIRED INPUT** — Design to spec the inline-prompt visual treatment per §3 visual rules.

---

## 9. What this unlocks

- **Pk-4** decision can be marked recommended at "soft + degraded preferred."
- `[QA] PACKAGING — Billing-to-Entitlement Logic Review` (NEXT) has the entitlement contract to audit against.
- `[DOC] PACKAGING — Upgrade Path Design` (NEXT) inherits the upgrade-prompt and downgrade rules.
- Eng has a deterministic spec to implement against.
- Support runbook (`_phase-2/04-support.md`) gets the entitlement-drift incident criteria.
