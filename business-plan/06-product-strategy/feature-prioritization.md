# Feature Prioritization

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **operating list of features**, classified by priority, by tier, and by what each one enables (trust / activation / retention / monetization). It is the document the founder reads before saying yes to any "let's add this" suggestion.

The prioritization framework is **conservative by design**: a feature must earn its way onto the must-have list, not be defaulted onto it. The discipline is:

1. **Necessary features beat impressive features.**
2. **Features that preserve the five differentiators (D1–D5) are non-negotiable.**
3. **Features that contradict a strategic constraint are disallowed regardless of perceived value.**
4. **Capacity is the binding constraint** — solo founder + P4 contractor at v2 build.

---

## 1. Prioritization framework

Each feature is classified along three axes:

### Axis A — Priority
- **Must-have** — without it, the stage cannot pass its readiness gate
- **Should-have** — high leverage; ship in stage if possible; defer to next stage if not
- **Later** — in scope eventually but explicitly not in current stage
- **Never** (in P0–P5 horizon) — out of scope by structural posture or sequencing

### Axis B — Tier
- **Free** / **Trader** / **Desk Preview** / **Desk Full v2** — first tier where the feature surfaces

### Axis C — Lens
- **Trust** — features that build / preserve trust premium
- **Activation** — features that drive Free → Paid or new-user → activated-user
- **Retention** — features that keep cohort engaged over 30 / 60 / 90 days
- **Monetization** — features that justify a tier upgrade or per-seat addition

A feature can be tagged with multiple lenses. The lens classification is what makes the feature defensible against scope creep — if a proposed feature does not score on any lens, it does not belong on the list.

---

## 2. Master feature table — Must-have / Should-have / Later

### MVP must-haves (P0 → P1 launch)

| # | Feature | Tier | Lens | Pillar |
|---|---|---|---|---|
| MH-1 | Multi-pair scanner with documented confluence ranking | Trader | Activation, Retention | 1 |
| MH-2 | Regime classifier (v3 ML) with confidence on every signal | Trader | Trust, Activation | 2 |
| MH-3 | Pre-arming risk gate (5 locked thresholds) with explicit refusal pattern | Trader | **Trust**, Retention | 3 |
| MH-4 | Position sizer with formula + inputs + output transparency | Trader | **Trust**, Activation | 3 |
| MH-5 | Configurable per-user thresholds | Trader | Trust, Retention | 3 |
| MH-6 | Single-account journal with R-multiple + rule-violation tagging | Trader | Activation, Retention | 5 |
| MH-7 | Telegram canonical payload (regime + confidence + gate result) | Trader | Activation, Retention | 4 |
| MH-8 | Web dashboard with first-class risk-numbers strip | Trader | Trust, Activation | 4 |
| MH-9 | Auth + onboarding flow with first-value pre-billing | Trader | Activation | — |
| MH-10 | Exchange connection (Binance Testnet) with least-privilege scope copy | Trader | **Trust**, Activation | — |
| MH-11 | Stripe billing wired against locked tier matrix | Trader | Monetization | — |
| MH-12 | Code-level testnet hard-gate (CI re-verified per release) | (substrate) | **Trust** | — |
| MH-13 | PCC v2 published artifact | (substrate) | **Trust** | — |
| MH-14 | Validation-phase disclaimer above the fold | (substrate) | **Trust** | — |
| MH-15 | Brand-voice enforcement skill in production | (substrate) | **Trust** | — |
| MH-16 | Free-tier scanner + regime sample (no risk-gate output) | Free | Activation | 1, 2 |

### Beta must-haves (P1 close target)

| # | Feature | Tier | Lens | Pillar |
|---|---|---|---|---|
| MH-17 | Multi-account view at Desk Preview | Desk Preview | Monetization, Retention | 4 |
| MH-18 | Advanced gates: per-account override, combination, time-of-day | Desk Preview | Monetization, Trust | 3 |
| MH-19 | Read API at Desk Preview (documented payloads) | Desk Preview | Monetization (P2 Karim) | 4 |
| MH-20 | Multi-account performance attribution | Desk Preview | Monetization, Retention | 5 |
| MH-21 | Audit log on threshold changes | Desk Preview | **Trust**, Monetization | 3 |
| MH-22 | Support inbox + SLA framework v1 in production | (substrate) | **Trust**, Retention | — |
| MH-23 | Incident playbook v1 + first dry-run | (substrate) | **Trust** | — |
| MH-24 | Vendor failure-mode runbooks extended; dry-run before P2 | (substrate) | **Trust** | — |
| MH-25 | Cohort observation cadence active; weekly cohort review | (substrate) | Retention (cohort signal) | — |
| MH-26 | §3.7 persona interviews complete; persona reconfirmation filed | (substrate) | Retention | — |

