# Validation Phase Exit Memo

> **Validation phase:** 2026-04-10 → 2026-05-09 (COI-41 dry-run paper-trading window)
> **Memo status:** Filled retrospectively while AWS VPS is suspended. Raw engine journals and telemetry are inaccessible; this memo records the metrics that are verifiable from the slide deck and marks the remainder as pending restoration.

---

## 0. Header

| Field | Value |
|---|---|
| Validation phase start | 2026-04-10 |
| Validation phase end | 2026-05-09 |
| Memo author | Mohammed (Founder) |
| Memo date | 2026-07-27 |
| Reviewers | Strategy Chief of Staff (Scoopy); External Risk Reviewer (TBD) |
| Decision (template options: PASS / EXTEND / RESTART / KILL) | **EXTEND** — 30-day extension required due to signal-quality P0 failures (WFV 6/18, CPCV 0/6) |
| Next gate evaluated | G1 (Closed Beta) only — G2 not evaluated at this point |

---

## 1. Executive Summary (≤200 words)

**Decision: EXTEND** for the validation-phase exit.

The engine ran for 31 days and 4 hours of uptime on Binance Futures Testnet, with the risk gate rejecting 68% of candidates and the kill switch engaging as recently as 2026-04-22. These three data points suggest the engine stayed online and the risk path remained active throughout the validation window. However, the AWS VPS hosting the validation environment is currently suspended, so the full trade journal, performance curve, and telemetry needed to complete the Production Candidate Criteria scorecard are not available for independent replay.

More importantly, repository history contains confirmed signal-quality P0 failures (WFV 6/18, CPCV 0/6). Under the pre-committed decision rule, any P0 failure — regardless of operational data gaps — triggers an **EXTEND** verdict rather than PASS or Conditional PASS. The validation phase is therefore extended by 30 days to address the failed signal-quality criteria before any G1 unlock can be considered. No real-capital or closed-beta access is authorized during the extension.

---

## 2. Validation Phase Scope (what was actually run)

| Field | Value |
|---|---|
| Engine version(s) deployed | Last deployed commit prior to AWS suspension; exact hash unavailable until VPS is restored |
| Network | Binance Futures Testnet (USDT-M) |
| Symbols traded | BTCUSDT, ETHUSDT, SOLUSDT (per Validation Data Analysis Plan v1.0) |
| Calendar days live | 30 (2026-04-10 → 2026-05-09) |
| Engine uptime (% of calendar days) | 31d 04h total uptime; exact % of calendar days TBC after log replay (raw uptime exceeds the 30-day window, indicating continuous operation) |
| Total signals generated | **Unavailable** — raw `/scan` log on suspended VPS |
| Total trades placed (paper) | **Unavailable** — raw `/journal` on suspended VPS |
| Total kill-switch trips | At least 1; last trip 2026-04-22; full count pending log replay |

**Material configuration changes during phase** (list each, with date and rationale):
- [x] None known. The validation window was intended to run under a frozen configuration per `component-map.md`.

---

## 3. Production Candidate Criteria Scorecard

> Reference: `docs/Production_Candidate_Criteria.md` (v2.0). Only engine criteria (S, D, X, plus engine-side O/M/R) are evaluated at validation exit. Product-layer criteria (CL, CP, T, B, US) gate G1, not this exit.

### 3.1 Signal Quality (S)
| ID | Criterion | Threshold | Observed | Pass? | Notes |
|---|---|---|---|---|---|
| S0 | LLM not in hot path | binary | **Pending static replay** | ☐ | Code audit can be re-run from repo once VPS is restored; not a metric-dependent cell. |
| S1 | Signal precision (rolling 30d) | ≥ baseline | **Unavailable** | ☐ | Journal inaccessible due to AWS suspension. |
| S2 | Confluence distribution | ≥80% of signals at confluence ≥ min | **Unavailable** | ☐ | `/scan` log inaccessible. |
| S3 | Regime stability | ≤1 flip / 4h / symbol avg | **Unavailable** | ☐ | `/regime/{symbol}` time series inaccessible. |
| S4 | False-positive risk-gate pass-throughs | 0 | **Unavailable** | ☐ | Requires journal + risk-gate log join. |
| S5 | Signal latency p95/p99 | ≤500/1500ms | **Unavailable** | ☐ | Telemetry store inaccessible. |

