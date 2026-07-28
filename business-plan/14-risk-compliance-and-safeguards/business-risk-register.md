# Business Risk Register

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]
**Inherits from:** `business-plan/12-risk-compliance-trust.md` v1 LOCKED (41-entry register, 7 categories, severity + status framing, anti-probability discipline)

---

## 1. Framing — severity + status, not severity × probability

Per §12.0 inherited discipline: probability framings sound precise but are inferred poorly pre-revenue. **Risks are tracked by severity (impact if triggered) + status (where the risk currently sits).**

| Severity | Definition |
|---|---|
| **5 — Catastrophic** | Existential to the business; recovery-path uncertain |
| **4 — Severe** | Material business impact; recovery requires phase extension or strategy revision |
| **3 — Significant** | Discrete operational impact; recovery within plan |
| **2 — Moderate** | Operational nuisance; recovery within ops cadence |
| **1 — Low** | Routine; absorbed without business impact |

| Status | Definition |
|---|---|
| **Monitoring** | Latent risk; signs not present; tracking only |
| **Active** | Signs present; mitigation engaged; not yet triggered |
| **Triggered** | Event occurred; contingency or stop-the-line invoked |
| **Resolved** | Event handled; lessons captured; back to monitoring |

This file is the **operator-grade restatement** of the §12 register, organized by business decision area rather than by inherited section. The full 41-entry register lives in §12. Here we present the highest-severity risks per category, with explicit early-warning indicators and mitigation direction the founder uses for go/no-go calls.

---

## 2. Key business risks (top 10 — ranked by severity-then-leading-criticality)

| Rank | Risk | Sev | Status | Why it ranks here |
|---|---|---|---|---|
| **B-1** | **PCC v2 §8 Capital Cap fails or is fudged at validation** (R-001 + R-013 inherited) | 5 | Monitoring | Existential — anti-overclaim moat collapses; brand irrecoverable |
| **B-2** | **Engine bug compromises capital-preservation primitives** (R-013) | 5 | Monitoring | Math wrong is category-fail; trust collapse from disciplined cohort |
| **B-3** | **MENA regulator classifies CoinScopeAI as advisory or broker requiring license** (R-001) | 5 | Monitoring | Forces entity restructure or geography pivot at the worst possible time |
| **B-4** | **Founder unavailable >2 weeks** (R-020) | 5 | Monitoring | Solo-founder bus factor; ops cease without handover protocol |
| **B-5** | **Validation cohort demonstrates marginal/zero edge** (R-017) | 5 | Monitoring | Thesis intact, demonstration fails; company-survival mode |
| **B-6** | **Anti-overclaim drift — production-ready claim before §8 passes** (R-002 + brand drift category) | 4 | Monitoring | One viral overclaim undoes months of discipline |
| **B-7** | **Vendor outage during P1/P2 cohort observation** (R-008) | 4 | Monitoring | Cohort signal degraded under audience visibility |
| **B-8** | **CoinGlass dual customer-vendor relationship reframes** (R-007) | 4 | Monitoring | Pricing change, product expansion, or partnership reframe |
| **B-9** | **Persona invalidation — §3.7 interviews show locked persona is wrong** (R-016) | 4 | Active (interviews in flight) | Pricing / positioning / GTM all built on personas |
| **B-10** | **AI-trading category trust collapse** (R-027) | 4 | Monitoring | Industry-level event taints CoinScopeAI by adjacency |

The full 41-entry register in §12 covers another 31 entries at severity 1–3 plus secondary 4s. The founder's daily attention budget orbits the top 10; the rest is reviewed quarterly.

---

## 3. Product risks

Risks specific to the engine, the dashboard, and the canonical surfaces.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **P-1** | Engine bug compromises gate / position sizer / kill switch (R-013) | 5 | Monitoring | Comprehensive test suite; CI verification; audit log on every engine decision; §10.2 incident-response runbook | Cohort report flags rule-violation rate spike; engine logs show gate firing at unexpected thresholds |
| **P-2** | Cohort drawdown spike beyond §8 thresholds (R-014) | 5 | Monitoring | §13.4 daily monitoring during validation; engine kill-switch enforces user-level thresholds | Drawdown approaches 8% account-level on multiple cohort users in a single session |
| **P-3** | Cohort gate-rejection acceptance <50% (R-015) | 4 | Monitoring | Investigate cause: tuning / recruiting drift / UX / fundamental ICP mismatch | User overrides exceed 50% sustained over 7 days |
| **P-4** | Trader-floor IB items fail to cross VTN by P3 end (R-018) | 3 | Monitoring | Soft-cohort observation produces VTN graduation evidence; engineering capacity allocated | Engineering velocity <80% planned in any 4-week window during P1–P2 |
| **P-5** | Desk Full v2 RM→IB items slip (R-019) | 3 | Monitoring | P4 contractor scenario funded; weekly status review | Contractor not engaged by M7; multi-account dashboard not at IB by M8 |
| **P-6** | Signal-quality bug producing wrong regime / confidence / gate result (new) | 5 | Monitoring | Test-and-simulation lab regression coverage; cohort report cross-checks; per-incident postmortem | User reports converge on a regime / gate / sizing anomaly within a 24h window |
| **P-7** | Telegram bot delivery degradation (R-008 / vendor scope) | 3 | Monitoring | Dashboard remains primary; Telegram is companion; rate-limiting + dedup per `alerting-and-user-experience` skill | Multi-user reports of missed alerts within a single session |

