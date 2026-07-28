# Changelog

All notable changes to CoinScopeAI are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> **Validation phase note:** The engine is in P0 testnet validation through ~May 31, 2026.
> No version is tagged as stable until PCC v2 §8 readiness criteria are met.

---

## [Unreleased]

### Changed
- `CLAUDE.md` → **v3.0** — replaced generic planning prompt with full Scoopy ops identity; canonical thresholds, pricing, personas, platform topology, phase map, pending actions
- `CONTEXT_PRIMER.md` → **v2.3** — bumped version, corrected git clone path (`coinscope-ai` → `CoinScopeAI`), corrected Scoopy prompt label (v2 → v3), folded COI-59 into COI-68 gate section
- `canonical-structure-spec.md` → **v1.2** — version bump for 2026-05-10 path corrections
- `Claude_Code_Script` — corrected launch path from `~/coinscopeai/scripts` → `/Users/mac/Documents/Claude/Projects/CoinScopeAI`
- `scripts/daily_status.sh` — corrected hardcoded position cap display from `/3` → `/5` (canonical MAX_OPEN_POSITIONS)
- `scripts/auto_sync.py` — corrected `REPO_DIR` from `~/Projects/coinscope-ai` → `~/Projects/CoinScopeAI`
- `scripts/sync_verify.py` — corrected `REPO` from `~/Projects/coinscope-ai` → `~/Projects/CoinScopeAI`
- `scripts/drift_detector.py` — added `"never quote"` to `HISTORICAL_MARKERS` to prevent false positives on CLAUDE.md v3 operating rules
- `scripts/risk_threshold_guardrail.py` — updated docstring reference from CLAUDE.md v2 → v3
- `.env.example` — Stripe price ID keys renamed from stale tier names (Starter/Pro/Elite/Team) → canonical Track B names (Free/Trader/Desk Preview/Desk Full v2); per-seat keys added
- `stripe_test_price_ids.json` — keys renamed to match canonical Track B tier names
- `coinscope_trading_engine/core/risk_gate.py` — constructor defaults corrected: `max_daily_loss_pct 0.10→0.05`, `max_drawdown_pct 0.20→0.10` (PCC v2 §8)
- `coinscope_trading_engine/live/pair_monitor.py` — `_save()` upgraded to atomic write + `OSError` handling; `record_trade()` logs warning on persist failure

### Fixed
- Stale path `~/coinscopeai/scripts` removed from all operator docs
- Stale path `~/Projects/coinscope-ai` removed from all scripts (repo renamed to `CoinScopeAI`)
- Cowork nightly drift-detector task working folder corrected (COI-73 closed)

---

## [Unreleased — pre-0.2.0]

### Added

- Full GitHub repository setup: branch protection on `main`, squash-only merge,
- PR template with validation-phase gate checklist
- Issue templates: bug report, feature request, strategy/risk change, config.yml chooser
- CODEOWNERS covering `risk_management/`, `engine/exchange/`, `engine/integrations/`,
  `coinscope.env.example`, `configs/environments/`, `CLAUDE.md`
- `Makefile` with `dev`, `test`, `lint`, `guardrail`, `sync`, `typecheck`, `clean` targets
- `pyproject.toml` with ruff, black, and pytest configuration
- Lint job added to CI (`ruff check` + `black --check`)
- `CHANGELOG.md` (this file)

### Changed
- `configs/environments/*.yaml`: `max_daily_loss_pct` corrected from `0.03` to `0.05`,
  `max_open_positions` corrected from `3` to `5`
- `risk_management/risk_gate.py`: constructor defaults corrected (`daily_loss 0.10→0.05`,
  `drawdown 0.20→0.10`)
- `coinscope_trading_engine/config.py`: `max_daily_loss_pct` default corrected `2.0→5.0`
- `coinscope_trading_engine/.env.example` / `.env.template`: `MAX_DAILY_LOSS_PCT` corrected
- README: correct repo structure, env filename, regime table, full endpoint list,
  circuit-breaker/reset endpoint, ADR table, validation freeze table
- CONTRIBUTING: two-reviewer paths corrected to v1 structure, protective scripts section added
- SECURITY: Sev-1/2/3 severity tiers added, coordinated disclosure policy
- Repo description updated to new tagline

### Fixed
- Stale `MAX_LEVERAGE=20x` references replaced with canonical `10x` across all docs
- Stale `MAX_OPEN_POSITIONS=3` references replaced with canonical `5` across all docs

---

## [0.1.0-testnet] — 2026-05-01

### Added
- Engine core: FastAPI HTTP layer, asyncio orchestrator, 5-scanner pipeline
- Risk gate: circuit breakers, exposure tracker, correlation analyzer, position sizer
- HMM regime detector (v3) — Trending / Mean-Reverting / Volatile / Quiet
- Telegram alert system (`@ScoopyAI_bot`) with rate limiting and priority queuing
- Binance USDT-M Testnet integration (REST + WebSocket)
- Redis cache layer with TTL management
- Prometheus metrics exporter on `:9090`
- Structured JSON logging with rotating file handler
- GitHub Actions CI: 15 smoke tests + security scan
- Business plan v1 locked across 16 sections (§1–§16)
- Canonical risk thresholds locked via PCC v2 §8 (2026-05-01):
  - `MAX_LEVERAGE=10x`, `MAX_OPEN_POSITIONS=5`, `MAX_DRAWDOWN_PCT=10%`,
    `MAX_DAILY_LOSS_PCT=5%`, `POSITION_HEAT_CAP_PCT=80%`, `KELLY_HARD_CAP_PCT=2%`
- DigitalOcean SGP1 deployment (Docker Compose + systemd)
- Stripe billing integration (test mode)
- Protective scripts: `drift_detector.py`, `risk_threshold_guardrail.py`,
  `sync_verify.py`, `daily_status.sh`

### Architecture decisions
- ADR-0001: FastAPI + Uvicorn as engine framework
- ADR-0002: Redis + Celery for async task queue
- ADR-0003: LLM calls prohibited on the hot path

---

[Unreleased]: https://github.com/3nz5789/CoinScopeAI/compare/v0.1.0-testnet...HEAD
[0.1.0-testnet]: https://github.com/3nz5789/CoinScopeAI/releases/tag/v0.1.0-testnet
