# SUPPORT — Ticket Routing and Escalation Rules

**Task:** `[DOC] SUPPORT — Ticket Routing and Escalation Rules`
**Type:** NOW
**Owner:** Founder + Strategy CoS
**Status:** DRAFT v0.1 — single-founder routing at v1; escalation paths for vendor-outage, PCC v2 §8, regulatory, billing
**Anchored to:** `01-support-operating-model.md` roles + responsibilities; `02-support-sla-framework.md` severity matrix; `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`; PCC v2 §8.

---

## 1. Routing principle at v1

**The founder is the single triager + responder + escalator for v1.** Routing rules at v1 are *internal* — they govern how the founder switches context across issue types and what escalates outside the founder. When team scales (per **Su-8** trigger), routing rules become *external* — owner per category + escalation tree.

This document is written for both states: the v1 form (founder = all routes) and the v2+ form (per-category owner + escalation paths). Most routing rules apply in both forms; v2+ is the operationally-cleaner form.

---

## 2. Routing table (per User Issue Taxonomy)

Routing maps every issue category to:
- **Owner** — who handles it (v1: founder; v2+: per-role)
- **Default severity** — assigned at triage (per `02-support-sla-framework.md` §2)
- **Escalation trigger** — what bumps it out of normal flow
- **Escalation target** — where it goes when escalated

| Issue category | Owner (v1) | Owner (v2+) | Default severity | Escalation trigger | Escalation target |
|---|---|---|---|---|---|
| **Account / authentication** | Founder | Support Lead | P3 | Auth bypass suspected → P1 | Founder + Eng (security) |
| **Email verification** | Founder | Support Lead | P3 | Failure pattern affects multiple users | Eng |
| **Password reset** | Founder | Support Lead | P3 | None (self-serve where possible) | — |
| **Region block dispute** | Founder | Support Lead | P3 | Legitimate non-US user blocked | Founder (region rule review) |
| **Exchange API key** | Founder | Support Lead | P3 | Engine-side auth failure | Eng |
| **Testnet/mainnet confusion** | Founder | Support Lead | P3 | Pattern across cohort | Founder (UX review with Design) |
| **Sub-$5k branch question** | Founder | Support Lead | P3 | None (canonical response per template) | — |
| **Signal interpretation** | Founder | Support Lead | P3 | Signal logic appears wrong → P2 | Eng |
| **Regime label question** | Founder | Support Lead | P3 | Classifier appears wrong → P2 | Eng (regime classifier) |
| **Demo gate decision question** | Founder | Support Lead | P3 | Gate logic appears wrong → P2 | Eng (risk-gate) |
| **Risk-gate config (T+)** | Founder | Support Lead | P3 | None | — |
| **Journal feature (T+)** | Founder | Support Lead | P3 | Feature broken → P2 | Eng |
| **Telegram bot connection** | Founder | Support Lead | P3 | Bot delivery broken → P2 | Eng |
| **Multi-account view (DP+)** | Founder | Support Lead | P3 | Feature broken → P2 | Eng |
| **Per-seat invoicing (DF+)** | Founder | Support Lead | P3 | Stripe / entitlement drift → P2 | Eng + FinOps |
| **Billing — payment failure** | Founder | FinOps Lead | P2 | Repeated failure pattern | Eng + Stripe support |
| **Billing — refund request** | Founder | FinOps Lead | P3 | Outside 14d window → P3 standard reply; abuse pattern → P2 | Founder (per **Su-7**) |
| **Billing — chargeback** | Founder | FinOps Lead | P2 | Per §6.7 | Founder + Stripe |
| **Billing — pricing question** | Founder | Support Lead | P3 | None | — |
| **Founder-cohort question** | Founder | Support Lead | P3 | None (canonical phrasing) | — |
| **PCC v2 §8 / "is it production-ready" question** | Founder | Founder (always) | P3 | None — single canonical response | — |
| **"Should I trade real money" question** | Founder | Founder (always) | P3 | Always | Founder (PCC v2 §8 routing) |
| **Real-capital risk reported** | Founder | Founder (always) | **P1** | Always | Founder + Eng (security) |
| **Wrong balance / wrong account state** | Founder | Founder (always) | **P1** | Always | Founder + Eng (data integrity) |
| **Unauthorized access suspected** | Founder | Founder (always) | **P1** | Always | Founder + Eng (security) |
| **Regulatory question** | Founder | Founder (always) | P3 | Anything substantive | Founder → UAE counsel (Phase 4) |
| **Privacy / GDPR data request** | Founder | Founder (always) | P3 | Per GDPR window | Founder → UAE counsel (Phase 4) |
| **Vendor outage (Binance / CoinGlass / Tradefeeds / CoinGecko / Claude)** | Founder | Founder + Eng | **P1** | Always P1 | Engine monitoring auto-trigger; status page; broadcast comms |
| **Engine incident (internal)** | Founder | Founder + Eng | P1 or P2 | Per scope | Eng + status page |
| **Feature request** | Founder | Support Lead | P4 | Multiple-user pattern → product roadmap input | Founder |
| **Bug report (cosmetic / non-blocking)** | Founder | Support Lead | P4 | None | — |
| **Bug report (functional)** | Founder | Support Lead | P3 | If blocking → P2 | Eng |
| **Anti-ICP outreach (signal-group / copy-trade / leverage promotion)** | Founder | Support Lead | P4 | None — canonical decline | — |
| **Partnership pitch** | Founder | Founder | P4 | None | — |
| **Press / media request** | Founder | Founder | P3 | Anything substantive | Founder |
| **Brand voice / copy feedback** | Founder | Strategy CoS | P4 | None | — |
| **Methodology challenge / academic question** | Founder | Founder + Eng | P4 | Substantive critique → product engagement | Founder |

