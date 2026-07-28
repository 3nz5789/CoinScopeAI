# 08 — Phase 1 Task Backlog (Claude Co-Work ready)

**Scope:** Phase 1 only — workstreams MARKET, ICP, POSITIONING, BRAND, PRODUCT, TRUST, RISK *(BRAND added 2026-05-04 via Path B charter amendment)*.
**Format:** `[TYPE] [AREA] — Action / Deliverable`. Grouped by workstream. Within each workstream: NOW / NEXT / LATER.
**Per-task fields:** objective · why it matters · dependency · expected output.

> **Source-of-truth note:** all seven Phase 1 workstream lists — **MARKET**, **ICP**, **POSITIONING**, **BRAND**, **PRODUCT**, **TRUST**, and **RISK** — are the user-supplied canonical lists as of 2026-05-04 and are reproduced verbatim. Phase 1 task backlog is complete.

---

## A. MARKET

### NOW

**`[RESEARCH] MARKET — Crypto Futures Category Map`**
- **Objective:** Map every adjacent shelf in crypto futures tooling: bot vendors, signal services, charting platforms, quant platforms, trader OS, risk-management tools.
- **Why:** Phase 1 needs a defensible category pick. We can't pick what we haven't enumerated.
- **Dependency:** none.
- **Output:** MD file in `_phase-1/_research/category-map.md` — table with category, exemplar vendors, lead claim, trust burden, pricing band.

**`[RESEARCH] MARKET — Total Addressable Segment Estimate`**
- **Objective:** Rough TAM/SAM/SOM for self-directed crypto futures traders globally, sliced by geography and account-size band.
- **Why:** Sets the ceiling on the realistic Trader-tier funnel and the realism of the 100-customer P1 target.
- **Dependency:** Category Map.
- **Output:** MD file with sourced numbers, explicit ASSUMPTION markers, and a one-sentence implication for Phase 1 sizing.

**`[RESEARCH] MARKET — Market Timing Thesis for AI Trading Infrastructure`**
- **Objective:** Establish whether 2026 is the right window for AI-flavoured trading infrastructure and what *kind* of AI claim still earns trust.
- **Why:** "AI" is positioning oxygen and positioning poison at the same time. We need a defensible read on which.
- **Dependency:** Category Map.
- **Output:** Timing thesis MD — three-paragraph max, signed.

**`[DOC] MARKET — CoinScopeAI Market Thesis v1`**
- **Objective:** One-page market thesis stitching category, segment, and timing into the CSAI-specific bet.
- **Why:** This is the document that v1 framework `02-market-thesis.md` should crosswalk to; Phase 1 lock.
- **Dependency:** Category Map, TAM Estimate, Timing Thesis.
- **Output:** `_phase-1/01-market.md` updated + Decision Memo signed by founder.

**`[RESEARCH] MARKET — Retail-to-Pro Trader Segment Breakdown`**
- **Objective:** Quantify how the self-directed trader segment splits between hobbyist / serious / semi-pro / pro across crypto futures.
- **Why:** ICP scoring uses this as input; primary persona pick (Omar) lives in the serious / semi-pro band.
- **Dependency:** TAM Estimate.
- **Output:** Segment bands with definition + size estimate per band.

### NEXT

**`[RESEARCH] MARKET — Institutional vs Individual Adoption Drivers`**
- **Objective:** Identify the structural differences in why funds adopt vs why individuals adopt.
- **Why:** Drives whether the Desk Full v2 narrative (Phase 5) is coherent with the P1 individual narrative.
- **Dependency:** Category Map.
- **Output:** Drivers MD; informs Decision Log entry on Layla deferral.

**`[RESEARCH] MARKET — Exchange Dependency Risk by User Segment`**
- **Objective:** Quantify how much each user segment cares about (and is hurt by) exchange-side outages.
- **Why:** Vendor-failure posture (RISK + TRUST) and the public posture toward Binance dependency.
- **Dependency:** Category Map.
- **Output:** Sensitivity table per segment + posture recommendation.

**`[DOC] MARKET — Why Now Narrative for CoinScopeAI`**
- **Objective:** Convert Timing Thesis into a fundraising-grade "why now" paragraph.
- **Why:** Used in cohort recruiting copy now; reused in fundraising in Phase 4.
- **Dependency:** Market Thesis v1, Timing Thesis.
- **Output:** 150-word paragraph; locked.

**`[METRICS] MARKET — Market Validation KPI Framework`**
- **Objective:** Define the KPIs that, if true, confirm the market thesis (and which would falsify it).
- **Why:** Without this, we cannot tell whether Phase 1 worked from a market POV.
- **Dependency:** Market Thesis v1.
- **Output:** KPI table — name, definition, source, target, falsifier.

**`[RESEARCH] MARKET — Macro Trends Impacting Crypto Trading Tool Demand`**
- **Objective:** Catalogue macro forces (rates, regulation, exchange consolidation, AI-skepticism cycle) and their plausible impact on demand.
- **Why:** Scenario planning input; hedges Phase 1 lock against external shocks.
- **Dependency:** Timing Thesis.
- **Output:** Trends register; one-line impact per trend.

### LATER

**`[RESEARCH] MARKET — Geographic Expansion Attractiveness Review`**
- **Objective:** Score expansion priorities outside UAE/MENA + global EN.
- **Why:** Phase 3 GTM input; Phase 1 just queues it.
- **Dependency:** Market Thesis v1, Jurisdictional posture (memory).
- **Output:** Geography scorecard.

