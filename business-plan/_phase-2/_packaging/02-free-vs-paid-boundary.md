# PACKAGING — Free vs Paid Feature Boundary

**Task:** `[DOC] PACKAGING — Free vs Paid Feature Boundary`
**Type:** NOW
**Owner:** Strategy CoS + Eng lead
**Status:** DRAFT v0.1 — depends on Phase 1 PRODUCT MVP/Beta/Scale Feature Matrix lock for full feature inventory
**Feeds decision:** **Pk-2**
**Anchored to:** §6.5 Free Scope B (locked); §5.3.2 paid feature list; Phase 1 Decision Pr-4 (recommended at "top 10 + 15-min delay"); §3.5 anti-persona sub-$5k disciplined.

---

## 1. Boundary principle

Free **demonstrates the gate** without **substituting for Trader**. Three operational rules:

1. Free shows the system *making decisions* (regime label, gate behavior on demo trades) but never *executes for the user*.
2. Free shows *delayed, curated* signal output — enough to evaluate methodology, never enough to replace the Trader feed.
3. Free preserves the §5.3.1 capital-preservation primitives on demo trades because those are the trust demo, not the paywall.

If a feature is execution-adjacent, real-time, configurable, or personalized, it is paid. If a feature is read-only, delayed, or methodology-disclosure, it is Free. Edge cases below.

---

## 2. Feature × tier matrix

Tag legend: **F** = Free included · **T** = Trader included · **DP** = Desk Preview included · **DF** = Desk Full v2 included · **+seat** = per-seat add-on enables · **—** = excluded · **🔒** = hard-gated · **▽** = soft-gated (degraded form available below) · **R** = read-only at lower tier

### A. Signal output

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| Top-5 curated signal list, daily refresh, 15-min delayed | ✓ | ✓ | ✓ | ✓ | §6.5 Free locked. Pr-4 recommended boundary. |
| Real-time signal feed (full fidelity, all symbols) | — | ✓ | ✓ | ✓ | §5.3.2 paid; §6.5 excluded from Free. |
| Per-symbol regime label (Trending / Mean-Reverting / Volatile / Quiet) | ✓ | ✓ | ✓ | ✓ | §6.5 Free locked. No confidence score on Free. |
| Regime confidence score (0.00–1.00) | — | ✓ | ✓ | ✓ | §6.5 Free excluded. Trader+ only. |
| Multi-timeframe confirmation overlay | — | ✓ | ✓ | ✓ | §5.3.2 paid (REQUIRED INPUT — confirm in Phase 1 PRODUCT matrix). |
| Custom watchlist (user-selected symbols) | — | ✓ | ✓ | ✓ | Personalization → paid. |

### B. Risk gate behavior

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| Demo-trade view of risk gate behavior (read-only) | ✓ | ✓ | ✓ | ✓ | §6.5 Free locked. Trust demo. |
| Configurable risk gate (drawdown, daily loss, leverage limits below caps) | — | ✓ | ✓ | ✓ | 🔒 §5.3.2 paid. Hard gate — risk-config is execution-adjacent. |
| Live risk-gate decision overlay on user account | — | ✓ | ✓ | ✓ | 🔒 Personal account → paid. |
| Position-heat visualization across portfolio | — | — | ✓ | ✓ | DP+ — multi-account context. |
| Cross-account risk aggregation (multi-exchange / multi-account view) | — | — | ✓ | ✓ | DP+ — Layla scaling feature. |

### C. Journal & analytics

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| Personal performance journal | — | ✓ | ✓ | ✓ | §5.3.2 paid; §6.5 excluded from Free *no exception for sub-$5k*. |
| Journal export (CSV) | — | ✓ | ✓ | ✓ | Trader+. |
| Tag taxonomy + custom tags | — | ✓ | ✓ | ✓ | Trader+. |
| Cohort comparison (your performance vs anonymized peers) | — | — | ✓ | ✓ | DP+. (REQUIRED INPUT — confirm in PRODUCT matrix.) |
| Static monthly PDF performance report | — | — | ✓ | ✓ | §5 v1 Desk Preview spec. |
| Audit-grade partner reporting (LP-style) | — | — | — | ✓ | DF only. v3-deferred at v1; spec'd at v2 per §6.6. |
| Tax-ready export | — | — | — | ✓ | v3-deferred at v1 per §6.10. (REQUIRED INPUT — Phase 5 confirm.) |

