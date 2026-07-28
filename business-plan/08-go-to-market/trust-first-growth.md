# Trust-First Growth

**Status:** Wave 2 · v1.1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/07-gtm-strategy.md` §4 (six trust commitments); `business-plan/09-brand-messaging.md`; `01-executive-summary/strategic-priorities.md` Priority 3 (anti-overclaim hold); `business-plan/13-support-and-trust-ops/public-claims-guardrails.md` (canonical anti-overclaim audit)
**Changelog v1 → v1.1:** §2 consolidated against the now-canonical `public-claims-guardrails.md` (was a parallel restatement); §7 trust signals reconciled with `gtm-strategy.md` §6 PP1–PP8 (was a renumbered duplicate); §3 / §4 restructured to remove topic-taxonomy duplication; §5.6 close phrased less absolutely; §1 Principle 1 verb fix; §3.1 channel terminology fix; voice-tic line removed; new §9 trust-decay protocol, §10 word-of-mouth amplification, §11 founder-bandwidth callout.

---

## 1. Trust-building growth principles

Six principles. Each is a binding constraint on every external claim, every channel decision, and every acquisition tactic.

1. **Earned visibility before paid visibility.** No paid channel activates until the underlying credibility is earned by published evidence (PCC v2 pass, cohort signal, incident handling). Trust cannot be bought; it can only be **amplified** after it is earned.
2. **Restraint is the message.** The buyer specifically rewards companies that exhibit restraint about what they claim, what they sell, and what they refuse to do. Restraint is the differentiator, not a marketing handicap.
3. **Founder visibility, not founder hype.** A named founder, contactable, with consistent voice across surfaces, is a trust asset. A founder positioned as a "guru" or "alpha-source" is a trust liability and undermines the product's positioning.
4. **Methodology disclosure as trust accelerant.** What competitors hide (their analytical logic, their failure modes, their not-yet-shipped capabilities), CoinScopeAI publishes. Transparency at the methodology layer compounds faster than any marketing investment.
5. **Operational integrity as marketing.** A clean incident postmortem published openly does more for trust than any paid placement could. Ops *is* marketing for a trust-sensitive trading product.
6. **Trust scales slower than acquisition; honor that.** A funnel that pulls 10x users in 60 days produces cohort signal that does not justify the acquisition velocity. Acquisition velocity is a function of trust velocity, not the other way around.

The synthesis: **growth at CoinScopeAI is the visible compound of earned trust signals, not the result of acquisition optimization.** Trying to invert this — optimizing acquisition to "scale" the trust — is the most reliable way to destroy both.

---

## 2. Anti-overclaim — GTM-surface applications

The canonical allowed-claim and forbidden-claim catalog lives in **`13-support-and-trust-ops/public-claims-guardrails.md`** (with `09-brand-messaging.md` and §6.10 as upstream sources). The pricing-page-specific applications live in `07-packaging-and-pricing/pricing-strategy.md` §9. This section covers GTM-surface-specific applications — the surfaces that don't sit on the pricing page but ship under the GTM motion.

### 2.1 Launch announcement (P2 public launch, single coordinated event)

- Validation-phase footer visible (per §6.10 + brand-voice review)
- "Production-ready" framing **forbidden** unless §8 passes AND counsel-reviewed (per `public-claims-guardrails.md` §3.2)
- "Going live next week / soon / imminently" **forbidden** — timeline-driven readiness claims
- One ≤25%/≤30-day promo permitted per `07-packaging-and-pricing/trial-and-discount-policy.md` §6; framing must include end-date and post-revert price
- Counsel + brand-voice review pass before publication

### 2.2 Founder POV op-eds (1 per quarter in methodology-aligned outlets)

- Methodology-grounded; never thought-leader puff; never sponsored
- No performance language even when adapted to host's audience tone
- Author byline names founder explicitly (Mohammed); never ghost-written or anonymized
- Brand-voice review pass before submission to host

### 2.3 Cohort observation summaries (quarterly, anonymized)

- Anonymized; **no per-user numbers, no aggregate return figures** — structural patterns only (rule-respect rate, retention bands, edge cases observed)
- Performance language **forbidden** even framed as "cohort observation" (per `public-claims-guardrails.md` §4.4)
- Counsel-cleared anonymization standard (CA-14 in `14-risk-compliance-and-safeguards/compliance-assumptions.md`)
- Brand-voice review before publication

### 2.4 Conference talks / podcast appearances (P3+ on invitation)

- Same brand-voice rules as written content
- Founder-named delivery; never delegated under voice-incongruent representation
- No paid speaking spots; no sponsored placements
- Talk-deck passes brand-voice review before recording

### 2.5 Substack / longform content (continuous cadence)

- Every post passes brand-voice review before publication
- Topics drawn from §4 approved taxonomy; novel angles require additional review
- No cross-posting to anti-channel venues per `channel-prioritization.md` § anti-channels

### 2.6 Telegram alert templates

- Canonical payload per Scoopy custom instructions: signal + regime + confidence + gate result + validation-phase footer
- Template changes pass brand-voice review (alerts are at-scale surfaces; copy drift compounds quickly)

A surface in any of the categories above that fails the canonical guardrails (per `public-claims-guardrails.md` § allowed/forbidden) is rejected at brand-voice review and not shipped.

---

## 3. Credibility-building motions

Six repeatable motions that compound trust over time. Cadence and mechanics here; topic taxonomy in §4.

### 3.1 Methodology longform (Substack — channel C1)

- **Cadence:** 1 deep post / 1–2 weeks during P0–P1; sustained at 1–2 / month through P5
- **Time per post:** ~4–6 founder hours including draft + brand-voice review
- **Engagement venues for distribution:** Quant-focused communities on X (engagement threads, not aggregator cross-posts); selective participation in closed methodology Discords (per `channel-prioritization.md` C3); founder Substack subscriber list
- **Not used:** mass-market subreddits (per `channel-prioritization.md` AC3); influencer cross-promotion (anti-channel)
- **Brand-voice review:** every post, before publication

### 3.2 Public methodology and reference pages (channel C4)

Five canonical surfaces:

- `coinscope.ai/methodology` — engine logic documented
- `coinscope.ai/what-we-dont-do` — explicit anti-claim list, in user-readable form
- `coinscope.ai/pcc-v2` (or equivalent) — Production Candidate Criteria v2 published
- `coinscope.ai/status` — uptime + vendor incident history
- `coinscope.ai/roadmap` — public roadmap with deferral status (P5 Desk Full v2 explicit)

Refresh quarterly; update at every phase advance with a decision-log entry.

### 3.3 Incident postmortems

- Every incident severity ≥ medium produces a postmortem (per `13-support-and-trust-ops/incident-communications.md` §5.5)
- Postmortem is published — not hidden in a status page footnote
- Format: incident summary; root cause; user-facing impact; mitigation deployed; learnings; runbook updates
- Founder-authored at v1; contractor-authored under brand-voice review at v2+

### 3.4 Founder POV / op-ed presence (channel C6)

- 1 founder POV piece per quarter in a methodology-aligned outlet
- Topics align with the methodology longform but adapted to host's audience
- Never paid placement; never sponsored
- ~6–8 founder hours per piece (≈0.5 hr/week amortized)

### 3.5 Cohort observation publication (anonymized, quarterly)

- First quarterly summary publishes post-S2 close; thereafter each quarter through P5
- Anonymized; no performance language; no leaderboards
- Format: cohort size; retention bands; rule-respect rate; what surprised us; what's next
- Brand-voice + counsel-anonymization-standard review before publication

### 3.6 Legal-posture surfaces with public change-logs

The legal documents (No Investment Advice memo, Risk Disclosure, ToS, Privacy Policy) are prerequisites, not credibility-building motions. The **motion** is publishing change-logs whenever any of these documents updates — material updates surface as a status-page entry or a methodology-page note, not as a silent push. Sole-prop status remains honestly disclosed on the about page through every update.

These six motions are the engine. Their compounding effect over 12–18 months is what scales acquisition — not paid channels, not influencer deals, not leaderboards.

---

## 4. Content and education topic taxonomy

Topic angles, ranked by trust-compounding effect for a P1-Omar-shaped reader. Example post titles included as calibration anchors; not commitments to publish those exact titles.

### 4.1 Strongest trust angles (default-allowed; brand-voice review only)

| Angle | Example post title |
|---|---|
| **Methodology transparency** | "How CoinScopeAI's regime classifier picks Trending vs. Mean-Reverting (and where it's wrong)" |
| **Anti-claim explanations** | "Why we don't show you a win-rate percentage" |
| **Math transparency** | "Position sizing under heat: the formula, the inputs, the failure modes" |
| **Validation-phase honesty** | "What §8 Capital Cap actually requires before we deploy real capital" |
| **Vendor reasoning** | "Why our P1 vendor stack is narrow on purpose — and what changes at P2" |
| **Operational discipline** | "Inside our incident-response runbook for a vendor outage" |

### 4.2 Strong-with-caveat angles (brand-voice review + caveat language)

| Angle | Caveat / required handling |
|---|---|
| **Anonymized cohort observation summaries** | No performance language; no leaderboards; structural patterns only. Same anonymization standard as §3.5. The "Day in the life of a P1 cohort user" framing belongs here, with the same rules. |
| **What we shipped, what we didn't** | Documented quarterly; tied to public roadmap; deferral status named explicitly |
| **Vendor incident postmortems published broadly** (vs. status page only) | Honest about what failed and why; no vendor-blame language per `incident-communications.md` §4.2 |

### 4.3 Risky angles (brand-voice + counsel review required)

| Angle | Why risky |
|---|---|
| **Comparative methodology pieces** (vs. CoinGlass, Nansen, etc.) | Direct competitor naming carries legal exposure; methodology-only framing required, never feature-checklist marketing; counsel review of the named-competitor section |
| **"How [user X] uses CoinScopeAI"** | Testimonial-as-endorsement risk; only with explicit user consent + brand-voice + counsel review |
| **"Industry trends" pieces** | Drifts toward thought-leader / influencer voice; allowed only when methodology-grounded and not marketing-fluff |

The boundary between §4.2 and §4.3 is **competitor naming** and **identifiable users**. Anonymized cohort observation (§4.2) describes patterns without naming users. Comparative methodology (§4.3) names competitors. "Day in the life" (§4.2) is acceptable when fully anonymized; "How [user X] uses CoinScopeAI" (§4.3) names a user and requires their explicit consent plus counsel review.

### 4.4 Forbidden angles

- ~~"How [user X] made [Y%] using CoinScopeAI"~~ — performance claim with named user
- ~~"Top 5 setups our scanner caught this week"~~ — signal-group framing
- ~~"How to maximize leverage in a Trending regime"~~ — anti-positioning (capital-preservation default)
- ~~"Beat your benchmark with AI"~~ — performance claim
- ~~"What our most successful users have in common"~~ — selection-bias performance claim

---

## 5. How to avoid looking like a black-box trading promise

Crypto-trading products historically suffer from a black-box-promise pattern: "the algorithm wins, trust us, here are the (curated) winners." CoinScopeAI's surfaces continuously contradict this pattern. Six explicit guardrails:

### 5.1 The engine is documented, not hidden

The methodology page is **public regardless of tier** (per locked Phase 1 §5.3.1). Buyers can read the regime classification logic, the risk-gate math, and the vendor stack reasoning before they sign up. A black-box promise survives by hiding the inside; CoinScopeAI inverts this.

### 5.2 Confidence and gate-result are first-class on every signal

Every signal output carries:

- Symbol + direction + entry
- Regime label (Trending / Mean-Reverting / Volatile / Quiet)
- Confidence score
- Gate result (pass / rejected with explicit gate that fired)
- Validation-phase footer

A black-box says "buy now"; CoinScopeAI says "long BTC @ 67,420 — confidence 0.72 — regime Trending — gate pass — testnet only." The buyer sees the work.

### 5.3 The product enforces user-defined thresholds

Risk-gate thresholds are user-configurable above our locked floors. A black-box system tells the user what to do; CoinScopeAI enforces what the user has already decided. The buyer's discipline is the input.

### 5.4 No performance claims, ever

No win-rate, no ROI, no "average user" data. Cohort observation summaries are anonymized and structural. Performance language is not used in any external surface, regardless of how flattering the underlying data might be.

### 5.5 Limits-of-product disclosure is published

`coinscope.ai/what-we-dont-do` enumerates explicitly:

- We don't generate alpha
- We don't deliver signals as recommendations to act on
- We don't custody capital
- We don't execute autonomously without authorization
- We don't make performance promises
- We don't operate in the US until licensure decision

A black-box promises everything; CoinScopeAI publishes what it is not.

### 5.6 Founder is named and contactable

Mohammed is named on the about page, the methodology bylines, and the cohort-onboarding kickoff. A black-box hides authorship; CoinScopeAI puts a face on it. Buyers can email the founder; many do, especially early in evaluation.

The combined effect: **CoinScopeAI's surfaces continuously contradict the black-box pattern.** A single careless content moment can damage trust, but it cannot fully undo the cumulative effect — and an honest correction note (per `incident-communications.md` §4.7) restores the trajectory if drift is caught early.

---

## 6. Review and checkpoint process before scaling growth

Trust-first growth requires explicit checkpoints. Five, in order.

### 6.1 Brand-voice audit (continuous)

Before any external surface ships:

- The brand-voice enforcement skill (`business-plan/09-brand-messaging.md`) reviews the copy
- Any flagged claim returns to the author for revision
- Founder is the named approver for surface launches

Cadence: every external surface, every time. No exceptions. A "small tweak to the pricing page" passes brand-voice review the same way as a launch announcement.

### 6.2 Pre-launch readiness review (S1)

Before P1 cohort opens (per `08-go-to-market/launch-plan.md` §4):

- Pre-launch checklist closeout meeting
- Counsel sign-off on legal documents
- Anti-overclaim audit pass against every shipping surface
- Decision-log entry for the go decision

### 6.3 Mid-cohort review (Week 4 of P1)

- Cohort signal vs. assumptions check
- Persona reconfirmation status check
- Incident handling review
- Decision-log entry for any course corrections

### 6.4 P1 → P2 exit gate review (S2 → S3)

Per `business-plan/14-launch-roadmap.md` §14.1:

- 30-day soft-cohort floor met
- Zero §14 stop-the-line conditions triggered
- IB items at "stabilizing-acceptable" maturity
- Desk Preview at quality bar
- §3.7 persona reconfirmation completed (or in-flight with sufficient signal)
- Decision-log entry for the S3 advance

### 6.5 Paid acquisition trigger evaluation (S4 close, ≈M5+)

Before any paid channel activates (D1 trigger):

- Trader CAC validates at LTV/CAC ≥ 3:1
- Cohort retention parity to organic across signup-source segments
- Founder-led distribution carry hypothesis (BMA5 in `01-executive-summary/business-model-summary.md` §8) checked: are we still on a glide path to ~500 paid users without paid acquisition? If yes, defer further.
- Decision-log entry; counsel review of any compliance implications of the chosen channel

If any checkpoint fails, the corresponding stage holds.

---

## 7. Trust signals needed before paid acquisition

The 8 evidence proof points are PP1–PP8 from `08-go-to-market/gtm-strategy.md` §6 — referenced rather than restated to avoid drift. This file adds two GTM-trust-specific extensions.

| # | Trust signal | Evidence | Stage gate |
|---|---|---|---|
| **PP1–PP8** | Per `gtm-strategy.md` §6: PCC v2 pass; 40-user cohort onboarded; persona reconfirmation; 30-day retention threshold; vendor runbook dry-run; Desk Preview at quality bar; Trader CAC at LTV/CAC ≥ 3:1; first incident handled cleanly | Per the evidence sources named in `gtm-strategy.md` §6 | Per the stage gates named in `gtm-strategy.md` §6 |
| **TS-A** | Anti-overclaim audit pass on every P2-launch surface | Brand-voice review log clean across the launch surface set | S3 advance |
| **TS-B** | Five canonical public surfaces live and refreshed: methodology, what-we-dont-do, pcc-v2, status, roadmap | Live URLs; quarterly refresh log | S1 → S2 |

**Threshold cite for PP4 (30-day retention):** see `12-onboarding-and-activation/activation-milestones.md` § Free / Trader activation criteria — the operative thresholds are working assumptions and validate at P1 close.

**The lock:** **all 8 PP plus both TS extensions must hold (or be in flight with sufficient signal) before paid acquisition activates.** The default state is "deferred." Active state requires affirmative evidence, not absence of negative evidence.

---

## 8. What "scaling growth" actually means here

The phrase is ambiguous in startup vocabulary. CoinScopeAI's per-stage definition, with anti-pattern column to prevent stage-bleed of inappropriate tactics.

| Stage | What "scaling growth" means | What stays anti-pattern at this stage |
|---|---|---|
| **P0 (validation)** | Not applicable; no growth-scaling occurs in this stage | All paid acquisition; all influencer; all leaderboards; all public launch comms |
| **P1 (cohort)** | Filling the 40-user cohort with curated candidates. "Scaling" beyond 40 is anti-strategy | Public launch announcement; press blitz; paid acquisition; affiliate / referral programs; >40 cohort fill; Desk Full v2 in market |
| **P2 (public launch)** | Founder-cohort 60-day window; methodology cadence sustained; one launch promo (≤25%/≤30 days, never on Desk Full v2) | Paid acquisition; influencer marketing; affiliate revenue share; press blitz beyond one placement; Desk Full v2 in market |
| **P3 (stabilization)** | CAC validation work answers "can we afford to acquire users at this rate?". "Scaling" means *unblocking* paid channels if and only if PP7 holds | Influencer marketing; affiliate revenue share; co-marketing with anti-ICP products; mass-market crypto channels; Desk Full v2 in market |
| **P4 (Desk Full v2 prep)** | Founder-cohort recruitment for Desk Full v2 candidates; broader funnel still throttled | Same as P3 + Desk Full v2 in market (pre-launch) |
| **P5 (Desk Full v2 launch)** | Desk Full v2 cohort fill + Desk Preview migration. Per-seat density is the sensitivity to test | Influencer marketing; affiliate revenue share; mass-market crypto channels (continued); performance leaderboards from cohort data |
| **Post-P5** | Compounding the established motion + opening previously deferred channels (paid acquisition, conferences, partnership-led) only if their underlying trust signals continue to hold | Anti-ICP cross-promotion; performance leaderboards; affiliate revenue share without brand-voice review gate; abandoning anti-overclaim discipline under growth pressure |

The principle: **"scaling growth" is a different action at each stage, never a default action.** A growth move appropriate at one stage may be anti-strategy at another. The anti-pattern column is the structural commitment that doesn't relax as phases advance.

---

## 9. Trust decay protocol

Trust-building has a companion: trust decay. A growth strategy that addresses only building is incomplete. Three components.

### 9.1 Leading indicators of trust decay

Watch weekly during P1+; quarterly at minimum thereafter.

| Indicator | Where to watch | What it suggests |
|---|---|---|
| **Brand-voice review log entries growing faster than surface count** | Brand-voice review log + surface inventory | Drift accumulating; review process under stress |
| **Cohort referral rate declining** | Signup attribution capture (per §10) | Word-of-mouth amplification weakening; product or trust posture issue |
| **Substack engagement declining despite consistent cadence** | Substack analytics + comparable post performance | Audience drift, voice drift, or saturation |
| **Refund-reason capture trending toward "fit mismatch"** | Refund flow capture (per `07-packaging-and-pricing/trial-and-discount-policy.md` §7) | Onboarding promises diverging from product delivery |
| **Cohort feedback flagging anti-overclaim drift** | Cohort observation notes; cohort interviews | Brand-voice surface(s) drifted past review |
| **Support ticket sentiment shifting toward "this isn't what I expected"** | Support inbox triage tags | Onboarding-trust-promise gap |
| **"Production-ready" / performance-language phrases appearing in search results for our brand** | Quarterly external monitoring | A surface shipped without review, or a third-party article uses our brand with overclaim language |

A single indicator is monitored. Two or more concurrent indicators escalate the trust-decay status from Monitoring to Active per the §12 risk register conventions.

### 9.2 Recovery protocol when decay is detected

Five steps, sequenced.

1. **Slow the growth motion.** Pause the next launch surface; pause new channel additions; hold current cohort cadence rather than expanding.
2. **Increase brand-voice review cadence.** Every surface per pass; second-author review on launch-relevant surfaces; weekly review-log audit instead of monthly.
3. **Increase founder visibility.** More direct cohort touchpoints (founder check-ins on P1 cohort users); named-founder presence in the methodology cadence (vs. byline-only).
4. **Publish honest correction or acknowledgment** if the decay traces to a specific surface or claim — per `13-support-and-trust-ops/incident-communications.md` §4.7 (anti-overclaim drift incidents).
5. **Decision-log entry** per recovery action; trust-decay status tracked in the §12 risk register.

### 9.3 Unrecoverable categories (no recovery path inside the existing brand)

Some failures cannot be recovered through the §9.2 protocol. Treat these as existential:

- A real-capital incident before §8 passes (the brand-defining anti-overclaim moat is gone)
- A "production-ready" claim screenshotted by a credible competitor before §8 passes
- A pattern of overclaim drift compounding across multiple quarters (single instance is recoverable; pattern is not)
- A security incident handled with cover-up or deflection
- A confirmed pattern of testimonials presented as endorsement (single instance is recoverable; pattern is not)
- Founder-led trust posture broken by founder behavior outside the product (one-off addressable; pattern existential)

These connect to §12 R-001, R-013, R-027, and the anti-overclaim drift risk category. Recovery in these cases is a brand reset, not a continuity protocol — and that is well outside this folder's scope.

---

## 10. Word-of-mouth amplification

Founder-led, anti-affiliate, anti-influencer growth has only one channel that compounds without the deferred-channel risks: **organic peer referral.** This section makes the mechanism operational.

### 10.1 What counts as a referral signal

| Signal | Source |
|---|---|
| Peer-referral signup | Signup attribution: "How did you hear about us?" free-text or selectable origin |
| Substack mention with link | Substack analytics + manual quarterly scan |
| Closed-Discord recommendation traceable to a signup | Founder presence in Discord (per `channel-prioritization.md` C3) + signup attribution |
| Conference / podcast unprompted mention | External monitoring via brand search |
| Cohort user introduces a peer to the founder directly | Founder DM / email log |
| Methodology-page deep-link traffic from a private community | Referrer analytics + founder Discord context |

### 10.2 How to track

- **Signup-source attribution capture** in the signup flow — required pre-P1 (REQUIRED INPUT cross-references `12-onboarding-and-activation/activation-milestones.md` § instrumentation)
- **Monthly external brand-mention scan** — manual quarterly during P1; automated post-P2
- **Cohort interview question** during the §3.7 persona-reconfirmation interviews and weekly observation: "Have you mentioned CoinScopeAI to anyone in your network? What did you say?"
- **Substack analytics** for referral traffic spikes correlated with external mentions
- **Quarterly cohort summary** reports referral rate as one of the structural patterns (not a performance metric)

### 10.3 How to encourage without affiliate adjacency

The product itself is the encouragement. Specific mechanisms allowed:

- **Methodology content shareable on its own merits** — every Substack post is a referral surface for the audience that finds it
- **Founder responsiveness to cohort users** — direct email / Discord interaction with cohort users (per §3.6 founder visibility motion)
- **Quarterly cohort summary publication** — cohort sees their cohort referenced; gives them something to share
- **Explicit anti-affiliate stance** — buyers tell their peers BECAUSE there's no affiliate. The absence of a referral-economic incentive is itself a trust signal

### 10.4 What is forbidden as referral mechanism

Per `07-packaging-and-pricing/trial-and-discount-policy.md` § discount-policy guardrails and `channel-prioritization.md` § anti-channels:

- ~~Affiliate revenue share~~ (locked off at P1–P2; revisit only post-P5 with brand-voice review gate)
- ~~Referral codes for discounts~~ (locked off; would create affiliate-class economics)
- ~~"Refer 3 friends, get free Pro" campaigns~~ (forbidden — `public-claims-guardrails.md` §3.3)
- ~~Public testimonials presented as endorsement~~ (forbidden unless explicit user consent + brand-voice + counsel review)
- ~~Compensated cohort-user advocacy of any form~~ (compensated advocacy is an affiliate adjacency)

---

## 11. Founder-bandwidth callout

Trust-building is built into the 12–22 hours/week GTM cap from `channel-prioritization.md` §5, not added on top.

| Activity | Hours / week (P1) | Hours / week (P2+) |
|---|---|---|
| Methodology longform (Substack, channel C1) | 4–6 (1 post per 1–2 weeks × ~5 hrs/post) | 2–3 (1–2 posts/month) |
| Quant-community engagement (Twitter / X, channel C2) | 2–4 | 2–4 |
| Closed Discord participation (channel C3) | 2–4 | 2–4 |
| Methodology + reference page refresh (channel C4) | <1 (quarterly amortized) | <1 |
| Cohort recruitment outreach (channel C5) | 4–8 (P1 ramp, then taper) | 1–2 (Desk Preview opportunistic) |
| Brand-voice review on shipping surfaces | 0.5–1 | 0.5–1 |
| Founder POV op-ed prep (channel C6) | 0.5 (amortized quarterly) | 0.5 |
| Quarterly cohort summary | <0.5 (one quarter only) | 0.5 |
| Incident postmortem authoring | Variable; ~4–8 hrs / incident | Variable |

**P1 baseline total:** ≈14–24 hrs/week — at the upper edge of the cap. The implication: trust-building cadence is **the** GTM activity during P1; there is no founder time for paid-acquisition planning, partnership outreach, or non-priority work without displacing trust-building.

This is the structural rationale for D1 paid-acquisition deferral and the D-series Strategic Priority deferrals: they are not just commercial choices, they are the only way the founder-time budget closes. Inverting this — adding paid-acquisition planning to the P1 founder week — burns the trust-building cadence the next 12 months of acquisition depend on.

---

## 12. Cross-references

- §7 v1 LOCKED canonical: `business-plan/07-gtm-strategy.md`
- §9 Brand and messaging: `business-plan/09-brand-messaging.md`
- §6.10 Anti-overclaim audit (upstream): `business-plan/06-pricing-monetization.md` §6.10
- §14 v1 LOCKED launch roadmap: `business-plan/14-launch-roadmap.md`
- Anti-overclaim canonical (Wave 2): `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications: `business-plan/13-support-and-trust-ops/incident-communications.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Validation Phase Exit Memo template: `business-plan/_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- GTM strategy: `business-plan/08-go-to-market/gtm-strategy.md`
- Channel prioritization: `business-plan/08-go-to-market/channel-prioritization.md`
- Launch plan: `business-plan/08-go-to-market/launch-plan.md`
- Activation milestones (threshold source): `business-plan/12-onboarding-and-activation/activation-milestones.md`
- Trial / discount policy (referral mechanism boundaries): `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
