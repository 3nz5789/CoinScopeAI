# Current State Assessment

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **sober readiness audit**. Everything below is calibrated against a strict anti-overclaim bar. If something is not yet validated, it is in the *Not yet validated* bucket — even if the founder is confident it works.

The four buckets in each section:

- **Confirmed current state** — verifiable today; would survive a careful audit
- **Likely current state** — believed to be true, but not yet verified to audit standard
- **Not yet validated** — design exists or partial work exists, but cannot be claimed
- **Implications** — what the readiness level means for plan and posture

---

## 1. What appears to exist now

### Confirmed current state

- A public web application reachable at coinscope.ai
- Auth, onboarding, exchange-connection, billing scaffolds, and dashboard surfaces in production
- A FastAPI engine surface exposing `/scan`, `/risk-gate`, `/position-size`, `/regime/{symbol}`, `/performance`, `/journal`
- A regime classifier (v3 ML — Trending / Mean-Reverting / Volatile / Quiet) producing labels with confidence
- Risk-gate logic enforcing the locked numbers (10% drawdown / 5% daily / 10x leverage / 5 positions / 80% heat)
- A Telegram companion (@ScoopyAI_bot) for alerts
- Stripe-ready billing; tier-matrix wiring per locked v1
- Live integration to Binance USDT-M Testnet via CCXT
- A working code-level gate preventing real-capital order placement during validation
- Documentation: 17 framework files, decision log, PCC v2, vendor failure-mode mapping, validation exit memo template, code-review trail through 2026-05-01
- A canonical repo at `/Users/mac/Code/CoinScopeAI/`
- Memory infrastructure (MemPalace) for cross-session continuity
- Drift detector runs nightly against critical config (per `reference_automation.md`)

### Likely current state

- Engine endpoints respond reliably under low-volume validation conditions; behavior under sustained P1 cohort load is unobserved
- The dashboard renders the locked risk numbers and regime labels with the brand-correct visual treatment (mint / neutral / amber / muted) — un-audited
- Telegram alerts surface signals with the canonical payload (regime, confidence, gate result) — payload-schema audit pending
- Journal data is captured and available for cohort review

### Not yet validated

- Engine + risk-gate behavior under realistic P1 cohort load (40 users, sustained)
- Vendor reliability claims (CoinGlass, Tradefeeds, CoinGecko) at P1 cadence
- Telegram alert latency under burst conditions
- Stripe billing flow at production cadence (creation, dunning, refunds, plan changes)
- Onboarding completion rate from signup → exchange connection
- Anti-overclaim discipline holds when external pressure increases (a P0 phase observation does not predict P1 behavior)

### Implications

The product *does things*; the product is not *proven to do them at scale or under pressure*. This is the precise distinction PCC v2 was built to enforce. Any external claim must remain inside the Confirmed bucket.

---

## 2. What is likely partially built

### Confirmed current state

- Desk Preview surface scaffolding exists in code; the multi-account view, advanced gate configuration, and read API are partial
- Support tooling and inbox routing are present but not battle-tested at >10 users
- Incident playbook exists in skeletal form; not exercised in a dry run

### Likely current state

- Cohort observation tooling: data captured; analysis pipeline partially automated, partially manual
- Onboarding flow: end-to-end works but has not been audited for friction at P1 cadence
- Operational runbooks: vendor-by-vendor drafts exist; not yet stitched into a single on-call playbook

### Not yet validated

- Desk Preview value-delivery quality bar (multi-account · advanced gates · read API) at P1 close
- Support response under simultaneous incidents
- Refund and dunning behavior under real billing failures
- Telegram fallback when the dashboard is degraded (or vice versa)

### Implications

Most "partially built" items are P1-window deliverables (not P0 deliverables). The risk is not whether these can be finished — the risk is whether they get finished to the *quality bar* the disciplined-trader cohort will judge against.

---

## 3. What is likely still in-progress

### Confirmed current state

- §3.7 persona-validation interviews are queued, not yet run to a documented count
- Validation_Phase_Exit_Memo template exists; the actual memo is not yet filed
- Counsel brief is at v2 (already locked); decisions on entity restructure are not yet made

### Likely current state

- Vendor-failure incident dry-run is planned but not yet executed
- Desk Preview API access (read) is in-progress on the engineering backlog
- Brand-voice enforcement skill is in active use; consistency audits across surfaces are partial
- Pre-mortem skill exists; routine application before threshold or framework changes is observed but not yet a documented gating step

### Not yet validated