### Should-haves (in stage if capacity allows; defer to next stage if not)

| # | Feature | Tier | Lens | Pillar | Stage |
|---|---|---|---|---|---|
| SH-1 | Cross-pair regime context on scanner | Trader | Activation, Retention | 1, 2 | Beta |
| SH-2 | Regime page with inputs + recent transitions | Trader | Trust | 2 | Beta |
| SH-3 | Telegram alert dedup / rate-limit / grouping per `alerting-and-user-experience` skill | Trader | Retention | 4 | MVP / Beta |
| SH-4 | Performance-by-regime breakdowns | Trader / Desk Preview | Retention | 5 | Beta |
| SH-5 | Manual-journal-abandonment leading-indicator surface | Trader | Retention | 5 | Beta |
| SH-6 | First-class risk-numbers strip on dashboard hero | Trader | Trust | 3, 4 | MVP |
| SH-7 | Locked-numbers display strip ("10% / 5% / 10x / 5 / 80%") visible when composing | Trader | Trust | 3 | MVP |
| SH-8 | API-key scope copy: explicit "no withdrawal scope, ever" copy at exchange-connection step | (substrate) | **Trust** | — | MVP |
| SH-9 | Anti-overclaim review pass on all surfaces before P1 launch | (substrate) | **Trust** | — | MVP |
| SH-10 | Founder-led distribution content artifact (long-form explainer) | (off-product) | Activation | — | Beta |
| SH-11 | Stripe annual prepay flow (rate **DECISION NEEDED**) | Trader / Desk Preview | Monetization | — | Beta |
| SH-12 | Cohort-data exit-memo artifact published post-validation | (off-product) | **Trust** | — | Beta close |

### Later (eventually in scope, but not in current or next stage)

| # | Feature | Tier | Lens | Earliest stage |
|---|---|---|---|---|
| L-1 | Bybit USDT-perp (read-only scan first; gate-and-arm parity later) | (cross-tier) | Activation, Retention | Scale-A (P2) |
| L-2 | Vendor redundancy (data) | (substrate) | Trust | Scale-A (P2) |
| L-3 | Public launch operations (signup at scale; support at scale) | (substrate) | Activation | Scale-A (P2) |
| L-4 | Cohort-level analytics surface | Desk Preview / Desk Full v2 | Retention, Monetization | Scale-A → Scale-B |
| L-5 | Per-seat permissions on shared accounts | Desk Full v2 | Monetization (per-seat) | Scale-B (P5) |
| L-6 | Partner read-only views | Desk Full v2 | Monetization (per-seat) | Scale-B (P5) |
| L-7 | Audit-grade journal with partner-readable reports | Desk Full v2 | Trust, Monetization | Scale-B (P5) |
| L-8 | Audit-grade regime history | Desk Full v2 | Trust | Scale-B (P5) |
| L-9 | Per-seat threshold permissions / rule-change log | Desk Full v2 | Trust, Monetization | Scale-B (P5) |
| L-10 | Backtest user-defined rules against history | (cross-tier; Desk+ likely) | Retention | Post-P5 evaluation |
| L-11 | Additional venues beyond Binance USDT-M and Bybit | (cross-tier) | Activation | Post-P2 evaluation |

### Never (P0–P5 horizon)

