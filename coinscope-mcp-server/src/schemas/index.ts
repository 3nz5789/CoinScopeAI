import { z } from "zod";
import { SUPPORTED_SYMBOLS } from "../constants.js";

export const SymbolSchema = z
  .enum(SUPPORTED_SYMBOLS)
  .describe(`Binance USDT-M perpetual symbol. Supported: ${SUPPORTED_SYMBOLS.join(", ")}`);

export const ScanInputSchema = z.object({
  min_confidence: z.number().min(0).max(1).optional()
    .describe("Filter signals below this confidence threshold (0.0–1.0). Omit to return all."),
  signal_type: z.enum(["BUY", "SELL", "HOLD", "ALL"]).default("ALL")
    .describe("Filter by signal direction. Default: ALL"),
}).strict();

export const PerformanceInputSchema = z.object({}).strict();

export const JournalInputSchema = z.object({
  symbol: SymbolSchema.optional().describe("Filter journal to a specific symbol. Omit for all."),
  limit: z.number().int().min(1).max(500).default(50)
    .describe("Maximum number of trade records to return (1–500). Default: 50"),
  side: z.enum(["LONG", "SHORT", "ALL"]).default("ALL")
    .describe("Filter by trade side. Default: ALL"),
}).strict();

export const RiskGateInputSchema = z.object({}).strict();

export const PositionSizeInputSchema = z.object({
  symbol: SymbolSchema.describe("Symbol to size a position for."),
  account_equity_usdt: z.number().positive().optional()
    .describe("Current account equity in USDT for Kelly calculation."),
}).strict();

export const RegimeInputSchema = z.object({
  symbol: SymbolSchema.describe("Symbol to detect market regime for."),
}).strict();

export type ScanInput = z.infer<typeof ScanInputSchema>;
export type PerformanceInput = z.infer<typeof PerformanceInputSchema>;
export type JournalInput = z.infer<typeof JournalInputSchema>;
export type RiskGateInput = z.infer<typeof RiskGateInputSchema>;
export type PositionSizeInput = z.infer<typeof PositionSizeInputSchema>;
export type RegimeInput = z.infer<typeof RegimeInputSchema>;
