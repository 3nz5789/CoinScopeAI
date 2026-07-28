# Trust Framework

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/01-executive-summary/strategic-priorities.md` (Priority 3 anti-overclaim hold; Priority 8 testnet hard gate); `business-plan/04-icp-and-segmentation/primary-icp.md` §6 (P1 Omar trust requirements); `business-plan/08-go-to-market/trust-first-growth.md`

---

## 1. Trust principles for CoinScopeAI

Six principles. Each is a binding constraint on every operational and external-facing surface.

1. **Trust is observable behavior, not an asserted attribute.** A company that says "we're trustworthy" is suspicious by default. A company whose pricing page, error messages, postmortems, and refund handling all behave consistently with their claim is not.
2. **Restraint compounds; bravado decays.** A surface that consistently underclaims and over-delivers builds trust at compounding rates. The reverse breaks instantly on the first contradiction.
3. **Anti-overclaim is the moat.** What we will not say is more durable than what we say. Competitors can copy a feature; they cannot copy years of disciplined refusal to overclaim.
4. **Transparency at the methodology and operations layer.** Buyers who can read the engine logic, the validation status, the incident history, and the legal posture form trust faster than buyers who cannot.
5. **The founder is named, contactable, and consistent.** A named human with consistent voice across surfaces is a structural trust asset. Anonymous brand-mascot positioning is fragile in trust-sensitive trading.
6. **Trust velocity is the constraint on growth velocity.** Acquisition cannot scale faster than trust. Trying to invert this destroys both.

The synthesis: **trust is the daily output of operational discipline applied consistently across product, support, comms, and brand surfaces — not a marketing message overlaid on top.**

---

## 2. What trust means in this product category

Crypto-perp trading products live in a **structurally low-trust category**. Buyers have been pitched by signal services, copy-trade platforms, autonomous-bot operators, and "AI trading" wrappers — most of which overpromise and underdeliver. The default buyer mindset is skepticism, especially among the disciplined cohort CoinScopeAI targets.

For this category, trust has four observable components.

### 2.1 Methodology trust

> "Does the team actually understand the math?"

Built by:

- Public methodology page (`coinscope.ai/methodology`)
- Position-sizing math transparency in product
- Regime classifier logic documented
- R-multiple and rule-violation reporting in journal

Broken by: black-box claims; "secret algorithm"; refusal to disclose how the engine works.

### 2.2 Operational trust

> "Does the team handle problems competently when they arise?"

Built by:

- Vendor failure-mode runbooks (rehearsed pre-launch)
- Incident postmortems published transparently
- Status page with incident history visible
- SLAs that match what gets delivered (not aspirational)

Broken by: silent outages; deflected blame; missed SLAs without acknowledgment; vague "we're investigating" notes that never resolve.

### 2.3 Posture trust

> "Does the team's behavior align with their claims about themselves?"

Built by:

- Anti-overclaim discipline across every surface
- Validation-phase honesty pinned to every page
- "What we don't do" page enumerating non-claims
- US-blocked-at-signup honoring the regulatory posture they claim
- Founder named, sole-prop status disclosed honestly

Broken by: marketing that contradicts the technical caveats; "production-ready" claims while §8 is gated; performance numbers from testnet data; testimonials presented as endorsement.

### 2.4 Financial trust

> "Will the team handle my money / billing / refunds without arguing?"

Built by:

- 14-day money-back guarantee, honored without arguing per `07-packaging-and-pricing/trial-and-discount-policy.md` §5
- Pricing locks ≥6 months post-validation; no surprise repricing
- "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies" honesty about time-bounding
- No discount stacking schemes; clean billing math

Broken by: surprise renewal price hikes; refund disputes; unclear billing; founder-cohort framed as permanent then later contradicted.

The four components reinforce each other. A failure in one degrades the others; a strength in one supports the others. **None can be skipped because the buyer's evaluation pattern checks all four.**

---

## 3. Trust signals the company should build

Trust signals are **observable, not asserted**. Each has a public surface or operational artifact.

### 3.1 Top-priority signals (must exist before P1 launch)

| # | Signal | Surface | Why critical for P1 |
|---|---|---|---|
| **TS-A** | Public methodology page | `coinscope.ai/methodology` | The entry point for credibility; P1 Omar reads it during evaluation |
| **TS-B** | "What we don't do" reference | `coinscope.ai/what-we-dont-do` | Anti-claim disclosure as continuous trust signal |
| **TS-C** | Production Candidate Criteria v2 published | `coinscope.ai/pcc-v2` (or equivalent) | Makes the validation-phase posture verifiable |
| **TS-D** | Validation-phase footer on every paid surface | "Testnet only. 30-day validation phase. No real capital." | Anti-overclaim discipline visible on every page |
| **TS-E** | Status / uptime page | `coinscope.ai/status` | Operational transparency baseline |
| **TS-F** | About page with named founder, sole-prop disclosure | `coinscope.ai/about` | Founder visibility; honest entity posture |
| **TS-G** | API-key safety language at exchange-connect | "Read-only scopes; withdrawal scope never requested" | Trust at the highest-friction onboarding gate |
| **TS-H** | Anti-overclaim audit pass on every shipping surface | Brand-voice review log | Operational guarantee against claim drift |
| **TS-I** | 14-day money-back guarantee | Pricing page + trial-and-discount-policy | Financial-trust baseline |
| **TS-J** | Risk Disclosure visible at signup | Signup flow + pricing surfaces | Counsel-aligned posture honesty |

### 3.2 Secondary signals (build during P1; mandatory by P2)

| # | Signal | Surface |
|---|---|---|
| **TS-K** | First incident postmortem published transparently | `coinscope.ai/postmortems` (or status page entry) |
| **TS-L** | Vendor failure-mode runbook dry-run executed and documented | Internal record + future external excerpt |
| **TS-M** | First weekly cohort observation note published (anonymized, no performance language) | Substack or company blog |
| **TS-N** | First persona reconfirmation publication (post-§3.7 interviews) | Methodology section + decision log |
| **TS-O** | Decision log entry for every phase advance | `business-plan/_decisions/decision-log.md` mirror published |

### 3.3 Tertiary signals (build at P2 / P3 — not blocking)

| # | Signal |
|---|---|
| **TS-P** | Quarterly cohort summary published (anonymized) |
| **TS-Q** | Founder POV op-eds in methodology-aligned outlets |
| **TS-R** | Public roadmap with deferral status visible |
| **TS-S** | First external audit / brand-voice peer review |
| **TS-T** | Counsel sign-off documents linked from legal posture page |

---

## 4. Product trust vs. operational trust vs. brand trust

Three trust layers, each with different building mechanisms and different decay risks.

### 4.1 Product trust

> "The product behaves the way the team says it does."

Built by:

- Code-level testnet hard gate verified in CI (per Strategic Priority 8)
- Risk-gate thresholds enforced exactly at user-configured values (no "default override" surprises)
- Math transparency: position-sizing shows inputs and outputs that match the user's hand calculation
- Engine status / uptime visible
- Test-and-simulation lab regression coverage on signal, gate, regime logic

Decays when: the product deviates from documented behavior; bugs are silent; gates fire at system defaults rather than user-configured thresholds (per `04-icp-and-segmentation/primary-icp.md` §8 churn trigger 1).

### 4.2 Operational trust

> "The team operates the product responsibly when things go wrong."

Built by:

- Defined coverage hours, met consistently
- Severity matrix triage executed correctly
- Vendor incidents communicated within minutes
- Postmortems published transparently
- Refunds honored without arguing within the 14-day window
- Decision log discipline (every phase advance recorded)

Decays when: incidents go silent; SLAs are missed without acknowledgment; refund disputes; postmortems are delayed or sanitized.

### 4.3 Brand trust

> "The team's external claims are calibrated to what they can deliver."

Built by:

- Anti-overclaim discipline across every surface
- Restraint in marketing language; locked phrasing list
- Validation-phase honesty pinned everywhere
- "What we don't do" disclosure
- No leaderboards, no testimonials presented as endorsement, no performance language

Decays when: a single overclaim ships unreviewed; "production-ready" appears before §8 passes; copy drifts during launch pressure; affiliate / influencer arrangements introduce voice discontinuity.

### 4.4 The interaction

The three layers are **multiplicative, not additive**. Strong product trust + strong operational trust × broken brand trust = collapse. The cohort sees the contradiction and discounts the product trust correspondingly.

That is why Wave 1 places anti-overclaim discipline (Priority 3) on equal footing with validation pass (Priority 1) and testnet hard gate (Priority 8). All three are existential.

---

## 5. How testnet-first and gating can strengthen trust if communicated well

The validation-phase posture is **not a marketing problem to solve around** — it is a marketing asset, when communicated correctly. Per `08-go-to-market/gtm-strategy.md` §5, three principles:

### 5.1 Lead with the gate, not despite it

Every product surface includes "Testnet only. 30-day validation phase. No real capital." Buyers who reject the framing self-select out (anti-ICP filter); buyers who accept it self-select in (ICP confirm).

### 5.2 Reframe the gate as a quality signal

Acceptable copy:

- *"We will not market the engine as production-ready until our published Production Candidate Criteria pass."*
- *"Capital preservation is the default. Real-capital deployment is gated by criteria, not by our willingness to ship."*
- *"You can run the engine on Binance Testnet today. Real-capital deployment opens through a phased ramp once §8 Capital Cap evidence accumulates."*

Unacceptable copy:

- ~~*"Going live soon!"*~~ — signals impending unsupported claims
- ~~*"Beta = production once you trust it"*~~ — undermines the gate
- ~~*"Testnet results indicate real-capital potential of X%"*~~ — performance promise from non-production data

### 5.3 Make the gate path visible

The product publishes:

- The Production Candidate Criteria v2 (`coinscope.ai/pcc-v2`)
- The §8 Capital Cap and phased-ramp framework, in user-readable summary
- The Validation_Phase_Exit_Memo template, made public when filed
- The decision log entry for any phase advance

Visibility is the differentiator. Most competitors hide their readiness state. CoinScopeAI publishes it. **That itself is the trust signal.**

---

## 6. Trust gaps likely to exist today

Operational reality check — gaps that exist or are likely to exist as P1 approaches. Each is paired with a fix priority.

### 6.1 Likely high-priority gaps (must close before P1 launch)

| # | Likely gap | Why critical | Fix priority |
|---|---|---|---|
| **G1** | Status / uptime page may not be live | TS-E baseline | Pre-P1 |
| **G2** | "What we don't do" page may not exist as a standalone surface | TS-B baseline | Pre-P1 |
| **G3** | Production Candidate Criteria v2 may not be publicly accessible (vs. internal) | TS-C baseline | Pre-P1 |
| **G4** | Validation-phase footer may not be on every surface (e.g., pricing page) | TS-D baseline | Pre-P1 |
| **G5** | About page may not name founder explicitly with sole-prop disclosure | TS-F baseline | Pre-P1 |
| **G6** | Exchange-connection step may not surface "no withdrawal scope ever" copy | TS-G baseline; trust-critical | Pre-P1 |
| **G7** | Refund flow may not be Stripe-clean at v1 (refund requires manual founder action vs. self-serve cancel) | Financial trust; honoring 14-day money-back without friction | Pre-P1 |
| **G8** | Incident comms templates may not exist (this folder closes the gap) | Operational trust at first incident | Pre-P1 |

### 6.2 Likely medium-priority gaps (close during P1)

| # | Likely gap | Fix priority |
|---|---|---|
| **G9** | Vendor failure-mode runbook dry-run not executed | P1 first 30 days |
| **G10** | Brand-voice audit log not maintained (every external surface change tracked) | P1 first 30 days |
| **G11** | Decision log mirror not publicly accessible (currently internal only) | P1 mid-cohort |
| **G12** | First persona reconfirmation publication not yet drafted | P1 close (Jul 2026) |

### 6.3 Likely lower-priority gaps (close at P2)

| # | Likely gap | Fix priority |
|---|---|---|
| **G13** | Counsel sign-off documents not linked from legal posture page | P2 |
| **G14** | Public roadmap surface not yet polished | P2 |
| **G15** | Quarterly cohort summary cadence not yet established | P2 close |

The gaps are addressed at the priorities listed; not all need to close pre-P1, but G1–G8 must.

---

## 7. Trust-building priorities

Top 10 priorities, ranked by **trust impact × earliest fixable date**. Cross-references the locked Strategic Priorities in `01-executive-summary/strategic-priorities.md`.

| Rank | Priority | Trust component | Owner | Window |
|---|---|---|---|---|
| **1** | Pass PCC v2 G1–G4 + §8 Capital Cap criteria honestly | Posture + product | Founder | P0 (May 2026) |
| **2** | Hold the line on anti-overclaim across every shipping surface | Brand | Founder + brand-voice review | Continuous |
| **3** | Maintain testnet-only discipline with code-level hard gate verified in CI | Product + posture | Founder | Continuous through P0–P5 |
| **4** | Publish Production Candidate Criteria v2 + Validation_Phase_Exit_Memo template | Posture | Founder | Pre-P1 |
| **5** | Publish "what we don't do" + about + status pages | Posture + operational | Founder | Pre-P1 |
| **6** | Stand up incident comms templates (this folder) + first vendor runbook dry-run | Operational | Founder | Pre-P1 + P1 first 30 days |
| **7** | Honor 14-day money-back without arguing for first refund request | Financial | Founder | First 30 days post-launch |
| **8** | Publish first incident postmortem transparently | Operational | Founder | First incident |
| **9** | Run §3.7 persona reconfirmation interviews; publish persona-reconfirmation note | Methodology + posture | Founder | P1 mid-cohort |
| **10** | First public quarterly cohort summary (anonymized, no performance language) | Brand + posture | Founder + brand review | P2 close |

---

## 8. Validation discipline — how trust is tested

Trust is tested at four moments during P1–P2. Each moment is an explicit checkpoint:

| Moment | What's tested | Pass criterion |
|---|---|---|
| **P1 launch (2026-06-01)** | Pre-launch trust signals (TS-A through TS-J) live | Pre-launch checklist clear; brand-voice audit pass |
| **First incident** | Incident comms timeliness; postmortem honesty | Comms within 15 min for P1; postmortem within 7 days |
| **First refund request** | Financial trust holds | Refund processed within 24h of request, no arguing |
| **P2 public launch (Aug–Sep 2026)** | Anti-overclaim discipline holds under launch pressure | Brand-voice audit pass on every launch surface |
| **First overclaim attempt** (likely from contractor or unconscious drift) | Brand discipline holds | Caught at brand-voice review; not shipped |

If any test fails, the corresponding trust component takes a hit and the recovery action documented in `04-icp-and-segmentation/primary-icp.md` §8 applies. Trust is recoverable on first occurrence handled openly; cumulative if pattern emerges.

---

## 9. Cross-references

- Strategic priorities: `business-plan/01-executive-summary/strategic-priorities.md`
- Primary ICP trust requirements: `business-plan/04-icp-and-segmentation/primary-icp.md` §6, §8
- Trust-first growth: `business-plan/08-go-to-market/trust-first-growth.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications: `business-plan/13-support-and-trust-ops/incident-communications.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Brand messaging: `business-plan/09-brand-messaging.md`
- Risk / compliance / trust: `business-plan/12-risk-compliance-trust.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
