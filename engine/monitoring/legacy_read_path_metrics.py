"""Passive metrics contracts for the legacy read path.

This module deliberately records observations only.  It does not export, persist,
route, cache, fit, or otherwise influence runtime or trading behaviour.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Iterable, Mapping


class ReadPathMetricOutcome(str, Enum):
    """Closed set of outcomes that a read-path observation may report."""

    FRESH = "fresh"
    STALE = "stale"
    UNAVAILABLE = "unavailable"
    ERROR = "error"


@dataclass(frozen=True, slots=True)
class LegacyReadPathMetric:
    """One passive read-path observation supplied by a caller."""

    operation: str
    dependency: str
    outcome: ReadPathMetricOutcome
    latency_ms: float

    def __post_init__(self) -> None:
        if not self.operation.strip():
            raise ValueError("operation must not be blank")
        if not self.dependency.strip():
            raise ValueError("dependency must not be blank")
        if not isfinite(self.latency_ms) or self.latency_ms < 0:
            raise ValueError("latency_ms must be finite and non-negative")


@dataclass(frozen=True, slots=True)
class LegacyReadPathMetricsSnapshot:
    """Immutable aggregate returned to observers."""

    total: int
    by_operation: Mapping[str, int]
    by_dependency: Mapping[str, int]
    by_outcome: Mapping[ReadPathMetricOutcome, int]
    total_latency_ms: float
    max_latency_ms: float

    @property
    def average_latency_ms(self) -> float:
        """Return the arithmetic mean, or zero when no observations exist."""

        return self.total_latency_ms / self.total if self.total else 0.0


class LegacyReadPathMetrics:
    """In-memory passive collector for deterministic read-path observations."""

    def __init__(self) -> None:
        self._total = 0
        self._total_latency_ms = 0.0
        self._max_latency_ms = 0.0
        self._by_operation: Counter[str] = Counter()
        self._by_dependency: Counter[str] = Counter()
        self._by_outcome: Counter[ReadPathMetricOutcome] = Counter()

    def observe(self, metric: LegacyReadPathMetric) -> None:
        """Record one observation without invoking any dependency or side effect."""

        self._total += 1
        self._total_latency_ms += metric.latency_ms
        self._max_latency_ms = max(self._max_latency_ms, metric.latency_ms)
        self._by_operation[metric.operation] += 1
        self._by_dependency[metric.dependency] += 1
        self._by_outcome[metric.outcome] += 1

    def extend(self, metrics: Iterable[LegacyReadPathMetric]) -> None:
        """Record a deterministic iterable of observations."""

        for metric in metrics:
            self.observe(metric)

    def snapshot(self) -> LegacyReadPathMetricsSnapshot:
        """Return a detached, immutable-by-convention aggregate snapshot."""

        return LegacyReadPathMetricsSnapshot(
            total=self._total,
            by_operation=dict(self._by_operation),
            by_dependency=dict(self._by_dependency),
            by_outcome=dict(self._by_outcome),
            total_latency_ms=self._total_latency_ms,
            max_latency_ms=self._max_latency_ms,
        )

    def reset(self) -> None:
        """Clear only this process-local collector."""

        self._total = 0
        self._total_latency_ms = 0.0
        self._max_latency_ms = 0.0
        self._by_operation.clear()
        self._by_dependency.clear()
        self._by_outcome.clear()


__all__ = [
    "LegacyReadPathMetric",
    "LegacyReadPathMetrics",
    "LegacyReadPathMetricsSnapshot",
    "ReadPathMetricOutcome",
]
