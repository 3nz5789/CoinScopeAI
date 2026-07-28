# Wave 1 — Closeout

**Status:** CLOSED · 2026-05-07
**Scope:** Folders `01-executive-summary/` through `06-product-strategy/`
**Owner:** Founder (Mohammed)
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## 1. What Wave 1 produced

Six folders, 27 files. Each folder is operator-grade scaffolding sitting alongside (not duplicating) the locked v1 framework files in `business-plan/`.

| Folder | Files | Lock state |
|---|---|---|
| `01-executive-summary/` | README · executive-summary-v1 · strategic-priorities · business-model-summary | v1 |
| `02-company-overview/` | README · company-overview · current-state-assessment · strategic-constraints | v1 |
| `03-market-thesis/` | README · market-thesis · why-now · market-risks | v1 |
| `04-icp-and-segmentation/` | README · primary-icp · secondary-icps · jobs-to-be-done · pains-triggers-wtp | v1 |
| `05-positioning/` | README · positioning-statement · category-decision · differentiation-framework · messaging-hierarchy | v1 |
| `06-product-strategy/` | README · product-strategy · core-product-pillars · mvp-vs-beta-vs-scale · feature-prioritization | v1 |

Total: **27 markdown files**, all operator-grade, all anti-overclaim-clean, all cross-referenced, all consistent with locked v1 framework artifacts.

---

## 2. Cross-document consistency state

The following are referenced identically across all six folders. Drift in any one location is a guardrail violation:

- **Vision A** (capital preservation, by default) + **Mission 1** (operational discipline software) — locked 2026-04-22
- **Personas** P1 Omar / P2 Karim / P3 Layla — internal names only; never used externally
- **Anti-personas** filtered at signup: US-resident retail · sub-$5k accounts · copy-traders/signal-buyers · fund LPs · custody-seekers · autonomy-seekers
- **Tier matrix** Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + per-seat ($149 or $249)
- **Risk numbers** 10% drawdown · 5% daily loss · 10x leverage · 5 max open positions · 80% heat (PCC v2 §8, locked 2026-05-01)
- **Phase map** P0 May 2026 (validation, cap 40) → P1 Jun–Jul 2026 (soft launch) → P2 Aug–Sep 2026 (vendor expansion + public launch) → P5 Mar–May 2027 (Desk Full v2 GA)
- **Posture** testnet-only · 30-day validation phase · no real capital · US blocked at signup · UAE/MENA + global EN
- **Anti-overclaim** discipline; locked phrasing list maintained
- **Five differentiators** D1 gate-before-arming · D2 regime-named · D3 custody-free · D4 anti-overclaim · D5 UAE-built

No drift detected at close.

---

## 3. Locks committed in Wave 1

Wave 1 commits four operator-grade locks that downstream Wave 2 folders inherit:

### Lock 1 — Primary ICP

**P1 Omar — Self-Taught Methodist** is the recommended primary ICP for P0 validation through P1 close. Source: `04-icp-and-segmentation/primary-icp.md`. Pending §3.7 interview reconfirmation.

### Lock 2 — Category framing

**Trader operating system (Option C) as primary frame; Institutional-grade signal/risk platform (Option D) as secondary anchor for Desk Preview and Desk Full v2 surfaces only.** Options A (AI trading intelligence platform) and B (automated crypto futures system) explicitly rejected. Source: `05-positioning/category-decision.md`. Carry to decision log as v1 LOCKED before P1 launch.

### Lock 3 — Five product pillars

**(1) Market Intelligence / Scanning · (2) AI-Assisted Signal Context · (3) Risk-Aware Decision Support · (4) Execution Discipline / Workflow · (5) Journaling / Performance Feedback.** Five is the maximum; adding a sixth requires pre-mortem and decision-log entry. Source: `06-product-strategy/core-product-pillars.md`.

### Lock 4 — Stage definitions

**MVP = Trader-tier surface on Binance Testnet, gated against PCC v2 §8 · Beta = 40-user P1 cohort, Desk Preview to quality bar by P1 close · Scale-A = P2 public launch + Bybit · Scale-B = P5 Desk Full v2 GA.** Stage transitions are gated, not calendar-driven. Source: `06-product-strategy/mvp-vs-beta-vs-scale.md`.

---

## 4. Open questions register (consolidated)

The full open-question register from Wave 1, ranked by leverage and dependency. Each item is tagged `DECISION NEEDED`, `REQUIRED INPUT`, or `ASSUMPTION`. The register below is the working list for Wave 2 entry.

### Tier 1 — Block Wave 2 entry