---

## 3. Escalation paths (escalation trees)

### Escalation A — P1 incidents (any severity-1)

```
P1 detected (engine monitoring OR user report)
  ↓
Founder paged immediately (24/7) via [REQUIRED INPUT — confirm paging tooling]
  ↓
Within 10 min: status-page update + broadcast email + Telegram alert (if affected user count >threshold)
  ↓
Within 30 min: substantive first-response on every P1 ticket
  ↓
Resolution per `02-support-sla-framework.md` §4 per-tier SLA
  ↓
Within 7 days post-resolution: post-mortem published on coinscope.ai/operations
```

**P1 escalation rules:**

- Vendor outage → engine monitoring auto-detects + auto-broadcasts; founder confirms within 30 min.
- Real-capital risk / unauthorized access / wrong balance → founder personally + Eng simultaneously paged.
- Internal engine incident → founder + Eng work concurrently; status page updated continuously.

### Escalation B — PCC v2 §8 / real-capital questions

Any user question touching:
- "Is the system production-ready?"
- "Can I use this with real money?"
- "When does live trading open?"
- "What's the status of the gates?"

→ **Single canonical response routed through founder** (always, even at v2+):

> "We're in the 30-day validation phase. Real-capital deployment is gated by Production Candidate Criteria v2 §8 — four gates (G1–G4) plus Capital Cap & Phased Ramp. Current status: [link to status page or PCC v2 doc summary]. We will publish gate-pass status before any real-capital path opens. Until then: testnet only."

**Why founder-always:** PCC v2 §8 is the highest-stakes communication in the business. A support contractor giving an inaccurate or off-tone reply here creates downstream reputation cost. Founder owns until PCC v2 §8 closes (i.e., real-capital path opens).

### Escalation C — Billing dispute / refund

```
Refund requested
  ↓
Within 14d window?
  ├─ Yes →
  │   ├─ First-time-paid? Yes → Founder approves; refund processed per tier SLA
  │   └─ First-time-paid? No → Anti-abuse check (§6.7: 1 refund per account lifetime); 
  │       if at limit → decline with template; if not → Founder approves
  └─ No →
      Standard decline reply with cancellation option (effective end of period)
  ↓
If user disputes decline → Founder reviews; if circumstances warrant exception, Founder approves with logged reason
  ↓
If chargeback filed → Account suspended pending review; per §6.7 chargeback handling
```

### Escalation D — Vendor outage

```
Engine monitoring detects vendor degradation
  ↓
Auto-classify P1 (full outage) or P2 (partial / single-feature degradation)
  ↓
Auto-broadcast comms (P1): status-page update + broadcast email + Telegram alert (affected users)
  ↓
Founder confirms detection accuracy within 10 min
  ↓
Founder coordinates with vendor enterprise support per `_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
  ↓
User-facing comms cadence:
  ├─ P1 every 30 min until resolution
  └─ P2 hourly until resolution
  ↓
Resolution: status-page-final + post-mortem within 7 days
```

### Escalation E — Regulatory / counsel routing

```
Regulatory question received (e.g., "Are you licensed?", "How does this comply with [regulation]?", 
"Is this a regulated investment service?")
  ↓
Founder responds with current canonical posture (per memory `project_jurisdictional`):
  "CoinScopeAI is a UAE-based sole proprietorship providing technology-as-a-service. We are not a 
   licensed investment service; we do not place trades, custody funds, or provide investment advice. 
   For specific regulatory questions about your jurisdiction, consult local counsel."
  ↓
If question is substantive (e.g., specific regulator inquiry, formal complaint, licensing requirement claim):
  → Founder routes to UAE counsel (Phase 4 trigger; counsel relationship established by then)
  ↓
Privacy / GDPR data request:
  → Founder responds within GDPR-mandated window (30 days)
  → If complex / multi-jurisdictional → counsel routing
