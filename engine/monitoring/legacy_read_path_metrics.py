"""Passive, in-memory contracts for legacy read-path metrics.

This module intentionally does not register Prometheus collectors or perform any
I/O.  A later, separately approved integration may translate these snapshots into
an exporter format.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import Enum
from math import isfinite
from types import MappingProxyType
from typing import Iterable, Mapping


LEGACY_READ_REQUESTS_TOTAL = "coinscopeai_legacy_read_requests_total"
LEGACY_READ_DURATION_SECONDS = "coinscopeai_legacy_read_duration_seconds"
LEGACY_READ_DEPENDENCY_DURATION_SECONDS = "coinscopeai_legacy_read_dependency_duration_seconds"
LEGACY_READ_ERRORS_TOTAL = "coinscopeai_legacy_read_errors_total"
LEGACY_REGIME_SOURCE_TOTAL = "coinscopeai_legacy_regime_source_total"

METRIC_NAMES = (
    LEGACY_READ_REQUESTS_TOTAL,
    LEGACY_READ_DURATION_SECONDS,
    LEGACY_READ_DEPENDENCY_DURATION_SECONDS,
    LEGACY_READ_ERRORS_TOTAL,
    LEGACY_REGIME_SOURCE_TOTAL,
)

# Fixed, finite, cumulative histogram boundaries in seconds.
HISTOGRAM_BUCKETS_SECONDS = (0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)
ROUTES = ("/scan", "/regime/{symbol}")
DEPENDENCIES = ("exchange", "database", "model", "cache")
ERROR_CLASSIFICATIONS = ("timeout", "rate_limited", "invalid_response", "internal")
REGIME_SOURCES = ("hmm_regime_v1", "hmm_fallback")


class ReadPathMetricOutcome(str, Enum):
    FRESH = "fresh"
    STALE = "stale"
    UNAVAILABLE = "unavailable"
    CIRCUIT_OPEN = "circuit_open"
    MODEL_UNAVAILABLE = "model_unavailable"


@dataclass(frozen=True, slots=True)
class HistogramSnapshot:
    """Cumulative fixed-bucket data sufficient for later histogram export."""

    buckets_seconds: tuple[float, ...]
    bucket_counts: tuple[int, ...]
    count: int
    total_seconds: float


@dataclass(frozen=True, slots=True)
class LegacyReadPathMetricsSnapshot:
    """Detached aggregate containing only bounded, non-sensitive dimensions."""

    requests_total: Mapping[str, int]
    duration_seconds: Mapping[str, HistogramSnapshot]
    dependency_duration_seconds: Mapping[str, HistogramSnapshot]
    errors_total: Mapping[tuple[str, str], int]
    regime_source_total: Mapping[tuple[str, str], int]

    @property
    def metric_names(self) -> tuple[str, ...]:
        return METRIC_NAMES


class LegacyReadPathMetrics:
    """Process-local passive collector; recording failure never affects a caller."""

    def __init__(self) -> None:
        self._requests: Counter[str] = Counter()
        self._route_durations: dict[str, list[float]] = defaultdict(list)
        self._dependency_durations: dict[str, list[float]] = defaultdict(list)
        self._errors: Counter[tuple[str, str]] = Counter()
        self._regime_sources: Counter[tuple[str, str]] = Counter()

    @staticmethod
    def _valid_duration(duration_seconds: float) -> bool:
        return isfinite(duration_seconds) and duration_seconds >= 0

    @staticmethod
    def _histogram(values: Iterable[float]) -> HistogramSnapshot:
        ordered = tuple(values)
        counts = tuple(sum(value <= bucket for value in ordered) for bucket in HISTOGRAM_BUCKETS_SECONDS)
        return HistogramSnapshot(
            buckets_seconds=HISTOGRAM_BUCKETS_SECONDS,
            bucket_counts=counts,
            count=len(ordered),
            total_seconds=sum(ordered),
        )

    def observe_request(
        self,
        route: str,
        outcome: ReadPathMetricOutcome | str,
        duration_seconds: float,
        error_classification: str | None = None,
    ) -> bool:
        """Record a route observation; reject invalid/unbounded input fail-open."""

        try:
            normalized_outcome = ReadPathMetricOutcome(outcome)
        except (TypeError, ValueError):
            return False
        if route not in ROUTES or not self._valid_duration(duration_seconds):
            return False
        if error_classification is not None and error_classification not in ERROR_CLASSIFICATIONS:
            return False
        self._requests[route] += 1
        self._route_durations[route].append(duration_seconds)
        if error_classification is not None:
            self._errors[(route, error_classification)] += 1
        # Keep the outcome validation meaningful even though request totals are
        # intentionally outcome-neutral for the first passive contract.
        _ = normalized_outcome
        return True

    def observe_dependency(self, dependency: str, duration_seconds: float) -> bool:
        """Record bounded dependency duration in seconds, fail-open on bad input."""

        if dependency not in DEPENDENCIES or not self._valid_duration(duration_seconds):
            return False
        self._dependency_durations[dependency].append(duration_seconds)
        return True

    def observe_regime_source(self, route: str, source: str) -> bool:
        """Record a bounded primary or fallback regime source."""

        if route != "/regime/{symbol}" or source not in REGIME_SOURCES:
            return False
        self._regime_sources[(route, source)] += 1
        return True

    def snapshot(self) -> LegacyReadPathMetricsSnapshot:
        """Return detached mappings and fixed-bucket aggregates."""

        return LegacyReadPathMetricsSnapshot(
            requests_total=MappingProxyType(dict(self._requests)),
            duration_seconds=MappingProxyType(
                {route: self._histogram(values) for route, values in self._route_durations.items()}
            ),
            dependency_duration_seconds=MappingProxyType(
                {dependency: self._histogram(values) for dependency, values in self._dependency_durations.items()}
            ),
            errors_total=MappingProxyType(dict(self._errors)),
            regime_source_total=MappingProxyType(dict(self._regime_sources)),
        )

    def reset(self) -> None:
        """Clear only this process-local collector."""

        self._requests.clear()
        self._route_durations.clear()
        self._dependency_durations.clear()
        self._errors.clear()
        self._regime_sources.clear()


__all__ = [
    "DEPENDENCIES",
    "ERROR_CLASSIFICATIONS",
    "HISTOGRAM_BUCKETS_SECONDS",
    "LEGACY_READ_DEPENDENCY_DURATION_SECONDS",
    "LEGACY_READ_DURATION_SECONDS",
    "LEGACY_READ_ERRORS_TOTAL",
    "LEGACY_READ_REQUESTS_TOTAL",
    "LEGACY_REGIME_SOURCE_TOTAL",
    "METRIC_NAMES",
    "REGIME_SOURCES",
    "ROUTES",
    "HistogramSnapshot",
    "LegacyReadPathMetrics",
    "LegacyReadPathMetricsSnapshot",
    "ReadPathMetricOutcome",
]
