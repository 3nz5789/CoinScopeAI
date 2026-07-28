# Compliance Assumptions

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_data/legal/Counsel_Brief_v2.md`; `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`; `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`; `business-plan/12-risk-compliance-trust.md` §12.1 (regulatory and compliance risks)

---

## 1. Posture — assumptions are not facts

CoinScopeAI operates today on a set of compliance-sensitive **working assumptions** that have not been fully validated by counsel. Some are likely correct; some carry meaningful risk; all are tracked here as **assumptions, not legal conclusions**.

The discipline:

- Every assumption is labeled explicitly.
- Counsel-review status is tracked per assumption.
- Business decisions that depend on an unvalidated assumption surface that dependency in their decision-log entry.
- An assumption that fails validation triggers the corresponding entry in `business-risk-register.md` to escalate from Monitoring to Active or Triggered.

**This file is not legal advice and contains no legal conclusions.** Final language for ToS, Privacy Policy, Risk Disclosure, and No-Investment-Advice memo lives in counsel-reviewed documents under `_data/legal/`.

---

## 2. Compliance-sensitive assumptions currently in force

Eighteen assumptions across six areas. Each carries a tracking ID (`CA-#`), a counsel-review status (Pending / In flight / Cleared / Conditional), and the business decision that depends on it.

### 2.1 Entity and operating posture

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-1** | UAE sole-prop posture is sufficient through validation phase (P0–P1) | **Pending** — Counsel Brief F-9 | Pre-P1 launch operating posture; pricing-page entity statement; About page sole-prop disclosure |
| **CA-2** | Post-validation entity restructure (DMCC FZE / mainland LLC / other) is the correct path before any structured raise | **Pending** — Strategic Priority 6 | Fundraising sequencing; vendor master-services contract scope; hiring posture |
| **CA-3** | Below-VAT-threshold posture (no VAT collection at v1) is correct, and threshold trigger at AED 375k (~$102k) annual revenue is the operative anchor | **Pending** — counsel + accountant | Pricing-page tax language; §11 financial model; revenue tracking cadence |
| **CA-4** | Cross-border GCC VAT obligations apply only if specifically registered in the partner jurisdiction (KSA, Bahrain, Oman) | **Pending** — counsel | MENA expansion sequencing; AED display copy; cross-border revenue tracking |

### 2.2 Product positioning and advisory line

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-5** | "Tools, not advice" positioning is defensible for the engine outputs (signals, regime, gate decisions, position-sizer) under MENA + EU/UK regulation | **In flight** — `No_Investment_Advice_Memo_v0_DRAFT.md` pending counsel | All product copy; pricing page tier descriptions; methodology page; support replies |
| **CA-6** | "Institutional-grade" usage is allowed for capability and audience-bridging value descriptions (not for status / certification / regulation / track record) | **Pending** — counsel + brand-voice review | Hero copy ("institutional-grade, AI-driven"); pricing-page tier descriptions; pitch deck |
| **CA-7** | Signals carrying "regime + confidence + gate result + sizing rationale" are descriptive engine outputs, not personalized investment recommendations | **In flight** — same as CA-5 | Telegram alert template; in-product signal cards; methodology page |
| **CA-8** | Risk-gate enforcement does not constitute "managed account" or "discretionary advisor" service when capital remains in the user's exchange account and execution is user-authorized | **In flight** — counsel review | Custody-free positioning; Desk Preview multi-account framing; Desk Full v2 audit-grade reporting framing |

### 2.3 Billing and subscription mechanics

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-9** | Stripe handles billing for all tiers in P1 with UAE entity support; Stripe ToS coverage is adequate for our jurisdictional mix | **Pending** — counsel + Stripe ops review | Pre-P1 payment flow; founder-cohort time-bounded promo codes; per-seat invoicing at Desk Full v2 |
| **CA-10** | 14-day money-back guarantee, single-use per account/email/payment method, is enforceable and aligned with UAE consumer-protection standards | **Pending** — counsel | `07-packaging-and-pricing/trial-and-discount-policy.md` §5; refund flow; anti-abuse enforcement |
| **CA-11** | "Founding-member pricing — locked through your first renewal cycle, then standard pricing applies" framing is defensible against permanent-discount-implication claims | **Pending** — counsel + brand-voice review | Founder-cohort messaging; pricing page; renewal email language |
| **CA-12** | Annual prepay refunds pro-rated only within 14-day window, then locked for the term, complies with consumer-protection norms | **Pending** — counsel | Refund flow; annual prepay marketing |

