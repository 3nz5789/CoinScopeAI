# 07 — BRAND (Phase 1)

**Purpose:** Translate the locked positioning sentence and Phase 1 trust posture into a writer-and-designer-facing brand strategy — voice, tone, visual rules, do/don't patternbook — so every external surface reads as one company.
**v1 reference:** `09-brand-messaging.md`; Scoopy custom-instructions; design-system manifest.
**Phase 1 outcome:** Brand strategy summary signed; voice + tone guidelines codified; trust pillars expressed in marketing-readable language; visual rules locked; do/don't patternbook live.

> **Charter amendment note:** BRAND was added to Phase 1 on 2026-05-04 via Path B activation of `_phase-3-pending/brand-canonical-list.md`. Original Phase 1 scope (six workstreams) is preserved; BRAND is the seventh.

---

## Why BRAND matters specifically for CoinScopeAI

The category we ship into is *correctly* skeptical of crypto-AI brands. The Scoopy operating principles already encode a brand posture (anti-overclaim, evidence-led, methodical, risk-first); what's missing is the **externalized writer-and-designer guide** that lets anyone — founder, agency, contractor, contributor — produce on-brand work without re-deriving the principles each time.

Three forces make BRAND load-bearing in Phase 1:

1. **Crypto-AI visual debt.** The category's visual conventions (neon gradients, lambo iconography, rocket emojis, hype typography) actively *reduce* trust in the buyer Omar/Karim/Layla. Visual rules pre-empt drift toward category debt.
2. **Voice-tier separation.** Scoopy custom-instructions split product-tier (technical, terse, declarative, no emoji) from social-tier (aspirational, meme-fluent, never inside the product). The boundary is currently in a system prompt; BRAND externalizes it for any external writer.
3. **Founder-led distribution.** P1 distribution is founder-led; the founder's surfaces (X, LinkedIn, Telegram, podcasts, press) carry brand. Without codified rules, founder fatigue produces inconsistency that compounds across surfaces.

BRAND's specific Phase 1 commitment is: *codify what is already implicit, don't invent new claims.* New claims belong to POSITIONING; BRAND is the articulation layer.

---

## Required subsections

1. **Brand strategy summary** — promise, personality, principles, primary/secondary audience reads.
2. **Voice and tone guidelines** — register table (product-tier vs social-tier), vocabulary, do/don't pairs.
3. **Trust and credibility pillars** — 3–5 marketing-readable pillars that translate MVTS into messageable language.
4. **Visual messaging rules** — palette, typography, iconography, photography/screenshot conventions, anti-patterns.
5. **Do/don't patternbook** — at least 10 paired examples across hero / about / Telegram / X / press.
6. **Surface ownership map** — for each external surface, who owns the brand-correct copy and review cadence.
7. **De-dup register** — items that overlap with POSITIONING and TRUST and how the overlap is resolved.

---

## Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Brand Strategy Summary (signed) | MD, 1 page | Founder |
| Voice and Tone Guidelines | MD with register table + examples | Founder + Strategy CoS |
| Trust and Credibility Pillars (3–5) | MD pillars MD with MVTS source-link per pillar | Founder + TRUST owner |
| Visual Messaging Rules | MD + linked design-system manifest | Founder + Design |
| Do/Don't Patternbook | MD with ≥10 paired examples | Founder + Strategy CoS |
| Surface Ownership Map | MD table | Strategy CoS |
| De-dup Register (BRAND ↔ POSITIONING ↔ TRUST) | MD table, in this file | Strategy CoS |

---

## De-dup register (BRAND ↔ POSITIONING ↔ TRUST)

Five BRAND tasks overlap with already-locked Phase 1 work. Each row decides direction at activation; recommendations carry over from `_phase-3-pending/brand-canonical-list.md`.

| BRAND task | Overlaps with | Direction (recommended) |
|---|---|---|
| `[DOC] BRAND — Voice and Tone Guidelines` | Scoopy custom-instructions; POSITIONING `Messaging Hierarchy v1` | BRAND **externalizes** Scoopy rules; Messaging Hierarchy stays the claim spine; BRAND adds register table + vocabulary + examples |
| `[DOC] BRAND — Trust and Credibility Pillars` | TRUST `MVTS one-pager`; TRUST `Trust Signal Inventory v1` | BRAND **translates** MVTS into 3–5 marketing pillars; MVTS is source of truth; BRAND links each pillar to its MVTS items |
| `[DOC] BRAND — Brand Do/Don't Examples` | POSITIONING `Claim Language Guardrails` (NEXT) | Guardrails are floor; BRAND patternbook is the writer-facing example bank that *applies* the guardrails |
| `[DOC] BRAND — Founder Profile Messaging` | TRUST `Founder Bio + Jurisdictional Posture Page` (LATER) | **Strict overlap. Decision needed.** Recommend BRAND owns the *messaging*; TRUST owns the *page artifact*. One canonical bio, two surface owners. |
| `[QA] BRAND — App-to-Marketing Brand Alignment Review` | POSITIONING `Messaging Consistency Review Across App and Site` (NEXT) | **Strict overlap. Decision needed.** Recommend collapse into one audit pass owned jointly by BRAND + POSITIONING; do not run twice. |