**`[DOC] MARKET — Market Expansion Scenarios`**
- **Objective:** Three scenarios for market evolution (base / upside / downside) to feed Phase-2 scenario planning.
- **Why:** Removes scenario-planning startup cost from Phase 2.
- **Dependency:** Macro Trends, Why Now Narrative.
- **Output:** Three-scenario MD.

**`[RESEARCH] MARKET — Adjacent Market Opportunities Beyond Futures`**
- **Objective:** Lightly scope spot, options, FX, equities-crypto crossovers — *not* to commit, just to bound.
- **Why:** Avoid premature lock that closes Phase 5 doors.
- **Dependency:** Category Map.
- **Output:** Adjacent shelf scan; no commitments.

---

## B. ICP

### NOW

**`[RESEARCH] ICP — Primary Customer Segment Recommendation`**
- **Objective:** Recommend one of {P1 Omar / P2 Karim / P3 Layla} as the **P1 primary** segment, with explicit deferral reasoning for the other two.
- **Why:** Phase 1 ICP exit hinges on locking primary; cohort cap of 40 cannot be split across three segments and produce signal.
- **Dependency:** v1 framework `03-icp-segmentation.md`; persona-fit tagging from candidate interviews.
- **Output:** Recommendation MD; feeds Decision Register entry I-1.

**`[RESEARCH] ICP — Jobs-to-Be-Done by Trader Type`**
- **Objective:** Articulate the JTBD per persona — what each trader hires CoinScopeAI to do for them on a normal trading day (Scan → Score → Gate → Size → Arm).
- **Why:** Forces us off feature-list thinking onto trader-loop thinking; input for Activation Triggers and PRODUCT MOSCOW.
- **Dependency:** Persona-fit interview tagging.
- **Output:** JTBD MD with one job-statement per persona + trigger / progress / outcome verbs.

**`[RESEARCH] ICP — Pain Point Matrix for Quant Traders and Funds`**
- **Objective:** Catalogue dominant pain points specifically for the more-deferred segments (Karim and Layla), not the primary.
- **Why:** Karim/Layla are P2 / Phase-5, but their pain inventory shapes which features become Should/Could in P1 vs deferred entirely. Avoids quiet over-build for them.
- **Dependency:** Outbound conversations with quant-trader and small-fund prospects; v1 `03-icp-segmentation.md`.
- **Output:** Pain matrix MD; informs PRODUCT MOSCOW Should/Could buckets.

**`[DOC] ICP — Ideal Customer Profile Definitions v1`**
- **Objective:** Convert the v1 framework's three named personas into formal ICP definitions (firmographic / behavioural / motivational fields).
- **Why:** Persona one-liners aren't operational; marketing, sales, and signup-form logic need ICP definitions with concrete fields.
- **Dependency:** JTBD MD; v1 `03-icp-segmentation.md`.
- **Output:** ICP definitions MD — one row per persona with the canonical fields.

**`[DOC] ICP — Primary vs Secondary Segment Decision Memo`**
- **Objective:** Lock the P1 primary, secondary (cohort-welcomed but not optimized), and deferred segments with stated reasoning.
- **Why:** Phase 1 exit gate; downstream of Primary Customer Segment Recommendation.
- **Dependency:** Primary Customer Segment Recommendation; ICP Definitions v1.
- **Output:** Signed memo; Decision Register entries I-1, I-2, I-3 mirror to `_decisions/decision-log.md`.

### NEXT

**`[RESEARCH] ICP — Willingness-to-Pay Interview Framework`**
- **Objective:** Build the interview script for testing willingness-to-pay specifically *during* the 30-day validation phase (not after a track record exists).
- **Why:** IQ-1 in `11-open-questions.md` is exit-blocking; needs a structured framework, not ad-hoc probing.
- **Dependency:** Primary vs Secondary Segment Decision Memo.
- **Output:** WTP interview framework MD — question bank, scoring rubric, tagging matrix.

**`[RESEARCH] ICP — Activation Triggers by Persona`**
- **Objective:** Identify the in-product event(s) that mark "this trader is now a real user" for each persona.
- **Why:** Activation triggers feed PRODUCT telemetry (cohort week-1 plan) and Phase-3 onboarding design.
- **Dependency:** JTBD MD; engine telemetry hooks.
- **Output:** Activation triggers MD — one trigger per persona, mapped to engine event(s).

**`[DOC] ICP — Objection Handling by Customer Type`**
- **Objective:** Document the most common objections per persona and the on-message response (anti-claim list respected).
- **Why:** Founder-led distribution and cohort recruiting both surface objections; consistency matters more than cleverness.
- **Dependency:** Primary vs Secondary Segment Decision Memo; POSITIONING anti-claim list.
- **Output:** Objection-handling MD; one section per persona.

**`[METRICS] ICP — Persona Fit Scoring Model`**
- **Objective:** Convert the qualitative fit matrix into a numeric scoring model applied to a candidate during signup intake.
- **Why:** Scales the cohort-fit decision; reduces founder-time bottleneck during recruiting.
- **Dependency:** ICP Definitions v1; Persona-fit interview tagging.
- **Output:** Scoring model MD + signup-form field schema.

**`[RESEARCH] ICP — Highest-Trust Entry Segment Analysis`**
- **Objective:** Of the three personas, identify which one *trusts* CoinScopeAI fastest with the smallest evidence load.
- **Why:** Phase 1 trust budget is finite (MVTS hard gate); we want the segment whose trust signal needs we can already meet.
- **Dependency:** Persona-fit interview tagging; MVTS one-pager (TRUST).
- **Output:** Trust-load comparison MD; recommends entry segment + the supporting trust signals it requires.

