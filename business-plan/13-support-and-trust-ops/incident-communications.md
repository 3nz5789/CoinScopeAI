# Incident Communications

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`; `business-plan/_phase-2/_support/02-support-sla-framework.md` (severity matrix); `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`

---

## 1. Incident communication philosophy

Five operating beliefs.

1. **Silence is the worst incident response.** A user who notices an issue before we do, and finds no acknowledgment when they look, concludes that the product is both unreliable AND opaque. That conclusion is far worse than the underlying issue.
2. **Honesty under pressure is the load-bearing trust signal.** Every incident is an unscheduled stress-test of brand-voice discipline. A clean incident postmortem published openly does more for trust than any paid placement could.
3. **Speed at the comms layer beats speed at the resolution layer.** Acknowledging "we see this; we're investigating" within minutes is more valuable than fixing it in hours without saying anything. The user's anxiety lives in the gap between detection and acknowledgment.
4. **Templated comms beat improvised comms — under pressure.** Pre-committed templates let the founder respond at incident speed without drafting under stress. They also enforce brand-voice discipline when the founder is fatigued or emotionally activated.
5. **Postmortems are public by default.** Severity ≥ medium incidents produce postmortems that are published. Hiding them is the start of cumulative trust drift.

The synthesis: **incident comms is the most demanding test of operational discipline, and CoinScopeAI's brand depends on passing it consistently.**

---

## 2. Categories of incidents

Five categories, each with distinct comms patterns. Cross-reference `_data/operations/Vendor_Failure_Mode_Mapping_v1.md` for the full vendor incident catalog.

### 2.1 Exchange outages

- **What it looks like:** Binance USDT-M API down, partially down, returning stale data, or rate-limiting our scanner.
- **User-facing impact:** Signals stale; gate decisions reference outdated state; demo-trade view degrades.
- **Severity default:** P1 if full outage; P2 if partial.
- **Source of truth:** Engine monitoring + Binance status page.

### 2.2 Other vendor outages (CoinGlass, Tradefeeds, CoinGecko, Stripe, Telegram, Claude API)

- **What it looks like:** OI / liquidation feed degraded; price reference lagging; alerts undelivered; LLM API throttled.
- **User-facing impact:** Specific to the vendor — see `support-operating-model.md` §7.2.
- **Severity default:** P2 unless majority of users affected (then P1).
- **Source of truth:** Engine monitoring + vendor status pages.

### 2.3 Signal quality issues

- **What it looks like:** Engine bug producing wrong regime label, wrong confidence, wrong gate result, or wrong position-sizing math; signals shipping with malformed data; gate firing at system defaults rather than user-configured thresholds.
- **User-facing impact:** **Trust-critical.** P1 Omar's #1 churn trigger (per `04-icp-and-segmentation/primary-icp.md` §8) is gates firing at wrong thresholds. Math wrong is category-fail.
- **Severity default:** P1 if math/gate; P2 if presentation issue.
- **Source of truth:** Cohort report + engine logs + test-and-simulation lab regression.

### 2.4 Billing issues

- **What it looks like:** Stripe payment processing failure; tier-change not applied; founder-cohort discount not applied at signup; refund stuck; per-seat invoicing wrong.
- **User-facing impact:** Financial trust — the buyer wonders if their payment / refund is at risk.
- **Severity default:** P2 — high; if blocking conversion or in 14-day refund window.
- **Source of truth:** Stripe dashboard + support inbox + DB billing state.

### 2.5 Security concerns

- **What it looks like:** Suspected unauthorized account access; API key misuse pattern; suspected data exposure; auth flow bypass.
- **User-facing impact:** **Existential.** A single security incident handled poorly is fatal.
- **Severity default:** P1 — critical, regardless of confirmation status (acknowledge first, investigate, then resolve).
- **Source of truth:** Auth logs + Stripe / Binance event feeds + user reports.

### 2.6 Product incidents (engine bug, dashboard outage, Telegram bot stoppage)

- **What it looks like:** /scan endpoint returning errors; dashboard rendering blank; Telegram bot not pushing alerts.
- **User-facing impact:** Variable; depends on what's degraded.
- **Severity default:** P1 if full outage; P2 if partial; P3 if cosmetic.
- **Source of truth:** Engine monitoring + user reports.

### 2.7 Anti-overclaim drift incidents (brand-voice violations)

- **What it looks like:** A claim ships unreviewed and contradicts the locked phrasing list; an external contractor publishes voice-incongruent copy; a press placement contains overclaim language.
- **User-facing impact:** Trust degrades silently; cohort notices; cumulative if pattern.
- **Severity default:** P2 — high, with brand-voice review pass mandatory before any further public surface ships.
- **Source of truth:** Cohort feedback + brand-voice review log + external monitoring.

---

## 3. Internal vs. external communication rules

### 3.1 Internal-first sequence (always)

The sequence at any incident is:

1. **Detect** — engine monitoring alert, user report, or vendor status.
2. **Acknowledge internally** — incident logged with severity, timestamp, observed impact.
3. **Initial external acknowledgment** — status page note + (if user-affecting) email or in-product banner. **Within 15 minutes for P1; within 30 minutes for P2.**
4. **Investigate** — root cause; document as you go.
5. **Mitigate** — deploy fix or workaround.
6. **Resolve** — confirm resolution; update status page.
7. **Postmortem** — published within 7 days for severity ≥ medium.

### 3.2 What goes external

- The fact that an incident exists (always)
- The user-facing impact in plain language (always)
- The current investigation / mitigation status (always)
- The estimated resolution window (when known; otherwise "next update at [timestamp]")
- The postmortem after resolution (severity ≥ medium)

### 3.3 What stays internal (pending counsel review)

- Detailed root-cause analysis touching counsel-sensitive matters
- User-specific data (other users' configs, financial details, etc.)
- Vendor contractual details
- Anything that would identify a specific affected user without their consent
- Credentials, keys, internal infrastructure paths

### 3.4 The line

**Concealment is forbidden; selectivity is allowed.** We may decline to publish counsel-sensitive details, but we never deny the existence of an incident or its user impact.

---

## 4. Communication priorities by incident type

### 4.1 Exchange outages

**Priority 1:** Tell affected users that the exchange is down within 15 minutes.

**What goes out (within 15 min):**
- Status page banner: "Binance USDT-M API experiencing [outage / degradation]. Scanner data may be stale. Engine fallback active. Next update at [timestamp]."
- In-product banner on affected surfaces (scanner, gate decision, journal if exchange-data dependent).
- Telegram alert (if Telegram still working): "Binance USDT-M data degraded — signals may be stale. Status: [link]."

**What does not go out:**
- Speculation about Binance's root cause.
- Predictions about resolution time we cannot verify.
- Performance-adjacent commentary ("luckily nobody's positions were affected" — never).

**Postmortem:** Published within 7 days. Includes vendor incident summary, our detection/acknowledgment timeline, our user-facing comms timeline, runbook updates.

### 4.2 Other vendor outages

**Priority 1:** Tell affected users the specific vendor + specific impact within 15 min (P1) or 30 min (P2).

**What goes out:**
- Status page entry naming the vendor and the specific data feed affected.
- Affected-feature note in product (e.g., "OI / liquidation feed degraded; signals may show outdated funding-rate context").
- Email to subscribed users (status-page-subscribers list — opt-in).

**What does not go out:**
- Vendor blame language ("[Vendor] is unreliable").
- Promises of vendor-stack changes during the incident ("we'll switch vendors!" — incident comms is not the right surface for strategic decisions).

### 4.3 Signal quality issues

**Priority 1:** **Tell users immediately if math, gate, or regime logic is producing wrong results.** This is trust-critical.

**What goes out (within 15 min of confirmation):**
- Status page banner: "Engine bug confirmed: [specific issue]. Affected scope: [user segment]. Mitigation: [paused affected feature / deployed fix / under investigation]. Next update at [timestamp]."
- In-product banner on affected surfaces.
- Direct email to affected users if a specific cohort can be identified.

**What does not go out:**
- Minimization language ("just a small bug" — never; let the user judge severity).
- Vague placeholder ("investigating" without follow-up timestamp).
- Performance commentary about whether the bug "would have caused losses" — speculative; structurally avoided.

**Postmortem:** Published within 7 days, with full root-cause analysis, mitigation deployed, and runbook / regression-test updates.

**Recovery action per `04-icp-and-segmentation/primary-icp.md` §8:** Math wrong is category-fail; honest postmortem + transparent regression-test commit is the recovery path.

### 4.4 Billing issues

**Priority 1:** Tell affected users their billing state is being investigated within 30 min.

**What goes out:**
- Direct email to affected users (do not put billing details on the status page banner — privacy).
- In-product banner if a billing-flow surface is broken (e.g., "Subscription management temporarily unavailable; refunds being processed manually — contact support@coinscope.ai").
- Status page entry if the issue is system-wide.

**What does not go out:**
- Other users' billing details.
- Specific Stripe-internal error codes that confuse users.
- Promises of "we'll comp you" outside policy — refund / credit decisions follow `07-packaging-and-pricing/trial-and-discount-policy.md` §5.

### 4.5 Security concerns

**Priority 1:** **Acknowledge the concern within 15 minutes of detection or report. Investigate. Tell affected users with counsel review.**

**What goes out (within 15 min):**
- If user-reported: direct response acknowledging the concern, severity P1, founder taking the ticket.
- If system-detected: status page entry confirming investigation; specific user notification once scope is identified.

**What does not go out without counsel review:**
- Confirmation or denial of breach scope until investigation completes
- Detailed attack-vector descriptions
- Specific user-data exposure claims

**What does go out always:**
- The fact that we are investigating
- The fact that we will publish a postmortem
- Counsel involvement disclosed if external comms goes out

**Postmortem:** Published with counsel review; timeline can extend past 7 days if necessary, but cadence updates continue.

### 4.6 Product incidents

**Priority 1:** Tell users which surface is affected and the workaround within 15 min (P1) or 30 min (P2).

**What goes out:**
- Status page banner.
- In-product surface note with workaround if available.
- Email to subscribed users for material outages.

**What does not go out:**
- Engineering jargon as user-facing copy ("BPF unwind failure") — translate to user-impact language.
- Speculative blame ("third-party library issue" — irrelevant to user; describe impact).

### 4.7 Anti-overclaim drift incidents

**Priority 1:** Pull or amend the offending surface immediately upon detection.

**What goes out:**
- The surface itself — corrected — within hours of detection (no public announcement of the correction needed for minor cases).
- For material cases (a launch announcement, a press placement, a pricing-page paragraph): **honest correction note** published with the corrected surface.

**What does not go out:**
- "Sorry, ignore what we said yesterday" — too casual; the correction note is calibrated and brand-voice reviewed.
- Defensive language ("we didn't mean it that way") — admission and amendment is the discipline.

**Postmortem (internal):** Brand-voice review log entry; what failed; what to fix in the review process.

---

## 5. Communication templates / template structure

Five template structures, one per major incident type. **All templates pass brand-voice review at draft time and again at instantiation.**

### 5.1 Status page entry (universal structure)

```
[INCIDENT TITLE — short, factual, no marketing voice]