### 3.2 Drawdown Discipline (D)
| ID | Criterion | Threshold | Observed | Pass? | Notes |
|---|---|---|---|---|---|
| D1 | Max drawdown | ≤10% | **Unavailable** | ☐ | Performance curve on suspended VPS. |
| D2 | Daily loss days | 0 days >5% | **Unavailable** | ☐ | Daily P&L inaccessible. |
| D3 | Leverage cap | 0 trades >10x | **Unavailable** | ☐ | `/position-size` log inaccessible. |
| D4 | Concurrent positions | 0 windows >5 | **Unavailable** | ☐ | Journal window analysis inaccessible. |
| D5 | Position heat | 0 trades >80% at entry | **Unavailable** | ☐ | `/position-size` log inaccessible. |
| D6 | DD recovery | ≤5 trading days from any 5% intraday | **Unavailable** | ☐ | Performance curve inaccessible. |
| D7 | Kill-switch trip behavior | All trips halted entries within 1 cycle | Last trip 2026-04-22 | ☐ | Slide-deck confirms engagement; per-trip halt verification pending log replay. |

### 3.3 Execution Integrity (X) — informational at G1; binding at G2
| ID | Criterion | Observed | Pass? | Notes |
|---|---|---|---|---|
| X1–X6 | (per criteria doc) | **Unavailable** | ☐ | All slippage, fill, sizing, and reconciliation data on suspended VPS. |

### 3.4 Operations & Reliability (O)
| ID | Criterion | Threshold | Observed | Pass? | Notes |
|---|---|---|---|---|---|
| O1 | MTBF | ≥168h | **Unavailable** | ☐ | Supervisor/Sentry logs inaccessible. |
| O2 | MTTR | ≤30 min | **Unavailable** | ☐ | Incident log incomplete without VPS. |
| O3 | VPS hardened | binary | **Blocked** | ☐ | AWS account suspension is the blocking issue. |
| O4 | Alert coverage | 100% of D1–D5, X1–X6 | **Unavailable** | ☐ | Alert config audit pending restoration. |
| O5 | Alert false-positive rate | ≤10% | **Unavailable** | ☐ | Alert log inaccessible. |
| O6 | Dashboard uptime | ≥99% | **Unavailable** | ☐ | External probe data unavailable. |
| O7 | Telegram delivery | ≥99% within 60s | **Unavailable** | ☐ | Bot log inaccessible. |

### 3.5 Monitoring & Observability (M)
| ID | Pass? | Notes |
|---|---|---|
| M1 KPI dashboard | ☐ | Dashboard state unverified while VPS is suspended. |
| M2 Trade journal complete | ☐ | Journal completeness audit pending data replay. |
| M3 Vendor health panel | ☐ | Panel inaccessible. |
| M4 Logs ≥90 days | ☐ | Log-store config audit pending restoration. |
| M5 Audit-grade event log | ☐ | Immutable-log verification pending. |

### 3.6 Rollback & Failure (R)
| ID | Pass? | Notes |
|---|---|---|
| R1 Manual kill switch | ☐ | Reachability drill pending restoration. |
| R2 Auto kill switch | ☐ | Auto-trip log unavailable. |
| R3 Position-close playbook | ☐ | Drill not replayed. |
| R4 Vendor failure tolerance | ☐ | Vendor failure-mode mapping exists but live drill pending. |
| R5 Code rollback ≤10min | ☐ | Drill pending. |
| R6 Catastrophic stop | ☐ | Drill pending. |

