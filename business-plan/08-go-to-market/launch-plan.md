# Launch Plan

**Status:** Wave 2 · v1 · 2026-05-08
**Disclaimer:** Validation phase active. P1+ dates are gate-driven targets, not calendar commitments. Stop-the-line conditions extend any phase if triggered.
**Inherits from:** `business-plan/14-launch-roadmap.md` v1 LOCKED; `business-plan/_phase-2/_gtm/04-launch-sequencing-framework.md`; `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`

---

## 1. What "launch" means for CoinScopeAI right now

CoinScopeAI's launch is **not a single event**. It is a phased progression of go/no-go gates, each producing different evidence and unlocking different audience access.

| What people often mean by "launch" | What we actually mean | Where in our plan |
|---|---|---|
| "We're shipping the product to everyone" | A controlled cohort opens; broader public exposure follows only after the cohort signal accumulates | P1 → P2 |
| "We're announcing publicly" | A single P2 announcement, brand-voice reviewed, with one ≤25%/≤30-day promo tied to founder-cohort window | P2 (Aug–Sep 2026) |
| "We're going live with real money" | Real-capital deployment opens through a phased ramp only after PCC v2 §8 evidence accumulates | Post-validation, gated |
| "We're feature-complete" | Trader is at quality bar at P1; Desk Preview at P1 close; Desk Full v2 at P5 | P1 → P5 |

The rule, locked in §14.0: **"P1+ dates are gate-driven targets, not calendar commitments. Stop-the-line conditions extend any phase if triggered."** A passing date is not a passing gate.

Therefore: in this folder, "launch" refers to the **staged motion**, not a date.

---

## 2. Staged launch approach

Six stages mapped to the locked phase plan. Each has an entry gate and an exit gate; each produces specific evidence.

| Stage | Window | What ships | Audience | Exit gate (must clear to advance) |
|---|---|---|---|---|
| **S0 — Validation pass** | P0 (May 2026) | Engine running on Binance USDT-M Testnet; PCC v2 G1–G4 + §8 criteria evaluated | Internal only | All four PCC v2 gates pass + §8 Capital Cap criteria met + Validation_Phase_Exit_Memo filed |
| **S1 — Pre-launch readiness** | Late May → 2026-06-01 | Pricing page live; methodology page live; `/what-we-dont-do` live; cohort recruitment list closed; support inbox + SLA framework v1 in production | Founder + cohort candidates | Pre-launch checklist (§4) cleared end-to-end |
| **S2 — P1 soft launch (cohort)** | Jun–Jul 2026 | Trader-tier surface live for 40 founder-cohort users; founder-led onboarding; weekly cohort observation | 40 cohort users (curated) | 30-day soft-cohort floor + zero §14 stop-the-line + IB items at "stabilizing-acceptable" maturity |
| **S3 — P2 public launch (v1)** | Aug–Sep 2026 | Public signup opens; Desk Preview opens; founder-cohort 60-day window; one ≤25%/≤30-day P2 launch promo (optional) | UAE/MENA + global EN; US blocked | Trader stable in market + first §3.7/§3.8 data lands; Desk Preview at quality bar |
| **S4 — P3 stabilization** | Oct–Dec 2026 | Trader at scale; Desk Preview filling; CAC validation work | All non-US | All Trader-floor IB items cross to VTN + §3 v1.1 published + §11 model reconciled to actuals; D1 paid-acquisition unblock evaluated against PP7 |
| **S5 — Desk Full v2 launch** | P5 (Mar–May 2027) | Desk Full v2 opens; Desk Preview users migrate; per-seat scaling validated | Desk Full v2 cohort + small funds | Desk Full v2 cohort signal; per-seat density vs. base case |

**The rule:** advance only when the exit gate clears. If a stage is not ready by its target date, the stage extends (per the discipline locked in `06-product-strategy/mvp-vs-beta-vs-scale.md` §1).

---

## 3. Soft-launch vs. early access vs. broader launch

The locked v1 vocabulary, with operator-grade definitions for clarity.

### Soft launch (S2 — P1)

- **Audience:** 40 curated cohort users.
- **Recruitment:** Curated outreach via founder-led distribution (per `channel-prioritization.md` §2 C5).
- **Pricing:** Founder-cohort applied automatically (≈25–30% off, locked through one renewal cycle).
- **Posture:** Private; no public launch announcement; cohort references the product but the company does not announce it publicly.
- **Goal:** Cohort signal — retention, rule-respect, edge cases, churn-reason capture.