### LATER

**`[RESEARCH] ICP — Team Buyer vs Solo Buyer Decision Path`**
- **Objective:** Map the buying-decision path for solo (Omar / Karim) vs team (Layla, Phase 5) buyers.
- **Why:** Phase-5 input — decision paths drive sales motion design and pre-empt premature enterprise-feature sprawl in P1.
- **Dependency:** ICP Definitions v1.
- **Output:** Decision-path MD; *no commitments*.

**`[DOC] ICP — Enterprise Buyer Readiness Notes`**
- **Objective:** Catalogue what an enterprise (small fund / Desk Full v2) buyer would need from CoinScopeAI before signing.
- **Why:** Phase-5 charter input; prevents premature enterprise-feature sprawl in P1.
- **Dependency:** Team Buyer vs Solo Buyer Decision Path.
- **Output:** Readiness notes MD; *no commitments*.

---

## C. POSITIONING

### NOW

**`[DOC] POSITIONING — Core Positioning Statement v1`**
- **Objective:** Lock the **one** positioning sentence (≤25 words) CoinScopeAI leads with on every external surface.
- **Why:** Hero, about, docs, Telegram bot intro, X bio, LinkedIn all source from this. Without a lock, copy drifts and cross-surface conflicts emerge.
- **Dependency:** Market Thesis v1 (MARKET); Primary vs Secondary Segment Decision Memo (ICP).
- **Output:** Signed memo + locked sentence; Decision Register entry P-1.

**`[DOC] POSITIONING — Category Definition Recommendation`**
- **Objective:** Recommend the category CoinScopeAI competes in (one of A/B/C/D from `01-market.md`) and articulate the trust contract that category implies.
- **Why:** Category lock = trust contract. It determines comparison set in the buyer's mind, which claims are credible / legal, and which adjacent shelves we will or won't be slotted into.
- **Dependency:** Crypto Futures Category Map (MARKET); Market Thesis v1 (MARKET).
- **Output:** Recommendation MD; cross-references Decision Register entry M-1.

**`[DOC] POSITIONING — Value Proposition Matrix by ICP`**
- **Objective:** Map the locked positioning sentence to a **per-persona** value prop (Omar primary, Karim secondary, Layla deferred) — different surface language, same claim spine.
- **Why:** One sentence does not serve three personas equally. A matrix prevents marketing from collapsing into Omar-only and pre-empts ad-hoc Layla overpromise under sales pressure.
- **Dependency:** Core Positioning Statement v1; Ideal Customer Profile Definitions v1 (ICP).
- **Output:** Value-prop matrix MD — one row per persona with allowed adjectives, headline language, and disallowed phrasing.

**`[DOC] POSITIONING — Messaging Hierarchy v1`**
- **Objective:** Define the message ladder — primary claim → supporting claims → proof points → anti-claims — that every external surface must respect.
- **Why:** Without an explicit hierarchy, supporting copy drifts off the primary claim under writer / agency / founder variation. Hierarchy outlasts copy iteration.
- **Dependency:** Core Positioning Statement v1; Claim Language Guardrails (NEXT, partial — anti-claim list).
- **Output:** Messaging hierarchy MD with the ladder + worked examples for hero, about, and docs surfaces.

**`[RESEARCH] POSITIONING — Trust-Centered Differentiation Analysis`**
- **Objective:** Analyze how each adjacent shelf (bot vendors, signal services, charting, quant platforms, trader OS, risk-management tools) earns trust today, and articulate how CoinScopeAI's trust contract differs from each.
- **Why:** Differentiation by *trust contract* is durable; differentiation by feature set is not. This is the source for the comparison-set table and competitive contrast messaging downstream.
- **Dependency:** Crypto Futures Category Map (MARKET).
- **Output:** Trust differentiation analysis MD; populates the comparison-set table in `03-positioning.md`.

### NEXT

**`[DOC] POSITIONING — Claim Language Guardrails`**
- **Objective:** Lock the anti-claim list (no P&L, no automation promise, no "institutional-grade", no "production-ready") **and** the *replacement* phrasings allowed at each risk-state (Validation / Narrow Ship / §8 Phase 1 / Desk Full).
- **Why:** Anti-claims without replacements leave a copy hole; replacements without anti-claims invite drift. Must be paired.
- **Dependency:** Core Positioning Statement v1; Risk-State Claim Allowance Matrix (RISK).
- **Output:** Guardrails MD; Decision Register entry P-2 + cross-link to RISK R-2.

**`[DOC] POSITIONING — Competitive Contrast Messaging`**
- **Objective:** Translate Trust-Centered Differentiation Analysis into ready-to-use contrast lines ("we are not the X that did Y to you") for each adjacent shelf.
- **Why:** Founder-led distribution and cohort recruiting surface objections framed in adjacent-shelf language; pre-written contrast lines reduce founder-time and ensure on-message consistency.
- **Dependency:** Trust-Centered Differentiation Analysis.
- **Output:** Contrast messaging MD; one block per adjacent shelf (bot vendors, signal services, charting, quant platforms).

