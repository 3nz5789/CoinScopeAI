import React, { createContext, useCallback, useContext, useEffect, useState } from "react";
import { getLoginUrl } from "../const";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

type AuthStatus = "loading" | "authenticated" | "unauthenticated";

interface AuthContextType {
  status: AuthStatus;
  logout: () => Promise<void>;
}

// ---------------------------------------------------------------------------
// Context
// ---------------------------------------------------------------------------

const AuthContext = createContext<AuthContextType | undefined>(undefined);

// ---------------------------------------------------------------------------
// Provider
// ---------------------------------------------------------------------------

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [status, setStatus] = useState<AuthStatus>("loading");

  // Check auth status on mount
  useEffect(() => {
    let cancelled = false;

    async function checkAuth() {
      try {
        const res = await fetch("/api/auth/status");
        if (cancelled) return;

        if (res.ok) {
          const data = (await res.json()) as { authenticated: boolean };
          setStatus(data.authenticated ? "authenticated" : "unauthenticated");
        } else {
          // Server unreachable or error — treat as unauthenticated
          setStatus("unauthenticated");
        }
      } catch {
        if (!cancelled) setStatus("unauthenticated");
      }
    }

    checkAuth();
    return () => { cancelled = true; };
  }, []);

  // Redirect to Manus OAuth portal when unauthenticated
  useEffect(() => {
    if (status === "unauthenticated") {
      // Only redirect if VITE_OAUTH_PORTAL_URL is configured
      const oauthPortalUrl = import.meta.env.VITE_OAUTH_PORTAL_URL;
      if (oauthPortalUrl) {
        window.location.href = getLoginUrl();
      }
      // If no portal configured (local dev), stay on page — server will allow through
    }
  }, [status]);

  const logout = useCallback(async () => {
    try {
      await fetch("/api/auth/logout", { method: "POST" });
    } finally {
      setStatus("unauthenticated");
    }
  }, []);

  return (
    <AuthContext.Provider value={{ status, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// ---------------------------------------------------------------------------
// Hook
// ---------------------------------------------------------------------------

export function useAuth(): AuthContextType {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}

// ---------------------------------------------------------------------------
// Gate component — renders children only when authenticated
// ---------------------------------------------------------------------------

export function AuthGate({ children }: { children: React.ReactNode }) {
  const { status } = useAuth();

  if (status === "loading") {
    return (
      <div className="flex h-screen w-full items-center justify-center bg-background">
        <div className="flex flex-col items-center gap-3 text-muted-foreground">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-current border-t-transparent" />
          <span className="text-sm">Authenticating…</span>
        </div>
      </div>
    );
  }

  // unauthenticated → redirect is already in flight (see useEffect above)
  if (status === "unauthenticated") {
    // Dev mode with no OAuth portal configured: render through so the
    // dashboard is usable locally. Production builds require the portal.
    if (import.meta.env.DEV && !import.meta.env.VITE_OAUTH_PORTAL_URL) {
      return <>{children}</>;
    }
    return (
      <div className="flex h-screen w-full items-center justify-center bg-background">
        <div className="flex flex-col items-center gap-3 text-muted-foreground">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-current border-t-transparent" />
          <span className="text-sm">Redirecting to login…</span>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