Status: [Investigating | Identified | Mitigating | Resolved]
Severity: [P1 | P2 | P3]
Started: [timestamp GMT+4]
Last updated: [timestamp GMT+4]
Next update: [timestamp GMT+4]

Impact:
[Plain-language description of what users see / cannot do]

Current actions:
[What we are doing right now]

Workaround (if available):
[How users can mitigate during the incident]

---
Updates:
[timestamp] — [factual update]
[timestamp] — [factual update]
```

Voice rules for the entry:

- Product-tier voice — terse, technical, declarative
- No marketing language; no "We apologize for the inconvenience" filler
- No speculation; if the cause is unknown, "Cause: under investigation"
- Update timestamp every time (so users know freshness)

### 5.2 Direct email — exchange / vendor outage

```
Subject: [Vendor] outage — [feature] affected — investigation underway

Hi [Name],

[Vendor] is currently experiencing an outage affecting [specific feature].
Our engine fallback is active; [specific user impact].

Status: [link to status page]

Next update: [timestamp].

— Mohammed
```

### 5.3 Direct email — signal quality issue

```
Subject: Engine bug confirmed — [specific scope] — action taken

Hi [Name],

We've confirmed an engine bug affecting [specific scope]. Specifically:
[plain-language description].

Action: [paused / mitigated / fix deployed]. Affected users: [scope].

