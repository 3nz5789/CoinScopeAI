# Review workflow & approval states

The lifecycle of every component in the catalog. Pairs with [`docs/contributing.md`](./contributing.md) (the workflow narrative) and [`docs/component-map.json`](./component-map.json) (the catalog the workflow updates).

---

## Owner codes

Every component has an `owner` field that picks the team responsible for the contract.

| Code | Team | Owns |
|---|---|---|
| `ds` | Design Systems | All tokens, all primitives, theme variants, density modes, chrome (Sidebar / StatusBar), shared base archetypes |
| `trading` | Trading UX | Signals, regimes, strategies, position rows, alert items, KPI tiles, coin icons |
| `risk` | Risk UX | Risk widget, risk gauges, banners, liquidation warnings, kill-switch interactions |
| `platform` | Platform UX | App shell, auth, settings, AI explainer panels, system status |
| `brand` | Brand | Marketing surfaces, logos, brand-mark behavior |

Cross-team work — e.g., a trading component using new tokens — requires sign-off from both owners. `ds` is always the second reviewer when tokens change.

---

## Approval states

The `status` field in `docs/component-map.json` is the single source of truth. Allowed values and what they imply:

| State | What it means | Who can approve the transition |
|---|---|---|
| `idea` | Proposal opened (Issue Form filed). Not in the catalog yet. | — *(triage outcome)* |
| `preview` | HTML specimen exists in `preview/<name>.html`. **Not shipped to production.** Tokens may still move. | `ds` triage |
| `beta` | Implemented in `client/src/components/`, gated by a **feature flag**. Tokens locked. Public contract may break in MINOR. | Owner team + `ds` (if tokens) |
| `stable` | Shipped without a flag. Contract frozen until next MAJOR. Usage doc + ship checklist + visual regression baseline all required. | Owner team + `ds` |
| `deprecated` | Still shipping but on a removal path. `deprecated_in` and `removed_in` versions populated in `component-map.json`. Console warning required when used. | `ds` — 30-day notice |
| `removed` | Source files deleted. Entry kept in `component-map.json` for one MAJOR after removal as a tombstone with `replaces_with`. | `ds` — only at MAJOR cut |

### Allowed transitions

```
idea ─→ preview ─→ beta ─→ stable ─→ deprecated ─→ removed
                                          ↑
   preview can park here (kept around for a quarter, then revisited)
```

Forward transitions only. You don't un-deprecate a component; you ship a new one that `replaces_with` it.

### What gates each transition

| Transition | Required to ship |
|---|---|
| `idea → preview` | Issue Form filed. `ds` triage decided "build the specimen." |
| `preview → beta` | Specimen + production component + tokens locked + feature flag wired + smoke tests + entry in `component-map.json` with `status: beta`. |
| `beta → stable` | + Usage doc (six-section) + all 14 a11y ship-checklist items passing + visual regression baseline captured + at least one production consumer + 2-week soak under the flag. |
| `stable → deprecated` | + `replaces_with` field populated + console warning on use + entry in `docs/CHANGELOG.md` `### Deprecated` + plan for `removed_in` in the next MAJOR. |
| `deprecated → removed` | + ≥ 30 days since deprecation + zero remaining consumers (CI verifies) + tombstone entry in `component-map.json` carrying `replaces_with`. |

---

## Review flow (per PR)

Every design-system PR follows the same eight-step gate. Steps 1–4 are author-side; 5–8 are reviewer-side.

### Author side

