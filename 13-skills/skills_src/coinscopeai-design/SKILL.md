---
name: coinscopeai-design
description: Use this skill to generate well-branded interfaces and assets for CoinScopeAI — the regime-aware crypto futures trading intelligence platform — for production or for throwaway prototypes/mocks. Contains the essential dark-HUD design rules, mint/amber/red palette, Inter + JetBrains Mono type pairing, brand assets, and a faithful recreation of the dashboard UI kit (sidebar, status bar, HudCard, SignalConsoleCard, RegimeCard, RiskWidget, gauges, tables).
user-invocable: true
---

# CoinScopeAI design skill

Read `README.md` in this skill folder before doing anything visual. It is short and covers:
- Content fundamentals (voice, casing, banned words, disclaimers)
- Visual foundations (palette, type pairing, spacing, motion, card archetypes, states)
- Iconography (Lucide React + the single custom crosshair mark)
- Logo files and known caveats (broken uploaded SVGs)

After the README, browse:
- `colors_and_type.css` — drop-in CSS variables for all tokens
- `preview/*.html` — small specimen cards you can use as visual references
- `assets/` — brand marks (logo, wordmark, icon-mark, icon-trend-up/down), `crypto-icons/svg/color/` (~480 CC0 coin glyphs from `spothq/cryptocurrency-icons`), `emoji-vocab.json` (the marketing/CT shortlist — do not import into product UI), and `figma-spec.json` (machine-readable component spec for the Figma library — variants, booleans, slots)
- `ui_kits/dashboard/` — running React (Babel) recreation of `app.coinscope.ai`. Start at `ui_kits/dashboard/README.md`, then `Chrome.jsx` for chrome and `HudComponents.jsx` for the three signature pieces (SignalConsoleCard, RegimeCard, RiskWidget).

## Theme variants

The default visual on `:root` is the dark HUD. Three opt-in themes are defined as `[data-theme="..."]` overrides at the bottom of `colors_and_type.css`; set the attribute on `<html>` for a full-page swap, or on any ancestor for scoped (the comparison specimen does the latter).

| `data-theme` | Use | Notes |
|---|---|---|
| _(none)_     | Default · operator app, command-center HUD | Mint emerald on navy. Canonical. |
| `light`      | Daylight reads, marketing pages, exported PDFs | Same brand colors darkened to clear 4.5:1 on white. Shadows become visible drops, not glows. |
| `hc`         | Accessibility mode · WCAG AAA-friendly | Pure black + white with 2px borders. Saturated state colors. No subtle tints. Replaces hover glow with a 2px outline. |
| `terminal`   | "Bloomberg mode" · power-user dense screens | Warm near-black bg, amber primary text, phosphor-green for up/long. Radii dropped to 0. Inter → JetBrains Mono everywhere. Stronger scanline. |

Specimen: `preview/theme-overview.html` (2×2 comparison of the same widget in all four).

Themes redeclare only the tokens that change; semantic aliases (`--success-*`, `--signal-*`, `--chart-*`, `--text-*`) follow automatically because they're declared *with `var()` indirection* on `:root`. Don't redeclare them in a theme — redeclare the underlying color and they'll re-resolve.

## Layout & grid

