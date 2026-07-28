import express, { type Request, type Response, type NextFunction } from "express";
import { createServer } from "http";
import path from "path";
import { fileURLToPath } from "url";
import { COOKIE_NAME, ONE_YEAR_MS } from "../shared/const.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ---------------------------------------------------------------------------
// Config
// ---------------------------------------------------------------------------
const OAUTH_PORTAL_URL = process.env.VITE_OAUTH_PORTAL_URL ?? "";
const APP_ID = process.env.VITE_APP_ID ?? "";
const SESSION_SECRET = process.env.SESSION_SECRET ?? "";

if (!OAUTH_PORTAL_URL || !APP_ID) {
  console.warn(
    "[auth] VITE_OAUTH_PORTAL_URL or VITE_APP_ID not set — OAuth flow will be inactive."
  );
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/**
 * Exchange an OAuth code for a session token via the Manus OAuth portal.
 * The portal returns { sessionId, ... } on success or { error } on failure.
 */
async function exchangeCodeForSession(
  code: string,
  redirectUri: string
): Promise<string | null> {
  try {
    const res = await fetch(`${OAUTH_PORTAL_URL}/api/auth/exchange`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, redirectUri, appId: APP_ID }),
    });
    if (!res.ok) {
      console.error(`[auth] Token exchange failed: HTTP ${res.status}`);
      return null;
    }
    const data = (await res.json()) as { sessionId?: string; error?: string };
    if (data.error || !data.sessionId) {
      console.error("[auth] Token exchange error:", data.error ?? "no sessionId");
      return null;
    }
    return data.sessionId;
  } catch (err) {
    console.error("[auth] Token exchange exception:", err);
    return null;
  }
}

/**
 * Verify a session token against the Manus OAuth portal.
 * Returns true if the token is valid and belongs to this appId.
 */
async function verifySession(sessionId: string): Promise<boolean> {
  if (!OAUTH_PORTAL_URL || !APP_ID) return false;
  try {
    const res = await fetch(`${OAUTH_PORTAL_URL}/api/auth/verify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sessionId, appId: APP_ID }),
    });
    if (!res.ok) return false;
    const data = (await res.json()) as { valid?: boolean };
    return data.valid === true;
  } catch {
    return false;
  }
}

// ---------------------------------------------------------------------------
// Auth middleware
// ---------------------------------------------------------------------------

/**
 * Reads the session cookie and verifies it. Attaches `req.isAuthenticated`.
 * Does NOT redirect — callers decide what to do with unauthenticated requests.
 */
async function authMiddleware(
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> {
  // If OAuth is not configured, allow everything through (dev / local mode).
  if (!OAUTH_PORTAL_URL || !APP_ID) {
    (req as Request & { isAuthenticated: boolean }).isAuthenticated = true;
    return next();
  }

  const sessionId = parseCookies(req.headers.cookie ?? "")[COOKIE_NAME];
  if (!sessionId) {
    (req as Request & { isAuthenticated: boolean }).isAuthenticated = false;
    return next();
  }

  const valid = await verifySession(sessionId);
  (req as Request & { isAuthenticated: boolean }).isAuthenticated = valid;
  next();
}

/** Minimal cookie parser — avoids adding a dependency. */
function parseCookies(cookieHeader: string): Record<string, string> {
  return Object.fromEntries(
    cookieHeader
      .split(";")
      .map((c) => c.trim().split("="))
      .filter((parts) => parts.length === 2)
      .map(([k, v]) => [k.trim(), decodeURIComponent(v.trim())])
  );
}

// ---------------------------------------------------------------------------
// Server
// ---------------------------------------------------------------------------

async function startServer() {
  const app = express();
  const server = createServer(app);

  app.use(express.json());

  // ── OAuth callback ────────────────────────────────────────────────────────
  // plugin:engineering:github auth flow lands here after the Manus OAuth portal
  // redirects back with ?code=<code>&state=<base64(redirectUri)>
  app.get("/api/oauth/callback", async (req: Request, res: Response) => {
    const { code, state, error } = req.query as Record<string, string | undefined>;

    if (error) {
      console.error("[auth] OAuth error from portal:", error);
      return res.redirect("/?auth_error=" + encodeURIComponent(error));
    }

    if (!code || !state) {
      console.error("[auth] Missing code or state in callback");
      return res.redirect("/?auth_error=missing_params");
    }

    // Recover the redirect URI we encoded into `state`
    let redirectUri: string;
    try {
      redirectUri = Buffer.from(state, "base64").toString("utf-8");
    } catch {
      console.error("[auth] Failed to decode state param");
      return res.redirect("/?auth_error=invalid_state");
    }

    const sessionId = await exchangeCodeForSession(code, redirectUri);
    if (!sessionId) {
      return res.redirect("/?auth_error=exchange_failed");
    }

    // Set the session cookie — httpOnly, sameSite strict, secure in prod
    const isProduction = process.env.NODE_ENV === "production";
    const cookieOptions = [
      `${COOKIE_NAME}=${encodeURIComponent(sessionId)}`,
      `Max-Age=${Math.floor(ONE_YEAR_MS / 1000)}`,
      "Path=/",
      "HttpOnly",
      "SameSite=Strict",
      ...(isProduction ? ["Secure"] : []),
    ].join("; ");

    res.setHeader("Set-Cookie", cookieOptions);
    res.redirect("/");
  });

  // ── Auth status endpoint (used by client to gate rendering) ───────────────
  app.get("/api/auth/status", authMiddleware, (req: Request, res: Response) => {
    const authenticated = (req as Request & { isAuthenticated: boolean }).isAuthenticated;
    res.json({ authenticated });
  });

  // ── Logout ────────────────────────────────────────────────────────────────
  app.post("/api/auth/logout", (_req: Request, res: Response) => {
    res.setHeader(
      "Set-Cookie",
      `${COOKIE_NAME}=; Max-Age=0; Path=/; HttpOnly; SameSite=Strict`
    );
    res.json({ ok: true });
  });

  // ── Static files ──────────────────────────────────────────────────────────
  const staticPath =
    process.env.NODE_ENV === "production"
      ? path.resolve(__dirname, "public")
      : path.resolve(__dirname, "..", "dist", "public");

  app.use(express.static(staticPath));

  // Client-side routing — serve index.html for all unmatched routes
  app.get("*", (_req: Request, res: Response) => {
    res.sendFile(path.join(staticPath, "index.html"));
  });

  const port = process.env.PORT || 3000;
  server.listen(port, () => {
    console.log(`[coinscope-dashboard] Server running on http://localhost:${port}/`);
    console.log(
      `[auth] OAuth portal: ${OAUTH_PORTAL_URL || "NOT SET (dev mode — auth disabled)"}`
    );
  });
}

startServer().catch(console.error);