### 2.4 Claims and marketing

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-13** | Anti-overclaim discipline (no performance language, no leaderboards, no testimonials presented as endorsement) provides legal cover against advisory / promissory claims | **Pending** — counsel | Brand-voice enforcement skill; public claims guardrails; quarterly cohort summary publication |
| **CA-14** | Cohort observation summaries (anonymized, no per-user numbers, no aggregate return figures) are descriptive operational disclosures, not regulated marketing claims | **Pending** — counsel | Quarterly cohort summary publication; Substack content cadence; conference talks |
| **CA-15** | Methodology page (engine logic, regime classifier, position-sizing math) is educational disclosure, not investment advice | **Pending** — counsel | `coinscope.ai/methodology` page; longform Substack content; founder POV op-eds |

### 2.5 User communications and incident comms

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-16** | Incident comms templates (status page entries, direct emails, postmortems) are operational disclosures, not regulated communications, when they describe vendor outages, signal quality issues, billing issues, or product incidents | **Pending** — counsel | `13-support-and-trust-ops/incident-communications.md` template set |
| **CA-17** | Risk Disclosure visible at signup + pricing surfaces is sufficient to gate user access via API auth ToS-gate | **In flight** — `Risk_Disclosure_v0_DRAFT.md` pending counsel | Pre-P1 signup flow; ToS-gate enforcement; API access |

### 2.6 Jurisdiction

| ID | Assumption | Counsel-review status | Business decision dependent on it |
|---|---|---|---|
| **CA-18** | US-blocked-at-signup posture (multi-layer: IP detection + KYC declaration + ban-and-refund flow) is sufficient pre-licensure | **Pending** — counsel | Pre-P1 signup flow; ban-and-refund SOP; D2 deferral until US licensure decision |

---

## 3. Areas requiring counsel review

Five priority areas, in dependency order. Items are **counsel-blocking** in the sense that ship-pause applies until counsel clears the area.

### 3.1 Phase A — counsel deliverables (per `_data/legal/Counsel_Brief_v2.md`)

| Document | Pre-P1 launch dependency | Status |
|---|---|---|
| **Terms of Service** | API auth ToS-gate cannot activate without finalized ToS | Pending counsel start |
| **Privacy Policy** | Signup flow + DPA cannot ship without finalized Privacy Policy | Pending counsel start |
| **Risk Disclosure** | Pricing page + signup gate cannot ship without finalized Risk Disclosure | DRAFT v0 in `_data/legal/Risk_Disclosure_v0_DRAFT.md` |
| **No-Investment-Advice memo** | "Tools, not advice" positioning cannot be confidently deployed without finalized memo | DRAFT v0 in `_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` |
| **Entity-formation recommendation** | Post-validation entity restructure decision blocked without recommendation | Pending — Counsel's first deliverable |

### 3.2 Phase A+ — review of operational documents

| Document | Pre-P1 launch dependency | Status |
|---|---|---|
| **Refund policy language** (CA-10) | 14-day money-back single-use enforcement | REQUIRED INPUT |
| **Founder-cohort framing** (CA-11) | Pricing page + email language | REQUIRED INPUT |
| **"Institutional-grade" usage** (CA-6) | Hero copy + pitch deck + about page | REQUIRED INPUT |
| **Incident comms templates** (CA-16) | Pre-P1 incident readiness | REQUIRED INPUT |
| **US-block enforcement language** (CA-18) | Signup flow Gate 1 copy | REQUIRED INPUT |

### 3.3 Phase B — pre-P2 review (Aug–Sep 2026)

| Item | Pre-P2 launch dependency |
|---|---|
| **Public launch announcement copy** | One coordinated event; brand-voice + counsel review |
| **One time-bounded P2 promo language** | If activated; ≤25%/≤30 days; counsel-cleared if material |
| **First incident postmortem language template** | Validated by first real-incident review |
| **Quarterly cohort summary language template** (anonymized) | Counsel-cleared anonymization standard |

### 3.4 Phase C — pre-P5 review (Mar–May 2027)

