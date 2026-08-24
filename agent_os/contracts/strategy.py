"""Portable strategy and agent-graph contracts for the CoinScopeAI Agent OS."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class NodeKind(str, Enum):
    SCHEDULE = "schedule"
    MARKET = "market"
    CONDITION = "condition"
    ENTRY = "entry"
    RISK = "risk"
    EXIT = "exit"


class StrategyLifecycle(str, Enum):
    DRAFT = "draft"
    BACKTEST_READY = "backtest_ready"
    BACKTEST_PASSED = "backtest_passed"
    PAPER_READY = "paper_ready"
    PAPER_ARMED = "paper_armed"
    LIVE_REVIEW_REQUIRED = "live_review_required"


@dataclass(frozen=True)
class StrategyNode:
    """One inspectable node in a strategy graph."""

    id: str
    kind: NodeKind
    title: str
    detail: str
    tone: str = "blue"

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["kind"] = self.kind.value
        return value


@dataclass
class StrategyDocument:
    """Versioned source of truth shared by prompt, graph, and replay."""

    name: str
    prompt: str
    nodes: list[StrategyNode] = field(default_factory=list)
    code: str = ""
    version: int = 1
    mode: str = "paper"
    lifecycle: StrategyLifecycle = StrategyLifecycle.DRAFT
    missing_fields: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "prompt": self.prompt,
            "nodes": [node.to_dict() for node in self.nodes],
            "code": self.code,
            "version": self.version,
            "mode": self.mode,
            "lifecycle": self.lifecycle.value,
            "missing_fields": list(self.missing_fields),
        }
