"""Normalized market-data contracts shared by live and replay adapters."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any


class MarketEventType(str, Enum):
    TICKER = "ticker"
    TRADE = "trade"
    ORDER_BOOK = "order_book"
    FUNDING = "funding"
    LIQUIDATION = "liquidation"
    OPEN_INTEREST = "open_interest"
    CANDLE = "candle"


class DataProvenance(str, Enum):
    FIXTURE = "fixture"
    REPLAY = "replay"
    LIVE = "live"


@dataclass(frozen=True)
class MarketEvent:
    """Provider-neutral event envelope; all timestamps are Unix seconds."""

    event_type: MarketEventType
    symbol: str
    event_time: float
    received_time: float
    payload: dict[str, Any]
    provider: str = "unknown"
    provenance: DataProvenance = DataProvenance.FIXTURE
    sequence: int | None = None

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["event_type"] = self.event_type.value
        value["provenance"] = self.provenance.value
        return value


@dataclass(frozen=True)
class DataStatus:
    """Truthful status for a provider or replay source."""

    provider: str
    state: str
    freshness_seconds: float | None
    last_event_time: float | None
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
