# 05 — TRUST (Phase 1)

**Purpose:** Inventory the **minimum viable trust set** — the 5–7 trust signals that must be live and verifiable before paid acquisition is ever turned on.
**v1 reference:** `12-risk-compliance-trust.md`, `10-operations-support.md`, Counsel Brief v2.
**Phase 1 outcome:** Documented list of trust signals with status, owner, and verification method per item. Each signal is binary (live / not live), not aspirational.

---

## Why TRUST matters specifically for CoinScopeAI

In crypto-AI trading software the buyer is *correctly* skeptical by default. The category has burned them. Every sentence we publish is read against that skepticism. Trust is therefore not a soft variable; it is the rate-limit on:

- conversion (no trust → no signup),
- pricing power (no trust → ceiling at $19/mo),
- support cost (low trust → high churn → high support load),
- regulatory exposure (low-trust copy attracts the wrong kind of attention).

The defining trust principle from the Scoopy operating instructions is **anti-overclaim**. Trust is built by:

1. **Verifiable claims** — every public number traces to a methodology document or an engine field.
2. **Visible risk controls** — drawdown, daily loss, leverage, heat are first-class UI.
3. **Phased work** — named phases (Scan → Score → Gate → Size → Arm) shown to the user.
4. **Cohort proof** — a visible 30-day validation cohort with cohort exit memo.

Phase 1 names which trust signals are **load-bearing** for paid acquisition and confirms each is live (or queues the work to make it live).

---

## Required subsections

1. **Trust signal inventory** — every signal we have or could have.
2. **Minimum viable trust set (MVTS)** — the 5–7 signals that gate paid acquisition.
3. **Signal status matrix** — Live / Partial / Missing per signal, with owner.
4. **Verification method per signal** — how does a stranger confirm this is true.
5. **Lock + review trigger** — when does the MVTS get re-cut.

---

## Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| Trust signal inventory | MD table, in this file | Strategy CoS |
| MVTS one-pager (signed) | MD | Founder |
| Public Risk Disclosure (Counsel Brief v2 derived, plain-English) | MD → live page | Founder + counsel |
| PCC v2 public summary (gates + §8 Capital Cap explained) | MD → live page | Founder |
| Cohort exit memo template (already in `_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`) | MD | Founder |
| Status page (uptime + incident log) | external (e.g., Statuspage.io or simple page) | Ops |
| Public methodology — what "confidence score" means | MD → live page | Eng + Founder |

---

## Trust signal inventory

| # | Signal | What it is | Why it earns trust | Phase 1 status (target) |
|---|---|---|---|---|
| T-1 | **Public risk disclosure** | Plain-English risk doc, signed by user before any feature use | Sets expectation; legal hygiene; signals seriousness | Live by P0 cohort start |
| T-2 | **PCC v2 public summary** | Plain-English version of Production Candidate Criteria v2 (G1–G4 + §8) | Shows the gate that prevents real-capital ramp; rare in the category | Live by P0 invite-out |
| T-3 | **Cohort transparency page** | Cohort cap (40), validation methodology, cohort exit memo published when complete | Public proof of method, not promise | Page live by P0 start; memo published at cohort close |
| T-4 | **First-class risk UI** | Drawdown, daily loss, leverage, heat visible at compose time | Behavioural proof that risk is not buried | Live (engine already enforces; UI placement audited) |
| T-5 | **Methodology pages** | One page each for: confluence score, regime classifier, gate result | Verifiable mechanism behind every public claim | Live by P1 Narrow Ship |
| T-6 | **Status page + incident log** | External uptime + incident history for engine and exchange dependencies | Operational maturity signal | Live by P0 invite-out |
| T-7 | **Anti-claim list (public)** | Short page: "Things we will not say" — the four locked anti-claims | Counter-positioning trust signal; rare in category | Live by P1 Narrow Ship |
| T-8 | **Counsel-reviewed copy** | Risk Disclosure + No-Investment-Advice Memo on every external surface | Legal hygiene + visible to user | Live before any paid acquisition |
| T-9 | **Founder identity** | Real name, real bio, jurisdictional posture (UAE) on About page | Most crypto-AI brands hide founders; surfacing is a trust signal | Live by P1 Narrow Ship |
| T-10 | **Audit log of own claims** | Every public claim has a source link in `/methodology` | Compounding trust over time | Live by P1, expanding |
| T-11 | **Privacy + data policy** | What we collect, what we don't, what we share (clearly: nothing) | Baseline; required regardless | Live by P0 invite-out |
| T-12 | **Vendor / dependency disclosure** | Public list of upstream dependencies (Binance, CoinGlass, etc.) and their failure-mode mapping at the level of "what happens if X is down" | Honest about provider risk | Live by P1 Narrow Ship |

