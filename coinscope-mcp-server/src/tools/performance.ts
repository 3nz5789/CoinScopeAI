import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { PerformanceInputSchema } from "../schemas/index.js";
import type { PerformanceMetrics } from "../types.js";
import { RISK_THRESHOLDS } from "../constants.js";

export function registerPerformanceTool(server: McpServer): void {
  server.registerTool(
    "coinscope_performance",
    {
      title: "Get Performance Metrics",
      description: `Retrieves the CoinScopeAI engine's current P&L and performance summary.
Returns: total_trades, win_rate, profit_factor, current_drawdown, total_pnl_usdt, sharpe_ratio.
Use when: "how is the engine performing?", "what's the win rate?", "show PnL"`,
      inputSchema: PerformanceInputSchema,
      annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: true, openWorldHint: false },
    },
    async () => {
      try {
        const result = await engineFetch<PerformanceMetrics>("/performance");
        const d = result.data;
        const ddPct = (d.current_drawdown * 100).toFixed(2);
        const ddLimit = RISK_THRESHOLDS.MAX_DRAWDOWN_PCT;
        const ddFlag = d.current_drawdown * 100 >= ddLimit * 0.8 ? " ⚠️ Approaching limit" : "";
        const lines = [
          `📊 Performance Summary`,
          `────────────────────────`,
          `Total trades:     ${d.total_trades}`,
          `Win rate:         ${(d.win_rate * 100).toFixed(1)}%`,
          `Profit factor:    ${d.profit_factor.toFixed(2)}`,
          `Current drawdown: ${ddPct}% / ${ddLimit}% limit${ddFlag}`,
        ];
        if (d.total_pnl_usdt !== undefined) {
          lines.push(`Total PnL:        ${d.total_pnl_usdt >= 0 ? "+" : ""}${d.total_pnl_usdt.toFixed(2)} USDT`);
        }
        if (d.sharpe_ratio !== undefined) lines.push(`Sharpe ratio:     ${d.sharpe_ratio.toFixed(3)}`);
        lines.push(``, `⚠️  All trading is Binance Testnet only (P0 validation phase).`);
        return { content: [{ type: "text", text: lines.join("\n") }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