12-column CSS grid with `gap: var(--grid-gap)` (12px default). All dashboard surfaces are laid out on this grid; production uses Tailwind `col-span-*` utilities. Breakpoints are designed around laptop+ — there is no mobile dashboard.
- **Breakpoints** · `--bp-compact 1280` (min supported · 13" laptop), `--bp-standard 1440` (default design target), `--bp-wide 1920`, `--bp-ultra 2560`. Note these are documentation tokens — CSS `@media` can't read custom properties; hard-code the px in your media queries.
- **Containers** · `--container-content 720` (marketing copy), `--container-narrow 960` (docs), `--container-default 1280` (dashboard min), `--container-wide 1600`, `--container-ultra 1920`.
- **Panel spacing** · `--panel-pad-x 16` / `--panel-pad-y 14`, `--page-pad-x 20` / `--page-pad-y 18`, `--row-h 28`, `--row-h-head 32`. All scale with density.
- **Grid gap** · `--grid-gap-tight 6` (tables), `--grid-gap 12` (cards), `--grid-gap-loose 20` (marketing).

### Density modes

Opt in via `[data-density="compact|cozy"]` (default density needs no attribute). Affects type scale, panel padding, grid gap, and table row height — semantic everywhere; you don't change component code, just the attribute.

| `data-density` | Base font | Row height | Panel pad | Grid gap |
|---|---|---|---|---|
| `compact` | 12px | 22px | 10/8 | 8px |
| _(none)_  | 13px | 28px | 16/14 | 12px |
| `cozy`    | 14px | 36px | 20/18 | 16px |

Specimens: `preview/layout-grid.html`, `preview/layout-breakpoints.html`, `preview/layout-density.html`.

## Usage documentation

Every component in `assets/figma-spec.json` ships with a Usage doc using a fixed six-section template: header → when-to-use → anatomy → behavior → content rules → common mistakes. Authoring rules and the full checklist are in `preview/_usage-docs-readme.md`; the canonical example is `preview/docs-usage-signal-card.html` (SignalCard). Match the template — operators expect the same answers in the same order across every component.

## Accessibility

CoinScopeAI is keyboard-first by design. The full a11y spec lives in `preview/docs-a11y.html` — contrast minimums (WCAG 2.2 AA dark/light, AAA `hc`), keyboard bindings (global / page / component scopes), focus order rules, screen-reader announcements (polite vs. assertive boundaries), and touch-target floors (44×44 primary, 32×32 auxiliary with hit-pad). End every shipping component by running the pre-ship checklist at the bottom of that doc.

## Content & style

Operator voice, no marketing. Full spec: `preview/docs-content-style.html` — voice, capitalization (Sentence case / UPPERCASE / snake_case / mono), canonical labels (one concept = one word), banned words (no "moon", "pump", "hodl", "guaranteed", no adverbs), icons+emoji (banned in product UI; 15-glyph shortlist for marketing only), alert tone (subject → state → number, never exclamation), and a 20-term trading glossary (Confluence, Gate, Regime, Kelly, Heat, …). Match the glossary verbatim — engine and UI ship the same terms.

## Release

Versioning follows SemVer; token renames are MAJOR, additions are MINOR, behavior tweaks that don't break consumers are PATCH. Full history in `docs/CHANGELOG.md`; deprecation schedule with target-removal versions in `docs/DEPRECATIONS.md`; per-version upgrade instructions and migration scripts in `docs/MIGRATION.md`. Visual changelog: `preview/docs-release.html`. **Current**: v1.5.0. Always link to a specific MIGRATION.md section when shipping a breaking change.

## Figma library

Code tokens are mirrored into the published Figma library as Variables — one collection per concern (color, semantic, typography, spacing, shape, effect, opacity, z-index, motion). Modes match the CSS themes (Default / Light / HC / Terminal) and density attribute (Default / Compact / Cozy). **`colors_and_type.css` is the source of truth**; Figma is downstream. Full mapping and sync workflow: `preview/docs-figma-vars.html`. Machine-readable manifest: `assets/figma-variables.json` (DTCG format, importable via Tokens Studio).

## Component map

Single lookup from design-system component name → production path → Storybook deep link → kit recreation → preview specimen → usage doc. 35 components covered (13 core + 11 trading + 4 risk + 2 messaging + 2 chrome + 3 pattern). Each row also lists owner team, since-version, tokens used, dependencies, consumers, and (for deprecated entries) `removed_in` + `replaces_with`. Manifest: `assets/component-map.json`. Visual: `preview/docs-component-map.html`. CI consumes this to verify every claimed file resolves; the Figma plugin uses it for one-click deep links to code, Storybook, and docs.

## Iconography

The system uses **three** icon sources. **Product UI is emoji-free**; a curated emoji shortlist is allowed in marketing / Crypto Twitter / community channels only (see Emoji policy below).

1. **UI icons** — Feather/Lucide outline style, 24×24 viewBox, stroke 1.75, `currentColor`. Use the facsimiles in `ui_kits/dashboard/Icons.jsx` for mocks; production uses `lucide-react@^0.453`.
2. **Coin icons** — `assets/crypto-icons/svg/color/` (CC0). In React, render with `<CoinIcon symbol="BTCUSDT" size={18} />` from `Icons.jsx`; in plain HTML, `<img src="assets/crypto-icons/svg/color/btc.svg">`. Pair with `assets/crypto-icons/manifest.json` for symbol→name→brand-color lookup.
3. **Brand mark** — the crosshair `CsMark` (`assets/icon-mark.svg`), used at the head of the sidebar and as the favicon.

The two trend arrows live as standalone assets too — `assets/icon-trend-up.svg` / `assets/icon-trend-down.svg` — the canonical replacements for 📈 📉 inside the product.

## Emoji policy

Emoji are forbidden inside the product UI and allowed, with constraints, in outward-facing copy. The line is the application boundary, not the message tone.

**Product UI — never** · dashboards, modals, bot/system messages, tooltips, table cells, status pills, error states, in-app notifications, transactional emails. Use the SVG icons above. Replacing a glyph with emoji is a bug.

**Outward-facing — allowed** · Crypto Twitter, Discord/Telegram community channels, blog posts, landing/marketing pages, newsletter body copy, in-app chat *user reactions* (not bot output). Keep emoji to the approved shortlist; 0–1 per product-adjacent surface, 1–3 per CT post.

**Approved shortlist** (and only these):

| Slot | Glyph | Meaning |
|---|---|---|
| Signal up | 📈 | Bullish setup / upward momentum |
| Signal down | 📉 | Bearish setup / downward momentum |
| Target | 🎯 | Take-profit hit / precision entry |
| Caution | ⚠️ | Elevated risk |
| Critical | 🔴 | Invalidation / stop-loss hit |
| Live | 🟢 | Active / healthy connection |
| Pending | 🕒 | Waiting / cooldown / not triggered |
| Confirmed | ✅ | Executed / validated |
| Profit | 💰 | Realized profit |
| Volatile PnL | 💸 | Fast gains-or-losses (CT only) |
| Breakout | 🚀 | Strong upside (CT only) |
| Stretch | 🌙 | Optimistic stretch target (CT only) |
| Bull mood | 🐂 | Bullish sentiment label |
| Bear mood | 🐻 | Bearish sentiment label |
| Asset | 🪙 / ₿ | Generic token / Bitcoin |

**Rules**

- Always text-first; emoji follows the word, never replaces it. `"BTC setup confirmed ✅"`, not `"✅ BTC"`.
- One emoji per UI element (CT posts: max three). Never chain (`🚀🚀💰`).
- No emoji-only system messages — screen readers announce names and lose context.
- ₿ is a Unicode symbol, not an emoji — don't expect color rendering; pair with text.

Specimen: `preview/brand-emoji-policy.html` (policy chart) and `preview/brand-marketing-tone.html` (CT/social usage examples).
Machine-readable shortlist: `assets/emoji-vocab.json`.

## When the user asks for visual artifacts (slides, mocks, throwaway prototypes)

- Copy assets out of this folder; do not link cross-project.
- Write static HTML files using `colors_and_type.css` and the patterns in `preview/`.
- For dashboard-shaped surfaces, lift entire components from `ui_kits/dashboard/` rather than rebuilding them.
- Use JetBrains Mono for every number, symbol, status label, and timestamp. Use Inter for everything else.
- Sharp corners (`2px` / `6px`), dark navy bg, mint primary, no gradients. **Emoji rule: see "Emoji policy" above.** Banned in product UI; curated shortlist allowed in marketing/CT surfaces.

## When the user is building production code

- **In this repo**, the canonical tokens live at [`coinscopeai-dashboard/client/src/index.css`](../../../coinscopeai-dashboard/client/src/index.css) (the spec's `apps/dashboard/src/index.css` mirrored — the SKILL.md upstream uses the canonical-spec path). Production-grounded component-to-code map: [`coinscopeai-dashboard/docs/component-map.md`](../../../coinscopeai-dashboard/docs/component-map.md) + [`coinscopeai-dashboard/docs/component-map.json`](../../../coinscopeai-dashboard/docs/component-map.json).
- Use `lucide-react@^0.453.0` for icons, not the facsimiles in `ui_kits/dashboard/Icons.jsx`.
- Use Recharts for charts; the sparkline in the UI kit is a substitute.
- Components in `coinscopeai-dashboard/client/src/components/ui/` are shadcn primitives — use the originals.
- Theme + density runtime toggle: [`coinscopeai-dashboard/client/src/components/ThemeSwitcher.tsx`](../../../coinscopeai-dashboard/client/src/components/ThemeSwitcher.tsx) — writes `data-theme` / `data-density` on `<html>`, persists to localStorage.

## When the user invokes this skill with no other guidance

Ask what they want to build (a new dashboard view? a deck? a marketing one-pager? a mock of an engine feature?). Confirm:
1. Audience (operator, investor, internal eng?)
2. Whether they want one variation or several
3. Whether to honor the production tone strictly or relax it (e.g. marketing decks can use bigger fonts, the wordmark hero, and the approved emoji shortlist per the Emoji policy; product mocks must stay emoji-free)

Then act as an expert designer who outputs HTML artifacts (preferred for review) **or** TypeScript/React production code (if the user is editing the engine). Default to HTML artifacts using the patterns in `preview/` and `ui_kits/dashboard/` unless told otherwise.

---

## Local skill — heavy bundle is remote

This skill folder is intentionally lightweight. Anything heavy (font TTFs, 483 crypto-icon SVGs, full preview HTML set, ui_kits/dashboard React kit, `uploads/` originals) is **not** mirrored locally — fetch the full v1.5.0 bundle on demand:

```bash
# 37 MB gzipped → 74 MB extracted, 843 entries
curl -sSL -o /tmp/coinscopeai-design.tar.gz \
  'https://api.anthropic.com/v1/design/h/33zOUClByxZsD4r9RfjkfQ'
mkdir -p /tmp/coinscopeai-design && tar xzf /tmp/coinscopeai-design.tar.gz -C /tmp/coinscopeai-design
# Bundle root: /tmp/coinscopeai-design/coinscopeai-design-system/project/
```

What **is** in this skill folder:
- [`SKILL.md`](./SKILL.md) — this file
- [`README.md`](./README.md) — content fundamentals + visual foundations (the file the skill body tells the agent to read first)
- [`colors_and_type.css`](./colors_and_type.css) — canonical token source of truth, mirrors `coinscopeai-dashboard/client/src/index.css`
- [`assets/component-map.json`](./assets/component-map.json) — 35-component lookup (spec format)
- Everything else: link to the bundle path above.
