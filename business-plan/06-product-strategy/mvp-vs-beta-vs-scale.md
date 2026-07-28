# MVP vs. Beta vs. Scale

**Status:** Wave 1 · v1 · 2026-05-07 · stage labels (MVP / Beta / Scale-A / Scale-B) are this file's working framing pending v1 framework reconciliation; phase map (P0 / P1 / P2 / P5) is locked
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file maps the product's evolution across three stages — **MVP**, **Beta**, **Scale** — onto the locked phase plan (P0 → P1 → P2 → P5). Each stage has an explicit definition, an in/out feature scope, a readiness gate to the next stage, and a stated business implication if expansion happens prematurely.

The discipline: **stage transitions are gated, not calendar-driven.** A passing date is not a passing gate. If the gate is not met, the stage extends; the plan slips before the discipline cracks.

---

## 1. Stage map at a glance

| Stage | Window (locked phase map) | What it produces | Gate to next stage |
|---|---|---|---|
| **MVP** | P0 — May 2026 (validation phase, ends late May) + ramp into P1 launch | Validation-grade evidence for the Trader-tier surface against PCC v2 §8 | PCC v2 G1–G4 + §8 pass; Validation_Phase_Exit_Memo filed |
| **Beta** | P1 — Jun–Jul 2026 (soft launch, 40-user cohort) into early P2 | Cohort-grade evidence on Trader; Desk Preview reaches quality bar by P1 close | P1 cohort exit criteria + Desk Preview quality bar; vendor failure-mode runbooks dry-run |
| **Scale** | P2 — Aug–Sep 2026 (public launch, vendor expansion) → P5 — Mar–May 2027 (Desk Full v2 GA) and beyond | Public launch operationally durable; Desk Preview at scale; Desk Full v2 launches at P5 | Desk Full v2 cohort signal; per-seat scaling validated |

The stages are **not** equal-length. MVP is short and validation-grade. Beta is a focused cohort-observation window. Scale is a long arc with two sub-stages (public launch through P2; Desk Full v2 GA at P5).

---

## 2. MVP product definition

### 2.1 What "MVP" means at CoinScopeAI

MVP at CoinScopeAI is **not** "minimum viable product in market." It is **minimum viable product for validation evidence**. Concretely, MVP is the Trader-tier surface running on Binance Testnet, instrumented for cohort observation, gated against real capital, sufficient to produce validation-grade evidence against PCC v2 §8 Capital Cap criteria.

> **MVP definition (Wave 1 v1 working):** The Trader-tier surface on Binance USDT-M Testnet, with the five core pillars functional at validation quality, the testnet hard-gate code-level enforced, the locked thresholds (10% / 5% / 10x / 5 / 80%) wired, the canonical alert payload shipping, and the journal capturing per-trade rule-respect and R-multiple data — sufficient to produce evidence against PCC v2 G1–G4 + §8 Capital Cap.

### 2.2 What MVP includes

Pillar coverage at MVP (P0 through ramp into P1 launch):

| Pillar | MVP scope |
|---|---|
| 1. Market Intelligence / Scanning | Multi-pair scanner across Binance USDT-M; confluence ranking; documented inputs |
| 2. AI-Assisted Signal Context | v3 ML regime classifier; confidence; regime page |
| 3. Risk-Aware Decision Support | Pre-arming gate (5 locked thresholds); position sizer with math transparency; configurable thresholds |
| 4. Execution Discipline / Workflow | Single-account workflow end-to-end; canonical Telegram + dashboard payload |
| 5. Journaling / Performance Feedback | Journal capture; R-multiple + rule-violation tagging; basic performance reporting |

Plus operating substrate:

- Auth, onboarding, exchange-connection (Binance Testnet only)
- Stripe billing wired against the locked tier matrix (cohort pricing applied per cohort document)
- Code-level testnet hard-gate (CI re-verified on every release)
- Documentation + decision log + PCC v2 published
- Brand-voice enforcement skill in production
- Support inbox + SLA framework v1 in production (already locked)
- Founder-led distribution active in methodology channels (discovery during MVP; scaled in Beta)

