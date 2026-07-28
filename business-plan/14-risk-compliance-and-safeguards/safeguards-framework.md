# Safeguards Framework

**Status:** Wave 2 · v1.1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`; `business-plan/14-launch-roadmap.md` v1 LOCKED (stop-the-line conditions); `business-plan/12-risk-compliance-trust.md` v1 LOCKED; `business-plan/13-support-and-trust-ops/public-claims-guardrails.md` v1.1 (canonical anti-overclaim); `business-plan/13-support-and-trust-ops/incident-communications.md` (canonical incident severity / response flow)
**Changelog v1 → v1.1:** B-S6 leaderboards/benchmarks corrected to "Never relax" matching the permanent-forbidden status in `public-claims-guardrails.md` §3.1; P-S4 wording inversion fixed (now "less conservative than locked floors"); P-S4 unblock condition corrected to "Never relax" matching NR-5; B-S2 pricing-lock unblock condition disambiguated to `Validation_Phase_Exit_Memo` anchor; P-S6 moved to §2.4 Proposed safeguards; Class column added to §2 tables (Standard / Structural / Proposed); §6 restructured to route severity/response to `incident-communications.md` as canonical and own only safeguard-specific recovery actions; §7 NR list re-organized into three categories (absolute-no-unblock / unblock-path-documented / governance-protected); §3.3/§3.4/§3.5 cleanup; §4/§5 overlap collapsed (§5 owns the per-axis checklist; §4 narrative cross-references); new §9 Monitoring cadence, §10 Decay protocol, §11 Dependency map, §12 Exception register, §13 Contractor onboarding, §14 Cost stack.

---

## 1. Safeguard philosophy

Six operating beliefs.

1. **Safeguards are gating, not ceremony.** A safeguard that is not actually a stop-condition is theater. Every safeguard in this file has a specific event it blocks until it clears.
2. **Hard gates beat soft gates.** Structural enforcement at multiple layers (testnet hard gate at engine level; US-block multi-layer at signup — IP detection + KYC declaration + ban-and-refund flow) is stronger than policy-level enforcement (founder commitment). Where structural enforcement is possible, use it.
3. **Pre-commit, don't improvise.** Safeguards work because they are committed before the situation arises. Improvising under launch pressure or incident pressure produces the failure mode the safeguard exists to prevent.
4. **Scale the moat, don't relax it.** As the company grows, safeguards add layers (counsel review, brand-voice audit, contractor onboarding gates, postmortem cadence). They do not loosen because growth pressure mounts.
5. **Document the unblock condition for every gate.** A gate without a defined unblock condition is a permanent block. The unblock condition makes the gate operational, not aspirational.
6. **Safeguards apply to the founder too.** The discipline is universal. Founder cannot self-authorize bypassing a gate; the unblock condition is the path.

The synthesis: **safeguards are the operational implementation of the validation-phase posture.** They make "we don't claim production-ready until §8 passes" something the company can actually do, week after week, against pressure.

---

## 2. Three layers — business / product / operational safeguards

CoinScopeAI's safeguards split into three layers. Each layer has different enforcement mechanisms and different failure modes.

**Class column:**
- **Standard** — live safeguard, relaxable via documented unblock condition
- **Structural** — live safeguard flagged in §7 NR list as not relaxable under any phase pressure
- **Proposed** — not yet implemented; tracked for future activation (see §2.4)

### 2.1 Business safeguards

> Decisions about positioning, pricing, channels, claims, and growth.

| Safeguard | What it blocks | Unblock condition | Mechanism | Class |
|---|---|---|---|---|
| **B-S1 Anti-overclaim discipline** | Forbidden claims (§3 in `public-claims-guardrails.md`) shipping on any external surface | Brand-voice review pass per `13-support-and-trust-ops/public-claims-guardrails.md` §8 | Brand-voice skill + founder approval | **Structural** (NR-2) |
| **B-S2 Pricing locks ≥6 months post-validation** | Surprise reprice mid-cycle | 6 months elapsed after `Validation_Phase_Exit_Memo` filed (P0 exit gate clearance) + decision-log review | Founder discipline + decision log | Standard |
| **B-S3 Founder-cohort time-bounding** | "Lifetime" / "forever" / "permanent" framing | Locked language only — never relax | Brand-voice review + decision log | Standard |
| **B-S4 No paid acquisition before PP7 trigger** | Channel activation before Trader CAC validates at LTV/CAC ≥ 3:1 | Per `gtm-strategy.md` §6 PP7 | D1 deferral + brand-voice review | Standard |
| **B-S5 No anti-ICP cross-promotion** | Co-marketing with signal groups, copy-trade, leverage maximizers | Never relax | `06-pricing-monetization.md` §5.3.3 lock + decision log | Standard |
| **B-S6 No leaderboards / public benchmarks** | Performance promise from any data source (testnet or post-§8) | **Never relax** — performance language is permanently forbidden per `public-claims-guardrails.md` §3.1, regardless of validation status | Anti-overclaim discipline + brand-voice review | Standard |
| **B-S7 No affiliate / referral revenue share at P1–P2** | Affiliate-driven discount classes; referral economics | Post-P5, only with brand-voice review gate | Decision log + brand-voice | Standard |
| **B-S8 Counsel review before public-facing legal claims** | "Institutional-grade" usage; "no investment advice" framing in marketing | Counsel sign-off | Counsel engagement + decision log | Standard |
| **B-S9 Strategic Priority deferrals D1–D12** | Premature work on Bybit, mobile app, Arabic UI, etc. | Per-deferral trigger condition | Founder discipline + Strategic Priorities review | Standard |
| **B-S10 Single canonical decision log** | Parallel decisions outside the log | Never relax | Decision log discipline | **Structural** (NR-8) |

### 2.2 Product safeguards

> Code-level and engine-level enforcement.

| Safeguard | What it blocks | Unblock condition | Mechanism | Class |
|---|---|---|---|---|
| **P-S1 Code-level testnet hard gate** | Real-capital deployment beyond §8 phased ramp | PCC v2 G1–G4 + §8 Capital Cap pass; phased-ramp activation per documented criteria | Code-level + CI verification + Strategic Priority 8 | **Structural** (NR-1) |
| **P-S2 US-block at signup** | US-resident account creation | US licensure decision + counsel sign-off | Multi-layer geo-detection (IP + KYC declaration) + ban-and-refund flow | **Structural** (NR-3) |
| **P-S3 Read-only API scopes only** | Withdrawal scope ever requested at exchange-connection | Never relax | Hard-coded scope request; manual security review on any change | **Structural** (NR-4) |
| **P-S4 Locked risk-gate floors** | User configurations less conservative than the locked floors (DD > 10%, daily loss > 5%, leverage > 10x, max positions > 5, heat > 80%) | **Never relax** — floors are structural commitments to capital preservation | Engine-level enforcement + CI regression tests | **Structural** (NR-5) |
| **P-S5 Engine kill switch on user-level threshold breach** | Trades arming when user thresholds violated | Always active (no relax condition) | Engine-level enforcement | Standard |
| **P-S7 Cohort-level drawdown halt** | Continued operation when cohort drawdown exceeds §8 thresholds | Investigation + root-cause + decision-log entry | §13.4 monitoring + §14 condition 1 | Standard |
| **P-S8 Sub-$5k disciplined "we'll be back" routing** | Upgrade pressure on sub-$5k accounts | Account size crosses $5k threshold | Account-level routing | Standard |
| **P-S9 Single-account ceiling on Trader tier** | Multi-account use without Desk Preview subscription | Tier upgrade | Account-count check at exchange-connect | Standard |
| **P-S10 Validation-phase footer on every paid surface** | Surface ships without disclaimer | §8 pass + counsel-reviewed disclaimer revision (footer copy changes, not removed) | Brand-voice review + design system | **Structural** (NR-6) |

### 2.3 Operational safeguards

> Process- and ops-level enforcement.

| Safeguard | What it blocks | Unblock condition | Mechanism | Class |
|---|---|---|---|---|
| **O-S1 Pre-launch checklist closeout** | P1 cohort opening before all pre-launch items clear (per `08-go-to-market/launch-plan.md` §4) | Founder + counsel sign-off | Pre-P1 readiness review meeting | Standard |
| **O-S2 Vendor failure-mode runbook drill cadence** | P1 launch without rehearsed incident response; ongoing drift | Pre-P1 dry-run completed + quarterly drill thereafter (per `incident-communications.md` §8) | Strategic Priority 5 + per-quarter calendar | Standard |
| **O-S3 Severity-driven SLA matrix** | Tickets handled by tier alone (vs. severity); a Free user with a P1 incident waiting for paid-tier triage | Locked policy; never relax | Support workflow | **Structural** (NR-7) |
| **O-S4 Incident comms within 15 min for P1 / 30 min for P2** | Silent vendor outages | Locked timing; never relax | Status page + email + Telegram (alerts) | Standard |
| **O-S5 Postmortem within 7 days for severity ≥ medium** | Incident closure without published postmortem | Locked cadence; never relax | Trust framework + decision log | Standard |
| **O-S6 Brand-voice review on every external surface** | Surface ships without review log entry | Brand-voice skill in production + founder approval | Per-surface audit log per `public-claims-guardrails.md` §8.5 | Standard |
| **O-S7 Decision-log entry per phase advance** | Phase advance without decision-log entry | Founder discipline | §14 phase exit gate | Standard |
| **O-S8 Quarterly documentation audit** | Founder-only knowledge gaps blocking emergency-contact handover | Audit completed + gaps closed | Per-quarter review | Standard |
| **O-S9 Refund processed within 24h of request** | Refund-dispute escalation patterns | Locked SLA; never relax for first refund | Stripe-clean refund flow | Standard |
| **O-S10 Counsel news subscription** | Regulatory drift unnoticed | Continuous monitoring | Counsel engagement | Standard |

### 2.4 Proposed safeguards (not yet active)

Future safeguards tracked here so they don't get listed inline as if they were live. Each has an implementation trigger.

| Proposed safeguard | What it would block | Implementation trigger | Status |
|---|---|---|---|
| **P-S6 Code-level anti-claim guard** | Forbidden claim phrases shipping in product strings (build-time check on user-facing strings) | P3+ when contractor brand-voice review begins; reduces post-publication detection burden | REQUIRED INPUT — design at P3 start |
| **O-S11 Automated pricing-page audit** | Pricing-page changes shipping without anti-overclaim audit log entry | P3+ when surface change frequency increases | REQUIRED INPUT — design at P3 start |
| **B-S11 Quarterly safeguards-attestation review** | Safeguards drifting from "documented" to "not actually enforcing" | P2 close — formalize the verification cadence in §9 | REQUIRED INPUT — schedule at P2 close |

---

## 3. Gating logic relevant to CoinScopeAI's current maturity

Gates that determine when CoinScopeAI can advance to a more aggressive operating posture. Each is a hard gate with a documented unblock condition.

### 3.1 Real-capital gate (P-S1 + Strategic Priority 8)

| Gate | Status | Unblock condition |
|---|---|---|
| **Real-capital deployment beyond §8 Capital Cap phased ramp** | **Blocked at code level** | PCC v2 G1–G4 + §8 Capital Cap criteria pass + `Validation_Phase_Exit_Memo` filed + decision-log entry |

This is the most important gate in the entire framework. **It does not relax under launch pressure, fundraising pressure, or cohort pressure.** The unblock condition is the path; there are no other paths.

### 3.2 US-residents gate (P-S2)

| Gate | Status | Unblock condition |
|---|---|---|
| **US-resident signup** | **Blocked at signup** | Strategic Priority Deferral D2 — US licensure decision + counsel sign-off; not before P5 |

### 3.3 Public-launch gate (`launch-plan.md` S2 → S3)

| Gate | Status | Unblock condition |
|---|---|---|
| **P2 public launch announcement** | **Blocked until S2 exit gate clears** | 30-day soft-cohort floor + zero §14 stop-the-line + IB items at "stabilizing-acceptable" maturity + Desk Preview at quality bar + §3.7 persona reconfirmation **completed** (per `gtm-strategy.md` §6 PP3) |

### 3.4 Paid acquisition gate (D1 + PP7)

| Gate | Status | Unblock condition |
|---|---|---|
| **Paid acquisition channel activation** | **Deferred per D1** | Per `gtm-strategy.md` §6 PP7 (Trader CAC validates at LTV/CAC ≥ 3:1; cohort retention parity to organic; ≈M5+) |

### 3.5 Desk Full v2 launch gate (P5 phase advance)

| Gate | Status | Unblock condition |
|---|---|---|
| **Desk Full v2 in market** | **Blocked until P5** | P4 capability flow: items advance from RM (Roadmap) → IB (In-Build) → VTN (Validated/Tested/Nominated). Specifically, multi-account dashboard, audit-grade reporting, and role-based seats must reach VTN. Plus counsel review of v2 audit-grade reporting language. (Lifecycle taxonomy per `06-product-strategy/feature-prioritization.md`.) |

### 3.6 Entity restructure gate (Strategic Priority 6)

| Gate | Status | Unblock condition |
|---|---|---|
| **Priced equity raise / vendor master-services contract / full-time hire** | **Blocked until post-validation entity decision** | Counsel-recommended entity (DMCC FZE / mainland LLC / other) + restructure plan documented |

### 3.7 Phase advance gate (§14)

| Gate | Status | Unblock condition |
|---|---|---|
| **Any phase advance (P0 → P1 → P2 → P3 → P4 → P5)** | **Gate-driven, not calendar-driven** | Per-phase exit gate criteria met + decision-log entry filed |

The cardinal rule: **a gate without a documented unblock condition is a permanent block; a gate with one is a path.** Both are valid; ambiguous "we'll see" is not.

---

## 4. Threshold-event narrative — when expansion is anti-strategy

Two threshold events that, if approached without specific safeguards in place, are anti-strategy. The actual checklists live in §5 (per-axis); this section is the high-level framing.

### 4.1 Before any expansion of monetization

(Desk Preview funnel optimization, paid promo, expansion pricing, founder-cohort window changes.)

The required safeguards-in-place set is per-axis-pricing per §5.2 plus the cohort-evidence checks below:

- Trader cohort retention ≥ assumed threshold at 30 days; at 90 days
- First refund handled within 24h
- First incident handled with public postmortem
- Brand-voice audit log clean over the 30-day window
- §3.7 persona reconfirmation completed
- Zero §14 stop-the-line triggers in the relevant window

### 4.2 Before any expansion of growth motion

(Paid acquisition, conferences, partnership-led, channel additions.)

The required safeguards-in-place set is per-axis-channels per §5.3 plus the trust-evidence checks below:

- Trader CAC validates at LTV/CAC ≥ 3:1 (PP7)
- Vendor failure-mode runbook dry-run executed (PP5)
- Cohort retention parity to organic across signup-source segments
- Anti-overclaim audit pass on every shipping surface
- Counsel-cleared launch announcement copy
- Counsel review of any partnership-driven contractual language
- First persona reconfirmation publication shipped

The principle: **safeguards must be earned before they are spent.** Monetization and growth expansions are spend-events on accumulated trust. If the trust isn't accumulated, the expansion damages the moat instead of cashing it in.

---

## 5. Per-axis pre-commit checklists

Each is a pre-commit review before the change ships. §4 narrative threshold-events cross-reference these.

### 5.1 Before expanding claims

- [ ] Brand-voice review pass on every claim being added or revised
- [ ] Anti-overclaim audit against `13-support-and-trust-ops/public-claims-guardrails.md` § forbidden claims
- [ ] Counsel review of any claim that touches advisory, automation, or institutional-grade language
- [ ] Validation-phase footer still visible on the surface (for paid surfaces and signup; not all surfaces — social-tier posts use different framing per `public-claims-guardrails.md` §1.1)
- [ ] Decision-log entry recording the change

### 5.2 Before expanding pricing

- [ ] Pricing-lock window (≥6 months post-validation) confirmed expired (anchor: `Validation_Phase_Exit_Memo` filed + 6 months) OR change documented as exception with decision-log + counsel review
- [ ] Founder-cohort framing still time-bounded; no "lifetime" drift
- [ ] Anti-stacking enforcement still working
- [ ] §3.7 persona reconfirmation supports the change
- [ ] Counsel review if the change touches refund or jurisdictional language
- [ ] Decision-log entry recording the change

### 5.3 Before expanding channels

- [ ] D1 paid-acquisition trigger conditions met (if paid channel) per `gtm-strategy.md` §6 PP7
- [ ] Founder-led capacity check (founder time available without competing with priority work; cross-reference §14 cost stack)
- [ ] Anti-ICP filter still in place at signup
- [ ] Brand-voice review on channel-specific copy
- [ ] No anti-channel breach (signal groups, copy-trade, leverage maximizers, influencer)
- [ ] Decision-log entry recording the channel-mix change

### 5.4 Before expanding product scope

- [ ] Phase exit gate from current phase satisfied
- [ ] Engine readiness verified at the new tier (e.g., audit-grade reporting at P5)
- [ ] Anti-overclaim audit on any new product surface
- [ ] Counsel review of any new tier's user-facing language
- [ ] Vendor stack stability verified (vendor expansion at P2 only after P1 stable)
- [ ] Decision-log entry recording the scope expansion

### 5.5 Before expanding geography

- [ ] Counsel review of jurisdictional posture (UAE primary, MENA expansion, EU/UK readiness)
- [ ] US-block enforcement still active
- [ ] If expansion includes specific GCC jurisdictions (KSA, Bahrain, Oman): cross-border VAT obligations reviewed
- [ ] Counsel sign-off on any jurisdiction-specific marketing
- [ ] Decision-log entry recording the expansion

---

## 6. Escalation logic when safeguards are breached

Severity, comms timing, and response flow for any incident are canonical in **`13-support-and-trust-ops/incident-communications.md` §2–§4**. This section names the **safeguard-specific recovery actions** — what to do AFTER the incident response is in motion.

When a safeguard breaks: route severity + first-response per `incident-communications.md` first; then apply the recovery action below per the safeguard category.

### 6.1 Code-level safeguard breach (P-S1, P-S2, P-S3, P-S4, P-S5)

> A code-level enforcement is bypassed or fails.

- **Severity / comms:** P1 per `incident-communications.md` §2.6 (product incident) + §2.5 if security implication
- **Safeguard-specific recovery:** Engine-level kill switch immediate; CI regression test added; counsel notification if real-capital exposure; retest all related code-level safeguards in the same release cycle (P-S1 / P-S3 / P-S4 share enforcement layer)
- **Trigger:** §14 stop-the-line condition 5 (engine bug) + decision-log entry; verification-status reset on all code-level safeguards in §10

### 6.2 Anti-overclaim breach (B-S1, B-S3, B-S5, B-S6, B-S7, P-S10)

> A forbidden claim ships on a public surface.

- **Severity / comms:** P2 (single instance) → P1 (pattern) per `incident-communications.md` §2.7 (anti-overclaim drift)
- **Safeguard-specific recovery:** Brand-voice review process hardened (e.g., automated content scanning before publish; second-author review; revert-pre-publish); §13 contractor onboarding refresh if a contractor-authored surface is involved; brand-voice review log entry per `public-claims-guardrails.md` §8.5
- **Trigger:** Single instance → review-process hardening; pattern (>1/quarter) → stop-the-line review; if pattern persists, escalates to §14 stop-the-line condition for brand-discipline failure

### 6.3 Compliance-assumption failure (CA-1 through CA-18)

> Counsel determines an assumption is wrong.

- **Severity / comms:** P2 → P1 depending on scope of dependent business decisions; surface comms per `incident-communications.md` §4.7 (anti-overclaim drift category) if it affects a public claim; per `incident-communications.md` §4.5 (security) if it affects a privacy claim
- **Safeguard-specific recovery:** Affected business decisions rolled back or modified; affected risk register entries escalated; public surfaces amended; CA-# status moved from "Pending" to "Validated as wrong" or "Conditional"; downstream files (`pricing-strategy.md`, `trust-first-growth.md`, etc.) audited for assumptions touching the failed CA
- **Trigger:** §14 stop-the-line condition 3 (regulatory event) if the failure is regulator-classification

### 6.4 Operational safeguard breach (O-S1 through O-S10)

> A process safeguard fails (e.g., incident comms delayed past 15 min; postmortem missed; brand-voice review skipped).

- **Severity / comms:** P2 (single instance) → P1 (pattern) per `incident-communications.md` §2.6
- **Safeguard-specific recovery:** Operational gap documented; immediate corrective action; process hardening — if pattern, ops capacity review (e.g., support hire trigger per `support-operating-model.md` §9; contractor audit cadence reset per `public-claims-guardrails.md` §8.6); verification-status reset on the breached safeguard in §10
- **Trigger:** Single instance → review; pattern → support / ops capacity adjustment

### 6.5 Phase-advance gate breach

> A phase boundary is crossed without exit-gate evidence.

- **Severity / comms:** P1; comms internal until phase reverted
- **Safeguard-specific recovery:** Phase reverted; decision-log entry corrected; affected business decisions paused; founder review of the phase-gate process for the structural failure that allowed the breach
- **Trigger:** §14 — phase advance discipline is structural

### 6.6 Strategic Priority deferral breach (D1–D12)

> Work begins on a deferred priority without trigger condition met.

- **Severity / comms by deferral category:**
  - **D1 (paid acquisition), D2 (US user signup unblock), D6 (copy-trading)** → **P2** (capital efficiency / compliance / structural-positioning risk)
  - **D3, D4, D5, D7–D12** → **P3** (capacity risk only)
- **Safeguard-specific recovery:** Work paused; capacity reallocated to priority work; decision-log entry; deferral re-affirmed or re-evaluated against `01-executive-summary/strategic-priorities.md`
- **Trigger:** Founder discipline + Strategic Priorities monthly review

---

## 7. Not-relaxable safeguards — three categories

Eight specific safeguards must not relax under launch pressure, growth pressure, or cohort pressure. They are flagged **Structural** in §2's Class column and re-listed here with explanatory copy and the three-category taxonomy.

The taxonomy matters because not all "structural" safeguards relax the same way:

### 7.1 Absolute structural — no documented unblock path

These cannot relax under any circumstance during validation phase. There is no procedure that opens them.

| # | Safeguard | Why it cannot have an unblock path |
|---|---|---|
| **NR-4** | Read-only API scopes (P-S3) | Withdrawal scope creates trust collapse irreversibly. No business case justifies the request, ever. |
| **NR-5** | Locked risk-gate floors (P-S4) | Floors are the structural commitment to capital preservation. Less-conservative defaults undermine the entire positioning. |

### 7.2 Documented unblock path — relaxable only via the named procedure

These can change, but only via a specific (non-decision-log-only) procedure that the company has committed to in advance.

| # | Safeguard | Unblock procedure |
|---|---|---|
| **NR-1** | Code-level testnet hard gate (P-S1) | PCC v2 G1–G4 + §8 Capital Cap pass; phased-ramp activation per documented criteria; counsel sign-off |
| **NR-3** | US-block at signup (P-S2) | US licensure decision + counsel sign-off (Strategic Priority Deferral D2; not before P5) |
| **NR-6** | Validation-phase footer on every paid surface (P-S10) | §8 pass + counsel-reviewed disclaimer revision (the footer copy changes; the footer itself does not get removed without that review) |

### 7.3 Governance-protected — relaxable via decision-log + counsel

These can have specific exceptions, but every exception requires its own decision-log entry plus counsel review. The default state is locked.

| # | Safeguard | What "exception" looks like |
|---|---|---|
| **NR-2** | Anti-overclaim discipline (B-S1) | A specific approved-list extension (new approved claim category) requires brand-voice review + counsel + decision-log entry — not a relaxation of the overall discipline |
| **NR-7** | Severity-driven SLA matrix (O-S3) | A specific severity reclassification on a single ticket is allowed via founder review; the matrix itself does not relax. A Free user with a P1 incident still gets P1 response. |
| **NR-8** | Single canonical decision log (B-S10) | Corrections / updates to a prior entry require new entries (the discipline is preservation of history, not perfection). The discipline itself never relaxes. |

### 7.4 What this means in practice

- The founder cannot self-authorize relaxing **any** of NR-1 through NR-8 alone. NR-1, NR-3, NR-6 require the documented unblock procedure. NR-2, NR-7, NR-8 require decision-log + counsel review for any exception. NR-4, NR-5 don't relax at all.
- Verification status of all 8 NR safeguards is a quarterly review item in §9.
- Any breach of an NR safeguard escalates to §14 stop-the-line review per §6.

---

## 8. Safeguard layering at maturity

How the safeguard set evolves across phases. Present tense for the current phase (P0); future tense for upcoming phases.

| Phase | Window | Safeguards layered |
|---|---|---|
| **P0 (current — May 2026)** | Active | All v1 safeguards live; pre-launch checklist in closeout; brand-voice enforcement skill in production |
| **P1 (Jun–Jul 2026)** | Upcoming | Severity-driven SLA matrix in production (O-S3); vendor failure-mode runbook dry-run executed (O-S2); cohort observation cadence active; first incident postmortem template in use |
| **P2 (Aug–Sep 2026)** | Upcoming | First persona reconfirmation publication shipped; first quarterly cohort summary template in use; counsel review on launch announcement copy; one-promo-per-year discipline locked |
| **P3 (Oct–Dec 2026)** | Upcoming | Brand-voice review hardening (if drift pattern emerges); CAC validation feeds into D1 unblock evaluation; second voice (contractor) onboarded under brand-voice audit (per `public-claims-guardrails.md` §8.6); proposed safeguards (P-S6, O-S11, B-S11) implementation begins |
| **P4 (Jan–Feb 2027)** | Upcoming | Second engineering contractor onboarded under documentation audit; Desk Full v2 audit-grade reporting language under counsel review |
| **P5+ (Mar 2027+)** | Upcoming | Per-seat ToS / addendum live; Desk Full v2 audit-grade reporting in production; channel-mix lock revisited; entity-restructure (per Strategic Priority 6) implemented |

The safeguards **do not loosen** as phases advance. They add layers (counsel touch points, contractor audit, postmortem cadence, persona reconfirmation, proposed-safeguard implementations). The layering is the maturity progression.

---

## 9. Safeguard monitoring cadence

Safeguards drift from "documented" to "not actually enforcing" without periodic verification. This section names the cadence per layer.

### 9.1 Business safeguards — review cadence

| Cadence | Activity |
|---|---|
| **Weekly (during P1)** | Brand-voice review log audit (founder reviews each prior-week entry per `public-claims-guardrails.md` §8.5) |
| **Monthly** | Decision-log audit (every new entry referenced against the safeguards it touches); Strategic Priority deferrals D1–D12 status review |
| **Quarterly** | Pricing-lock window status; founder-cohort framing audit on live surfaces; anti-ICP cross-promotion scan |

### 9.2 Product safeguards — verification cadence

| Cadence | Activity |
|---|---|
| **Per release (CI)** | P-S1 testnet hard gate verified uncircumventable; P-S3 read-only scope check; P-S4 floor-violation regression test; P-S5 kill-switch unit test |
| **Quarterly synthetic-attack tests** | P-S1 — attempt real-capital deployment in testnet env (must fail); P-S2 — US-IP user agent at signup (must block); P-S3 — withdrawal-scope request (must reject); P-S4 — DD > 10% configuration attempt (must reject) |
| **Per phase advance** | P-S7 cohort drawdown halt monitoring active; P-S8 sub-$5k routing check on live signups; P-S10 validation-phase footer audit on every paid surface |

### 9.3 Operational safeguards — drill cadence

| Cadence | Activity |
|---|---|
| **Weekly (during P1)** | Incident comms timing report (O-S4); refund SLA actuals (O-S9) |
| **Monthly** | SLA matrix actual-vs-target review (O-S3); decision-log entry per phase-advance check (O-S7) |
| **Quarterly** | Vendor failure-mode runbook drill (O-S2); documentation audit (O-S8); counsel news scan (O-S10) |

### 9.4 Verification log

Every verification activity above produces a log entry in **`business-plan/_data/safeguard-verification-log.md`** (REQUIRED INPUT — file to be created pre-P1) with fields: safeguard ID, verification type, date, outcome (pass / fail / observed-drift), founder approver, follow-up action if applicable.

---

## 10. Safeguard-decay protocol

A safeguard that hasn't been verified for >quarter risks "in-place drift" — documented but not actually enforcing.

### 10.1 Verification-status discipline

Each safeguard in §2 carries a (notional, tracked in `_data/safeguard-verification-log.md`) **last-verified date** updated per §9 cadence.

### 10.2 Stale-verification triggers

| Stale-status condition | Action |
|---|---|
| Code-level safeguard not CI-verified in >2 releases | Add CI test to next release; flag as P3 ops issue if not added |
| Synthetic-attack test missing for >1 quarter | Schedule next quarterly cycle |
| Operational drill missing for >1 quarter | Schedule next quarterly cycle (per Strategic Priority 5) |
| Brand-voice review log not audited in >2 weeks (during P1) | Founder calendar block immediate audit |

### 10.3 Stale-status escalation

If a safeguard's last-verified date exceeds 2x its expected cadence, the safeguard's class temporarily downgrades from Standard → Stale until verification completes. NR-flagged safeguards that go stale escalate to §14 stop-the-line review.

---

## 11. Safeguard-dependency map

Safeguards depend on each other. A failure in one cascades to others. This section names the primary dependencies.

### 11.1 Brand-voice dependency cluster

```
B-S1 (anti-overclaim discipline)
  ↓ depends on
