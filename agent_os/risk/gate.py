"""Mandatory Agent OS risk boundary.

The facade keeps Agent OS contracts separate from the existing P0 paper-trading
implementation while delegating the actual safety checks to that implementation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agent_os.contracts import (
    ExecutionMode,
    RiskCheckRequest,
    RiskDecision,
    RiskDecisionStatus,
)
from services.paper_trading.config import TradingConfig
from services.paper_trading.safety import KillSwitch, SafetyGate


@dataclass(frozen=True)
class RiskGateConfig:
    """Phase-1 policy values that are intentionally conservative."""

    allowed_symbols: tuple[str, ...] = (
        "BTCUSDT",
        "ETHUSDT",
        "SOLUSDT",
        "BNBUSDT",
        "XRPUSDT",
    )
    policy_version: str = "phase1-paper-v1"


class AgentRiskGate:
    """Single risk API for strategy, paper, and future execution callers."""

    def __init__(
        self,
        config: RiskGateConfig | None = None,
        safety_gate: SafetyGate | None = None,
    ) -> None:
        self.config = config or RiskGateConfig()
        self.kill_switch = KillSwitch()
        self.safety_gate = safety_gate or SafetyGate(
            TradingConfig(symbols=list(self.config.allowed_symbols)),
            kill_switch=self.kill_switch,
        )

    def _decision(
        self,
        request: RiskCheckRequest,
        status: RiskDecisionStatus,
        reasons: list[str],
    ) -> RiskDecision:
        return RiskDecision(
            request_id=request.request_id,
            status=status,
            policy_version=request.policy_version or self.config.policy_version,
            mode=request.mode,
            reasons=reasons,
            audit_id=f"audit-{request.request_id}",
        )

    def evaluate(self, request: RiskCheckRequest) -> RiskDecision:
        """Return an auditable decision; no adapter is invoked here."""
        if not request.request_id or not request.idempotency_key or not request.actor_id:
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                ["request_identity_incomplete"],
            )

        if request.mode is not ExecutionMode.PAPER:
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                ["phase1_live_and_testnet_order_submission_disabled"],
            )

        if request.connector_id != "paper":
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                ["phase1_connector_must_be_paper"],
            )

        if request.symbol.upper() not in self.config.allowed_symbols:
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                ["symbol_not_allowed"],
            )

        if request.quantity <= 0 or request.price <= 0 or request.leverage <= 0:
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                ["invalid_order_parameters"],
            )

        approved, rejection_reason, message = self.safety_gate.validate_order(
            request.to_order_request()
        )
        if not approved:
            return self._decision(
                request,
                RiskDecisionStatus.REJECTED,
                [
                    rejection_reason.value if rejection_reason else "safety_gate_rejected",
                    message,
                ],
            )

        return self._decision(
            request,
            RiskDecisionStatus.APPROVED,
            ["canonical_safety_gate_approved"],
        )

    def update_account(
        self,
        *,
        equity: float | None = None,
        daily_pnl: float | None = None,
        positions: dict[str, dict[str, Any]] | None = None,
    ) -> None:
        """Update state from the paper account; unavailable state stays fail-closed."""
        if equity is not None:
            self.safety_gate.update_equity(equity)
        if daily_pnl is not None:
            self.safety_gate.update_daily_pnl(daily_pnl)
        if positions is not None:
            self.safety_gate.update_positions(positions)

    def status(self) -> dict[str, Any]:
        """Return safety telemetry without exposing credentials."""
        return self.safety_gate.get_status()
