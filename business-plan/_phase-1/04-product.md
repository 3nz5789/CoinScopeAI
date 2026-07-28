# 04 — PRODUCT (Phase 1)

**Purpose:** Define the **P1 Narrow Ship** offer — what is in, what is core/premium, and what is deferred. Ground every commitment in an existing engine endpoint.
**v1 reference:** `05-product-strategy.md`, engine endpoints (`/scan`, `/risk-gate`, `/position-size`, `/regime/{symbol}`, `/performance`, `/journal`).
**Phase 1 outcome:** P1 Narrow Ship offer scope written as a one-page MOSCOW (Must / Should / Could / Won't), each item tied to an existing engine endpoint or marked as `NEW SCOPE` with a build cost estimate.

---

## Why PRODUCT matters specifically for CoinScopeAI

The product surface in P1 is *narrow on purpose*. Three forces push us toward narrow:

1. **Engine truth.** The engine has six known-good endpoints. Anything we sell that isn't backed by one of those six is either deferred work or a marketing claim with no implementation.
2. **Risk envelope.** PCC v2 §8 caps capital exposure during validation. The product must not promise behaviour the gates would block.
3. **Cohort math.** 40 seats in P0, growing to ~100 by end of P1. With this sample, broad surface = no statistical signal anywhere. Narrow surface = readable signal.

Three forces push us *not* to be too narrow:

1. **Pricing tolerance.** Trader $79/mo needs enough surface to feel worth it. If the offer is "scanner only", price compression is immediate.
2. **Competitive shelf.** A product that's *only* a risk gate looks like a feature, not a tool.
3. **Persona retention.** Omar (P1 primary) has a journaling habit; if we don't carry the journal, we lose his daily loop.

The MOSCOW below tries to find the productive middle.

---

## Required subsections

1. **MOSCOW table** — every feature mapped to Must / Should / Could / Won't.
2. **Endpoint backing column** — every Must/Should item must reference an engine endpoint (or be marked `NEW SCOPE`).
3. **Tier matrix mapping** — which features land on Free / Trader / Desk Preview (Desk Full v2 is *out* of Phase 1).
4. **Premium / core / deferred boundary lines** — clear, decision-ready.
5. **P0 → P1 delta** — what changes between cohort validation product and P1 Narrow Ship.

---

## Recommended artifacts

| Artifact | Format | Owner |
|---|---|---|
| P1 MOSCOW (this doc) | MD table | Founder + Strategy CoS |
| Engine-endpoint backing matrix | MD table, in this file | Engineering lead |
| Tier feature matrix (Free / Trader / Desk Preview) | MD table | Founder |
| P0 → P1 delta memo | MD, 1 page | Founder |
| Feature deprecation / freeze list | MD, in this file | Engineering lead |

---

## P1 Narrow Ship MOSCOW (draft for review)

| Feature | Bucket | Tier | Engine endpoint backing | Phase 1 commit |
|---|---|---|---|---|
| Multi-pair USDT-M scanner (Binance) | **Must** | Free (limited) / Trader (full) | `/scan` | YES |
| Confluence-scored signals (0–12) | **Must** | Trader | `/scan` | YES |
| Risk gate evaluation per signal | **Must** | Trader | `/risk-gate` | YES |
| Position sizing helper | **Must** | Trader | `/position-size` | YES |
| Regime label per symbol | **Must** | Trader | `/regime/{symbol}` | YES |
| Per-trade journal with gate result | **Must** | Trader | `/journal` | YES |
| Performance dashboard (cohort-level) | **Must** | Trader | `/performance` | YES |
| Telegram alert on new gated signal | **Must** | Trader | composed (no new endpoint) | YES |
| Daily digest summary | **Should** | Trader | composed from `/performance` + `/journal` | YES if cohort feedback supports |
| Manual override audit log | **Should** | Trader | `/journal` extension | YES |
| Custom thresholds (per-user heat cap) | **Could** | Desk Preview | `/risk-gate` extension | NO in P1 |
| Multi-account / per-seat | **Could** | Desk Preview (Phase 5+) | NEW SCOPE | NO in P1 |
| Bybit support | **Won't** (P1) | — | NEW SCOPE — design only | NO in P1 (P2 design) |
| Copy-trading | **Won't** (ever, in current form) | — | not aligned with anti-claim list | NO |
| Auto-execute on real capital | **Won't** (P1) | — | gated by PCC v2 §8 | NO |
| Strategy marketplace | **Won't** (P1) | — | scope creep | NO |
| Mobile native app | **Won't** (P1) | — | dashboard mobile-responsive only | NO |

---

## Tier feature matrix (P1 Narrow Ship)

| Feature | Free | Trader $79 | Desk Preview $399 |
|---|---|---|---|
| Scanner (top pairs, delayed) | ✓ (top 10, 15-min delay) | ✓ (full universe, real-time-ish) | ✓ |
| Signals with confluence score | — | ✓ | ✓ |
| Risk gate result per signal | — | ✓ | ✓ |
| Position sizing helper | — | ✓ | ✓ |
| Regime labels | — | ✓ | ✓ |
| Journal with gate result | — | ✓ | ✓ |
| Telegram alerts | — | ✓ | ✓ + custom routing |
| Performance dashboard | — | ✓ (cohort) | ✓ + per-user views |
| Daily digest | — | ✓ | ✓ + custom cadence |
| Custom thresholds | — | — | ✓ |
| Vendor expansion (P2 venues) | — | — | as P2 ships |
| Per-seat additions | — | — | not yet (Phase 5+) |

> **Note:** Desk Full v2 ($1,199/mo) is *not* a Phase 1 product. Its surface is locked behind the Phase 5 entry criteria (Mar–May 2027).

---

## P0 → P1 delta (what changes after cohort validation)

| Item | P0 (Validation) | P1 (Narrow Ship) | Trigger |
|---|---|---|---|
| Cohort cap | 40 | open up to 100 by end-Jul 2026 | PCC v2 G1–G3 green |
| Pricing live? | No (cohort comp'd) | Yes — Trader $79 | Cohort exit memo signed |
| Real-capital allowed? | No (testnet only) | Phase 1 of §8 Capital Cap (small notional, gated) | PCC v2 G1–G4 + §8 Phase 1 entry |
| Marketing copy | "Validation cohort" | "Narrow ship" | Positioning Phase 1 lock |
| Telegram alerts | cohort-only group | Trader-tier in-bot alerts | Trader subscribers exist |
| Performance dashboard | cohort aggregate | per-user (with privacy notice) | Account isolation reviewed |

---

## Premium / core / deferred boundary

- **Core (Trader)** — everything that lets a single self-directed trader scan, score, gate, size, alert, and journal a single account. The full Omar daily loop.
- **Premium (Desk Preview)** — anything that customizes the gate (custom thresholds), adds routing (custom Telegram destinations), or adds reporting (per-user views).
- **Deferred (out of P1)** — anything that requires multi-seat, multi-venue beyond Binance, or any marketplace / social mechanic.

---

## Decisions required (Phase 1)

| # | Decision | Recommendation | Owner |
|---|---|---|---|
| Pr-1 | Lock the P1 MOSCOW | As above; subject to founder + engineering sanity check | Founder + Eng lead |
| Pr-2 | Allow Manual override audit log into Must | Recommend Yes — Omar journaling habit depends on it | Founder |
| Pr-3 | Daily digest in P1? | Recommend Should (ship if cohort week-2 feedback asks for it) | Founder |
| Pr-4 | Free tier limits (top 10? 15-min delay?) | DECISION NEEDED — too generous = no Trader conversion; too tight = no acquisition funnel | Founder |
| Pr-5 | Manual real-capital go decision per cohort member after PCC v2 §8 Phase 1 opens | Yes — manual approval per user, no auto-promote | Founder + RISK owner |

---

## Failure modes to avoid

- **Building before cohort feedback.** Anything in *Should* that doesn't have a cohort-validated ask is engineering on speculation.
- **Stretching for Karim or Layla.** API access, advanced reporting, multi-venue — all tempting, all wrong for P1.
- **Letting Free become a substitute for Trader.** Free should *demonstrate* the gate, not deliver the loop.
- **Implicit features.** "Of course it has X" — write it down or it doesn't exist.
- **Real-capital pressure breaking the gate.** A cohort member asking to skip §8 is a *NO* by design.

---

## Tasks (canonical — user-supplied 2026-05-04; see `08-task-backlog.md` for the full four-field backlog)

**NOW**

- `[DOC] PRODUCT — Product Strategy Overview`
- `[DOC] PRODUCT — Core Product Pillars`
- `[DOC] PRODUCT — MVP vs Beta vs Scale Feature Matrix`
- `[DOC] PRODUCT — Product Value Ladder`
- `[RESEARCH] PRODUCT — Must-Have Features for First Paying Users`

**NEXT**

- `[DOC] PRODUCT — User Journey from Signup to First Value`
- `[DOC] PRODUCT — Feature Prioritization Framework`
- `[RESEARCH] PRODUCT — Retention Drivers for Pro Traders`
- `[DOC] PRODUCT — Product Scope Guardrails`
- `[QA] PRODUCT — Current Feature Surface vs Strategy Review`

**LATER**

- `[DOC] PRODUCT — Team and Fund Product Variant Concept`
- `[DOC] PRODUCT — Expansion Opportunities Beyond Core Trading Intelligence`
