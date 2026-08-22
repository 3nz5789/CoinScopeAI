"""Provider-neutral data ports used by runtime and replay."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Protocol

from agent_os.contracts import DataStatus, MarketEvent


class MarketDataPort(Protocol):
    """Minimum interface consumed by an agent graph."""

    def status(self) -> DataStatus:
        """Return current provider/replay state."""

    def events(self) -> Iterable[MarketEvent]:
        """Yield normalized events in event-time order."""


class EventSource:
    """Small in-memory source used by fixtures and deterministic tests."""

    def __init__(self, events: Iterable[MarketEvent], provider: str = "fixture") -> None:
        self._events = tuple(events)
        self._provider = provider

    def events(self) -> Iterator[MarketEvent]:
        yield from self._events

    def status(self) -> DataStatus:
        last_event_time = self._events[-1].event_time if self._events else None
        return DataStatus(
            provider=self._provider,
            state="live" if self._events else "offline",
            freshness_seconds=0.0 if self._events else None,
            last_event_time=last_event_time,
            message="Deterministic local source" if self._events else "No events available",
        )
