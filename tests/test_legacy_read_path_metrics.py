from __future__ import annotations

import ast
from pathlib import Path

from engine.monitoring.legacy_read_path_metrics import (
    DEPENDENCIES,
    ERROR_CLASSIFICATIONS,
    HISTOGRAM_BUCKETS_SECONDS,
    LEGACY_READ_DEPENDENCY_DURATION_SECONDS,
    LEGACY_READ_DURATION_SECONDS,
    LEGACY_READ_ERRORS_TOTAL,
    LEGACY_READ_REQUESTS_TOTAL,
    LEGACY_REGIME_SOURCE_TOTAL,
    METRIC_NAMES,
    REGIME_SOURCES,
    ROUTES,
    LegacyReadPathMetrics,
    ReadPathMetricOutcome,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "engine" / "monitoring" / "legacy_read_path_metrics.py"


def test_exact_metric_names_are_exposed_without_registration() -> None:
    assert METRIC_NAMES == (
        LEGACY_READ_REQUESTS_TOTAL,
        LEGACY_READ_DURATION_SECONDS,
        LEGACY_READ_DEPENDENCY_DURATION_SECONDS,
        LEGACY_READ_ERRORS_TOTAL,
        LEGACY_REGIME_SOURCE_TOTAL,
    )
    assert all(name.startswith("coinscopeai_") for name in METRIC_NAMES)


def test_outcome_vocabulary_preserves_all_approved_distinctions() -> None:
    assert tuple(outcome.value for outcome in ReadPathMetricOutcome) == (
        "fresh",
        "stale",
        "unavailable",
        "circuit_open",
        "model_unavailable",
    )


def test_route_and_dependency_histograms_are_second_based_and_fixed_bucketed() -> None:
    metrics = LegacyReadPathMetrics()
    assert metrics.observe_request("/scan", "fresh", 0.01)
    assert metrics.observe_request("/regime/{symbol}", "stale", 2.0)
    assert metrics.observe_dependency("exchange", 0.005)
    assert metrics.observe_dependency("model", 0.5)

    snapshot = metrics.snapshot()
    route_histogram = snapshot.duration_seconds["/scan"]
    dependency_histogram = snapshot.dependency_duration_seconds["exchange"]
    assert route_histogram.buckets_seconds == HISTOGRAM_BUCKETS_SECONDS
    assert route_histogram.bucket_counts == (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    assert route_histogram.count == 1
    assert route_histogram.total_seconds == 0.01
    assert dependency_histogram.bucket_counts[0] == 1
    assert dependency_histogram.total_seconds == 0.005


def test_errors_and_regime_sources_are_bounded_and_counted() -> None:
    metrics = LegacyReadPathMetrics()
    assert metrics.observe_request("/scan", "unavailable", 0.2, "timeout")
    assert metrics.observe_request("/regime/{symbol}", "circuit_open", 0.3, "rate_limited")
    assert metrics.observe_request("/regime/{symbol}", "model_unavailable", 0.4, "internal")
    assert metrics.observe_regime_source("/regime/{symbol}", "hmm_regime_v1")
    assert metrics.observe_regime_source("/regime/{symbol}", "hmm_fallback")
    assert metrics.observe_regime_source("/regime/{symbol}", "hmm_fallback")

    snapshot = metrics.snapshot()
    assert snapshot.errors_total == {
        ("/scan", "timeout"): 1,
        ("/regime/{symbol}", "rate_limited"): 1,
        ("/regime/{symbol}", "internal"): 1,
    }
    assert snapshot.regime_source_total == {
        ("/regime/{symbol}", "hmm_regime_v1"): 1,
        ("/regime/{symbol}", "hmm_fallback"): 2,
    }


def test_all_bounded_vocabulary_values_are_accepted() -> None:
    metrics = LegacyReadPathMetrics()
    for outcome in ReadPathMetricOutcome:
        assert metrics.observe_request("/scan", outcome, 0.0)
    for route in ROUTES:
        assert metrics.observe_request(route, "fresh", 0.0)
    for dependency in DEPENDENCIES:
        assert metrics.observe_dependency(dependency, 0.0)
    for error in ERROR_CLASSIFICATIONS:
        assert metrics.observe_request("/scan", "fresh", 0.0, error)
    for source in REGIME_SOURCES:
        assert metrics.observe_regime_source("/regime/{symbol}", source)


def test_invalid_unbounded_or_sensitive_values_fail_open() -> None:
    metrics = LegacyReadPathMetrics()
    assert not metrics.observe_request("/scan?symbol=BTCUSDT", "fresh", 0.1)
    assert not metrics.observe_request("/scan", "fresh", -0.1)
    assert not metrics.observe_request("/scan", "fresh", 0.1, "raw exception text")
    assert not metrics.observe_dependency("https://provider.example", 0.1)
    assert not metrics.observe_regime_source("/regime/BTCUSDT", "hmm_regime_v1")
    assert metrics.snapshot().requests_total == {}


def test_snapshot_is_detached_and_reset_is_local() -> None:
    metrics = LegacyReadPathMetrics()
    metrics.observe_request("/scan", "fresh", 0.1)
    first = metrics.snapshot()
    metrics.reset()
    assert first.requests_total == {"/scan": 1}
    assert metrics.snapshot().requests_total == {}


def test_contract_module_has_no_prohibited_imports_or_calls() -> None:
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    prohibited_modules = {
        "ccxt", "fastapi", "http", "numpy", "pandas", "psycopg2", "requests",
        "socket", "sqlalchemy", "subprocess", "torch", "urllib",
    }
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert imported.isdisjoint(prohibited_modules)
    prohibited_calls = {"connect", "execute", "fit", "open", "place_order", "run", "submit", "write"}
    assert not any(
        isinstance(node, ast.Attribute) and node.attr in prohibited_calls
        for node in ast.walk(tree)
    )
