import { ENGINE_BASE_URL, REQUEST_TIMEOUT_MS } from "../constants.js";
import type { EngineResponse } from "../types.js";

export class EngineApiError extends Error {
  constructor(
    message: string,
    public readonly statusCode?: number,
    public readonly endpoint?: string
  ) {
    super(message);
    this.name = "EngineApiError";
  }
}

export async function engineFetch<T>(
  path: string,
  params?: Record<string, string | number>
): Promise<EngineResponse<T>> {
  const url = new URL(path, ENGINE_BASE_URL);
  if (params) {
    for (const [key, value] of Object.entries(params)) {
      url.searchParams.set(key, String(value));
    }
  }
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(url.toString(), {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      signal: controller.signal,
    });
    if (!response.ok) {
      throw new EngineApiError(
        `Engine returned HTTP ${response.status} for ${path}. Check VPS status — COI-68 may still be pending.`,
        response.status,
        path
      );
    }
    return (await response.json()) as EngineResponse<T>;
  } catch (err) {
    if (err instanceof EngineApiError) throw err;
    if (err instanceof Error && err.name === "AbortError") {
      throw new EngineApiError(
        `Engine request timed out after ${REQUEST_TIMEOUT_MS}ms. Is the VPS online? COI-68 restart may be required.`,
        undefined,
        path
      );
    }
    throw new EngineApiError(
      `Engine unreachable at ${ENGINE_BASE_URL}${path}: ${String(err)}. Run bash scripts/health_check.sh to diagnose.`,
      undefined,
      path
    );
  } finally {
    clearTimeout(timeout);
  }
}

export function formatEngineError(err: unknown): string {
  if (err instanceof EngineApiError) return `🔴 Engine Error: ${err.message}`;
  if (err instanceof Error) return `🔴 Unexpected error: ${err.message}`;
  return `🔴 Unknown error: ${String(err)}`;
}