- Whether the persona interviews will confirm or revise P1 Omar / P2 Karim / P3 Layla
- Post-validation legal-entity posture (sole prop → DMCC FZE / mainland LLC / other)
- Annual prepay discount rate (DECISION NEEDED)
- Whether founder-led distribution scales to ~500 paid users without paid acquisition (the M5 CAC trigger)

### Implications

In-progress items concentrate around three vectors: persona validation, post-validation legal posture, and acquisition mechanics. None is blocking P0 validation; all three become blocking by mid-P1.

---

## 4. Current business readiness level

| Dimension | Readiness | Evidence | Gap |
|---|---|---|---|
| Legal entity | Sole prop, UAE-resident founder | `project_jurisdictional.md` | Restructure decision pending; needed before priced raise |
| Counsel coverage | Counsel brief v2 | `business-plan/_data/legal/Counsel_Brief_v2.md` | Entity, US posture, advice framing — open items |
| Insurance | Not in place | — | Likely required at P2 / post-restructure |
| Banking and payments | UAE personal banking; Stripe ready | — | Business banking aligned to entity decision |
| Tax / VAT | UAE-resident treatment | — | EU/MENA cross-border VAT handling REQUIRES INPUT |
| Vendor contracts | Self-serve / individual tier | — | Master-services agreements gated on entity restructure |

### Not yet validated

- Tax / VAT behavior on cross-border revenue at cohort scale
- Insurance requirements at P2 / post-restructure
- Banking adequacy under cohort cash-flow (especially annual prepay timing)
- Whether the entity restructure path will land on DMCC FZE, mainland LLC, or other (decision pending)

### Implications
Business-readiness level is **"sufficient for validation, insufficient for priced raise."** Several blockers cluster around the entity decision; doing them in the right order matters more than doing them fast.

---

## 5. Current go-to-market readiness level

| Dimension | Readiness | Evidence | Gap |
|---|---|---|---|
| Positioning | Locked v1 (`_phase-1/03-positioning.md` + `business-plan/04-problem-value-prop.md`) | Locked 2026-05-01 | Validated against cohort yet to come |
| Brand voice | Locked v1; product tier vs. social tier separated | `09-brand-messaging.md` + voice rules | Audit cadence across all surfaces |
| Channels | Founder-led distribution; content-driven trust play | `_phase-2/_gtm/` | Channel-fit not yet measured at P1 cohort scale |
| Pipeline | Warm-conversation pipeline; no formal CRM volume | — | Cohort attribution and CAC measurement at P1 |
| Paid acquisition | Disabled by policy until Trader CAC validates | `01-executive-summary/strategic-priorities.md` D1 | M5+ trigger; not active |
| Partnerships | None signed; some warm directions identified | — | Vendor partnerships separate from distribution partnerships |
| Public launch readiness | Soft launch (P1) opens 2026-06-01; public launch (P2) Aug–Sep 2026 | Phase map locked | P1 cohort observation gates P2 expansion |

### Not yet validated

- Channel-fit at P1 cohort scale (which methodology channels actually convert)
- Founder-led distribution scaling to ~500 paid users without paid acquisition (M5+ trigger evaluation)
- Soft-launch CAC under cohort observation
- Brand-voice discipline holding under acquisition pressure (P0-phase observation does not predict P1 behavior)

### Implications
GTM readiness is **"validated for soft launch, untested for public launch."** The soft launch's purpose is to *generate* the data that will validate or revise GTM posture before P2.

---

## 6. Current product readiness level

| Dimension | Readiness | Evidence | Gap |
|---|---|---|---|
| Engine + risk gate | Live on Binance Testnet | Confirmed | Production-ready claim gated by PCC v2 §8 |
| Regime classifier (v3 ML) | Producing labels with confidence | Confirmed | Cohort-scale label-quality observation |
| Trader tier surface | Functional end-to-end | Confirmed | Cohort-load testing |
| Desk Preview surface | Partial | Locked v1 §5 + P1-close target | Multi-account · advanced gates · read API by P1 close |
| Desk Full v2 | Design-only | Locked v1 phase map | P5 (Mar–May 2027) deliverable |
| Bybit / additional venues | Design-only | Phase map | P2 |
| Dashboard | Live; visual treatment un-audited | Likely | Accessibility audit, mobile responsiveness audit |
| Telegram | Live; payload-schema audit pending | Likely | Burst-load behavior |
| Mobile / native app | Not in scope | — | Not planned in P0–P5 |
| Code-level testnet hard gate | In place | Confirmed | Re-verified in CI on every release |

### Not yet validated

