---
name: coinscopeai-architecture
description: CoinScopeAI System Architecture. Use this skill to understand the tech stack, project structure, dashboard deployments, GitHub repository, environment tiers, and deployment recommendations.
---

# CoinScopeAI System Architecture

**Last updated:** 2026-05-19 (Mac paths corrected — repo relocated 2026-05-04)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + TypeScript, Zustand, Recharts / TradingView Lightweight Charts |
| Backend Engine | FastAPI (Python 3.11+), SQLAlchemy, Pydantic, Celery |
| ML | LightGBM + Logistic Regression ensemble (162 features, v3 models) |
| Cache / Queue | Redis |
| Database | PostgreSQL (prod), SQLite (local dev) |
| Infrastructure | Docker Compose, GitHub Actions CI/CD |
| Integrations | Binance USDT-M Futures (testnet), Telegram Bot API, Stripe, OpenAI API (off hot path) |

---

## Repo Structure (v1 public — `3nz5789/CoinScopeAI`)

```
engine/              — FastAPI engine, risk gate, position sizing
apps/                — Application layer
backend/             — Backend services
services/            — Data ingestion pipelines
risk_management/     — Risk framework, kill switch
frontend/            — React dashboard (coinscopeai-dashboard/)
scripts/             — Operator tooling
tests/               — CI smoke tests + unit tests
docs/                — Architecture, runbooks, ADRs, ML docs
```

Mac Cowork layout (`~/Documents/Claude/Projects/CoinScopeAI/`):

```
coinscope_trading_engine/   — Core engine source (working tree)
coinscopeai-dashboard/      — Frontend React app (working tree)
docs/
  architecture/
    design-system-manifest.md   ← CANONICAL PATH (disk-verified 2026-05-18)
scripts/                    — drift_detector.py, sync_verify.py, guardrail, etc.
business-plan/              — §01–§16 + _decisions/decision-log.md
01-project-overview/
03-roadmap/
08-sessions/
13-skills/                  — skills_src/<plugin>/SKILL.md
```

---

## GitHub Repositories

| Repo | Visibility | Purpose |
|---|---|---|
| `3nz5789/CoinScopeAI` | Public | v1 engine — renamed 2026-05-09 from `coinscope-ai` |
| `3nz5789/CoinScopeAI_v2` | Private | v2 canonical thresholds — HEAD `4248912` |

### Mac Clone Paths (CORRECT — verified 2026-05-19)

| Repo | Mac Path | Status |
|---|---|---|
| v1 engine | `~/Code/CoinScopeAI` | ✅ Active (relocated 2026-05-04, commit `9645a79`) |
| v2 docs | `~/Documents/Claude/Projects/CoinScopeAI_v2` | ✅ Active |
| Cowork | `~/Documents/Claude/Projects/CoinScopeAI` | ✅ Active |
| `~/Projects/coinscope-ai` | RETIRED 2026-05-04 | ❌ Do not use |

**Never force-push between repos — independent git histories.**

---

## VPS

| Property | Value |
|---|---|
| Provider | DigitalOcean SGP1 |
| Host | `ubuntu@ip-172-31-15-30` |
| Engine dir | `/opt/coinscopeai/` |
| SSH key | `~/.ssh/` (standard Mac key) |
| Engine port | 8001 |
| Status | 🔴 Config stale — COI-68 pending |

---

## Dashboard

- **Live:** `https://coinscope.ai` / `https://app.coinscope.ai`
- **Engine API:** `https://api.coinscope.ai` (prod) / `http://localhost:8001` (local)
- Currently serving **mock data** — VPS restart pending (COI-68)

---

## Deployment

| Property | Value |
|---|---|
| Provider | DigitalOcean (NOT Hetzner — blocked by VAT ID for non-EU) |
| Spec | Basic 2 vCPU / 4 GB RAM / 80 GB SSD (~$24/mo) |
| Region | Singapore (SGP1) — low latency to Asian exchanges |
| Management | Docker Compose + systemd |

---

## CI/CD

| Job | Runner | Status |
|---|---|---|
| Tests (15 smoke tests) | ubuntu-22.04 | ✅ passing (commit `9724a1fd`) |
| Security Scan | ubuntu-22.04 | ✅ passing |
| CoinScopeAI CD | GitHub-native | ✅ always passes |

CI confirmed green — commit `9724a1fd`. Guardrail `tests/` exclusion added 2026-05-10.

---

## Claude Code Setup (verified 2026-05-19)

| Item | Value |
|---|---|
| Version | v2.1.144 |
| Login | `abu3anzeh@gmail.com` |
| Launch path | `cd ~/Code/CoinScopeAI && claude` |
| macOS permission | System Settings → Privacy & Security → Files and Folders → enable Claude |
| Known issue | Cannot launch nested `claude` from inside an active session — exit first (Ctrl+D) |

---

## Environment Tiers

1. **Research Idea** — prototyping new alpha or architecture
2. **Prototype** — local dev, isolated testing
3. **Staging Candidate** — Binance Testnet (current phase through ~May 31, 2026)
4. **Production Candidate** — live trading (gated by PCC v2 §8 readiness checklist)

All trading: **Binance Testnet only** (`testnet.binancefuture.com`) during validation.

---

## Design System (v3)

- Manifest: `docs/architecture/design-system-manifest.md` ← CANONICAL PATH (disk-verified 2026-05-18)
- CSS tokens in `coinscopeai-dashboard/client/src/index.css` (OKLCH color system)
- Primary/Profit: `oklch(0.70 0.17 162)` Emerald
- Background: `oklch(0.12 0.02 260)` Dark navy
- 45 shadcn/ui + 10 CoinScopeAI HUD components

*For risk thresholds: `coinscopeai-trading-rules`. For platform IDs: `coinscopeai-ops-secrets`.*
