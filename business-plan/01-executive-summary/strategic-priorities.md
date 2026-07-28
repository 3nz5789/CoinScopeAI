# Strategic Priorities

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the founder's working priority list. It exists to prevent priority drift during the validation window and the P1 soft-launch period. If anything in this file conflicts with the locked v1 narrative or the decision log, the decision log wins and this file is updated in the same pass.

---

## 1. Top 10 priorities (ranked, near-term)

Ranking is by **risk-weighted leverage**: impact on the validation pass + P1 cohort × probability the priority will be poorly executed if not explicitly held.

### Priority 1 — Pass P0 validation against PCC v2 §8 Capital Cap criteria

- **Why it matters:** Everything downstream — P1 launch, fundraising narrative, anti-overclaim credibility, the entire structural premise of the business — depends on validation passing on documented criteria. If validation fails or is fudged, the brand is irrecoverable.
- **What "done" looks like:** All four PCC v2 gates (G1–G4) and §8 Capital Cap criteria pass; Validation_Phase_Exit_Memo is filed; decision log is updated.
- **Owner:** Founder. **Window:** P0 (May 2026, ends late May).
- **Risk if mis-executed:** Fatal. Plan stops here.

### Priority 2 — Open P1 soft launch on 2026-06-01 with the 40-user cohort

- **Why it matters:** P1 is the first revenue and the first cohort observation. The 40-user cap is a deliberate throttle; honoring it preserves anti-overclaim discipline and keeps support load tractable.
- **What "done" looks like:** 40 founder-cohort users onboarded; cohort pricing applied; cohort observation cadence active; support inbox + incident process running.
- **Owner:** Founder. **Window:** 2026-06-01 → end of P1 (Jul 2026).
- **Risk if mis-executed:** Cohort opens hot, support breaks, anti-overclaim discipline cracks under launch pressure.

### Priority 3 — Hold the line on anti-overclaim across product, brand, and external claims

- **Why it matters:** Anti-overclaim is the trust moat. Once we say "production-ready" without earning it, the moat is gone — and so is the differentiation against existing signal-group economics.
- **What "done" looks like:** Brand-voice enforcement skill in production; review pass before any external claim; locked phrasing list maintained; no "production-ready" claim until §8 passes.
- **Owner:** Founder. **Window:** Continuous; especially active during P1 and P2.
- **Risk if mis-executed:** Brand drift; one viral overclaim is enough to undo months of disciplined posture.

### Priority 4 — Run §3.7 interviews to confirm or revise locked personas before P1 mid-cohort review

- **Why it matters:** Personas P1/P2/P3 are locked v1 but unvalidated by cohort data. If actual paid users are not Omar/Karim/Layla, downstream pricing/positioning/GTM will misalign.
- **What "done" looks like:** ≥12 interviews conducted; persona-fit analysis shipped; persona file updated or reconfirmed.
- **Owner:** Founder (interviews) + Founder (analysis). **Window:** Pre-P1 launch ideal; P1 mid-cohort hard deadline.
- **Risk if mis-executed:** P1 pricing/positioning is built for personas that don't represent the buying cohort.

### Priority 5 — Lock vendor failure-mode runbooks before P2 expansion

- **Why it matters:** P2 (Aug–Sep 2026) adds vendors and surface area. Without runbooks, every incident is a fire drill, and incidents under cohort observation are existential.
- **What "done" looks like:** Vendor_Failure_Mode_Mapping_v1 reviewed and extended; on-call playbook v1 in place; incident classification matched to severity; first dry-run executed.
- **Owner:** Founder. **Window:** End of P1 / start of P2.
- **Risk if mis-executed:** Vendor outage during P2 cohort observation triggers cohort churn and trust damage.

### Priority 6 — Decide post-validation legal-entity posture before structured raise opens

