import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { engineFetch, formatEngineError } from "../services/engine-client.js";
import { ScanInputSchema, type ScanInput } from "../schemas/index.js";
import type { SignalCandidate } from "../types.js";
import { CHARACTER_LIMIT } from "../constants.js";

function formatSignal(s: SignalCandidate, idx: number): string {
  const conf = (s.confidence * 100).toFixed(1);
  const regime = s.regime ? ` | regime: ${s.regime}` : "";
  const score = s.score !== undefined ? ` | score: ${s.score}` : "";
  return `${idx + 1}. ${s.symbol} — ${s.signal} (${conf}% confidence${regime}${score}) @ ${s.timestamp}`;
}

export function registerScanTool(server: McpServer): void {
  server.registerTool(
    "coinscope_scan",
    {
      title: "Scan Market Signals",
      description: `Scans the CoinScopeAI engine for active trading signal candidates across all supported USDT-M perpetual symbols.

Args:
  - min_confidence (number, optional): Drop signals below this threshold (0.0–1.0)
  - signal_type ('BUY' | 'SELL' | 'HOLD' | 'ALL'): Filter by direction (default: ALL)

Returns list of signal candidates with symbol, signal, confidence, timestamp, regime, score.
Use when: "what signals are active?", "any BUY setups?", "scan the market"`,
      inputSchema: ScanInputSchema,
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        idempotentHint: false,
        openWorldHint: true,
      },
    },
    async (params: ScanInput) => {
      try {
        const result = await engineFetch<SignalCandidate[]>("/scan");
        let signals = result.data ?? [];
        if (params.min_confidence !== undefined) {
          signals = signals.filter((s) => s.confidence >= (params.min_confidence ?? 0));
        }
        if (params.signal_type !== "ALL") {
          signals = signals.filter((s) => s.signal === params.signal_type);
        }
        if (signals.length === 0) {
          return { content: [{ type: "text", text: "No signals matched the requested filters." }] };
        }
        let text = `📡 Scan Results — ${signals.length} signal(s)\n\n` + signals.map(formatSignal).join("\n");
        if (text.length > CHARACTER_LIMIT) {
          text = text.slice(0, CHARACTER_LIMIT) + "\n… (truncated — use min_confidence to narrow)";
        }
        return { content: [{ type: "text", text }] };
      } catch (err) {
        return { content: [{ type: "text", text: formatEngineError(err) }] };
      }
    }
  );
}