---

## 4. Trust / reputation risks

Risks that damage the moat — anti-overclaim discipline, founder credibility, brand congruence.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **T-1** | "Production-ready" claim before §8 passes (brand drift) | 5 | Monitoring | Brand-voice enforcement skill in production; review pass before any external claim | Single instance of forbidden phrasing on any external surface (per `13-support-and-trust-ops/public-claims-guardrails.md`) |
| **T-2** | Performance language drift (testnet results published) | 5 | Monitoring | Anti-overclaim audit on every shipping surface; locked phrasing list | Any external surface contains a number or % describing user trading outcomes |
| **T-3** | Solo PM regulatory line drift (R-002) | 4 | Monitoring | Quarterly copy audit; explicit objection table; messaging discipline | Desk Preview / Desk Full v2 copy contains "fund" / "AUM" / "performance fee" framing |
| **T-4** | Anti-ICP cross-promotion (signal groups, copy-trade) | 4 | Monitoring | §5.3.3 lock; brand-voice review on partnership candidacy | Co-marketing proposal accepted without brand-voice gate |
| **T-5** | Cumulative anti-overclaim drift via affiliate/influencer arrangements | 4 | Monitoring | Affiliate program locked off at P1–P2; influencer marketing anti-channel | Any compensated external author publishes on CoinScopeAI's behalf |
| **T-6** | Testimonial presented as endorsement (without explicit consent + brand-voice + counsel review) | 4 | Monitoring | Locked anti-claim; testimonials require triple-review pass | User quote appears on a public surface without the audit log |
| **T-7** | Founder identity / sole-prop status hidden or downplayed | 3 | Monitoring | About page names founder; sole-prop status disclosed honestly | Re-design of about page removes sole-prop disclosure |
| **T-8** | First incident postmortem missed or sanitized | 4 | Monitoring | Postmortem cadence locked at severity ≥ medium; published transparently | First medium-severity incident closes without published postmortem within 7 days |

---

## 5. Provider / exchange dependency risks

Risks from the vendor stack that supports the engine.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **V-1** | Binance USDT-M API outage during P1/P2 cohort observation (R-008 specific) | 4 | Monitoring | Vendor failure-mode runbook; status page comms within 15 min; engine fallback active | Binance status page shows degradation; engine monitoring detects request weight saturation |
| **V-2** | CoinGlass pricing change or product expansion into our space (R-007) | 4 | Monitoring | Quarterly relationship review; vendor-swap optionality (alternate liquidations feed) | API pricing increase >$200/mo from baseline; CoinGlass announces a direct user-facing competitor product |
| **V-3** | Tradefeeds integration still STN at P3 (R-010) | 3 | Active | Alternate sentiment-data provider scouted; replace if Tradefeeds fails to cross IB→VTN | Tradefeeds at IB and not graduating by mid-P2 |
| **V-4** | Stripe processing fees exceed 3.5% blended assumption (R-011) | 2 | Monitoring | Quarterly Stripe fee actuals review; consider Paddle merchant-of-record if compliance burden grows | Actual blended fees >4.5% sustained for 60 days |
| **V-5** | Bybit deferred to P2; later vendor expansion friction | 2 | Monitoring | Phase map keeps Bybit at P2; P1 narrow stack proves durability first | Founder pressured to add Bybit before P1 close — refused per phase map |
| **V-6** | Telegram Bot API access changes (rate limits, auth) | 2 | Monitoring | Dashboard remains primary; Telegram is companion | Telegram-side policy notice; sustained delivery failures |
| **V-7** | Claude API throttling or pricing change | 2 | Monitoring | Minimal Claude use during P1; usage held deliberately small | Claude Anthropic-side policy or pricing change |
| **V-8** | Vendor contractual exposure (Binance / CoinGlass / Stripe ToS changes) | 3 | Monitoring | Monitor vendor ToS changes; counsel-review for material updates | Vendor publishes ToS update affecting our usage pattern |

