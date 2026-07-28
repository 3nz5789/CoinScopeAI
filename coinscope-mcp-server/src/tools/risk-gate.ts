import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { RiskGateInputSchema } from "../schemas/index.js";
import type { RiskGateStatus } from "../types.js";
import { RISK_THRESHOLDS } from "../constants.js";

export function registerRiskGateTool(server: McpServer): void {
  server.registerTool(
    "coinscope_risk_gate",
    {
      title: "Check Risk Gate Status",
      description: `Returns the current status of all CoinScopeAI risk management gates.

Canonical limits (locked PCC v2 §8, 2026-05-01):
  MAX_DRAWDOWN_PCT=10%, MAX_DAILY_LOSS_PCT=5%, MAX_OPEN_POSITIONS=5, MAX_LEVERAGE=10x, POSITION_HEAT_CAP_PCT=80%

Returns: daily_loss_limit_hit, drawdown_limit_hit, kill_switch_armed, open_positions, daily_loss_pct, current_drawdown_pct.
Use when: "is the gate open?", "can we trade?", "what's the gate status?"`,
      inputSchema: RiskGateInputSchema,
      annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false },
    },
    async () => {
      try {
        const result = await engineFetch<RiskGateStatus>("/risk-gate");
        const g = result.data;
        const gateOpen = !g.daily_loss_limit_hit && !g.drawdown_limit_hit && !g.kill_switch_armed;
        const status = gateOpen ? "🟢 GATE OPEN — trading permitted" : "🔴 GATE CLOSED — no new positions";
        const lines = [
          `🛡️  Risk Gate Status`,
          `────────────────────────`,
          status,
          ``,
          `Kill switch armed:     ${g.kill_switch_armed ? "YES ⚠️" : "No"}`,
          `Daily loss limit hit:  ${g.daily_loss_limit_hit ? "YES ⚠️" : "No"} (limit: ${RISK_THRESHOLDS.MAX_DAILY_LOSS_PCT}%)`,
          `Drawdown limit hit:    ${g.drawdown_limit_hit ? "YES ⚠️" : "No"} (limit: ${RISK_THRESHOLDS.MAX_DRAWDOWN_PCT}%)`,
        ];
        if (g.open_positions !== undefined) lines.push(`Open positions:        ${g.open_positions} / ${RISK_THRESHOLDS.MAX_OPEN_POSITIONS} max`);
        if (g.daily_loss_pct !== undefined) lines.push(`Current daily loss:    ${(g.daily_loss_pct * 100).toFixed(2)}%`);
        if (g.current_drawdown_pct !== undefined) lines.push(`Current drawdown:      ${g.current_drawdown_pct.toFixed(2)}%`);
        lines.push(``, `⚠️  All trading is Binance Testnet only (P0 phase).`);
        return { content: [{ type: "text", text: lines.join("\n") }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
