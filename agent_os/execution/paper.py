"""Paper-only execution adapter for Phase 1."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import time
from typing import Any

from agent_os.contracts import ExecutionRequest, RiskDecisionStatus
from agent_os.risk import AgentRiskGate


@dataclass(frozen=True)
class PaperFill:
    """A simulated fill; it has no exchange order identifier."""

    request_id: str
    symbol: str
    side: str
    quantity: float
    price: float
    mode: str = "paper"
    status: str = "filled"
    filled_at: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class PaperExecutor:
    """Risk-gated paper executor with an in-memory fill ledger."""

    def __init__(self, risk_gate: AgentRiskGate | None = None) -> None:
        self.risk_gate = risk_gate or AgentRiskGate()
        self.fills: list[PaperFill] = []

    def submit(self, request: ExecutionRequest) -> dict[str, Any]:
        """Re-evaluate risk and create a simulated fill only when approved."""
        from agent_os.contracts import RiskCheckRequest

        decision = self.risk_gate.evaluate(
            RiskCheckRequest(
                request_id=request.request_id,
                idempotency_key=request.idempotency_key,
                actor_id=request.actor_id,
                symbol=request.symbol,
                side=request.side,
                quantity=request.quantity,
                price=request.price,
                leverage=request.leverage,
                mode=request.mode,
                connector_id=request.connector_id,
                policy_version=request.policy_version,
                reduce_only=request.reduce_only,
            )
        )
        if decision.status is not RiskDecisionStatus.APPROVED:
            return {
                "status": "rejected",
                "decision": decision.to_dict(),
                "fill": None,
            }

        fill = PaperFill(
            request_id=request.request_id,
            symbol=request.symbol,
            side=request.side,
            quantity=request.quantity,
            price=request.price,
            filled_at=time.time(),
        )
        self.fills.append(fill)
        return {
            "status": "filled",
            "decision": decision.to_dict(),
            "fill": fill.to_dict(),
        }
