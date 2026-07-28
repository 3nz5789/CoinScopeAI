"""
Kelly Criterion Position Sizing with Risk Caps

Implements fractional Kelly formula with layered risk caps:
- Fractional Kelly (default 25% of full Kelly)
- Regime-aware multipliers (bull 1.0x, chop 0.5x, bear 0.3x)
- Drawdown-based position reduction
- Consecutive-loss streak penalty
- Daily/rolling loss cap
- Volatility scaling
- Hard per-trade cap (default 2% of account)
- Max position cap (default 25% of account)
- Minimum viable position threshold
"""

from __future__ import annotations

from collections import deque
from datetime import datetime, timedelta
from typing import Optional

import numpy as np


class KellyRiskController:
    """Kelly criterion position sizing controller with layered risk caps."""

    def __init__(
        self,
        fraction: float = 0.25,              # fractional Kelly (conservative)
        hard_cap_pct: float = 0.02,          # never exceed this % per trade
        max_position_pct: float = 0.25,      # never exceed this % in one position
        min_position_usd: float = 10.0,      # skip tiny positions below this
        max_consecutive_losses: int = 3,     # start penalizing after N losses
        streak_penalty_step: float = 0.25,   # reduce size by this per loss over max
        daily_loss_cap_pct: float = 0.05,    # max daily loss before halting
        daily_lookback_hours: float = 24.0,  # rolling window for daily loss calc
        volatility_lookback: int = 20,       # candles for realized vol
        max_volatility_annualized: float = 1.00,  # cap sizing when vol > 100%
    ):
        self.fraction = fraction
        self.hard_cap = hard_cap_pct
        self.max_position_pct = max_position_pct
        self.min_position_usd = min_position_usd
        self.max_consecutive_losses = max_consecutive_losses
        self.streak_penalty_step = streak_penalty_step
        self.daily_loss_cap_pct = daily_loss_cap_pct
        self.daily_lookback = timedelta(hours=daily_lookback_hours)
        self.volatility_lookback = volatility_lookback
        self.max_volatility_annualized = max_volatility_annualized

        self.REGIME_MULT = {
            "bull": 1.0,
            "chop": 0.5,
            "bear": 0.3,
        }

        self.peak_equity: Optional[float] = None
        self.consecutive_losses: int = 0
        self.trade_pnl_log: deque = deque()  # (timestamp, pnl_pct)

        # Last-multiplier cache for summary/reporting
        self._last_dd_mult: float = 1.0
        self._last_streak_mult: float = 1.0
        self._last_daily_mult: float = 1.0
        self._last_vol_mult: float = 1.0
        self._last_cap_hit: Optional[str] = None

    # ── Public API ──────────────────────────────────────────────────────────

    def calculate_position_size(
        self,
        win_rate: float,
        avg_win: float,
        avg_loss: float,
        regime: str,
        account_balance: float,
        recent_returns: Optional[list[float]] = None,
    ) -> float:
        """
        Calculate position size in USD using Kelly + risk caps.

        Parameters
        ----------
        win_rate : float
            Historical win rate (0-1).
        avg_win : float
            Average win size (% as decimal, e.g. 0.021).
        avg_loss : float
            Average loss size (% as decimal, e.g. 0.010).
        regime : str
            Current market regime ('bull', 'chop', 'bear').
        account_balance : float
            Current account balance in USD.
        recent_returns : list[float] | None
            Recent return series for volatility scaling (optional).

        Returns
        -------
        float
            Recommended position size in USD.
        """
        self._last_cap_hit = None

        if account_balance <= 0 or avg_loss <= 0 or win_rate <= 0:
            return 0.0

        # Full Kelly fraction
        b = avg_win / avg_loss
        p = win_rate
        q = 1.0 - p
        kelly_full = (b * p - q) / b
        if kelly_full <= 0:
            return 0.0

        # Layer 1: fractional Kelly
        raw_pct = kelly_full * self.fraction

        # Layer 2: regime multiplier
        regime_mult = self.REGIME_MULT.get(regime, 0.5)
        raw_pct *= regime_mult

        # Layer 3: drawdown multiplier
        dd_mult = self._drawdown_multiplier(account_balance)
        self._last_dd_mult = dd_mult
        raw_pct *= dd_mult

        # Layer 4: consecutive-loss streak multiplier
        streak_mult = self._streak_multiplier()
        self._last_streak_mult = streak_mult
        raw_pct *= streak_mult

        # Layer 5: daily/rolling loss cap multiplier
        daily_mult = self._daily_loss_multiplier(account_balance)
        self._last_daily_mult = daily_mult
        raw_pct *= daily_mult

        # Layer 6: volatility scaling
        vol_mult = self._volatility_multiplier(recent_returns)
        self._last_vol_mult = vol_mult
        raw_pct *= vol_mult

        # Layer 7: hard per-trade cap
        if raw_pct > self.hard_cap:
            raw_pct = self.hard_cap
            self._last_cap_hit = "hard_cap"

        # Layer 8: max position cap
        if raw_pct > self.max_position_pct:
            raw_pct = self.max_position_pct
            self._last_cap_hit = "max_position_pct"

        # Layer 9: minimum viable position
        size = account_balance * raw_pct
        if size < self.min_position_usd:
            return 0.0

        return round(size, 2)

    def record_trade_result(self, pnl_pct: float, timestamp: Optional[datetime] = None) -> None:
        """
        Record a completed trade PnL so the sizer can update streak and
        rolling-loss state.

        Parameters
        ----------
        pnl_pct : float
            Trade PnL as a decimal (e.g. -0.012 for -1.2%).
        timestamp : datetime | None
            Defaults to utcnow().
        """
        ts = timestamp or datetime.utcnow()

        if pnl_pct < 0:
            self.consecutive_losses += 1
        else:
            self.consecutive_losses = 0

        self.trade_pnl_log.append((ts, pnl_pct))
        self._prune_pnl_log(ts)

    def reset(self) -> None:
        """Reset all state (peak equity, streaks, PnL log)."""
        self.peak_equity = None
        self.consecutive_losses = 0
        self.trade_pnl_log.clear()

    # ── Internal multipliers ────────────────────────────────────────────────

    def _drawdown_multiplier(self, equity: float) -> float:
        """Reduce size as drawdown deepens."""
        if self.peak_equity is None:
            self.peak_equity = equity

        self.peak_equity = max(self.peak_equity, equity)
        dd = (equity - self.peak_equity) / self.peak_equity

        if dd > -0.05:
            return 1.0
        elif dd > -0.10:
            return 0.75
        elif dd > -0.15:
            return 0.50
        else:
            return 0.25

    def _streak_multiplier(self) -> float:
        """Penalize size after a run of consecutive losses."""
        excess = self.consecutive_losses - self.max_consecutive_losses
        if excess <= 0:
            return 1.0
        return max(0.0, 1.0 - excess * self.streak_penalty_step)

    def _daily_loss_multiplier(self, equity: float) -> float:
        """If rolling loss exceeds daily cap, reduce new trades to 0."""
        if equity <= 0:
            return 0.0

        now = datetime.utcnow()
        self._prune_pnl_log(now)

        rolling_pnl = sum(pnl for _, pnl in self.trade_pnl_log)
        if rolling_pnl <= -self.daily_loss_cap_pct:
            return 0.0
        return 1.0

    def _volatility_multiplier(self, recent_returns: Optional[list[float]]) -> float:
        """Scale down when recent realized volatility is excessive."""
        if not recent_returns or len(recent_returns) < self.volatility_lookback:
            return 1.0

        arr = np.array(recent_returns[-self.volatility_lookback:])
        if arr.std() == 0:
            return 1.0

        # Annualized realized vol assuming daily returns
        realized_vol = arr.std() * np.sqrt(365)
        if realized_vol <= 0:
            return 1.0

        ratio = realized_vol / self.max_volatility_annualized
        if ratio <= 1.0:
            return 1.0
        # Linear taper: at 2x max vol, multiplier is 0.5
        return max(0.1, 1.0 / ratio)

    def _prune_pnl_log(self, now: datetime) -> None:
        """Drop PnL records outside the rolling lookback window."""
        cutoff = now - self.daily_lookback
        while self.trade_pnl_log and self.trade_pnl_log[0][0] < cutoff:
            self.trade_pnl_log.popleft()

    # ── Reporting ───────────────────────────────────────────────────────────

    def size_summary(
        self,
        win_rate: float,
        avg_win: float,
        avg_loss: float,
        regime: str,
        balance: float,
        recent_returns: Optional[list[float]] = None,
    ) -> dict:
        """Get detailed sizing summary."""

        peak_before = self.peak_equity
        size = self.calculate_position_size(
            win_rate, avg_win, avg_loss, regime, balance, recent_returns
        )

        if avg_loss <= 0 or win_rate <= 0:
            return {
                "kelly_full_pct": 0.0,
                "kelly_fraction_pct": 0.0,
                "regime_mult": self.REGIME_MULT.get(regime, 0.5),
                "dd_mult": self._last_dd_mult,
                "streak_mult": self._last_streak_mult,
                "daily_loss_mult": self._last_daily_mult,
                "volatility_mult": self._last_vol_mult,
                "raw_pct": 0.0,
                "capped_pct": 0.0,
                "final_size_usd": 0.0,
                "final_pct": 0.0,
                "cap_applied": "none",
            }

        b = avg_win / avg_loss
        p = win_rate
        q = 1.0 - p
        kelly_full = max(0.0, (b * p - q) / b)
        kelly_fraction = kelly_full * self.fraction

        raw_pct = (
            kelly_fraction
            * self.REGIME_MULT.get(regime, 0.5)
            * self._last_dd_mult
            * self._last_streak_mult
            * self._last_daily_mult
            * self._last_vol_mult
        )
        capped_pct = (size / balance * 100) if balance > 0 else 0.0

        return {
            "kelly_full_pct": round(kelly_full * 100, 4),
            "kelly_fraction_pct": round(kelly_fraction * 100, 4),
            "regime_mult": self.REGIME_MULT.get(regime, 0.5),
            "dd_mult": round(self._last_dd_mult, 3),
            "streak_mult": round(self._last_streak_mult, 3),
            "daily_loss_mult": round(self._last_daily_mult, 3),
            "volatility_mult": round(self._last_vol_mult, 3),
            "raw_pct": round(raw_pct * 100, 4),
            "capped_pct": round(capped_pct, 4),
            "final_size_usd": size,
            "final_pct": round(capped_pct, 4),
            "cap_applied": self._last_cap_hit or "none",
            "peak_equity": peak_before,
        }


# Example usage
if __name__ == "__main__":
    kelly = KellyRiskController(fraction=0.25)

    # Example: 44% win rate, 2.1% avg win, 1.0% avg loss
    size = kelly.calculate_position_size(
        win_rate=0.44,
        avg_win=0.021,
        avg_loss=0.010,
        regime="bull",
        account_balance=10000,
    )

    print(f"Position size: ${size:.2f}")

    # Get summary
    summary = kelly.size_summary(0.44, 0.021, 0.010, "bull", 10000)
    print(f"Summary: {summary}")