| # | Feature / direction | Why never |
|---|---|---|
| N-1 | Custody / pooled capital / managed accounts | Structural posture |
| N-2 | Autonomous execution without user authorization | Custody-free + user-authorized posture |
| N-3 | Alpha generation as a product | Out of scope; Vision A mismatch |
| N-4 | Signal subscription / signal-as-deliverable | Anti-signal-service positioning |
| N-5 | Copy-trading / leader-follower mechanics | Custody-free + anti-overclaim |
| N-6 | Fund-formation tooling | Out of scope; counsel-line |
| N-7 | Spot exchange operations / brokerage / market-making | Out of scope |
| N-8 | US-licensed retail flow | Until licensure decision |
| N-9 | Public benchmarks / leaderboards / "track record" pages while on testnet | Anti-overclaim |
| N-10 | Affiliate / referral payouts pre-validation | Anti-overclaim risk |
| N-11 | White-label / private-label arrangements | Out of scope |
| N-12 | Native mobile app pre-P5 | Capacity discipline; web + Telegram cover |
| N-13 | Multi-language UI beyond EN pre-P5 | Capacity discipline |
| N-14 | "AI" as standalone feature without specific evidence | Anti-overclaim |
| N-15 | Performance-promising surfaces (any) | Anti-overclaim |

---

## 3. Features by lens

A consolidated read of the master table, organized by what each feature enables.

### 3.1 Features that support TRUST

The trust premium is the moat. These features are non-negotiable.

| Feature | How it builds trust |
|---|---|
| Pre-arming risk gate with explicit refusal pattern (MH-3) | Discipline is enforced, observable in 30 seconds |
| Math transparency in position sizer (MH-4) | The buyer can verify; we cannot hide |
| Code-level testnet hard-gate (MH-12) | Posture is enforced, not just claimed |
| PCC v2 publication (MH-13) | Production-ready criteria are public and falsifiable |
| Validation-phase disclaimer above the fold (MH-14) | State is honest, not buried |
| Brand-voice enforcement skill (MH-15) | Anti-overclaim discipline is mechanical, not willpower-based |
| Least-privilege API-key scope copy (SH-8) | API-key trust earned at the friction step |
| Audit log on threshold changes (MH-21, Desk Preview+) | Trust through transparency |
| Vendor failure-mode runbooks + dry-run (MH-24) | Trust through incident-readiness |
| Cohort-data exit memo (SH-12) | Trust through evidence post-validation |
| First-class risk-numbers strip (SH-6, SH-7) | Risk numbers are first-class UI |

### 3.2 Features that support ACTIVATION

Free → Paid; new-user → activated-user.

| Feature | How it activates |
|---|---|
| Free-tier scanner + regime sample (MH-16) | First-value experience pre-billing |
| Multi-pair scanner (MH-1) | Replaces the user's manual watchlist; immediate utility |
| Regime classifier with confidence (MH-2) | Replaces the user's mental regime classification |
| Position sizer with math transparency (MH-4) | Match-to-hand-calculation moment converts |
| Telegram canonical payload (MH-7) | First good alert is an activation moment |
| Auth + onboarding with first-value pre-billing (MH-9) | Smooth path from signup to first useful output |
| Exchange connection with least-privilege copy (MH-10) | Trust at the friction step |
| Cross-pair regime context (SH-1) | Increases day-one usefulness |
| Founder-led distribution artifact (SH-10) | Drives qualified discovery |

### 3.3 Features that support RETENTION

30 / 60 / 90-day cohort retention; manual-journal abandonment as a leading indicator.

| Feature | How it retains |
|---|---|
| Pre-arming risk gate (MH-3) | The gate firing correctly during volatile sessions is the durable retention moment |
| Configurable per-user thresholds (MH-5) | Framework-respect is durable |
| Single-account journal with R-multiple tagging (MH-6) | The journal is a sticky surface — replaces a hated manual task |
| Telegram canonical payload (MH-7) | Reliable, low-noise alerts retain |
| Telegram dedup / rate-limit / grouping (SH-3) | Alert fatigue is the largest churn driver |
| Multi-account view (MH-17) | Retention pillar for P3 Layla |
| Manual-journal-abandonment surface (SH-5) | Leading indicator; product makes the surface irreversible |
| Cohort observation cadence (MH-25) | Retention quality at the cohort level |
| Performance-by-regime breakdowns (SH-4) | Reflection moments retain |
| Support inbox + SLA framework (MH-22) | First incident handled well — retention multiplier |

### 3.4 Features that support MONETIZATION

Trader → Desk Preview → Desk Full v2 upgrade economics; per-seat scaling.

