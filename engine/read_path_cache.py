"""Pure in-memory contracts for bounded legacy read-path caches.

This module contains data contracts and a process-local cache only. It has no
filesystem, network, exchange, database, model-loading, execution, or risk
behavior.
"""

from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
from math import isfinite
from typing import Generic, TypeVar


class CacheOutcome(str, Enum):
    """Typed result states emitted by the cache."""

    fresh = "fresh"
    stale = "stale"
    unavailable = "unavailable"
    circuit_open = "circuit_open"
    model_unavailable = "model_unavailable"


FreshnessOutcome = CacheOutcome


@dataclass(frozen=True, slots=True)
class MarketCacheKey:
    source: str
    venue: str
    normalized_symbol: str
    timeframe: str
    bar_limit: int

    def __post_init__(self) -> None:
        _require_text(self.source, "source")
        _require_text(self.venue, "venue")
        _require_text(self.normalized_symbol, "normalized_symbol")
        _require_text(self.timeframe, "timeframe")
        if not isinstance(self.bar_limit, int) or isinstance(self.bar_limit, bool) or self.bar_limit <= 0:
            raise ValueError("bar_limit must be a positive integer")
        object.__setattr__(self, "source", self.source.strip().lower())
        object.__setattr__(self, "venue", self.venue.strip().lower())
        object.__setattr__(self, "normalized_symbol", self.normalized_symbol.strip().upper())
        object.__setattr__(self, "timeframe", self.timeframe.strip().lower())


@dataclass(frozen=True, slots=True)
class ModelCacheKey:
    source: str
    venue_or_none: str | None
    registry_symbol: str
    model_type: str
    feature_version: str
    model_version: str
    model_checksum: str

    def __post_init__(self) -> None:
        _require_text(self.source, "source")
        if self.venue_or_none is not None:
            _require_text(self.venue_or_none, "venue_or_none")
            object.__setattr__(self, "venue_or_none", self.venue_or_none.strip().lower())
        for field_name in (
            "registry_symbol",
            "model_type",
            "feature_version",
            "model_version",
            "model_checksum",
        ):
            value = getattr(self, field_name)
            _require_text(value, field_name)
            object.__setattr__(
                self,
                field_name,
                value.strip().upper() if field_name == "registry_symbol" else value.strip(),
            )
        object.__setattr__(self, "source", self.source.strip().lower())


@dataclass(frozen=True, slots=True)
class MarketSnapshotCacheEntry:
    key: MarketCacheKey
    snapshot: object
    stored_at: float
    ttl_seconds: float

    def __post_init__(self) -> None:
        _validate_clock_values(self.stored_at, self.ttl_seconds)


@dataclass(frozen=True, slots=True)
class ModelCacheEntry:
    key: ModelCacheKey
    model: object
    stored_at: float
    ttl_seconds: float

    def __post_init__(self) -> None:
        _validate_clock_values(self.stored_at, self.ttl_seconds)


Entry = TypeVar("Entry", MarketSnapshotCacheEntry, ModelCacheEntry)


@dataclass(frozen=True, slots=True)
class CacheResult(Generic[Entry]):
    """Typed cache outcome; cache-state callers never receive raw ``None``."""

    outcome: CacheOutcome
    entry: Entry | None = None
    reason: str | None = None


class ReadPathCache(Generic[Entry]):
    """Bounded insertion-order in-memory cache for market and model entries."""

    def __init__(self, max_entries: int = 128) -> None:
        if not isinstance(max_entries, int) or isinstance(max_entries, bool) or max_entries <= 0:
            raise ValueError("max_entries must be a positive integer")
        self._entries: OrderedDict[MarketCacheKey | ModelCacheKey, Entry] = OrderedDict()
        self._invalidated: dict[MarketCacheKey | ModelCacheKey, CacheResult[Entry]] = {}
        self._max_entries = max_entries

    def get(
        self,
        key: MarketCacheKey | ModelCacheKey,
        now: float,
    ) -> CacheResult[Entry]:
        """Return a typed fresh, stale, unavailable, or model-unavailable result."""

        _validate_key(key)
        _validate_now(now)
        invalidated = self._invalidated.get(key)
        if invalidated is not None:
            return invalidated
        entry = self._entries.get(key)
        if entry is None:
            outcome = (
                CacheOutcome.model_unavailable
                if isinstance(key, ModelCacheKey)
                else CacheOutcome.unavailable
            )
            return CacheResult(outcome=outcome)
        self._entries.move_to_end(key)
        outcome = CacheOutcome.fresh if now < entry.stored_at + entry.ttl_seconds else CacheOutcome.stale
        return CacheResult(outcome=outcome, entry=entry)

    def put(self, entry: Entry) -> CacheResult[Entry]:
        """Insert or replace an entry and return its typed fresh result."""

        _validate_entry(entry)
        self._invalidated.pop(entry.key, None)
        self._entries[entry.key] = entry
        self._entries.move_to_end(entry.key)
        while len(self._entries) > self._max_entries:
            self._entries.popitem(last=False)
        return CacheResult(outcome=CacheOutcome.fresh, entry=entry)

    def invalidate(
        self,
        key: MarketCacheKey | ModelCacheKey,
        reason: CacheOutcome | str = CacheOutcome.unavailable,
    ) -> CacheResult[Entry]:
        """Remove a key and retain a typed invalidation outcome until replaced."""

        _validate_key(key)
        explanation: str | None = None
        if isinstance(reason, CacheOutcome):
            outcome = reason
        elif reason in {outcome.value for outcome in CacheOutcome}:
            outcome = CacheOutcome(reason)
        else:
            outcome = (
                CacheOutcome.model_unavailable
                if isinstance(key, ModelCacheKey)
                else CacheOutcome.unavailable
            )
            explanation = reason
        if outcome is CacheOutcome.fresh or outcome is CacheOutcome.stale:
            raise ValueError("invalidate reason must describe an unavailable state")
        self._entries.pop(key, None)
        result: CacheResult[Entry] = CacheResult(outcome=outcome, reason=explanation)
        self._invalidated[key] = result
        return result

    def clear(self) -> None:
        """Clear entries and invalidation outcomes from this cache instance."""

        self._entries.clear()
        self._invalidated.clear()

    def __len__(self) -> int:
        return len(self._entries)


def _require_text(value: object, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _validate_now(now: float) -> None:
    if not isinstance(now, (int, float)) or isinstance(now, bool) or not isfinite(now):
        raise ValueError("now must be a finite numeric clock value")


def _validate_clock_values(stored_at: float, ttl_seconds: float) -> None:
    _validate_now(stored_at)
    if not isinstance(ttl_seconds, (int, float)) or isinstance(ttl_seconds, bool):
        raise ValueError("ttl_seconds must be numeric")
    if not isfinite(ttl_seconds) or ttl_seconds < 0:
        raise ValueError("ttl_seconds must be finite and non-negative")


def _validate_key(key: object) -> None:
    if not isinstance(key, (MarketCacheKey, ModelCacheKey)):
        raise TypeError("key must be a MarketCacheKey or ModelCacheKey")


def _validate_entry(entry: object) -> None:
    if not isinstance(entry, (MarketSnapshotCacheEntry, ModelCacheEntry)):
        raise TypeError("entry must be a MarketSnapshotCacheEntry or ModelCacheEntry")


__all__ = [
    "CacheOutcome",
    "CacheResult",
    "FreshnessOutcome",
    "MarketCacheKey",
    "MarketSnapshotCacheEntry",
    "ModelCacheEntry",
    "ModelCacheKey",
    "ReadPathCache",
]
