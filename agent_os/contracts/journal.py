"""Audit and journal contracts for the Agent OS."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class JournalEvent:
    """A non-secret event that explains what the agent did and why."""

    event_id: str
    event_type: str
    occurred_at: float
    strategy_id: str
    strategy_version: int
    mode: str
    request_id: str = ""
    decision: str = ""
    reason: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
