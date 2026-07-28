---
name: coinscopeai-platform-sync
description: >
  CoinScopeAI Cross-Platform Sync — the complete operational workflow for keeping all folders,
  docs, sheets, images, and assets consistently structured and always in sync across Mac (Cowork),
  Google Drive, Notion, Linear, and GitHub. Use this skill whenever creating, moving, renaming,
  or updating ANY file or asset; when starting or ending a session; when a deliverable is produced;
  when a decision is made; when a doc needs to go to multiple platforms; or when any platform
  appears out of sync. Claude must sync automatically without being asked. Triggers on: sync
  platforms, where does this go, create a doc, add to notion, update drive, keep in sync,
  what folder, session end, new asset, new file, move this, upload to drive, structure, consistent.
---
# CoinScopeAI Cross-Platform Sync
**Last updated:** 2026-05-19 | **Rule 0:** Claude syncs automatically — never wait to be asked.
---
## Platform Status (live — 2026-05-19)
| Platform | Status | Auth |
|---|---|---|
| GitHub v1 (`CoinScopeAI`) | ✅ Live — CI green (`422d99f0`) | SSH key |
| GitHub v2 (`CoinScopeAI_v2`) | ✅ HEAD `4248912` | SSH key |
| Google Drive | ✅ Live (root writes only) | OAuth MCP |
| Notion | ✅ Live — all 14 sections current | OAuth MCP |
| Linear | ✅ Live — issues triaged | OAuth MCP |
| Mac / Cowork | ✅ Clean root, 15 folders | Filesystem MCP |
| VPS Engine | ✅ AWS ap-southeast-1 live — 13.214.218.162 (COI-111 Done) | SSH (manual) |
---
## Canonical Naming Convention
| Platform | Format | Example |
|---|---|---|
| Mac Cowork folders | `NN-kebab-case/` | `08-sessions/` |
| Google Drive folders | `NN — Title Case` | `08 — Session Notes & Logs` |
| Notion sections | `NN Title Case` | `08 Engineering & Architecture` |
| GitHub directories | `kebab-case/` | `risk-management/` |
| Linear issues | `[Domain · Type] Short verb phrase` | `[P0 · VPS] Reload .env on VPS` |
---
## Google Drive — Folder IDs
| Folder | Drive ID |
|---|---|
| Root | `1-rhyCJaycpf4GAGM45rxNZcH6MeSzkB8` |
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
**Drive API constraints:**
- ❌ Write to synced folders → fails with `User cannot add children`
- ✅ Write to My Drive root only → then drag to folder via browser
- ❌ No trash / move / rename via API
---
## Notion — Key Page IDs
| Section | Notion ID |
|---|---|
| Workspace root | `33a29aaf938e81efa983e47b83e15775` |
| 01 Executive Dashboard | `33a29aaf938e8192af9deaada6a36a0a` |
| 08 Engineering | `33a29aaf938e814e8acbc54b8bdc4e79` |
| 11 Reports | `33a29aaf938e812799e3d6eecd08cdc8` |
| 12 Meetings | `33a29aaf938e81118c76f4add856ba03` |
| Linked Tools | `35529aaf938e81199690cd74dffb700f` |
**Notion MCP constraints:**
- `update_content`: cannot match `[text](url)` in `old_str` — use plain text only
- `replace_content` with child pages: fails if would delete children — confirm first
---
## Linear
| Asset | Value |
|---|---|
| Team ID | `fbee0298-d944-40fd-b8e2-428dc5633276` |
| Workspace | `coinscopeai.linear.app` |
| Issue prefix | `COI-` |
27 labels, 5 projects. See `coinscopeai-ops-secrets` for active issues.
---
## GitHub
| Asset | Value |
|---|---|
| v1 repo | `3nz5789/CoinScopeAI` (public) |
| v2 repo | `3nz5789/CoinScopeAI_v2` (private) |
| Mac clone v1 | `~/Code/CoinScopeAI` (relocated 2026-05-04; `~/Projects/coinscope-ai` RETIRED) |
| Mac clone v2 | `~/Documents/Claude/Projects/CoinScopeAI_v2` |
**Token requirement:** Classic PAT (`ghp_` prefix) for Labels API — fine-grained returns 401.
---
## Sync Order (always follow this sequence)
1. **Mac / Git** — commit and push first
2. **Linear** — update issue status
3. **Notion** — update dashboard + relevant pages
4. **Drive** — upload if canonical doc changed
---
## Source of Truth Hierarchy
1. `~/Documents/Claude/Projects/CoinScopeAI_v2` (v2/main) — canonical risk thresholds
2. `~/Code/CoinScopeAI` (v1/main) — runbooks, ADRs, `.env.example` (relocated 2026-05-04)
3. Drive `01 — Project Overview/business-plan-v1/` — framework docs
4. Notion — mirror of Drive, always secondary
5. Linear — issue tracker, never a doc source
---
## Session Checklist
**Session start:** read CONTEXT_PRIMER.md → check Linear for urgent issues → verify sync_verify.py passes
**Session end:** commit all Mac changes → update Linear issue statuses → update Notion 01 Dashboard → `python3 scripts/auto_sync.py`
---
## sync_verify.py Status
35/37 checks passing — should reach 37/37 now engine is live on AWS (COI-111 Done).
*For all platform IDs and quirks: `coinscopeai-ops-secrets`.*