| Feature | How it monetizes |
|---|---|
| Multi-account view at Desk Preview (MH-17) | Trader → Desk Preview upgrade lever |
| Advanced gates at Desk Preview (MH-18) | Desk Preview value-delivery surface |
| Read API at Desk Preview (MH-19) | P2 Karim → Desk Preview upgrade lever |
| Multi-account performance attribution (MH-20) | Desk Preview → Desk Full v2 upgrade lever |
| Audit log on threshold changes (MH-21) | Desk Preview value-delivery surface; partial-foreshadowing of Desk Full v2 |
| Stripe annual prepay flow (SH-11) | Cash-flow timing + cohort commitment |
| Per-seat permissions (L-5, L-6) | Desk Full v2 per-seat economics |
| Audit-grade journal + partner-readable reports (L-7) | Desk Full v2 anchor |
| Audit-grade regime history (L-8) | Desk Full v2 differentiation |

---

## 4. Rationale for prioritization

The prioritization above follows five rules that hold across the master table:

1. **Capital preservation features (Pillar 3) are non-negotiable.** MH-3, MH-4, MH-5 carry the locked Vision A; if any one is weak, the product fails its primary identity test.
2. **Trust-building substrate is must-have, not should-have.** MH-12, MH-13, MH-14, MH-15 are not "nice-to-haves" — they are the structural posture in product form. Without them, the anti-overclaim moat is rhetorical, not real.
3. **Free-tier discipline is a monetization decision, not a product decision.** MH-16 deliberately omits risk-gate output from Free. This is the locked tier-matrix integrity rule. Re-litigating it requires `06-pricing-monetization.md` review.
4. **Beta must-haves cluster around Desk Preview quality bar.** MH-17 through MH-21 are the Desk Preview surface; if Desk Preview is weak by P1 close, the upgrade narrative collapses and the post-validation fundraise narrative weakens.
5. **Operational maturity features appear in Beta.** MH-22, MH-23, MH-24, MH-25 are not "product features" in the conventional sense, but they are part of the product surface in a discipline-software context. Without them, Beta cannot pass its readiness gate.

The trade-offs that are *deliberately* made:

- **Bybit (L-1) is deferred to P2** even though it's technically buildable in Beta. Engine stability + cohort signal quality on a single venue is more valuable than venue breadth at this stage.
- **Read API (MH-19)** is at Desk Preview, not Trader, even though P2 Karim might pay $79 for it. The tier-matrix integrity rule wins; read API is the Desk Preview value-delivery anchor for P2 Karim.
- **Backtest user-defined rules (L-10)** is deferred to post-P5, even though it would deepen Pillar 5. The retention lift does not justify the build cost during validation.
- **Native mobile app (N-12)** is durable-deferred even with cohort demand. Web + Telegram cover; capacity discipline wins.

---

## 5. Feature-deferral decision template

When a new feature is proposed, use this template before adding to the must-have list:

```
Feature: [name]
Pillar: [1–5 or substrate]
Tier: [Free / Trader / Desk Preview / Desk Full v2]
Lens: [trust / activation / retention / monetization — one or more]
Stage: [MVP / Beta / Scale-A / Scale-B / Later / Never]
Differentiator preserved: [D1 / D2 / D3 / D4 / D5 — which]
Strategic constraint preserved: [list any HARD or OPERATIONAL constraint touched]
Capacity estimate: [founder-weeks; if >2 weeks, requires pre-mortem]
What it displaces: [what current must-have or should-have moves down]
Decision: [add / should-have / later / never]
```

A feature without a documented entry in this template does not enter the priority list. This is the discipline that prevents scope creep from advisor / vendor / cohort suggestions.

---

## 6. Cross-references

- Locked v1 §5: `business-plan/05-product-strategy.md`
- Pillar definitions: `06-product-strategy/core-product-pillars.md`
- Stage definitions: `06-product-strategy/mvp-vs-beta-vs-scale.md`
- Tier matrix: `01-executive-summary/business-model-summary.md` §3
- WTP indicators by segment: `04-icp-and-segmentation/pains-triggers-wtp.md` §4
- JTBD emphasis matrix: `04-icp-and-segmentation/jobs-to-be-done.md` §6
- Differentiation framework: `05-positioning/differentiation-framework.md`
- Strategic priorities: `01-executive-summary/strategic-priorities.md`
- Strategic constraints: `02-company-overview/strategic-constraints.md`
- KPI / OKR: `business-plan/13-kpi-okr.md`
- Engine API reference: `coinscopeai-engine-api` skill
- Trading rules: `coinscopeai-trading-rules` skill

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
