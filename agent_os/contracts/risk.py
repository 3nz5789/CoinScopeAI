"""Risk policy and decision contracts for the Agent OS boundary."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class ExecutionMode(str, Enum):
    PAPER = "paper"
    TESTNET = "testnet"
    LIVE = "live"


class RiskDecisionStatus(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class RiskCheckRequest:
    """A strategy intent before any simulated or provider-side order action."""

    request_id: str
    idempotency_key: str
    actor_id: str
    symbol: str
    side: str
    quantity: float
    price: float
    leverage: int
    mode: ExecutionMode = ExecutionMode.PAPER
    connector_id: str = "paper"
    policy_version: str = "phase1-paper-v1"
    reduce_only: bool = False

    def to_order_request(self) -> Any:
        """Convert to the existing canonical paper-trading safety model."""
        from services.paper_trading.safety import OrderRequest

        return OrderRequest(
            symbol=self.symbol,
            side=self.side,
            order_type="MARKET",
            quantity=self.quantity,
            price=self.price,
            leverage=self.leverage,
            reduce_only=self.reduce_only,
        )


@dataclass(frozen=True)
class RiskDecision:
    """Backend-verifiable decision returned by the risk gate."""

    request_id: str
    status: RiskDecisionStatus
    policy_version: str
    mode: ExecutionMode
    reasons: list[str] = field(default_factory=list)
    audit_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["status"] = self.status.value
        value["mode"] = self.mode.value
        return value
