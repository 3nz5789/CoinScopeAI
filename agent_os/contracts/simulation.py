"""Simulation and paper-session result contracts."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class SimulationMetrics:
    """Metrics envelope; formulas and assumptions belong to the run metadata."""

    net_pnl: float = 0.0
    win_rate: float = 0.0
    profit_factor: float = 0.0
    max_drawdown: float = 0.0
    trade_sharpe: float = 0.0
    funding_rate_drag: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SimulationRun:
    """A replay or backtest result with explicit provenance and assumptions."""

    run_id: str
    strategy_version: int
    source: str
    mode: str = "paper"
    status: str = "created"
    assumptions: dict[str, Any] = field(default_factory=dict)
    metrics: SimulationMetrics = field(default_factory=SimulationMetrics)
    trades: list[dict[str, Any]] = field(default_factory=list)
    equity: list[dict[str, float]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["metrics"] = self.metrics.to_dict()
        return value


@dataclass(frozen=True)
class PaperSession:
    """Paper account state; it has no provider-side order capability."""

    session_id: str
    starting_equity: float
    current_equity: float
    status: str = "paused"
    mode: str = "paper"
    simulated_fills: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
