# Product Strategy

**Status:** Wave 1 · v1 · 2026-05-07
**Companion to:** `business-plan/05-product-strategy.md` (locked v1) — single source of truth for feature-by-feature commitment
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

---

## 1. Product strategy overview

CoinScopeAI is building a **trader operating system that enforces the discipline disciplined crypto-perp traders have already built.** The product is the analytical and gating layer between the user's intent and the exchange's order book. Capital stays in the user's exchange account; orders are user-authorized; risk gates run *before* trades arm; regime + confidence + gate result accompany every signal.

Strategically, this means:

- **The product is process software, not signal software.** We surface setups, but the buyer's gates decide whether they can be armed. The unit of value is *enforcement*, not *prediction*.
- **The product is custody-free by structural choice.** We do not pool, custody, or hold capital under any tier or phase. Custody-free is structural alignment with regulatory direction, not a feature.
- **The product is testnet-only during validation, real-capital-gated until §8 passes.** The hard gate is enforced at code level, not just policy.
- **The product surface is shaped by the locked tier matrix.** Free / Trader / Desk Preview / Desk Full v2 — each tier wraps a different scope of the same engine, with feature classification protected by `feature-prioritization.md`.

The product strategy holds across three horizons:

- **Near-term (P0–P1, May–Jul 2026):** prove the Trader-tier surface against P1 Omar; ship Desk Preview to quality bar by P1 close
- **Medium-term (P2, Aug–Sep 2026):** vendor expansion (Bybit + redundancy); public launch; cohort-data discipline
- **Long-term (P5+, Mar 2027 onward):** Desk Full v2 launch with per-seat scaling for solo PMs and small desks

---

## 2. Who the product is for first

The primary product target through P0 → P1 close is **P1 Omar — the Self-Taught Methodist** (per `04-icp-and-segmentation/primary-icp.md`).

Operationally, this means feature priorities are weighted toward what P1 Omar values most:

1. Configurable risk gates that respect the user's own thresholds
2. Math transparency (formula + inputs + output for position sizing)
3. R-multiple + rule-violation tagging in the journal
4. Canonical, rate-limited Telegram alerts that don't drown the user
5. Regime label + confidence + gate result on every signal
6. Anti-overclaim posture observable in 30 seconds across surfaces

P3 Layla (strategic secondary) influences product strategy in a specific way: **Desk Preview surface must hit quality bar by P1 close** (multi-account view + advanced gates + read API + Desk-grade analytics) so the upgrade story works for the early Layla referrals that arrive through P1 Omar's network. P2 Karim (watch-list secondary) influences product strategy modestly — primarily through API documentation quality at Desk Preview.

The product is **not** for: signal-buyers, copy-trading audiences, autonomous-execution seekers, custody-seekers, US-resident retail (until licensure), beginner traders without methodology, sub-$5k accounts, fund LPs. These segments should not see features built for them on the P0–P5 roadmap.

---

## 3. What core workflow it should own

CoinScopeAI's locked operating workflow is **Scan → Score → Gate → Size → Arm**. This is the canonical workflow the engine runs, and it is the workflow the product surface must own end-to-end.

| Step | Engine endpoint | User-visible artifact | Owns the user's |
|---|---|---|---|
| **Scan** | `/scan` | Multi-pair scanner, ranked by confluence | Watchlist time |
| **Score** | within `/scan` payload | Confluence score; regime + confidence | Setup-evaluation time |
| **Gate** | `/risk-gate` | Pre-arming gate; explicit refusal with reason | Discipline-enforcement moment |
| **Size** | `/position-size` | Position sizer with formula + inputs + output | Position-math moment |
| **Arm** | (user → exchange API) | User-authorized trade, journal entry created | Authorization moment |
| **Observe** | `/regime/{symbol}`, `/performance`, `/journal` | Regime page, performance reports, journal | Post-trade reflection |

The workflow is **not** owned end-to-end by any adjacent product category. Signal services own *Score*. Exchange-native interfaces own *Arm*. Journaling apps own *Observe*. Simple scanners own *Scan*. CoinScopeAI is the only product that owns the workflow as a single, gated, auditable surface — and that integration is the moat.

The workflow design is locked. It is not a candidate for restructuring within Wave 1. New features either reinforce one of these six steps or they are out of scope.

---

## 4. What problems it solves first

Operator-grade restatement, in priority order:

| # | Problem | Severity | Who feels it most | Solved by |
|---|---|---|---|---|
| 1 | Manual gating breaks at edge cases (multiple positions, after-hours, news-driven volatility) | High | P1 Omar, P3 Layla | Risk gate runs before order arming, 24/7 |
| 2 | Existing tools either replace the user's framework or ignore it | High | P1 Omar | Configurable thresholds; framework-respect copy |
| 3 | Journal is in spreadsheets; performance attribution is painful | High | P1 Omar, P3 Layla | Integrated journal with R-multiple + rule-violation tagging |
| 4 | Regime is implicit; the user holds it in their head | Medium-High | P1 Omar, P2 Karim | Named regime + confidence on every signal |
| 5 | Multi-account juggling (own book + partner book) | High | P3 Layla | Multi-account view at Desk Preview |
| 6 | Programmable risk + clean APIs are unavailable in adjacent products | High | P2 Karim | Read API at Desk Preview |
| 7 | 24/7 markets eat sleep; manual monitoring is unsustainable | Medium-High | P1, P3 | Always-on engine + canonical Telegram alerts + dashboard |
| 8 | Existing crypto products carry overclaim and casino aesthetics | Medium | All | Anti-overclaim brand voice, product-tier UI |

Problems **deliberately not solved first** include: alpha generation, signal subscription, copy-trading mechanics, custody, fund-formation tooling, native mobile app, multi-language UI, US licensure flow. Each is rejected on a structural posture or sequencing basis (per `02-company-overview/strategic-constraints.md` §8).

---

## 5. Where trust and risk fit into product strategy

Trust and risk are **not** features layered on top of the product strategy. They are the spine. The product strategy is structured so that trust and risk are observable in 30 seconds of using the product:

| Trust / risk surface | How it appears in the product | Where it lives |
|---|---|---|
| Risk gates as first-class UI | Composing-position view shows current drawdown / daily-loss / leverage / heat / position-count vs. threshold | Dashboard primary view; Telegram alerts; gate refusal pattern |
| Math transparency | Position-sizing formula visible (formula · inputs · output) | Position-sizer step; documentation |
| Validation-phase honesty | Disclaimer above the fold ("Testnet only. 30-day validation phase. No real capital.") | All surfaces |
| Code-level testnet hard gate | No real-capital path exists during validation | Engineering invariant; CI re-verified on every release |
| Least-privilege API-key scopes | Onboarding copy: "Read + trade scopes. **No withdrawal scope, ever.**" | Exchange-connection step |
| Regime + confidence + gate result on every signal payload | Canonical schema on dashboard and Telegram | All signal surfaces |
| Anti-overclaim copy | Locked phrasing list; brand-voice review pass | All surfaces |
| Incident transparency | Postmortems published in product-tier voice; status page | Status / incidents page |
| PCC v2 publication | G1–G4 + §8 visible; gates against "production-ready" claim | About page; PCC v2 dedicated page |
| Configurable thresholds | User can override system defaults | Gate-config UI |

The implication for product strategy is that any feature that *weakens* one of these trust/risk surfaces — even if technically attractive — is rejected. Custody features, autonomous-execution features, performance-promising surfaces, leaderboards, social-tier voice in-product — all rejected by this design rule.

---

## 6. Product boundaries

The boundaries below are not negotiable within the P0–P5 horizon. Each is a hard product constraint with rationale.

### 6.1 In-scope (in P0–P5)

- USDT-perpetual futures on supported venues (Binance USDT-M now; Bybit at P2)
- Risk gates: drawdown, daily loss, leverage, position heat, max open positions
- Regime classification (Trending / Mean-Reverting / Volatile / Quiet) with confidence
- Position sizing with formula transparency
- Multi-pair scanner with confluence scoring
- Performance + journal endpoints with R-multiple and rule-violation tagging
- Web dashboard at coinscope.ai
- Telegram alerts via @ScoopyAI_bot (canonical payload)
- Tier matrix as locked: Free / Trader / Desk Preview / Desk Full v2 + per-seat
- Read API (Desk Preview, post P1 close)
- Multi-account view (Desk Preview, post P1 close)
- Audit-grade journal + advanced reporting (Desk Full v2, P5)
- Per-seat permissions and partner read-only views (Desk Full v2, P5)

### 6.2 Out-of-scope (across all P0–P5 phases)

- Custody, pooled capital, managed accounts
- Autonomous execution without user authorization
- Alpha generation as a product
- Signal subscription / signal-as-deliverable
- Copy-trading / leader-follower mechanics
- Fund-formation tooling
- Brokerage / market-making
- Spot exchange operations
- US-licensed retail flow (until licensure path decided)
- Native iOS / Android app (web + Telegram cover the cohort)
- Multi-language UI beyond EN
- Affiliate / referral payout systems pre-validation
- Public benchmarks / leaderboards / "track record" pages while on testnet
- White-label / private-label arrangements

### 6.3 Conditional / future scope (post-P5 or post explicit decision)

