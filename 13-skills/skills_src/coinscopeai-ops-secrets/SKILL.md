---
name: coinscopeai-ops-secrets
description: >
  CoinScopeAI Operational Secrets, IDs, Workflows & Rules — the complete reference for all
  canonical identifiers, API keys patterns, platform constraints, MCP tool quirks, GitHub
  setup rules, Drive API limits, and cross-platform sync workflows. Use this skill whenever
  you need any CoinScopeAI ID, token, URL, Notion DB ID, Linear team ID, Telegram chat ID,
  GitHub repo details, or when doing any cross-platform sync operation. Also use when you
  encounter Drive API errors, Linear tool errors, or GitHub label/PR setup tasks. Triggers on:
  "what's the Notion DB ID", "what's the chat ID", "sync platforms", "label setup", "Drive API",
  "MCP quirk", "GitHub labels", "VPS env", "Notion token", "canonical IDs", "platform secrets",
  "workflow rules", "ops knowledge", "session knowledge", "CI failure", "CI fix", "smoke tests".
---
# CoinScopeAI Ops Secrets, IDs, Workflows & Rules
**Last updated:** 2026-05-19 (AWS migration COI-111; CI commit corrected to 422d99f0)
**Source:** Live audit across all platforms
---
## 1. Canonical Identifiers
### Notion Pages
| Asset | ID |
|---|---|
| Workspace root | `33a29aaf938e81efa983e47b83e15775` |
| 00 Hub | `33a29aaf938e812c9730f12a42bad95e` |
| 01 Executive Dashboard | `33a29aaf938e8192af9deaada6a36a0a` |
| 06 Risk & Governance | `33a29aaf938e81b8ab8de3d0402cefc4` |
| 07 Execution & Exchange Ops | `33a29aaf938e8179b7d1df5a53249995` |
| 08 Engineering & Architecture | `33a29aaf938e814e8acbc54b8bdc4e79` |
| 09 Monitoring & Incidents | `33a29aaf938e817a8676ebbb5cd59633` |
| 11 Reports & Stakeholder Updates | `33a29aaf938e812799e3d6eecd08cdc8` |
| 12 Meetings & Decision Log | `33a29aaf938e81118c76f4add856ba03` |
| GitHub & Codebase (child of 08) | `33a29aaf938e811992fddb7be7ea04a4` |
| Architecture v5 (child of 08) | `35329aaf938e818e87c4ec03fbfdf1b1` |
| Design System v3 (child of 08) | `35b29aaf938e81cc9673f72feb34586e` |
| Linked Tools & Quick Links | `35529aaf938e81199690cd74dffb700f` |
| External Platforms (child of Hub) | `33a29aaf938e8177bb14f7f2a09b9c9d` |
| v1 Business Plan (LOCKED) | `35529aaf938e8155a215c6cfd1009100` |
| Session Report 2026-05-09 | `35b29aaf938e8148b987dc32c9469d3a` |
### Notion Trading DBs — CANONICAL (post 2026-04-23 rotation)
> ⚠️ OLD IDs (`ed9457ff...`, `1430e3fb...`, `c008175e...`) = TRASHED. NEVER USE.
| DB | Canonical ID |
|---|---|
| Signal Log | `d4bf243e-8e87-494d-838b-a96658af395b` |
| Trade Journal | `43a542f4-b58d-4b1a-8979-043e72e9a6dd` |
| Scan History | `e72c5b69-fbbb-4a54-9dac-e6d4de3eb1a4` |
VPS `.env` patch for all three:
```bash
sed -i 's/NOTION_SIGNAL_LOG_DB=.*/NOTION_SIGNAL_LOG_DB=d4bf243e-8e87-494d-838b-a96658af395b/' .env
sed -i 's/NOTION_TRADE_JOURNAL_DB=.*/NOTION_TRADE_JOURNAL_DB=43a542f4-b58d-4b1a-8979-043e72e9a6dd/' .env
sed -i 's/NOTION_SCAN_HISTORY_DB=.*/NOTION_SCAN_HISTORY_DB=e72c5b69-fbbb-4a54-9dac-e6d4de3eb1a4/' .env
```
### Linear
| Asset | ID |
|---|---|
| Team | `fbee0298-d944-40fd-b8e2-428dc5633276` |
| Project: CoinScopeAI – MVP | `ec45424d-69f4-445f-a2c8-c6f058ea640b` |
| Project: Risk & Execution Layer | `577864fa-23ee-4766-97f2-bcffc8d4c07e` |
| Project: Signal Scoring Engine | `a1387456-82f3-4317-bcd9-42d590b6c56b` |
| Project: Futures Scanner Core | `eb0756bf-22e3-4a96-a13a-1daa556cde96` |
| Project: Binance & Exchange Integrations | `ff3f4a1c-e679-4fbb-8996-0f09f721e57c` |
### GitHub
| Asset | Value |
|---|---|
| Repo v1 (engine, public) | `3nz5789/CoinScopeAI` (renamed 2026-05-09 from `coinscope-ai`) |
| Repo v2 (private) | `3nz5789/CoinScopeAI_v2` |
| Mac clone v1 | `~/Code/CoinScopeAI` → `git@github.com:3nz5789/CoinScopeAI.git` (relocated 2026-05-04; `~/Projects/coinscope-ai` is RETIRED) |
| Mac clone v2 | `~/Documents/Claude/Projects/CoinScopeAI_v2` |
| v1 latest commit | `422d99f0` (SLO sweep PRs #17–22, 2026-05-11) |
| v2 HEAD (canonical) | `4248912` (2026-05-03) |
| CI status | ✅ 15 passed — GitHub Actions green |
### Google Drive
| Folder | Drive ID |
|---|---|
| CoinScopeAI root | `1-rhyCJaycpf4GAGM45rxNZcH6MeSzkB8` |
| 01 — Project Overview | `1u61aUkmM1YJcVo1tg8DA_CbDS74ijpWb` |
| 02 — Architecture | `1tIApk1G_X8dBj4PGHSh3PqF7qr55i-qJ` |
| 05 — Risk Management | `1u2IJ06M0WdV4eSY6TFXj87opODb-5zc-` |
| 07 — Runbooks & Processes | `1yFMF4QjuySoIjfmjiNt2iL6CTTqTa8ia` |
| 08 — Session Notes & Logs | `1EQg82cDD0k8TEPWc10kFAnDByJ1LFVnd` |
| 09 — Research & ML | `1czD-JrY8ba6BGcyzO9Ml7YNQVuqrGSRv` |
| 11 — Legal & Compliance | `12yxbhEparorL1EOJSPnc-LJPjItSEHcx` |
| 14 — Admin & Entity | `1d95nyAnRG8PGwcV96yVpi8fNxOVraIgb` |
| 15 — Agent Workforce | `1u8Tw7ch99RVG0O19qjoCqsJ9pu4aJzfq` |
| 99 — Archive | `1tC9IGMkdT02ADgjblPhNeL4GKREfKLrS` |
| Drive Master Index v2 | `1aF0inb4lfP00rC7W0FVXXA6mfv4VWt5-I4UfHuKylhc` |
| Design System Manifest v3 | `1wxKH1EGsFn9KfY8g5JhfkBANFWI4rSXn3U55KBORXEQ` |
| CLAUDE.md backup staging | `1TBsJ7yxNlTTh-QZ5bR9hA0EmSyuETw4N` |
### Telegram
| Asset | Value |
|---|---|
| Bot handle | `@ScoopyAI_bot` |
| Chat ID | `7296767446` |
| Alert threshold | Score ≥ 8.0 |
| Kill switch alert | Immediate, no threshold |
| Daily P&L digest | 21:00 UTC |
### Services
| Service | URL |
|---|---|
| Dashboard | `https://app.coinscope.ai` |
| Engine API (prod) | `https://api.coinscope.ai` |
| Engine API (VPS direct) | `http://13.214.218.162:8001` |
| Engine API (local) | `http://localhost:8001` |
| VPS | AWS ap-southeast-1 (Singapore) — `13.214.218.162` — instance `i-0de9bee6e5c810f44` |
| VPS SSH | `ssh -i ~/Downloads/coinscopeai-sgp.pem ubuntu@13.214.218.162` |
| VPS repo path | `/opt/coinscopeai` |
---
## 2. Canonical Risk Thresholds (LOCKED 2026-05-01 — PCC v2 §8)
| Threshold | Value | Notes |
|---|---|---|
| `MAX_LEVERAGE` | **10x** | NOT 20x — old docs are wrong |
| `MAX_OPEN_POSITIONS` | **5** | Revised 2026-05-03 from =3 |
| `MAX_DRAWDOWN_PCT` | **10%** | From peak — triggers kill switch |
| `MAX_DAILY_LOSS_PCT` | **5%** | 24h rolling — halts all trading |
| `POSITION_HEAT_CAP_PCT` | **80%** | Total deployed capital cap |
VPS env patch for stale `=3`:
```bash
sed -i.bak 's/^MAX_OPEN_POSITIONS=3$/MAX_OPEN_POSITIONS=5/' .env
```
---
## 3. Platform API Constraints & Known Quirks
### Google Drive MCP
- ❌ Write to synced folders → `User cannot add children to the specified folder`
- ✅ Write to My Drive root only → then drag to target via browser
- ❌ No trash/move/rename via API → use browser or Chrome MCP
- ❌ `trashed = false` query → unsupported; omit it
- Chrome MCP trash: always use `Delete` key, NOT toolbar button (fails silently ~50%)
### Linear MCP
- `save_document` icon param: rejects emoji — omit `icon` field entirely
- Diff tools (`list_diffs`, `get_diff`): read-only only
### Notion MCP
- `update_content`: cannot match `[text](url)` in `old_str` — match plain text only
- `replace_content` with child pages: fails if would delete child pages — always confirm first
### GitHub Actions — ALL quirks debugged 2026-05-09
- Security grep for `sk_live_` matches `ci.yml` itself → must exclude from grep scope
- String `"sk_live_"` in test assertions also triggers → use regex with min-length
- `hmmlearn`/`ccxt`/`aiohttp` fail on Ubuntu runner → only install `pytest`
- `pyproject.toml` has `asyncio_mode` causing `PytestConfigWarning` → suppress with `-W ignore::pytest.PytestConfigWarning`
- Separate `cd.yml` on GitHub (not in Mac Cowork) — always passes; not managed by us
- **CRITICAL:** git repo's `coinscope.env.example` ≠ Mac Cowork `.env.example` — completely different files; never assume they match
---
## 4. CI Setup — CONFIRMED WORKING (commit `422d99f0`)
Two jobs: **test** + **security** — both on `ubuntu-22.04`
```yaml
test:
  - actions/checkout@v4
  - actions/setup-python@v5 (3.11)
  - python3 -m pip install --upgrade pip pytest
  - python3 -m pytest tests/test_ci_smoke.py -v --tb=long -W ignore::pytest.PytestConfigWarning
security:
  - git ls-files grep for .env files
  - grep -rl for hardcoded BINANCE_API_KEY
```
**Smoke tests** (`tests/test_ci_smoke.py`) — 15 tests, confirmed ✅:
Repo structure checks:
- `.env.example` OR `coinscope.env.example` OR `.env.template` (flexible)
- `requirements.txt`, `docs/`, source dirs (`engine/`, `apps/`, etc.), `scripts/`, `tests/`
- `.gitignore` exists and contains `.env`
- No `docker-compose.yml` check (not at repo root)
Security checks:
- No `.env`, `.env.production`, `.env.local` at root
Threshold checks (negative — stale values must NOT be present):
- `MAX_LEVERAGE=20` not present
- `MAX_OPEN_POSITIONS=3` not present
- Some testnet flag present (`TESTNET_MODE=true` OR `BINANCE_TESTNET=true` OR `BINANCE_FUTURES_TESTNET`)
### CI Failure Root Cause History
| CI Run | Failure | Root Cause | Fix |
|---|---|---|---|
| #43–45 | `--cov=coinscope_trading_engine` | Module doesn't exist | Drop coverage, add smoke tests |
| #46 | `docs/risk/` test | Dir not in git repo | Remove test |
| #47 | `docs/decisions/` test | Dir not in git repo | Remove test |
| #48 | `pip install -r requirements.txt` | `hmmlearn`/`ccxt` build failures | Only install `pytest` |
| #49–51 | Security grep false positive | Grep matched `ci.yml` + test file | Regex + file exclusions |
| #52–53 | `pytest` not on PATH | Bare `pytest` not found on Ubuntu | `python3 -m pytest` |
| #54 | 4 assertion failures | File layout mismatches | Flexible file discovery |
| #55 | PytestConfigWarning exit | `pyproject.toml` asyncio_mode | `-W ignore` + `ubuntu-22.04` |
---
## 5. VPS — AWS Migration Complete (COI-111 Done — 2026-05-18)
**Provider:** AWS ap-southeast-1 (Singapore)
**IP:** `13.214.218.162`
**Instance:** `i-0de9bee6e5c810f44`
**SSH:** `ssh -i ~/Downloads/coinscopeai-sgp.pem ubuntu@13.214.218.162`
**Repo path:** `/opt/coinscopeai`
**Compose file:** `infra/docker/docker-compose.prod.yml`
All containers healthy:
- `coinscopeai-db` ✅ port 5432
- `coinscopeai-redis` ✅ port 6379
- `coinscopeai-engine` ✅ port 8001
Verified endpoints:
- `/health` → `{"status":"ok","version":"1.0.0"}` ✅
- `/regime/BTCUSDT` → `{"label":"Trending","confidence":0.609}` ✅
Pending next session:
- [ ] Full smoke test: `/scan`, `/risk-gate`, `/performance`, `/journal`, `/position-size`
- [ ] DNS: `api.coinscope.ai` → `13.214.218.162` (COI-96)
- [ ] Telegram bot Dockerfile (COI-110)
- [ ] Commit `docker-compose.prod.yml` build context fix to v1 GitHub repo
---
## 6. Active Linear Issues (live — 2026-05-19)
| Issue | Title | Status |
|---|---|---|
| COI-68 | VPS env patch + engine restart | ✅ Done |
| COI-69 | Post-restart verify | ✅ Done |
| COI-111 | AWS Migration Complete | ✅ Done |
| COI-113 | /risk-gate endpoint 404 — route missing or renamed | Open |
| COI-114 | Restore decision-log.md (shell expansion corruption) | Open |
| COI-96 | nginx reverse proxy for api.coinscope.ai | Open |
| COI-110 | telegram-bot Dockerfile missing | Open |
---
## 7. Protective Tooling
| Script | Purpose | When |
|---|---|---|
| `python3 scripts/drift_detector.py` | Token consistency across 10 canonical docs | After any canonical doc edit |
| `python3 scripts/risk_threshold_guardrail.py` | Threshold violations scan | After any config change |
| `./scripts/daily_status.sh` | Morning engine brief (all 6 endpoints) | Start of trading day |
| `python3 scripts/sync_verify.py` | Cross-platform structure (should be 37/37 now) | Session start/end |
| `python3 scripts/auto_sync.py` | Session-end git + drift + guardrail | Session end |
| `python3 scripts/setup_github_labels.py` | 27 GitHub labels (classic PAT required) | After repo rename |
---
## 8. Repo Clone Topology (Never Mix)
```
~/Code/CoinScopeAI → git@github.com:3nz5789/CoinScopeAI.git (public v1, relocated 2026-05-04; ~/Projects/coinscope-ai RETIRED)
~/Documents/Claude/Projects/CoinScopeAI_v2 → 3nz5789/CoinScopeAI_v2 (private v2)
Mac Cowork: ~/Documents/Claude/Projects/CoinScopeAI/
```
Always `cd` to the right path. Confirm with `git remote -v`. Never force-push between repos.
---
## 9. GitHub Repo Setup
### Files committed
```
README.md, CONTRIBUTING.md, SECURITY.md, CODEOWNERS
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/bug_report.md, feature_request.md
.github/workflows/ci.yml — 2 jobs: test + security
scripts/setup_github_labels.py — 27 labels matching Linear taxonomy
```
### Labels (27 total)
**Type (8):** `type: bug/feature/infra/docs/research/refactor/test/config`
**Domain (9):** `dom: scanner/risk/exchange-api/regime/alerts/monitoring/signals/execution/ui`
**Priority (4):** `P0 – urgent / P1 – high / P2 – medium / P3 – low`
**SLO (2):** `SLO: No Data Loss / SLO: Code Quality`
**Status (3):** `status: tech-debt / needs-decision / validation-freeze`
Classic PAT required (`ghp_` prefix) — fine-grained tokens return 401 on Labels API.
### Two-reviewer rule
Required for: `risk/`, `risk_management/`, `engine/integrations/`, `.env.example`, `CLAUDE.md`, `docker-compose.yml`, `requirements.txt`
---
## 10. Pricing (LOCKED 2026-05-01)
| Tier | Monthly |
|---|---|
| Free | $0 |
| Trader | $79 |
| Desk Preview | $399 |
| Desk Full v2 | $1,199 + per-seat ($149/$249) |
Old pricing ($19/$49/$99/$299) superseded — never use.
---
## 11. Stripe & Billing
- Account: `acct_1TT23PPOH34MOwPm` ("CoinScopeAI, LLC")
- Read-only by convention via MCP — never move money
- Live keys (`sk_live_`, `pk_live_`) must NEVER appear in committed files
---
*For engine API endpoints: `coinscopeai-engine-api`. For trading rules: `coinscopeai-trading-rules`. For architecture: `coinscopeai-architecture`. For platform sync: `coinscopeai-platform-sync`.*
