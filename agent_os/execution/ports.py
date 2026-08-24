"""Execution adapter ports."""

from __future__ import annotations

from typing import Any, Protocol

from agent_os.contracts import ExecutionRequest


class ExecutionPort(Protocol):
    """An execution adapter must accept only typed requests."""

    def submit(self, request: ExecutionRequest) -> dict[str, Any]:
        """Submit a request after a mandatory risk check."""
