# CoinScopeAI — Canonical Structure Specification
# Version: 1.2 | Established: 2026-05-09 | Updated: 2026-05-10
# Authority: Single source of truth for naming and structure
# across Mac (Cowork), Drive, Notion, Linear, GitHub, and Claude project knowledge.

---

## 1. Naming Rules (Universal)

| Layer | Format | Example |
|---|---|---|
| Mac folders (numbered) | `NN-kebab-case/` | `01-project-overview/` |
| Mac folders (unnumbered, system) | `kebab-case/` | `scripts/`, `docs/` |
| Mac files | `kebab-case.ext` | `decision-log.md` |
| Drive folders | `NN — Title Case` | `01 — Project Overview` |
| Drive files | Title Case (Google Doc convention) | `Architecture v5` |
| Notion sections | `NN Title Case` | `01 Executive Dashboard` |
| Notion icons | Consistent per section (see §4) | `📊` for Dashboard |
| Linear labels | `scope: value` or `type: value` | `dom: risk`, `P1 – high` |
| GitHub branches | `type/coi-NN-short-desc` | `fix/coi-55-scanner-imports` |
| GitHub files | `kebab-case.ext` | `risk-framework.md` |

---

## 2. Canonical Folder Taxonomy (Mac + Drive)

15 numbered folders + archive. Applies to both Mac and Drive (different separators).

| # | Mac Name | Drive Name | Purpose | Drive Color |
|---|---|---|---|---|
| 01 | `01-project-overview/` | `01 — Project Overview` | Vision, OKRs, business plan, strategy | Blue |
| 02 | `02-architecture/` | `02 — Architecture` | Architecture docs, design system, ADRs | Gray |
| 03 | `03-roadmap/` | `03 — Roadmap & Planning` | Sprints, milestones, PCC criteria | Teal |
| 04 | `04-development/` | `04 — Development` | Engine code refs, .env templates, CI | Yellow |
| 05 | `05-risk/` | `05 — Risk Management` | Risk docs, thresholds, kill switch | Red |
| 06 | `06-reports/` | `06 — Reports & Analytics` | Weekly digests, KPI reviews | Orange |
| 07 | `07-runbooks/` | `07 — Runbooks & Processes` | SOPs, deployment, daily-ops | Purple |
| 08 | `08-sessions/` | `08 — Session Notes & Logs` | Code reviews, session summaries, audits | Pink |
| 09 | `09-research/` | `09 — Research & ML` | Market research, ML experiments, backtests | Cyan |
| 10 | `10-templates/` | `10 — Templates` | Reusable doc templates | Green |
| 11 | `11-legal/` | `11 — Legal & Compliance` | ToS, risk disclosures, data retention | Brown |
| 12 | `12-finance/` | `12 — Finance` | Budgets, P&L, Stripe records | Dark Blue |
| 13 | `13-marketing/` | `13 — Marketing & GTM` | GTM plans, brand, messaging | Magenta |
| 14 | `14-admin/` | `14 — Admin & Entity` | Corporate docs, EIN, entity records | Dark Gray |
| 15 | `15-agent-workforce/` | `15 — Agent Workforce` | AI agent definitions, prompts, hiring pipeline | Lime/Light Green |
| 99 | `99-archive/` | `99 — Archive` | Retired docs, pre-v1 material | Dark Gray |

### Note on folder 15 — Agent Workforce
The `agency-agents` Drive folder (currently unnumbered at Drive root) maps to this slot.
**Action needed:** rename `agency-agents` → `15 — Agent Workforce` in Drive UI.
Mac: create `15-agent-workforce/` when the agent pipeline work begins.
Notion: add `15 Agent Workforce` section to the OS when agents are actively being designed.
This is a **planned** slot — kept, not archived. Contents: agent system prompts, capability specs,
task delegation rules, hiring criteria, and per-agent SKILL.md files.

---

## 3. Mac Root — Allowed Files Only

Root should contain ONLY these files and directories:

**Config/system files (root-level OK):**
- `.env.example`, `.env.template`, `.gitignore`
- `docker-compose.yml`, `prometheus.yml`
- `requirements.txt`, `stripe_test_price_ids.json`
- `canonical-structure-spec.md` ← this file

**GitHub convention docs (root-level required):**
- `CLAUDE.md`, `CONTEXT_PRIMER.md`, `README.md`
- `CONTRIBUTING.md`, `CODEOWNERS`, `SECURITY.md`

**Directories:**
- Numbered: `01-project-overview/` through `15-agent-workforce/`, `99-archive/`
- System: `.claude/`, `.github/`, `.pytest_cache/`, `scripts/`, `docs/`
- Code: `coinscope_trading_engine/`, `coinscopeai-dashboard/`, `tests/`
- Skill sources: `skills/`

**Stale ghost dirs (empty, marked MOVED.txt — delete manually):**
```bash
rm -rf admin/ architecture/ legal/ incidents/ ml/ research/ strategy/
```

---

## 4. Notion Section Icons (Canonical — applied 2026-05-09)

| Section | Icon |
|---|---|
| CoinScopeAI OS (root) | 🚀 |
| 00 Hub | 🏠 |
| 01 Executive Dashboard | 📊 |
| 02 Projects & Roadmap | 🗺️ |
| 03 Tasks & Sprint Board | ✅ |
| 04 Quant Research Lab | 🔬 |
| 05 Strategy Validation | 🧪 |
| 06 Risk & Governance | 🛡️ |
| 07 Execution & Exchange Ops | ⚡ |
| 08 Engineering & Architecture | ⚙️ |
| 09 Monitoring & Incidents | 📡 |
| 10 Dashboard & Product UI | 🖥️ |
| 11 Reports & Stakeholder Updates | 📋 |
| 12 Meetings & Decision Log | 🗣️ |
| 13 Knowledge Base | 📚 |
| 15 Agent Workforce (future) | 🤖 |
| 99 Archive | 🗃️ |

---

## 5. Linear Label Taxonomy (27 labels — canonical, created 2026-05-09)

**Type (8):** `type: bug`, `type: feature`, `type: infra`, `type: docs`,
`type: research`, `type: refactor`, `type: test`, `type: config`

**Domain (9):** `dom: scanner`, `dom: risk`, `dom: exchange-api`, `dom: regime`,
`dom: alerts`, `dom: monitoring`, `dom: signals`, `dom: execution`, `dom: ui`

**Priority (4):** `P0 – urgent` (red), `P1 – high` (orange), `P2 – medium` (yellow), `P3 – low` (gray)

**SLO (2):** `SLO: No Data Loss` (red), `SLO: Code Quality` (blue)

**Status (3):** `status: tech-debt`, `status: needs-decision`, `status: validation-freeze`

---

## 6. GitHub Conventions

- Files: `kebab-case.ext`
- Branches: `type/coi-NN-short-description`
- Commits: `type(scope): description`
- Labels: match Linear taxonomy (script: `scripts/setup_github_labels.py`, classic PAT required)

---

## 7. Cross-Platform Sync Rules

1. Canonical doc change → update ALL platforms same session
2. Decision log: `business-plan/_decisions/decision-log.md` (Mac) + Notion `12 Meetings` (mirror)
3. Drive write: create in My Drive root → drag to folder via Finder (API writes to synced folders fail)
4. Duplicate Drive files: keep newest by `modifiedTime`, delete older copy
5. Sync order: Mac/GitHub → Linear → Notion → Drive
6. Ghost dirs (empty after moves): leave MOVED.txt, delete manually via Terminal

---

## 8. Drive Manual Actions Pending (API cannot rename)

Open Drive browser and do these 4 actions:

| Current | Action |
|---|---|
| `07 — Workflows & Processes` | Rename → `07 — Runbooks & Processes` |
| `09 — Resources & Research` | Rename → `09 — Research & ML` |
| `agency-agents` | Rename → `15 — Agent Workforce` |
| `.claude` | Delete (Cowork internal folder, shouldn't be in Drive) |
