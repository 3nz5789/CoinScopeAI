# CoinScopeAI — Context Primer
# Version: 2.4 | Updated: 2026-05-19 (VPS COI-68 Done, AWS migration, clone paths corrected, DSM path fixed)

**Read first** when starting a new Scoopy session. The 60-second on-ramp.

---

## Who am I (Scoopy)

The named in-product AI agent and Telegram companion (@ScoopyAI_bot) for CoinScopeAI.
Source-of-truth prompt is `CLAUDE.md` at the project root. Read it for voice, registers, copy.

---

## Canonical Folder Structure (post 2026-05-09 restructure)

```
CoinScopeAI/                          ← Cowork project root (Mac)
├── CLAUDE.md                         ← Master Scoopy prompt ★
├── CONTEXT_PRIMER.md                 ← This file ★
├── README.md / CONTRIBUTING.md / SECURITY.md / CODEOWNERS
├── .env.example / .env.template / .gitignore / docker-compose.yml
├── requirements.txt / prometheus.yml / stripe_test_price_ids.json
│
├── 01-project-overview/              ← Vision, OKRs, business-plan v1, strategy
│   ├── business-plan-v1.md
│   ├── business-plan/                ← 17 framework sections (§00–§16)
│   └── strategy/
│       └── strategic-memo-2026-04-29.md
│
├── 03-roadmap/                       ← PCC v2, MVP checklist, validation plans
│   ├── production-candidate-criteria-v2.md
│   ├── mvp-readiness-checklist.md
│   ├── validation-data-analysis-plan-v1.md
│   └── validation-phase-exit-memo-template.md
│
├── 08-sessions/                      ← Session notes, code reviews, audits
│   ├── CODE_REVIEW_*.md
│   ├── CONFIG_AUDIT_*.md
│   ├── OPS_Linear_Tickets_v1.md
│   ├── enhancement-audit-2026-05-02.md
│   └── session-summary-2026-05-02.md
│
├── 09-research/                      ← Market research, vendor analysis
│   ├── vendor-failure-mode-mapping-v1.md
│   └── massive-vs-ccxt-pro.md
│
├── 11-legal/                         ← ToS, risk disclosures, data retention
│   ├── tos-and-disclosures-DRAFT.md  ← PRE-COUNSEL
│   ├── data-retention.md
│   └── counsel-brief-v2.md
│
├── 14-admin/                         ← EIN docs, entity forms
│   └── *.pdf
│
├── 99-archive/                       ← Retired material
│   └── dashboard-html-stale/         ← Old HTML mockups
│
├── docs/                             ← Technical documentation
│   ├── architecture/                 ← architecture.md (v5), design-system-manifest.md
│   ├── risk/                         ← risk-framework, risk-gate, position-sizing, kill-switch
│   ├── runbooks/                     ← deployment, daily-ops, troubleshooting
│   ├── ml/                           ← regime-detection, confidence baseline, classifiers
│   ├── incidents/                    ← incident reports, digests, drift log
│   ├── decisions/                    ← ADRs (adr-000N-*.md)
│   ├── onboarding/                   ← new dev guide
│   └── api/                          ← API reference
│
├── scripts/                          ← Operator scripts
│   ├── drift_detector.py
│   ├── risk_threshold_guardrail.py
│   ├── daily_status.sh
│   ├── setup_github_labels.py
│   ├── billing_server.py
│   └── validation_analysis.py
│
├── skills/                           ← Operational skill scripts (drift-detector, decision-log-appender)
│   ├── decision-log-appender/
│   └── drift-detector/
│
├── 13-skills/                        ← Plugin skill sources (canonical)
│   └── skills_src/                   ← 7 coinscopeai-* plugin SKILL.md files
│       ├── coinscopeai-architecture/
│       ├── coinscopeai-engine-api/
│       ├── coinscopeai-mempalace-ops/
│       ├── coinscopeai-ops-secrets/
│       ├── coinscopeai-platform-sync/
│       ├── coinscopeai-task-naming-standard/
│       └── coinscopeai-trading-rules/
│
├── coinscope_trading_engine/         ← Python engine (mirrors git repo)
├── coinscopeai-dashboard/            ← React dashboard (mirrors git repo)
└── tests/                            ← Top-level test suite
```

Git repos (separate, NOT inside this folder):
- `~/Code/CoinScopeAI` → `github.com/3nz5789/CoinScopeAI` (public; relocated 2026-05-04 from `~/Projects/coinscope-ai`)
- `~/Documents/Claude/Projects/CoinScopeAI_v2` → `github.com/3nz5789/CoinScopeAI_v2` (private; `~/Projects/CoinScopeAI_v2` RETIRED)

---

## Where canonical truth lives

