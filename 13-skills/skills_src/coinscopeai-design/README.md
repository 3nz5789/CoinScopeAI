# CoinScopeAI Design — content + visual fundamentals

> Short reference card. The `SKILL.md` next door is the routing doc; this file is what you read **first**, before drawing or writing anything visual.

CoinScopeAI is a regime-aware, risk-first command console for USDT-perpetual crypto futures. Copy and visuals follow that — operator console, no marketing tone, no decorative ornament. Production dashboard runs at `app.coinscope.ai`; this design system underwrites it and every adjacent surface (Telegram alerts, marketing pages, the Figma library).

---

## Content fundamentals

**Voice.** Imperative, declarative, second person ("you"). Never "we". Never marketing-active. Banned: *powerful, seamless, AI-powered, intelligent, best-in-class, robust, just, moon, pump, hodl, guaranteed*. The engine and the panel address the operator; the operator addresses the market.

**Casing.**
- Page titles, card headings: **Title Case** — "Live Scanner", "Risk Gate", "Recording Daemon".
- Eyebrow labels, status pills, action levels, breaker states: **ALL CAPS** with wide letter-spacing, in JetBrains Mono — `LIVE`, `EXECUTE`, `HALT`, `PASS`, `FAIL`, `NOMINAL`, `WARNING`, `CRITICAL`, `ACTIVATED`, `DISARMED`.
- Symbols: uppercase, no separator — `BTCUSDT`, not `BTC-USDT` or `BTC/USDT`.
- Engine identifiers: `snake_case` — `circuit_breaker.state`, `signal.regime`.

**Tone — from the production source.**
> Engine is online and scanning — no candidate currently meets the active filters.

> Kill switch engaged. Do not execute. Disengage requires a written reason in the journal.

> Gate rejected: heat 78% > 80%. No action — wait for the next candidate.

Every line states **inputs and next move**. The console never decides for the operator and never softens a risk fact. No "may want to consider", no "looks like".

**Numbers are non-negotiable.** Always tabular, always with explicit units, always with the limit alongside the value when there is a budget: `2.4% / 5%`, `4.2x / 10x`, `64% / 80%`. Percentages: two decimals for prices, one for risk gauges. Dollars: `$1,840` (no decimals under $10K). Times: UTC, ISO-slice format `HH:MM:SS UTC`.

**Banned.** Emoji (see `SKILL.md` Emoji policy for the marketing-only shortlist). Exclamation marks. Em-dash filler. The word "just".

**Disclaimer.** Every public surface that references trading must carry:
> CoinScopeAI is a risk management and signal intelligence tool. It does not provide investment advice, manage funds, or place trades autonomously.

Legal: `app.coinscope.ai/legal`.

**Glossary.** Twenty terms ship verbatim in engine + UI: *Confluence, Gate, Regime, Kelly, Heat, Drawdown, Breaker, Kill Switch, EXECUTE, CONSIDER, WATCH, SKIP, HALT, LONG, SHORT, NOMINAL, WARNING, CRITICAL, ARMED, DISARMED.* Match them exactly — `preview/docs-content-style.html` has the full list and rules.

---

## Visual foundations

### Palette

Built on a **dark navy HUD** — `oklch(0.145 0.028 264.05)` page bg. Four surface lightness steps:

| Token | Value | Used for |
|---|---|---|
| `--navy-deep` | `oklch(0.12 0.025 264.05)` | sidebar + status bar — deepest |
| `--bg` | `oklch(0.145 0.028 264.05)` | page background |
| `--surface-1` | `oklch(0.185 0.02 264.05)` | card |
| `--surface-2` | `oklch(0.22 0.02 264.05)` | secondary / hover |
| `--surface-3` | `oklch(0.25 0.015 264.05)` | muted / input bg |

Brand color is **mint emerald** `#00FFB8` ≈ `oklch(0.696 0.17 162.48)`. One meaning — **alive and safe**: `LIVE` pulse, `PASS` gate, `EXECUTE` action, `LONG` direction, `NOMINAL` risk, active nav, primary button. Don't decorate with it.

Semantic colors are fixed to outcomes:
- **Crimson** `oklch(0.637 0.237 25.331)` — `FAIL` / `HALT` / `SHORT` / `CRITICAL` / kill switch `ARMED`. Used on `border-l-destructive` and chip backgrounds at 10% alpha.
- **Amber** `oklch(0.795 0.184 86.047)` ≈ `#F5A623` — `WARNING` / `CONSIDER` / `SKIP` / Volatile regime / breaker mid-state / leverage chip.
- **Blue (info)** `oklch(0.623 0.214 259.815)` — informational banners only. Never for state.

