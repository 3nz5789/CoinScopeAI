/**
 * ThemeSwitcher — toggles `data-theme` and `data-density` on <html>.
 *
 * Theme variants (v1.5.0 design system):
 *   - default · dark navy HUD, mint emerald on navy (canonical)
 *   - light   · daylight, brand darkened to 4.5:1 on white
 *   - hc      · WCAG AAA · pure b&w with 2px borders
 *   - terminal · phosphor amber, zero radii, mono everywhere
 *
 * Density:
 *   - default · 13px base · 28px rows · 16/14 panel pad
 *   - compact · 12px base · 22px rows · 10/8  panel pad
 *   - cozy    · 14px base · 36px rows · 20/18 panel pad
 *
 * Persists both to localStorage. Re-applies on mount.
 */

import { cn } from '@/lib/utils';
import { Maximize2, Minimize2, Monitor, Moon, Sun, Terminal } from 'lucide-react';
import { useEffect, useState } from 'react';

export type Theme = 'default' | 'light' | 'hc' | 'terminal';
export type Density = 'default' | 'compact' | 'cozy';

const THEME_KEY = 'cs-theme';
const DENSITY_KEY = 'cs-density';

const THEME_META: Record<Theme, { label: string; subtitle: string; Icon: typeof Moon }> = {
  default:  { label: 'Dark HUD',  subtitle: 'Operator app · canonical', Icon: Moon },
  light:    { label: 'Light',     subtitle: 'Daylight · marketing',     Icon: Sun },
  hc:       { label: 'High Contrast', subtitle: 'WCAG AAA · b&w · 2px borders', Icon: Monitor },
  terminal: { label: 'Terminal',  subtitle: 'Phosphor amber · mono · radius 0', Icon: Terminal },
};

const DENSITY_META: Record<Density, { label: string; subtitle: string; Icon: typeof Maximize2 }> = {
  compact: { label: 'Compact', subtitle: '12px · 22px rows', Icon: Minimize2 },
  default: { label: 'Default', subtitle: '13px · 28px rows', Icon: Monitor },
  cozy:    { label: 'Cozy',    subtitle: '14px · 36px rows', Icon: Maximize2 },
};

function readTheme(): Theme {
  if (typeof window === 'undefined') return 'default';
  const v = localStorage.getItem(THEME_KEY) as Theme | null;
  return v && v in THEME_META ? v : 'default';
}

function readDensity(): Density {
  if (typeof window === 'undefined') return 'default';
  const v = localStorage.getItem(DENSITY_KEY) as Density | null;
  return v && v in DENSITY_META ? v : 'default';
}

function applyTheme(theme: Theme) {
  const root = document.documentElement;
  if (theme === 'default') root.removeAttribute('data-theme');
  else root.setAttribute('data-theme', theme);
}

function applyDensity(density: Density) {
  const root = document.documentElement;
  if (density === 'default') root.removeAttribute('data-density');
  else root.setAttribute('data-density', density);
}

/** Hook — keep <html> attributes in sync with localStorage on mount + writes. */
export function useThemeState() {
  const [theme, setTheme] = useState<Theme>('default');
  const [density, setDensity] = useState<Density>('default');

  // Bootstrap from localStorage exactly once
  useEffect(() => {
    const t = readTheme();
    const d = readDensity();
    setTheme(t);
    setDensity(d);
    applyTheme(t);
    applyDensity(d);
  }, []);

  function pickTheme(next: Theme) {
    setTheme(next);
    applyTheme(next);
    localStorage.setItem(THEME_KEY, next);
  }

  function pickDensity(next: Density) {
    setDensity(next);
    applyDensity(next);
    localStorage.setItem(DENSITY_KEY, next);
  }

  return { theme, density, pickTheme, pickDensity };
}

// ─── Full switcher card (Settings) ────────────────────────────────────────

