# SUPPORT — User Issue Taxonomy

**Task:** `[DOC] SUPPORT — User Issue Taxonomy`
**Type:** NOW
**Owner:** Strategy CoS
**Status:** DRAFT v0.1 — exhaustive issue catalogue with default severity, resolution path, common-cause notes
**Anchored to:** `02-support-sla-framework.md` severity matrix; `03-ticket-routing-and-escalation-rules.md` routing table; ONBOARDING `_onboarding/05-friction-audit-across-current-flow.md` (predicted issue load); §12 vendor failure-mode mapping; PACKAGING / PRICING workstream artifacts (gating + billing surfaces).

---

## 1. Taxonomy structure

Every ticket is categorized at triage with:

- **Category** — top-level area (e.g., Account, Billing, Signal, Vendor)
- **Subcategory** — specific issue within area
- **Default severity** — P1 / P2 / P3 / P4 per `02-support-sla-framework.md`
- **Owner (v1)** — founder for all v1 tickets per `01-support-operating-model.md`
- **Owner (v2+)** — per `03-ticket-routing-and-escalation-rules.md` §2
- **Resolution path** — primary path to resolution
- **Common cause** — most-likely-cause notes for triage acceleration
- **Deflection-eligible** — yes/no whether KB article or in-product copy could deflect

Category codes (used in ticket tags):
- `ACC` — Account / authentication / region
- `EXC` — Exchange connectivity (Binance / future Bybit)
- `SIG` — Signal interpretation, regime, gate decision
- `RSK` — Risk-gate behavior + configuration (T+)
- `JRN` — Journal feature (T+)
- `ALT` — Alerts (in-app, email, Telegram)
- `MAC` — Multi-account / portfolio (DP+)
- `RPT` — Reporting (PDF, audit-grade)
- `BIL` — Billing, payments, refunds, subscriptions
- `ENT` — Entitlement / gating leak / tier confusion
- `VND` — Vendor outage / dependency
- `INC` — Incident (engine-side, security, data)
- `PCC` — Production Candidate Criteria / real-capital questions
- `REG` — Regulatory / counsel-routed
- `BUG` — Bug report (functional or cosmetic)
- `FRQ` — Feature request
- `MSG` — Brand / messaging / press / partnership outreach
- `ANT` — Anti-ICP outreach (signal-group / copy-trade promotion)

---

## 2. Issue catalogue

### Account / authentication / region (`ACC`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `ACC.SIGNUP_BLOCKED` — region check denied legitimate signup | P3 | Verify IP geolocation accuracy; manual override if confirmed legitimate non-US user | VPN to US server; IP misclassification | No — case-by-case |
| `ACC.EMAIL_NOT_RECEIVED` — verification email not delivered | P3 | Resend; check spam; verify email address typo; confirm SMTP delivery | Spam filter; typo at signup | Yes — KB article |
| `ACC.PASSWORD_RESET` — password reset request | P3 | Self-serve reset flow; manual help if flow fails | User forgot password | Yes — self-serve flow |
| `ACC.UNAUTHORIZED_ACCESS_SUSPECTED` — user reports possible account compromise | **P1** | Per Escalation A; immediate account suspension + Eng security review | Phishing; credential reuse | No |
| `ACC.MFA_QUESTION` — questions about 2FA / authentication | P3 | If 2FA exists at v1 (REQUIRED INPUT) — guidance; if not — deferred | Awareness gap | Yes — KB article |
| `ACC.ACCOUNT_DELETION` — user requests account deletion | P3 | Self-serve where possible; manual purge per data-retention policy (§6.7) | User churning | Yes — self-serve flow |
| `ACC.DATA_EXPORT` — GDPR or general data export request | P3 | Per §6.7 + GDPR window if applicable | Compliance request | Yes — KB article |

