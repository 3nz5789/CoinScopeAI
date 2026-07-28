export interface EngineResponse<T> {
  status: "success" | "error";
  data: T;
}

export interface SignalCandidate {
  symbol: string;
  signal: "BUY" | "SELL" | "HOLD";
  confidence: number;
  timestamp: string;
  regime?: string;
  score?: number;
}

export type ScanResponse = EngineResponse<SignalCandidate[]>;

export interface PerformanceMetrics {
  total_trades: number;
  win_rate: number;
  profit_factor: number;
  current_drawdown: number;
  total_pnl_usdt?: number;
  sharpe_ratio?: number;
}

export type PerformanceResponse = EngineResponse<PerformanceMetrics>;

export interface TradeRecord {
  trade_id: string;
  symbol: string;
  side: "LONG" | "SHORT";
  entry_price: number;
  exit_price: number | null;
  pnl: number | null;
  timestamp: string;
  gate_decision?: string;
  regime?: string;
}

export type JournalResponse = EngineResponse<TradeRecord[]>;

export interface RiskGateStatus {
  daily_loss_limit_hit: boolean;
  drawdown_limit_hit: boolean;
  kill_switch_armed: boolean;
  open_positions?: number;
  daily_loss_pct?: number;
  current_drawdown_pct?: number;
}

export type RiskGateResponse = EngineResponse<RiskGateStatus>;

export interface PositionSizeResult {
  symbol: string;
  recommended_size_usdt: number;
  leverage: number;
  kelly_fraction?: number;
  heat_cap_pct?: number;
}

export type PositionSizeResponse = EngineResponse<PositionSizeResult>;

export interface RegimeResult {
  symbol: string;
  regime: "trending" | "mean-reverting" | "volatile" | "quiet";
  confidence: number;
  timestamp?: string;
}

export type RegimeResponse = EngineResponse<RegimeResult>;