| # | Question | Source | Type | Owner | Window |
|---|---|---|---|---|---|
| W1-Q1 | Ratify category lock (C-primary + D-anchor) in decision log | `05/README.md` Q1 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q2 | Annual prepay discount rate (15–20% range typical for primary ICP) | `01/business-model-summary.md` BMA4; `04/pains-triggers-wtp.md` §4 | DECISION NEEDED | Founder | Before P1 billing live |
| W1-Q3 | Trial mechanics — Free-tier-as-trial vs. time-bounded trial | `04/pains-triggers-wtp.md`; `02/strategic-constraints.md` B4 | DECISION NEEDED | Founder | Before P1 billing live |
| W1-Q4 | Per-seat tier anchor — $149 vs $249 at Desk Full v2 | `06/README.md` Q3 | DECISION NEEDED | Founder | Before P5 charter (Desk Full v2 GA) |
| W1-Q5 | Free-tier scope — risk-gate output included? Working recommendation: scanner + regime sample only; no gate output | `06/README.md` Q4 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q6 | Numerical thresholds for invalidation signals I4–I6 (cohort retention, churn, Desk Preview signup) | `03/market-risks.md` §9 | DECISION NEEDED | Founder | Before P1 mid-cohort review (carry to `13-kpi-okr.md`) |

### Tier 2 — Block downstream Wave 2 folders

| # | Question | Source | Type | Owner | Window |
|---|---|---|---|---|---|
| W1-Q7 | Force 1 confirmation threshold — declare confirmed at what unprompted-mention rate in §3.7? Locked v1 suggests ~30% | `03/README.md` Q3 | DECISION NEEDED | Founder | Before P1 mid-cohort review |
| W1-Q8 | P3 Layla promotion to co-primary if P1 cohort produces strong Layla signal in first 20 paid users | `04/README.md` Q3 | DECISION NEEDED | Founder | At P1 mid-cohort review |
| W1-Q9 | Prop-firm-funded traders — elevate from served-not-led? | `04/README.md` Q5 | DECISION NEEDED | Founder | By end of P1 |
| W1-Q10 | Desk Preview "advanced gates" — ship at P1 close or split P1/P2? | `06/README.md` Q1 | DECISION NEEDED | Founder | Before P1 close |
| W1-Q11 | Bybit at P2 — read-only scan first, or full feature parity? Working recommendation: phased | `06/README.md` Q5 | DECISION NEEDED | Founder | At P2 charter |
| W1-Q12 | Audit log on threshold changes — first-class at Desk Preview or Desk Full v2 only? Working recommendation: Desk Preview | `06/README.md` Q7 | DECISION NEEDED | Founder | Before P1 close |
| W1-Q13 | Single approved one-liner across product / brand / fundraising / recruiting — ratify which form for which surface | `02/README.md` Q1 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q14 | Validation-disclaimer prominence on website (working recommendation: hero footer + about + dedicated PCC page; never below-the-fold) | `05/README.md` Q3 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q27 | Voice taxonomy ratification — four-tier system (product locked / brand working / founder-voice working / social locked) needs ratification or collapse to two-tier (product / social) | `05/messaging-hierarchy.md` §0 | DECISION NEEDED | Founder | At Wave 2 brand pass (`09-brand-messaging.md`) |
| W1-Q28 | "Live demo of refused trade" homepage CTA — verify ship status of the linked surface before homepage publication | `05/messaging-hierarchy.md` §6 hero CTA | REQUIRED INPUT | Founder | Before P1 launch |

### Tier 3 — Lower-leverage, can carry into Wave 2

| # | Question | Source | Type | Owner | Window |
|---|---|---|---|---|---|
| W1-Q15 | Single canonical narrative — merge `01-executive-summary.md` (locked) with `01-executive-summary/executive-summary-v1.md` or keep companion model? | `01/README.md` Q1 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q16 | Cadence for re-running `current-state-assessment.md` — fixed (each phase end) or material-change-driven? | `02/README.md` Q2 | DECISION NEEDED | Founder | At Wave 2 entry |
| W1-Q17 | Constraints to promote from policy-level to code-level enforced (US block, no-withdrawal-scope, etc.) | `02/README.md` Q3 | REQUIRED INPUT | Founder + test-lab | Before P1 close |
| W1-Q18 | Need for non-engineering hire (GTM / content / ops) before P2? | `01/strategic-priorities.md` P6 | DECISION NEEDED | Founder | At P1 mid-cohort |
| W1-Q19 | Post-validation entity posture — DMCC FZE / mainland LLC / other? | `01/strategic-priorities.md` P6 | DECISION NEEDED | Founder + counsel | Before structured raise |
| W1-Q20 | Read API on Desk Preview sufficient, or P2 Karim needs write API at any tier? Working recommendation: read-only through P2; write API not on roadmap pre-P5 | `06/README.md` Q2 | DECISION NEEDED | Founder | At P2 charter |
| W1-Q21 | Native mobile app — durable defer (post-P5 only on cohort demand) | `06/README.md` Q6 | DECISION NEEDED | Founder | Durable |
| W1-Q22 | Localization (Arabic / multi-language UI) before P1 / P2? Working recommendation: post-P5 | `05/README.md` Q7 | DECISION NEEDED | Founder | At P5 charter |
| W1-Q23 | TAM/SAM/SOM — qualitative-only sustainable through fundraise, or sized at structured raise? | `03/README.md` Q6 | ASSUMPTION | Founder + advisors | At fundraise prep |
| W1-Q24 | Positioning artifact (manifesto post / "why we exist" essay) before P1 launch? | `05/README.md` Q5 | DECISION NEEDED | Founder | Before P1 launch |
| W1-Q25 | "Scoopy" appearance in public positioning — product-tier-only or external? | `05/README.md` Q6 | REQUIRED INPUT | Founder | At Wave 2 brand pass |
| W1-Q26 | Decision log openness on coinscope.ai (post-validation public link) | `05/messaging-hierarchy.md` §3 | DECISION NEEDED | Founder | Post-validation |