### Exchange connectivity (`EXC`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `EXC.API_KEY_INVALID` — API key not authenticating | P3 | Walk through key creation; verify scope (read-only); verify testnet/mainnet match | Key typo; wrong testnet/mainnet endpoint; API key not yet activated | Yes — KB article + in-product help |
| `EXC.WRITE_PERMISSION_BLOCKED` — user submitted write-scope key | P3 | Block per `_onboarding/03` Step 8; instruct read-only key creation | User created broad-scope key | Yes — KB article |
| `EXC.TESTNET_VS_MAINNET_CONFUSION` — user used wrong endpoint | P3 | Explain testnet/mainnet distinction per PCC v2 §8; switch endpoint | Documentation gap | Yes — KB article + UI clarity (audit row 3.3) |
| `EXC.IP_RESTRICTION_QUESTION` — user wants to restrict API key by IP | P3 | Provide static IP allowlist (REQUIRED INPUT — confirm we publish) | Security-conscious user | Yes — KB article |
| `EXC.RATE_LIMIT_HIT` — user hit Binance API rate limit | P3 | Engine-side throttle adjustment; on Trader → upgrade-to-DP path triggers | Karim P2 trigger per §6.2 | Partial — depends on tier |
| `EXC.BINANCE_OUTAGE` — Binance side outage | **P1** | Per Escalation D vendor-outage flow | Vendor downtime | No — comms-driven |
| `EXC.MULTI_ACCOUNT_QUESTION` — user wants to connect multiple accounts | P3 | Per `_packaging/02` row F — DP+ feature; explain tier path | Feature confusion | Yes — KB article |
| `EXC.BYBIT_QUESTION` — user wants to use Bybit | P4 | "Bybit is on the P2 roadmap (Aug-Sep 2026)"; no commitments | Roadmap awareness | Yes — KB article |

### Signal interpretation (`SIG`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `SIG.WHAT_IS_REGIME` — user asks what regime label means | P3 | Explain Trending / Mean-Reverting / Volatile / Quiet per Scoopy custom instructions | New-user confusion | Yes — KB article + in-product hover-reveal |
| `SIG.WHY_NO_SIGNALS` — user sees few or no signals | P3 | Explain Quiet regime suppression; reframe absence as discipline signal | Quiet regime active | Yes — KB article + in-product copy |
| `SIG.SIGNAL_LOOKS_WRONG` — user disputes a specific signal | P3 (P2 if pattern) | Provide per-signal trace (T+); methodology link; if pattern across users → escalate to Eng | User disagrees with classifier; OR classifier bug | Partial — KB article on methodology; per-case for specifics |
| `SIG.WHY_DELAY_ON_FREE` — Free user asks about 15-min delay | P3 | Explain Free Scope B per §6.5; Trader removes delay | Tier confusion | Yes — KB article + in-product copy |
| `SIG.HOW_DOES_CONFIDENCE_WORK` — Trader+ user asks about confidence score | P3 | Methodology link + per-signal trace | Trader+ feature awareness | Yes — KB article |
| `SIG.SIGNAL_NOT_RECEIVED` — user expected signal but didn't get one | P3 | Investigate alert routing; Telegram connection; email digest cadence | Alert routing gap | Partial |

### Risk-gate behavior + configuration (`RSK`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `RSK.DEMO_GATE_REJECTED_QUESTION` — user asks why demo gate rejected | P3 | Explain reasoning bullets per `_onboarding/04` §2 layout; methodology link | Confusion about caps | Yes — KB article |
| `RSK.GATE_LOGIC_LOOKS_WRONG` — user disputes gate decision | P3 (P2 if pattern) | Per-decision trace; methodology link; pattern → Eng escalate | User disagrees; OR gate bug | Partial |
| `RSK.WANT_TO_CHANGE_THRESHOLDS` — user wants thresholds outside Capital Cap | P3 | Explain PCC v2 §8 Capital Cap is locked; Trader+ allows config within caps | Power-user pushing limits | Yes — KB article |
| `RSK.GATE_CONFIG_NOT_SAVING` — Trader+ user can't save risk-gate config | P2 | Eng investigation | Bug | No — escalate |

### Journal feature (`JRN`) — T+ only

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `JRN.IMPORT_NOT_WORKING` — auto-import from exchange not pulling trades | P2 | Eng investigation | API change; bug | No — escalate |
| `JRN.EXPORT_QUESTION` — how to export journal as CSV | P3 | Self-serve export flow | Awareness gap | Yes — KB article |
| `JRN.TAGGING_HELP` — how to use custom tags | P3 | KB article + in-product help | Awareness gap | Yes — KB article |
| `JRN.JOURNAL_NOT_VISIBLE_ON_FREE` — Free user expects journal | P3 | Explain §5.3.2 / §6.5 — journal is T+ only | Tier confusion | Yes — KB article + in-product copy |