---

## 6. Support / ops risks

Risks in the operational layer — support load, incident response, billing, founder bandwidth.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **O-1** | Founder bandwidth fails under cohort + support + product simultaneously (R-022 inherited) | 4 | Active | Phased GTM allocation; contractor support frees engineering at P4; weekly time tracking | Content cadence lags >30% for 2 consecutive weeks; SLA breach >10% in any week |
| **O-2** | Support SLA breach in first 90 days post-P1 launch | 4 | Monitoring | Published SLAs realistic; internal targets ~30% tighter; severity-driven prioritization | First-response SLA missed on >5% of P1 cohort tickets |
| **O-3** | First incident handled poorly under cohort observation pressure | 5 | Monitoring | Vendor failure-mode runbook dry-run pre-P1; incident comms templates committed | Status page entry delayed >15 min for P1 / >30 min for P2 |
| **O-4** | Refund processing friction (manual founder action vs. self-serve) | 3 | Active (likely) | Stripe-clean refund flow before P1; honor 14-day money-back without arguing | First refund request takes >24h to process |
| **O-5** | Support contractor (when added at v2) replies voice-incongruent | 3 | Monitoring | Brand-voice skill audit on every reply; founder-approval until quality bar holds | Single reply ships without brand-voice review pass |
| **O-6** | Engine documentation insufficient for emergency-contact handover (R-023) | 4 | Monitoring | Quarterly documentation audit; runbooks in Notion; secrets vault accessible | Documentation audit reveals gaps preventing 1-week handover |

---

## 7. Pricing / GTM risks

Risks in commercial decisions — pricing locks, channel choices, launch sequencing.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **G-1** | Free → Trader conversion below 3% downside (R-029) | 4 | Monitoring | §3.7 interview validation; §3.8 cohort observation; weekly conversion tracking | Free → Trader conversion <3% over any 30-day window post-P2 |
| **G-2** | Per-seat density at Desk Full v2 below 1.5/2.0 downside (R-030) | 3 | Monitoring | Time-varying base case; KPI tracking | Average seats per Desk Full v2 account <1.5 in first 90 days post-launch |
| **G-3** | Desk Preview → Desk Full v2 migration <50% (R-031) | 3 | Monitoring | KPI tracking; first-look pricing; migration discount | Migration rate <50% sustained over first 60 days post-P5 |
| **G-4** | Premature paid acquisition trigger before PP7 holds | 4 | Monitoring | D1 deferral hard gate; LTV/CAC ≥ 3:1 floor | Founder considers paid acquisition before M5 + CAC validation evidence |
| **G-5** | Surprise mid-cycle reprice damages trust | 4 | Monitoring | Pricing locks ≥6 months post-validation; any reprice ≥30 days advance notice | Internal pressure to reprice before lock window closes |
| **G-6** | Founder-cohort framing drifts toward "permanent" | 4 | Monitoring | Locked language: "founding-member pricing — locked through your first renewal cycle" | Marketing copy uses "lifetime" / "forever" / "always" |
| **G-7** | Discount theatre at P2 launch (excess promo) | 3 | Monitoring | Maximum 25% off, ≤30-day window, no Desk Full v2; brand-voice review | Multiple promos chained; promo on Desk Full v2; promo extends past 30 days |
| **G-8** | Anti-channel breach (influencer / affiliate / signal-group bundling) | 5 | Monitoring | §5.3.3 lock; brand-voice review on every external-author arrangement | Compensated external author proposal reaches founder approval |

---

## 8. Execution risks

Risks in the delivery layer — phase advancement, contractor engagement, fundraising sequencing.

| ID | Risk | Sev | Status | Mitigation direction | Early-warning indicator |
|---|---|---|---|---|---|
| **E-1** | Phase advance happens on calendar rather than on gate evidence | 5 | Monitoring | §14 gate-driven progression; decision log entry per advance; founder discipline | Phase advance occurs without exit-gate criteria documented as met |
| **E-2** | Solo-founder bus factor at P4 highest engineering load (R-021) | 4 | Active (mitigated) | 2 engineering contractors funded ~3 months at $48k spike per Scenario 3 | Contractors not engaged by M7 |
| **E-3** | Counsel engagement delay blocks P1 launch | 4 | Active | Counsel selection in flight; Phase A scope defined | Counsel not selected by mid-May 2026 |
| **E-4** | Post-validation entity decision delayed | 3 | Monitoring | Decision targeted post-P0 pass; Strategic Priority 6 | Post-validation, no entity decision within 60 days |
| **E-5** | Fundraising opens on projections rather than cohort data | 4 | Monitoring | §15 narrative refresh post-validation; ask calibrated to cohort signal | Fundraising materials surface before P1 cohort signal accumulates |
| **E-6** | Capacity drain from non-priority work (Bybit early, mobile app, Arabic UI) | 3 | Monitoring | Strategic Priority deferrals D1–D12 enforced; founder discipline | Founder spends >10% of any week on a deferred priority |
| **E-7** | Decision-log discipline lapses | 3 | Monitoring | Single canonical decision log; entries per phase advance and major decision | Decision log not updated for >14 days during a phase advance |