| Asset | Path |
|---|---|
| Master prompt (Scoopy v3) | `CLAUDE.md` (project root) |
| Architecture v5 | `docs/architecture/architecture.md` |
| Design system manifest | `docs/architecture/design-system-manifest.md` |
| Decision log (append-only) | `business-plan/_decisions/decision-log.md` |
| ADRs | `docs/decisions/` |
| Risk framework | `docs/risk/risk-framework.md` |
| Risk gate doc | `docs/risk/risk-gate.md` |
| Position sizing | `docs/risk/position-sizing.md` |
| Kill switches | `docs/risk/failsafes-and-kill-switches.md` |
| Business plan v1 (LOCKED) | `01-project-overview/business-plan/` |
| PCC v2 (production gate) | `03-roadmap/production-candidate-criteria-v2.md` |
| MVP checklist | `03-roadmap/mvp-readiness-checklist.md` |
| ToS draft | `11-legal/tos-and-disclosures-DRAFT.md` |
| Data retention | `11-legal/data-retention.md` |
| Canonical structure spec | `canonical-structure-spec.md` (root) |

---

## What runs where

| Service | URL |
|---|---|
| Engine API (dev) | `http://localhost:8001` |
| Engine API (prod) | `https://api.coinscope.ai` |
| Dashboard | `https://app.coinscope.ai` |
| GitHub v1 | `https://github.com/3nz5789/CoinScopeAI` |
| GitHub v2 | `https://github.com/3nz5789/CoinScopeAI_v2` |
| Drive root | `https://drive.google.com/drive/folders/1-rhyCJaycpf4GAGM45rxNZcH6MeSzkB8` |
| Claude.ai project | `https://claude.ai/project/019d2c36-cda3-71c0-8dd6-a71426f17bef` |
| Notion workspace | `https://www.notion.so/33a29aaf938e81efa983e47b83e15775` |
| Telegram bot | `@ScoopyAI_bot` (Chat ID: `7296767446`) |
| Stripe account | `acct_1TT23PPOH34MOwPm` "CoinScopeAI, LLC" (live, read-only by convention; rotated from `acct_1Fpg5iAnTwL0DrQw` between 2026-05-03 and 2026-05-11) |

---

## Canonical Risk Thresholds (LOCKED 2026-05-01, PCC v2 §8)

| Threshold | Value |
|---|---|
| MAX_LEVERAGE | **10x** per position (NOT 20x) |
| MAX_OPEN_POSITIONS | **5** concurrent (revised 2026-05-03 from =3) |
| MAX_DRAWDOWN_PCT | **10%** from peak |
| MAX_DAILY_LOSS_PCT | **5%** rolling 24h |
| POSITION_HEAT_CAP_PCT | **80%** deployed capital |

---

## Operating principles

1. **Testnet only** — never place real orders; gated by PCC v2 §8
2. **Anti-overclaim** — never say "production-ready" without PCC v2 §8 reference
3. **Risk-first** — thresholds above are first-class, non-negotiable
4. **No engine changes** during validation phase
5. **Canonical structure** — everything in numbered folders; nothing loose at root except the 6 GitHub convention files

---

## Protective tooling

```bash
python3 scripts/drift_detector.py           # check canonical doc consistency
python3 scripts/risk_threshold_guardrail.py # check codebase for threshold violations
./scripts/daily_status.sh                   # morning engine brief (all 6 endpoints)
python3 scripts/setup_github_labels.py      # rebuild GitHub labels (needs classic ghp_ token)
```

---

## VPS action gate — COMPLETED (COI-68 Done 2026-05-17, COI-69 Done)

```bash
# All applied. MAX_OPEN_POSITIONS=5, MAX_LEVERAGE=10 confirmed on VPS 2026-05-19.
# VPS: AWS ap-southeast-1 (Singapore) — 13.214.218.162 — /opt/coinscopeai/
# SSH: ssh -i ~/Downloads/coinscopeai-sgp.pem ubuntu@13.214.218.162
```

---

## Platform sync rules

| Platform | Naming format | Color/style |
|---|---|---|
| Mac | `NN-kebab-case/` | — |
| Drive | `NN — Title Case` | Color per section (see canonical-structure-spec.md) |
| Notion | `NN Title Case` | Icon per section (see spec) |
| Linear | `type: value`, `dom: value` | Priority = color-coded |
| GitHub | `kebab-case` files, `type/coi-NN-desc` branches | — |

Sync order: Mac/GitHub → Linear → Notion → Drive

---

## Anti-pattern reminders

- ❌ `20x` leverage → it's `10x`
- ❌ Old pricing `$19/$49/$99/$299` → `Free / Trader $79 / Desk Preview $399 / Desk Full $1,199`
- ❌ "production-ready" without PCC v2 §8 reference
- ❌ `coinscope-ai` repo → now `CoinScopeAI`
- ❌ Loose files at project root
- ❌ Old Cowork path `~/coinscopeai/` or `~/Projects/coinscope-ai` → canonical: `/Users/mac/Documents/Claude/Projects/CoinScopeAI`
- ❌ `architecture/` folder at root → now `docs/architecture/`
- ❌ `legal/` folder at root → now `11-legal/`
- ❌ `incidents/` at root → now `docs/incidents/`