### 3.7 Legal (L) — gating
| ID | Pass? | Notes |
|---|---|---|
| L1 ToS | ☐ | Counsel-reviewed docs in draft; not evaluated at validation exit. |
| L2 Risk Disclosure | ☐ | Draft exists in `11-legal/tos-and-disclosures-DRAFT.md`. |
| L3 Privacy Policy | ☐ | Draft exists. |
| L4 No-advice memo | ☐ | Marketing-copy audit pending. |

### 3.8 Aggregate
- Total P0 criteria evaluated: **3 metrics only** (uptime, gate rejection rate, kill-switch last-engagement date)
- P0 pass: **0 / 0** formally — insufficient data to assert pass/fail
- P1 pass: **0 / 0** formally
- **Any single P0 failure?** ☑ Yes  ☐ No  — Signal-quality P0 failures recorded (WFV 6/18, CPCV 0/6)

---

## 4. Material Findings

### 4.1 What worked as documented
- **Sustained uptime:** 31d 04h of engine uptime across the validation window, exceeding the 30-calendar-day target.
- **Risk-gate activity:** 68% candidate rejection rate, consistent with a conservative gate posture.
- **Kill-switch engagement:** Kill switch last engaged on 2026-04-22, indicating the halt path was armed and triggered at least once.

### 4.2 Surprises (positive)
- None independently verifiable without the raw data pack.

### 4.3 Surprises (negative)
- **Signal-quality P0 failures** are present in repository history (WFV 6/18, CPCV 0/6). By the pre-committed decision rule, this alone requires an EXTEND verdict.
- **AWS VPS suspension** occurred after the validation window, blocking access to the full trade journal, telemetry, and observability stack needed to complete this memo mechanically. This is an operational dependency, not an engine defect, but it prevents a clean PASS.

### 4.4 Near-misses
- None verifiable without the raw data pack.

---

## 5. Incidents (if any)

No engine incidents were recorded in the slide-deck summary. The only post-phase operational event is the AWS account suspension, which is documented separately and is outside the validation window.

If zero incidents, write: "Zero incidents recorded. Verified by reviewing the alert log and the journal for the full validation window."
> **Zero engine incidents recorded in the available summary.** Full verification requires log replay after AWS restoration.

---

## 6. Vendor Behavior Summary

Per vendor, one line:

| Vendor | Outage events | Total downtime | Within tolerance? | Notes |
|---|---|---|---|---|
| Binance Futures (testnet) | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |
| CCXT | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |
| CoinGlass | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |
| Tradefeeds | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |
| CoinGecko | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |
| Anthropic Claude | **Unavailable** | **Unavailable** | ☐ | Data on suspended VPS. |

---

## 7. Decision

> Pre-committed decision rule (Production Candidate Criteria §10):
>
> - **All G1 P0 pass + ≥80% P1 pass** → **PASS** (unlock G1, closed paper-trading beta)
> - **G1 P0 partial pass (≥1 P0 fails)** → **EXTEND** (30-day extension; address failed criteria)
> - **≥2 P0 fail OR D-category breach observed** → **RESTART**
> - **Multiple D-category breaches OR kill-switch failure** → **KILL** (full engine review)

**Decision:** ☐ PASS  ☐ Conditional PASS  ☑ **EXTEND**  ☐ RESTART  ☐ KILL

**Reasoning (≤150 words):**

The three externally verifiable metrics — 31d 04h uptime, 68% gate rejection, and kill-switch engagement on 2026-04-22 — are consistent with an engine that stayed online and risk-disciplined. However, repository history contains confirmed signal-quality P0 failures (WFV 6/18, CPCV 0/6). The pre-committed decision rule is unambiguous: any P0 failure requires EXTEND. The AWS VPS suspension additionally prevents replay of the full scorecard, but it does not override the signal-quality finding. The phase is extended by 30 days to address the failed criteria and re-verify before any G1 unlock.

