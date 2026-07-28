# Primary ICP

**Status:** Wave 1 · v1 · 2026-05-07 · INFERENCE-based pending §3.7 / §3.8 cohort data
**Companion to:** `business-plan/03-icp-segmentation.md` (locked v1, 2026-05-01; itself inference-tagged) — full persona card lives there
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file is the **operator-grade primary-ICP recommendation**. It commits to a single segment, explains why, and defines the operating shape of an ideal early account. It is decisive on purpose. The locked v1 §3 file frames three personas (P1, P2, P3); this file declares which one to target *first*, and how to treat the other two while the primary cohort is being built.

**Persona-name use:** Internal names (P1 Omar / P2 Karim / P3 Layla) are used inside this file for clarity. They must **not** appear in external copy — website, sales conversation, content, social, recruiting, fundraising. External phrasing per `05-positioning/positioning-statement.md` §4.

---

## 1. Recommended primary ICP

**Primary ICP: P1 — The Self-Taught Methodist (working name: "Omar").**

A disciplined retail crypto-perp trader, age 28–50, account size $20k–$150k typical, who built their methodology through deliberate study (Van Tharp, Schwager, position-sizing literature, Seykota commentary) before sizing up. Predominantly UAE/MENA-resident or global-EN-fluent. Not necessarily a coder. Has a written trading plan they have actually followed for 12+ months. Buys *process* and *enforcement*, not signals or autonomy.

**Default tier:** Trader $79/mo.

This is the canonical primary anchor for P0 validation through end of P1. It is not the only segment we will serve in P1; it is the segment the cohort, content, onboarding, and support are *led with*.

---

## 2. Why this segment should come first

Five reasons, ordered by leverage on the validation window and the locked priorities in `01-executive-summary/strategic-priorities.md`.

### 2.1 Highest match between locked Vision and observable buyer pain

Vision A — *capital preservation, by default* — is product-market fit against P1 Omar specifically. They already operate from a capital-preservation premise, they already do manual gating, and they already buy tools that respect their framework. The product's first-class UI (drawdown, daily loss, leverage, heat, position count) maps 1-to-1 to surfaces they already maintain by hand.

### 2.2 Lowest-friction acquisition under founder-led distribution

P1 Omar is reachable through methodology-focused channels (closed Discords, Substacks, applied-quant Twitter, position-sizing reading lists). These channels reward founder credibility and earned content. They punish performance promises and "10x your account" language — which CoinScopeAI structurally cannot make. The match between who CoinScopeAI is and who P1 Omar listens to is high.

### 2.3 Strongest fit with anti-overclaim posture

P1 Omar specifically rewards anti-overclaim language. They have been pitched to by signal services and reject the genre. They notice and value *evidence-led* claims, *methodical* writing, and *transparent* refusal patterns. The voice posture that constrains us with other segments (P2 Karim is neutral on it; P3 Layla expects formality) is a feature with P1 Omar.

### 2.4 Best signal-to-noise on the validation cohort

The 40-user P1 cap means the cohort needs to be informative, not just full. P1 Omar produces high-quality cohort signal because:
- They use the product carefully (low support burden per user)
- They surface real edge cases (multiple positions, after-hours setups, news-driven volatility)
- They give specific, evidence-cited feedback rather than generic complaints
- Their retention behavior at month 1, 2, 3 is a clean signal on whether the product *enforces what they already do*

### 2.5 Cleanest persona-to-tier alignment

P1 Omar at Trader $79/mo is the tier-matrix anchor. The expected pattern (working hypothesis): most P1 Omars stay at Trader; some graduate to Desk Preview around the ~$50k-across-multiple-positions threshold where manual processes break (per locked v1 §3.2). P1 cohort data will confirm or revise.

---

## 3. Characteristics of the ideal early user/account

