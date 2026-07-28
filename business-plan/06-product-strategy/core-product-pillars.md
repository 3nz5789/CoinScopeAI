# Core Product Pillars

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file declares the **five core product pillars** that the product surface organizes around. Each pillar maps to a specific engine endpoint or set of endpoints, a buyer-side job-to-be-done, and a tier where it first becomes premium. Each pillar carries a **table-stakes vs. differentiator** classification that determines whether it carries marketing weight (differentiator) or is invisible-but-required (table stakes).

The discipline: **fewer pillars, deeply executed**, beats more pillars, shallowly executed. Five is the maximum. Adding a sixth requires a pre-mortem and a decision-log entry.

---

## 1. The five pillars at a glance

| # | Pillar | Locked engine endpoint | Owns the buyer's | First-tier surface |
|---|---|---|---|---|
| 1 | **Market Intelligence / Scanning** | `/scan` | Watchlist time | Free (sample) → Trader (full) |
| 2 | **AI-Assisted Signal Context** | `/regime/{symbol}` + `/scan` payload | Setup-evaluation moment | Free (sample) → Trader (full) |
| 3 | **Risk-Aware Decision Support** | `/risk-gate` + `/position-size` | Discipline-enforcement moment | Trader (locked numbers) → Desk Preview (advanced) |
| 4 | **Execution Discipline / Operating Workflow** | scan → score → gate → size → arm flow | Authorization moment | Trader → Desk Preview (multi-account) → Desk Full v2 (per-seat) |
| 5 | **Journaling / Performance Feedback** | `/performance` + `/journal` | Post-trade reflection | Trader (basic) → Desk Preview (analytics) → Desk Full v2 (audit-grade) |

Each pillar is examined below: what it is, why it matters, what's table stakes vs. differentiator, and what should be central in early versions.

---

## 2. Pillar 1 — Market Intelligence / Scanning

### What it is

A multi-pair scanner that surfaces setups across USDT-perpetual venues (Binance USDT-M now; Bybit at P2), ranking them by a documented confluence score. The output is a confluence-ranked list with regime + confidence + gate result on each entry, not a feed of trade ideas.

### Why it matters

Without scanning, the user must manually monitor a watchlist of 20–40 pairs across a 24/7 market. That manual monitoring is the failure mode `03-market-thesis/why-now.md` §4 describes — *manual discipline breaks at fragmentation scale.* The scanner is the consolidation surface that fixes it.

### Table stakes vs. differentiator

| Aspect | Classification |
|---|---|
| The fact that we scan multiple pairs | Table stakes — every adjacent product does this |
| Confluence scoring with documented inputs | Differentiator — most adjacent products hide their scoring |
| Regime + confidence + gate result on each scanner row | **Strong differentiator** (D2 + D1) — no foil category does this end-to-end |
| 24/7 always-on operation with low-latency updates | Table stakes for crypto-perp |
| Multi-venue aggregation | Will be table stakes after P2 (Bybit); differentiator only briefly |

### What should be central in early versions

- **Confluence-score transparency** — the buyer can see what produces a high score, not just the score itself
- **Regime + confidence on every row** — never strip these out for "cleaner UI"
- **Gate result on every row at Trader+** — the buyer knows in advance whether they could arm
- **Configurable filtering** — by regime, by gate result, by confluence threshold

What stays out of early versions: predictive ranking ("this will work"), historical-backtest banners on rows, "hot setup" badges, urgency framing, trade-now CTAs.

---

## 3. Pillar 2 — AI-Assisted Signal Context

### What it is

The regime classifier (v3 ML — Trending / Mean-Reverting / Volatile / Quiet) that produces labels with confidence values, paired on every signal payload. AI-assistance also extends to signal confluence weighting and (minimally) to natural-language explanations where appropriate.

### Why it matters

The buyer's existing methodology already classifies regime — usually informally, under cognitive load, with bias. Naming the regime explicitly with confidence removes cognitive load and reduces decision-fatigue. *AI-assisted* is the right framing because the buyer's framework remains primary; AI provides context, not authority.

### Table stakes vs. differentiator

| Aspect | Classification |
|---|---|
| Some form of regime / volatility readout | Increasingly table stakes |
| **Named regime label (4-state) with calibrated confidence** | **Strong differentiator** (D2) |
| Regime label paired with gate result on every signal | **Strong differentiator** — only CoinScopeAI does this end-to-end |
| Natural-language explanation of regime transitions | Table stakes if minimal; differentiator if methodical |
| Predicting the next regime | Out of scope — anti-overclaim risk |

### What should be central in early versions

- **The four-state regime label with confidence** — surfaced in every relevant view
- **Regime page** — current regime, confidence, recent transitions, inputs (what the model saw)
- **Pairing with gate result** — never separate regime from gate context
- **Calibrated confidence values** — confidence is not a marketing decoration; it is a calibrated number

What stays out of early versions: regime *predictions* (we describe the present, not the future), regime "scoring" against historical archetypes presented as future success probability, "AI" as a hero hook in the regime UI.

---

## 4. Pillar 3 — Risk-Aware Decision Support