**RECOMMENDATION (DECISION NEEDED — pre-2026-06-01):** Curated outreach over open application. Reasons:

- Cohort quality is the cap; first-come-first-served lets noise in.
- Founder controls the persona mix (target ~30 P1 Omar / 8 P3 Layla / 2 P2 Karim).
- Application form invites application work without commitment; 40 named candidates from network are pre-qualified.
- Open application creates queue management overhead that competes with cohort onboarding work.

If counter-arguments emerge (e.g., insufficient candidates from network), a hybrid is acceptable: 30 named-outreach slots + 10 by application form with explicit qualifying questions.

### Early access (between S2 and S3 — late P1 / early P2)

- **Audience:** Cohort users plus a small expansion of founder-network candidates who didn't make the original 40.
- **Recruitment:** No public push; expansion is by invitation.
- **Pricing:** Founder-cohort still applied for new signups within the eligibility window.
- **Posture:** Quiet expansion; product is more visible but still not publicly announced.
- **Goal:** Stress-test the cohort observation cadence and support workflow at modest expansion (~60–80 total users).

This is **optional**; it can be skipped if S2 cohort signal is clean and S3 is ready on schedule.

### Broader launch / public launch (S3 — P2)

- **Audience:** Public, UAE/MENA + global EN. US blocked.
- **Recruitment:** Single launch announcement; methodology content cadence sustained; first time-bounded promo (optional, ≤25%/≤30 days).
- **Pricing:** Standard pricing live; founder-cohort 60-day window opens for new public signups.
- **Posture:** Anti-overclaim launch announcement; named-founder voice; published cohort evidence (anonymized as appropriate).
- **Goal:** Funnel volume meaningful enough for §11 model validation; CAC observation begins.

The rule: **"public launch" still excludes paid acquisition.** D1 paid-acquisition deferral remains in effect through P3 close at minimum.

---

## 4. Pre-launch checklist (S1)

Items that must clear before P1 cohort opens 2026-06-01. Each item is `[OWNER] — Action / Output`.

### 4.1 Product readiness

- [ ] `[FOUNDER] PRODUCT — PCC v2 G1–G4 + §8 Capital Cap criteria evaluated; pass evidence captured`
- [ ] `[FOUNDER] PRODUCT — Code-level testnet→mainnet hard gate verified uncircumventable in CI`
- [ ] `[FOUNDER] PRODUCT — Trader-tier surface (engine API + dashboard + journal + Telegram) at MVP quality bar`
- [ ] `[FOUNDER] PRODUCT — Risk gate at locked thresholds (10% DD / 5% daily / 10x lev / 5 max pos / 80% heat) wired and tested`
- [ ] `[FOUNDER] PRODUCT — Position sizer with math transparency surface; user-configurable thresholds above floors`

### 4.2 Pricing and packaging

- [ ] `[FOUNDER] PRICING — Pricing page renders all four tiers + per-seat openly per §6.6`
- [ ] `[FOUNDER] PRICING — Founder-cohort pricing applied to P1 cohort users at signup`
- [ ] `[FOUNDER] PRICING — Stripe configured for monthly + annual + per-seat; promo-code anti-stacking enforced`
- [ ] `[FOUNDER] PRICING — Validation-phase disclaimer visible on pricing page (per §6.10 Flag 2)`
- [ ] `[FOUNDER] PRICING — AED conversion display configured per §6.8 with the verbose tax-honesty footer`

### 4.3 Trust surfaces

- [ ] `[FOUNDER] TRUST — coinscope.ai/methodology page live; engine logic documented`
- [ ] `[FOUNDER] TRUST — coinscope.ai/what-we-dont-do reference page live (per §5.3.4)`
- [ ] `[FOUNDER] TRUST — PCC v2 published (`coinscope.ai/pcc-v2` or equivalent)`
- [ ] `[FOUNDER] TRUST — Validation_Phase_Exit_Memo template prepared for post-pass publication`
- [ ] `[FOUNDER] TRUST — Status / uptime page live`
- [ ] `[FOUNDER] TRUST — About page with named founder, sole-prop status disclosed honestly`
- [ ] `[FOUNDER] BRAND — Brand-voice enforcement skill in production`
- [ ] `[FOUNDER] BRAND — Anti-overclaim audit pass against all P1-shipping surfaces`

### 4.4 Onboarding

