# PACKAGING — Canonical Task List (Phase 2 staging)

**Status:** **PATH A ACTIVATED 2026-05-04 — ABSORBED INTO PHASE 2.** Canonical list reproduced verbatim in `_phase-2/01-packaging.md` §8 and operationalized across `_phase-2/_packaging/01..05*.md`. This staging file is retained for audit / activation-history; the live source of truth is `_phase-2/01-packaging.md`. PACKAGING NOW tasks remain dependency-aware of Phase 1 PRODUCT NOW outputs (Product Value Ladder + MVP/Beta/Scale Feature Matrix); drafts call out REQUIRED INPUT items pending PRODUCT lock.
**Source of truth:** user-supplied canonical list 2026-05-04, reproduced verbatim.
**Format:** `[TYPE] [AREA] — Action / Deliverable`. Per-task fields: objective · why it matters · dependency · expected output.

---

## Why this is staged, not absorbed

Phase 1 charter (`_phase-1/00-phase-1-charter.md`) §2 lists "Pricing experiments, packaging A/B tests" as out-of-scope. §8 explicitly defers:

- *"Pricing tiers final form — Track B canonical exists in v1, but the Trader $79 / Desk Preview $399 / Desk Full $1,199 numbers are not Phase-1-decisions. They get tested in Phase 2."*
- *"Per-seat $149 vs $249 split — packaging detail, Phase 2."*

Per the project-instructions 21-section structure, "Packaging and Pricing" is Section 7 and lives natively in **Phase 2 (Market, product, and pricing validation)**. PACKAGING work is also dependency-blocked on locked Phase 1 outputs (Product Value Ladder, MVP/Beta/Scale Feature Matrix, Free-tier limit decision Pr-4) — running it before those inputs land would be premature.

Three paths to activate this list (same shape as the BRAND staging precedent):

1. **Defer to Phase 2** (default, recommended). When Phase 2 charter opens, this file becomes the seed of `_phase-2/01-packaging.md` (or equivalent) and the PACKAGING section of the Phase 2 backlog.
2. **Amend Phase 1 charter to add PACKAGING.** Requires patches in one pass: charter §2/§4/§6/§7/§8, new `_phase-1/08-packaging.md` scaffold (renumbering meta files 08→09 / 09→10 / 10→11 / 11→12), PACKAGING section in `08-task-backlog.md` (now `09-task-backlog.md`) and `09-deliverable-map.md` (now `10-deliverable-map.md`), `Pk-*` IDs in the decision register, PACKAGING questions in open questions. This conflicts with the Phase 1 charter §8 deliberate deferral — would require a defensible reason to override.
3. **Mark MOOT.** Archive the canonical list and stop.

---

## Overlap with already-locked Phase 1 work

Multiple PACKAGING tasks are downstream of (or overlap with) locked Phase 1 PRODUCT and POSITIONING work. Flagging now so dependencies are explicit at activation time:

| PACKAGING task | Phase 1 dependency / overlap | Direction |
|---|---|---|
| `[DOC] PACKAGING — Tier Structure Recommendation` | PRODUCT `Product Value Ladder` (NOW) | Tier structure ratifies or revises the v1 Track B (Free / Trader $79 / Desk Preview $399 / Desk Full $1,199). The value ladder must be locked first. |
| `[DOC] PACKAGING — Free vs Paid Feature Boundary` | PRODUCT `MVP vs Beta vs Scale Feature Matrix` (NOW); Decision Register **Pr-4** (Free-tier limits) | Feature boundary is the *operational* form of Pr-4. The matrix supplies the feature inventory. |
| `[DOC] PACKAGING — Plan Comparison Table v1` | POSITIONING `Surface Variant Table`; BRAND `Website Copy Structure` (NEXT) | Plan comparison is a website surface; copy structure governs how it lands. |
| `[DOC] PACKAGING — Premium Feature Gating Rules` | PRODUCT `Product Scope Guardrails` (NEXT); MVP/Beta/Scale Matrix | Gating rules implement the strategy guardrails at feature granularity. |
| `[QA] PACKAGING — Billing-to-Entitlement Logic Review` | Stripe integration; engine entitlement flags (engineering) | Pure Phase 2+ work; depends on Phase 1 PRODUCT decisions being locked so the audit has a stable spec. |
| `[DOC] PACKAGING — Fund/Desk Plan Concept` | PRODUCT `Team and Fund Product Variant Concept` (LATER); ICP `Layla Phase-5 Pre-read` (LATER) | Phase 5 input — concept only. Cannot be committed in Phase 2. |

Net effect: PACKAGING is **dependency-blocked on Phase 1 PRODUCT outputs**. Even if you Path-B amend the charter, the PACKAGING NOW tasks cannot productively run before PRODUCT NOW tasks complete.

---

## A. PACKAGING — canonical list (verbatim)

### NOW