**`[DOC] POSITIONING — Homepage Narrative Structure`**
- **Objective:** Define the section order, content type, and length budget for the coinscope.ai homepage so the locked positioning sentence and messaging hierarchy land correctly.
- **Why:** Homepage structure outlasts copy iteration; without it, every redesign relitigates positioning. Section structure is also where MVTS trust signals get embedded.
- **Dependency:** Messaging Hierarchy v1; Core Positioning Statement v1; MVTS one-pager (TRUST).
- **Output:** Structure MD with section-by-section content brief + length budgets.

**`[DOC] POSITIONING — Product Tagline Options`**
- **Objective:** Lock the canonical tagline pairs ("Trade Smarter With AI" / "Trade Smarter") and the surface assignment for each (hero / X bio / LinkedIn / Telegram).
- **Why:** Per Scoopy custom-instructions the tagline pairs are pre-approved, but their surface assignment is not locked. Cross-surface consistency requires explicit assignment.
- **Dependency:** Core Positioning Statement v1.
- **Output:** Tagline rules MD; Decision Register entry P-3.

**`[QA] POSITIONING — Messaging Consistency Review Across App and Site`**
- **Objective:** Walk every external surface (hero, about, docs, Telegram bot intro, X bio, LinkedIn, in-app onboarding copy) and flag any drift from the locked positioning sentence, messaging hierarchy, or anti-claim list.
- **Why:** POSITIONING is only as strong as the audit; product surfaces (in-app copy) drift fastest because they iterate independently.
- **Dependency:** Core Positioning Statement v1; Messaging Hierarchy v1; Claim Language Guardrails.
- **Output:** Audit report; copy patches.

### LATER

**`[DOC] POSITIONING — Institutional Expansion Narrative`**
- **Objective:** Outline the positioning narrative for Desk Full v2 (Phase 5) — how "AI trading intelligence platform" earns the right to use "institutional-grade" language.
- **Why:** Phase-5 charter input. Pre-empts premature use of institutional language in P1 *and* ad-hoc rewriting under sales pressure later.
- **Dependency:** Core Positioning Statement v1; Validation cohort exit memo.
- **Output:** Narrative MD; *no commitments* in P1.