### Alerts (`ALT`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `ALT.TELEGRAM_NOT_DELIVERING` — Telegram alerts missing | P2 | Eng investigation; check bot status; check user's Telegram connection | Bot outage; user disconnected bot | Partial |
| `ALT.TELEGRAM_CONNECT_HELP` — how to connect Telegram bot | P3 | KB article + in-product flow | Awareness gap | Yes — KB article |
| `ALT.EMAIL_DIGEST_NOT_RECEIVED` — email digest not arriving | P3 | Check spam; verify email address; verify cadence (Free weekly vs T+ daily) | Spam; cadence confusion | Yes — KB article |
| `ALT.WEBHOOK_QUESTION` — DP+ user asks about webhook setup | P3 | KB article + spec | Power-user feature | Yes — KB article |
| `ALT.MULTI_CHANNEL_TELEGRAM` — DF+ user asks about custom routing | P3 | KB article (DF + per-seat feature) | Power-user feature | Yes — KB article |

### Multi-account / portfolio (`MAC`) — DP+ only

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `MAC.ADD_SECOND_ACCOUNT` — DP+ user wants to add second exchange account | P3 | Self-serve flow | Awareness gap | Yes — KB article + self-serve |
| `MAC.MULTI_ACCOUNT_VIEW_BROKEN` — multi-account view not rendering | P2 | Eng investigation | Bug; data sync delay | No — escalate |
| `MAC.HEAT_VIZ_QUESTION` — questions about portfolio heat visualization | P3 | KB article + methodology link | Awareness gap | Yes — KB article |

### Reporting (`RPT`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `RPT.MONTHLY_PDF_NOT_GENERATED` — DP user expects monthly PDF | P2 | Eng investigation | Bug; first month-end timing | Partial |
| `RPT.AUDIT_REPORTING_QUESTION` — DF user asks about LP-style report | P3 | "Audit-grade reporting is on the v2 roadmap (Mar-May 2027)"; no commitments | Roadmap awareness | Yes — KB article |
| `RPT.TAX_EXPORT_QUESTION` — user asks about tax-ready export | P3 | "Tax-ready export is on the v3 roadmap"; no commitments | Roadmap awareness | Yes — KB article |

### Billing (`BIL`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `BIL.PAYMENT_FAILED` — Stripe payment failed | P2 | Per §6.7 retry logic (3 retries / 7 days); user updates payment method | Card expired; insufficient funds | Partial |
| `BIL.PAST_DUE` — account in past-due state | P2 | User-action required; account in read-only state | Payment failure cascading | Partial |
| `BIL.REFUND_REQUEST_IN_WINDOW` — refund within 14d | P3 | Per Escalation C; founder-approved per §6.7; processed per tier SLA | Buyer's remorse; product mismatch | No — case-by-case |
| `BIL.REFUND_REQUEST_OUT_OF_WINDOW` — refund outside 14d | P3 | Standard decline reply with cancel-anytime option | User unaware of policy | Yes — KB article |
| `BIL.CHARGEBACK` — chargeback filed | P2 | Per §6.7; account suspended pending review | User dispute; fraud | No — escalate |
| `BIL.PRICING_QUESTION` — user asks about pricing | P3 | Per pricing-page FAQ; canonical responses | Pre-purchase | Yes — KB article + pricing page FAQ |
| `BIL.FOUNDER_COHORT_QUESTION` — questions about founder-cohort window or terms | P3 | Per `_pricing/03` §6 canonical phrasing | Pre-purchase | Yes — KB article + pricing page FAQ |
| `BIL.PER_SEAT_QUESTION` — DF user asks about adding/removing seats | P3 | Self-serve seat management; per `_packaging/05` Class D | Power-user feature | Yes — KB article + self-serve |
| `BIL.ANNUAL_VS_MONTHLY` — user asks about cadence switch | P3 | Per §6.7 mid-cycle changes; only at renewal boundary | Awareness gap | Yes — KB article |
| `BIL.UPGRADE_QUESTION` — user wants to upgrade tier | P3 | Self-serve upgrade flow; pro-rated billing | Conversion event | Yes — self-serve |
| `BIL.DOWNGRADE_QUESTION` — user wants to downgrade | P3 | Per §6.7 — effective at next renewal; data retention 30 days | Churn risk; cost optimization | Yes — KB article + self-serve |
| `BIL.AED_DISPLAY_QUESTION` — MENA user asks about AED display | P3 | Per §6.8 — courtesy display; billed in USD | Awareness gap | Yes — KB article |
| `BIL.VAT_QUESTION` — UAE user asks about VAT | P3 | Pre-threshold: not collected (per §6.8); post-threshold: handled per Phase 4 setup | Pre/post threshold confusion | Yes — KB article |