- Engine + risk-gate behavior at sustained P1 cohort load (40 users)
- Regime classifier label quality at cohort scale (calibration of confidence values)
- Telegram burst-load latency under simultaneous regime flips or news events
- Dashboard accessibility (WCAG) and mobile responsiveness
- Canonical payload-schema parity between dashboard and Telegram (un-audited)

### Implications
Product readiness is **"Trader tier validated for cohort observation, Desk Preview partial, Desk Full v2 design-only."** The product can carry P1 if Desk Preview reaches its quality bar by close of P1.

---

## 7. Current operational readiness level

| Dimension | Readiness | Evidence | Gap |
|---|---|---|---|
| Documentation discipline | Documented; framework v1 + decision log + PCC v2 + brief v2 in place | Confirmed | Maintenance cadence |
| Memory + sync | MemPalace + Drive dual-tree + Notion + Linear + GitHub | `reference_automation.md`, `project_drive_dual_tree.md` | Connector health audit cadence; sync rules locked |
| CI / release | GitHub Actions, drift detector, brand-voice guardrail, CLAUDE.md tripwire | `reference_automation.md` | First incident dry-run pending |
| Support inbox | Live; SLA framework v1 in place | `_phase-2/_support/` | First incident dry-run pending |
| Incident playbook | Skeletal | `_phase-2/_support/03-ticket-routing-and-escalation-rules.md` | Vendor-specific runbooks + on-call |
| On-call | Solo-founder | — | P4 contractor at v2 build |
| Bus factor | Low (solo) | — | Documentation discipline mitigates partially |
| Vendor failure mapping | v1 | `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md` | v1 → extension + dry-run before P2 charter |
| Real-capital gate | Code-level enforced | Confirmed | CI re-verification on every release |

### Not yet validated

- First incident dry-run not yet executed
- Vendor-failure dry-run not yet executed
- Multi-incident response (simultaneous failures) not exercised
- P4 contractor not yet engaged for v2 build window
- On-call coverage during founder unavailability

### Implications
Operational readiness is **"sufficient for ≤40 paid users in P1, insufficient for P2 expansion without runbook completion."** The most concentrated risk is incident response under simultaneous failures, especially while solo.

---

## 8. Gaps between present state and desired positioning

The brand promise — *AI-driven capital-preservation infrastructure that enforces the discipline you've already built* — is honest today on testnet, in scope, and at low cohort scale. It will be tested as the cohort grows. The gaps below are the ones that, if unclosed, will erode the promise's credibility.

| Promise dimension | Today | Desired | Closure path |
|---|---|---|---|
| "AI-driven" | v3 ML regime classifier live; minimal LLM use | Same — minimal use is by design, not weakness | No change required |
| "Capital-preservation" | Risk gates enforced on testnet | Risk gates enforced on real capital, validated in cohort | PCC v2 §8 pass + cohort observation |
| "Infrastructure" | Engine + dashboard + Telegram + journal | Same, plus Desk Preview multi-account + read API | P1 close |
| "Enforces" | Gates run before trade arming on testnet | Same, on real capital, with documented refusal patterns | PCC v2 §8 pass |
| "The discipline you've already built" | Persona-aligned at v1 lock | Persona reconfirmed against P1 cohort | §3.7 interviews + P1 mid-cohort review |
| "UAE-built, MENA-rooted" | Founder + sole-prop in UAE | Same, with substantiated MENA presence (cohort, partnerships, content) | P1 cohort geo-mix + P2 partnerships |
| "Anti-overclaim" | Locked voice + brand audit cadence | Same, under acquisition pressure | Continuous discipline; brand-voice skill in production |
| "Trusted partner" | No incident track record yet | Documented incident response track record | First incident dry-run + first P1 incident response |

### Implications
A leading gap is the absence of **incident track record**. Trust compounds during well-handled incidents; the company has not yet been observed handling an incident under cohort scrutiny. Closing this gap is what `strategic-priorities.md` priorities 5 and 7 exist to address. Other comparably-leading gaps include the bus-factor exposure (§7) and pending §3.7 persona reconfirmation (§3) — none ranks below the others without further data.

---

## 9. Cross-references

- Upstream: `01-executive-summary/executive-summary-v1.md`, `business-model-summary.md`, `strategic-priorities.md`
- PCC v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor failure mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Validation exit memo template: `business-plan/_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`
- Phase charters: `_phase-1/00-phase-1-charter.md`, `_phase-2/00-phase-2-charter.md`, `_phase-3/00-phase-3-charter.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
