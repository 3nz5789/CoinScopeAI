// CoinScopeAI canonical constants — locked 2026-05-01 via PCC v2 §8
export const ENGINE_BASE_URL =
  process.env.COINSCOPE_ENGINE_URL ?? "http://localhost:8001";

export const SUPPORTED_SYMBOLS = [
  "BTCUSDT",
  "ETHUSDT",
  "SOLUSDT",
  "BNBUSDT",
  "XRPUSDT",
] as const;

export type SupportedSymbol = (typeof SUPPORTED_SYMBOLS)[number];

// Canonical risk thresholds — locked 2026-05-01 (PCC v2 §8 Capital Cap)
// Revised 2026-05-03: MAX_OPEN_POSITIONS 3 → 5
export const RISK_THRESHOLDS = {
  MAX_LEVERAGE: 10,
  MAX_OPEN_POSITIONS: 5,
  MAX_DRAWDOWN_PCT: 10,
  MAX_DAILY_LOSS_PCT: 5,
  POSITION_HEAT_CAP_PCT: 80,
  KELLY_HARD_CAP_PCT: 2,
} as const;

export const REQUEST_TIMEOUT_MS = 10_000;
export const CHARACTER_LIMIT = 8_000;