```

---

## 4. Cross-routing patterns

### Pattern 1 — One ticket, multiple categories

User reports: "My account balance shows wrong, and I want a refund." → routes simultaneously to:
- P1 wrong-balance escalation (founder + Eng)
- P3 refund request (founder approval pending wrong-balance resolution)

Refund decision held until wrong-balance is investigated. If wrong-balance was a CSAI bug, refund is offered proactively (regardless of user's request).

### Pattern 2 — Issue category unclear

User reports: "It's not working." → triage as P3 with founder following up to establish category:
- "Could you tell us which surface (dashboard / Telegram / email) and which feature?"

Auto-template for "ambiguous" tickets ensures founder doesn't over-invest in early diagnosis.

### Pattern 3 — User confused about gating, reports as bug

User on Free reports "Telegram alerts not working." → triage as P3 (account / gating); routes to founder; canonical response: "Telegram bot routing is part of Trader and above; here's how Free + Trader differ [link]."

Per `_packaging/04-premium-feature-gating-rules.md` §2.D — Telegram bot is hard-gated; Free user should not see Telegram-connect UI. If they do, that's a P2 gating leak (audit row 4.4 in ONBOARDING `_onboarding/05`).

### Pattern 4 — Multi-user pattern detection

Multiple tickets in 24 hours about the same issue → auto-flag as potential P2 incident; founder reviews for systemic cause; if confirmed → status-page update + broadcast comms.

### Pattern 5 — Founder-relationship out-of-band ticket

P3 prospect DMs founder personally about Desk Preview question → founder responds in DM but logs ticket internally for KPI tracking. Out-of-band founder relationships are valid but must not break support audit trail.

---

## 5. Routing for incidents (incident comms tree)

When an incident is declared (engine outage, vendor outage, security event, data integrity event), the following comms tree fires:

```
Incident declared
  ↓
[T+0] Internal: founder + Eng paged
  ↓
[T+10 min] External:
  ├─ Status page updated (canonical incident description)
  ├─ Broadcast email to affected user segment
  ├─ Telegram alert to affected user segment (if applicable)
  └─ Pricing page banner (if user-acquisition-affecting)
  ↓
[Continuous] Status page updates per cadence (P1: 30 min; P2: 60 min)
  ↓
[Resolution] Status page resolution-final
  ↓
[T+ resolution + 7d] Post-mortem published on coinscope.ai/operations
  ↓
[T+ resolution + 14d] Lessons-learned summary in next release notes / status digest
```

### Post-mortem format (canonical)

Per `_data/operations` patterns + memory `feedback_premortem_required` (post-mortems mirror pre-mortems in structure):

1. **Summary** — what happened, when, who was affected.
2. **Detection** — how was it detected, time-to-detection.
3. **Comms** — when did external comms fire, what was said.
4. **Root cause** — methodical, evidence-led; vendor blame is acceptable when accurate; CSAI cause is acknowledged when accurate.
5. **Resolution** — what was done.
6. **Customer impact** — quantified (users affected, duration, revenue / trust impact).
7. **Remediation** — what we changed; what we did NOT change and why.
8. **Anti-overclaim audit** — did the comms violate any §6.10 flag? if yes, mitigation.

---

## 6. Routing failure modes

- **Real-capital question gets non-canonical response.** Support drift on PCC v2 §8 question = single highest reputation cost. Escalation B is founder-always for a reason.
- **Vendor outage detected by user before us.** Routing fails because monitoring missed it. Engine monitoring coverage gap; route as P1 + improve monitoring.
- **Refund granted outside §6.7 rules.** Founder approves out of empathy; precedent set; abuse pattern emerges. Escalation C is the discipline.
- **P1 not paged out-of-coverage.** Coverage-hour SLA breach + trust-load violation. Paging tooling REQUIRED INPUT must be reliable.
- **Multi-user incident not detected as systemic.** 5 separate tickets about the same issue routed independently = 5x founder time without status-page broadcast. Pattern 4 mitigates.
- **Out-of-band founder DM bypasses audit trail.** Pattern 5 mitigates if logged; missing log = invisible to KPIs.
- **Counsel-route question handled by founder without legal review.** Phase 4 counsel relationship is the gate; pre-Phase 4 substantive regulatory questions = "we're working with our counsel; we'll come back to you" template + log for counsel review when established.

---

## 7. Anti-overclaim audit on routing rules

| Routing element | §6.10 flag | Mitigation |
|---|---|---|
| PCC v2 §8 canonical response | Flag-clean (no Flag 1/2/3 risk) | Single canonical phrasing in Escalation B |
| Real-capital question routing | Flag-clean | Founder-always; never delegated |
| Vendor outage comms | Flag-clean | Status page + post-mortem; vendor blame attributed accurately |
| Refund decline copy | Flag-clean | Per §6.7 rules; never improvised |
| Regulatory question canonical response | Flag-clean | Acknowledges UAE sole-prop posture; never overclaims license / regulation |
| Founder-cohort question response | Flag 1 risk | Canonical phrasing per `_pricing/03` §6 only |

---

## 8. What this unlocks

- Routing table v1 is canonical; consumed by `04-user-issue-taxonomy.md` for severity defaults.
- `05-support-inbox-and-response-workflow.md` consumes routing table for triage logic.
- `Standard Response Templates` (NEXT) inherits canonical phrasings from Escalations B + C + E.
- `Billing Support Playbook` (NEXT) consumes Escalation C as the master flow.
- `Exchange Connectivity Support Playbook` (NEXT) consumes Escalation D vendor-outage flow.
- Phase 4 counsel engagement has explicit trigger (Escalation E substantive regulatory question).
- Eng has explicit handoff contract: which support categories route to Eng + at what severity (rows in §2 marked "Eng" target).
