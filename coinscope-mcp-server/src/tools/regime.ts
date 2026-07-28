import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { RegimeInputSchema, type RegimeInput } from "../schemas/index.js";
import type { RegimeResult } from "../types.js";

const REGIME_META: Record<RegimeResult["regime"], { emoji: string; description: string }> = {
  trending: { emoji: "📈", description: "Strong directional momentum — trend-following setups favored." },
  "mean-reverting": { emoji: "↔️", description: "Price oscillating around mean — mean-reversion entries viable." },
  volatile: { emoji: "⚡", description: "High volatility / erratic price action — tighter sizing, wider stops." },
  quiet: { emoji: "😴", description: "Low volatility / low volume — signals less reliable, reduce size." },
};

export function registerRegimeTool(server: McpServer): void {
  server.registerTool(
    "coinscope_regime",
    {
      title: "Detect Market Regime",
      description: `Returns the current market regime label and ML confidence for a given symbol.

v3 ML classifier labels: trending | mean-reverting | volatile | quiet.

Args:
  - symbol (required): e.g. "BTCUSDT"

Returns: regime, confidence (0.0–1.0), timestamp.
Use when: "what regime is BTC in?", "is ETH trending?", "check regime before sizing"`,
      inputSchema: RegimeInputSchema,
      annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: false, openWorldHint: true },
    },
    async (params: RegimeInput) => {
      try {
        const result = await engineFetch<RegimeResult>(`/regime/${params.symbol}`);
        const r = result.data;
        const meta = REGIME_META[r.regime] ?? { emoji: "❓", description: "Unknown regime." };
        const conf = (r.confidence * 100).toFixed(1);
        const confFlag = r.confidence < 0.6 ? " ⚠️ Low confidence — treat as uncertain" : r.confidence >= 0.85 ? " ✅ High confidence" : "";
        const lines = [
          `${meta.emoji} Regime Detection — ${r.symbol}`,
          `────────────────────────`,
          `Regime:     ${r.regime.toUpperCase()}`,
          `Confidence: ${conf}%${confFlag}`,
          ``,
          meta.description,
        ];
        if (r.timestamp) lines.push(``, `Detected at: ${r.timestamp}`);
        return { content: [{ type: "text", text: lines.join("\n") }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