export default function ThemeSwitcher() {
  const { theme, density, pickTheme, pickDensity } = useThemeState();

  return (
    <div className="hud-panel overflow-hidden">
      <div className="cs-card-head">
        <div className="flex items-baseline">
          <span className="cs-card-title">Appearance</span>
          <span className="cs-card-sub">v1.5.0 · per-device</span>
        </div>
      </div>

      <div className="p-5 space-y-5">
        {/* Theme grid */}
        <div>
          <label className="eyebrow block mb-2">Theme</label>
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
            {(Object.keys(THEME_META) as Theme[]).map((key) => {
              const meta = THEME_META[key];
              const Ico = meta.Icon;
              const active = theme === key;
              return (
                <button
                  key={key}
                  onClick={() => pickTheme(key)}
                  className={cn(
                    'flex flex-col items-start gap-1.5 p-3 rounded-md border text-left transition-colors cs-focus',
                    active
                      ? 'bg-emerald/10 border-emerald/40 text-emerald'
                      : 'bg-secondary/60 border-border text-muted-foreground hover:text-foreground hover:border-emerald/30',
                  )}
                  aria-pressed={active}
                  aria-label={`${meta.label} theme`}
                >
                  <div className="flex items-center gap-2">
                    <Ico className="w-4 h-4 shrink-0" />
                    <span className="text-sm font-semibold">{meta.label}</span>
                  </div>
                  <span className="text-[10px] text-muted-foreground leading-tight">
                    {meta.subtitle}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Density row */}
        <div>
          <label className="eyebrow block mb-2">Density</label>
          <div className="grid grid-cols-3 gap-2">
            {(Object.keys(DENSITY_META) as Density[]).map((key) => {
              const meta = DENSITY_META[key];
              const Ico = meta.Icon;
              const active = density === key;
              return (
                <button
                  key={key}
                  onClick={() => pickDensity(key)}
                  className={cn(
                    'flex flex-col items-start gap-1 p-3 rounded-md border text-left transition-colors cs-focus',
                    active
                      ? 'bg-emerald/10 border-emerald/40 text-emerald'
                      : 'bg-secondary/60 border-border text-muted-foreground hover:text-foreground hover:border-emerald/30',
                  )}
                  aria-pressed={active}
                  aria-label={`${meta.label} density`}
                >
                  <div className="flex items-center gap-2">
                    <Ico className="w-4 h-4 shrink-0" />
                    <span className="text-sm font-semibold">{meta.label}</span>
                  </div>
                  <span className="text-[10px] text-muted-foreground">
                    {meta.subtitle}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        <p className="text-[10px] text-muted-foreground leading-relaxed">
          Theme + density preferences persist to <code className="font-mono text-foreground">localStorage</code> on this device.
          Production app forces dark by default; switching here is opt-in per session and won't ship to your account.
        </p>
      </div>
    </div>
  );
}

// ─── Compact picker (TopBar) ──────────────────────────────────────────────

export function ThemeSwitcherCompact() {
  const { theme, pickTheme } = useThemeState();
  const keys: Theme[] = ['default', 'light', 'hc', 'terminal'];

  return (
    <div className="flex items-center gap-0.5 border border-border rounded-md overflow-hidden">
      {keys.map((key) => {
        const meta = THEME_META[key];
        const Ico = meta.Icon;
        const active = theme === key;
        return (
          <button
            key={key}
            onClick={() => pickTheme(key)}
            className={cn(
              'h-6 w-7 flex items-center justify-center text-muted-foreground transition-colors cs-focus',
              active && 'bg-emerald/15 text-emerald',
              !active && 'hover:text-foreground hover:bg-secondary/60',
            )}
            title={`${meta.label} · ${meta.subtitle}`}
            aria-label={`Switch to ${meta.label} theme`}
            aria-pressed={active}
          >
            <Ico className="w-3 h-3" />
          </button>
        );
      })}
    </div>
  );
}