- [ ] `[FOUNDER] ONBOARDING — Sign-up → exchange-connection → first-value journey designed and tested per _phase-2/_onboarding/`
- [ ] `[FOUNDER] ONBOARDING — US-resident block at signup verified`
- [ ] `[FOUNDER] ONBOARDING — Sub-$5k disciplined "we'll be back" routing live`
- [ ] `[FOUNDER] ONBOARDING — Onboarding email sequence drafted, brand-voice reviewed, queued for cohort`

### 4.5 Support and incident readiness

- [ ] `[FOUNDER] SUPPORT — Support inbox + SLA framework v1 in production (per locked _phase-2/_support/)`
- [ ] `[FOUNDER] SUPPORT — Ticket routing + escalation rules documented and tested`
- [ ] `[FOUNDER] OPS — Vendor failure-mode runbooks reviewed; first dry-run executed`
- [ ] `[FOUNDER] OPS — Incident severity matrix in production; on-call playbook v1 live`
- [ ] `[FOUNDER] OPS — Incident dry-run executed end-to-end (synthetic vendor failure scenario)`

### 4.6 Cohort recruitment

- [ ] `[FOUNDER] GTM — Named cohort candidate list closed at ≥40 candidates`
- [ ] `[FOUNDER] GTM — Cohort outreach sequence sent and acknowledged by ≥40 candidates`
- [ ] `[FOUNDER] GTM — Cohort onboarding kickoff schedule confirmed for first 7 days post-launch`
- [ ] `[FOUNDER] GTM — Cohort observation cadence (weekly check-in template, structured feedback capture) prepared`

### 4.7 Legal / compliance

- [ ] `[FOUNDER + COUNSEL] LEGAL — No Investment Advice memo finalized (`_data/legal/No_Investment_Advice_Memo_v0_DRAFT.md` → v1)`
- [ ] `[FOUNDER + COUNSEL] LEGAL — Risk Disclosure v0 → v1 finalized (`_data/legal/Risk_Disclosure_v0_DRAFT.md`)`
- [ ] `[FOUNDER + COUNSEL] LEGAL — Terms of Service / Privacy Policy / DPA reviewed; UAE sole-prop posture honestly disclosed`
- [ ] `[FOUNDER + COUNSEL] LEGAL — US-block compliance language reviewed`

### 4.8 Measurement

- [ ] `[FOUNDER] METRICS — KPI feed live (per `business-plan/13-kpi-okr.md` v1)`
- [ ] `[FOUNDER] METRICS — Cohort attribution capture (signup source, channel, persona inference) live`
- [ ] `[FOUNDER] METRICS — Refund-reason capture in cancel/refund flow`
- [ ] `[FOUNDER] METRICS — MAVT (Monthly Active Validated Trader) flag wiring tested`

A pre-launch readiness review meeting (founder + counsel + any contractor support) is held within 7 days of 2026-06-01. Any unchecked item triggers either (a) close-out work + delay, or (b) explicit acceptance with documented mitigation in the decision log.

---

## 5. Launch readiness dependencies

Cross-functional dependencies that, if degraded, block a stage advance.

| Dependency | Owner | Stage(s) blocked | Mitigation |
|---|---|---|---|
| **PCC v2 §8 Capital Cap pass** | Founder | S0 → S1, all subsequent | Locked stop-the-line; if failure, P0 extends |
| **Code-level testnet hard gate** | Founder | All stages — never bypassed | CI verification on every release |
| **Vendor stack stability** (Binance, Stripe, CoinGlass, Tradefeeds, CoinGecko, Claude API) | Founder + vendor relationships | S2 → S3 onwards | Vendor failure-mode runbooks; vendor expansion at P2 only after P1 stable |
| **Founder bandwidth** | Founder | All stages | 12–22 hrs/week GTM cap during P1; remainder for product/support/ops |
| **Counsel readiness** | Founder + counsel | S1 → S2 (legal pre-launch); S3 → S4 (entity decision) | Counsel brief v2 in motion; entity decision per Strategic Priority #6 |
| **Support workflow capacity** | Founder | S2 → S3 onwards | SLA framework v1 sized to 40 cohort users; revise pre-S3 |
| **Brand-voice audit pass** | Founder + brand-voice skill | Every external-facing surface ship | Skill in production; review pass mandatory before publication |
| **Persona reconfirmation** (§3.7 interviews) | Founder | S3 → S4 (sustained content) | ≥12 interviews completed by P1 mid-cohort review |

If a dependency is yellow (partially ready), founder + decision-log entry covers the call. If a dependency is red, the relevant stage holds until cleared.