**`[DOC] PACKAGING — Tier Structure Recommendation`**
- **Objective:** Recommend the tier structure (count, gating, naming) for the P1+ commercial product, anchored to the locked Product Value Ladder. Ratifies or revises v1 Track B (Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199).
- **Why:** Tier count is a high-leverage decision. Too many tiers = analysis paralysis at signup; too few = pricing compression. The recommendation is the input to every other PACKAGING task.
- **Dependency:** Product Value Ladder (PRODUCT NOW); ICP Definitions v1; v1 framework `06-pricing-monetization.md` (Track B canonical).
- **Output:** Tier structure recommendation MD; signed; feeds Decision Register entry Pk-1 (when Phase 2 register opens).

**`[DOC] PACKAGING — Free vs Paid Feature Boundary`**
- **Objective:** Lock the precise boundary between Free and the lowest paid tier (Trader $79). Resolves Phase-1 open question PrQ-1 ("Free demonstrates the gate without substituting for Trader") at the operational level.
- **Why:** Free-tier shape is the funnel valve. Wrong shape kills either acquisition (too tight) or conversion (too generous). Phase 1 Decision Pr-4 is recommended at "top 10 + 15-min delay" — Phase 2 ratifies, revises, or A/B tests.
- **Dependency:** MVP vs Beta vs Scale Feature Matrix (PRODUCT NOW); Product Value Ladder; Phase 1 Decision Register entry Pr-4.
- **Output:** Free vs Paid boundary MD — every feature explicitly tagged Free / Paid / Tier-specific.

**`[DOC] PACKAGING — Plan Comparison Table v1`**
- **Objective:** External-facing plan comparison table for the pricing page (Free / Trader / Desk Preview).
- **Why:** Plan comparison is one of the highest-leverage conversion surfaces. Consistency with the value ladder and feature matrix is non-negotiable; drift here misrepresents the product.
- **Dependency:** Tier Structure Recommendation; Product Value Ladder; Free vs Paid Feature Boundary; POSITIONING Surface Variant Table.
- **Output:** Plan comparison table MD; ready to render on the pricing page; pairs with BRAND `Website Copy Structure` (NEXT).

**`[DOC] PACKAGING — Premium Feature Gating Rules`**
- **Objective:** Define the gating logic for premium features — what triggers an upgrade prompt, what gracefully degrades, what's hard-gated.
- **Why:** Soft vs hard gating is a UX trust signal. Aggressive gating reads as user-hostile (counter-positioning to anti-overclaim brand); soft gating leaves revenue on the table. Each feature needs an explicit gating type.
- **Dependency:** Free vs Paid Feature Boundary; Tier Structure Recommendation; Phase 1 Product Scope Guardrails (PRODUCT NEXT).
- **Output:** Gating rules MD with feature-by-feature gating type (hard / soft / degraded / read-only).

**`[RESEARCH] PACKAGING — Packaging Friction Review`**
- **Objective:** Review existing crypto-trading-tool packaging for the most common friction points (lock-in, surprise charges, feature withholding, downgrade restrictions, opaque billing).
- **Why:** Anti-friction packaging is itself a trust signal in a category that frequently engineers friction. Codifying anti-patterns up-front prevents drift toward category packaging debt.
- **Dependency:** v1 framework `06-pricing-monetization.md`; competitive intelligence pass.
- **Output:** Friction review MD — anti-pattern list + packaging design rules.

### NEXT

**`[DOC] PACKAGING — Beta Access Offer Design`**
- **Objective:** Design the offer for the P0 → P1 transition cohort (e.g., grandfathered Trader pricing, founder-cohort discount, free-extension).
- **Why:** Beta-access offers reward early users without setting bad pricing precedents. Needs explicit design — ad-hoc offers create entitlement disputes later.
- **Dependency:** Tier Structure Recommendation; Cohort exit memo; Phase 2 pricing direction.
- **Output:** Beta access offer MD — terms, eligibility criteria, expiration rules, prorated migration.

**`[DOC] PACKAGING — Fund/Desk Plan Concept`**
- **Objective:** Sketch the Fund / Desk plan concept (Desk Full v2 $1,199 + per-seat at $149 or $249) for Phase 5 ramp.
- **Why:** Concept-only in Phase 2; Phase 5 charter input. Concepts now reduce Phase-5 ramp time and pre-empt premature Desk Full sprawl.
- **Dependency:** Layla Phase-5 Pre-read (ICP LATER); Team and Fund Product Variant Concept (PRODUCT LATER).
- **Output:** Fund/Desk plan concept MD; *no commitments*.