A full postmortem will be published within 7 days at [link].

If this affected your evaluation or use, please reply directly. Refund within
the 14-day window applies if eligible.

— Mohammed
```

### 5.4 Direct email — billing issue

```
Subject: Billing issue affecting your account — being resolved

Hi [Name],

We identified a billing issue affecting your account: [specific issue —
charge timing / refund delay / tier-change / per-seat invoicing].

Action taken: [specific resolution].
Resolution timeline: [specific].

Your billing data is not at risk. If you have questions, please reply.

— Mohammed
```

### 5.5 Postmortem (severity ≥ medium)

```
# Postmortem — [Incident Title]

Date: [date]
Severity: [P1 | P2]
Detection: [timestamp; how detected]
First user-facing acknowledgment: [timestamp]
Resolution: [timestamp]
Total impact window: [duration]

## What happened
[Factual narrative; no minimization; no blame]

## User-facing impact
[Specific impact on cohort / subset]

## Root cause
[Technical narrative; counsel-sensitive details may be redacted]

## Mitigation deployed
[Specific actions taken]

## What we changed
[Runbook updates; regression test added; vendor-stack changes; review-process changes]

## What we did well
[Honest assessment of what the response got right]

## What we missed
[Honest assessment of what we should have done sooner / differently]

## Open follow-ups
[Items still in flight after resolution]

