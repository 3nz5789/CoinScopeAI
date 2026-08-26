from __future__ import annotations

import ast
from pathlib import Path

from engine.read_path_cache import (
    CacheOutcome,
    MarketCacheKey,
    MarketSnapshotCacheEntry,
    ReadPathCache,
)


ROOT = Path(__file__).resolve().parents[1]
CACHE_SOURCE = ROOT / "engine" / "read_path_cache.py"


def _tree() -> ast.Module:
    return ast.parse(CACHE_SOURCE.read_text(encoding="utf-8"))


def test_cache_module_imports_no_prohibited_runtime_modules() -> None:
    prohibited = {
        "ccxt",
        "fastapi",
        "fitz",
        "http",
        "numpy",
        "pandas",
        "psycopg2",
        "requests",
        "risk_management",
        "socket",
        "sqlalchemy",
        "subprocess",
        "torch",
        "urllib",
    }
    imported: set[str] = set()
    for node in ast.walk(_tree()):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])

    assert imported.isdisjoint(prohibited)


def test_cache_module_contains_no_prohibited_io_or_execution_hooks() -> None:
    prohibited_calls = {
        "connect",
        "create_connection",
        "execute",
        "fit",
        "open",
        "place_order",
        "run",
        "submit",
        "system",
        "write",
    }
    calls = {
        node.func.id
        for node in ast.walk(_tree())
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert calls.isdisjoint(prohibited_calls)
    assert not any(isinstance(node, ast.Attribute) and node.attr in prohibited_calls for node in ast.walk(_tree()))


def test_cache_outcomes_cannot_create_order_or_risk_execution_paths() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    key = MarketCacheKey("replay", "binance", "BTCUSDT", "1m", 10)
    cache.put(MarketSnapshotCacheEntry(key, ("bar",), 100.0, 5.0))

    for result in (cache.get(key, 101.0), cache.get(key, 105.0), cache.invalidate(key, CacheOutcome.circuit_open)):
        assert result.outcome in {CacheOutcome.fresh, CacheOutcome.stale, CacheOutcome.circuit_open}
        assert not hasattr(result, "submit")
        assert not hasattr(result, "execute")
        assert not hasattr(result, "fit")


def test_entries_are_process_local_and_in_memory_only() -> None:
    key = MarketCacheKey("replay", "binance", "BTCUSDT", "1m", 10)
    first: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    second: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    entry = MarketSnapshotCacheEntry(key, {"close": 100}, 100.0, 5.0)
    first.put(entry)

    assert first.get(key, 101.0).entry == entry
    assert second.get(key, 101.0).outcome is CacheOutcome.unavailable
    assert not any(name in dir(first) for name in ("save", "load", "persist", "filename", "fit"))