**`[DOC] PACKAGING — Usage Add-On Concepts`**
- **Objective:** Catalogue usage-based add-on candidates (custom thresholds, API access tier, additional venues post-Bybit, extra Telegram routing, per-seat additions).
- **Why:** Usage add-ons let core tiers stay simple while power users pay more. Deciding the *shape* of add-ons in Phase 2 keeps the core tier matrix stable through Phase 3+.
- **Dependency:** Tier Structure Recommendation; Karim API Surface Scoping (deferred PRODUCT LATER).
- **Output:** Add-on concepts MD — each concept's pricing model (flat / metered / overage).

**`[QA] PACKAGING — Billing-to-Entitlement Logic Review`**
- **Objective:** Walk every entitlement (feature flag, tier check, upgrade prompt, downgrade revocation) and verify it correctly reflects the locked tier structure and gating rules.
- **Why:** Entitlement drift is the single most expensive packaging failure mode (revenue loss + support load + trust hit). Audit before any pricing change ships.
- **Dependency:** Premium Feature Gating Rules; Stripe integration; current product feature flags.
- **Output:** Audit report; remediation backlog if any.

**`[DOC] PACKAGING — Upgrade Path Design`**
- **Objective:** Design the in-product upgrade path — when prompts appear, how the upgrade flow works, prorated billing, downgrade rules, refund/credit policy.
- **Why:** Upgrade path UX shapes ARR. Ad-hoc designs leak conversions and create churn surface.
- **Dependency:** Premium Feature Gating Rules; Tier Structure Recommendation; Stripe billing flows.
- **Output:** Upgrade path design MD with flow diagrams + edge-case rules.

### LATER

**`[DOC] PACKAGING — High-Touch White-Glove Onboarding Offer`**
- **Objective:** Sketch a high-touch onboarding offer (e.g., for Desk Full v2 buyers or larger-book traders) — what it includes, what it costs, who delivers it.
- **Why:** Phase 5 input. Small books / funds expect high-touch, but it's a margin trap if mispriced or under-staffed.
- **Dependency:** Fund/Desk Plan Concept; Enterprise Buyer Readiness Notes (ICP LATER).
- **Output:** Concept MD; *no commitments*.

**`[DOC] PACKAGING — API/Data Product Packaging Concept`**
- **Objective:** Concept the API / data product as a separate packaged offering (e.g., Karim P2 API surface; risk-as-a-service).
- **Why:** Phase 3+ input. Bounds future scope discussion without committing. Keeps the core PACKAGING surface clean (API as a *separate* product, not a tier add-on, if that proves correct).
- **Dependency:** Karim API Surface Scoping (deferred); Expansion Opportunities Beyond Core Trading Intelligence (PRODUCT LATER).
- **Output:** Concept MD; *no commitments*.

---

## Activation paths

**Path A — Defer to Phase 2 (default, recommended).**
No further action now. When Phase 2 charter opens, this file becomes the seed of the PACKAGING section of the Phase 2 backlog. The overlap table above guides dependency sequencing against locked Phase 1 PRODUCT outputs.

**Path B — Amend Phase 1 charter to include PACKAGING.**
Requires the following patches in one pass:
1. `_phase-1/00-phase-1-charter.md` — patch §2 in-scope (move "Pricing experiments, packaging A/B tests" from out-of-scope to in-scope), §4 exit criteria (add a PACKAGING row), §6 outputs, §7 crosswalk, §8 deferred decisions (remove pricing/per-seat deferral lines or qualify them).
2. Create `_phase-1/08-packaging.md` scaffold.
3. Renumber meta files: `08-task-backlog.md` → `09-task-backlog.md`, `09-deliverable-map.md` → `10-deliverable-map.md`, `10-decision-register.md` → `11-decision-register.md`, `11-open-questions.md` → `12-open-questions.md`.
4. Add PACKAGING section to the renamed task backlog (verbatim, with four-field annotations).
5. Add PACKAGING rows to the renamed deliverable map.
6. Add PACKAGING decisions (`Pk-*` IDs) to the renamed decision register.
7. Add PACKAGING open questions to the renamed open questions file.

**Important caveat for Path B:** PACKAGING NOW tasks are dependency-blocked on PRODUCT NOW tasks (Product Value Ladder + MVP/Beta/Scale Feature Matrix). Even if Phase 1 includes PACKAGING, work cannot start until PRODUCT scaffolds clear. Path B therefore offers no schedule benefit unless PRODUCT NOW lands faster than expected.

**Path C — Mark MOOT.**
Archive the canonical list and stop.

---

## What I did NOT do

- Did **not** modify any `_phase-1/` file.
- Did **not** add PACKAGING to `_phase-1/08-task-backlog.md` or `_phase-1/09-deliverable-map.md`.
- Did **not** create a `_phase-1/08-packaging.md` scaffold.
- Did **not** renumber Phase 1 meta files.
- Did **not** update Source-of-truth note in `_phase-1/08-task-backlog.md` (still: MARKET, ICP, POSITIONING, BRAND, PRODUCT canonical; TRUST, RISK draft).

Phase 1 boundaries are intact. Awaiting your decision (A / B / C).