| Item | Pre-P5 launch dependency |
|---|---|
| **Desk Full v2 audit-grade reporting language** | Per-seat invoicing + LP-style reporting framing |
| **Per-seat ToS / addendum** | Partner read-only seats / analyst seats add-on terms |
| **Multi-jurisdiction expansion review** | If MENA expansion beyond UAE primary registers cross-border concerns |

### 3.5 Continuous — counsel touch points

| Item | Cadence |
|---|---|
| **Counsel news subscription** | Continuous monitoring of MENA virtual-asset advisory licensing developments |
| **Quarterly counsel review** | Brand-voice surface audit; risk register review; assumption status update |
| **Per-incident counsel notification** | Severity ≥ medium incidents; security events; refund disputes |
| **Per-decision-log-major-entry counsel review** | Phase advances; pricing locks; entity decisions; market expansion |

---

## 4. Product, billing, claims, comms, jurisdiction — assumption summaries

| Area | Active assumptions | Validation pathway |
|---|---|---|
| **Product** | CA-5, CA-7, CA-8 — engine outputs are tools, not advice; signals are descriptive; risk-gate enforcement is not managed-account service | Counsel review of `No_Investment_Advice_Memo_v0_DRAFT.md`; "tools, not advice" stress-tested on pricing / methodology / support copy |
| **Billing** | CA-9, CA-10, CA-11, CA-12 — Stripe ToS coverage adequate; refund mechanics enforceable; founder-cohort framing defensible; annual prepay locks adequate | Counsel review of refund policy; Stripe ops review of promo-code mechanics |
| **Claims** | CA-13, CA-14, CA-15 — anti-overclaim provides legal cover; cohort summaries are operational disclosures; methodology is educational disclosure | Counsel review of Substack content sample; quarterly cohort summary template; methodology page review |
| **User communications** | CA-16, CA-17 — incident comms are operational disclosures; Risk Disclosure gates user access via ToS | Counsel review of `Risk_Disclosure_v0_DRAFT.md` and incident comms templates |
| **Jurisdiction** | CA-1, CA-2, CA-3, CA-4, CA-18 — UAE sole-prop posture sufficient; entity restructure scoped post-validation; below-VAT posture correct; cross-border GCC VAT scoped; US-block enforcement adequate | Counsel review of entity-formation recommendation; counsel review of US-block enforcement language; quarterly review of MENA regulator publications |

---

## 5. What the company should NOT assume without validation

Eight specific things that a typical SaaS company might assume but that CoinScopeAI **must not** assume without counsel validation. Each is a specific anti-pattern.

| # | Do not assume | Why this is risky |
|---|---|---|
| **NA-1** | "Our positioning is fine because the engine is technically a tool, not a recommendation engine" | The line between "tool" and "advice" depends on regulator characterization, not our internal framing. Cleared via CA-5 + counsel sign-off. |
| **NA-2** | "Performance numbers from cohort observation are okay because they're anonymized and aggregate" | Aggregate performance language can still constitute regulated marketing claims. Cleared via CA-13 + counsel review of any draft. |
| **NA-3** | "Founder-cohort discount is fine because we tell users it's time-bounded" | Time-bounded language can drift toward "permanent" implication; permanent-discount claims expose founder-cohort framing as misleading. Cleared via CA-11 + brand-voice + counsel. |
| **NA-4** | "Stripe handles all our billing compliance" | Stripe handles payment processing. It does not absolve us of marketing-language compliance, refund-enforcement compliance, or jurisdiction-specific consumer-protection compliance. Cleared via CA-9 + CA-10 + counsel. |
| **NA-5** | "Sole-prop is fine indefinitely" | Sole-prop blocks priced equity raises, vendor master-services contracts, and full-time hires. Cleared via CA-2 + Strategic Priority 6 + counsel recommendation. |
| **NA-6** | "Below-VAT-threshold means no tax obligation" | Tax obligations exist below the VAT threshold (e.g., income tax in some scenarios; cross-border GCC VAT if registered there). Cleared via CA-3 + CA-4 + counsel + accountant. |
| **NA-7** | "US-block at signup form is sufficient because we display the warning" | Geo-blocking enforcement requires multi-layer detection (IP + KYC declaration + ban-and-refund). A warning alone is not enforcement. Cleared via CA-18 + counsel + ops verification. |
| **NA-8** | "Anti-overclaim discipline alone shields us from advisory classification" | Anti-overclaim reduces marketing risk, not regulatory classification risk. The advisory line is a regulator-characterization question, not a marketing-restraint question. Cleared via CA-5 + CA-8 + counsel. |

