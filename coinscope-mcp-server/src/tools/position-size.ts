import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { PositionSizeInputSchema, type PositionSizeInput } from "../schemas/index.js";
import type { PositionSizeResult } from "../types.js";
import { RISK_THRESHOLDS } from "../constants.js";

export function registerPositionSizeTool(server: McpServer): void {
  server.registerTool(
    "coinscope_position_size",
    {
      title: "Calculate Position Size",
      description: `Calculates Kelly-fractional position size subject to canonical risk caps.

Hard caps: KELLY_HARD_CAP_PCT=2% equity per trade, MAX_LEVERAGE=10x, POSITION_HEAT_CAP_PCT=80%.
Run coinscope_risk_gate FIRST — this tool does not re-check the gate.

Args:
  - symbol (required): e.g. "BTCUSDT"
  - account_equity_usdt (optional): current equity for Kelly calculation

Returns: recommended_size_usdt, leverage, kelly_fraction, heat_cap_pct.
Use when: "how much should I trade on SOL?", "what size for this BTC signal?"`,
      inputSchema: PositionSizeInputSchema,
      annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: false, openWorldHint: false },
    },
    async (params: PositionSizeInput) => {
      try {
        const queryParams: Record<string, string | number> = { symbol: params.symbol };
        if (params.account_equity_usdt !== undefined) queryParams["equity"] = params.account_equity_usdt;
        const result = await engineFetch<PositionSizeResult>("/position-size", queryParams);
        const s = result.data;
        if (s.leverage > RISK_THRESHOLDS.MAX_LEVERAGE) {
          return {
            content: [{
              type: "text",
              text: `🔴 Guard violation: engine returned leverage=${s.leverage}x which exceeds canonical MAX_LEVERAGE=${RISK_THRESHOLDS.MAX_LEVERAGE}x. Do NOT use this size — report to operator as potential COI incident.`,
            }],
          };
        }
        const lines = [
          `📐 Position Size — ${s.symbol}`,
          `────────────────────────`,
          `Recommended size: ${s.recommended_size_usdt.toFixed(2)} USDT`,
          `Leverage:         ${s.leverage}x / ${RISK_THRESHOLDS.MAX_LEVERAGE}x max`,
        ];
        if (s.kelly_fraction !== undefined) lines.push(`Kelly fraction:   ${(s.kelly_fraction * 100).toFixed(2)}%`);
        if (s.heat_cap_pct !== undefined) {
          const heatFlag = s.heat_cap_pct >= RISK_THRESHOLDS.POSITION_HEAT_CAP_PCT * 0.9 ? " ⚠️ Near heat cap" : "";
          lines.push(`Heat cap usage:   ${s.heat_cap_pct.toFixed(1)}% / ${RISK_THRESHOLDS.POSITION_HEAT_CAP_PCT}%${heatFlag}`);
        }
        lines.push(``, `Hard caps: ≤${RISK_THRESHOLDS.KELLY_HARD_CAP_PCT}% equity per trade, ≤${RISK_THRESHOLDS.MAX_LEVERAGE}x leverage.`, `⚠️  Confirm risk gate is open before placing any order.`);
        return { content: [{ type: "text", text: lines.join("\n") }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
