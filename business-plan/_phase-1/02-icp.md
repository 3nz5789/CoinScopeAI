# 02 — ICP (Phase 1)

**Purpose:** Choose **one** primary persona for P1 Narrow Ship. Defer the others with stated reason.
**v1 reference:** `03-icp-segmentation.md`
**Phase 1 outcome:** P1 primary persona named; the other two on a deferred list with a reason and a re-evaluation trigger.

---

## Why ICP matters specifically for CoinScopeAI

The v1 framework already locked three personas (internal names): **P1 Omar — Self-Taught Methodist**, **P2 Karim — Engineer Trader**, **P3 Layla — Solo PM** ($200k–$1M aggregate book). What v1 did *not* lock is which of the three is the **primary execution target for P1 Narrow Ship (Jun–Jul 2026)**.

This matters more for CoinScopeAI than for most startups because:

- The product surface (engine endpoints, dashboard, Telegram bot) is *one* surface — the persona we optimize for sets the default copy, the default dashboard, the default alerts.
- Trust signals scale per-persona. Omar trusts evidence. Karim trusts open code and observability. Layla trusts process and counterparty discipline. Those are *different trust burdens* with different artifact requirements.
- Pricing tolerance differs. Trader $79 lands clean on Omar/Karim; Desk Preview $399 needs Layla-grade narrative. Picking the wrong primary makes the wrong tier the default.
- The cohort cap is **40** for P0 validation. That is a tiny sample. We cannot afford to split it across three personas and learn nothing about any.

---

## Required subsections

1. **Persona one-pagers (3)** — locked from v1, restated for Phase 1 quick reference.
2. **Persona scoring matrix** — five dimensions: trust fit, pricing fit, product fit (P1 surface), reachability, retention plausibility.
3. **Primary persona pick + rationale**.
4. **Deferred persona reasons + re-evaluation trigger**.
5. **First-100-customer thought experiment** — for the chosen primary, what does the first 100 actually look like?

---

## Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Persona scoring matrix | MD table, in this file | Strategy CoS |
| ICP Pick Memo | MD, 1 page | Founder |
| First-100 customer composition sketch | MD, in this file | Founder + Strategy CoS |
| Cohort-recruit checklist (gates a candidate must pass to enter the P0 cohort) | MD, separate file in `_data/operations/` | Founder |

---

## Persona scoring matrix (initial, to be ratified in Phase 1)

Score 1–5 for each dimension. Higher is better fit.

| Dimension | P1 Omar (Self-Taught Methodist) | P2 Karim (Engineer Trader) | P3 Layla (Solo PM) |
|---|---|---|---|
| Trust fit (evidence-led claims) | 5 | 5 | 4 |
| Pricing fit (Trader $79 → Desk Preview $399) | 4 (Trader tier) | 4 (Trader → Preview) | 3 (Preview → Desk Full only) |
| Product fit (current P1 surface: scanner, signals, gate, journal) | 5 | 4 (wants API + raw data) | 3 (wants reporting + audit log) |
| Reachability (founder-led distribution feasible) | 4 (forums, niche communities) | 3 (needs technical content) | 2 (relationship-led, slow) |
| Retention plausibility on a 30-day validation product | 5 | 4 | 2 (will not commit before live track record) |
| **Total (weighted, equal weight)** | **23** | **20** | **14** |

**Implication:** Omar is the natural P1 primary; Karim is the natural P2/P3 *expansion* persona once the engine has more telemetry surfaces; Layla is a Phase-5 (Desk Full v2) persona.

---

## Decisions required (Phase 1)

| # | Decision | Recommendation path | Owner |
|---|---|---|---|
| I-1 | Lock P1 primary persona | **Omar (P1)** | Founder |
| I-2 | Karim posture in P1 | Welcomed in cohort, but no copy/UX changes for him until P2 | Founder |
| I-3 | Layla posture in P1 | Not in cohort. Single line on the site: "Desk plans for small books open in 2027." | Founder |
| I-4 | Cohort-recruit checklist (must-have gates) | Trader has ≥6mo crypto futures experience, has a journaling habit, will run on Binance USDT-M testnet, signs the Risk Disclosure draft, accepts daily check-in cadence | Founder |
| I-5 | Disqualifiers (auto-out) | Day-one beginners, US-based residents (per jurisdictional posture), traders who refuse the testnet phase, copy-trade-only seekers | Founder |

---

## Assumptions to validate (Phase 1)

- ASSUMPTION — Omar will pay $79/mo to access a scanner + signals + gate journal *during* a 30-day validation phase. That is *during* validation, not after a track record exists. → REQUIRED INPUT from first 5 cohort calls.
- ASSUMPTION — the personas are real cohorts in the buyer pool, not just constructs. → REQUIRED INPUT — interview ≥10 candidates and tag them; if <60% map cleanly to one of the three, redo segmentation.
- ASSUMPTION — Omar can be reached without paid acquisition in P1. → DECISION NEEDED if we cannot hit cohort cap of 40 by end of May 2026 with founder-led only.

---

## Failure modes to avoid

- **All-three-equally** — splitting the 40-seat cohort across Omar/Karim/Layla learns nothing about any of them.
- **Optimizing for Layla too early** — the financial logic is tempting (higher ARPU). The trust logic is fatal (Layla won't engage without a track record).
- **Pseudo-personas** — accepting cohort members who don't pass the Omar gate "just to fill seats". Each off-persona seat is noise in the validation signal.
- **Treating the persona as a marketing target instead of a product target** — Omar should change which features ship next, which copy is on the dashboard, and which Telegram alerts are default-on. If the persona pick doesn't change product decisions, it's not a real pick.

---

## First-100-customer composition sketch (Omar primary)

If we pick Omar, the first 100 paying customers (target by end of P1, Jul 2026) should look approximately like:

- ~70 Omar (primary)
- ~20 Karim who self-onboarded and accepted Omar-tuned defaults
- ~10 cross-over (Omar drifting into Karim, or Karim under-fitting his depth ask)

If actual composition diverges materially (e.g., >40% Karim), that is a Phase 2 decision trigger — either widen the surface to serve Karim properly or tighten qualification to keep Omar the primary.

---

## Tasks (canonical — user-supplied 2026-05-04; see `08-task-backlog.md` for the full four-field backlog)

**NOW**

- `[RESEARCH] ICP — Primary Customer Segment Recommendation`
- `[RESEARCH] ICP — Jobs-to-Be-Done by Trader Type`
- `[RESEARCH] ICP — Pain Point Matrix for Quant Traders and Funds`
- `[DOC] ICP — Ideal Customer Profile Definitions v1`
- `[DOC] ICP — Primary vs Secondary Segment Decision Memo`

**NEXT**

- `[RESEARCH] ICP — Willingness-to-Pay Interview Framework`
- `[RESEARCH] ICP — Activation Triggers by Persona`
- `[DOC] ICP — Objection Handling by Customer Type`
- `[METRICS] ICP — Persona Fit Scoring Model`
- `[RESEARCH] ICP — Highest-Trust Entry Segment Analysis`

**LATER**

- `[RESEARCH] ICP — Team Buyer vs Solo Buyer Decision Path`
- `[DOC] ICP — Enterprise Buyer Readiness Notes`
