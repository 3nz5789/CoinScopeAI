from __future__ import annotations

from dataclasses import dataclass

from engine.monitoring.legacy_read_path_metrics import (
    HISTOGRAM_BUCKETS_SECONDS,
    LEGACY_READ_DEPENDENCY_DURATION_SECONDS,
    LEGACY_READ_DURATION_SECONDS,
    LEGACY_READ_ERRORS_TOTAL,
    LEGACY_READ_REQUESTS_TOTAL,
    LEGACY_REGIME_SOURCE_TOTAL,
    LegacyReadPathMetrics,
    ReadPathMetricOutcome,
)


@dataclass
class ControlledDependency:
    """Deterministic dependency double; it performs no external I/O."""

    latency_seconds: float = 0.002
    calls: int = 0

    def read(self) -> float:
        self.calls += 1
        return self.latency_seconds


def run_controlled_read_batch(dependency: ControlledDependency, count: int) -> LegacyReadPathMetrics:
    collector = LegacyReadPathMetrics()
    for _ in range(count):
        duration_seconds = dependency.read()
        collector.observe_dependency("exchange", duration_seconds)
        collector.observe_request("/scan", ReadPathMetricOutcome.FRESH, duration_seconds)
    collector.observe_request("/scan", ReadPathMetricOutcome.UNAVAILABLE, 0.1, "timeout")
    collector.observe_request("/regime/{symbol}", ReadPathMetricOutcome.MODEL_UNAVAILABLE, 0.2, "internal")
    collector.observe_regime_source("/regime/{symbol}", "hmm_regime_v1")
    collector.observe_regime_source("/regime/{symbol}", "hmm_fallback")
    return collector


def test_controlled_benchmark_is_repeatable_and_exposes_all_contract_names() -> None:
    first_dependency = ControlledDependency()
    second_dependency = ControlledDependency()
    first = run_controlled_read_batch(first_dependency, 100).snapshot()
    second = run_controlled_read_batch(second_dependency, 100).snapshot()

    assert first == second
    assert first_dependency.calls == second_dependency.calls == 100
    assert first.metric_names == (
        LEGACY_READ_REQUESTS_TOTAL,
        LEGACY_READ_DURATION_SECONDS,
        LEGACY_READ_DEPENDENCY_DURATION_SECONDS,
        LEGACY_READ_ERRORS_TOTAL,
        LEGACY_REGIME_SOURCE_TOTAL,
    )
    assert first.duration_seconds["/scan"].buckets_seconds == HISTOGRAM_BUCKETS_SECONDS
    assert first.dependency_duration_seconds["exchange"].count == 100
    assert first.errors_total[("/scan", "timeout")] == 1
    assert first.regime_source_total[("/regime/{symbol}", "hmm_fallback")] == 1


def test_controlled_benchmark_fail_open_rejects_bad_dependency_observations() -> None:
    dependency = ControlledDependency(latency_seconds=0.5)
    collector = LegacyReadPathMetrics()
    assert collector.observe_dependency("exchange", dependency.read())
    assert not collector.observe_dependency("unapproved_provider", 0.1)
    assert not collector.observe_request("/scan", "unknown", 0.1)
    assert not collector.observe_regime_source("/regime/{symbol}", "unknown_source")

    snapshot = collector.snapshot()
    assert dependency.calls == 1
    assert snapshot.dependency_duration_seconds["exchange"].count == 1
    assert snapshot.requests_total == {}