---

## 9. Severity / status — at-a-glance summary

| Severity | Top risks |
|---|---|
| **5 — Catastrophic** | B-1 (validation pass), B-2 (engine bug), B-3 (regulator advisory), B-4 (founder unavailable), B-5 (cohort marginal edge), P-1 (engine compromises gate), P-2 (cohort drawdown), P-6 (signal quality), T-1 (production-ready overclaim), T-2 (performance language), O-3 (first incident handled poorly), G-8 (anti-channel breach), E-1 (phase advance on calendar) |
| **4 — Severe** | B-6 through B-10 + multiple per-category 4s (T-3, T-4, T-5, T-6, T-8, V-1, V-2, O-1, O-2, O-6, G-1, G-4, G-5, G-6, E-2, E-3, E-5) |
| **3 — Significant** | Rest of register; reviewed quarterly |

The 4–5 severity entries are the founder's daily attention budget. Severity 1–3 entries are reviewed in weekly cohort observation notes and monthly business review.

---

## 10. Early-warning indicator dashboard

The most useful indicators across the register — what the founder watches every week.

| Watch | Signal | Risk it leads |
|---|---|---|
| **Brand-voice review log** | Any flagged-but-not-corrected entry | T-1, T-2, T-3, T-6 |
| **Cohort observation note** | Rule-violation rate spike; gate override rate >50%; drawdown approaching 8% | P-1, P-2, P-3, B-5 |
| **Engine logs** | Gate firing at unexpected thresholds; signal quality anomaly reports converging | P-1, P-6 |
| **Vendor status feeds** (Binance, CoinGlass, Tradefeeds, CoinGecko, Stripe, Telegram, Claude) | Any status not green | V-1, V-2, V-3, V-6, V-7 |
| **Vendor pricing newsletters / subscription notifications** | API pricing change > $200/mo; vendor product announcement | V-2 (CoinGlass especially) |
| **Counsel news subscription / regulator publications** | Public statement re: virtual-asset advisory licensing in MENA | B-3 (R-001) |
| **Support inbox volume** | Daily ticket count crossing capacity threshold | O-1, O-2 |
| **First-response SLA report** | Any first-response missed within coverage hours | O-2 |
| **Founder time log** | >50 hours/week sustained for 4 weeks | B-4, O-1 |
| **Conversion funnel report** | Free → Trader <3% over 30-day window | G-1 |
| **Brand-voice review log size** | Multiple flagged surfaces in a single quarter | Indicates pattern (T-1 / T-2 cumulative) |
| **Phase exit-gate checklist** | Any exit gate at "yellow" or "red" pre-advance | E-1 |
| **Decision log entry cadence** | No entry for >14 days during a phase advance | E-7 |

---

## 11. Mitigation discipline rules

Inherited and restated for operator clarity:

1. **Severity-5 risks have a documented response plan** — not just "we'll handle it"; explicit comms / ops / legal steps committed pre-trigger.
2. **Severity-4 risks have a named owner** — founder or contractor responsible for monitoring; entry in `_decisions/decision-log.md` if unstaffed.
3. **A risk's status escalates from Monitoring → Active when a second leading indicator fires** within a 14-day window.
4. **A risk's status changes to Triggered only when an event occurs** — speculative is not Triggered.
5. **A Triggered risk freezes adjacent decisions** until contingency plays out.
6. **Mitigation lessons are logged** in the decision log; they update the register's mitigation column.

---

## 12. Cross-references

- §12 v1 LOCKED canonical: `business-plan/12-risk-compliance-trust.md`
- §14 v1 LOCKED launch roadmap (stop-the-line conditions): `business-plan/14-launch-roadmap.md`
- §16 v1 LOCKED scenario planning (anti-probability framing): `business-plan/16-scenario-planning.md`
- Production Candidate Criteria v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Vendor failure-mode mapping: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Compliance assumptions (this folder): `business-plan/14-risk-compliance-and-safeguards/compliance-assumptions.md`
- Safeguards framework (this folder): `business-plan/14-risk-compliance-and-safeguards/safeguards-framework.md`
- Regulatory question list (this folder): `business-plan/14-risk-compliance-and-safeguards/regulatory-question-list.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