The two strict-overlap rows are reflected in Decision Register entries B-4 and B-5.

---

## Assumptions to validate (Phase 1)

- ASSUMPTION — the Scoopy product-tier voice rules survive externalization into a writer guide without dilution. → REQUIRED INPUT — first draft of Voice and Tone Guidelines reviewed by founder against Scoopy custom-instructions.
- ASSUMPTION — visual rules tuned against crypto-AI category visual debt land correctly with the *Omar* persona, not just defensively. → REQUIRED INPUT — cohort-recruit landing-page A/B between current visual treatment and a more-conventional fintech treatment.
- ASSUMPTION — three-to-five trust pillars (BRAND) is the right cardinality; fewer reads thin, more reads as a feature list. → DECISION NEEDED if first draft exceeds five.

---

## Decisions required (Phase 1)

| # | Decision | Recommendation path | Owner |
|---|---|---|---|
| B-1 | Lock the Brand Strategy Summary | Sign as drafted after first founder pass | Founder |
| B-2 | Voice-tier boundary in writer guide | Codify product-tier (no emoji, no hype, declarative) and social-tier (aspirational, meme-fluent, never inside product) per Scoopy custom-instructions; *no new tier* | Founder |
| B-3 | Number of trust pillars | 3–5; recommend 4 | Founder |
| B-4 | Founder Profile Messaging ownership (BRAND vs TRUST) | BRAND owns the *messaging*; TRUST owns the *page artifact* | Founder |
| B-5 | App-to-Marketing audit collapse with POSITIONING audit | Collapse into one joint audit pass; do not run twice | Founder + Strategy CoS |
| B-6 | Visual treatment lock vs A/B test | Lock current treatment for Phase 1 cohort; queue A/B as Phase 2 input | Founder |
| B-7 | Founder-led distribution surface list (X, LinkedIn, Telegram, podcasts, press) | All four; press behind Phase-3 PR kit (LATER) | Founder |

---

## Failure modes to avoid

- **Brand-by-aspiration.** Writing the brand we want to be at Desk Full v2, not the brand we are at P0/P1. Phase 1 BRAND describes *what is true today*.
- **Inventing claims.** BRAND is articulation, not invention. New claims belong to POSITIONING.
- **Visual debt by default.** Defaulting to category visual conventions (neon, hype, rocket emojis) because they're "what crypto looks like". The whole point of CoinScopeAI's positioning is *not to look like that*.
- **Voice-tier leak.** Social-tier language inside the product is the most expensive consistent leak — destroys the anti-overclaim posture instantly.
- **Patternbook by abstraction.** Rules without paired examples teach less than examples without rules. Patternbook must be paired (good vs bad) on real surfaces.
- **Audit duplication.** Running BRAND audit and POSITIONING audit separately doubles effort and produces conflicting findings. Collapse.

---

## Tasks (canonical — user-supplied 2026-05-04; see `08-task-backlog.md` for the full four-field backlog)

**NOW**

- `[DOC] BRAND — Brand Strategy Summary`
- `[DOC] BRAND — Voice and Tone Guidelines`
- `[DOC] BRAND — Trust and Credibility Pillars`
- `[DOC] BRAND — Visual Messaging Rules for Fintech/Crypto Audience`
- `[DOC] BRAND — Brand Do/Don't Examples`

**NEXT**

- `[DOC] BRAND — Social Profile Copy Pack`
- `[DOC] BRAND — Website Copy Structure`
- `[DOC] BRAND — Founder Profile Messaging`
- `[DOC] BRAND — Community Presence Standards`
- `[QA] BRAND — App-to-Marketing Brand Alignment Review`

**LATER**

- `[DOC] BRAND — Media Kit and Partnership Intro Pack`
- `[DOC] BRAND — Long-Form Thought Leadership Themes`