- **Why it matters:** Sole-prop is fine for validation; not for a priced equity round, not for vendor master-services, not for hiring. The decision is downstream-blocking.
- **What "done" looks like:** Counsel brief reviewed; entity option chosen (DMCC FZE / mainland LLC / other); restructure plan documented with cost and timeline.
- **Owner:** Founder + counsel. **Window:** Post-P0 pass, before structured raise.
- **Risk if mis-executed:** Raise stalls or structures awkwardly; vendor contracts limited.

### Priority 7 — Stand up support and incident operations sufficient for 40 paid users

- **Why it matters:** Support is part of the value delivery, not a cost center. A disciplined-trader cohort will judge the company on incident response inside the first 90 days.
- **What "done" looks like:** Support inbox routing live; SLA framework v1 (already locked) in production; incident severity matrix in production; first incident dry-run executed.
- **Owner:** Founder. **Window:** Pre-P1 launch.
- **Risk if mis-executed:** First incident in P1 surfaces a support gap; cohort confidence drops.

### Priority 8 — Maintain testnet-only discipline with zero real-capital deployment until §8 criteria pass

- **Why it matters:** A single real-capital incident pre-validation is a fatal anti-overclaim breach. The hard gate must remain hard at code level, not just policy level.
- **What "done" looks like:** Code-level gate verified in CI; test-and-simulation lab validates the gate is uncircumventable; no environment variable, config, or feature flag bypasses it.
- **Owner:** Founder. **Window:** Continuous through P0–P5.
- **Risk if mis-executed:** Existential. Single incident kills the brand.

### Priority 9 — Ship Desk Preview ($399) value-delivery surface at quality bar before P1 close

- **Why it matters:** Desk Preview is the bridge from Trader to Desk Full v2. If Desk Preview is weak, the upgrade narrative collapses and Desk Full v2 (P5) lacks an installed base.
- **What "done" looks like:** Multi-account view, Desk-grade analytics, API read access, advanced gates — all functional and on-brand by end of P1.
- **Owner:** Founder. **Window:** P1 (Jun–Jul 2026).
- **Risk if mis-executed:** Tier matrix breaks down; pricing rationale weakens; per-seat expansion stalls.

### Priority 10 — Write the post-validation fundraising narrative against actual cohort data, not projections

- **Why it matters:** Pre-validation, the raise narrative is hypothetical. Post-validation, it must center on what the cohort showed — that is the structural credibility unlock and the entire reason for the disciplined validation phase.
- **What "done" looks like:** §15 Investor Narrative refreshed with cohort data; post-validation pitch lands within 30 days of validation pass; ask is calibrated to cohort signal, not aspiration.
- **Owner:** Founder. **Window:** Within 30 days after validation pass.
- **Risk if mis-executed:** Raise opens on projections, anti-overclaim breaks, valuation defense weakens.

---

## 2. Suggested order

The 10 priorities above are roughly ordered by risk-weighted leverage. Operationally, the dependency-aware order is:

```
P1 ── P3 ── P8 ──▶ continuous
        │
        ▼
       P4 ──┐
            ├──▶ P2 ── P7 ── P9 ──▶ P5 ── P6 ── P10
            │
            ▼
         persona-confirmed cohort
```

- **Priorities 1, 3, 8** run continuously from now through P5; they are not "do, then move on."
- **Priority 4** is upstream of P2 because it informs onboarding, pricing copy, and cohort cadence.
- **Priorities 2, 7, 9** are P1-window deliverables.
- **Priority 5** is the P1→P2 transition gate.
- **Priorities 6 and 10** are post-validation actions — sequenced after P0 passes.

---

## 3. What should not be prioritized yet

These are deliberately deferred. Putting energy here before its time burns founder capacity and risks anti-overclaim drift.