---

## Minimum Viable Trust Set (MVTS) — load-bearing for paid acquisition

The MVTS is **all of T-1, T-2, T-3, T-4, T-6, T-8, T-11**. Seven signals. Each must be:

1. **Live** (not aspirational, not "coming soon").
2. **Verifiable** (a stranger can find and check it).
3. **Owned** (one named owner; status tracked weekly during Phase 1).
4. **Linked** (referenced from at least one of: hero, footer, signup, Telegram bot intro).

**Hard gate:** No paid acquisition spend until **all seven** are live + verified. This is non-negotiable in Phase 1.

---

## MVTS status table (Phase 1 target — weekly review)

| Signal | Current status | Owner | Verification method | Target live date |
|---|---|---|---|---|
| T-1 Risk Disclosure (public) | Drafts in `_data/legal/` | Founder + counsel | Open page → reads correctly + linked from signup | end-May 2026 |
| T-2 PCC v2 public summary | Internal v2 locked; public version not drafted | Founder | Open page → references the four G1–G4 + §8 | early-Jun 2026 |
| T-3 Cohort transparency page | Concept only | Founder + Strategy CoS | Open page → cap=40, methodology, cohort exit memo template visible | end-May 2026 |
| T-4 First-class risk UI | Engine enforces; UI placement unverified | Eng lead | Walkthrough — drawdown / daily loss / leverage / heat visible at compose | mid-May 2026 |
| T-6 Status page + incident log | Not live | Ops | External page reachable, last-90-days incident view | early-Jun 2026 |
| T-8 Counsel-reviewed copy | Drafts in `_data/legal/`; counsel review pending | Founder + counsel | Counsel sign-off email archived | end-Jun 2026 |
| T-11 Privacy + data policy | Not drafted | Founder + counsel | Open page; cookie/data audit recorded | end-Jun 2026 |

---

## Decisions required (Phase 1)

| # | Decision | Recommendation | Owner |
|---|---|---|---|
| Tr-1 | Lock MVTS at 7 signals | T-1, T-2, T-3, T-4, T-6, T-8, T-11 | Founder |
| Tr-2 | Hard gate paid acquisition on full MVTS | YES — non-negotiable in Phase 1 | Founder |
| Tr-3 | Cohort transparency page format | Single page; cohort cap, methodology, exit memo when ready | Founder |
| Tr-4 | Where to publish PCC v2 public summary | docs.coinscope.ai (or `/methodology/risk-gate`) — needs decision | Founder |
| Tr-5 | Vendor disclosure depth (T-12) | Recommend ship in P1 even though *not* in MVTS — too cheap to skip | Founder |
| Tr-6 | Status page provider | Recommend Statuspage.io or open-source equivalent; do not roll our own | Ops |

---

## Failure modes to avoid

- **Trust theatre.** Logos, vague badges ("trusted by 1,000 traders"), recycled boilerplate. Each MVTS signal must be *third-party verifiable* or *cohort-verifiable*.
- **Trust as a marketing project.** MVTS items live in legal, ops, and engineering — not in marketing's lane. Owner per item is critical.
- **Soft launch on paid acquisition before MVTS is full.** This is the single most expensive mistake the company can make in P1. Hard gate.
- **Aspirational dates.** "Live by Q3" is not a status. Either it's live (with URL) or it's not.
- **Skipping the cohort exit memo.** The cohort transparency page without the published exit memo at cohort close *destroys* the signal it was meant to build.

---

## Tasks (canonical — user-supplied 2026-05-04; see `08-task-backlog.md` for the full four-field backlog)

**NOW**

- `[DOC] TRUST — Trust Framework for CoinScopeAI`
- `[DOC] TRUST — Public Safety Messaging Rules`
- `[DOC] TRUST — Real-Capital Gate Communication Strategy`
- `[DOC] TRUST — Product Claims Approval Checklist`
- `[QA] TRUST — Public-Facing Trust Gap Review`

**NEXT**

- `[DOC] TRUST — Security and Reliability FAQ`
- `[DOC] TRUST — Transparency Page Requirements`
- `[DOC] TRUST — Risk Disclosure Draft`
- `[DOC] TRUST — Trust Signals Needed Before Paid Scaling`
- `[OPS] TRUST — Incident Communication Workflow`

**LATER**

- `[DOC] TRUST — Institutional Trust Package`
- `[DOC] TRUST — Third-Party Validation Roadmap`
