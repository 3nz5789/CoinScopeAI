# BRAND — Canonical Task List (Phase 3 staging)

**Status:** **PATH B ACTIVATED 2026-05-04.** BRAND was promoted into Phase 1 as the seventh workstream. Canonical task list now lives in `_phase-1/08-task-backlog.md` Section D. BRAND. Scaffold lives in `_phase-1/07-brand.md`. This file is retained as a record of the Phase-3-pending → Phase-1-active transition.
**Source of truth:** user-supplied canonical list 2026-05-04, reproduced verbatim (mirrored to `_phase-1/`).
**Format:** `[TYPE] [AREA] — Action / Deliverable`. Per-task fields: objective · why it matters · dependency · expected output.

---

## Why this is staged, not absorbed

Phase 1 charter (`_phase-1/00-phase-1-charter.md`) §2 lists in-scope workstreams as MARKET, ICP, POSITIONING, PRODUCT, TRUST, RISK and explicitly defers "Brand visual system, content calendar" to later phases. Per the 21-section project-instructions structure, "Brand and Content Strategy" is Section 11 and belongs to Phase 3 (GTM, trust, and operating readiness).

Two paths to activate this list:

1. **Defer to Phase 3** (default). When Phase 3 charter opens, this file becomes the seed of the BRAND section in the Phase 3 backlog. No further action now.
2. **Amend Phase 1 charter** to add BRAND as a seventh workstream. Requires updating `00-phase-1-charter.md` §2 in/out-of-scope, §4 exit criteria, §6 outputs, §7 crosswalk; creating `_phase-1/07-brand.md` scaffold; expanding `08-deliverable-map.md`; expanding `09-decision-register.md` with `B-*` IDs.

---

## Overlap with already-locked Phase 1 work

Several BRAND tasks overlap with locked Phase 1 work in POSITIONING and TRUST. Flagging now so de-dup is cheap when Phase 3 opens (or now if you amend Phase 1):

| BRAND task | Phase 1 task it overlaps | De-dup recommendation |
|---|---|---|
| `[DOC] BRAND — Voice and Tone Guidelines` | Scoopy custom-instructions (already locked); `[DOC] POSITIONING — Messaging Hierarchy v1` (NOW) | Voice/tone is *codified* already (anti-overclaim, evidence-led, methodical, risk-first); BRAND task narrows to surfaces and examples |
| `[DOC] BRAND — Trust and Credibility Pillars` | TRUST MVTS one-pager + Trust Signal Inventory v1 | BRAND task should *re-express* trust pillars in marketing language; the inventory is the source |
| `[DOC] BRAND — Brand Do/Don't Examples` | `[DOC] POSITIONING — Claim Language Guardrails` (NEXT) | Guardrails are the floor; BRAND examples are the patternbook for writers |
| `[DOC] BRAND — Founder Profile Messaging` | `[DOC] TRUST — Founder Bio + Jurisdictional Posture Page` (LATER) | Strict overlap; pick one canonical owner |
| `[QA] BRAND — App-to-Marketing Brand Alignment Review` | `[QA] POSITIONING — Messaging Consistency Review Across App and Site` (NEXT) | Strict overlap; collapse into one audit |

---

## A. BRAND — canonical list (verbatim)

### NOW

**`[DOC] BRAND — Brand Strategy Summary`**
- **Objective:** One-pager defining CoinScopeAI's brand strategy — promise, personality, principles, primary/secondary audience reads — anchored to the locked positioning sentence.
- **Why:** Without a single brand strategy artifact, content / partnerships / press all freelance from first principles. The summary is the seed every downstream BRAND task references.
- **Dependency:** Core Positioning Statement v1 (POSITIONING NOW); Primary vs Secondary Segment Decision Memo (ICP NOW).
- **Output:** Brand strategy summary MD; signed.

