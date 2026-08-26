from __future__ import annotations

from dataclasses import dataclass

from engine.monitoring.legacy_read_path_metrics import (
    LegacyReadPathMetric,
    LegacyReadPathMetrics,
    ReadPathMetricOutcome,
)


@dataclass
class ControlledDependency:
    """Deterministic dependency double used by the benchmark foundation."""

    latency_ms: float = 2.0
    calls: int = 0

    def read(self) -> tuple[str, float]:
        self.calls += 1
        return ("controlled-value", self.latency_ms)


def run_controlled_read_batch(
    dependency: ControlledDependency, count: int
) -> LegacyReadPathMetrics:
    """Record a fixed batch of reads against a dependency double."""

    collector = LegacyReadPathMetrics()
    for _ in range(count):
        _, latency_ms = dependency.read()
        collector.observe(
            LegacyReadPathMetric(
                operation="controlled_read",
                dependency="controlled_dependency",
                outcome=ReadPathMetricOutcome.FRESH,
                latency_ms=latency_ms,
            )
        )
    return collector


def test_controlled_dependency_benchmark_is_repeatable() -> None:
    first_dependency = ControlledDependency(latency_ms=2.0)
    second_dependency = ControlledDependency(latency_ms=2.0)

    first = run_controlled_read_batch(first_dependency, count=100).snapshot()
    second = run_controlled_read_batch(second_dependency, count=100).snapshot()

    assert first == second
    assert first_dependency.calls == 100
    assert second_dependency.calls == 100
    assert first.total == 100
    assert first.average_latency_ms == 2.0


def test_benchmark_controls_dependency_calls_and_does_not_hide_failures() -> None:
    dependency = ControlledDependency(latency_ms=7.5)
    collector = run_controlled_read_batch(dependency, count=3)

    snapshot = collector.snapshot()
    assert dependency.calls == 3
    assert snapshot.by_dependency == {"controlled_dependency": 3}
    assert snapshot.by_outcome == {ReadPathMetricOutcome.FRESH: 3}
    assert snapshot.total_latency_ms == 22.5
    assert snapshot.max_latency_ms == 7.5
