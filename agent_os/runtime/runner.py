"""Runtime inspection and replay seam for Phase 1."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from agent_os.contracts import MarketEvent, StrategyDocument
from agent_os.data.ports import MarketDataPort

from .graph import AgentGraph, GraphValidation


@dataclass
class RuntimeResult:
    """Safe runtime output for API, CLI, and dashboard consumers."""

    status: str
    graph: GraphValidation
    events_seen: int = 0
    observations: list[dict[str, Any]] = field(default_factory=list)
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["graph"] = self.graph.to_dict()
        return value


class AgentRunner:
    """Run graph inspection against fixture/replay data only.

    This class deliberately emits observations rather than execution requests.
    The risk facade and paper executor are the only later stages permitted to
    handle an execution request.
    """

    def __init__(self, source: MarketDataPort) -> None:
        self._source = source

    def inspect(self, document: StrategyDocument) -> RuntimeResult:
        validation = AgentGraph(document).validate()
        if not validation.valid:
            return RuntimeResult(
                status="blocked",
                graph=validation,
                message="Strategy draft is incomplete; no execution request was created",
            )

        observations: list[dict[str, Any]] = []
        for event in self._source.events():
            observations.append(self._observation(event))
        return RuntimeResult(
            status="ready",
            graph=validation,
            events_seen=len(observations),
            observations=observations,
            message="Graph inspected against data source; execution remains paper-gated",
        )

    @staticmethod
    def _observation(event: MarketEvent) -> dict[str, Any]:
        return {
            "event_type": event.event_type.value,
            "symbol": event.symbol,
            "event_time": event.event_time,
            "provenance": event.provenance.value,
            "payload": event.payload,
        }