| Dimension | Ideal account profile | Why this matters |
|---|---|---|
| **Age** | 28–50 | Matches earned-discipline cohort |
| **Account size** | $20k–$150k typical (sweet spot $50k+) | Above the threshold where manual gating breaks; below the threshold where Desk Preview is forced |
| **Geography** | UAE / MENA primary; global EN secondary | Matches operating posture; non-US |
| **Primary occupation** | Professional or self-employed (lawyer, doctor, business owner, mid-level engineer, consultant) — not necessarily coder | Reflects deliberate-study origin; daytime constraints make 24/7 monitoring software valuable |
| **Trading frequency** | Active (weekly+); not day-trading-as-content | High engagement without alert-fatigue mismatch |
| **Methodology** | Has a written trading plan followed 12+ months; uses position-sizing math; reads the canon | Compatible with risk-gate UI; does not need education on why discipline matters |
| **Toolchain today** | Spreadsheet/Notion journal; exchange-native interface; possibly Edgewonk-equivalent on the equities side | The "discipline lives in tools the user doesn't love" gap CoinScopeAI fills |
| **Buying behavior** | Pays for tools; values craft over hype; reads long-form before purchase | High signal in evaluation; high commitment after purchase |
| **Network** | Member of one or more closed methodology-focused communities | Word-of-mouth amplification potential under founder-led distribution |
| **Anti-fit reject** | Wants to be told what to trade; rejects external constraints; sub-$5k account; copy-trading audience; US-resident | Each is an explicit anti-persona signal. Filter at signup (sub-$5k, US-resident, copy-trading language); detect in conversation (override-seeking, alpha-seeking) |

---

## 4. What they care about most

In inferred priority order (working hypothesis pending §3.7 data):

1. **Their methodology is respected, not replaced.** Configurable gates that honor their thresholds. The product is a *tool*, not a *system that overrides them*.
2. **Math transparency.** Show the position-sizing formula, the inputs, the outputs. If the math is wrong, they will notice. Hiding it is a fail signal.
3. **R-multiple and rule-violation reporting.** Their journal already tracks this manually; software that surfaces it cleanly is high-value.
4. **24/7 monitoring without alert fatigue.** Canonical Telegram alerts; rate-limited; gated by relevance and regime.
5. **Trust signals.** Anti-overclaim writing; testnet-only honesty; founder credibility; PCC v2 published criteria; transparent incident response.
6. **Gateway to multi-account or higher-tier capability.** Most stay at Trader; some upgrade path to Desk Preview for multi-account / read API.

---

## 5. How they evaluate tools like CoinScopeAI

Their evaluation is **slow, reading-heavy, and skeptical-by-default**. The pattern, inferred from the locked v1 §3 persona card (un-validated until §3.7 data lands; all timing values below are working estimates):

| Stage | Behavior | Time | What converts |
|---|---|---|---|
| Discovery | Peer recommendation in closed community, or long-form content via Substack / Twitter | Days–weeks | Content that demonstrates the team understands position-sizing math |
| First-look | Reads the website thoroughly; checks for performance promises (red flag) | Hours | Anti-overclaim language; transparent state of validation |
| Free-tier evaluation | Activates Free; plays with scanner sample; checks regime + confidence reasoning | Days–weeks | First-value experience pre-billing; Free is genuinely useful |
| Trial / paid evaluation | Connects exchange (read-only first if possible); runs in parallel with manual workflow | 2–6 weeks | Configurable gates that honor their thresholds; math transparency |
| Commitment | Subscribes to Trader; eventually moves journal to CoinScopeAI; references in their network | Weeks–months | Consistent product behavior; no overclaim; clean incident response |

The implication (working hypothesis): **conversion is earned, not closed**. There is no expected "demo and discount" path with this segment. The cohort cap of 40 in P1 is well-matched to this evaluation pattern — it gives the founder time to onboard each user thoughtfully.

---

## 6. What they need to trust before paying

Trust requirements are explicit and observable:

| Trust requirement | How CoinScopeAI provides it | Where it shows up |
|---|---|---|
| The team understands the math | Long-form content with formula transparency; position-sizing explainer; R-multiple reporting | Content motion, dashboard, journal |
| The product respects their framework | Configurable gates; user-defined thresholds; "bring your own framework" copy | Onboarding, gate configuration UI |
| Validation status is honest | Testnet-only honesty; PCC v2 publication; anti-overclaim posture | Header disclaimer, about page, all surfaces |
| API-key safety | Least-privilege scopes; "no withdrawal scope ever"; explicit copy at exchange-connection step | Onboarding flow |
| Operational discipline | Incident transparency; postmortems in product-tier voice; runbooks before P2 | Incidents, status page |
| No performance promises | "No production-ready claim until §8 passes"; no leaderboards; no testimonials presented as endorsement | Brand voice, all surfaces |
| Founder credibility | UAE-resident, MENA-rooted; founder named (Mohammed) and contactable; sole-prop status disclosed honestly (not hidden); consistent voice across surfaces | About page, founder content, Telegram |

The aggregate test: **a careful P1 Omar reads the website, the about page, and the locked PCC v2 — and finds nothing that contradicts what they already believe a serious product should look like.**

