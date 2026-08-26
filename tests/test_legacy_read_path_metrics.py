from __future__ import annotations

import ast
from pathlib import Path

import pytest

from engine.monitoring.legacy_read_path_metrics import (
    LegacyReadPathMetric,
    LegacyReadPathMetrics,
    ReadPathMetricOutcome,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "engine" / "monitoring" / "legacy_read_path_metrics.py"


def metric(
    operation: str = "market_snapshot",
    dependency: str = "exchange",
    outcome: ReadPathMetricOutcome = ReadPathMetricOutcome.FRESH,
    latency_ms: float = 10.0,
) -> LegacyReadPathMetric:
    return LegacyReadPathMetric(operation, dependency, outcome, latency_ms)


def test_observation_aggregates_by_operation_dependency_and_outcome() -> None:
    collector = LegacyReadPathMetrics()
    collector.extend(
        (
            metric(latency_ms=10.0),
            metric(latency_ms=20.0),
            metric(dependency="cache", outcome=ReadPathMetricOutcome.STALE, latency_ms=5.0),
        )
    )

    snapshot = collector.snapshot()
    assert snapshot.total == 3
    assert snapshot.by_operation == {"market_snapshot": 3}
    assert snapshot.by_dependency == {"exchange": 2, "cache": 1}
    assert snapshot.by_outcome == {
        ReadPathMetricOutcome.FRESH: 2,
        ReadPathMetricOutcome.STALE: 1,
    }
    assert snapshot.total_latency_ms == 35.0
    assert snapshot.max_latency_ms == 20.0
    assert snapshot.average_latency_ms == pytest.approx(35.0 / 3.0)


def test_snapshot_is_detached_from_later_observations() -> None:
    collector = LegacyReadPathMetrics()
    collector.observe(metric())
    first = collector.snapshot()
    collector.observe(metric(operation="regime", outcome=ReadPathMetricOutcome.UNAVAILABLE))

    assert first.total == 1
    assert first.by_operation == {"market_snapshot": 1}
    assert collector.snapshot().total == 2


def test_reset_clears_only_the_process_local_collector() -> None:
    collector = LegacyReadPathMetrics()
    collector.observe(metric())
    collector.reset()

    snapshot = collector.snapshot()
    assert snapshot.total == 0
    assert snapshot.average_latency_ms == 0.0
    assert snapshot.by_operation == {}
    assert snapshot.by_dependency == {}
    assert snapshot.by_outcome == {}


@pytest.mark.parametrize(
    "kwargs",
    (
        {"operation": ""},
        {"dependency": " "},
        {"latency_ms": -1.0},
        {"latency_ms": float("inf")},
    ),
)
def test_invalid_observations_are_rejected(kwargs: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        metric(**kwargs)  # type: ignore[arg-type]


def test_contract_module_has_no_external_or_execution_dependencies() -> None:
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    prohibited_modules = {
        "ccxt",
        "fastapi",
        "http",
        "numpy",
        "pandas",
        "psycopg2",
        "requests",
        "socket",
        "subprocess",
        "torch",
        "urllib",
    }
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert imported.isdisjoint(prohibited_modules)
    assert not any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"connect", "execute", "open", "run", "submit", "write"}
        for node in ast.walk(tree)
    )
