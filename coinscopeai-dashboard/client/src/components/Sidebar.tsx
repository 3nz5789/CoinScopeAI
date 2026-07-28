import { useAppStore } from '@/lib/store';
import { cn } from '@/lib/utils';
import {
  Activity,
  BarChart3,
  Bell,
  BookOpen,
  Calculator,
  ChevronLeft,
  ChevronRight,
  ClipboardList,
  CreditCard,
  Database,
  LayoutDashboard,
  LineChart,
  Radio,
  Scan,
  Server,
  Settings,
  Shield,
  TrendingUp,
  Zap,
} from 'lucide-react';
import { useLocation } from 'wouter';

/* The brand mark — crosshair target ring, single color, path-only.
   Lifted from the design-system bundle (project/ui_kits/dashboard/Icons.jsx
   `CsMark`). Inlined to keep the chrome self-contained. */
function CsMark({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 118 118"
      fill="currentColor"
      aria-hidden="true"
      className={className}
    >
      <path d="M63.1,29.59c.26.04.53.07.79.12,12.12,2.04,21.74,11.46,24.03,23.47.09.45.16.9.23,1.36h29.64C115.72,25.34,92.35,2.02,63.1,0v29.59Z" />
      <path d="M54.69,87.88c-.44-.06-.87-.13-1.3-.22-11.89-2.28-21.25-11.69-23.43-23.6-.32-1.72-.48-3.5-.48-5.32s.16-3.6.48-5.32c2.16-11.85,11.42-21.21,23.22-23.56.5-.1,1-.18,1.51-.25V.01C24.12,2.2,0,27.66,0,58.75s24.12,56.55,54.69,58.74v-29.6Z" />
      <path d="M87.92,64.31c-2.27,11.88-11.7,21.23-23.62,23.4-.4.07-.79.14-1.2.19v29.59c29.25-2.02,52.62-25.34,54.69-54.54h-29.64c-.06.45-.14.91-.23,1.36Z" />
      <path d="M54.5,36.77c-8.77,1.75-15.61,8.86-16.94,17.77h8.64c1.28-3.95,4.37-7.07,8.3-8.4v-9.37Z" />
      <path d="M62.91,36.77v9.37c3.93,1.33,7.02,4.45,8.3,8.4h8.64c-1.34-8.91-8.17-16.02-16.94-17.77Z" />
      <path d="M62.91,80.72c8.77-1.75,15.61-8.86,16.94-17.77h-8.64c-1.28,3.95-4.37,7.07-8.3,8.4v9.37Z" />
      <path d="M54.5,80.72v-9.37c-3.93-1.33-7.02-4.45-8.3-8.4h-8.64c1.34,8.91,8.17,16.02,16.94,17.77Z" />
      <circle cx="58.89" cy="59.34" r="7.64" />
    </svg>
  );
}

const NAV_SECTIONS = [
  {
    label: 'CORE',
    items: [
      { path: '/', label: 'Overview', icon: LayoutDashboard },
      { path: '/scanner', label: 'Live Scanner', icon: Scan },
      { path: '/positions', label: 'Positions', icon: Activity },
      { path: '/journal', label: 'Trade Journal', icon: BookOpen },
    ],
  },
  {
    label: 'ANALYTICS',
    items: [
      { path: '/performance', label: 'Performance', icon: BarChart3 },
      { path: '/equity', label: 'Equity Curve', icon: LineChart },
      { path: '/risk-gate', label: 'Risk Gate', icon: Shield },
      { path: '/regime', label: 'Regime Detection', icon: Radio },
    ],
  },
  {
    label: 'TOOLS',
    items: [
      { path: '/position-sizer', label: 'Position Sizer', icon: Calculator },
      { path: '/alpha', label: 'Alpha Signals', icon: Zap },
      { path: '/market-data', label: 'Market Data', icon: Database },
      { path: '/backtest', label: 'Backtest Results', icon: TrendingUp },
    ],
  },
  {
    label: 'SYSTEM',
    items: [
      { path: '/settings', label: 'Settings', icon: Settings },
      { path: '/pricing', label: 'Pricing', icon: CreditCard },
      { path: '/system-status', label: 'System Status', icon: Server },
      { path: '/decisions', label: 'Decisions', icon: ClipboardList },
      { path: '/alerts', label: 'Alerts', icon: Bell },
    ],
  },
];

export default function Sidebar() {
  const [location, setLocation] = useLocation();
  const { sidebarCollapsed, toggleSidebar } = useAppStore();

  return (
    <aside
      className={cn(
        'fixed left-0 top-0 h-screen z-40 flex flex-col border-r border-sidebar-border bg-sidebar transition-all duration-200',
        sidebarCollapsed ? 'w-[64px]' : 'w-[220px]'
      )}
    >
      {/* Brand lockup — crosshair mark + typographic wordmark.
          Mint emerald icon + foreground text per kit canonical. */}
      <div className="flex items-center h-14 px-4 border-b border-sidebar-border shrink-0">
        <div className="flex items-center gap-2.5 overflow-hidden">
          <CsMark className="w-6 h-6 text-emerald shrink-0" />
          {!sidebarCollapsed && (
            <span className="text-[15px] font-semibold text-foreground tracking-tight whitespace-nowrap leading-none">
              COINSCOPE<span className="text-emerald">AI</span>
            </span>
          )}
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto py-3 px-2">
        {NAV_SECTIONS.map((section) => (
          <div key={section.label} className="mb-4">
            {!sidebarCollapsed && (
              <div className="px-2 mb-1.5 text-[10px] font-semibold tracking-[0.12em] text-muted-foreground/60 uppercase">
                {section.label}
              </div>
            )}
            <div className="space-y-0.5">
              {section.items.map((item) => {
                const isActive = location === item.path;
                const Icon = item.icon;
                return (
                  <button
                    key={item.path}
                    onClick={() => setLocation(item.path)}
                    className={cn(
                      'relative flex items-center gap-2.5 w-full rounded-md text-sm transition-colors duration-150',
                      sidebarCollapsed ? 'justify-center px-2 py-2' : 'px-2.5 py-1.5',
                      isActive
                        ? 'bg-emerald/10 text-emerald'
                        : 'text-muted-foreground hover:text-foreground hover:bg-secondary/60'
                    )}
                    title={sidebarCollapsed ? item.label : undefined}
                  >
                    {/* 3px emerald left bar — kit canonical active indicator */}
                    {isActive && (
                      <span
                        aria-hidden="true"
                        className="absolute left-0 top-1/2 -translate-y-1/2 w-[3px] h-5 bg-emerald rounded-r-full"
                      />
                    )}
                    <Icon className={cn('shrink-0', sidebarCollapsed ? 'w-5 h-5' : 'w-4 h-4')} />
                    {!sidebarCollapsed && (
                      <span className="truncate">{item.label}</span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        ))}
      </nav>

      {/* Collapse toggle */}
      <div className="border-t border-sidebar-border p-2 shrink-0">
        <button
          onClick={toggleSidebar}
          className="flex items-center justify-center w-full py-1.5 rounded-md text-muted-foreground hover:text-foreground hover:bg-secondary/60 transition-colors"
        >
          {sidebarCollapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
        </button>
      </div>
    </aside>
  );
}