The Tier 1 list is what Wave 2 entry depends on; the rest can carry. **Strongly recommend** addressing Tier 1 before opening Wave 2 folder `07-packaging-pricing/` because four of the six Tier 1 items are direct inputs to packaging and pricing decisions.

---

## 5. Drift watch list

Items to monitor for drift between Wave 1 close and Wave 2 entry. The brand-voice enforcement skill, drift detector, and CLAUDE.md tripwire should catch these, but worth restating for the founder's own discipline:

- **Locked phrasing list** in `05-positioning/messaging-hierarchy.md` §5 — additions of disallowed phrasing across any surface (website, sales, content, social, in-product) are violations
- **The 5 risk numbers** (10% / 5% / 10x / 5 / 80%) — any drift at any location requires `risk-pcc-pre-flight` skill + simultaneous patch of CLAUDE.md, docs/, .env*, master prompt paste
- **Anti-personas** filtered at signup — any softening (e.g., quietly accepting US signups, sub-$5k accounts) breaks the cohort discipline
- **The 3 strategic invariants** in `06-product-strategy/product-strategy.md` §9 — capital stays in user account; user authorization required; real capital gated until §8 — any violation is treated as critical
- **Brand-voice tier separation** — product-tier in product, social-tier on social only; Scoopy speaks in product-tier only. Working four-tier extension (product / brand / founder-voice / social) declared in `05-positioning/messaging-hierarchy.md` §0; ratification pending (W1-Q27).
- **The 15 "Never (P0–P5 horizon)" features** in `06-product-strategy/feature-prioritization.md` §2 — any of them creeping back onto the roadmap requires explicit decision-log entry
- **Working category recommendation** (C-primary + D-anchor) — until ratified in decision log per W1-Q1, treat as recommendation; do not yet treat as locked-and-public

---

## 6. Wave 2 entry checklist

Before opening Wave 2 folder `07-packaging-pricing/`, the founder should:

1. **Resolve Tier 1 open questions** (W1-Q1 through W1-Q6) — at minimum, draft positions even if not fully decided
2. **Run brand-voice enforcement audit** across all 27 Wave 1 files (catch any inadvertent disallowed phrasing)
3. **File the category-lock decision-log entry** ratifying C-primary + D-anchor (W1-Q1)
4. **Confirm §3.7 interview cohort plan** is on track for P1 mid-cohort review (P1 Omar reconfirmation, fourth-archetype test)
5. **Run `consolidate-memory` skill** to merge any Wave 1 learnings into MEMORY.md
6. **Snapshot the locked-numbers state** (10% / 5% / 10x / 5 / 80%) and confirm CI re-verification of testnet hard-gate is clean
7. **Confirm `coinscope-connector-health` artifact** is green and brand-voice / drift-detector guardrails are running

---

## 7. Wave 2 sequence (recommended)

Inheritance and dependency order:

| Wave 2 folder | Inherits from | Highest-leverage open questions resolved |
|---|---|---|
| `07-packaging-pricing/` | `01` (tier matrix) + `04` (WTP) + `06` (feature classification) | W1-Q2, W1-Q3, W1-Q4, W1-Q5 |
| `08-gtm-strategy/` | `04` (channels) + `05` (positioning) + `07` (packaging) | (downstream of W1-Q2/Q3) |
| `09-sales-strategy/` | `08` | — |
| `10-partnerships/` | `02` (provider constraints) + `09` | — |
| `11-brand-content/` | `05` (messaging hierarchy) + `09` | W1-Q24, W1-Q25 |
| `12-onboarding-activation/` | `04` + `05` + `06` | W1-Q5, W1-Q14 |
| `13-support-trust-ops/` | `02` (constraints) + `06` (operational maturity) | W1-Q17 |
| `14-risk-compliance-safeguards/` | `02` + `06` | W1-Q19 |
| `15-revenue-finance/` | `01` (BMA1–BMA10) + `07` | W1-Q23 |
| `16-kpi-okrs/` | `03` (invalidation signals) + `06` (cohort observation) | W1-Q6, W1-Q7 |
| `17-team-operating-model/` | `01` (priorities) + `06` (capacity) | W1-Q18 |
| `18-roadmap/` | `06` (mvp-vs-beta-vs-scale) + `16` | W1-Q10, W1-Q11, W1-Q20, W1-Q21 |
| `19-fundraising/` | `01` + `15` | W1-Q19, W1-Q23 |
| `20-scenarios/` | `03` (forces, kill triggers) + `15` | — |
| `21-decision-log/` | All — formal decision register | All Tier 1, Tier 2 |
| `99-task-backlog/` | All — Claude Co-Work-ready backlog | All |

