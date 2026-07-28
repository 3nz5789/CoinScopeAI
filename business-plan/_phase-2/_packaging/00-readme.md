# PACKAGING — Workstream Index

**Phase:** 2 — Monetization
**Status:** All five NOW deliverables drafted at v0.1. Workstream-NOW complete pending decisions Pk-1 through Pk-6 and Phase 1 PRODUCT lock for REQUIRED INPUT items.
**Closed:** 2026-05-04

---

## Files

| # | File | Type | Status | Feeds decision |
|---|---|---|---|---|
| 0 | `00-readme.md` | Index | DONE | — |
| 1 | `01-tier-structure-recommendation.md` | DOC NOW | DRAFT v0.1 | **Pk-1** |
| 2 | `02-free-vs-paid-boundary.md` | DOC NOW | DRAFT v0.1 | **Pk-2** |
| 3 | `03-plan-comparison-table-v1.md` | DOC NOW | DRAFT v0.1 | **Pk-5** |
| 4 | `04-premium-feature-gating-rules.md` | DOC NOW | DRAFT v0.1 | **Pk-4** |
| 5 | `05-packaging-friction-review.md` | RESEARCH NOW | DRAFT v0.1 | (informs Pk-2, Pk-4, Pk-6) |

---

## NEXT (queued, not started)

- `[DOC] PACKAGING — Beta Access Offer Design` → **Pk-6** · depends on P0 cohort exit memo
- `[DOC] PACKAGING — Fund/Desk Plan Concept` · concept-only, Phase 5 input
- `[DOC] PACKAGING — Usage Add-On Concepts` · concept-only
- `[QA] PACKAGING — Billing-to-Entitlement Logic Review` · depends on entitlement matrix YAML
- `[DOC] PACKAGING — Upgrade Path Design` · depends on Stripe billing flows confirm

## LATER (queued, not started)

- `[DOC] PACKAGING — High-Touch White-Glove Onboarding Offer` · Phase 5 input, concept-only
- `[DOC] PACKAGING — API/Data Product Packaging Concept` · Phase 3 input, concept-only

---

## Decisions surfaced (consolidated)

These ride into the Phase 2 decision register (`_phase-2/08-decision-register.md` when written):

| ID | Decision | Recommendation | Locks at |
|---|---|---|---|
| **Pk-1** | Tier structure ratify or revise Track B | **Ratify** Track B (4 tiers + 2 per-seat add-on) | After P0 cohort exit memo |
| **Pk-2** | Free vs Paid boundary final form | **Scope B as-locked** (§6.5); 2 post-validation candidates queued | Before pricing-page lock |
| **Pk-3** | Per-seat $149 / $249 split | **Ratify** $149 partner read-only / $249 analyst | Phase 2 Q3 |
| **Pk-4** | Gating type default | **Soft + degraded preferred over hard** (hard reserved for execution-adjacent + 5 "no exceptions") | Before gating rules ship |
| **Pk-5** | Plan comparison table form | **4-tier horizontal grid + per-seat sub-section** (mobile: stacked) | Before pricing-page v1 |
| **Pk-6** | Beta-access offer form | TBD — depends on P0 cohort exit memo | Before P0 → P1 transition |

---

## Open questions surfaced (consolidated)

These ride into Phase 2 open questions (`_phase-2/09-open-questions.md` when written):

1. **PkQ-1** — Does the §6.5 Free Scope B drive Free → Trader conversion ≥ 5% over 90 days? (P0 cohort exit memo answers; if no, Pk-2 reopens.)
2. **PkQ-2** — Does per-seat density on Desk Full v2 hit ≥ 1.5 average? (Phase 2 monitoring; if no, Pk-3 reopens.)
3. **PkQ-3** — Daily vs weekly email digest cadence on Free — what's the engagement delta? (REQUIRED INPUT; influences Pk-2.)
4. **PkQ-4** — Does Stripe Atlas account configuration support 7-day-prior monthly + 30-day-prior annual pre-renewal notification natively? (REQUIRED INPUT; if no, build in app.)
5. **PkQ-5** — Self-serve seat-removal UI exists in current DF flow? (REQUIRED INPUT — Eng confirm; if no, queue `[BUILD] PACKAGING — Self-serve Seat Management UI`.)
6. **PkQ-6** — Phase 1 PRODUCT MVP/Beta/Scale Feature Matrix completion date — affects all five NOW drafts marked REQUIRED INPUT.

