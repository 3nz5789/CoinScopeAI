from __future__ import annotations

from engine.read_path_cache import (
    CacheOutcome,
    MarketCacheKey,
    MarketSnapshotCacheEntry,
    ModelCacheEntry,
    ModelCacheKey,
    ReadPathCache,
)


def market_key(**changes: object) -> MarketCacheKey:
    values: dict[str, object] = {
        "source": "replay",
        "venue": "binance",
        "normalized_symbol": "BTCUSDT",
        "timeframe": "1m",
        "bar_limit": 100,
    }
    values.update(changes)
    return MarketCacheKey(**values)  # type: ignore[arg-type]


def model_key(**changes: object) -> ModelCacheKey:
    values: dict[str, object] = {
        "source": "registry",
        "venue_or_none": "binance",
        "registry_symbol": "BTCUSDT",
        "model_type": "hmm",
        "feature_version": "features-v1",
        "model_version": "model-v1",
        "model_checksum": "sha256:abc",
    }
    values.update(changes)
    return ModelCacheKey(**values)  # type: ignore[arg-type]


def market_entry(key: MarketCacheKey, stored_at: float = 100.0) -> MarketSnapshotCacheEntry:
    return MarketSnapshotCacheEntry(key, ("bar",), stored_at, 10.0)


def model_entry(key: ModelCacheKey, stored_at: float = 100.0) -> ModelCacheEntry:
    return ModelCacheEntry(key, object(), stored_at, 10.0)


def test_market_key_isolation_across_all_canonical_dimensions() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    base = market_key()
    cache.put(market_entry(base))

    for field, value in (
        ("source", "live"),
        ("venue", "bybit"),
        ("normalized_symbol", "ETHUSDT"),
        ("timeframe", "5m"),
        ("bar_limit", 200),
    ):
        result = cache.get(market_key(**{field: value}), now=105.0)
        assert result.outcome is CacheOutcome.unavailable
        assert result.entry is None


def test_model_key_isolation_across_all_canonical_dimensions() -> None:
    cache: ReadPathCache[ModelCacheEntry] = ReadPathCache()
    base = model_key()
    cache.put(model_entry(base))

    for field, value in (
        ("source", "artifact"),
        ("venue_or_none", None),
        ("registry_symbol", "ETHUSDT"),
        ("model_type", "xgboost"),
        ("feature_version", "features-v2"),
        ("model_version", "model-v2"),
        ("model_checksum", "sha256:def"),
    ):
        result = cache.get(model_key(**{field: value}), now=105.0)
        assert result.outcome is CacheOutcome.model_unavailable
        assert result.entry is None


def test_fresh_and_expired_results_use_fixed_clock() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    key = market_key()
    entry = market_entry(key, stored_at=100.0)
    cache.put(entry)

    fresh = cache.get(key, now=109.999)
    expired = cache.get(key, now=110.0)

    assert fresh.outcome is CacheOutcome.fresh
    assert fresh.entry == entry
    assert expired.outcome is CacheOutcome.stale
    assert expired.entry == entry


def test_typed_unavailable_states_are_distinct_and_not_raw_none() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    missing_market = cache.get(market_key(), now=100.0)
    missing_model = ReadPathCache[ModelCacheEntry]().get(model_key(), now=100.0)
    circuit = cache.invalidate(market_key(), CacheOutcome.circuit_open)

    assert missing_market.outcome is CacheOutcome.unavailable
    assert missing_model.outcome is CacheOutcome.model_unavailable
    assert circuit.outcome is CacheOutcome.circuit_open
    assert all(result is not None for result in (missing_market, missing_model, circuit))


def test_invalidate_replaces_read_with_typed_reason_until_replacement() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    key = market_key()
    cache.put(market_entry(key))

    invalidated = cache.invalidate(key, "stale upstream")
    result = cache.get(key, now=101.0)
    cache.put(market_entry(key, stored_at=101.0))
    replaced = cache.get(key, now=102.0)

    assert invalidated.outcome is CacheOutcome.unavailable
    assert invalidated.reason == "stale upstream"
    assert result.outcome is CacheOutcome.unavailable
    assert replaced.outcome is CacheOutcome.fresh


def test_clear_removes_entries_and_invalidation_outcomes() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache()
    key = market_key()
    cache.put(market_entry(key))
    cache.invalidate(key, CacheOutcome.circuit_open)
    cache.clear()

    result = cache.get(key, now=100.0)
    assert len(cache) == 0
    assert result.outcome is CacheOutcome.unavailable


def test_replacement_does_not_grow_cache() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache(max_entries=2)
    key = market_key()
    cache.put(market_entry(key, stored_at=100.0))
    cache.put(market_entry(key, stored_at=101.0))

    assert len(cache) == 1
    assert cache.get(key, now=102.0).entry == market_entry(key, stored_at=101.0)


def test_bounded_insertion_order_eviction_is_deterministic() -> None:
    cache: ReadPathCache[MarketSnapshotCacheEntry] = ReadPathCache(max_entries=2)
    first, second, third = market_key(), market_key(normalized_symbol="ETHUSDT"), market_key(normalized_symbol="SOLUSDT")
    cache.put(market_entry(first))
    cache.put(market_entry(second))
    cache.put(market_entry(third))

    assert len(cache) == 2
    assert cache.get(first, now=101.0).outcome is CacheOutcome.unavailable
    assert cache.get(second, now=101.0).outcome is CacheOutcome.fresh
    assert cache.get(third, now=101.0).outcome is CacheOutcome.fresh
