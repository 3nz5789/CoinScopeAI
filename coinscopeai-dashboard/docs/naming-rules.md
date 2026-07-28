# Naming rules · CoinScopeAI design system

Single source of naming truth for components, tokens, classes, files, branches, and commits. CI enforces some of these (`pnpm lint:design-tokens`, `eslint-plugin-import`, `commitlint`); the rest are caught in PR review.

---

## Components

| Surface | Convention | Example |
|---|---|---|
| Component file name | `PascalCase.tsx` | `SignalDecisionCard.tsx`, `RiskGauge.tsx` |
| shadcn primitive file | `kebab-case.tsx` (matches shadcn upstream) | `dropdown-menu.tsx`, `alert-dialog.tsx` |
| Component default export | matches file name | `export default function SignalDecisionCard()` |
| Component named exports | `PascalCase` | `export function ThemeSwitcherCompact()` |
| Hook | `useThing` camelCase | `useThemeState`, `useLivePrices` |
| Type / interface | `PascalCase` | `interface SignalData`, `type Theme` |
| Prop interface | `<Component>Props` suffix | `interface MetricCardProps` |
| Variant union | `<Component>Variant` | `type ButtonVariant = 'primary' \| 'outline'` |

**One concept = one word.** "Direction" not "buyOrSell". "Confluence" not "score-strength-thing". The 20-term trading glossary (Confluence, Gate, Regime, Kelly, Heat, …) is in the spec's `preview/docs-content-style.html` — never substitute synonyms. Engine and UI ship the same terms verbatim.

**Don't suffix `Component`.** `SignalCard`, not `SignalCardComponent`. Files are React components by definition.

**Don't prefix `I` on interfaces.** TypeScript-flavored Hungarian notation is banned. `interface Position`, not `interface IPosition`.

## Tokens (CSS custom properties)

Two layers — palette and semantic. Never reference a palette value directly when a semantic alias exists.

| Token kind | Pattern | Examples |
|---|---|---|
| Palette (raw color) | `--<name>` | `--emerald`, `--crimson`, `--amber-warn` |
| Surface ladder | `--surface-<n>`, `--bg`, `--navy-deep`, `--fg`, `--fg-<n>` | `--surface-1`, `--fg-muted` |
| Semantic state | `--<state>-{bg,border,fg}` | `--success-bg`, `--danger-border` |
| Signal vocabulary | `--signal-<action>` | `--signal-execute`, `--signal-halt` |
| Chart aliases | `--chart-<role>` | `--chart-up`, `--chart-grid`, `--chart-area-up` |
| Regime taxonomy | `--regime-<state>` | `--regime-trending`, `--regime-volatile` |
| Spacing scale | `--space-<n>` (4px multiples) | `--space-4` = 16px |
| Type size scale | `--fs-<size>` | `--fs-base`, `--fs-xl`, `--fs-2xl` |
| Radii | `--radius`, `--radius-{sm,md,lg,pill}` | `--radius`, `--radius-pill` |
| Border width | `--border-w-<n>` | `--border-w-1`, `--border-w-3` |
| Opacity | `--o-<percent>` | `--o-10`, `--o-40` |
| Z-index | `--z-<role>` | `--z-sticky`, `--z-modal`, `--z-tooltip` |
| Motion | `--duration-<role>`, `--ease-<curve>` | `--duration-pulse`, `--ease-out` |
| Shadow | `--shadow-<role>` | `--shadow-hover`, `--shadow-crit` |
| Layout | `--grid-gap`, `--grid-gap-{tight,loose}`, `--panel-pad-{x,y}`, `--row-h`, `--row-h-head`, `--container-<size>` | `--container-default` |
| Tracking | `--tracking-<size>` | `--tracking-wide`, `--tracking-widest` |
| Tailwind utility binding | `--color-<name>` mirror | `--color-emerald`, `--color-crimson` |

**Rules:**

- Lowercase, hyphenated. Never camelCase, never SCREAMING-CASE.
- Semantic before palette. Write `var(--signal-execute)` in component CSS, not `var(--emerald)`. Theme variants re-route the semantic alias automatically; the palette literal won't.
- A theme variant (`[data-theme="light"]` etc.) **redeclares only what changes**. Don't redeclare semantic aliases — they cascade through `var()` indirection. Redeclare the palette token they point at.
- When adding a token: it goes in `client/src/index.css` `:root` (or the matching theme block), is mirrored into `@theme inline` as `--color-<name>` if it should generate Tailwind utilities, and is listed in the new component's `tokens_used` in `docs/component-map.json`.
- Renaming a token = MAJOR per SemVer. Adding one = MINOR. Tweaking a value = PATCH if it doesn't break consumers.

## CSS classes (custom helpers in `index.css`)

Custom helper classes use the `cs-` prefix to avoid colliding with Tailwind, shadcn, or Recharts.

