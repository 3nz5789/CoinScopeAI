# DOC_UPDATE_REPORT — 2026-05-08

**Run type:** Scheduled (`documentation-update`, autonomous mode)
**Author:** Scoopy (Claude)
**Scope:** `CoinScopeAI-Context.md` · `README.md` · `docs/api/*` · new-feature log since the 2026-05-01 run
**Mode notes:** Autonomous run — user not present. Reasonable choices were made and are noted inline. Edits applied in this run are listed in §6; everything else is recommendations.

---

## 1. Executive summary

- **`docs/api/backend-endpoints.md` was materially out of date.** It described 21 endpoints organised around an aspirational `/risk-gate`, `/symbols`, `/depth/{symbol}`, `/ready`, `/kill-switch`, `/metrics` surface that does not exist in `coinscope_trading_engine/api.py`. The live engine ships **60 routes** (55 on the app + 5 on the billing router). The previous version had been flagged as "outstanding 12 days" in the 2026-05-01 report and was overdue. **Action taken this run:** rewritten end-to-end against the live source. See §6.
- **`docs/api/api-overview.md` is structurally fine** — base URL, error envelope, content-type, observability hooks, copyright posture all still match reality. Two surgical edits applied: added a `Last verified: 2026-05-08` line and rephrased the versioning timeline so the cutover is anchored to phase exit (post-P0, June 2026) rather than the now-passed `2026-04-30` date.
- **Root `README.md` is mostly accurate** but the "Current status" header still says `(2026-04-20)`. The body content remains correct against the engine code (no signed-WS routing change, no new endpoint group, scan cadence unchanged at 10 s). **Recommendation only — not auto-edited:** bump the date and append a one-line "wave 1 of business plan closed 2026-05-07" note. Reasoning for not auto-editing: the README's status block is operator-facing and should be touched by the founder rather than by an autonomous run.
- **`CoinScopeAI-Context.md`** is still in `archive/historical_reports/`. It remains stale (engine version 2.0.0 listed, but the v2.0.0 endpoint count is itself wrong: 26 vs the actual 60). It is correctly retired and is not linked from any live doc. No action — leave archived.
- **New-feature log** (since 2026-05-01) is dominated by **business-plan Wave 1 close** (27 markdown files across folders 01–06, locked 2026-05-07) and a string of **engineering-discipline scaffolds** (4 Scoopy skills, 2 risk-guardrail scripts, 4 new runbooks, 4 architecture deep-dives, 2 risk-framework docs, 2 incident digests, 1 vendor-spike research note, 1 legal starter pack + ToS draft). Detailed list in §5.

Overall grade: **documentation drift on the API surface (CRITICAL — now resolved) + healthy growth on planning, risk, and runbook surfaces**. The engine code has remained essentially unchanged since 2026-05-03 17:30 (most files), so the API doc rewrite is itself a long-overdue catch-up rather than coverage of new endpoints.

---

## 2. CoinScopeAI-Context.md — Status

**File:** `archive/historical_reports/CoinScopeAI-Context.md` · last on-disk touch 2026-04-18 23:32 (unchanged).

- Status: retired. Stamped `Last updated: 2026-04-15`, claims engine `2.0.0` (still accurate as a version string), but its endpoint table (≈26 entries) is now ~57% complete vs the live 60-route surface.
- It is not linked from the root `README.md`, `docs/README.md`, or any live doc — confirmed via grep across the live tree.
- Recommendation: **no action.** Leave in archive. The current source-of-truth chain is `README.md` → `docs/README.md` → `docs/api/{api-overview,backend-endpoints}.md` → live `api.py`. Reviving the historical Context doc would re-introduce a parallel canonical view.

---

## 3. README.md — Stale "Current status" header (recommendation only)

**File:** `/README.md` · last on-disk touch 2026-05-03 17:33.

Body content was re-verified against the tree on 2026-05-08 and is still accurate:

- Engine running on `demo-fapi.binance.com` (Binance Futures Demo). ✓
- Endpoint groups table matches the live route inventory (this report's §6 rewrite of `backend-endpoints.md` is a superset, but the README's grouped summary is internally consistent). ✓
- Scan cadence `SCAN_INTERVAL_SECONDS=10` matches `coinscope_trading_engine/config.py`. ✓
- Persistence list (`logs/{coinscope.log,journal.json,decisions.jsonl,klines.sqlite}`) matches the on-disk store. ✓
- Risk-framework reading order points at `docs/risk/{risk-framework,risk-gate,position-sizing,failsafes-and-kill-switches}.md`. The first three exist; `failsafes-and-kill-switches.md` was not located in this run. **Flag for follow-up.**

The single material edit recommended is the date stamp:

```
## Current status (2026-04-20)
```

→ should become

```
## Current status (2026-05-08)
```

…with one or two short notes appended that reflect the week's ground truth:

- `Engine code unchanged since 2026-05-03; daily code-review reports continue (latest: CODE_REVIEW_2026-05-08_daily.md, 9 open items).`
- `Business-plan Wave 1 closed 2026-05-07 — see business-plan/_wave-1-closeout.md.`

**Why not auto-edited:** the "Current status" line is operator-facing copy that the founder typically owns. An autonomous run editing it without a paired commit can re-introduce drift. Holding for next manual pass.

---

## 4. API documentation — REWRITTEN

The single biggest doc-debt item from the past three weeks of reports.

### Findings on the previous `docs/api/backend-endpoints.md`

| Issue | Detail |
|---|---|
| Header claimed **21 endpoints** | Live count is **60** (55 in `api.py` + 5 in `billing/stripe_gateway.py`). |
| `/risk-gate`, `/symbols`, `/depth/{symbol}`, `/ready`, `/kill-switch`, `/metrics` documented | None of these are wired in `api.py`. |
| `GET /scan` (read) documented | Real surface is `GET /signals` (cached) + `POST /scan` (trigger) + `GET /scan/status`. |
| `GET /position-size` shape | Body-style spec; live endpoint takes query parameters. |
| `GET /billing/me` | Renamed in code to `GET /billing/subscription`. |
| Whole tag groups missing | `/account/*`, `/orders/*`, `/autotrade/*`, `/decisions/*`, `/historical/*`, `/prices/*`, `/exposure`, `/correlation`, `/journal/{entry_id}/trace`, `/scale*`, `/validate`, `/anomaly`, `/sentiment`, `/circuit-breaker/trip` — all unmentioned. |

### Action

`docs/api/backend-endpoints.md` rewritten end-to-end. Inventory now organised by tag matching the FastAPI grouping, with a verification snippet at the bottom that regenerates the table from `api.py` + `billing/stripe_gateway.py`. The "what changed in this revision" section calls out every aspirational endpoint that was previously documented and where its real equivalent lives.

`docs/api/api-overview.md` lightly amended:

- Added `Last verified: 2026-05-08` under the status line.
- Rephrased the `/v2/` cutover anchor from `After 2026-04-30` (now stale) to `Once the validation phase exits (target: post-P0, June 2026)`.

The bearer-token + entitlement-gating posture documented in `api-overview.md` is the production target, not the validation-phase reality. A new sentence at the top of `backend-endpoints.md` makes that explicit so a reader running the engine locally during validation isn't confused by `Authorization: Bearer …` requirements that aren't enforced today.

---

## 5. New features / artifacts in the past week (2026-05-02 → 2026-05-08)

The repo activity falls into four buckets. None of these are engine-code feature additions; they are operational, planning, and discipline scaffolding.

### 5.1 Business-plan Wave 1 closure (largest single change)

`business-plan/_wave-1-closeout.md` (2026-05-07) closes folders 01–06 with **27 markdown files**:

- 01-executive-summary/ — README, executive-summary-v1, strategic-priorities, business-model-summary
- 02-company-overview/ — README, company-overview, current-state-assessment, strategic-constraints
- 03-market-thesis/ — README, market-thesis, why-now, market-risks
- 04-icp-and-segmentation/ — README, primary-icp, secondary-icps, jobs-to-be-done, pains-triggers-wtp
- 05-positioning/ — README, positioning-statement, category-decision, differentiation-framework, messaging-hierarchy
- 06-product-strategy/ — README, product-strategy, core-product-pillars, mvp-vs-beta-vs-scale, feature-prioritization

Four operator-grade locks committed: primary ICP (P1 Omar), category framing (trader operating system primary, institutional-grade signal/risk platform secondary), five product pillars, and stage definitions (MVP/Beta/Scale-A/Scale-B). 28 open questions registered (Tier 1 = 6 items that block Wave 2 entry).

Phase-2 and Phase-3 working trees are also present (`business-plan/_phase-2/*`, `business-plan/_phase-3/*`) with charters and packaging/pricing/onboarding/support/GTM/operations/metrics drafts.

### 5.2 New Scoopy skills (`skills_src/`)

Four new operator skills, all dated this week:

