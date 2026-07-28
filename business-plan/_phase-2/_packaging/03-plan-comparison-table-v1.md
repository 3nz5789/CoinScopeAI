# PACKAGING — Plan Comparison Table v1

**Task:** `[DOC] PACKAGING — Plan Comparison Table v1`
**Type:** NOW
**Owner:** Strategy CoS + Design
**Status:** DRAFT v0.1 — render-ready for pricing page; pending Phase 1 BRAND `Website Copy Structure` for tone alignment
**Feeds decision:** **Pk-5**
**Anchored to:** §6.6 prices, §6.5 Free Scope B, `_phase-2/_packaging/02-free-vs-paid-boundary.md` matrix, Phase 1 POSITIONING Surface Variant Table, §6.10 anti-overclaim audit.

---

## 1. Page-level scaffolding

### Header (above the table)

```
Pricing
Trade Smarter With AI

Testnet only. 30-day validation phase. No real capital.
```

(Per Scoopy custom instructions: every risk surface pairs with this disclaimer. Per §6.10 Flag 2: validation status visible alongside prices.)

### Sub-header

```
Pick the tier that matches how you trade. Capital preservation first, profit generation second.
Annual billing saves ~17%. Founder-cohort pricing available through [LAUNCH DATE + 60 days].
```

### Footer (below the table)

```
USD primary. AED courtesy display for MENA users at checkout. UAE sole prop (Mohammed). 
Other GCC users responsible for any local tax obligations.

Capital Cap: 10x leverage / 10% account drawdown / 5% daily loss / 5 open positions / 80% position heat.
Production Candidate Criteria v2 §8 enforces all caps.
```

(Per §6.8 currency disclosure + Scoopy canonical 5 tokens.)

---

## 2. Comparison table (4 tiers + per-seat add-on row)

### Tier headers row

| | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| **Monthly** | $0 | **$79** | **$399** | **$1,199** |
| **Annual (paid yearly)** | — | $790 ($66/mo equiv) | $3,990 ($333/mo equiv) | $11,990 ($999/mo equiv) |
| **Founder-cohort (60-day window)** | — | $59/mo | $299/mo | $899/mo |
| **Best for** | Trying the system. Sub-$5k disciplined traders building toward Trader. | P1 Methodists and P2 Engineers running a single account. | Solo PMs running a $200k–$1M book. P2 power-users hitting API limits. | Solo PMs scaling with partners. Multi-account, audit-grade reporting (v2). |
| **Status** | — | Includes engine API + dashboard *(stabilizing in cohort)* | Multi-account aggregation + static monthly PDF | v2 launches Mar–May 2027 |
| **CTA** | Verify account | Start Trader | Start Desk Preview | Talk to founder |

(Per §6.10 Flag 2: "stabilizing in cohort" must appear on Trader card. Per Phase 2 charter §5: real-capital language traces to PCC v2 §8.)

### Feature rows

#### Signal output

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| Top-5 curated signals, 15-min delayed | ✓ | ✓ | ✓ | ✓ |
| Real-time signal feed (full fidelity, all symbols) | — | ✓ | ✓ | ✓ |
| Per-symbol regime label | ✓ | ✓ | ✓ | ✓ |
| Regime confidence score | — | ✓ | ✓ | ✓ |
| Multi-timeframe confirmation | — | ✓ | ✓ | ✓ |
| Custom watchlist | — | ✓ | ✓ | ✓ |

#### Risk gate

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| Demo-trade gate behavior view | ✓ | ✓ | ✓ | ✓ |
| Configurable risk gate (within Capital Cap) | — | ✓ | ✓ | ✓ |
| Live gate decisions on your account | — | ✓ | ✓ | ✓ |
| Multi-account portfolio heat | — | — | ✓ | ✓ |
| Cross-exchange risk aggregation | — | — | ✓ | ✓ |

#### Journal & analytics

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| Personal performance journal | — | ✓ | ✓ | ✓ |
| Journal export (CSV) | — | ✓ | ✓ | ✓ |
| Custom tags | — | ✓ | ✓ | ✓ |
| Cohort comparison | — | — | ✓ | ✓ |
| Static monthly PDF report | — | — | ✓ | ✓ |
| Audit-grade partner reporting (LP-style) | — | — | — | v2 |
| Tax-ready export | — | — | — | v3 |

#### Alerts & integration

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| In-app alerts | Read-only, delayed | Real-time | Real-time | Real-time |
| Telegram bot routing | — | ✓ | ✓ | ✓ |
| Custom Telegram routing (multi-channel) | — | — | — | ✓ +seat |
| Email digest | Weekly | Daily | Daily | Daily |
| Webhook egress | — | — | ✓ | ✓ |

#### API & power-user

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| API access | — | Limited (~1 req/sec/endpoint) | Standard | Standard |
| Backtest sandbox | — | — | ✓ | ✓ |

#### Account

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| Account verification | ✓ | ✓ | ✓ | ✓ |
| Single exchange account (Binance USDT-M) | ✓ | ✓ | ✓ | ✓ |
| Multi-account / multi-exchange | — | — | ✓ | ✓ |
| Bybit (P2) | — | — | (Aug-Sep 2026) | (Aug-Sep 2026) |
| Per-seat invoicing | — | — | — | ✓ |

#### Trust & methodology *(public on every tier)*

