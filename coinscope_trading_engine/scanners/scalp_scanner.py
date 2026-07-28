"""
scalp_scanner.py — CoinScopeAI Scalping Signal Scanner
Part of: app/engine/

Scans USDT-perpetual pairs for short-timeframe scalp setups using
technical indicators and exchange data from the integrations layer.

Import rule (post 2026-04-19 restructure):
    Exchange-specific helpers MUST come from app.integrations.<provider>
    NOT from app.engine.scanner (which no longer exports exchange helpers).
    See app/integrations/README.md for full scope documentation.
"""

from app.integrations.binance import (
    get_klines,
    get_orderbook,
    get_funding_rate,
    get_open_interest,
)
# OKX is REST klines fallback ONLY — do not use for trading
# See COI-56 for scope documentation
from app.integrations.okx import get_klines as get_klines_okx

import numpy as np
import pandas as pd
from typing import Optional


class ScalpScanner:
    """
    Short-timeframe signal scanner for USDT-perpetual futures.

    Scans on 1m/5m/15m timeframes for momentum, mean-reversion,
    and microstructure-based scalp setups.

    Capital preservation rules apply — all signals pass through
    the risk gate before sizing or execution.
    """

    # Canonical risk thresholds — locked 2026-05-01 (PCC v2 §8)
    # DO NOT modify without a decision-log entry + ADR
    MAX_LEVERAGE = 10          # per position ceiling
    MAX_OPEN_POSITIONS = 5     # concurrent positions ceiling
    MIN_SIGNAL_SCORE = 5.5     # minimum confluence score to surface

    def __init__(
        self,
        symbols: list[str],
        timeframe: str = "5m",
        min_score: float = 5.5,
        use_okx_fallback: bool = False,
    ):
        """
        Args:
            symbols: List of USDT-perpetual symbols e.g. ["BTCUSDT", "ETHUSDT"]
            timeframe: Candle timeframe — "1m", "5m", "15m"
            min_score: Minimum confluence score to include in output (0–12)
            use_okx_fallback: Use OKX REST klines when Binance returns 451.
                              OKX is data-only — never used for execution.
        """
        self.symbols = symbols
        self.timeframe = timeframe
        self.min_score = max(min_score, self.MIN_SIGNAL_SCORE)
        self.use_okx_fallback = use_okx_fallback

    def _fetch_klines(self, symbol: str) -> Optional[pd.DataFrame]:
        """Fetch OHLCV data with OKX fallback for 451 regions."""
        try:
            return get_klines(symbol=symbol, interval=self.timeframe, limit=200)
        except Exception as e:
            if self.use_okx_fallback and "451" in str(e):
                # OKX REST klines fallback — data only, no execution
                return get_klines_okx(symbol=symbol, interval=self.timeframe, limit=200)
            raise

    def _score_signal(
        self,
        df: pd.DataFrame,
        funding_rate: float,
        open_interest_delta: float,
    ) -> dict:
        """
        Compute confluence score (0–12) across 6 factors × 2 points each:
          RSI, EMA alignment, ATR momentum, Volume, CVD, Entry Timing

        Returns signal dict with score, direction, and factor breakdown.
        """
        if df is None or len(df) < 50:
            return {}

        close = df["close"].values
        high = df["high"].values
        low = df["low"].values
        volume = df["volume"].values

        score = 0.0
        direction = None
        factors = {}

        # 1. RSI (2 pts)
        rsi = self._rsi(close, period=14)
        if rsi < 30:
            score += 2.0
            direction = "LONG"
            factors["rsi"] = f"{rsi:.1f} — oversold ✅"
        elif rsi > 70:
            score += 2.0
            direction = "SHORT"
            factors["rsi"] = f"{rsi:.1f} — overbought ✅"
        else:
            factors["rsi"] = f"{rsi:.1f} — neutral"

        # 2. EMA alignment (2 pts)
        ema20 = self._ema(close, 20)
        ema50 = self._ema(close, 50)
        if close[-1] > ema20 > ema50:
            score += 2.0 if direction in (None, "LONG") else 0.0
            factors["ema"] = "20 > 50, price above — bullish ✅"
        elif close[-1] < ema20 < ema50:
            score += 2.0 if direction in (None, "SHORT") else 0.0
            factors["ema"] = "20 < 50, price below — bearish ✅"
        else:
            factors["ema"] = "mixed"

        # 3. ATR momentum (2 pts)
        atr = self._atr(high, low, close, period=14)
        body = abs(close[-1] - close[-2])
        if body > atr * 0.8:
            score += 2.0
            factors["atr"] = f"body {body:.4f} > 0.8×ATR — momentum ✅"
        else:
            factors["atr"] = f"body {body:.4f} < 0.8×ATR — weak"

        # 4. Volume (2 pts)
        avg_vol = np.mean(volume[-20:])
        if volume[-1] > avg_vol * 1.5:
            score += 2.0
            factors["volume"] = f"vol {volume[-1]:.0f} > 1.5×avg — surge ✅"
        else:
            factors["volume"] = f"vol {volume[-1]:.0f} — normal"

        # 5. Funding rate (2 pts)
        if abs(funding_rate) > 0.0008:  # >0.08% = extreme
            if funding_rate < -0.0008 and direction in (None, "LONG"):
                score += 2.0
                factors["funding"] = f"{funding_rate:.4%} — extreme negative, mean-reversion LONG ✅"
            elif funding_rate > 0.0008 and direction in (None, "SHORT"):
                score += 2.0
                factors["funding"] = f"{funding_rate:.4%} — extreme positive, mean-reversion SHORT ✅"
            else:
                factors["funding"] = f"{funding_rate:.4%} — extreme but against direction"
        else:
            factors["funding"] = f"{funding_rate:.4%} — neutral"

        # 6. Open interest delta (2 pts)
        if open_interest_delta > 0.02 and direction == "LONG":
            score += 2.0
            factors["oi"] = f"+{open_interest_delta:.1%} OI rising — confirms LONG ✅"
        elif open_interest_delta < -0.02 and direction == "SHORT":
            score += 2.0
            factors["oi"] = f"{open_interest_delta:.1%} OI falling — confirms SHORT ✅"
        else:
            factors["oi"] = f"{open_interest_delta:.1%} OI — no confirmation"

        return {
            "score": round(score, 1),
            "direction": direction,
            "factors": factors,
        }

    def scan(self) -> list[dict]:
        """
        Run full scan across all symbols.

        Returns list of signal dicts sorted by score descending,
        filtered to min_score threshold.
        """
        results = []

        for symbol in self.symbols:
            try:
                df = self._fetch_klines(symbol)
                funding = get_funding_rate(symbol=symbol)
                ob = get_orderbook(symbol=symbol, limit=5)
                oi_now = get_open_interest(symbol=symbol)
                oi_1h_ago = get_open_interest(symbol=symbol, lookback_hours=1)

                oi_delta = (
                    (oi_now - oi_1h_ago) / oi_1h_ago
                    if oi_1h_ago and oi_1h_ago > 0
                    else 0.0
                )

                signal = self._score_signal(
                    df=df,
                    funding_rate=funding.get("funding_rate", 0.0),
                    open_interest_delta=oi_delta,
                )

                if signal and signal.get("score", 0) >= self.min_score:
                    signal["symbol"] = symbol
                    signal["timeframe"] = self.timeframe
                    results.append(signal)

            except Exception as e:
                # Non-fatal — log and continue scanning other symbols
                print(f"[ScalpScanner] {symbol} error: {e}")
                continue

        return sorted(results, key=lambda x: x["score"], reverse=True)

    # ── Technical indicator helpers ──────────────────────────────────────────

    @staticmethod
    def _rsi(close: np.ndarray, period: int = 14) -> float:
        deltas = np.diff(close)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)
        avg_gain = np.mean(gains[-period:])
        avg_loss = np.mean(losses[-period:])
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return round(100 - (100 / (1 + rs)), 2)

    @staticmethod
    def _ema(close: np.ndarray, period: int) -> float:
        k = 2 / (period + 1)
        ema = close[0]
        for price in close[1:]:
            ema = price * k + ema * (1 - k)
        return ema

    @staticmethod
    def _atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> float:
        tr = np.maximum(
            high[1:] - low[1:],
            np.maximum(
                np.abs(high[1:] - close[:-1]),
                np.abs(low[1:] - close[:-1]),
            ),
        )
        return float(np.mean(tr[-period:]))