The discipline: **when in doubt about a compliance question, default to counsel review, not to an internally-reasoned safe path.**

---

## 6. How compliance uncertainty should affect business planning

Five operational rules for navigating the uncertainty.

### 6.1 Stage-gate decisions to evidence, not to calendar

If a counsel question is in flight, the dependent business decision waits. Not because counsel is the bottleneck — because launching on an unvalidated assumption is the bottleneck on recovery if the assumption fails.

Per §14.0: **"P1+ dates are gate-driven targets, not calendar commitments."** The same discipline applies to compliance gates.

### 6.2 Document the assumption when the decision must proceed

If a decision cannot wait (operational pressure, vendor lock-in, etc.), document the underlying assumption explicitly in the decision-log entry. Mark the assumption with its CA-# from this file and note "counsel-review pending" status. This makes the assumption recoverable: if it fails validation, the decision-log entry surfaces it for review.

### 6.3 Do not market what counsel has not cleared

Surfaces that depend on a CA-# entry **do not ship to public surfaces** until counsel clears the underlying assumption. Internal docs, founder communications, and cohort communications can use working language with explicit caveats; public surfaces cannot.

### 6.4 When an assumption fails validation

If counsel determines an assumption is wrong (e.g., "tools, not advice" framing is insufficient in a specific jurisdiction):

1. The corresponding business decision is rolled back or modified.
2. The decision-log entry is updated.
3. Affected risk register entries escalate from Monitoring to Active or Triggered.
4. Public surfaces are amended.
5. If a public-surface change has trust implications (per `13-support-and-trust-ops/`), an honest correction note may be published.

### 6.5 Compliance uncertainty is funded, not denied

Counsel engagement budget per Counsel Brief: **USD $10,000–$15,000 mid-tier UAE / regional firm** for Phase A. This is a non-deferrable expense. Founder-funded; included in §11 financial model.

The principle: **compliance uncertainty is a structural feature of the business, not an obstacle**. Funding it explicitly is part of the discipline.

---

## 7. Validation checkpoints

Specific moments when assumption status is re-evaluated.

| Checkpoint | Window | What's reviewed |
|---|---|---|
| **Counsel engagement start** | Pre-P1 (target: by mid-May 2026) | All Phase A assumptions; Counsel Brief F-1 through F-11 founder-correctable values |
| **Pre-P1 launch readiness** | 7 days before 2026-06-01 | All pre-launch counsel deliverables cleared; CA-5, CA-9, CA-10, CA-11, CA-13, CA-16, CA-17, CA-18 status confirmed |
| **P1 mid-cohort review** | Week 4 of P1 | Operational assumption holdings; first-incident handling; refund-flow behavior |
| **P1 → P2 exit gate** | End of P1 (Jul 2026) | Phase B pre-P2 reviews; entity-restructure decision started |
| **P2 launch readiness** | 7 days before P2 launch | Phase B counsel reviews cleared; launch announcement counsel-cleared |
| **Quarterly counsel review** | Q3 2026 onwards | Continuous-touch items; brand-voice surface audit; risk register review |
| **Pre-P5 launch readiness** | Q4 2026 → Q1 2027 | Phase C counsel reviews; Desk Full v2 audit-grade reporting language |

---

## 8. Cross-references

- Counsel Brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- No Investment Advice memo (DRAFT): `business-plan/_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md`
- Risk Disclosure (DRAFT): `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- §12 v1 LOCKED risk register: `business-plan/12-risk-compliance-trust.md`
- Strategic Priority 6 (entity decision): `business-plan/01-executive-summary/strategic-priorities.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Business risk register (this folder): `business-plan/14-risk-compliance-and-safeguards/business-risk-register.md`
- Safeguards framework (this folder): `business-plan/14-risk-compliance-and-safeguards/safeguards-framework.md`
- Regulatory question list (this folder): `business-plan/14-risk-compliance-and-safeguards/regulatory-question-list.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
