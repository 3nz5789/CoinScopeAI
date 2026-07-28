import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { JournalInputSchema, type JournalInput } from "../schemas/index.js";
import type { TradeRecord } from "../types.js";
import { CHARACTER_LIMIT } from "../constants.js";

function formatTrade(t: TradeRecord, idx: number): string {
  const pnl = t.pnl !== null ? `${t.pnl >= 0 ? "+" : ""}${t.pnl.toFixed(2)} USDT` : "open";
  const exit = t.exit_price !== null ? `→ ${t.exit_price}` : "→ (open)";
  const regime = t.regime ? ` [${t.regime}]` : "";
  const gate = t.gate_decision ? ` gate:${t.gate_decision}` : "";
  return `${idx + 1}. [${t.trade_id}] ${t.symbol} ${t.side}${regime} @ ${t.entry_price} ${exit} | PnL: ${pnl}${gate} | ${t.timestamp}`;
}

export function registerJournalTool(server: McpServer): void {
  server.registerTool(
    "coinscope_journal",
    {
      title: "Get Trade Journal",
      description: `Retrieves the append-only trade and gate-decision journal from the CoinScopeAI engine.

Args:
  - symbol (optional): Filter to one symbol e.g. "BTCUSDT"
  - limit (number): Max records 1–500 (default: 50)
  - side ('LONG' | 'SHORT' | 'ALL'): Filter by direction (default: ALL)

Use when: "show recent trades", "what trades did we take on BTC?", "audit the journal"`,
      inputSchema: JournalInputSchema,
      annotations: { readOnlyHint: true, destructiveHint: false, idempotentHint: false, openWorldHint: false },
    },
    async (params: JournalInput) => {
      try {
        const queryParams: Record<string, string | number> = { limit: params.limit };
        if (params.symbol) queryParams["symbol"] = params.symbol;
        const result = await engineFetch<TradeRecord[]>("/journal", queryParams);
        let trades = result.data ?? [];
        if (params.side !== "ALL") trades = trades.filter((t) => t.side === params.side);
        if (trades.length === 0) {
          return { content: [{ type: "text", text: "No trade records matched the filters." }] };
        }
        let text = `📒 Trade Journal — ${trades.length} record(s)\n\n` + trades.map(formatTrade).join("\n");
        if (text.length > CHARACTER_LIMIT) {
          text = text.slice(0, CHARACTER_LIMIT) + "\n… (truncated — reduce limit or filter by symbol/side)";
        }
        return { content: [{ type: "text", text }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
