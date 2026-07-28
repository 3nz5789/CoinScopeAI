# Contributing to the CoinScopeAI design system

> Engineering-wide contribution rules live in [`/CONTRIBUTING.md`](../../CONTRIBUTING.md) at the repo root. This doc is **design-system-specific** — what changes when the work touches `client/src/index.css`, a component in `client/src/components/`, a page in `client/src/pages/`, or the canonical token sheet.

## The four kinds of design-system contribution

| What you're doing | Open this | Approval gate |
|---|---|---|
| Propose a **new component** | [Issue Form · new component](https://github.com/3nz5789/CoinScopeAI/issues/new?template=design-component-proposal.yml) | `ds` team + owner team |
| Change an **existing component** | [Issue Form · component change](https://github.com/3nz5789/CoinScopeAI/issues/new?template=design-component-change.yml) | Owner team; `ds` only if tokens move |
| Deprecate or remove a component | [Issue Form · deprecation](https://github.com/3nz5789/CoinScopeAI/issues/new?template=design-deprecation.yml) | `ds` team + 30-day notice |
| Token-only change (color, spacing, radius, motion) | Engineering PR with `design-system: tokens` label | `ds` team — SemVer rules apply (rename = MAJOR) |

The Issue Form is required even for trivial-looking changes. The form's structured fields feed `docs/component-map.json` directly — it's how the catalog stays accurate.

## Workflow at a glance

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. PROPOSAL                                                             │
│    Open one of three Issue Forms. Filled-in form is the proposal.       │
│    Label auto-applied: design-system + (component | tokens | deprec).   │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 2. TRIAGE                                                               │
│    ds team triages in the weekly design-system sync.                    │
│    Outcomes: APPROVED → preview slot · PARK → backlog · REJECT → close. │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 3. PREVIEW BUILD                                                        │
│    Author ships an HTML specimen in preview/<name>.html using ONLY      │
│    tokens from colors_and_type.css. No production code yet.             │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 4. PRODUCTION PR                                                        │
│    Implement in client/src/components/. Update docs/component-map.json. │
│    Run qa-checklist.md § 5 ship checklist. Add tests/states.            │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 5. REVIEW                                                               │
│    Owner team reviews behavior + content. ds reviews tokens.            │
│    QA captures 11-frame minimum-run baseline.                           │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ 6. MERGE → STATUS                                                       │
│    Lands as preview (no FF) · beta (feature flag) · stable (full ship). │
│    CHANGELOG entry under [Unreleased]; CI updates component-map.json.   │
└─────────────────────────────────────────────────────────────────────────┘
```

Full review flow, owner-code definitions, and approval states are in [`docs/review-workflow.md`](./review-workflow.md).

## Things that block a merge

In rough order of how often they bite:

1. **No preview specimen.** Every new component needs `preview/<name>.html`. No specimen = no merge.
2. **Tokens missing from `tokens_used`** in the component-map entry. CI runs `pnpm lint:design-tokens` and fails if a component references a token that isn't in its declared list.
3. **A11y ship checklist not run.** The 14-item list in [qa-checklist.md § 5](./qa-checklist.md#5-accessibility-ship-checklist) is mandatory. Failing any item is a regression, not a nice-to-have.
4. **Not rendered under `data-theme="light"` and `data-theme="hc"`.** Both themes must visually parse. `terminal` is recommended but optional.
5. **No usage doc on a stable component.** Every component marked `status: stable` ships with a six-section usage doc per the [usage doc template](#usage-doc-template-six-section). Beta and preview components can skip it; stable cannot.
6. **Naming drift.** Component file names, token names, and CSS class names must match the rules in [`docs/naming-rules.md`](./naming-rules.md). PR title format too.
7. **`CHANGELOG.md` not updated.** Every merge gets an entry under `## [Unreleased]` in `docs/CHANGELOG.md` (per the spec's release model). Token renames go in `### Breaking`; additions in `### Added`; tweaks in `### Changed`.

## Usage doc template (six-section)

Every `stable` component ships with a usage doc following this exact structure:

1. **Header** — name, status, owner, since-version, one-line summary
2. **When to use** — situations where this is the right component, and a "don't use when" list
3. **Anatomy** — labeled diagram of the component with every slot/prop named
4. **Behavior** — interactions, state transitions, animations, keyboard bindings
5. **Content rules** — what text goes where, capitalization, max lengths, glossary terms
6. **Common mistakes** — three real-world wrong implementations and what to do instead

Canonical example: `preview/docs-usage-signal-card.html` in the v1.5.0 bundle. Match the structure verbatim — operators expect the same answers in the same order across every component.

## Where things live

| Artifact | Path |
|---|---|
| Canonical tokens (source of truth) | [`client/src/index.css`](../client/src/index.css) |
| Component map (production-grounded) | [`docs/component-map.md`](./component-map.md), [`docs/component-map.json`](./component-map.json) |
| QA checklist + matrix | [`docs/qa-checklist.md`](./qa-checklist.md), [`docs/qa-matrix.json`](./qa-matrix.json) |
| Naming rules | [`docs/naming-rules.md`](./naming-rules.md) |
| Review workflow + approval states | [`docs/review-workflow.md`](./review-workflow.md) |
| Visual regression skeleton | [`tests/visual.spec.ts.example`](../tests/visual.spec.ts.example) |
| Design skill (local) | [`13-skills/skills_src/coinscopeai-design/`](../../13-skills/skills_src/coinscopeai-design/) |
| Full v1.5.0 design bundle | `https://api.anthropic.com/v1/design/h/33zOUClByxZsD4r9RfjkfQ` |

## Quick links

- 35-component catalog with owners + status + dependencies → [`docs/component-map.md`](./component-map.md)
- Ship checklist (a11y, contrast, keyboard, focus) → [`docs/qa-checklist.md` § 5](./qa-checklist.md#5-accessibility-ship-checklist)
- The 11-frame minimum visual regression run → [`docs/qa-matrix.json` `_minimum_run`](./qa-matrix.json)
- Spec CHANGELOG / MIGRATION / DEPRECATIONS → fetch the v1.5.0 bundle URL above