| Skill | Purpose |
|---|---|
| `daily-status/` | One-screen morning brief from `/performance` + `/risk-gate`-equivalent + `/journal` + `/regime`. Validation-phase safe; localhost-only. |
| `decision-log-appender/` | Structured append to `business-plan/_decisions/decision-log.md` (64+ entries; append-only, supersede via new entries). |
| `drift-detector/` | Cross-checks canonical-token consistency across CLAUDE.md, design-system-manifest, business-plan/*, decision-log. Catches the `20x → 10x` leverage-slip class of regression. |
| `kill-switch-protocol/` | Codified 4-step halt sequence (assess → halt → alert → postmortem-stub) with exact Engine API calls and Telegram template. |

Companion scripts in `scripts/`:

- `scripts/drift_detector.py` — programmatic version of the drift-detector skill.
- `scripts/risk_threshold_guardrail.py` — focused subset that scans for code referencing risk thresholds with non-canonical values.

### 5.3 New documentation surfaces (`docs/`)

| Path | What it is |
|---|---|
| `docs/runbooks/daily-market-scan-runbook.md` | Daily 4×/day scanner cadence + EOD summary; testnet only. |
| `docs/runbooks/vps-engine-restart.md` | Apply patched `.env` to `api.coinscope.ai`, verify `/config` reflects new canonical thresholds. Bundled with COI-40. |
| `docs/runbooks/drive-vs-git.md` | Locked 2026-05-04 — git working trees do not belong inside Google Drive Desktop sync paths. Permanent rule from the 2026-05-03/04 sync race. |
| `docs/runbooks/mirror-v1-deltas-to-v2.md` | Mac-side runbook to mirror the five 2026-05-03 v1 working-tree files into `3nz5789/CoinScopeAI_v2`. |
| `docs/risk/risk-framework.md` | Philosophy + invariants — required reading for `risk/`, `execution/`, sizing. |
| `docs/risk/position-sizing.md` | Fractional Kelly + hard cap + regime multiplier pipeline. |
| `docs/architecture/trading-pipeline.md` | "Bought a tool, now turn it on" plain-English walkthrough + auto-trading roadmap. |
| `docs/architecture/dashboard-status.md` | Per-page live/mock/source matrix for the React dashboard. |
| `docs/architecture/data-flow.md` | Tick → gate-rejection-or-order narrative. |
| `docs/architecture/engine-internals.md` | File-by-file map of what runs, what talks to what, what is orphaned. |
| `docs/ml/confidence_scoring_baseline.md` | Draft v1 measurement + spec for the confidence scoring layer (engine code freeze in effect). |
| `docs/backend/configuration.md` | Authoritative semantics for env vars; `.env.example` remains authoritative for field names. |

### 5.4 Other artifacts

- `incidents/digest-2026-05-03.md`, `incidents/digest-2026-05-04.md` — incident digests covering the Drive-vs-Git sync race that destroyed 4 unpushed commits.
- `incidents/drift-log.md` — running drift-detector pass log (PASS, 10 files scanned, several entries this week).
- `architecture/architecture.md` (v5), `architecture/design-system-manifest.md` (v2), `architecture/enhancement-audit-2026-05-02.md`, `architecture/session-2026-05-02-summary.md` — top-level architecture canon, kept paired with `mvp-readiness-checklist.md`.
- `legal/COI-60-starter-pack.md`, `legal/tos-and-disclosures-DRAFT.md` — ToS + risk-disclosures starter pack (v0.1 draft, requires counsel review before any public link).
- `research/massive-vs-ccxt-pro.md` — vendor spike, verdict: drop Massive, keep CCXT Pro through Phase 1, pull in Tardis.dev as the Phase 2 backtest source.
- 4 fresh daily code reviews (`CODE_REVIEW_2026-05-05_daily.md` through `CODE_REVIEW_2026-05-08_daily.md`).

---

## 6. Edits applied in this run

| File | Change | Status |
|---|---|---|
| `docs/api/backend-endpoints.md` | Full rewrite — 60 endpoints inventoried by tag from live source; aspirational endpoints reconciled in a "what changed" table; verification snippet appended. | **Applied** |
| `docs/api/api-overview.md` | Added `Last verified: 2026-05-08`; rewrote `/v2/` cutover anchor away from the stale 2026-04-30 date to "post-P0, June 2026". | **Applied** |
| `README.md` "Current status (2026-04-20)" | Bump date and append a 1-line note about Wave 1 closeout + ongoing daily code-review cadence. | **Recommended, not applied** — operator-owned line; defer to next manual pass. |
| `docs/risk/failsafes-and-kill-switches.md` | README's risk-framework reading order references this file but it was not located in the working tree. | **Recommended** — confirm location, create or relocate. |

No engine source files were modified in this run.

---

## 7. Open follow-ups for the next scheduled run

1. **Verify `docs/risk/failsafes-and-kill-switches.md`.** Either it lives elsewhere in the tree, has been renamed, or needs to be created. README's reading order assumes it exists.
2. **README "Current status" date bump** still pending — operator action.
3. **Standalone billing service decommission record.** The previous `CoinScopeAI-Context.md` and several archive files reference `billing/webhook_handler.py` running on port 8002. Today's working tree has only `billing/{models.py, stripe_gateway.py, webhooks.py}` under `coinscope_trading_engine/`. Confirm the standalone service is officially retired and add a one-line decommission note to `docs/ops/stripe-billing.md` if not already there.
4. **Engine code freeze status.** Five focus modules (`data/binance_websocket.py`, `data/binance_rest.py`, `data/market_stream.py`, `scanner/liquidation_scanner.py`, `signals/backtester.py`) have been unchanged for **5 days**. Daily code reviews continue to flag the same items (notably the WS_TESTNET_URL → mainnet-fallback CRITICAL, open since 2026-05-03). When freeze ends, the verification snippet in `backend-endpoints.md` should be re-run as part of the unfreeze PR.
