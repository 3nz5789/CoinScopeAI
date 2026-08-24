"""Deterministic local market fixtures for Phase 1."""

from __future__ import annotations

from agent_os.contracts import DataProvenance, MarketEvent, MarketEventType


def btcusdt_fixture() -> list[MarketEvent]:
    """Return a tiny ordered event stream with no external dependencies."""
    return [
        MarketEvent(
            event_type=MarketEventType.TICKER,
            symbol="BTCUSDT",
            event_time=1_700_000_000.0,
            received_time=1_700_000_000.0,
            payload={"price": 40_000.0, "volume": 1.0},
            provider="phase1-fixture",
            provenance=DataProvenance.FIXTURE,
            sequence=1,
        ),
        MarketEvent(
            event_type=MarketEventType.FUNDING,
            symbol="BTCUSDT",
            event_time=1_700_000_001.0,
            received_time=1_700_000_001.0,
            payload={"funding_rate": -0.0001},
            provider="phase1-fixture",
            provenance=DataProvenance.FIXTURE,
            sequence=2,
        ),
        MarketEvent(
            event_type=MarketEventType.TICKER,
            symbol="BTCUSDT",
            event_time=1_700_000_002.0,
            received_time=1_700_000_002.0,
            payload={"price": 40_100.0, "volume": 1.2},
            provider="phase1-fixture",
            provenance=DataProvenance.FIXTURE,
            sequence=3,
        ),
    ]