| Feature | Free | Trader | Desk Preview | Desk Full v2 |
|---|---|---|---|---|
| Engine methodology docs | ✓ | ✓ | ✓ | ✓ |
| Validation phase status | ✓ | ✓ | ✓ | ✓ |
| "What we don't do" reference | ✓ | ✓ | ✓ | ✓ |
| Engine status / uptime page | ✓ | ✓ | ✓ | ✓ |
| Per-signal trace | — | ✓ | ✓ | ✓ |

---

## 3. Per-seat add-on (separate sub-section below main table)

Heading: **Add seats to Desk Full v2**

| Seat type | Monthly | Annual | Founder-cohort | What it includes |
|---|---|---|---|---|
| Partner read-only seat | $149 | $1,490 | $99/mo | Read-only access to multi-account view, performance reports, and per-signal traces. No risk-gate config. No journal edit. |
| Analyst seat | $249 | $2,490 | $179/mo | Read + write: journal edit, tag management, custom watchlists for portfolio coverage. No risk-gate config. |

Footnote: "1 PM seat included with every Desk Full v2 subscription. Add seats anytime — pro-rated charge applies."

---

## 4. FAQ block (below the table)

The following six questions are pre-addressed to reduce sales friction and surface anti-overclaim discipline:

1. **Is this safe with real capital?** No. Validation phase is testnet-only. Real-capital deployment is gated by Production Candidate Criteria v2 §8. We will publish the gate-pass status before any real-capital path opens.
2. **Why is Free useful?** Verifies an exchange account, demonstrates the regime classifier and risk-gate behavior on demo trades, and shows the top-5 curated signals on a 15-minute delay. It is a trust demo, not a stripped product.
3. **What if my account is below $5k?** Free is yours. The system positions Trader as the destination when your account crosses the $5k threshold. We will notify you. We do not paywall sub-$5k traders.
4. **Can I cancel anytime?** Yes. Effective at the end of the current billing period. 14-day money-back guarantee for first-time paid subscriptions.
5. **What's the difference between Desk Preview and Desk Full v2?** Preview is multi-account aggregation + a static monthly PDF report. Full v2 (launching Mar–May 2027) adds audit-grade partner reporting (LP-style) and per-seat support for partners and analysts.
6. **Is founder-cohort pricing locked in forever?** No. Founder-cohort applies to sign-ups in the first 60 days post-public-launch and locks through your first renewal cycle. After that, standard pricing applies.

(Q1, Q3, Q6 directly address §6.10 anti-overclaim flags.)

---

## 5. Anti-overclaim audit on this surface

| Surface element | §6.10 flag | Mitigation in this draft |
|---|---|---|
| Trader card description | Flag 2 — pricing tension on "stabilizing" | Explicit "(stabilizing in cohort)" qualifier on Trader status row |
| Founder-cohort row | Flag 1 — drift to "lifetime" | Sub-header: "Founder-cohort pricing available through [LAUNCH DATE + 60 days]." FAQ Q6 explicit. No "founder discount locked-in" language anywhere. |
| AED display posture | Flag 3 — local-entity implication | Footer: "AED courtesy display for MENA users at checkout. UAE sole prop (Mohammed). Other GCC users responsible for any local tax obligations." |
| "Audit-grade partner reporting" | Audit clean | Tagged "v2" in the matrix; not promised at v1; FAQ Q5 reinforces. |
| "Trade Smarter With AI" tagline | Audit clean | Per Scoopy custom instructions — primary marketing tagline; allowed in social/marketing tier; pricing page is product-tier surface but tagline appears in header for brand continuity. |
| Capital Cap footer | Audit clean | Canonical 5 tokens reproduced verbatim from Scoopy custom instructions. PCC v2 §8 referenced. |
| "What we don't do" link | Audit clean | Public on every tier per §5.3.4. |

---

## 6. Visual / layout requirements (handoff to Design)

- **Sticky header on scroll** — tier names + price + CTA always visible while user scrolls feature rows.
- **Mobile collapse** — stacked tier cards; feature rows expand-on-tap; per-seat add-on as separate card below.
- **Validation badge** — "Testnet only · 30-day validation" badge prominent on every tier card on mobile.
- **No "most popular" highlight** — per Phase 1 BRAND voice (anti-overclaim, anti-pressure). The user picks the tier that fits their trading, not the one with the badge.
- **Annual / monthly toggle** — single toggle above the table; updates all four tier prices simultaneously.
- **Tabular numerals** — prices use tabular figures per Scoopy product-tier register (numbers monospaced).
- **Color regime tokens** — regime labels in feature rows use the canonical regime colors (Trending #00FFB8, Mean-Reverting #A3ADBD, Volatile #F5A623, Quiet #5B6472) per Scoopy custom instructions.

---

## 7. Open dependencies

- **Phase 1 BRAND Website Copy Structure (NEXT)** — pricing-page copy ladder must inherit from the website copy ladder.
- **Pk-5** decision (table form) — currently drafted as 4-tier horizontal grid; Design may recommend collapsed-rows variant for desktop.
- **§9 messaging matrix** — "Best for" row copy must align with §9 tier descriptions.
- **REQUIRED INPUT** — exact Trader API rate-limit number ("~1 req/sec/endpoint" from §5; needs PRODUCT confirm before publishing on pricing page).
- **REQUIRED INPUT** — daily vs weekly email digest assumption needs Pr-4 confirmation.

---

## 8. What this unlocks

- **Pk-5** decision can be marked recommended at 4-tier horizontal grid + per-seat sub-section.
- Pricing page v1 development can begin against this spec.
- §9 messaging matrix gets concrete tier descriptions to align against.
- §10 ops gets the FAQ block to seed the support knowledge base (per `_phase-2/04-support.md`).