| Pattern | Examples |
|---|---|
| `cs-<role>` for primitives | `cs-chip`, `cs-pill`, `cs-card-head`, `cs-focus` |
| `cs-<role>-<variant>` for variants | `cs-chip-em`, `cs-chip-dn`, `cs-chip-wn`, `cs-card-title` |
| `al-<action>` for action-level borders | `al-execute`, `al-halt`, `al-skip`, `al-watch`, `al-consider` |
| `hud-<role>` for HUD primitives | `hud-panel`, `hud-panel-glow`, `hud-grid-bg` |
| `animate-<thing>` for animations | `animate-pulse-dot` |

**Don't:**
- Add new top-level utility classes without a `cs-` / `hud-` / `al-` / `animate-` prefix
- Override Tailwind's class names (`text-emerald` etc. — they're generated from `@theme inline`)
- Style by element when a class would do (`button { … }` is banned in components; use shadcn's `button.tsx` variants)

## Files & directories

| What | Where |
|---|---|
| shadcn primitives | `client/src/components/ui/<kebab-case>.tsx` |
| Custom components | `client/src/components/<PascalCase>.tsx` |
| Pages | `client/src/pages/<PascalCase>.tsx` |
| Composite patterns (KPI strip, Market Overview, etc.) | `client/src/patterns/<PascalCase>.tsx` (create when first pattern lands) |
| Hooks | `client/src/lib/<thing>/hooks.ts` (or per-feature subdir) |
| Tests for component `Foo` | `client/src/components/Foo.test.tsx` (colocated) |
| Visual regression spec | `tests/visual.spec.ts` |
| Design-system docs | `docs/` (this folder) |

**One component per file.** If you find yourself wanting two PascalCase exports from the same file, they're probably the same component — combine — or they belong in separate files.

## Branches

| Branch type | Pattern | Example |
|---|---|---|
| Feature | `feature/ds-<short>` | `feature/ds-coin-icon` |
| Fix | `fix/ds-<short>` | `fix/ds-scanline-z-index` |
| Token change | `tokens/<short>` | `tokens/add-info-state` |
| Deprecation | `deprecate/<component>` | `deprecate/metric-card` |
| Refactor (no behavior change) | `refactor/ds-<short>` | `refactor/ds-extract-risk-gauge` |

Prefix design-system work with `ds-` to keep CI label routing clean.

## Commits

[Conventional Commits](https://www.conventionalcommits.org/), enforced by `commitlint` once wired:

```
<type>(<scope>): <imperative subject>

[body]

[footer]
```

| Type | When |
|---|---|
| `feat` | New component, new variant, new token |
| `fix` | Bug fix in existing component / token resolution / theme parity |
| `refactor` | No behavior change (extract `RiskGauge` from inline, etc.) |
| `style` | CSS-only change with no token rename |
| `docs` | docs/, README, CONTRIBUTING, comments |
| `test` | Visual regression specs, unit tests |
| `chore` | Build, deps, tooling |
| `breaking` | Token rename, removed export, signature change |

**Scopes** — one of `ds` (cross-cutting design-system), or a component name (`signal-card`, `risk-gauge`), or `tokens`, `theme`, `density`, `chrome`, `qa`.

```
feat(coin-icon): add CoinIcon component using crypto-icons set
fix(scanner): SignalDecisionCard score arc misaligned at 1280w
refactor(ds): extract RiskGauge from Overview + RiskGate inlines
breaking(tokens): rename --bg-tertiary to --surface-3
```

**Imperative subject**, no trailing period, ≤ 72 chars. The body wraps at 72.

## Pull request titles

PR title = the canonical commit message of the squash merge. Same Conventional Commits format.

```
feat(coin-icon): add CoinIcon component using crypto-icons set (#142)
```

## Storybook story names

Storybook isn't wired in this repo yet — but if/when it lands, story names follow the spec's `storybook_path` field in `docs/component-map.json`:

```
ui-button--primary       → core/Button stories, "Primary" variant
trading-signalcard--exec → trading/SignalCard stories, "Execute" variant
risk-widget--nominal     → risk/RiskWidget stories, "Nominal" variant
```

Hierarchy follows the component-map `category`. Variant follows the variant union in the component code.

## Things that must NOT happen

- Emoji in any component file, page file, or system message string. Period. The 15-glyph marketing shortlist is for blog/CT/community only — see [SKILL.md Emoji policy](../../13-skills/skills_src/coinscopeai-design/SKILL.md#emoji-policy).
- Hex color literals in components. If you find yourself typing `#00FFB8`, you wanted `var(--emerald)` or the `text-emerald` Tailwind class.
- `style={{ color: '...' }}` inline overrides for design-system colors. Tokens or utility classes only.
- `border-radius` literals. Use `--radius`, `--radius-sm`, `--radius-md`, `--radius-pill`, or `rounded-md` etc.
- New `dark:` Tailwind variants. The app is dark-by-default with opt-in themes via `[data-theme]`; don't fork a parallel mode system.
- `backdrop-filter: blur(...)`. The HUD is a flat industrial console, not glassmorphic. Spec ban, see SKILL.md.