### What it is

The risk gate (drawdown · daily loss · leverage · position heat · max open positions) plus the position sizer. The gate runs *before* trade arming; position sizing is computed at user-configured thresholds with formula transparency.

### Why it matters

This is the pillar that makes CoinScopeAI a *trader operating system* rather than another scanner. Manual gating breaks at scale; the risk gate is the mechanical answer. Position sizing math run with transparency replaces the user's manual hand-calculation. Locked Vision A is operationalized by this pillar more than any other.

### Table stakes vs. differentiator

| Aspect | Classification |
|---|---|
| Some form of risk parameter visible | Increasingly table stakes |
| **Pre-arming risk gate with explicit refusal pattern** | **Strong differentiator** (D1) — defining feature |
| Configurable per-user thresholds | Differentiator with primary ICP |
| Position sizing with formula + inputs + output transparency | **Strong differentiator** with primary ICP |
| Locked thresholds (10%/5%/10x/5/80%) as defaults | Trust signal; not differentiator alone |
| Audit log on threshold changes | Trust signal; differentiator at Desk Preview+ |
| Conditional / combination / time-of-day gates | Differentiator at Desk Preview |

### What should be central in early versions

- **Pre-arming gate is non-negotiable** — never a post-hoc audit
- **Explicit refusal with the gate that fired** — never generic "blocked" copy
- **Math transparency in the position sizer** — formula visible, inputs visible, output visible
- **Configurable thresholds at Trader+** — the user's framework is respected
- **Locked numbers (10%/5%/10x/5/80%) as defaults across the cohort** — visible when composing a position