O-S6 (brand-voice review on every external surface)
  ↓ depends on
public-claims-guardrails.md §8.5 brand-voice review log artifact
```

If `_data/brand-voice-review-log.md` doesn't exist or isn't audited, B-S1 / O-S6 / P-S10 / B-S3 / B-S6 all degrade.

### 11.2 Code-level safeguard cluster

```
P-S1 testnet hard gate ←→ P-S3 read-only scopes ←→ P-S4 locked floors
  All depend on engine-level enforcement + CI verification
```

If CI verification is skipped on a release, all three code-level safeguards may regress simultaneously. §6.1 recovery action specifies retesting all related safeguards.

### 11.3 Incident comms cluster

```
O-S4 (incident comms within 15 min) → O-S5 (postmortem within 7 days) → §10 verification-status of breached safeguards
```

If O-S4 fails (silent vendor outage), O-S5 doesn't fire, the postmortem is missing, the breached safeguard's verification status isn't updated.

### 11.4 Pricing-lock cluster

```
B-S2 (pricing locks) ←→ B-S3 (founder-cohort time-bounding) ←→ B-S6 (no leaderboards)
  All depend on brand-voice review (B-S1) + founder discipline
```

A breach in B-S3 (founder-cohort framing drifts to "lifetime") tends to co-occur with B-S2 surface drift (pricing copy hints at structural reprice) — they fail together.

### 11.5 Implication

**Primary cascading-failure pathways** (a single root failure that takes out multiple safeguards):

- Brand-voice review log not maintained → B-S1, O-S6, P-S10, B-S3, B-S6 all degrade
- CI verification skipped → P-S1, P-S3, P-S4 simultaneously regress
- Founder bandwidth exhausted (per §14) → O-S6 review skipped → cascade above

These are the failure modes the verification log (§9.4) and the cost stack (§14) exist to detect early.

---

## 12. Safeguard-exception register

Some safeguards must be temporarily relaxed under specific circumstances (e.g., emergency security patch ships before brand-voice review of the announcement; counsel approves a one-time partnership exception). The general decision log captures these but a dedicated exception register makes them retrievable.

### 12.1 Artifact

**Location:** `business-plan/_data/safeguard-exception-register.md` (REQUIRED INPUT — file to be created at the first exception, or pre-P1 as a placeholder).

### 12.2 Schema per entry

- Exception ID (E-NNN, sequential)
- Safeguard affected (B-S#, P-S#, O-S#, NR-#)
- Date of exception
- Reason
- Approver (founder; counsel if applicable; brand-voice review if applicable)
- Duration (start date → end date, or "until decision-log entry resolves")
- Decision-log entry link
- Outcome / resolution
- Follow-up review date (when the safeguard returns to default status)

### 12.3 Access

- Founder: read-write
- Counsel: read-only on request
- Contractors: read-only within their scope

### 12.4 Cadence

- Founder reviews open exceptions weekly
- Quarterly audit of resolved exceptions for pattern detection

### 12.5 What does NOT go in the exception register

- Routine decision-log entries that don't relax a safeguard
- Standard unblock-path advances (e.g., post-§8 pass on NR-1 — that's a procedure, not an exception)
- Brand-voice review approvals (those go in the brand-voice review log per `public-claims-guardrails.md` §8.5)

---

## 13. Contractor safeguard onboarding

When contractors join (P3+ brand-voice contractor; P4 engineering contractors; P3+ support contractor), they need to understand which safeguards apply to their work. Per-contractor-type subset:

### 13.1 Brand-voice contractor (P3+)

Applicable safeguards:

- **B-S1** Anti-overclaim discipline (primary responsibility)
- **B-S3** Founder-cohort time-bounding
- **B-S6** No leaderboards / public benchmarks
- **B-S7** No affiliate / referral revenue share
- **P-S10** Validation-phase footer on every paid surface
- **O-S6** Brand-voice review on every external surface
- **NR-2** Anti-overclaim discipline (governance-protected)
- **NR-6** Validation-phase footer (structural with documented unblock path)

Onboarding docs: `public-claims-guardrails.md` (full read); this file §2.1 + §7; brand-voice review log artifact (`public-claims-guardrails.md` §8.5).

### 13.2 Engineering contractor (P4+)

Applicable safeguards:

- **P-S1** Code-level testnet hard gate (primary responsibility)
- **P-S3** Read-only API scopes only
- **P-S4** Locked risk-gate floors
- **P-S5** Engine kill switch
- **P-S6** Code-level anti-claim guard (when implemented)
- **P-S7** Cohort-level drawdown halt
- **NR-1** Testnet hard gate (structural with unblock path)
- **NR-4** Read-only API scopes (absolute structural)
- **NR-5** Locked risk-gate floors (absolute structural)

Onboarding docs: this file §2.2 + §7; PCC v2; CI verification cadence in §9.2; design-system manifest.

### 13.3 Support contractor (P3+)

Applicable safeguards:

- **O-S3** Severity-driven SLA matrix (primary responsibility)
- **O-S4** Incident comms within 15 min for P1 / 30 min for P2
- **O-S5** Postmortem within 7 days for severity ≥ medium
- **O-S9** Refund processed within 24h of request
- **NR-7** Severity-driven SLA (governance-protected)

Onboarding docs: `support-operating-model.md`; `incident-communications.md`; this file §2.3 + §7.

### 13.4 Universal contractor onboarding (all roles)

- **B-S10** Single canonical decision log (NR-8)
- **B-S5** No anti-ICP cross-promotion
- Anti-overclaim discipline awareness (cross-functional)

---

## 14. Safeguard cost stack

Each safeguard has an enforcement cost. Without surfacing the total stack, founder bandwidth (12–22 hr/week per `08-go-to-market/channel-prioritization.md` §5) is consumed without visibility.

### 14.1 Estimated weekly founder hours per safeguard (P1)

| Safeguard | Cost | Notes |
|---|---|---|
| **B-S1 / O-S6 Brand-voice review on every external surface** | 0.5–1 hr/week | At P1 surface change cadence; scales with frequency |
| **B-S2 / B-S3 / B-S6 Pricing-lock + founder-cohort + leaderboards discipline** | <0.25 hr/week (passive) | Active only on pricing-page changes |
| **B-S4 / B-S9 Strategic Priority deferral discipline** | 0.5 hr/week (monthly review amortized) | |
| **B-S10 Decision log discipline** | 0.5 hr/week | Per phase-advance and major-decision entries |
| **P-S1–P-S4 Code-level safeguards (CI verification)** | <0.25 hr/week (automated CI) | Quarterly synthetic-attack tests add ~2 hr/quarter ≈ 0.15 hr/week |
| **O-S2 Vendor runbook drill (quarterly)** | ~0.3 hr/week (4 hr/quarter amortized) | |
| **O-S3 / O-S4 / O-S5 SLA + incident comms** | 1–2 hr/week (variable; spikes during incidents) | |
| **O-S6 Brand-voice review log audit** | 0.5 hr/week | Per `public-claims-guardrails.md` §8.5 |
| **O-S8 Quarterly documentation audit** | ~0.3 hr/week (4 hr/quarter amortized) | |
| **O-S9 Refund processing (within 24h)** | <0.25 hr/week | Variable with refund volume |
| **§9.1–§9.3 Verification cadence + log maintenance** | 0.5 hr/week | Per quarterly review schedule |
| **§12 Exception register maintenance** | <0.1 hr/week | Variable with exception frequency |

### 14.2 Total weekly founder hours on safeguards (P1 baseline)

**~5–6 hr/week** sustained, plus incident spikes.

### 14.3 Total against the 12–22 hr/week GTM cap

The 12–22 hr/week cap from `channel-prioritization.md` §5 is the GTM time budget. Safeguards consume **additional** founder time outside that cap (operational, not GTM) — primarily ops. The total founder budget across GTM + ops + safeguards + product + support is the structural constraint.

| Activity | Weekly hours (P1) | Source |
|---|---|---|
| GTM (content, cohort, community, outreach) | 12–22 | `channel-prioritization.md` §5 |
| Safeguards monitoring / verification / reviews | 5–6 | This section |
| Support coverage (Sun–Thu 09:00–15:00 GMT+4) | ~30 | `support-operating-model.md` §2.1 |
| Product (engine maintenance, regression tests, instrumentation) | 5–10 | Variable |
| Cohort-onboarding kickoff calls (P1 only) | 4–8 | `gtm-strategy.md` §4.4 |

P1 baseline total: ~56–76 hr/week. **At the upper edge of sustainable founder bandwidth.** This is the structural rationale for D1 (paid acquisition deferred), D7 (mobile app deferred), and other Strategic Priority deferrals — they are not just commercial choices, they are how the founder-time budget closes.

### 14.4 Cost growth as company grows

Safeguard cost grows as:

- Surface count increases → brand-voice review load grows
- Cohort size increases → support load grows; SLA pressure increases
- Vendor count increases → drill cadence grows
- Contractor count increases → contractor audit cadence grows

Cost growth is the rationale for the contractor onboarding ladder in §13 — at P3+, brand-voice contractor takes review load; at P4+, engineering contractor takes CI verification load; at v2.5+, support lead takes ops load. The safeguard cost doesn't disappear — it's distributed across the team that grows around the safeguards.

---

## 15. Cross-references

- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- §14 v1 LOCKED launch roadmap (stop-the-line conditions): `business-plan/14-launch-roadmap.md`
- §12 v1 LOCKED risk register: `business-plan/12-risk-compliance-trust.md`
- Strategic priorities + deferrals D1–D12: `business-plan/01-executive-summary/strategic-priorities.md`
- Public claims guardrails (canonical anti-overclaim): `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Incident communications (canonical severity / response flow): `business-plan/13-support-and-trust-ops/incident-communications.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Support operating model (contractor cadence reference): `business-plan/13-support-and-trust-ops/support-operating-model.md`
- GTM strategy (PP1–PP8 trust signals): `business-plan/08-go-to-market/gtm-strategy.md`
- Channel prioritization (12–22 hr/week founder cap): `business-plan/08-go-to-market/channel-prioritization.md`
- Pricing strategy (≥6 months post-validation lock anchor): `business-plan/07-packaging-and-pricing/pricing-strategy.md`
- Trial / discount policy: `business-plan/07-packaging-and-pricing/trial-and-discount-policy.md`
- Plan matrix: `business-plan/07-packaging-and-pricing/plan-matrix.md`
- Feature prioritization (RM/IB/VTN lifecycle taxonomy): `business-plan/06-product-strategy/feature-prioritization.md`
- Business risk register (this folder): `business-plan/14-risk-compliance-and-safeguards/business-risk-register.md`
- Compliance assumptions (this folder): `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`
- Regulatory question list (this folder): `business-plan/14-risk-compliance-and-safeguards/regulatory-question-list.md`
- Brand-voice review log artifact (REQUIRED INPUT pre-P1): `business-plan/_data/brand-voice-review-log.md`
- Safeguard verification log artifact (REQUIRED INPUT pre-P1): `business-plan/_data/safeguard-verification-log.md`
- Safeguard exception register artifact (REQUIRED INPUT at first exception): `business-plan/_data/safeguard-exception-register.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