### Entitlement / gating leak (`ENT`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `ENT.PAID_FEATURE_VISIBLE_ON_FREE` — Free user sees paid feature exposed | **P2** | Eng investigation; entitlement audit per `_packaging/04` §6 | Tier-matrix YAML drift | No — escalate |
| `ENT.PAID_FEATURE_NOT_AVAILABLE_ON_PAID` — paid user can't access entitled feature | P2 | Stripe webhook → entitlement YAML pipeline check | Webhook delay; YAML drift | No — escalate |
| `ENT.WRONG_TIER_AFTER_UPGRADE` — Stripe says one tier, product says another | P2 | Per `_packaging/04` §6 — server-side authoritative; sync issue | Webhook delay; race condition | No — escalate |
| `ENT.SUB_5K_TIER_CONFUSION` — sub-$5k user confused about tier | P3 | Per `_packaging/02` §3 — Free Scope B identical; "we'll be back" framing | Awareness gap | Yes — KB article + in-product banner |

### Vendor outage / dependency (`VND`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `VND.BINANCE_OUTAGE` — Binance USDT-M futures outage | **P1** | Per Escalation D | Binance-side incident | No — comms-driven |
| `VND.COINGLASS_OUTAGE` — CoinGlass data outage | **P1** (or P2 if partial) | Per Escalation D | CoinGlass-side incident | No |
| `VND.TRADEFEEDS_OUTAGE` — Tradefeeds outage | P2 | Per Escalation D | Tradefeeds-side | No |
| `VND.COINGECKO_OUTAGE` — CoinGecko outage | P2 | Per Escalation D | CoinGecko-side | No |
| `VND.CLAUDE_OUTAGE` — Claude API outage (where used minimally per memory `project_phased_rollout`) | P2 | Per Escalation D; degraded fallback if available | Claude-side | No |
| `VND.STRIPE_OUTAGE` — Stripe billing outage | **P1** (P2 if partial) | Per Escalation D; billing actions queued | Stripe-side incident | No |

### Incident (`INC`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `INC.ENGINE_DOWN` — engine fully down | **P1** | Per Escalation A; Eng + Founder concurrent response | Internal incident | No |
| `INC.ENGINE_DEGRADED` — partial engine functionality | P2 | Per Escalation A; status page + comms | Internal incident | No |
| `INC.SECURITY_EVENT` — suspected security breach | **P1** | Per Escalation A; immediate Eng security review + counsel awareness | Security incident | No |
| `INC.DATA_INTEGRITY_EVENT` — data corruption suspected | **P1** | Per Escalation A; Eng + counsel awareness | Internal | No |
| `INC.WRONG_BALANCE_REPORTED` — user reports wrong balance | **P1** | Per Escalation A | Engine bug; vendor-data delay; user misread | No |

### PCC v2 §8 / real-capital (`PCC`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `PCC.IS_IT_PRODUCTION_READY` — "is the system production-ready?" | P3 | Per Escalation B canonical response | Sales-cycle inquiry | Yes — KB article + pricing page FAQ |
| `PCC.WHEN_REAL_CAPITAL` — "when will live trading open?" | P3 | Per Escalation B canonical response; PCC v2 §8 gates | Pre-purchase / cohort | Yes — KB article |
| `PCC.GATE_STATUS` — "what's the status of G1–G4?" | P3 | Status page + canonical response | Cohort awareness | Yes — KB article + status page |
| `PCC.SHOULD_I_TRADE_REAL_MONEY` — user asks for advice | P3 | Canonical decline: "We don't provide trading advice. Validation phase is testnet only per PCC v2 §8." | Sales / advice request | Yes — KB article |

### Regulatory (`REG`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `REG.LICENSING_QUESTION` — "are you licensed?" | P3 | Per Escalation E canonical response (UAE sole prop, technology-as-a-service) | Pre-purchase / regulator-curious | Yes — KB article |
| `REG.JURISDICTION_QUESTION` — questions about user's jurisdiction | P3 | Per Escalation E; route to local counsel for user | Compliance-curious | Yes — KB article |
| `REG.GDPR_DATA_REQUEST` — formal data request | P3 | Per §6.7 + GDPR window | EU user | No — case-by-case |
| `REG.FORMAL_REGULATOR_INQUIRY` — formal inquiry from regulator | **P1** | Per Escalation E; immediate counsel routing (Phase 4 trigger) | Regulator action | No |