What stays out of early versions: gate "predictions" (it either fires or it doesn't), risk *scoring* presented as a quality measure, "AI risk" as a hero hook, automatic threshold tuning ("we've optimized your risk for you").

---

## 5. Pillar 4 — Execution Discipline / Operating Workflow

### What it is

The end-to-end **scan → score → gate → size → arm** workflow run as a single coherent surface. Tabs, views, and alerts compose into a working day for the user. At Desk Preview, multi-account discipline. At Desk Full v2 (P5), per-seat permissions and partner read-only views.

### Why it matters

Each step alone is a feature. The **workflow** is the product. The integration is what no foil category provides; signal services own *score* and journaling apps own *observe* but neither owns the chain. Owning the chain is the moat at the workflow layer.

### Table stakes vs. differentiator

| Aspect | Classification |
|---|---|
| Each individual step (scan, score, gate, size) | Each is table stakes alone |
| **The integrated workflow as a single surface** | **Strong differentiator** (D1 + D2 + D3 combined) |
| Single canonical payload schema across dashboard and Telegram | Differentiator at the polish layer |
| Multi-account view as part of the workflow | Differentiator at Desk Preview |
| Per-seat permissions + partner read-only views | Differentiator at Desk Full v2 (P5) |
| User-authorized arming step (vs. autonomous) | Posture, not feature |

### What should be central in early versions

- **The full chain visible in a single dashboard layout** — not five separate apps
- **Telegram + dashboard sharing the canonical payload** — never two schemas
- **The user authorizes the arm step explicitly** — no autonomous path; no "set it and forget it"
- **Workflow continuity across web + Telegram surfaces** — a user using only Telegram sees a coherent slice
- **Multi-account view at Desk Preview by P1 close** — the upgrade story for P3 Layla depends on this

What stays out of early versions: autonomous trading, mass-cancel-and-reset macros, "auto-rebalance" of positions, multi-strategy templates that the system "runs for you."

---

## 6. Pillar 5 — Journaling / Performance Feedback

### What it is

The journal (every trade captured with rule-respect / rule-violation tagging, R-multiple result, regime and gate context) plus the performance surface (analytics, attribution, per-account breakdowns). At Desk Full v2, audit-grade journal with partner-readable reports and per-seat audit trails.

### Why it matters

The buyer's existing journal lives in spreadsheets or Notion. They dread maintaining it. Without good journaling, the discipline-software promise is incomplete — the user can't tell whether their framework is working. This pillar closes the loop between rule and outcome.

### Table stakes vs. differentiator

| Aspect | Classification |
|---|---|
| Trade history capture | Table stakes |
| **R-multiple + rule-violation tagging on every trade** | **Differentiator** with primary ICP |
| Regime context preserved per trade entry | Differentiator |
| Performance attribution by regime / setup / gate | Differentiator at Desk Preview |
| Audit-grade journal with partner-readable reports | Differentiator at Desk Full v2 (P5) |
| Backtest user-defined rules against history | Future-tier feature; not P0–P2 |
| Public performance leaderboards | Anti-overclaim — disallowed |

### What should be central in early versions

- **Journal entries automatic from the workflow** — the journal is the byproduct, not a separate task
- **Rule-respect / rule-violation tagging visible** — the user can see when they followed and didn't follow their framework
- **R-multiple reporting that matches hand-calculation** — math transparency extends here
- **Per-trade regime context preserved** — looking back, the user can see what regime the trade was made in
- **Manual-journal abandonment** as a leading indicator of upgrade potential — design the surface so the user can stop maintaining their parallel journal

What stays out of early versions: leaderboards, social-tier sharing of trades, "best traders this week" UI, performance presented as endorsement, public benchmarks, "track record" pages.

---

## 7. Pillar coverage by tier

A consolidated view of how the five pillars carry across the locked tier matrix:

| Pillar | Free | Trader $79 | Desk Preview $399 | Desk Full v2 $1,199 + per-seat |
|---|---|---|---|---|
| 1. Market Intelligence | Sample only | Full scanner; configurable filters | Full + advanced filters; multi-account scanning | All Desk Preview + cohort-level analytics |
| 2. AI-Assisted Signal Context | Regime label only | Regime + confidence + gate result | Regime + confidence + gate + multi-account context | All Desk Preview + audit-grade regime history |
| 3. Risk-Aware Decision Support | Read-only sample (no gate output) | Risk gate + position sizer; configurable thresholds | Advanced gates (combination / time-of-day / per-account override); audit log on threshold changes | All Desk Preview + per-seat threshold permissions |
| 4. Execution Discipline / Workflow | Read-only | Full single-account workflow | Multi-account workflow; read API | All Desk Preview + per-seat permissions + partner read-only views |
| 5. Journaling / Performance Feedback | Read-only sample | Single-account journal; R-multiple + rule-violation tagging | Multi-account analytics; performance attribution | All Desk Preview + audit-grade journal + partner-readable reports |

The premium feature placement matches the WTP indicators in `04-icp-and-segmentation/pains-triggers-wtp.md` §4 and the JTBD emphasis matrix in `04-icp-and-segmentation/jobs-to-be-done.md` §6.

---

## 8. Pillar-by-pillar quality bar (P1 close)

By the close of P1 (target end-Jul 2026), the following quality bars must be met for each pillar:

### Pillar 1 (Market Intelligence)

- Scanner runs continuously across the supported pair universe
- Confluence scoring is documented (inputs, weights, output formula)
- Regime + gate result paired on every row
- 24/7 stability under P1 cohort load (40 users)

### Pillar 2 (AI-Assisted Signal Context)

- Regime labels with confidence on every signal (Telegram + dashboard)
- Regime page shows current state, confidence, recent transitions
- Confidence values calibrated against documented thresholds
- Regime transitions surface within the locked latency budget (`DECISION NEEDED` for explicit number)

### Pillar 3 (Risk-Aware Decision Support)

- Pre-arming gate fires correctly across all five locked thresholds
- Explicit refusal patterns visible to the user with inputs
- Position sizer math transparent (formula + inputs + output)
- Configurable thresholds at Trader+; advanced gate configurability at Desk Preview

### Pillar 4 (Execution Discipline / Workflow)

- Single-account workflow end-to-end on Trader
- Multi-account view at Desk Preview by P1 close
- Read API at Desk Preview by P1 close (documented payloads)
- Telegram + dashboard share the canonical payload

### Pillar 5 (Journaling / Performance Feedback)

- Journal entries automatic from the workflow
- R-multiple + rule-violation tagging
- Single-account performance reporting at Trader
- Multi-account performance attribution at Desk Preview by P1 close

If any pillar's P1-close quality bar is missed, the implication is reflected in `mvp-vs-beta-vs-scale.md` readiness gates and may push P2 charter timing.

---

## 9. What pillars deliberately do NOT cover

The pillars are five by design. Several adjacent product domains are deliberately **not** pillars:

| Adjacent domain | Why not a pillar | Disposition |
|---|---|---|
| Alpha generation | Out of scope; Vision A mismatch | Never a pillar |
| Signal subscription / signal-as-deliverable | Custody-free + anti-overclaim posture | Never a pillar |
| Copy-trading / leader-follower | Custody-free + anti-overclaim posture | Never a pillar |
| Custody / managed accounts | Structural posture | Never a pillar |
| Fund formation / fund administration | Out of scope; counsel-line | Never a pillar |
| Spot exchange operations | Out of scope | Never a pillar |
| Brokerage / market-making | Out of scope | Never a pillar |
| Native mobile-app pillar | Web + Telegram cover | Not before P5 at earliest |
| Localization (multi-language UI) | Capacity discipline | Post-P5 |
| Affiliate / referral systems | Anti-overclaim risk | Post-validation, structured guardrails only |
| Public benchmarks / leaderboards | Anti-overclaim, validation-phase posture | Disallowed |

These do not appear as pillars, do not get engineering capacity, and do not appear in the product roadmap.

---

## 10. Cross-references

- Locked v1 §5: `business-plan/05-product-strategy.md`
- Engine API reference: `coinscopeai-engine-api` skill
- Trading rules: `coinscopeai-trading-rules` skill
- Alerting design: `alerting-and-user-experience` skill
- Tier matrix: `01-executive-summary/business-model-summary.md` §3
- JTBD emphasis matrix: `04-icp-and-segmentation/jobs-to-be-done.md` §6
- Differentiation framework: `05-positioning/differentiation-framework.md`
- Strategic constraints: `02-company-overview/strategic-constraints.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