- Additional venues beyond Binance USDT-M and Bybit (P2+)
- Write API for programmatic order placement (post-P5 at earliest)
- Native mobile app (post-P5, only if cohort demands)
- Arabic / multi-language UI (post-P5)
- Audit log on threshold changes as a public feature (Desk Preview decision pending)

These boundaries combine to keep the product surface narrow enough that a solo founder + P4 contractor can execute to quality bar within the locked phase windows.

---

## 7. What must be excellent for early success

Excellence (not adequacy) is required in five areas through P1 close. Adequacy in any one of them produces churn in the disciplined-survivor cohort.

### 7.1 Risk-gate behavior

Every gate must fire when it should, never when it shouldn't, return the explicit gate that fired with inputs, and respect user-configured thresholds. **Test bar:** P1 Omar can configure a low daily-loss threshold, attempt a breach, observe the refusal, and verify the math. If any of the five locked gates produces a wrong result once, trust damage is high. Excellence here is non-negotiable.

### 7.2 Math transparency

Position-sizing math must be visible — formula, inputs, output — and must match the user's hand-calculation. P1 Omar will hand-verify within the first two weeks; P2 Karim will verify against their own scripts. **Test bar:** the math can be reproduced by a careful user without internal documentation.

### 7.3 Regime classification quality

Regime labels must be defensible — confidence values must be calibrated, transitions must be timely, regime + confidence + gate result must arrive together on every signal. **Test bar:** a P1 Omar reading the regime page can see *why* the regime is what it is (inputs, confidence, recent transitions) and is not surprised by the label.

### 7.4 Alert canonicality

Telegram alerts must follow a single, canonical payload schema (regime + confidence + gate result + symbol + side + price). Alerts must rate-limit, dedupe, and group per the `alerting-and-user-experience` skill. **Test bar:** a P1 Omar receives no more than N alerts/day (`DECISION NEEDED` for explicit cap), no duplicate alerts, no off-canonical alerts.

### 7.5 Onboarding and exchange-connection trust

API-key scope copy must be explicit, the testnet-only honesty must be visible above the fold, the first-value experience must occur before billing capture. **Test bar:** a careful P1 Omar reads the onboarding flow and finds nothing that contradicts the anti-overclaim posture.

These five areas absorb the largest share of P0/P1 engineering capacity by design.

---

## 8. What should remain intentionally limited early on

The discipline is: **constraints are features.** Several things stay limited not because we can't build them but because limiting them is the right product strategy through P1 / P2.

| Limited area | Why limited | When (if ever) revisited |
|---|---|---|
| Number of supported venues (Binance USDT-M only through P1) | Engine stability + cohort signal quality | P2 (Bybit) |
| Number of supported pair types (USDT-perp only) | Focus; capital efficiency | Post-P5 if cohort demands |
| Free-tier scope (scanner + regime sample only) | Tier integrity; first-value pre-billing | P1 review (Q4 in `README.md`) |
| Native mobile app (no native client) | Web + Telegram cover; capacity discipline | Post-P5, only if cohort demands |
| Write API (read-only at Desk Preview) | Authorization safety; anti-overclaim | Post-P5 at earliest |
| Multi-language UI (EN only) | Geo target; capacity | Post-P5 |
| Public benchmarks / track record pages | Anti-overclaim, validation-phase posture | Post-validation + counsel review |
| Cohort cap of 40 in P1 | Support discipline; signal quality | P1 cohort exit criteria |
| Real-capital deployment | PCC v2 §8 gate | Validation pass |
| US user signup | Regulatory posture | US licensure decision |
| Affiliate / referral payouts | Anti-overclaim risk | Post-validation, structured guardrails |

Each of these is either a `02-company-overview/strategic-constraints.md` constraint or a `01-executive-summary/strategic-priorities.md` deferral. Re-litigating them outside of the documented amendment procedure produces drift, not progress.

---

## 9. Strategic invariants

Across all stages, three invariants hold and are not subject to per-phase optimization:

1. **Capital stays in the user's exchange account.** Custody is structurally rejected.
2. **User authorization is required for any trade arming.** Autonomy is structurally rejected.
3. **Real capital is gated until PCC v2 §8 passes.** Code-level enforcement; CI re-verification on every release.

Any feature proposal that conflicts with one of these invariants is rejected without further review. This is the single bright line in product strategy.

---

## 10. Cross-references

- Locked v1 §5: `business-plan/05-product-strategy.md`
- Tier matrix: `01-executive-summary/business-model-summary.md` §3
- Strategic constraints: `02-company-overview/strategic-constraints.md`
- Jobs-to-be-done emphasis matrix: `04-icp-and-segmentation/jobs-to-be-done.md`
- Differentiation framework: `05-positioning/differentiation-framework.md`
- PCC v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- MVP readiness checklist: `business-plan/_data/operations/mvp-readiness-checklist.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