---

## 6. Soft-launch (S2) plan in detail

### 6.1 Day-by-day (first 7 days)

| Day | Action | Output |
|---|---|---|
| Day -1 (May 31) | Final go/no-go review against pre-launch checklist; final brand-voice audit pass; cohort onboarding kickoff schedule confirmed | Go decision logged; cohort users notified of Day 1 |
| **Day 1 (Jun 1)** | Cohort signup opens to the 40 named candidates; Stripe captures first signups; founder-cohort pricing applied | First signups; first onboarding kickoff calls |
| Days 2–4 | Onboarding kickoff calls continue (founder-led; ~10–15 min per cohort user); exchange connections completed; first signal exposure | Each cohort user has a working configuration by Day 4 |
| Days 5–7 | First week of operation; founder monitors cohort behavior + support inbox; Telegram alerts canonical | Day 7 observation note; any incidents logged |

### 6.2 Cohort observation cadence (Weeks 1–8)

- Weekly cohort observation note (founder-authored): retention, rule-respect, edge cases, churn-reason if any
- Bi-weekly cohort interview rotation: founder talks to ~5 cohort users per fortnight (structured 30-min calls)
- Mid-cohort review at Week 4: persona reconfirmation status, KPI snapshot, decision-log entry
- End-of-soft-launch review at Week 8 (~Jul 26): full cohort-cycle close; S2 → S3 exit gate evaluation

### 6.3 What is not done during S2

- No public launch announcement.
- No paid acquisition.
- No press outreach.
- No affiliate / referral push.
- No Desk Preview funnel optimization (Desk Preview is welcome to receive cohort users but not actively promoted).
- No Desk Full v2 mention beyond the public roadmap.
- No new channel additions beyond the prioritized P1 channels.

The discipline of S2 is **doing fewer things, more carefully, with closer observation.** Anything that would compromise that is deferred.

---

## 7. P2 public launch (S3) plan

### 7.1 Triggers (from §14.1)

S3 begins only after S2 exit gate clears:

- 30-day soft-cohort floor met
- Zero §14 stop-the-line conditions triggered during S2
- IB items at "stabilizing-acceptable" maturity
- Desk Preview at quality bar
- §3.7 persona reconfirmation completed (or in-flight with mid-cohort signal sufficient to advance)

### 7.2 The single launch announcement

Format: longform Substack + Twitter thread + email to existing cohort + landing-page update on `coinscope.ai`. **One coordinated event, one anti-overclaim review, one decision-log entry.**

Approved phrasing patterns (per `09-brand-messaging.md` and §14.4):

- *"After our P0 validation phase and a 40-user soft cohort, CoinScopeAI opens public signup."*
- *"Our Production Candidate Criteria pass evidence is published at `coinscope.ai/pcc-v2`."*
- *"For the next 60 days, founding-member pricing applies to new signups — locked through your first renewal cycle."*
- *"We do not deploy real capital outside our published phased ramp. Today we are running on Binance USDT-M Testnet for full evaluation."*

Rejected phrasing (anti-overclaim violations — restated for explicit reference):

- ~~*"We are now production-ready."*~~ unless §8 Capital Cap fully passed AND counsel-reviewed
- ~~*"Beta users saw [X% return]."*~~ — no performance claims from cohort data
- ~~*"Launch sale — limited time only!"*~~ — discount theatre
- ~~*"Get featured as a top user on our leaderboard."*~~ — no leaderboards
- ~~*"Refer 3 friends and unlock free Pro."*~~ — no affiliate push at P1–P2

### 7.3 The single P2 launch promo (optional)

Per `07-packaging-and-pricing/trial-and-discount-policy.md` §6:

- ≤25% off, ≤30-day window, auto-revert to standard at next renewal
- Does **not** apply to Desk Full v2 (preserve the v2 anchor)
- Does **not** stack with founder-cohort or annual prepay
- Disclosed with end date and post-revert price

If the founder-cohort 60-day window is judged sufficient incentive on its own, the launch promo is skipped. **DECISION NEEDED — pre-S3.**

### 7.4 Press / media

One placement at most. Founder-authored op-ed or named-author profile in a methodology-aligned outlet. Not a press blitz. Not a sponsored placement. **Selectivity is the message.**

---

## 8. Launch risks

Eleven failure modes with specific guards.