---

## REQUIRED INPUT items (consolidated)

Pending Phase 1 PRODUCT lock or Eng confirmation. Drafts proceed; lock waits.

| Item | Source | Affects |
|---|---|---|
| Multi-timeframe confirmation as feature row | Phase 1 PRODUCT MVP/Beta/Scale Feature Matrix | `02-free-vs-paid-boundary.md` row A |
| Cohort comparison feature scope | Phase 1 PRODUCT matrix | `02-free-vs-paid-boundary.md` row C, `03-plan-comparison-table-v1.md` |
| Backtest sandbox feature scope | Phase 1 PRODUCT matrix | `02-free-vs-paid-boundary.md` row E, `04-premium-feature-gating-rules.md` row E |
| Trader API rate-limit exact number | Phase 1 PRODUCT matrix; §5 v1 spec | `03-plan-comparison-table-v1.md` row E |
| Tier-matrix YAML (`_data/entitlements/tier-matrix.yaml`) | Eng | `04-premium-feature-gating-rules.md` §6 |
| Inline-prompt visual treatment | Design | `04-premium-feature-gating-rules.md` §3 |
| Stripe pre-renewal notification config | Eng / Stripe | `05-packaging-friction-review.md` §2 Class B |
| Region-block (US) at signup behavior | Eng | `05-packaging-friction-review.md` §2 Class C |
| Self-serve seat management UI | Eng | `05-packaging-friction-review.md` §6 |

---

## Anti-overclaim audit roll-up

Every NOW draft was authored against the §6.10 anti-overclaim flags. Consolidated audit pass:

- **Flag 1 (founder-cohort drift to "lifetime"):** clean. "Locked through your first renewal cycle, then standard pricing applies" is the canonical phrasing across all five drafts.
- **Flag 2 (Trader "stabilizing in cohort" must be visible):** clean. Surfaced on tier card in `03-plan-comparison-table-v1.md`; surfaced as feature-status row in `02-free-vs-paid-boundary.md`.
- **Flag 3 (AED display vs local-entity implication):** clean. Footer in `03-plan-comparison-table-v1.md` reproduces the §6.10 mitigation language verbatim.

No new overclaim risks introduced by these drafts. Per Phase 2 charter §10 — anti-overclaim audit clean across every monetization surface is a Phase 2 → Phase 3 handoff requirement; PACKAGING contributes a clean baseline.

---

## Linkage to Phase 2 charter exit criteria

Phase 2 charter §4 requires (PACKAGING row):

> **PACKAGING** — Tier structure final; Free vs Paid Feature Boundary locked; Plan Comparison Table v1 signed; Premium Feature Gating Rules with per-feature gating type (hard / soft / degraded / read-only). Documented in `_phase-2/01-packaging.md`.

Status against exit criteria:

- ✓ Tier structure recommendation drafted; lock pending Pk-1 (P0 cohort exit memo).
- ✓ Free vs Paid boundary drafted; lock pending Pk-2 + Phase 1 PRODUCT matrix.
- ✓ Plan comparison table v1 drafted; lock pending Pk-5 + BRAND copy structure.
- ✓ Gating rules drafted with per-feature type assignment; lock pending Pk-4 + entitlement YAML.
- ✓ Friction review drafted (additional NOW deliverable).

PACKAGING workstream NOW work is **draft-complete**. Lock requires the six **Pk-*** decisions and the eight REQUIRED INPUT items above.
