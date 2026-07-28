# PACKAGING — Tier Structure Recommendation

**Task:** `[DOC] PACKAGING — Tier Structure Recommendation`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — pending P0 cohort exit memo for ratify/revise lock
**Feeds decision:** **Pk-1**
**Anchored to:** v1 framework `06-pricing-monetization.md` §6.6 Track B; §6.5 Free Scope B; §6.3 Model C (subscription + per-seat); Phase 1 PRODUCT Value Ladder.

---

## TL;DR

**Recommend: ratify Track B as the P1 Narrow Ship commercial structure.**

- 4 paid-or-free tiers + 2 per-seat add-on rows.
- Free / Trader $79 / Desk Preview $399 / Desk Full v2 $1,199 + partner $149 / analyst $249.
- Internal naming: keep "Trader / Desk Preview / Desk Full" — never "Pro / Premium / Enterprise" (per §5.3.3 packaging principle).
- Lock through P0 cohort exit memo; revise only if exit memo surfaces a structural mismatch (defined below).

**Three alternatives evaluated and rejected** with reasoning. **Two ratify-conditions** must hold at P0 exit memo to confirm the lock.

---

## 1. Track B as recommended (ratify)

| Tier | Monthly | Annual | Founder cohort* | Persona anchor | Function in funnel |
|---|---|---|---|---|---|
| Free | $0 | $0 | $0 | sub-$5k disciplined ("we'll be back"); P1 trial | Conversion valve + trust demo |
| Trader | $79/mo | $790/yr | $59/mo | P1 Methodist (Omar); P2 Engineer (Karim) entry | Volume tier; LTV $1,580 base case |
| Desk Preview | $399/mo | $3,990/yr | $299/mo | P3 Solo PM (Layla) entry; P2 power-user trigger | Pre-Desk-Full discovery; LTV ~$10k |
| Desk Full v2 | $1,199/mo | $11,990/yr | $899/mo | P3 Layla scaling | Margin tier; LTV ~$52k incl. seats |
| + partner read-only seat | $149/mo | $1,490/yr | $99/mo | P3 partners / co-PMs | Per-seat density (§11 sensitivity #1) |
| + analyst seat | $249/mo | $2,490/yr | $179/mo | P3 analyst hires | Higher because of write privileges |

*Founder cohort: first 60 days post-public-launch (P2 phase per §5.4). Locks through one renewal cycle. No grandfather, no "lifetime" framing.

---

## 2. Why ratify (the case for not changing)

1. **§6 v1 LOCKED 2026-05-01** with the full §6.5 / §6.6 / §6.7 / §6.8 / §6.9 / §6.10 chain committed. Changing tier structure forces re-derivation downstream (§11 financial model, §13 KPIs, §9 messaging). Lock is itself a feature.
2. **WTP bands fit cleanly** (per §6.2): P1 lands in $40–$150 ($79 mid-band); P3 entry lands in $250–$500 ($399 mid-band); P3 scaling lands in $750–$1,500 ($1,199 mid-band). No tier sits at the wrong end of its band.
3. **4 tiers is the maximum coherent count** for a comparison surface. SaaS norms — TradingView (4), Glassnode (4), Nansen (3), Tradervue (3) — cluster at 3–4. Five tiers crowds the page; three forces P3 into a single ceiling tier and loses the Preview→Full discovery step.
4. **Per-seat add-on captures P3 asymmetry** (§6.2: P3 carries 5–10x P1 per-user revenue). Per-seat is the §11 sensitivity-rank #1 input. Removing it collapses Layla into a single $1,199 SKU and forfeits ~$2,700/yr per Desk Full account at base-case density.
5. **Free Scope B is load-bearing for the funnel** (§6.5). Removing Free or moving to a free trial breaks the "we'll be back" sub-$5k branch and the §5.3.1 demo-trade trust signal.

---

## 3. Three alternatives evaluated

### Alternative A — Collapse Desk Preview into Desk Full v2 (3-tier)

**Shape:** Free / Trader $79 / Desk $899 (no Preview).

**Pro:** Simpler comparison surface; one fewer upgrade event in the funnel.

**Con:**
- Loses the Preview → Full discovery step. P3 buyers expect a "try before scale" tier; Layla canvas explicitly references graduated commitment.
- Compresses pricing power: $899 single tier sits in the awkward middle of $250–$1,500 P3 WTP band. Either too high for entry or too low to justify Desk Full features.
- §11 sensitivity #4 (Preview → Full v2 migration rate) becomes meaningless — there's nothing to migrate from.

**Reject.** Preview → Full is a structural step P3 buyers expect.

### Alternative B — Add Trader Annual-only sub-tier ("Trader Lite")

**Shape:** Free / Trader Lite $39 (annual-only, ~$468/yr, reduced feature set) / Trader $79 / Desk Preview / Desk Full v2.

**Pro:** Captures sub-$79 WTP that bounces off Trader.

**Con:**
- Violates §5.3.3 "no anti-ICP bundling" by creating a sub-tier that targets the price-sensitive end of P1 — the segment most likely to also be the casual-retail buyer §3.5 explicitly de-prioritizes.
- 5 tiers crowd the comparison surface (failure mode #1 in `01-packaging.md`).
- Trader Lite at $39 is below the §6.2 P1 floor of $40–$150; signals "discount product" rather than "discipline product."
- Cannibalizes Trader at minimum 30% of the WTP-marginal cohort (inference, not measured).

**Reject.** Wrong segment (anti-ICP), wrong signal (discount), wrong tier count (5).

### Alternative C — Per-seat $149/$249 collapsed to single $199

**Shape:** Track B as-is, but Desk Full per-seat is one row at $199 instead of two ($149 partner / $249 analyst).

**Pro:** Single per-seat row is simpler on the comparison surface and in Stripe.

**Con:**
- Loses the role distinction. Partner read-only and analyst (write privileges) have materially different functional access; pricing them the same misprices both — partner seats become overpriced (friction for adding partners), analyst seats become underpriced (revenue leak).
- §6.6 rationale explicitly anchors $249 analyst at ~21% of base because of write-privilege exposure. Single $199 weakens that anchor.
- P3 buyers (especially LP-aware Solo PMs) are accustomed to seat-role distinctions from financial-services tooling (Bloomberg, FactSet, PMS systems). Collapsing reads as unsophisticated.

**Reject.** The $100 spread between partner and analyst is meaningful and load-bearing.

---

## 4. Conditions under which Track B should be revised

Lock Track B at Phase 2 close *unless* the P0 cohort exit memo (per `_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`) surfaces one or more of the following:

| Trigger | Implies | Recommended revision |
|---|---|---|
| Free → Trader conversion < 2% over 90 days for §6.5 Scope B | Free scope is too tight (acquisition fine, conversion broken) | Reopen **Pk-2** to revise Free vs Paid boundary (Scope B + post-validation journal-read-only exception) — *not* tier structure |
| Trader → Desk Preview conversion < 4% over 12 months | Preview tier is not pulling P3 entry | Reopen tier structure: consider raising Trader floor or repositioning Preview as P2 power-user tier |
| Per-seat density < 1.5 average across Desk Full accounts | P3 buyers not adding partners; per-seat is theatre | Reopen **Pk-3** — collapse to single seat row or remove per-seat entirely |
| Desk Preview → Desk Full v2 migration rate < 50% at v2 launch | Preview is an end-state, not a step | Collapse Preview into Full (Alternative A becomes valid post-data) |
| Cohort feedback explicitly requests Trader Annual-only at lower price | Real WTP segment exists below $79 | Reopen Alternative B *with persona-fit screen* to confirm not anti-ICP |

If none trigger: ratify, lock, and close **Pk-1**.

---

## 5. Naming guard

Per §5.3.3 packaging principles, the following tier names are **disallowed**:

- "Pro" — implies Free is amateur; counter-positions Free Scope B's trust demo.
- "Premium" — vague pricing-power signal with no functional referent.
- "Enterprise" — implies fund-formation use-case (forbidden per §3.5 anti-persona and §12 risk register Solo PM regulatory carve-out).
- "Lite" — implies feature withholding; reads as discount product.
- "Starter" — diminishes Free; Free is not a starter, it's a trust demo.

Acceptable:
- **Trader** — functional, accurate, anchors to §3 P1/P2 personas.
- **Desk Preview** — explicit lifecycle qualifier; primes the Preview → Full step.
- **Desk Full v2** — explicit version qualifier; signals iteration discipline.

---

## 6. Open dependencies

- **Pr-4 final form** (Free-tier limits) ratified or revised → operationalizes Free vs Paid boundary (next deliverable).
- **P0 cohort exit memo** → triggers the revision-condition table above.
- **Phase 1 PRODUCT MOSCOW** → confirms feature inventory aligns with §6.5 Scope B + §5.3.2 paid feature list.

---

## 7. What this unlocks

- **Pk-1** decision can be marked recommended-ratify pending P0 exit memo.
- `[DOC] PACKAGING — Free vs Paid Feature Boundary` proceeds against ratified Track B.
- `[DOC] PACKAGING — Plan Comparison Table v1` has the row count locked (4 tiers + 2 per-seat add-on rows).
- `[DOC] PACKAGING — Premium Feature Gating Rules` has the tier-set locked for gating-type assignment.
- §11 financial model uses Track B inputs without re-derivation risk.