— Mohammed
```

The postmortem is the single most important trust artifact in the operational layer. It must read as honest, technical, and self-critical — never defensive.

---

## 6. What should never be delayed

Six specific comms acts that must occur within their window regardless of investigation completeness.

| # | Act | Window | Reason |
|---|---|---|---|
| **1** | Initial status page entry for any P1 incident | 15 min from detection | Closes the silence gap |
| **2** | Initial status page entry for any P2 incident | 30 min from detection | Same |
| **3** | Direct email to affected users on signal quality issue | 15 min from confirmation of scope | Trust-critical |
| **4** | Direct email to affected users on billing issue | 30 min from confirmation | Financial trust |
| **5** | Direct email to user reporting suspected security concern | 15 min from receipt | Existential |
| **6** | Brand-voice violation surface correction | hours from detection | Stop the drift |

If any of these is delayed, the trust damage compounds beyond the original incident. **The discipline:** the timestamps in the templates are not aspirational; they are the bright line.

---

## 7. What should never be claimed during incidents

Eight claim categories that are forbidden during any active incident, regardless of pressure to "reassure" users.

| # | Forbidden during incidents | Why |
|---|---|---|
| **1** | "No user funds are at risk" — unless verified by counsel-cleared evidence | Speculation of safety is itself a risk claim |
| **2** | "This will be resolved within [X minutes]" — unless verified | Promises that miss compound trust damage |
| **3** | "[Vendor] is unreliable" — even when accurate | Vendor-blame language is incident comms anti-pattern |
| **4** | "We've identified the bad actor" / "We've patched the vulnerability" — without counsel review | Security claims need counsel pass |
| **5** | "Our cohort is unaffected" / "Performance impact is minimal" — performance language | Anti-overclaim violation; testnet posture; speculative |
| **6** | "We're sorry" + nothing else — empty apology pattern | Apology must be paired with action and information |
| **7** | "Going to compensate everyone" — outside policy | Refund / credit decisions follow policy; ad-hoc commitments mid-incident undermine policy discipline |
| **8** | "This won't happen again" — unverifiable promise | Honest framing: "Runbook updated; regression test added" — describe action, not certainty |

The discipline: **every word of incident comms is judged against the brand-voice standard, even at incident speed.** Templated comms make this achievable; improvised comms do not.

---

## 8. Internal incident drill cadence

Per Strategic Priority 5, the vendor failure-mode runbook dry-run is a P1-launch-blocking dependency. Beyond that, drill cadence:

| Drill | Cadence | What it tests |
|---|---|---|
| **Vendor failure-mode dry-run** | Pre-P1 + per-quarter | Detection → status page → email → postmortem flow against a synthetic vendor outage |
| **Signal-quality bug dry-run** | Pre-P2 + semi-annually | Engine bug detection → user-affecting comms → postmortem |
| **Security-incident tabletop** | Pre-P2 + annually | Security report → counsel involvement → user notification flow |
| **Billing-incident tabletop** | Pre-P2 + annually | Stripe edge case → user notification → resolution |
| **Brand-voice violation drill** | Continuous via brand-voice review log | Catch drift before publication |

The drill is the discipline. **A team that has rehearsed the comms flow handles a real incident calmly; a team that has not is improvising under stress.**

---

## 9. Cross-references

- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Support SLA framework: `business-plan/_phase-2/_support/02-support-sla-framework.md`
- Support operating model: `business-plan/13-support-and-trust-ops/support-operating-model.md`
- Trust framework: `business-plan/13-support-and-trust-ops/trust-framework.md`
- Public claims guardrails: `business-plan/13-support-and-trust-ops/public-claims-guardrails.md`
- Brand messaging: `business-plan/09-brand-messaging.md`
- Counsel brief v2: `business-plan/_data/legal/Counsel_Brief_v2.md`
- Risk Disclosure: `business-plan/_data/legal/Risk_Disclosure_v0_DRAFT.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