| # | Risk | Stage | Why it kills CoinScopeAI specifically | Guard |
|---|---|---|---|---|
| **LR1** | **Validation fails or is fudged** | S0 → S1 | Existential — anti-overclaim moat collapses | Stop-the-line; P0 extends; no S1 advance until §8 evidence captured honestly |
| **LR2** | **Cohort opens before pre-launch checklist clears** | S1 → S2 | First-week incidents under-resourced; trust damage | Hard gate at §4 checklist |
| **LR3** | **Cohort cap exceeded** | S2 | Support breaks; founder bandwidth fails; cohort signal degrades | 40-user cap enforced at signup form |
| **LR4** | **First incident handled poorly** | S2 | Disciplined-buyer judgment in first 90 days defines the brand | Vendor failure-mode runbook + post-incident postmortem published transparently |
| **LR5** | **Anti-overclaim drift in launch announcement** | S3 | Brand-voice review failure; trust collapse | Mandatory brand-voice audit pass before any S3 surface ships |
| **LR6** | **P2 launch coincides with vendor outage** | S3 | Audience surge meets degraded service; trust damage | Vendor expansion at P2 happens *after* public launch stabilizes; Tradefeeds/CoinGecko backups validated |
| **LR7** | **Public launch with Desk Preview not at quality bar** | S3 | Promise > delivery; tier matrix breaks | S2 → S3 exit gate requires Desk Preview at quality bar (PP6) |
| **LR8** | **Press blitz draws anti-ICP audience** | S3 | Mass crypto-press surfaces the wrong cohort | One placement only; methodology-aligned outlet only |
| **LR9** | **Paid acquisition triggered too early at P3** | S4 | CAC unvalidated; capital burn; cohort dilution | D1 — paid acquisition gated to PP7; LTV/CAC ≥ 3:1 floor |
| **LR10** | **Desk Full v2 announced before P5 readiness** | S5 | "v2" implies feature-complete that P5 may not deliver | Desk Full v2 launch only after S4 exit gate + P4 capability flow |
| **LR11** | **Performance claims surfaced from soft-cohort data** | Any | Anti-overclaim violation; testnet data does not justify performance claims | Locked — no performance language in any launch surface |

---

## 9. Suggested launch sequencing — summary table

| When | What ships | Who hears it | Who does NOT hear it | Decision needed by |
|---|---|---|---|---|
| **Late May 2026** | S0 validation pass; pre-launch checklist closeout | Internal | Public, press, broader network | Founder, end of P0 |
| **2026-06-01** | S2 P1 soft launch; 40-user cohort opens | 40 named candidates | Public, press | Founder, pre-2026-06-01 |
| **Jun–Jul 2026** | Cohort observation cadence; weekly notes; mid-cohort review | Cohort users | Public | Continuous |
| **Late Jul 2026** | S2 → S3 exit gate evaluation | Founder + cohort | Public until S3 confirmed | Founder, end of P1 |
| **Aug–Sep 2026** | S3 P2 public launch; founder-cohort 60-day window opens; optional ≤25%/≤30-day promo; one press placement | Public (UAE/MENA + global EN) | US, anti-ICP segments | Founder + brand-voice review, pre-S3 |
| **Oct–Dec 2026** | S4 P3 stabilization; CAC validation work; D1 paid-acquisition trigger evaluation | Public | Paid acquisition channels (until PP7) | Founder, P3 close |
| **Mar–May 2027** | S5 Desk Full v2 launch; per-seat scaling activates; Desk Preview migration | P3 Layla + small-fund segment | Anti-ICP segments, US | Founder + counsel, pre-P5 |

The principle: **each row's "who hears it" gates the next row's announcement.** No skipping a row to reach a faster public launch.

---

## 10. Cross-references

- §14 v1 LOCKED launch roadmap: `business-plan/14-launch-roadmap.md`
- PCC v2: `business-plan/_data/operations/Production_Candidate_Criteria_v2.md`
- Validation Phase Exit Memo template: `business-plan/_data/operations/Validation_Phase_Exit_Memo_TEMPLATE.md`
- Vendor Failure Mode Mapping v1: `business-plan/_data/operations/Vendor_Failure_Mode_Mapping_v1.md`
- Phase 2 GTM launch sequencing: `business-plan/_phase-2/_gtm/04-launch-sequencing-framework.md`
- GTM strategy: `08-go-to-market/gtm-strategy.md`
- Channel prioritization: `08-go-to-market/channel-prioritization.md`
- Trust-first growth: `08-go-to-market/trust-first-growth.md`
- Decision log: `business-plan/_decisions/decision-log.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-08.