**`[DOC] POSITIONING — Media and PR Messaging Kit`**
- **Objective:** Build a reusable kit (founder bio, fact sheet, do-say / don't-say guide) for inbound or outbound press in P2+.
- **Why:** Press is a real exposure surface for crypto-AI trading software; off-message press damages trust faster than off-message marketing.
- **Dependency:** Core Positioning Statement v1; Claim Language Guardrails; Founder Bio + Jurisdictional Posture Page (TRUST).
- **Output:** PR kit MD bundle.

---

## D. BRAND

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
- **Why:** Crypto-AI brands carry visual liabilities (hype iconography, neon gradients, lambo imagery). Rules pre-empt drift toward category visual debt.
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
- **Dependency:** Brand Strategy Summary; Voice and Tone Guidelines; Product Tagline Options (POSITIONING NEXT).
- **Output:** Copy pack MD — one block per surface with character-count constraints honored.

**`[DOC] BRAND — Website Copy Structure`**
- **Objective:** Section-by-section copy structure for coinscope.ai pages (hero, about, methodology, pricing teaser, status page index).
- **Why:** Strict overlap with `[DOC] POSITIONING — Homepage Narrative Structure` (NEXT) — at execution time, collapse into one structure document jointly owned. Holding here keeps them aligned.
- **Dependency:** Homepage Narrative Structure (POSITIONING NEXT); Brand Strategy Summary.
- **Output:** Page-by-page copy structure MD with content briefs and length budgets.

**`[DOC] BRAND — Founder Profile Messaging`**
- **Objective:** Founder bio short + long forms; speaking-engagement bio; About page block; jurisdictional posture line.
- **Why:** Founder identity is a trust signal in a category that mostly hides founders. Strict overlap with TRUST `[DOC] TRUST — Founder Bio + Jurisdictional Posture Page` (LATER); per Decision B-4, BRAND owns *messaging*, TRUST owns *page artifact*.
- **Dependency:** Brand Strategy Summary; TRUST T-9.
- **Output:** Founder messaging pack MD.

**`[DOC] BRAND — Community Presence Standards`**
- **Objective:** Define how CoinScopeAI shows up in any public community (X, Telegram, Discord-adjacent, forums) — moderation posture, response cadence, escalation, do-not-engage list.
- **Why:** Community surfaces leak fastest; a pre-codified standard reduces founder-time and pre-empts sales-pressure exceptions.
- **Dependency:** Voice and Tone Guidelines; Claim Language Guardrails (POSITIONING NEXT).
- **Output:** Community standards MD; covers reactive (replies, support) + proactive (posts) postures.

**`[QA] BRAND — App-to-Marketing Brand Alignment Review`**
- **Objective:** Walk every public surface and flag drift between in-app copy and marketing brand. Strict overlap with POSITIONING `[QA] POSITIONING — Messaging Consistency Review Across App and Site` (NEXT); per Decision B-5, collapse into one joint audit pass.
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

## E. PRODUCT

### NOW

**`[DOC] PRODUCT — Product Strategy Overview`**
- **Objective:** One-pager defining the product strategy — primary trader loop (Scan → Score → Gate → Size → Arm), product principles, and the explicit non-goals.
- **Why:** Every Phase-1 product decision references this. Without it, pillars / matrix / value ladder / feature requests all freelance from first principles.
- **Dependency:** Market Thesis v1 (MARKET); Primary vs Secondary Segment Decision Memo (ICP); Core Positioning Statement v1 (POSITIONING).
- **Output:** Product strategy MD; signed; Decision Register entry Pr-1.

**`[DOC] PRODUCT — Core Product Pillars`**
- **Objective:** Define 3–5 pillars that organize every feature decision (e.g., risk-first execution, evidence-led signals, regime-aware sizing, trader-loop journaling).
- **Why:** Pillars stop feature debate from becoming personal preference; every Should/Could decision tests against pillar fit.
- **Dependency:** Product Strategy Overview; engine endpoint inventory (`/scan`, `/risk-gate`, `/position-size`, `/regime/{symbol}`, `/performance`, `/journal`).
- **Output:** Pillars MD with pillar name, definition, owning engine surface, and disqualifier criteria.

**`[DOC] PRODUCT — MVP vs Beta vs Scale Feature Matrix`**
- **Objective:** Map the full feature surface across three lifecycle bands — MVP (P0 cohort validation), Beta (P1 Narrow Ship), Scale (Phase 5 Desk Full v2).
- **Why:** MOSCOW captures one shipping window; lifecycle bands make the *deferred* surface auditable for re-evaluation at each phase. Replaces the prior MOSCOW framing with a forward-compatible view.
- **Dependency:** Product Strategy Overview; Core Product Pillars; engine endpoint inventory.
- **Output:** Feature matrix MD — features × {MVP / Beta / Scale} × {endpoint backing / NEW SCOPE / Won't}.

**`[DOC] PRODUCT — Product Value Ladder`**
- **Objective:** Define the user-perceived value progression Free → Trader $79 → Desk Preview $399, expressed in *outcomes* (what the trader can do) not features.
- **Why:** Pricing experiments (Phase 2) need a stable outcome ladder to A/B against. Tier matrices express features; the ladder expresses why each tier exists.
- **Dependency:** MVP vs Beta vs Scale Feature Matrix; Core Product Pillars; ICP Definitions v1.
- **Output:** Value ladder MD — one outcome statement per tier + the proof point that earns the statement.

**`[RESEARCH] PRODUCT — Must-Have Features for First Paying Users`**
- **Objective:** Identify the *minimum* feature set the first 100 paying users (Trader $79) need to convert from Free → paid and not churn week-1.
- **Why:** P1 Narrow Ship is at risk of overscoping; this research bounds the Must bucket against actual willingness-to-pay rather than founder intuition.
- **Dependency:** Persona-fit interview tagging (ICP); Willingness-to-Pay Interview Framework (ICP NEXT); cohort week-1 feedback.
- **Output:** Must-have feature list MD — each feature mapped to its willingness-to-pay signal and the cohort evidence supporting it.

### NEXT

**`[DOC] PRODUCT — User Journey from Signup to First Value`**
- **Objective:** Map the end-to-end journey from "user lands on cohort landing page" → "user has experienced first gated signal in their journal", including failure paths and drop-off triggers.
- **Why:** Activation triggers (ICP NEXT) feed this; journey design exposes onboarding gaps before they cost retention. Phase-3 onboarding work depends on the journey map being locked.
- **Dependency:** Activation Triggers by Persona (ICP NEXT); Cohort-Product Readiness Checklist; engine endpoints.
- **Output:** Journey map MD — steps, expected duration per step, drop-off failure modes, metric per step.

**`[DOC] PRODUCT — Feature Prioritization Framework`**
- **Objective:** Define the framework (e.g., RICE / Cost-of-Delay / pillar-fit-weighted) used to score every new feature ask in P1+.
- **Why:** "Loudest voice" is the default prioritization mode under cohort feedback pressure; an explicit framework shifts decisions onto criteria.
- **Dependency:** Core Product Pillars; Product Strategy Overview.
- **Output:** Framework MD with scoring rubric + worked examples on three sample feature asks.

**`[RESEARCH] PRODUCT — Retention Drivers for Pro Traders`**
- **Objective:** Identify what keeps a serious self-directed trader using a tool past month 1 — vs the typical churn cliff in trader tools.
- **Why:** Retention model determines which Should-bucket items are actually critical (e.g., daily digest, journal extension) vs. nice-to-have. Without this, Should drifts into Must by inertia.
- **Dependency:** Persona-fit interview round (ICP); cohort week-2 feedback; v1 framework retention notes.
- **Output:** Retention drivers MD — top 3–5 drivers + recommendation for which P1 features support each driver.

**`[DOC] PRODUCT — Product Scope Guardrails`**
- **Objective:** Define the explicit "we will not build this in P1" guardrails — the disqualifier list for feature requests during P0/P1.
- **Why:** Phase 1 charter §2 has out-of-scope items at the strategy level; the *product* needs an operational version that the team can quote at request-time.
- **Dependency:** Product Strategy Overview; Phase 1 charter §2; MVP vs Beta vs Scale Feature Matrix.
- **Output:** Guardrails MD with disqualifier list + escalation path for genuine exceptions.

**`[QA] PRODUCT — Current Feature Surface vs Strategy Review`**
- **Objective:** Audit the currently-live product surface (dashboard, Telegram bot, scanner, signals UI, journal) against the locked Product Strategy Overview and Core Product Pillars; flag drift.
- **Why:** The product was built ahead of the locked Phase 1 strategy; this audit closes the loop and identifies any live feature that no longer fits.
- **Dependency:** Product Strategy Overview; Core Product Pillars; live product walkthrough.
- **Output:** Audit report; remediation backlog if any.

### LATER

**`[DOC] PRODUCT — Team and Fund Product Variant Concept`**
- **Objective:** Sketch the concept for the team / fund variant (Desk Full v2, Phase 5) — multi-seat, per-account isolation, custom thresholds, audit log.
- **Why:** Phase-5 charter input; pre-empts premature multi-seat sprawl in P1 and removes the Phase-5 startup cost.
- **Dependency:** Layla Phase-5 Pre-read (ICP LATER); Enterprise Buyer Readiness Notes (ICP LATER).
- **Output:** Concept MD; *no commitments* in P1.

**`[DOC] PRODUCT — Expansion Opportunities Beyond Core Trading Intelligence`**
- **Objective:** Catalogue opportunities adjacent to the core (e.g., risk-as-a-service API, audit-grade reporting, education) — *not* to commit, just to bound.
- **Why:** Phase-3+ input; bounds future scope discussion without committing. Prevents premature lock that closes Phase 5 doors.
- **Dependency:** Core Product Pillars; Adjacent Market Opportunities Beyond Futures (MARKET LATER).
- **Output:** Opportunities MD; *no commitments*.

---

## F. TRUST

### NOW

**`[DOC] TRUST — Trust Framework for CoinScopeAI`**
- **Objective:** One-pager defining CoinScopeAI's overall trust framework — anti-overclaim posture, evidence-led claims, visible risk controls, phased work, cohort proof. Reconciles Scoopy operating principles with public-surface needs.
- **Why:** Every TRUST task downstream references this. Without a framework, signals / copy / disclosures all freelance from first principles.
- **Dependency:** Scoopy custom-instructions; Core Positioning Statement v1 (POSITIONING); PCC v2 (locked).
- **Output:** Trust framework MD; signed.

**`[DOC] TRUST — Public Safety Messaging Rules`**
- **Objective:** Lock the rules for any public message that mentions safety, capital protection, risk gates, drawdown limits, or testnet status.
- **Why:** Safety messaging is the highest-stakes copy surface; an off-message safety claim damages trust faster than any other category. Anti-overclaim is non-negotiable here.
- **Dependency:** Trust Framework for CoinScopeAI; Risk-State Claim Allowance Matrix (RISK); POSITIONING Claim Language Guardrails.
- **Output:** Public safety messaging rules MD; pairs with required disclaimers and the canonical 5 risk tokens.

**`[DOC] TRUST — Real-Capital Gate Communication Strategy`**
- **Objective:** Define how the §8 Capital Cap (real-capital gate) is communicated to users, prospects, and the public — when it appears, what it says, when it changes.
- **Why:** §8 is a load-bearing trust feature in P0/P1 ("we will not let you ramp real capital until G1–G4 + §8 Phase 1 are open"). It must be loud, dateable, and verifiable, not buried.
- **Dependency:** PCC v2 + §8 Capital Cap; Risk-State Claim Allowance Matrix (RISK); Trust Framework for CoinScopeAI.
- **Output:** Communication strategy MD — surface map, copy variants per phase, banner / UI placement rules.

**`[DOC] TRUST — Product Claims Approval Checklist`**
- **Objective:** Operational checklist that any new public claim (marketing, product copy, social, press) must pass before going live — anti-claim list, methodology link, risk-state allowance, disclaimer pairing.
- **Why:** Anti-overclaim posture is only as strong as the enforcement mechanism. A checklist makes founder-level claim review repeatable and delegable.
- **Dependency:** POSITIONING Claim Language Guardrails (NEXT); Risk-State Claim Allowance Matrix (RISK); Public Safety Messaging Rules.
- **Output:** Approval checklist MD; integrated into copy review workflow.

**`[QA] TRUST — Public-Facing Trust Gap Review`**
- **Objective:** Audit every public-facing surface (coinscope.ai, docs, Telegram bot intro, X bio, LinkedIn, in-app onboarding) for trust gaps — claims without methodology links, missing disclaimers, soft-edged risk numbers, opaque vendor disclosure.
- **Why:** Trust gaps compound. The audit identifies them before paid acquisition activates the MVTS hard gate and before they cost cohort trust.
- **Dependency:** Trust Framework for CoinScopeAI; Public Safety Messaging Rules; existing surfaces walkthrough.
- **Output:** Trust gap audit report; remediation backlog.

### NEXT

**`[DOC] TRUST — Security and Reliability FAQ`**
- **Objective:** Public FAQ covering security model (no execution authority, testnet-first, gated real capital, exchange API key scope), reliability posture, vendor dependencies, incident handling.
- **Why:** Security & reliability are the first concerns of professional traders evaluating a tool that touches their account. An FAQ pre-empts repeat questions and signals operational maturity.
- **Dependency:** Trust Framework for CoinScopeAI; existing security architecture docs; Vendor / Dependency Disclosure.
- **Output:** Security & reliability FAQ MD; live page.

**`[DOC] TRUST — Transparency Page Requirements`**
- **Objective:** Define the requirements for the cohort transparency page — cohort cap (40), validation methodology, exit memo placeholder, real-time cohort status, update cadence.
- **Why:** Locks the content shape and update cadence of the cohort transparency page (a core MVTS item) so it is verifiable rather than aspirational.
- **Dependency:** Trust Framework for CoinScopeAI; Validation Phase Exit Memo template; cohort recruiting active.
- **Output:** Transparency page requirements MD; live page spec.

**`[DOC] TRUST — Risk Disclosure Draft`**
- **Objective:** Counsel-cleared Risk Disclosure document — plain-English version covering testnet phase, real-capital gate, exchange dependency, no investment advice, jurisdictional limits.
- **Why:** Foundational trust artifact; signed by every user at signup. Existing draft in `_data/legal/Risk_Disclosure_v0_DRAFT.md` needs counsel pass + cohort-recruit-checklist integration.
- **Dependency:** Counsel Brief v2; Trust Framework for CoinScopeAI; existing `Risk_Disclosure_v0_DRAFT.md`.
- **Output:** Counsel-cleared Risk Disclosure MD; live page; signature flow integrated.

**`[DOC] TRUST — Trust Signals Needed Before Paid Scaling`**
- **Objective:** Lock the list of trust signals that must be live and verifiable before paid acquisition is turned on (the MVTS hard gate, in operational form). Ratifies the seven-signal MVTS in `05-trust.md`.
- **Why:** This *is* the paid-acquisition floor. Without an explicit signed list, paid spend leaks before the floor is set.
- **Dependency:** Trust Framework for CoinScopeAI; existing Trust Signal Inventory v1 (in `05-trust.md`).
- **Output:** Signed MVTS one-pager; Decision Register entries Tr-1, Tr-2.

**`[OPS] TRUST — Incident Communication Workflow`**
- **Objective:** Operational workflow for incident comms — who detects, who decides public-or-internal, who writes, who approves, where it goes (status page, Telegram, X).
- **Why:** Incident comms speed and consistency is itself a trust signal. Without a workflow, every incident becomes ad-hoc and inconsistent — undercutting the trust posture.
- **Dependency:** Vendor Incident Comms Templates (RISK); Status Page provisioned; Real-Capital Gate Communication Strategy.
- **Output:** Incident comms workflow MD; lives in `_data/operations/`.

### LATER

**`[DOC] TRUST — Institutional Trust Package`**
- **Objective:** Sketch the trust package required for institutional buyers (small funds, Phase 5 Desk Full v2) — security questionnaire responses, audit reports, SOC 2 readiness narrative, exchange-relationship attestations.
- **Why:** Phase 5 input. Institutional buyers will demand a package; sketching it now bounds Phase-5 ramp time and influences which trust artifacts produce institutional value vs individual-trader value.
- **Dependency:** Trust Framework for CoinScopeAI; Enterprise Buyer Readiness Notes (ICP LATER).
- **Output:** Institutional trust package outline; *no commitments* in P1.

**`[DOC] TRUST — Third-Party Validation Roadmap`**
- **Objective:** Map the third-party validations (SOC 2, security audit, code audit, exchange-relationship attestations, performance audit) that compound trust over time.
- **Why:** Phase-3+ input. Validations have long lead times; deciding which to pursue (and when) requires planning ahead. Skipping the roadmap creates ad-hoc Phase-4 panic when fundraising / institutional buyers ask.
- **Dependency:** Trust Framework for CoinScopeAI; budget posture (Phase 4 fundraising).
- **Output:** Validation roadmap MD; sequenced plan; *no commitments* in P1.

---

## G. RISK

### NOW

**`[DOC] RISK — Business Risk Register v1`**
- **Objective:** Catalogue every material business risk facing CoinScopeAI in Phase 1 — operational, vendor, regulatory, market, reputational, financial, key-person, technical — with severity × likelihood scoring and mitigation owner per row.
- **Why:** Without a single risk register, attention is reactive (whatever broke last week). A v1 register gives leadership a defensible scan of what's likely vs catastrophic. The locked Phase 1 5-token table and PCC v2 §8 are *engine-layer* risk artifacts; this register is the *business-layer* artifact that sits next to them.
- **Dependency:** PCC v2; Vendor Failure Mode Mapping v1; Counsel Brief v2; Phase 1 charter §5 risks.
- **Output:** Risk register MD with severity × likelihood matrix + mitigation owner per row.

**`[DOC] RISK — Provider Dependency Risk Matrix`**
- **Objective:** Map every upstream provider (Binance USDT-M, CoinGlass, Tradefeeds, CoinGecko, Claude/OpenAI, Stripe, Telegram) against impact (engine, signals, billing, comms) and the mitigation posture per provider.
- **Why:** Provider-dependency risk is *the* dominant business risk for CSAI in P0/P1 (Binance is the only execution venue). Without an explicit matrix, dependency drift is invisible until it bites.
- **Dependency:** Vendor Failure Mode Mapping v1 (existing); Phase 1 charter dependency notes.
- **Output:** Provider dependency matrix MD; mitigation status per provider; stale-data detection rules.

**`[DOC] RISK — Operational Failure Scenario Map`**
- **Objective:** Map the canonical operational failure scenarios (engine outage, exchange outage, vendor degradation, signal-storm, single-account drawdown, account drift, key-person unavailable) with response playbooks.
- **Why:** Scenarios > generic risk language. A scenario map is what runbooks actually reference at 2am when something breaks.
- **Dependency:** Provider Dependency Risk Matrix; existing engine runbooks; PCC v2 §8 entry/exit conditions.
- **Output:** Scenario map MD; one playbook stub per scenario; cross-listed with TRUST Incident Communication Workflow.

**`[DOC] RISK — Exchange Outage Business Response Plan`**
- **Objective:** Define the *business-level* response when Binance USDT-M (the P0/P1 only venue) is degraded or fully out — comms cadence, refund posture, cohort retention play, status-page integration, paid-acquisition pause logic.
- **Why:** Exchange outage is the single highest-impact dependency event. The *business* response (comms, refunds, retention) sits alongside the *engineering* response (degrade, failover at P2). Without this plan, an outage produces ad-hoc decisions that cost trust.
- **Dependency:** Provider Dependency Risk Matrix; Real-Capital Gate Communication Strategy (TRUST); existing Vendor Failure Mode Mapping v1.
- **Output:** Exchange outage response plan MD; lives in `_data/operations/`.

**`[RISK] RISK — Product Promise vs Risk Exposure Review`**
- **Objective:** Walk every product promise (locked positioning sentence, plan comparison claims, Telegram bot replies, marketing copy, in-app onboarding) against the actual risk exposure the engine + vendors can deliver. Flag any promise the gates cannot uphold.
- **Why:** A promise the gates cannot uphold is a credibility crisis trigger. This review closes the loop between marketing, product, and engineering reality. Anti-overclaim posture is enforced here.
- **Dependency:** Core Positioning Statement v1 (POSITIONING); PCC v2; canonical 5 risk tokens; Provider Dependency Risk Matrix.
- **Output:** Promise vs exposure review report; remediation list; copy patches.

### NEXT

**`[DOC] RISK — Drawdown and Reputation Risk Framework`**
- **Objective:** Define the framework for handling drawdown events on real-capital accounts (post-§8 Phase 1) — what triggers public comms, what triggers cohort comms, what triggers private follow-up, who approves each level.
- **Why:** A drawdown event handled poorly publicly is a worse trust hit than the drawdown itself. Framework reduces ad-hoc decisions under pressure.
- **Dependency:** PCC v2 §8 (post-Phase-1 entry); canonical risk tokens; Real-Capital Gate Communication Strategy (TRUST); Incident Communication Workflow (TRUST).
- **Output:** Drawdown response framework MD; integrated with Incident Communication Workflow.

**`[DOC] RISK — Billing and Churn Risk Review`**
- **Objective:** Catalogue billing-side risks (failed payments, dispute rate, churn drivers, downgrade waves, refund posture, subscription fraud) and define mitigation policies.
- **Why:** Billing risk is invisible until ARR contracts; explicit cataloguing lets ops + finance pre-empt rather than react.
- **Dependency:** Stripe integration; PACKAGING Tier Structure (Phase 2 dependency — flagged); existing churn/billing telemetry.
- **Output:** Billing & churn risk review MD; policy suggestions; integrated into the Business Risk Register.

**`[DOC] RISK — Counterparty and Vendor Risk Policy`**
- **Objective:** Lock the counterparty and vendor risk policy — what we do *before* signing a new vendor, what we monitor, when we replace, contractual minimums (uptime SLAs, data export, exit clauses).
- **Why:** Phase 2 vendor expansion (CoinGlass, Tradefeeds, others) will pile up vendors quickly. A policy now prevents ad-hoc onboarding that creates tail-risk later.
- **Dependency:** Provider Dependency Risk Matrix; PCC v2 G2 vendor reliability gate.
- **Output:** Vendor risk policy MD; pre-signing checklist; ongoing monitoring rules.

**`[OPS] RISK — Risk Review Cadence`**
- **Objective:** Operationalize the risk review cadence — weekly (operational triage), monthly (register update), quarterly (board-level), annual (token review per `feedback_risk_threshold_reconciliation`).
- **Why:** A risk register that isn't reviewed decays into a static document. Cadence keeps it live and forces explicit re-affirmation of the 5 canonical tokens.
- **Dependency:** Business Risk Register v1; Provider Dependency Risk Matrix.
- **Output:** Cadence MD; calendar entries; review template per cadence level.

**`[METRICS] RISK — Leading Risk Indicators Dashboard`**
- **Objective:** Define and wire the leading indicators that *predict* a risk crystallizing — vendor latency drift, drawdown approach to gate, daily-loss approach to gate, dispute rate, churn rate, key-person availability flag.
- **Why:** Lagging indicators arrive too late for action. A leading-indicator dashboard is the difference between mitigation and reaction.
- **Dependency:** Business Risk Register v1; engine telemetry hooks; billing telemetry; cohort telemetry.
- **Output:** Indicator definitions MD; dashboard panel; alert thresholds.

### LATER

**`[DOC] RISK — Scale-Stage Risk Governance Model`**
- **Objective:** Sketch the risk governance model needed at scale (Phase 5+) — formal risk committee, board-level reporting, risk appetite statement, escalation matrix, founder-out scenario.
- **Why:** Phase 5+ governance is materially different from founder-led Phase 1; sketching now reduces the Phase 5 startup cost and forces clarity on what governance evolution looks like.
- **Dependency:** Business Risk Register v1; fundraising posture (Phase 4); team/headcount plan (Phase 4).
- **Output:** Governance model MD; *no commitments* in P1.

**`[DOC] RISK — External Audit Readiness Requirements`**
- **Objective:** Enumerate the audit-readiness requirements — security audit, code audit, financial audit, controls audit (SOC 2 Type 1, then Type 2), exchange-relationship attestations — and the prep work each demands.
- **Why:** Audit readiness has long lead times; deciding which audits to pursue (and when) requires planning ahead. Cross-listed with TRUST Third-Party Validation Roadmap.
- **Dependency:** TRUST Third-Party Validation Roadmap (LATER); Phase 4 fundraising posture.
- **Output:** Audit readiness requirements MD; sequenced plan; *no commitments* in P1.