### Bug report (`BUG`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `BUG.FUNCTIONAL` — feature broken in user-impacting way | P3 (P2 if blocking) | Eng investigation | Bug | No — escalate |
| `BUG.COSMETIC` — UI / display issue | P4 | Logged for next design pass | Bug | No |
| `BUG.PERFORMANCE` — slowness | P3 (P2 if widespread) | Eng investigation | Engine load; vendor latency | No — escalate |

### Feature request (`FRQ`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `FRQ.ROADMAP_FEATURE` — request for already-roadmapped feature (e.g., Bybit, audit reporting) | P4 | Canonical "on roadmap, no commitments" response | Roadmap awareness | Yes — KB article + roadmap page |
| `FRQ.NEW_FEATURE` — net-new feature request | P4 | Logged; reviewed at quarterly product cadence | User input | No — log and respond |
| `FRQ.ANTI_ICP_FEATURE` — request for anti-ICP feature (signal-group integration, copy-trade, leverage maximization) | P4 | Canonical decline: "Not on our roadmap; this is anti-ICP per our positioning." | Anti-ICP user | Yes — KB article on positioning |

### Brand / messaging / press / partnership (`MSG`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `MSG.PRESS_REQUEST` — media inquiry | P3 | Founder review; if substantive → engagement | Media interest | No |
| `MSG.PARTNERSHIP_PITCH` — partnership outreach | P4 | Founder review; if anti-ICP → decline; if aligned → engage | Inbound partnership | No |
| `MSG.BRAND_FEEDBACK` — copy or design feedback | P4 | Logged for Phase 1 BRAND review | User feedback | No |

### Anti-ICP outreach (`ANT`)

| Subcategory | Default severity | Resolution path | Common cause | Deflection-eligible |
|---|---|---|---|---|
| `ANT.SIGNAL_GROUP_OUTREACH` — signal-group operator wanting integration | P4 | Canonical decline per §5.3.3 | Anti-ICP outreach | Yes — KB article on positioning |
| `ANT.COPY_TRADE_PITCH` — copy-trade product pitch | P4 | Canonical decline per §5.3.3 | Anti-ICP | Yes — KB article |
| `ANT.LEVERAGE_PROMOTION` — leverage-maximizer co-marketing | P4 | Canonical decline per §5.3.3 | Anti-ICP | Yes — KB article |
| `ANT.AFFILIATE_PROGRAM_PITCH` — affiliate program partnership | P4 | Canonical decline (no affiliate program at v1 per `_packaging/05` design rule 8) | Generic outreach | Yes — KB article |

---

## 3. Top issue categories — predicted volume distribution

Based on category norms + ONBOARDING `_onboarding/05` audit findings + PACKAGING / PRICING surface design. **INFERENCE — actual distribution emerges from cohort data.**

| Predicted volume rank | Category | Reasoning |
|---|---|---|
| 1 | `EXC.*` (especially `EXC.API_KEY_INVALID`, `EXC.TESTNET_VS_MAINNET_CONFUSION`) | Exchange connectivity is the highest-friction step; expected highest ticket source |
| 2 | `BIL.*` (especially `BIL.PRICING_QUESTION`, `BIL.FOUNDER_COHORT_QUESTION`) | Pre-purchase + post-purchase billing curiosity; high-volume but low-severity |
| 3 | `SIG.*` + `RSK.*` (especially `SIG.WHY_NO_SIGNALS`, `RSK.DEMO_GATE_REJECTED_QUESTION`) | First-value confusion; deflection-eligible via KB |
| 4 | `PCC.*` (especially `PCC.IS_IT_PRODUCTION_READY`, `PCC.WHEN_REAL_CAPITAL`) | Validation phase generates these; canonical responses critical |
| 5 | `ALT.*` | Alert routing common point of confusion |
| 6 | `FRQ.*` | Feature requests inevitable; mostly P4 logging |
| 7 | `ACC.*` | Account / auth issues; mostly self-serve |
| 8 | `MAC.*` + `RPT.*` | DP+ feature questions; lower volume but higher per-ticket time |
| 9 | `VND.*` | Vendor outages bursty; comms-driven not ticket-driven |
| 10 | `INC.*`, `ENT.*`, `REG.*`, `BUG.*` | Lower volume, higher impact per ticket |

---

## 4. Deflection priorities

Categories ranked by deflection ROI (likely volume × KB-article-feasibility):

