# Component-to-code reference map

Lookup from design-system component name → production code path → kit recreation → preview specimen.

- **Spec source:** `project/assets/component-map.json` in the design-system bundle (v1.5.0, generated 2026-05-19) at `https://api.anthropic.com/v1/design/h/33zOUClByxZsD4r9RfjkfQ`.
- **Production root:** [client/src/](../client/src/) in this repo.
- **Storybook:** not yet wired in this repo; the spec's `storybook_path` values point at the design-system team's instance.
- **Status legend** (`stable / beta / preview / deprecated`): see [`docs/CHANGELOG.md`](https://api.anthropic.com/v1/design/h/33zOUClByxZsD4r9RfjkfQ) in the spec bundle.
- **Exists in this repo:** ✓ in production, △ inline (logic present but not extracted to its own file), ✗ not yet implemented.

---

## Core (13 components, shadcn primitives)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| Button | stable | ✓ [client/src/components/ui/button.tsx](../client/src/components/ui/button.tsx) | preview/components-buttons.html | |
| Input | stable | ✓ [client/src/components/ui/input.tsx](../client/src/components/ui/input.tsx) | preview/components-form.html | |
| Select | stable | ✓ [client/src/components/ui/select.tsx](../client/src/components/ui/select.tsx) | preview/components-menus.html | |
| Dropdown | stable | ✓ [client/src/components/ui/dropdown-menu.tsx](../client/src/components/ui/dropdown-menu.tsx) | preview/components-menus.html | |
| Tabs | stable | ✓ [client/src/components/ui/tabs.tsx](../client/src/components/ui/tabs.tsx) | preview/components-tabs.html | variants: underline · segmented · vertical |
| Modal | stable | ✓ [client/src/components/ui/dialog.tsx](../client/src/components/ui/dialog.tsx) | preview/components-modal.html | spec calls this `Dialog` |
| Drawer | stable | ✓ [client/src/components/ui/sheet.tsx](../client/src/components/ui/sheet.tsx) | preview/components-drawer.html | spec calls this `Sheet` |
| Tooltip | stable | ✓ [client/src/components/ui/tooltip.tsx](../client/src/components/ui/tooltip.tsx) | preview/components-tooltip.html | |
| Table | stable | ✓ [client/src/components/ui/table.tsx](../client/src/components/ui/table.tsx) | preview/data-sortable-table.html | |
| Card | stable | ✓ [client/src/components/ui/card.tsx](../client/src/components/ui/card.tsx) + `.hud-panel` helper | preview/components-hud-card.html | dashboard prefers `.hud-panel` class for the HUD archetype |
| Badge | stable | ✓ [client/src/components/ui/badge.tsx](../client/src/components/ui/badge.tsx) + `.cs-chip` / `.cs-pill` helpers | preview/components-badges.html | helpers in [client/src/index.css](../client/src/index.css) match the kit's chip / pill specs |
| Toast | stable | ✓ [client/src/components/ui/sonner.tsx](../client/src/components/ui/sonner.tsx) | preview/components-toast.html | uses `sonner` library |
| Pagination | stable | ✓ [client/src/components/ui/pagination.tsx](../client/src/components/ui/pagination.tsx) | preview/components-pagination.html | |

## Trading (11 components)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| SignalCard | stable | △ [client/src/components/SignalDecisionCard.tsx](../client/src/components/SignalDecisionCard.tsx) | preview/trading-signal-card.html | Production component is richer than spec — score arc, gate checks, price rail, expandable evidence. Treat as superset. |
| SignalConsoleCard | stable | △ inline in Scanner page via `SignalDecisionCard` | preview/components-hud-card.html | Production rolls the console card semantics into `SignalDecisionCard`. |
| PairChip | stable | ✗ not extracted | preview/trading-pair-pnl.html | Tokens used: `--surface-2`, `--border`, `--success-bg`. |
| CoinIcon | stable | ✗ not extracted | preview/brand-crypto-icons.html | Asset set: `project/assets/crypto-icons/svg/color/` (483 CC0 SVGs). Spec implementation: `<CoinIcon symbol="BTCUSDT" size={18} />`. |
| PnlCell | stable | ✗ not extracted (inline `.text-emerald` / `.text-crimson` per cell) | preview/trading-pair-pnl.html | variants: up · down · flat · hero |
| ConfluenceMeter | stable | △ inline SVG arc in `SignalDecisionCard.tsx` | preview/trading-confidence.html | variants: linear · dial · history. Production uses the `dial` variant only. |
| RegimeCard | stable | △ inline in [client/src/pages/RegimeDetection.tsx](../client/src/pages/RegimeDetection.tsx) | preview/colors-regime.html | 3px regime-color left border + chip in header + confidence bar — applied 2026-05-19. |
| RegimeTile | stable | ✗ not extracted | preview/pattern-market-overview.html | dense grid tile variant of RegimeCard. |
| StrategyCard | stable | ✗ not implemented | preview/trading-strategy-card.html | variants: active · paused · draft. Consumer would be a `/strategies` page (not present). |
| AlertItem | stable | ✗ not extracted | preview/trading-alert-center.html | variants: success · warning · danger · info · pending. Consumer: AlertCenter. |
| MetricCard | **deprecated** in spec (replaces_with: `KpiHero`, removed_in: 2.0.0) | ✓ [client/src/components/MetricCard.tsx](../client/src/components/MetricCard.tsx) — still in active use | — | Production still uses `MetricCard` widely (Overview, etc.). Migrating to a separate `KpiHero` is a v2.0 task per spec MIGRATION.md. |
| SignalRow | **deprecated** in spec (replaces_with: `SignalCard` density=compact, removed_in: 2.0.0) | ✗ not present in this repo | — | Already gone — production never had `SignalRow`. |

## Risk (4 components)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| RiskBanner | stable | ✗ not extracted (inline panels in Overview + RiskGate pages) | preview/trading-banners.html | variants: success · warning · danger. |
| LiquidationWarning | stable | ✗ not implemented | preview/trading-banners.html | tokens: `--danger`, `--danger-bg`, `--shadow-crit`. Consumer: PositionDetail + AlertCenter. |
| RiskWidget | stable | △ inline in [client/src/pages/Overview.tsx](../client/src/pages/Overview.tsx) (`RiskGauge` × 4 + kill switch row) | preview/components-gauges.html | Spec wants a top-level `<RiskWidget>` component; production composes it inline. Logic is identical. |
| RiskGauge | stable | △ inline in [client/src/pages/Overview.tsx](../client/src/pages/Overview.tsx) + [client/src/pages/RiskGate.tsx](../client/src/pages/RiskGate.tsx) | preview/components-gauges.html | Inline `RiskGauge` function — could be extracted to `client/src/components/RiskGauge.tsx`. |

## Chrome (2 components)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| Sidebar | stable | ✓ [client/src/components/Sidebar.tsx](../client/src/components/Sidebar.tsx) | preview/components-sidebar.html | Production has 4 nav sections (CORE / ANALYTICS / TOOLS / SYSTEM) and 17 items vs the kit's flat 10-item nav. |
| StatusBar | stable | ✓ [client/src/components/TopBar.tsx](../client/src/components/TopBar.tsx) | — | Spec calls it `StatusBar` (LIVE/UTC/Return/Risk). Production calls it `TopBar` and shows a live price ticker — production-superior. |

## Viz (1 component)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| Sparkline | stable | △ inline `<AreaChart>` from Recharts in Overview | preview/data-chart-overlays.html | Spec implementation is hand-drawn SVG; production uses Recharts. Equivalent at the API level. |

## Pattern (2 components)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| KpiStrip | stable | △ inline in [client/src/pages/Overview.tsx](../client/src/pages/Overview.tsx) (4-column `MetricCard` row) | preview/pattern-kpi-strip.html | variants: classic · sparked · gauged. Production currently uses the `classic` shape. |
| MarketOverview | stable | ✗ not implemented as a single pattern | preview/pattern-market-overview.html | Would compose `RegimeTile` × N. Could fit on Overview as a bottom-row replacement. |

## Messaging (2 components)

| Component | Status | Production path | Preview specimen | Notes |
|---|---|---|---|---|
| AiExplain | beta | ✗ not implemented | preview/msg-ai-explain.html | Feature flag: `ai_explain.v2`. Tokens: `--info-bg`, `--info-border`, `--info`. |
| AiChat | preview | ✗ not implemented (spec says deferred to v1.7) | preview/msg-ai-chat.html | Specimen only — no production target until the v1.7 release. |

---

## Coverage summary

| Category | In spec | ✓ production | △ inline | ✗ missing |
|---|---:|---:|---:|---:|
| Core | 13 | 13 | 0 | 0 |
| Trading | 11 (+2 deprecated) | 1 (`MetricCard`) | 4 (`SignalCard`, `SignalConsoleCard`, `ConfluenceMeter`, `RegimeCard`) | 6 |
| Risk | 4 | 0 | 2 (`RiskWidget`, `RiskGauge`) | 2 |
| Chrome | 2 | 2 | 0 | 0 |
| Viz | 1 | 0 | 1 (`Sparkline`) | 0 |
| Pattern | 2 | 0 | 1 (`KpiStrip`) | 1 |
| Messaging | 2 | 0 | 0 | 2 |
| **Total** | **35** | **16** | **8** | **11** |

**Gap to close before "1.5.0 ready" status:**
1. Extract inline `RiskWidget` + `RiskGauge` to their own components (used in both Overview + RiskGate).
2. Extract inline `Sparkline` wrapper around Recharts (used in Overview + Performance + EquityCurve).
3. Add `CoinIcon` component using the bundle's `assets/crypto-icons/svg/color/*` set (483 SVGs, CC0). Replaces emoji-style coin glyphs.
4. Add `PairChip`, `PnlCell` — simple but used everywhere; extracting reduces inline JSX.
5. Add `RiskBanner`, `LiquidationWarning` — risk-team owned components; production currently inlines these patterns.

Items that are intentionally out of scope for this repo:
- `KpiStrip` (composite — already used as inline 4-col grid)
- `StrategyCard` (no `/strategies` page yet)
- `AlertItem` (no AlertCenter yet)
- `MarketOverview`, `RegimeTile` (would replace bottom rows of Overview — optional)
- `AiExplain` (beta, behind flag)
- `AiChat` (preview only, deferred to v1.7)

## Token reference

Every component's `tokens_used` list points at variables defined in [client/src/index.css](../client/src/index.css) — the dashboard's port of the canonical `colors_and_type.css` (v1.5.0). All theme variants (`light` / `hc` / `terminal`) and density modes (`compact` / `cozy`) re-skin these tokens automatically.

## Machine-readable manifest

See [`docs/component-map.json`](./component-map.json) — same data with production paths, ready for CI/lint scripts.
