# Visual QA · CoinScopeAI Dashboard

Run this before any merge that touches `client/src/index.css`, `client/src/components/`, a page in `client/src/pages/`, or the theme switcher.

- **Themes in scope:** `default` (dark HUD), `light`, `hc` (WCAG AAA), `terminal`
- **Density modes:** `default` (13px / 28px rows), `compact` (12 / 22), `cozy` (14 / 36)
- **Breakpoint floor:** 1280px (13" laptop). No mobile target.
- **Companion files:** [qa-matrix.json](./qa-matrix.json) (machine-readable combo matrix), [../tests/visual.spec.ts.example](../tests/visual.spec.ts.example) (Playwright skeleton).
- **A11y reference:** spec ships a full pre-ship checklist at `preview/docs-a11y.html` in the v1.5.0 bundle.

---

## 1. Pre-flight — does the foundation still work?

Run before opening any page.

| # | Check | How |
|---|---|---|
| 1 | Token sheet imports | `pnpm run build` succeeds with no new errors in `client/src/index.css` |
| 2 | All 24 canonical v1.5.0 tokens resolve | `getComputedStyle(document.documentElement).getPropertyValue('--success-bg')` returns a non-empty value for every token listed in the [Token sanity list](#token-sanity-list) below |
| 3 | Tailwind utility classes still work | `bg-emerald`, `text-crimson`, `bg-amber-warn`, `text-cyan-accent`, `rounded-md` all resolve to expected colors |
| 4 | TypeScript clean | `pnpm exec tsc --noEmit` returns zero new errors (pre-existing Performance.tsx error is the only known) |
| 5 | Dev server starts on `localhost:5174` | `pnpm dev` ready in < 2s, no module resolution errors |

### Token sanity list

If any of these come back empty after a CSS edit, the regression is in `index.css`:

```
Surface     : --navy-deep --bg --background --card --secondary --muted
Foreground  : --foreground --fg --fg-2 --fg-muted
Brand       : --emerald --primary --warning --danger --info
Semantic    : --success-bg --success-border --warning-bg --danger-bg --info-bg
Signal      : --signal-execute --signal-consider --signal-watch --signal-halt
Chart       : --chart-up --chart-down --chart-grid --chart-area-up
Regime      : --regime-trending --regime-volatile --regime-mean-reverting --regime-quiet
Scales      : --border-w-3 --o-40 --z-modal --duration --ease-in-out
Layout      : --row-h --row-h-head --grid-gap --panel-pad-x --container-default
Effect      : --shadow-hover --shadow-glow --shadow-crit --ring-focus
```

---

## 2. Visual regression — per-component checklist

Each row is verified once per theme (×4) — most regressions show up under `hc` or `terminal` because those re-skin the most.

### Chrome

| Component | Check | Pass when |
|---|---|---|
| **Sidebar** | Brand mark renders | `CsMark` SVG visible in emerald at 24×24, not blank or boxed |
| **Sidebar** | Wordmark | "COINSCOPE" reads in Inter (or JetBrains Mono under `terminal`); "AI" tinted emerald |
| **Sidebar** | Active nav item | 3px emerald left bar present, label color = `--emerald`, bg = `--emerald/10%` |
| **Sidebar** | Section labels | "CORE / ANALYTICS / TOOLS / SYSTEM" rendered uppercase with `tracking-[0.12em]` |
| **Sidebar** | Collapse toggle | Chevron animates 200ms; collapsed width = 64px, expanded = 220px |
| **TopBar** | Background | `var(--sidebar)` (= `--navy-deep` in default, matches sidebar) |
| **TopBar** | No `backdrop-filter` | Spec explicitly bans `backdrop-blur-*`; verify `getComputedStyle(header).backdropFilter === 'none'` |
| **TopBar** | Live ticker | Price rows render with mono price + emerald/crimson change pct; clock at right ticks each second |
| **TopBar** | Risk pill | GREEN/YELLOW/RED chip with pulsing dot at `--duration-pulse` (2000ms) |
| **TopBar** | Theme picker | 4 icon buttons; active one highlighted; tooltip visible on hover |
| **Layout** | Grid bg | `.hud-grid-bg` 40px linear-gradient visible at `--chart-grid` color |
| **Layout** | Scanline overlay | Position `fixed`, `pointer-events: none`, `z-index: 1` (= `--z-grid`) |
| **Layout** | Page padding | `p-5` (20px) — verify content not flush against sidebar |

### Card archetypes

| Component | Check | Pass when |
|---|---|---|
| **.hud-panel** | At rest | 1px `--border`, no shadow |
| **.hud-panel** | On hover | Border lifts to `--emerald @ 40%`, `--shadow-hover` (= `0 0 20px emerald/6%`) appears within 200ms |
| **.hud-panel** | Under `hc` | No glow on hover; border becomes 2px outline (`--border-w-1: 2px` override) |
| **.cs-card-head** | Layout | Title (12px caps, `--tracking-wide`) left, optional link right, 1px `--border-soft` bottom |
| **.al-execute / .al-halt / .al-skip / .al-watch / .al-consider** | Left border | 3px in the action's color; no other side has a thick border |
| **MetricCard** | KPI | Eyebrow label top-left, lucide icon top-right, big mono number, small sub line |
| **MetricCard** | Trend tint | `trend="up"` → sub line in `--success`; `trend="down"` → `--danger` |
| **SignalDecisionCard** | Score arc | 56×56 SVG arc, dasharray reflects score/100, color step at 50/65/80 |
| **SignalDecisionCard** | Gate chips | `4H MTF / Regime / No Anomaly / Setup Valid` — each ✓ / ⚠ / ✗ icon matches state |
| **SignalDecisionCard** | Price rail | STOP (crimson) / ENTRY / TP1 (emerald/70) / TP2 (emerald) — entry centered between |
| **RegimeCard** | Border-left color | Trending→emerald, Mean-Reverting→cyan-accent, Volatile→amber-warn, Quiet→muted |
| **RegimeCard** | Confidence bar | Width = confidence %, color = regime color |
| **RiskGauge** | Color step | < 50% → emerald, 50-80% → amber-warn, ≥ 80% → crimson |
| **RiskGauge** | Value display | `{value}{unit} / {limit}{unit}` mono tabular, no truncation |

### Chips / pills / status

| Component | Check | Pass when |
|---|---|---|
| **.cs-chip** | Square chip | 2px radius, 11px mono tabular, color matches `cs-chip-{em/dn/wn/cy/mu}` variant |
| **.cs-pill** | Status pill | 999px radius, optional `.dot` element pulses if `animate-pulse-dot` applied |
| **.cs-pill-em** (LIVE) | Animation | `pulse-dot` animation runs at 2s ease-in-out infinite, fades opacity 1 → 0.55 → 1 |
| **StatusBadge** | Color × variant | Each of green/yellow/red/cyan/muted/black resolves to the expected token |
| **Direction chip** | LONG vs SHORT | LONG = `cs-chip-em`, SHORT = `cs-chip-dn`; both readable under all 4 themes |

### Data display

| Component | Check | Pass when |
|---|---|---|
| **Tables** | Header row | `--row-h-head` (32px default / 26 compact / 40 cozy) |
| **Tables** | Body rows | `--row-h` (28 / 22 / 36) |
| **Tables** | Hover state | `bg: white/2%` (not the cell color changing) |
| **Tables** | Column alignment | Numbers right-aligned + tabular-nums; symbols left-aligned; status center |
| **Recharts area** | Gradient stops | Top stop = `--chart-area-up` (or `-dn`), bottom stop transparent |
| **Recharts grid** | Color | `--chart-grid` (slate at 30% alpha default; lighter under light theme) |
| **Recharts tooltip** | Surface | Background = `--surface-1`, border = `--border`, radius 6px |

---

## 3. Responsive test states

The spec's documented breakpoints. Capture each page at every relevant width.

| Breakpoint token | px | Use | Capture |
|---|---|---|---|
| `--bp-compact` | 1280 | 13" laptop · min supported | ✓ required |
| `--bp-standard` | 1440 | Default design target | ✓ required |
| `--bp-wide` | 1920 | Desktop monitor | ✓ required |
| `--bp-ultra` | 2560 | 4K / multi-monitor | △ spot check |

**No mobile** — confirmed in the spec ("there is no mobile dashboard"). Don't test < 1280; the Sidebar's 220px + nav text doesn't collapse below that.

**Per-page coverage:**

| Page | 1280 | 1440 | 1920 | 2560 | What to look for |
|---|---|---|---|---|---|
| `/` Overview | ✓ | ✓ | ✓ | △ | 4 KPIs single row (not wrapping); Equity+Risk side-by-side; 3-col bottom row |
| `/scanner` | ✓ | ✓ | ✓ | △ | SignalDecisionCard grid: 1 col @ 1280, 2 col @ 1440+; filter bar doesn't wrap awkwardly |
| `/risk-gate` | ✓ | ✓ | ✓ | △ | Kill-switch row prominent; per-symbol health table scrolls horizontally if needed (not page) |
| `/regime` | ✓ | ✓ | ✓ | △ | 5 regime cards in a row at ≥ 1440; 2 cols at 1280; bar chart fills width |
| `/positions` | ✓ | ✓ | ✓ | △ | Position rows render without column truncation |
| `/journal` | ✓ | ✓ | ✓ | △ | Trade rows; date filter aligned |
| `/equity` | ✓ | ✓ | ✓ | △ | Recharts AreaChart fills container; axis labels not clipped |
| `/performance` | ✓ | ✓ | ✓ | △ | KPI strip + chart layout intact |
| `/alpha`, `/market-data`, `/backtest`, `/settings`, `/pricing`, `/system-status`, `/decisions`, `/alerts` | ✓ | △ | △ | △ | Inherit chrome correctly; no horizontal scroll on page |

---

## 4. Dark-mode review frames

The 4-theme matrix. Each row is one comparison frame to capture and review.

| Theme | Default density | Compact | Cozy | Pages of interest |
|---|---|---|---|---|
| `default` (dark HUD) | ✓ baseline | △ | △ | All pages |
| `light` | ✓ | △ | — | Overview + Settings + Pricing (these are most likely to be shown to non-operators) |
| `hc` | ✓ a11y baseline | — | — | Scanner + RiskGate (a11y-critical interactive surfaces) |
| `terminal` | ✓ | ✓ best fit | — | Scanner + MarketData (dense data screens — terminal is built for these) |

### Per-theme regressions to watch for

**Default (dark HUD):**
- Card hover glow visible and ≤ 200ms
- 3px emerald left bar on active sidebar item
- Equity area chart emerald gradient fades to transparent

**Light:**
- Page bg fully `--bg` (near-white), not muddy
- Brand emerald darkened — text on emerald should still pass 4.5:1 (spec rebalances this; verify)
- Card shadow becomes visible drop, not glow (`--shadow-hover` redefined)
- Theme picker icons stay legible in TopBar

**HC (high contrast):**
- Pure black bg, pure white text
- Borders are 2px (`--border-w-1: 2px` override) everywhere — should look heavier
- Hover glow disabled (`--shadow-hover: none`)
- Focus ring `--ring-focus` = 3px solid emerald, never alpha
- Every interactive element reachable via `Tab` in source order
- Color is never the only signal — every chromatic state has a redundant label

**Terminal:**
- Background switches to warm-near-black, not navy
- Text rendered in JetBrains Mono everywhere (`--font-sans` aliased to mono)
- All radii → 0 (cards, chips, buttons — sharp corners)
- Phosphor green replaces mint (`--emerald` redefined)
- Scanline overlay is stronger (4% amber phosphor vs 1.2% in default)
- Grid bg uses amber tint

### Capture protocol

For each frame:
1. Open the target page at 1440×900
2. Apply theme: `document.documentElement.setAttribute('data-theme', '<theme>')` (or click the TopBar picker)
3. Apply density: `document.documentElement.setAttribute('data-density', '<density>')` (or click Settings picker)
4. Wait 300ms for transitions to finish
5. Screenshot full viewport
6. File name: `qa-<page>-<theme>-<density>-1440.png`

---

## 5. Accessibility ship checklist

Lifted verbatim from `preview/docs-a11y.html` § 6 (v1.5.0). Required for any component or page edit; failing any item is a regression, not a nice-to-have.

- [ ] **Contrast** · all text ≥ 4.5:1 (or 3:1 for large bold)
- [ ] **Color-blind** · every chromatic signal has a redundant text or shape
- [ ] **Keyboard reach** · every interactive element via `Tab` in source order
- [ ] **No keyboard traps** · except inside intentional modal/drawer overlays
- [ ] **Focus ring** · 3px `--ring-focus` visible on every focusable element
- [ ] **Restored focus** · closing a modal/drawer returns to the originator
- [ ] **Skip link** · "Skip to content" visible on first `Tab`
- [ ] **Touch targets** · primary controls ≥ 44×44 · auxiliary ≥ 32×32 with pad
- [ ] **Screen reader** · component name, role, value, and state announced
- [ ] **Live regions** · used only for state changes, never tick drift
- [ ] **SVG charts** · marked `aria-hidden` + summary `aria-label` on wrapper
- [ ] **Forms** · every `<input>` has a programmatic `<label>`; errors linked via `aria-describedby`
- [ ] **Hide** decorative icons with `aria-hidden="true"`
- [ ] **Themes** · render checked under `data-theme="light"` and `"hc"`

---

## 6. Common regressions — what to look for first

A short list of things that have already broken or are easy to break, ordered by how often they bite:

1. **Font fallback flash.** If `--font-sans` is set to `var(--font-mono)` under `terminal` but Inter is still loading, text renders in monospace then re-flows. Pre-load both variable fonts in `<head>`.
2. **`bg-navy-deep` Tailwind class doesn't exist if nothing references it.** Tailwind v4 JIT only generates utilities that appear in source. If you removed the only consumer, the class silently no-ops — use `bg-sidebar` (which maps to `--sidebar: var(--navy-deep)`) for chrome.
3. **Scanline z-index covers content.** `--z-grid: 1` is intentional — anything below sits behind. If a card becomes unclickable, check the scanline overlay isn't `pointer-events: auto`.
4. **3px left bar on sidebar item missing.** The `::before` pseudo-element needs `position: absolute` on the button. If a refactor changes the button to `position: static`, the bar disappears.
5. **`.hud-panel:hover` overrides explicit borders.** If a card has its own `border-left` (action level), the global hover rule on `border-color` will repaint all four sides — apply hover style only to `border-block` + `border-right` if needed, or use `transition: border-top-color, border-right-color, border-bottom-color` to leave the left alone.
6. **Recharts default colors leak.** If you forget to set `stroke` and `fill` on the `<Area>`, Recharts uses its purple default. Always pass `stroke="var(--chart-up)"` or `oklch(0.696 0.17 162.48)`.
7. **Body font-size drift.** Spec's `--fs-base: 13px` is opt-in via `[data-density]`. The dashboard runs on Tailwind's 16px default. Don't override `body { font-size: 13px }` globally — it cascades unpredictably across 19 pages.
8. **AuthGate dev bypass.** `import.meta.env.DEV && !VITE_OAUTH_PORTAL_URL` lets the dashboard render without auth in dev. Verify production builds are unaffected (`import.meta.env.DEV === false`).

---

## 7. Run-it-yourself snippet

Drop-in JavaScript for the browser console — exercises every theme + density combo in sequence so you can eyeball them all without re-clicking:

```js
(async () => {
  const themes = ['default', 'light', 'hc', 'terminal'];
  const densities = ['default', 'compact', 'cozy'];
  for (const t of themes) {
    for (const d of densities) {
      document.documentElement[t === 'default' ? 'removeAttribute' : 'setAttribute']('data-theme', t);
      document.documentElement[d === 'default' ? 'removeAttribute' : 'setAttribute']('data-density', d);
      console.log(`%c${t.padEnd(9)} · ${d}`, `background: ${getComputedStyle(document.documentElement).getPropertyValue('--bg')}; color: ${getComputedStyle(document.documentElement).getPropertyValue('--fg')}; padding: 6px 10px;`);
      await new Promise(r => setTimeout(r, 1200));
    }
  }
})();
```

For automated capture, see [`tests/visual.spec.ts.example`](../tests/visual.spec.ts.example) — a Playwright skeleton ready to copy into a real test file.