| Priority | Category | KB-article focus |
|---|---|---|
| 1 | `EXC.API_KEY_INVALID` + `EXC.TESTNET_VS_MAINNET_CONFUSION` | "How to connect Binance USDT-M with a read-only API key" — single article covering creation, scope, testnet/mainnet, IP allowlist |
| 2 | `BIL.PRICING_QUESTION` + `BIL.FOUNDER_COHORT_QUESTION` | Pricing-page FAQ already covers; KB cross-links |
| 3 | `SIG.WHAT_IS_REGIME` + `SIG.WHY_NO_SIGNALS` + `RSK.DEMO_GATE_REJECTED_QUESTION` | "Reading the engine: regime labels, signals, and gate decisions" — single comprehensive article |
| 4 | `PCC.IS_IT_PRODUCTION_READY` + `PCC.WHEN_REAL_CAPITAL` + `PCC.GATE_STATUS` | "Validation phase + Production Candidate Criteria v2 §8" — single canonical article |
| 5 | `ACC.EMAIL_NOT_RECEIVED` | "Email delivery troubleshooting" — short article |
| 6 | `BIL.REFUND_REQUEST_OUT_OF_WINDOW` | "Cancellation, refund, and reactivation" — references §6.7 |
| 7 | `ALT.TELEGRAM_CONNECT_HELP` | "Connecting the @ScoopyAI_bot Telegram channel" |
| 8 | `JRN.JOURNAL_NOT_VISIBLE_ON_FREE` + `EXC.MULTI_ACCOUNT_QUESTION` + `RPT.AUDIT_REPORTING_QUESTION` | "Free vs Trader vs Desk Preview vs Desk Full v2 — what each tier includes" — references `_packaging/03` plan comparison |

---

## 5. Severity assignment edge cases

Ambiguities documented to ensure consistent triage:

| Ambiguous case | Default severity | Reasoning |
|---|---|---|
| User reports "wrong balance" but uses Free tier and connected mainnet (read-only) | **P1** initially → reclassify to P3 if confirmed user-misread | Wrong balance is real-capital-context risk regardless of tier |
| User asks "should I trade real money" + reports $50k account | P3 (canonical PCC v2 §8 response) | Sales-cycle question, not safety question |
| Multiple users report "Telegram alerts missing" within 1 hour | Single ticket → P3; pattern → escalate to P2 (`ALT.TELEGRAM_NOT_DELIVERING`) | Pattern-detection per Pattern 4 in `03` §4 |
| User threatens chargeback if refund denied | P3 + standard reply (don't escalate based on threat) | Threat doesn't change refund eligibility; per §6.7 |
| User claims "I was promised X" where X conflicts with documented terms | P3 + Founder review | Documentation is canonical; review for actual marketing-copy drift if any |
| Vendor outage detected by single user before monitoring | P3 → escalate to **P1** if confirmed by founder + Eng | Verify before broadcasting |
| User on Free reports `ENT.PAID_FEATURE_VISIBLE_ON_FREE` (gating leak) | **P2** | Per `_packaging/04` §6 entitlement contract; Eng escalate |

---

## 6. Failure modes specific to this taxonomy

- **Taxonomy drift over time.** New issue categories emerge; if not added, tickets get miscategorized. Quarterly taxonomy review.
- **Severity inflation under support pressure.** Founder marks P3 as P2 to "get it done faster" → P2 metrics inflate, real P2s lost. Severity is per the matrix, not per founder mood.
- **Catch-all "Other" category becomes default.** "Other" tag means no triage discipline. Force categorization; add new category if needed.
- **Deflection-eligible tickets not getting deflection investment.** Top-3 deflection priorities (§4) get KB articles within Phase 2 NEXT (`Help Center Structure`).
- **PCC v2 §8 questions getting non-canonical responses.** Single-canonical-response is non-negotiable per Escalation B. Founder-only routing in v1.

---

## 7. What this unlocks

- `05-support-inbox-and-response-workflow.md` consumes taxonomy as triage tag inventory.
- `Standard Response Templates` (NEXT) maps templates 1:1 to deflection-eligible categories in §4.
- `Help Center Structure` (NEXT) consumes top-8 deflection priorities as KB article seed.
- `Billing Support Playbook` (NEXT) consumes all `BIL.*` categories.
- `Exchange Connectivity Support Playbook` (NEXT) consumes all `EXC.*` and `VND.*` categories.
- `Support KPI Dashboard` (NEXT METRICS) tracks ticket volume + resolution time per category for trend analysis.
- §13 KPI framework gets ticket-volume-per-category as a leading indicator (e.g., `EXC.*` spike = onboarding flow drift).