### 2.3 What MVP does NOT include

- Real-capital deployment (gated against)
- Bybit or any second venue (P2)
- Desk Preview multi-account view, advanced gates, read API (P1 close target)
- Desk Full v2 (P5)
- Mobile app
- Multi-language UI
- Public launch
- Paid acquisition
- Custody, autonomy, signal-as-deliverable, copy-trading
- Public benchmarks / leaderboards

### 2.4 MVP readiness gate (to Beta)

The gate is PCC v2 G1–G4 + **§8 Capital Cap & Phased Ramp** criteria pass. The gate is documented; the criteria are public; the gate is binary on G1–G4 and graduated on §8 Phased Ramp. If any one of G1–G4 or the §8 Capital Cap criteria fails, MVP extends.

**Real-capital authorization at Beta entry:** PCC v2 §8 specifies a Capital Cap **and Phased Ramp** — a graded authorization framework, not a binary on/off. After the MVP gate passes, real-capital deployment in Beta proceeds under the §8 Phased Ramp schedule (per-cohort and/or per-account caps documented in PCC v2). The code-level testnet hard-gate is replaced by operational gates running against the locked thresholds (10% / 5% / 10x / 5 / 80%) plus the Phased Ramp limits — not by an absence of safeguards. Verify this framework in `_data/operations/Production_Candidate_Criteria_v2.md` §8 before MVP→Beta transition.

Carry to `_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md` for the post-pass filing.

### 2.5 Business implication if MVP expansion is premature

If MVP is declared passed without §8 truly passing, or if Bybit / multi-account / Desk Preview features are added before §8 passes:

- Anti-overclaim posture cracks (the production-ready claim arrives unearned)
- Trust premium erodes for the disciplined-survivor cohort
- Cohort signal becomes muddy (the cohort isn't observing the validated surface)
- Real-capital incidents become possible before the testnet hard-gate is fully verified
- Any subsequent fundraise loses its single most valuable artifact (clean cohort data against documented criteria)

The cost of premature MVP expansion is **fatal**, not recoverable. This is why the MVP gate is hard.

---

## 3. Beta product definition

### 3.1 What "Beta" means at CoinScopeAI

Beta at CoinScopeAI is **the soft-launch cohort window** — the first paid users at founder-cohort terms, Trader-tier as primary surface, Desk Preview ramping to quality bar by stage close. The cohort observes the product under real-but-limited conditions; the company observes the cohort.

> **Beta definition (Wave 1 v1 working):** The 40-user P1 cohort (opened 2026-06-01), running Trader-tier and (incrementally) Desk Preview surfaces under PCC v2 §8 Capital Cap & Phased Ramp authorization, observed against `13-kpi-okr.md` cohort exit criteria, with vendor failure-mode runbooks dry-run before Beta close.

### 3.2 What Beta includes (additive to MVP)

| Pillar | Beta-stage additions |
|---|---|
| 1. Market Intelligence / Scanning | Cohort-load stability; configurable filtering; Desk Preview multi-account scanning by stage close |
| 2. AI-Assisted Signal Context | Calibration verification under cohort load; cross-pair regime context |
| 3. Risk-Aware Decision Support | Advanced gate configurability at Desk Preview (per-account overrides, combination gates, audit log on threshold changes) |
| 4. Execution Discipline / Workflow | Multi-account workflow at Desk Preview; read API documented and shipping at Desk Preview; canonical payload stable |
| 5. Journaling / Performance Feedback | Multi-account performance attribution at Desk Preview; performance-by-regime breakdowns |

Plus operating maturity (Beta-stage scaling of items already running in MVP substrate):

- Incident playbook + first dry-run executed
- Vendor failure-mode runbooks extended and dry-run before P2
- Cohort observation cadence active; weekly cohort review
- §3.7 persona interviews completed; persona reconfirmation or revision filed
- Founder-led distribution scaled in methodology channels
- Real-capital deployment under PCC v2 §8 Capital Cap & Phased Ramp (replaces testnet hard-gate post-MVP pass)

### 3.3 What Beta does NOT include

- Real-capital deployment beyond what's authorized post-MVP (TBD per validation pass)
- Public launch (gated by Beta exit criteria)
- Bybit (P2 charter dependent)
- Paid acquisition (deferred until M5+ and only if Trader CAC validates)
- Desk Full v2 features (P5)
- Mobile app
- Multi-language UI
- Affiliate / referral payouts

### 3.4 Beta readiness gate (to Scale)

Three components must pass:

1. **Cohort exit criteria pass** (carried in `13-kpi-okr.md`; specific thresholds **DECISION NEEDED** (W1-Q6) for retention, churn, gate-fire patterns, alert health)
2. **Desk Preview quality bar** at multi-account view + advanced gates + read API
3. **Vendor failure-mode runbooks** dry-run completed and incident playbook v1 in production
4. **Real-capital posture under §8 Phased Ramp documented** — per-cohort / per-account caps and authorization status filed for Scale-A entry

If any one fails, Beta extends. Public launch (P2) does not open until all four pass.

### 3.5 Business implication if Beta expansion is premature

If public launch (P2) opens before Beta exit criteria pass, or if the cohort cap of 40 is exceeded for "growth" reasons:

- Support load spikes; founder is solo on call; quality of incident response degrades
- Cohort signal becomes muddy as the cohort grows beyond the support window
- Brand-voice discipline cracks under launch pressure
- Vendor outage during scale-out produces churn the company can't recover from
- Anti-overclaim posture is tested at exactly the moment we cannot afford it to fail
- The single most valuable post-Beta artifact (clean Beta cohort data) is contaminated

Premature Beta expansion is **highly recoverable** technically (re-throttle, etc.) but **structurally damaging** to trust. The 40-user cap is hard for that reason.

---

## 4. Scale-stage product direction

### 4.1 What "Scale" means at CoinScopeAI

Scale at CoinScopeAI is the long arc from public launch (P2) through Desk Full v2 GA (P5). It has two sub-stages:

| Sub-stage | Window | Focus |
|---|---|---|
| **Scale-A** | P2 (Aug–Sep 2026) → end-2026 | Public launch durability; vendor expansion (Bybit + redundancy); founder-led distribution at scale; post-validation fundraise |
| **Scale-B** | P5 (Mar–May 2027) onward | Desk Full v2 GA; per-seat scaling for solo PMs and small desks; MENA institutional inroads |

> **Scale definition (Wave 1 v1 working):** Public launch durable; Trader, Desk Preview, and (at P5) Desk Full v2 surfaces all in market; vendor stack expanded to include Bybit and redundancy; cohort scaling beyond the 40-user Beta cap under expanded §8 Phased Ramp authorization; per-seat scaling validated against P3 Layla cohort.

### 4.2 What Scale includes (additive to Beta)

| Pillar | Scale-stage additions |
|---|---|
| 1. Market Intelligence / Scanning | Bybit (P2); additional venues optional post-P2; cohort-level analytics |
| 2. AI-Assisted Signal Context | Audit-grade regime history; cross-venue regime context |
| 3. Risk-Aware Decision Support | Per-seat threshold permissions (P5 Desk Full v2); audit-grade rule-change log |
| 4. Execution Discipline / Workflow | Per-seat permissions + partner read-only views (P5 Desk Full v2); Bybit-parity workflow at P2 |
| 5. Journaling / Performance Feedback | Audit-grade journal + partner-readable reports (P5 Desk Full v2) |

Plus operating maturity:

- Public launch operations (signup at scale; support at scale)
- Vendor redundancy in place
- Paid acquisition active (if Trader CAC validates per M5+ trigger)
- Post-validation fundraise narrative refreshed against cohort data
- Entity restructure executed (sole prop → DMCC FZE / mainland LLC / other; **DECISION NEEDED**)
- P4 contractor active around v2 build (highest-risk window)
- Counsel coverage extended for Desk Full v2 launch

### 4.3 What Scale does NOT include (still)

- Custody, autonomy, signal-as-deliverable, copy-trading (never; structural)
- US licensure flow (until US licensure decision)
- Native mobile app (post-P5 at earliest, only if cohort demands)
- Multi-language UI (post-P5)
- Funds >$5M AUM (post-P5; specific decision required)
- Public benchmarks / leaderboards (gated by counsel review even post-validation)

### 4.4 Scale readiness gate (to next stage / to platform durability)

Scale is a long arc, not a discrete stage with a single gate. The implicit gates are:

1. **P2 charter exit:** Bybit stable; vendor redundancy in place; cohort growth healthy; paid-acquisition CAC trigger evaluated
2. **P5 charter entry:** Desk Full v2 quality bar; per-seat scaling validated against intent letters and P3 Layla cohort signal
3. **Post-P5:** Desk Full v2 cohort signal; structural defensibility consolidated (cohort data + brand voice + jurisdictional alignment)

### 4.5 Business implication if Scale expansion is premature

The Scale-stage analog of premature MVP / Beta expansion:

- **Premature P2 vendor expansion** (multiple new venues, multiple new data vendors at once): cost step-up exceeds revenue step-up; gross margin compresses below the ~76% base-case assumption (per locked v1 §15); pricing pressure forces tier restructure
- **Premature paid acquisition** (before Trader CAC validates): burns capital on a CAC the company hasn't validated; pulls cohort signal off-distribution
- **Premature Desk Full v2 launch** (before P5 charter): the surface is incomplete; "institutional-grade" frame breaks on contact
- **Premature US opening** (before licensure decision): regulatory exposure; operating discipline fractures
- **Premature mobile-app investment**: capacity discipline cracks; founder bandwidth diverts from validation-grade scale-out

The pattern across Scale: **premature expansion is recoverable in revenue, but each instance damages anti-overclaim posture and trust premium**, both of which are slow-compounding moats and slow to repair.

---

## 5. What features belong in each stage

A consolidated map. Each entry is a feature; each cell shows which stage adds (or first surfaces) that feature.

| Feature / capability | MVP | Beta | Scale-A | Scale-B (P5) |
|---|---|---|---|---|
| Multi-pair scanner | ✅ | maintained | maintained + Bybit | maintained + cohort analytics |
| Regime classifier (v3 ML) + confidence | ✅ | calibration verification | cross-venue regime | audit-grade regime history |
| Pre-arming risk gate (5 locked thresholds) | ✅ | maintained | maintained | maintained |
| Position sizer with math transparency | ✅ | maintained | maintained | maintained |
| Configurable thresholds at Trader+ | ✅ | maintained | maintained | maintained |
| Single-account journal + R-multiple tagging | ✅ | maintained | maintained | maintained |
| Telegram canonical payload | ✅ | maintained | maintained | maintained |
| Dashboard + Telegram parity | ✅ | maintained | maintained | maintained |
| Stripe billing | ✅ | maintained | maintained | maintained |
| Code-level testnet hard-gate | ✅ | retired (post-§8 pass); operational gates per locked thresholds + §8 Phased Ramp authorization | operational gates active under expanded Phased Ramp | operational gates active |
| PCC v2 publication | ✅ | maintained | maintained | maintained |
| Multi-account view | — | added at Desk Preview | maintained | maintained |
| Advanced gates (per-account overrides, combination, time-of-day) | — | added at Desk Preview | maintained | maintained |
| Read API at Desk Preview | — | added | maintained | maintained |
| Audit log on threshold changes | — | added at Desk Preview | maintained | maintained |
| Multi-account performance attribution | — | added at Desk Preview | maintained | maintained |
| Bybit USDT-perp | — | — | added | maintained |
| Vendor redundancy (data) | — | — | added | maintained |
| Public launch operations | — | — | added | maintained |
| Per-seat permissions | — | — | — | added at Desk Full v2 |
| Partner read-only views | — | — | — | added at Desk Full v2 |
| Audit-grade journal + partner-readable reports | — | — | — | added at Desk Full v2 |
| Cohort-level analytics surface | — | — | added | maintained |

---

## 6. What NOT to include too early

A consolidated "do not yet" feature register, drawn from `01-executive-summary/strategic-priorities.md` §3 and `02-company-overview/strategic-constraints.md` §8. Each is mapped to its earliest revisit window:

| Feature / direction | Disposition | Earliest revisit |
|---|---|---|
| Bybit | Defer until P2 | P2 charter |
| Desk Full v2 surface | Defer until P5 | P5 charter |
| Native mobile app | Durable defer | Post-P5, only on cohort demand |
| Multi-language UI | Durable defer | Post-P5 |
| Public benchmarks / leaderboards | Disallowed pre-validation | Post-validation + counsel review |
| Affiliate / referral payouts | Defer | Post-validation, structured guardrails |
| Write API for programmatic order placement | Durable defer | Post-P5 at earliest |
| Custody, fund formation, autonomous execution | Never | — |
| Copy-trading / leader-follower | Never | — |
| US licensure flow | Defer | Counsel-confirmed US path |
| Paid acquisition | Defer | Trader CAC validates (M5+) |
| Backtest user-defined rules against history | Defer (Pillar 5 future surface) | Post-P5 evaluation |
| White-label / private-label arrangements | Out of scope | — |

The discipline is: **each item above has been reviewed and rejected for the current stage with a documented reason.** Re-litigating without documented reason produces drift.

---

## 7. Stage transition checklist

A consolidated checklist for each transition. Use as a pre-mortem checklist before declaring a stage passed.

### MVP → Beta

- [ ] PCC v2 G1 passed
- [ ] PCC v2 G2 passed
- [ ] PCC v2 G3 passed
- [ ] PCC v2 G4 passed
- [ ] PCC v2 §8 Capital Cap criteria passed
- [ ] Validation_Phase_Exit_Memo filed
- [ ] Code-level testnet hard-gate verified in CI
- [ ] Anti-overclaim audit pass on all surfaces
- [ ] Cohort pricing terms documented
- [ ] §3.7 interview cohort plan ready

### Beta → Scale-A (public launch / P2)

- [ ] P1 cohort exit criteria pass (`13-kpi-okr.md`; thresholds **DECISION NEEDED** (W1-Q6))
- [ ] Desk Preview multi-account view at quality bar
- [ ] Desk Preview advanced gates at quality bar
- [ ] Desk Preview read API documented and shipping
- [ ] Vendor failure-mode runbooks v1 + dry-run executed
- [ ] Incident playbook v1 in production; ≥1 incident dry-run
- [ ] §3.7 interviews complete; persona reconfirmation or revision filed
- [ ] Founder-led distribution active in methodology channels
- [ ] Brand-voice enforcement skill maintained in production
- [ ] Real-capital deployment posture and §8 Phased Ramp authorization status documented
- [ ] Anti-overclaim audit pass

### Scale-A → Scale-B (Desk Full v2 / P5)

- [ ] Bybit integration stable; cohort observation through P2 confirms
- [ ] Vendor redundancy in production
- [ ] Public launch durability evidenced (incident response track record)
- [ ] Paid acquisition decision evaluated (CAC validated or not)
- [ ] Entity restructure executed (sole prop → restructured)
- [ ] Counsel coverage extended for Desk Full v2 framing
- [ ] P3 Layla cohort signal — at least N intent letters or evaluation cohort (`DECISION NEEDED` for explicit number)
- [ ] Per-seat scaling design complete and engineering-validated
- [ ] Anti-overclaim audit pass

---

## 8. Cross-references

- Locked v1 §5: `business-plan/05-product-strategy.md`
- Locked v1 §14 launch roadmap: `business-plan/14-launch-roadmap.md`
- PCC v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Validation Phase Exit Memo template: `business-plan/_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`
- MVP readiness checklist: `business-plan/_data/operations/mvp-readiness-checklist.md`
- Tier matrix: `01-executive-summary/business-model-summary.md` §3
- Phase charters: `business-plan/_phase-1/00-phase-1-charter.md`, `_phase-2/00-phase-2-charter.md`, `_phase-3/00-phase-3-charter.md`
- KPI / OKR (cohort exit criteria): `business-plan/13-kpi-okr.md`
- Strategic priorities: `01-executive-summary/strategic-priorities.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