**`[DOC] BRAND — Voice and Tone Guidelines`**
- **Objective:** Codify product-tier vs social-tier voice, register rules, vocabulary, and worked examples (good / bad pairs) — reconciling Scoopy custom-instructions with public-surface needs.
- **Why:** Scoopy custom-instructions already define voice principles (anti-overclaim, evidence-led, methodical, risk-first); this task externalizes them into a writer-facing guide and adds tone-by-surface rules.
- **Dependency:** Brand Strategy Summary; Scoopy custom-instructions (locked).
- **Output:** Voice + tone MD with register table, vocabulary lists, do/don't examples per surface.

**`[DOC] BRAND — Trust and Credibility Pillars`**
- **Objective:** Translate the TRUST workstream's MVTS + Trust Signal Inventory into 3–5 pillars expressed in marketing-readable language.
- **Why:** MVTS items are operational; pillars are messageable. Without translation, marketing borrows uncodified pillars and drifts toward overclaim.
- **Dependency:** MVTS one-pager (TRUST NOW); Trust Signal Inventory v1 (TRUST NOW).
- **Output:** Pillars MD — 3–5 pillars with the underlying MVTS items each pillar references.

**`[DOC] BRAND — Visual Messaging Rules for Fintech/Crypto Audience`**
- **Objective:** Define visual rules — palette, typography, iconography, photography/screenshot conventions, anti-patterns — tuned for a fintech/crypto audience that is correctly skeptical by default.
- **Why:** Crypto-AI brands carry visual liabilities (hype iconography, neon gradients, lambo imagery, etc.). Rules pre-empt drift toward category visual debt.
- **Dependency:** Brand Strategy Summary; design-system manifest (memory ref).
- **Output:** Visual messaging rules MD; pairs with the existing design-system manifest.

**`[DOC] BRAND — Brand Do/Don't Examples`**
- **Objective:** Patternbook of good/bad copy and visual examples grounded in the locked anti-claim list and the Voice + Tone Guidelines.
- **Why:** Rules teach less than examples; a patternbook reduces founder-time on copy review and accelerates onboarding of any external writer or designer.
- **Dependency:** Voice and Tone Guidelines; Claim Language Guardrails (POSITIONING NEXT).
- **Output:** Do/don't examples MD with at least 10 paired examples across hero / about / Telegram / X / press.

### NEXT

**`[DOC] BRAND — Social Profile Copy Pack`**
- **Objective:** Lock the canonical bio / one-liner / pinned-post copy for X, LinkedIn, Telegram, GitHub, and any other public profile surface.
- **Why:** Profile copy is high-surface, low-iteration; the cost of inconsistency compounds.
- **Dependency:** Brand Strategy Summary; Voice and Tone Guidelines; Tagline Approval Set (POSITIONING NEXT).
- **Output:** Copy pack MD — one block per surface with character-count constraints honored.

**`[DOC] BRAND — Website Copy Structure`**
- **Objective:** Section-by-section copy structure for coinscope.ai pages (hero, about, methodology, pricing teaser, status page index).
- **Why:** Overlaps with `[DOC] POSITIONING — Homepage Narrative Structure` (NEXT) — when Phase 3 opens these may be merged. Holding here keeps them aligned.
- **Dependency:** Homepage Narrative Structure (POSITIONING NEXT); Brand Strategy Summary.
- **Output:** Page-by-page copy structure MD with content briefs and length budgets.

**`[DOC] BRAND — Founder Profile Messaging`**
- **Objective:** Founder bio short + long forms; speaking-engagement bio; About page block; jurisdictional posture line.
- **Why:** Founder identity is a trust signal in a category that mostly hides founders. Strict overlap with TRUST `[DOC] TRUST — Founder Bio + Jurisdictional Posture Page` (LATER) — when Phase 3 opens, collapse into one owner.
- **Dependency:** Brand Strategy Summary; TRUST T-9.
- **Output:** Founder messaging pack MD.

**`[DOC] BRAND — Community Presence Standards`**
- **Objective:** Define how CoinScopeAI shows up in any public community (X, Telegram, Discord-adjacent, forums) — moderation posture, response cadence, escalation, do-not-engage list.
- **Why:** Community surfaces leak fastest; a pre-codified standard reduces founder-time and pre-empts sales-pressure exceptions.
- **Dependency:** Voice and Tone Guidelines; Anti-Claim List (POSITIONING).
- **Output:** Community standards MD; covers reactive (replies, support) + proactive (posts) postures.