### D. Alerts & integration

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| In-app alert feed (web) | ✓ R | ✓ | ✓ | ✓ | F gets read-only delayed; T+ gets real-time. |
| Telegram bot (@ScoopyAI_bot) routing | — | ✓ | ✓ | ✓ | §5.3.2 paid; §6.5 excluded from Free. |
| Custom Telegram routing (multi-channel, role-based) | — | — | — | ✓ +seat | DF + seat-aware. |
| Email alert digest (daily) | ✓ | ✓ | ✓ | ✓ | F gets weekly; T+ gets daily. (ASSUMPTION — confirm Pk-2.) |
| Webhook alert egress | — | — | ✓ | ✓ | DP+. |

### E. API & power-user

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| API access | — | ▽ | ✓ | ✓ | §5.3.2 paid. T = limited rate (~1 req/sec/endpoint per §5 v1); DP+ = standard. |
| API rate limit upgrade (Karim P2 trigger) | — | — | ✓ | ✓ | DP triggers upgrade per §6.2. |
| Backtest sandbox | — | — | ✓ | ✓ | DP+. (REQUIRED INPUT — confirm in PRODUCT matrix; Phase 5 v3 candidate.) |

### F. Methodology disclosure & trust signals

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| Engine methodology documentation | ✓ | ✓ | ✓ | ✓ | §5.3.1 — public regardless of tier. |
| Validation phase status disclosure | ✓ | ✓ | ✓ | ✓ | §5.3.1 — public. |
| "What CoinScopeAI does not do" reference page | ✓ | ✓ | ✓ | ✓ | §5.3.4 — public. |
| Live engine status / uptime page | ✓ | ✓ | ✓ | ✓ | Trust signal — public. |
| Per-signal trace (regime + confidence + gate result + sizing rationale) | — | ✓ | ✓ | ✓ | T+ — methodology-evidence link to actual signals. |

### G. Account & billing

| Feature | F | T | DP | DF | Notes / source |
|---|---|---|---|---|---|
| Account verification at signup | ✓ | ✓ | ✓ | ✓ | §6.5 — Free is account-verified. |
| Single-account exchange connection | ✓ | ✓ | ✓ | ✓ | Required for verification. Binance USDT-M only at P1. |
| Multi-account exchange connection | — | — | ✓ | ✓ | DP+. Layla canvas. |
| Multi-venue (Bybit when P2 ships) | — | — | (P2) | (P2) | Design-only at Phase 2; P2 = Aug-Sep 2026. |
| Annual billing | — | ✓ | ✓ | ✓ | All paid tiers. ~17% discount per §6.6. |
| Founder-cohort pricing (60-day window) | — | ✓ | ✓ | ✓ | §6.7. |
| Per-seat invoicing | — | — | — | ✓ +seat | DF only. Stripe quantity-based. |

---

## 3. Sub-$5k disciplined branch (locked, operational form)

Per §6.5: Free **includes** account verification at any size. For verified accounts where the connected exchange account is below $5k:

- All Free features above remain available.
- Persistent in-product copy frames Trader as the destination, not a paywall (§6.5 — never "upgrade now" pressure copy).
- Optional "notify me when account crosses $5k" subscription — opt-in, account-balance-event driven.
- Demo-trade capital-preservation primitives (kill switch, drawdown ceilings) operate on demo trades to demonstrate that we treat their discipline seriously.
- §13 KPI: track sub-$5k Free → Trader conversion separately from $5k+ Free → Trader. Different conversion-trigger mechanics.