**If EXTEND:** Specify failed criteria and corrective tasks below. A new end date will be set once the signal-quality fixes are validated.
**Failed criteria:** Signal quality (S) — WFV 6/18, CPCV 0/6.
**Corrective tasks:**
1. Diagnose root cause of WFV and CPCV signal-quality failures.
2. Implement and test fixes in the signal-generation path.
3. Re-run walk-forward validation and cross-validation to confirm pass.
4. Restore AWS VPS, replay validation logs, and complete §3 scorecard.
5. Obtain Founder sign-off before updating this memo to PASS.

---

## 8. Corrective Work During EXTEND

Because the decision is **EXTEND**, the items below are **required** before the memo can be updated to PASS and G1 unlock can be considered.

| Item | Owner | Target date |
|---|---|---|
| Diagnose WFV 6/18 and CPCV 0/6 signal-quality failures | Founder | Within 7 days |
| Implement signal-generation fixes and unit tests | Founder | Within 14 days |
| Re-run walk-forward validation and cross-validation to confirm pass | Founder | Within 21 days |
| Restore AWS VPS and replay validation logs | Founder | TBD — pending AWS support |
| Complete §3 scorecard and sign memo | Founder | After signal-quality P0 passes |
| Closed beta cohort recruited | Founder | After memo signed |
| ToS + Risk Disclosure live | Founder + Counsel | Before first beta invite |
| First beta user invited | Founder | After all G1 criteria pass |
| First weekly beta review | Founder | Within 7 days of first invite |

**G2 evaluation:** Not authorized at this point. G2 evaluation requires ≥60 days of clean closed-beta operation under G1, plus completion of all G2-specific P0 criteria (X1–X6, R3–R6, L5, L6, I1, I2).

---

## 9. What Stays Locked

> Even on PASS, list anything that remains explicitly off the table. This protects against scope creep into "well, since we passed validation..."

- Real-capital trading: **LOCKED** (G2 not evaluated; §8 gate remains locked).
- External user funds: **LOCKED** (C5 — never accepted under current product scope).
- Managed/discretionary trading: **LOCKED** (requires separate document and licensure).
- Production claims in marketing: **LOCKED** (we are in closed beta only; no "production" or "live" claims in public copy).
- Public signup and payments: **LOCKED** until Customer Layer / Compliance criteria (CL1–CL5, CP4, B1–B7) are evaluated and pass.

---

## 10. Sign-Offs

| Role | Name | Date | Signature/Commit hash |
|---|---|---|---|
| Founder | Mohammed | | |
| Strategy Chief of Staff | Scoopy | | |
| External Risk Reviewer | TBD | | |

> **G1 unlock requires:** Founder sign-off + commit hash of this memo in the repo.
> **G2 unlock requires:** All three sign-offs above + a separate G2 memo.

**Commit hash of this memo:** (to be filled at commit time)

---

## 11. Appendix

- A. Full criteria scorecard (raw numbers): **Pending AWS restoration.**
- B. Trade journal export for the validation window: **Pending AWS restoration.**
- C. Incident log: **Pending AWS restoration.**
- D. Alert log: **Pending AWS restoration.**
- E. Vendor health log: **Pending AWS restoration.**
- F. Engine version diff (start vs. end of validation): **Pending AWS restoration.**

---

## 12. Filing instructions

1. Save as `docs/validation_exit_memo_2026-05-09.md` in the repo. ✅
2. Commit with a message containing the decision (e.g., `docs: validation exit memo — DECISION: EXTEND`).
3. Because the decision is **EXTEND**, do **not** open the G1 unlock checklist until the failed signal-quality criteria are addressed, the AWS replay corrective task is complete, and the memo is updated to a full PASS.
4. Update the project state memory file with the corrective task and target replay date.
5. Notify the external reviewer once the replay is complete and the final decision is recorded.