| # | Deferred priority | Why deferred | Earliest revisit |
|---|---|---|---|
| D1 | Paid acquisition (Google, Meta, X, etc.) | Trader CAC unvalidated; 40-user cohort cap makes paid pointless | M5+, only if Trader CAC validates |
| D2 | US user signup unblock | Regulatory posture not yet defined; counsel brief incomplete | Post-P5, with explicit US licensure decision |
| D3 | Bybit + additional venues beyond P1 narrow stack | Engine + risk gates must prove stable on Binance USDT-perp first | P2 (Aug–Sep 2026) |
| D4 | Desk Full v2 launch | Locked v1 phase map places GA at P5 (Mar–May 2027); contractor capacity is the binding constraint | P5 |
| D5 | Fund / institutional product (>$5M AUM) | Not a P0–P5 priority; not on roadmap | Post-P5, only after Desk Full v2 cohort signal |
| D6 | Copy-trading, signal resale, or alpha generation | Out of scope by anti-overclaim charter | Not planned |
| D7 | Mobile app (native iOS/Android) | Web + Telegram cover the cohort; native app is capacity drain | Post-P2, only if cohort demands it |
| D8 | Multi-language UI beyond EN | Target geo (UAE/MENA + global EN) is EN-fluent; Arabic localization is downstream | Post-P5 |
| D9 | Affiliate / referral program with payouts | Anti-overclaim risk; mis-incentivizes content | Post-validation, only with structured guardrails |
| D10 | Hiring full-time engineers pre-validation | Capital efficiency; founder + P4 contractor sufficient | Post-validation, post-raise |
| D11 | Custody, exchange, or fund-formation product | Structural posture is custody-free | Not planned |
| D12 | Public benchmarks, "track record" pages, model leaderboards | Anti-overclaim risk; testnet-only data does not justify public benchmarks | Only after §8 passes + counsel review |

---

## 4. Now / Next / Later table

| Horizon | Window | Items |
|---|---|---|
| **Now** | Today → P1 launch (2026-06-01) | P1 (validation pass) · P3 (anti-overclaim hold) · P4 (persona interviews) · P7 (support stand-up) · P8 (testnet hard gate verified) |
| **Next** | P1 → P2 close (Jun → Sep 2026) | P2 (40-user cohort) · P5 (vendor runbooks) · P9 (Desk Preview quality bar) · D1 trigger evaluation (paid acquisition only if CAC validates) |
| **Later** | Q4 2026 → P5 (Mar–May 2027) | P6 (legal-entity posture) · P10 (post-validation fundraise narrative) · D3 (Bybit at P2) · D4 (Desk Full v2 GA) |

---

## 5. Recommended task list (tagged for backlog import)

These are the priority-derived tasks that should land in `99-task-backlog/` when Wave 2 reaches it. Tagged in canonical format `[TYPE] [AREA] — Action / Deliverable`:

- `[OPS] OPERATIONS — Validate PCC v2 G1–G4 + §8 gates and file Validation_Phase_Exit_Memo`
- `[OPS] OPERATIONS — Confirm code-level testnet→mainnet hard gate uncircumventable in CI`
- `[GTM] GTM — Open P1 founder-cohort signup at 40-user cap on 2026-06-01`
- `[RESEARCH] ICP — Conduct ≥12 §3.7 persona interviews; confirm or revise P1/P2/P3`
- `[OPS] OPERATIONS — Extend Vendor_Failure_Mode_Mapping_v1 + dry-run incident playbook`
- `[OPS] SUPPORT — Stand up support inbox + SLA framework v1 in production`
- `[BUILD] PRODUCT — Ship Desk Preview multi-account + advanced gates + read API for P1 close`
- `[LEGAL] COMPLIANCE — Decide post-validation entity posture with counsel`
- `[DOC] FUNDRAISING — Refresh §15 investor narrative against P0+P1 cohort data within 30 days of validation pass`
- `[QA] TRUST — Run anti-overclaim audit pass against all external surfaces before P1 launch`

---

## 6. Cross-references

- Locked v1 narrative: `business-plan/01-executive-summary.md`
- Operator-grade summary: `business-plan/01-executive-summary/executive-summary-v1.md`
- Business-model summary: `business-plan/01-executive-summary/business-model-summary.md`
- Decision log: `business-plan/_decisions/decision-log.md`
- PCC v2 gates: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Phase charters: `business-plan/_phase-1/00-phase-1-charter.md`, `_phase-2/00-phase-2-charter.md`, `_phase-3/00-phase-3-charter.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