Regime palette is **separate from semantic** — taxonomic, not value-laden:

| Regime | Color token |
|---|---|
| Trending | `--regime-trending` (mint) |
| Volatile | `--regime-volatile` (amber) |
| Mean-Reverting | `--regime-mean-reverting` (slate) |
| Quiet | `--regime-quiet` (deep slate) |

### Type

Two families, no third.

| Use | Family | Where |
|---|---|---|
| UI chrome — titles, body, labels | **Inter** | All headings, sentence copy, sidebar items |
| Numbers, IDs, symbols, status pills | **JetBrains Mono** | Every price, % change, P&L, confluence score, timestamp, gate state, action chip |

The mono family is the signature — hitting it for any character that is data, even single-letter direction tags (`L` / `S`), is what makes the product read as institutional rather than retail. `font-variant-numeric: tabular-nums` is on every mono surface so columns align without explicit widths.

Scale: `10 · 11 · 13 · 15 · 17 · 20 · 28 · 40` px. The 28px hero is for KPI tiles, the 40px is for marketing. **Default body is 13px** in the design system (12 in `compact`, 14 in `cozy`). Production currently runs on Tailwind's default 16px body and uses `text-xs / text-sm` for data — that's a deliberate deviation; switching to 13px globally would cascade unpredictably.

### Spacing & rhythm

Base unit **4px**. Card padding 16px. Grid gap 12px. Page padding 20px. Inside a card, 12px between datum rows, 16px for the six-cell signal console grid. The 40px CSS grid background (`.hud-grid-bg`) is the only ambient texture, under `<main>` at 30% alpha on a soft border color, with a CRT-style 1.5% repeating-gradient scanline (`.scanline-overlay`) on top.

### Corner radii

Sharp on purpose:

| Token | Value | Used for |
|---|---|---|
| `--radius-sm` | `2px` | chips and status pills |
| `--radius` | `6px` | cards, inputs (default) |
| `--radius-md` | `8px` | larger panel (rare) |
| `--radius-pill` | `999px` | status dots only |

Anything `≥ 12px` reads as friendly-consumer and is wrong here. Don't import `rounded-2xl`.

### Borders & shadows

Every card is `1px solid --border` at rest with **no shadow**. The signature interaction is on hover: border lifts to `emerald @ 40%` and a soft `0 0 20px emerald/6%` glow appears for 200ms (`--shadow-hover`).

Action-level cards swap the **left border to 3px** in the action's color — `border-l-emerald` for `EXECUTE`, `border-l-destructive` for `HALT`. This is the only place left-border accents appear and they always carry information (no decorative bars).

### Backgrounds & textures

No imagery. No background gradients. Two textures only, both on the main viewport:
- **40px CSS grid** at 30% border opacity — `linear-gradient` overlay, never asset
- **CRT scanline** — `repeating-linear-gradient` at 1.5% emerald, 2px stripe / 2px gap

Both are pure CSS, both subtle enough that they read as "the screen is on" rather than as a pattern. The brand does not use photographs.

### Motion

| Action | Curve | Duration |
|---|---|---|
| Hover (border + shadow on card) | `cubic-bezier(.2,.6,.2,1)` (`--ease-out`) | 200ms |
| State swap (gauge fill, bar width) | linear / cubic | 500ms |
| Sidebar collapse / page change | ease-out | 200ms |
| `pulse-live` (LIVE dot, radar, kill switch) | ease-in-out, infinite | 2000ms |

No bounce. No spring. No scroll-driven animation. Trading product — motion is acknowledgement, not personality.

### States

| Element | Rest | Hover | Active / Selected | Focus |
|---|---|---|---|---|
| Card | `border: var(--border)`, no shadow | border emerald @40%, shadow emerald @6% | — | — |
| Sidebar item | text muted | text fg, bg `white/4%` | text emerald, bg `emerald/10%`, 3px left bar | 3px ring emerald @30% |
| Primary button | bg emerald, fg navy | opacity 90% | — | 3px ring emerald @30% |
| Ghost link | text emerald | text emerald @80% | — | — |
| Toggle off→on | bg surface-3 | — | bg emerald @25%, dot translated 16px | — |