1. **Filed Issue Form?** PR links the proposal issue. If no issue, this is a token-only PR or a trivial fix — note that in the description.
2. **`component-map.json` updated?** Every new file or status change goes in the catalog. CI fails otherwise.
3. **CHANGELOG entry under `[Unreleased]`?** Categorize: `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, or `### Breaking`.
4. **Ship checklist run?** The 14 items in [qa-checklist.md § 5](./qa-checklist.md#5-accessibility-ship-checklist). Paste the checklist into the PR body with each item checked or explicitly N/A.

### Reviewer side

5. **Owner-team review** — confirms behavior, content rules, glossary terms, naming match [docs/naming-rules.md](./naming-rules.md).
6. **`ds` review (if tokens move)** — confirms semantic-before-palette discipline, theme parity, no hex literals, no `backdrop-filter`.
7. **QA review** — minimum-run visual baseline captured ([qa-matrix.json `_minimum_run`](./qa-matrix.json)). Diffs accepted intentionally are noted in PR.
8. **Merge** — squash with the Conventional Commits PR title (see [naming-rules.md § Commits](./naming-rules.md#commits)). CI promotes the catalog status, updates baselines, and rolls the CHANGELOG into the next release.

---

## Reviewer assignment matrix

When you open the PR, request reviewers based on what you touched. CI auto-routes by file path; this is the human escalation order.

| If you touched … | Required reviewers |
|---|---|
| `client/src/index.css` | `ds` lead |
| `client/src/components/ui/*` (shadcn primitives) | `ds` lead + 1 platform engineer |
| `client/src/components/<Custom>.tsx` | Owner team (per component-map `owner`) + `ds` if tokens move |
| `client/src/pages/*` (page-level composition) | Owner team for that page area |
| `docs/component-map.json` | `ds` lead (catalog integrity) |
| `docs/qa-*` | `ds` lead + QA owner |
| `13-skills/skills_src/coinscopeai-design/*` | `ds` lead |
| `.github/ISSUE_TEMPLATE/design-*` | `ds` lead |

**Two-reviewer rule for breaking changes.** Any PR with `breaking` in the type, or any change touching deprecated → removed transitions, requires two reviewers and 48-hour open time before merge.

---

## Triage cadence

The `ds` team triages design-system Issue Forms in a weekly 30-minute sync. Outcomes per issue:

- **APPROVED** — assigned a `preview` slot for the current quarter. Author starts the HTML specimen.
- **PARK** — backlog. Re-reviewed at next triage. Default outcome for "interesting but not now."
- **REJECT** — closed with a written reason. Common reasons: "already covered by [existing component]", "conflicts with content-style rule X", "scope belongs in feature work, not the system."

A proposal in `PARK` for 90 days without further activity is auto-closed.

---

## Escalation

Disagreements between reviewers are resolved in this order:

1. **`ds` lead** has final say on tokens, theme parity, naming, and accessibility minimums.
2. **Owner team lead** has final say on the component's behavior and content semantics.
3. **Product / engineering directors** if (1) and (2) conflict for more than one review cycle.

Don't escalate without first writing a one-paragraph "what we disagree about" in the PR. Most disagreements resolve when both sides have to type their position.

---

## CI gates (enforced)

| Gate | What it checks | Where |
|---|---|---|
| `pnpm exec tsc --noEmit` | TypeScript clean in changed files | PR check |
| `pnpm run build` | Production build succeeds | PR check |
| `pnpm lint:design-tokens` | Every token referenced in components appears in `tokens_used` for that component in `docs/component-map.json` | PR check (planned — wire from existing component-map.json) |
| Visual regression | Minimum-run baseline (11 captures) diffs are within `maxDiffPixelRatio: 0.001` | PR check (planned — see `tests/visual.spec.ts.example`) |
| CHANGELOG check | PR adds a line under `## [Unreleased]` | PR check |
| Issue form linked | PR description links to a `design-component-*` issue, or has `tokens-only` label | PR check |

Items marked "planned" are skeleton-wired in `tests/visual.spec.ts.example` and `docs/component-map.json`'s `tokens_used` arrays; the GitHub Actions wiring isn't shipped yet.

---

## Release model

Versioning follows the spec's [SemVer rules](../../13-skills/skills_src/coinscopeai-design/SKILL.md#release):

| Change kind | Bump |
|---|---|
| Token rename · component removal · breaking prop signature | MAJOR |
| New component · new token · new variant · `beta → stable` promotion · new theme | MINOR |
| Token value tweak · bug fix · content rule clarification · `stable` component internal refactor | PATCH |

Token renames require a deprecation period: rename in the current MINOR, ship the shim in `legacy-tokens.css` for one MAJOR, remove the shim at the next MAJOR. Migration scripts go in `docs/MIGRATION.md` and are referenced from the CHANGELOG entry.