**Anti-pattern guard:** sub-$5k users do **not** get a tighter feature subset than $5k+ Free. Same Free Scope B, different conversion messaging. Tightening Free for sub-$5k reads as second-class treatment and breaks §3.5 "we'll be back" stance.

---

## 4. The five hard "no exceptions"

These five are excluded from Free with no envisioned exception, even post-validation:

1. **Real-time signal feed** — execution-adjacent; differentiates trust-demo from operational tool.
2. **Configurable risk gate** — execution-adjacent; configuring a gate on a real account is the line.
3. **Personal performance journal** — personalization; explicit §5.3.2 + §6.5 exclusion.
4. **Telegram bot routing** — alert egress to a personal channel is operational use.
5. **API access** — operational use by definition.

If a future decision opens any of these to Free, it requires explicit amendment to §6.5 with founder sign-off and §13 KPI re-baseline (per Phase 2 charter §5 risk row "Free tier scope drift").

---

## 5. The two soft "post-validation candidates"

These two could plausibly open as Free post-validation if §13 KPIs surface conversion problems:

| Candidate | Trigger to consider | Form |
|---|---|---|
| Journal *read-only* (no editing, no tagging, last 30 days) | Free → Trader < 2% over 90 days at Scope B | Read-only journal as a 30-day teaser; tag/edit/export remain paid |
| Daily email digest (vs current weekly assumption) | Daily-digest engagement metric outperforms weekly by >2x for similar tools in benchmark | Move daily digest to Free; keep custom routing paid |

Both are **opt-in revisions** post-P0 cohort, not Phase 2 commitments.

---

## 6. Edge cases

| Case | Behavior | Reasoning |
|---|---|---|
| Free user crosses $5k mid-week | "Notify me" fires; in-product CTA shifts to Trader entry; no auto-upgrade | Auto-upgrade without consent breaks consent + creates billing surprise. |
| Trader user's account drops below $5k | No tier change. They're already paying. | Account-size floor applies at signup, not retention. |
| Free user has multi-exchange account but only connects Binance | Free works; multi-account view is DP+ regardless of exchange count | Multi-account view = paid feature, not exchange-count gating. |
| Trader user wants Telegram on more than one channel | Single channel at T; multi-channel routing is DF +seat | Per §5.3.2 + DF feature set. |
| Desk Preview user wants partner read-only | Not available — partner seats are DF-only add-on | Per-seat is DF differentiator; offering on DP collapses Preview→Full step. |
| Sub-$5k user complains about journal exclusion | Reaffirm: sub-$5k Free is not entitled to journal; "we'll be back" framing | §5.3.2 packaging principle, §6.5 explicit. No exception. |
| Free user tries to connect mainnet account | Account verification accepts; demo trades only; no execution | §5.3.1 demo-trade primitives work on connected mainnet account; no orders placed. PCC v2 §8 enforces. |

---

## 7. Open dependencies

- **Pr-4 final form** (Free-tier limits) — directly determines the "top-5 + 15-min delay" specifics in row A.
- **Phase 1 PRODUCT MVP/Beta/Scale Feature Matrix** — supplies the canonical feature inventory; rows marked REQUIRED INPUT must be reconciled against it.
- **Phase 1 PRODUCT Scope Guardrails** — defines "personalized" / "execution-adjacent" so the boundary principle is operationally testable.
- **§5.2.3 dashboard IB items** — "stabilizing in cohort" status must be visually surfaced per §6.10 Flag 2; affects Trader feature display on pricing page.

---

## 8. What this unlocks

- **Pk-2** decision can be marked recommended at Scope B as-locked.
- `[DOC] PACKAGING — Plan Comparison Table v1` consumes the matrix above directly.
- `[DOC] PACKAGING — Premium Feature Gating Rules` consumes the 🔒 / ▽ / R columns to assign gating type per feature.
- §13 KPI framework gets two distinct conversion metrics: sub-$5k Free → Trader and $5k+ Free → Trader.
- Onboarding flow (`_phase-2/03-onboarding.md`) gets the sub-$5k branch spec.
