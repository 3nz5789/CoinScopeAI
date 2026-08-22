"""Execution and connector contracts; Phase 1 exposes paper mode only."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .risk import ExecutionMode


@dataclass(frozen=True)
class ConnectorSummary:
    """Redacted connector state suitable for rendering in the UX."""

    connector_id: str
    provider: str
    environment: str
    connection_state: str = "not_configured"
    read_only: bool = True
    trade_enabled: bool = False
    withdrawals_disabled: bool = True
    verification_status: str = "pending"
    redacted_fingerprint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ExecutionRequest:
    """The only request shape accepted by an execution adapter."""

    request_id: str
    idempotency_key: str
    actor_id: str
    connector_id: str
    mode: ExecutionMode
    symbol: str
    side: str
    quantity: float
    price: float
    leverage: int
    requires_confirmation: bool = False
    reduce_only: bool = False
    policy_version: str = "phase1-paper-v1"

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["mode"] = self.mode.value
        return value
