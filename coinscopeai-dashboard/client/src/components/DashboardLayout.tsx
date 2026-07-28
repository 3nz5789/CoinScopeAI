import { useAppStore } from '@/lib/store';
import { cn } from '@/lib/utils';
import Sidebar from './Sidebar';
import TopBar from './TopBar';

interface DashboardLayoutProps {
  children: React.ReactNode;
}

export default function DashboardLayout({ children }: DashboardLayoutProps) {
  const { sidebarCollapsed } = useAppStore();

  return (
    <div className="min-h-screen bg-background">
      <Sidebar />
      {/* Fixed CRT scanline overlay — sits above main content, ignores pointer events.
          Kit canonical "the screen is on" texture. */}
      <div className="scanline-overlay" aria-hidden="true" />
      <div
        className={cn(
          'transition-all duration-200',
          sidebarCollapsed ? 'ml-[64px]' : 'ml-[220px]'
        )}
      >
        <TopBar />
        <main className="hud-grid-bg p-5 min-h-[calc(100vh-2.5rem)]">
          {children}
        </main>
      </div>
    </div>
  );
}