There is **no `:hover` color change on data**. A row in a table gets a `bg: white/2%` highlight; the *value* never changes color on hover.

### Transparency & blur

Used sparingly. Chips: 10% color overlay + 20% border for the lit look without overpowering. **No `backdrop-filter: blur`** anywhere — the HUD reads as a flat industrial console, not glassmorphic. Modals: full-opacity `--surface-1` cards on top of an `rgba(0,0,0,0.6)` scrim — no blur.

### Fixed layout

Sidebar `220px` (collapsed `68px`), always pinned left. Status bar `40px`, always pinned top within the main column. Both render on `--navy-deep` so they read as chrome, not content. Page content scrolls under the fixed scanline overlay; the grid background scrolls with content.

### Card archetypes — pick from these

1. **Metric card** — eyebrow label + small icon, big mono number, small mono sub. KPI grids on Overview.
2. **HudCard** — title (caps + tracking) + optional subtitle + optional `link` right; bordered body.
3. **Action card** — same shell as HudCard with a `3px` colored left border, action chip top-right, six-datum grid inside. Only used for `SignalConsoleCard` / `SignalDecisionCard`.
4. **Gauge row** — eyebrow label + `NOMINAL/WARNING/CRITICAL` status pill on a single line, then a value/limit row, then a 5px progress track. Used inside `RiskWidget`.

Never invent a new card archetype. If a screen seems to need one, it's usually a sign the data is wrong.

---

## Iconography quick reference

Three sources, all `currentColor` so the cascade re-tints under theme swaps:

1. **UI icons** — `lucide-react@^0.453.0`. Outlined, 1.75 stroke, round caps and joins.
2. **Coin icons** — `assets/crypto-icons/svg/color/*.svg` (CC0, 483 glyphs from `spothq/cryptocurrency-icons`). Pair with `assets/crypto-icons/manifest.json`.
3. **Brand mark** — `CsMark` crosshair (`assets/icon-mark.svg`). Only custom icon. Don't redraw, recolor outside the canonical five (mint / black / white / grey / red), or rotate.

The trend arrows have standalone assets too — `assets/icon-trend-up.svg` / `icon-trend-down.svg` — the canonical replacements for 📈 📉 inside the product UI. (Emoji are banned in product UI; see SKILL.md Emoji policy.)

---

## Logo files — known caveats

The originally-uploaded `Full_Logo_Mint_Horizontal.svg` and `Wordmark_Mint*.svg` files shipped without inline style definitions (`cls-1/2/3` referenced but undefined) and used `<text>` elements with an unembedded font — both rendered blank.

The bundle ships **path-only rebuilt** SVGs at:
- `assets/logo-full-{mint,black,white,grey,red}.svg`
- `assets/logo-vert-{mint,black,white,grey,red}.svg`
- `assets/wordmark.svg` (+ `wordmark-{black,white,grey,red}.svg`)
- `assets/icon-mark.svg` + `assets/cs-sprite.svg`

Use the rebuilt files. The originals live in `uploads/` for archival reference only.

**Recolor pattern.** Path-only SVGs have a hardcoded `fill` on the root `<g>` so they render correctly via `<img src=…>`. To recolor via `currentColor`, **inline** the SVG (`<svg>…</svg>` directly in your markup) and set `fill="currentColor"` on the root; the rest of the geometry inherits.

---

## What's next door in this skill folder

- `SKILL.md` — routing doc · themes, density, layout, accessibility, content, release, Figma, component map, iconography, emoji policy
- `colors_and_type.css` — canonical token source of truth (v1.5.0)
- `assets/component-map.json` — 35-component lookup (spec format)
- `assets/emoji-vocab.json` — approved 15-glyph marketing/CT shortlist

Heavy stuff (fonts, full preview set, ui_kits/, 483 crypto-icon SVGs, brand asset uploads) is **not** mirrored locally. Fetch the full v1.5.0 bundle on demand:

```bash
curl -sSL -o /tmp/coinscopeai-design.tar.gz \
  'https://api.anthropic.com/v1/design/h/33zOUClByxZsD4r9RfjkfQ'
mkdir -p /tmp/coinscopeai-design && tar xzf /tmp/coinscopeai-design.tar.gz -C /tmp/coinscopeai-design
# Then: /tmp/coinscopeai-design/coinscopeai-design-system/project/
```
