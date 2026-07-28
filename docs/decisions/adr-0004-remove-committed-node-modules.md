# ADR-0004: Remove committed frontend/node_modules from git index

**Status:** accepted
**Date:** 2026-05-12
**Authors:** Mohammed Abuanza, Scoopy
**Related:** COI-86, `chore/remove-node-modules` PR (merged 2026-05-12)

## Context

The v1 repo (`3nz5789/CoinScopeAI`) had `frontend/node_modules/` committed in its git tree — 24,432 tracked files. This happened because the directory was added before the `.gitignore` rule covering it was in place. Once files are tracked in the git index, `.gitignore` rules have no effect on them; the rule was present but silently inert.

The presence of vendored JS dependencies in the repo caused three concrete problems:

1. **Clone bloat** — every `git clone` downloaded 24,432 binary and generated files that belong in `.pnpm-store`, not version control.
2. **CI overhead** — the `actions/checkout` step in every CI run transferred all those files unnecessarily.
3. **Credibility signal** — a public repo with committed `node_modules` reads as unpolished, which matters during P0 when the cohort and early investors may inspect the codebase.

The `.gitignore` already had `coinscopeai-dashboard/node_modules/`, but the actual committed path was `frontend/node_modules/` — a naming mismatch that meant neither rule fired.

## Decision

Remove all `frontend/node_modules/` entries from the git index using `git rm -r --cached`, add the correct `frontend/node_modules/` rule to `.gitignore`, and merge via the standard protected-branch PR flow.

The lockfile (`pnpm-lock.yaml`) is retained — it is source-controlled by design as the reproducibility anchor for `pnpm install`.

## Alternatives considered

- **Leave it** — no upside; bloat stays, CI stays slow, repo looks undisciplined. Rejected.
- **Delete the files from disk** — unnecessary and dangerous; `--cached` is the correct flag. Disk contents are the developer's working install and must not be removed.
- **Rewrite git history (BFG/filter-branch)** — would shrink `.git` pack size further but requires force-pushing, which violates the standing repo rule and disrupts any open branches. Not worth it for this size. Revisit if pack size becomes a problem.

## Consequences

**Positive:**
- `git clone` no longer downloads 24,432 vendored files
- CI `checkout` step is leaner
- `.gitignore` rules are now enforced correctly for both `frontend/` and `coinscopeai-dashboard/`
- Repo presents cleanly to P0 cohort reviewers and future contributors

**Negative / costs:**
- Developers must run `pnpm install` inside `frontend/` (or `coinscopeai-dashboard/`) after a fresh clone — this is standard and expected, but needs a note in `CONTRIBUTING.md`
- Historical git objects for the removed files remain in the `.git` pack until garbage collection; they are unreachable but not immediately purged

**Neutral but worth noting:**
- The `type: config` label was attempted on COI-86 but did not apply (label may not exist in workspace); `SLO: Code Quality` applied correctly

## Revisit when

- If `.git` pack size becomes a clone-speed issue after multiple large removals, run `git gc --aggressive` or BFG to rewrite history
- If a `frontend/` → `coinscopeai-dashboard/` rename happens, ensure `.gitignore` is updated and the index is clean before the rename commit

## Notes

The commit message on the merge was:

```
chore: remove committed node_modules from git index

frontend/node_modules was tracked (24,432 files) despite .gitignore.
Evicted with git rm -r --cached. Added frontend/node_modules/ rule
to .gitignore. Lockfile retained. Run pnpm install after fresh clone.
```

Linear: COI-86 (Done)