---

## 7. What success looks like for them

Success for P1 Omar (as the buyer; this is the user-side success definition, not the company-side metric):

- Their drawdown stays inside their declared threshold across an entire month
- Daily-loss halts trigger correctly when needed and stay quiet otherwise
- Their journal has clean R-multiple reporting and rule-violation tagging
- They sleep through volatile sessions because monitoring is automated and alerts are canonical
- They reference the product to one or two peers in their closed methodology community without it feeling like a recommendation they'll regret
- Position-sizing math is transparent and matches their hand-calculation
- After 90 days, they have stopped maintaining their parallel manual journal

Operationalized as cohort metrics that belong in `13-kpi-okr.md`:

- 30-day retention ≥ TBD (**DECISION NEEDED** explicit threshold)
- Monthly Active Validated Trader (MAVT) flag set
- ≥1 referral or unprompted mention per N users by day 90 (**DECISION NEEDED** explicit threshold)
- Manual-journal abandonment as a leading indicator of upgrade potential

---

## 8. What would make them churn

Five explicit churn triggers, in inferred order of likelihood (un-validated until §3.7 data; all recovery-window and detection-time values below are working estimates):

1. **Configuration / implementation bug — gates fire on system defaults rather than user-configured thresholds.** This is an implementation failure, not a positioning failure (positioning failures are caught upstream at brand-voice review). Recovery: code fix + threshold-respect verification in CI. Trust damage: low if fixed within ~30 days, high if pattern observed.
2. **Math is wrong** — position-sizing or R-multiple math diverges from the user's hand-calculation. Expected detection within ~2 weeks of paid-evaluation use. Recovery: math correction + transparent postmortem. Trust damage: high; this is a category-fail.
3. **Alert fatigue** — Telegram alerts are noisy or non-canonical. Recovery: alert tuning, rate-limit, dedup per `alerting-and-user-experience` skill. Trust damage: low–medium.
4. **Anti-overclaim drift** — copy on a marketing page or in a launch announcement reads as "performance promise" or "guaranteed" language. Recovery: brand-voice review pass + correction + acknowledgement. Trust damage: high if pattern observed; low if isolated and corrected.
5. **Unhandled incident** — vendor outage or engine bug surfaces during their session and is not transparently communicated. Recovery: postmortem + runbook update. Trust damage: medium if first incident handled well; high if pattern observed.

The pattern across all five: **trust damage is recoverable for first-time issues handled openly; cumulative if pattern emerges**. P1 Omar specifically rewards companies that own their failures.

---

## 9. Operating implications for the rest of the plan

| Plan area | Implication for primary ICP P1 Omar |
|---|---|
| Positioning (`05-positioning/`) | Trader operating system as primary frame; emphasize *enforcement of your discipline*, not *automation of trades* |
| Product strategy (`06-product-strategy/`) | Configurability of gates is non-negotiable; math transparency is non-negotiable; R-multiple journal is high-priority |
| Pricing (`business-plan/06-pricing-monetization.md`) | Trader $79 is the working anchor; founder-cohort price applied to the 40 P1 users; revisit at P1 cohort review |
| Onboarding (`business-plan/_phase-2/_onboarding/`) | First-value pre-billing; exchange connection with least-privilege scopes; framework-respect copy at gate-config step |
| Support (`business-plan/_phase-2/_support/`) | Methodical, terse, technically-fluent responses; product-tier voice; no marketing language in replies |
| Brand (`business-plan/09-brand-messaging.md`) | Locked phrasing list; no leaderboards; no testimonials presented as endorsement; long-form content over short-form hype |
| GTM (`business-plan/07-gtm-strategy.md`) | Methodology-focused channels (Substack, applied-quant Twitter, closed Discords); founder-led distribution; no paid acquisition pre-CAC |
| KPIs (`business-plan/13-kpi-okr.md`) | MAVT north-star; 30-day retention; manual-journal abandonment; referral rate by day 90 |

---

## 10. Cross-references

- Locked v1 §3 persona card (full): `business-plan/03-icp-segmentation.md` §3.2 Persona 1
- Locked v1 §4 problem and value prop: `business-plan/04-problem-value-prop.md`
- Decision log (locked primary ICP framing): `business-plan/_decisions/decision-log.md`
- Anti-personas: `business-plan/03-icp-segmentation.md` §3.0 + `04-icp-and-segmentation/secondary-icps.md` §6
- Strategic priorities (P4 persona interviews): `01-executive-summary/strategic-priorities.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
