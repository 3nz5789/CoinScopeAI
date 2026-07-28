# /99-archive — active dump for post-restructure superseded files

**Status:** active
**Charter:** Files superseded after the 2026-04-18 cleanup land here.
**Sister archive:** `../archive/` is the **frozen** pre-2026-04-18 archive — do not add to it.

Nothing in this folder is load-bearing. Items here are kept for history. They can be reviewed for deletion on a rolling basis.

## Current contents

| Item | What it is | Why it's here |
| --- | --- | --- |
| `CLAUDE.md.bak.20260503-151747` | CLAUDE.md backup snapshot | Captured before a major prompt edit on 2026-05-03 |
| `billing-root-legacy/` | Old billing module from before the structured `docs/ops/stripe-billing-runbook.md` reorganization | Superseded by the documented runbook + Stripe MCP read-only convention |
| `dashboard-html-stale/` | Pre-React dashboard HTML scraps (`pnl_widget.html`, `pricing.html`, `billing_success.html`) | Replaced by the React `coinscopeai-dashboard/` |
| `skills_src-empty/` | Empty placeholder folder from earlier skill scaffolding | Superseded by the populated `13-skills/skills_src/` |
| `testnet_trader/` | Old testnet trader scratch files | Superseded by the canonical engine + the testnet validation cohort runbook |

## How to add to this archive

```bash
git mv <path-to-superseded-thing> 99-archive/<descriptive-name>/
```

Update this README with a row in the table when you do.

## How to resurrect something

```bash
git mv 99-archive/<path> <where it should live>
```

History is preserved — these files are NOT git-ignored.

## Why two archives?

`archive/` was created during the 2026-04-18 repo cleanup and is a snapshot of pre-restructure state — frozen on purpose so old code reviews and pre-restructure context stay coherent. `99-archive/` is the ongoing dump for things superseded after that cleanup.

If `archive/` reaches its 2026-07-01 review date and gets cleared, the two folders may merge — but that's a deliberate decision, not an automatic consequence.