**`[QA] BRAND — App-to-Marketing Brand Alignment Review`**
- **Objective:** Walk every public surface and flag drift between in-app copy and marketing brand. Strict overlap with POSITIONING `[QA] POSITIONING — Messaging Consistency Review Across App and Site` (NEXT) — when Phase 3 opens, collapse into one audit pass.
- **Why:** App copy iterates independently of marketing copy; drift is the default state without an audit.
- **Dependency:** Voice and Tone Guidelines; Brand Do/Don't Examples; Messaging Hierarchy v1 (POSITIONING).
- **Output:** Audit report; copy patches.

### LATER

**`[DOC] BRAND — Media Kit and Partnership Intro Pack`**
- **Objective:** Assemble the reusable kit (logo lockups, founder bio, fact sheet, do-say / don't-say, screenshot library) for press and partnership intros.
- **Why:** Partnership outbound and inbound press are real exposure surfaces in P3+; kit reduces ad-hoc drafting and pre-empts off-message press.
- **Dependency:** Visual Messaging Rules; Founder Profile Messaging; Trust and Credibility Pillars.
- **Output:** Media kit + partnership intro pack — single bundle (folder + index MD).

**`[DOC] BRAND — Long-Form Thought Leadership Themes`**
- **Objective:** Lock 3–5 long-form thematic pillars (e.g., risk-first design, evidence-led claims, capital preservation in crypto futures) that author-bylined content will rotate across.
- **Why:** Without a theme set, long-form content drifts and competes with itself for attention; pillars create compounding voice.
- **Dependency:** Brand Strategy Summary; Trust and Credibility Pillars.
- **Output:** Themes MD with 3–5 pillars + worked-example outline per pillar.

---

## Activation paths

**Path A — Defer to Phase 3 (default, recommended).**
No further action now. When Phase 3 charter opens, this file becomes the seed of `_phase-3/01-brand.md` and the BRAND section of the Phase 3 task backlog. The overlap table above guides de-dup with Phase 1 POSITIONING/TRUST work.

**Path B — Amend Phase 1 charter to include BRAND.**
Requires the following patches in one pass (per `feedback_risk_threshold_reconciliation` reconciliation discipline):
1. `_phase-1/00-phase-1-charter.md` — add BRAND to §2 in-scope, §4 exit criteria, §6 outputs, §7 crosswalk.
2. Create `_phase-1/07-brand.md` scaffold (eight-block structure: purpose → why for CSAI → required subsections → recommended artifacts → assumptions → decisions required → failure modes → tasks).
3. Add BRAND section to `_phase-1/07-task-backlog.md` (verbatim, with four-field annotations).
4. Add BRAND rows to `_phase-1/08-deliverable-map.md`.
5. Add BRAND decisions (`B-*` IDs) to `_phase-1/09-decision-register.md`.
6. Add BRAND open questions to `_phase-1/10-open-questions.md`.
7. Renumber existing scaffold files only if necessary (they are not currently 7-positioned; safe).

If you pick Path B, also confirm the de-dup direction for the five overlap rows in the table above.

**Path C — Do not pursue BRAND in Phase 1 or Phase 3.**
Mark this file `MOOT` with reason and a phase pointer. The canonical list stays archived for future reference.

---

## What I did NOT do

- Did **not** modify any `_phase-1/` file.
- Did **not** add BRAND to `_phase-1/07-task-backlog.md` or `_phase-1/08-deliverable-map.md`.
- Did **not** create a `_phase-1/07-brand.md` scaffold.
- Did **not** update Source-of-truth note in `_phase-1/07-task-backlog.md` (still: MARKET, ICP, POSITIONING canonical; PRODUCT, TRUST, RISK draft).

Phase 1 boundaries are intact. Awaiting your decision (A / B / C).