**Highest-leverage Wave 2 starting point:** `07-packaging-pricing/`. Resolves four Tier 1 open questions; unblocks Wave 2 cleanly; feeds locked v1 §6 pricing canonical.

---

## 8. Top 10 priorities (re-stated from `01-executive-summary/strategic-priorities.md`)

For the founder's own ongoing reference. None of these changed during Wave 1.

1. Pass P0 validation against PCC v2 §8 Capital Cap criteria
2. Open P1 soft launch on 2026-06-01 with the 40-user cohort
3. Hold the line on anti-overclaim across product, brand, and external claims
4. Run §3.7 interviews to confirm or revise locked personas before P1 mid-cohort
5. Lock vendor failure-mode runbooks before P2 expansion
6. Decide post-validation legal-entity posture before structured raise
7. Stand up support and incident operations sufficient for 40 paid users
8. Maintain testnet-only discipline with zero real-capital deployment until §8 passes
9. Ship Desk Preview ($399) value-delivery surface at quality bar before P1 close
10. Write the post-validation fundraising narrative against actual cohort data, not projections

---

## 9. Biggest strategic mistakes to avoid (from Wave 1 work)

1. **Calling the product "production-ready" before PCC v2 §8 passes.** Single-incident kill of trust premium.
2. **Letting the 40-user P1 cohort cap slip to chase growth.** Support load + cohort signal both degrade.
3. **Adding a sixth pillar.** The five-pillar discipline is what makes the surface focused; expansion dilutes it.
4. **Letting "AI" become a hero hook.** Degraded keyword in primary ICP; pulls toward rejected category Option A.
5. **Selling Desk Preview to P3 Layla before its quality bar is met.** Showing the partial surface to the most demanding audience accelerates churn.
6. **Activating paid acquisition before Trader CAC validates.** Burns capital on unvalidated CAC.
7. **Opening US signups before US licensure path is decided.** Regulatory exposure with no upside.
8. **Promoting "institutional-grade" usage outside Desk Preview / Desk Full v2 surfaces.** Reserved phrasing erodes when overused.
9. **Treating constraints as suggestions.** The 7 constraint categories in `02-company-overview/strategic-constraints.md` are binding.
10. **Re-litigating Wave 1 locks without running pre-mortem first.** Drift, not progress.

---

## 10. The minimum viable business plan for aggressive launch

Distilled from Wave 1 — what *must* be true on the day P1 opens (2026-06-01):

- PCC v2 G1–G4 + §8 passed; Validation_Phase_Exit_Memo filed
- Code-level testnet hard-gate verified in CI on the release that ships
- Brand-voice audit pass on website, about page, pricing page, onboarding, in-product copy
- Tier matrix wired in Stripe with founder-cohort terms documented
- Free tier scoped: scanner + regime sample only (W1-Q5 ratified)
- Annual prepay rate decided (W1-Q2 ratified) and trial mechanics decided (W1-Q3 ratified)
- Category lock ratified in decision log: C-primary + D-anchor (W1-Q1 ratified)
- Single approved one-liner per surface (W1-Q13 ratified)
- §3.7 interview plan ready and 1–2 interviews already in flight
- Support inbox + SLA framework v1 in production
- Incident playbook v1 + first dry-run executed
- Validation-disclaimer prominence decided and shipped (W1-Q14 ratified)
- Cohort observation cadence active

If any of these is not true on launch day, P1 should slip to the next clean window.

---

## 11. Wave 1 — closeout signoff

Wave 1 is **CLOSED**. All six folders complete. All cross-document consistency commitments held. No drift detected at close. 28 open questions logged for Wave 2 entry, of which 6 are Tier 1 (block Wave 2) and 10 are Tier 2 (block downstream Wave 2 folders). W1-Q27 and W1-Q28 added 2026-05-07 from Wave 1 file-review pass.

Next session entry point: address Tier 1 open questions (W1-Q1 through W1-Q6), then open Wave 2 with `07-packaging-pricing/`.

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
