"""Normalizes raw exchange payloads into a unified internal schema."""
from __future__ import annotations
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class DataNormalizer:
    @staticmethod
    def normalize_order_book(raw: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "type": "order_book",
            "symbol": raw.get("s", "").upper(),
            "timestamp": raw.get("E"),
            "last_update_id": raw.get("u"),
            "bids": [[float(p), float(q)] for p, q in raw.get("b", [])],
            "asks": [[float(p), float(q)] for p, q in raw.get("a", [])],
        }

    @staticmethod
    def normalize_trade(raw: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "type": "trade",
            "symbol": raw.get("s", "").upper(),
            "timestamp": raw.get("T"),
            "price": float(raw.get("p", 0)),
            "quantity": float(raw.get("q", 0)),
            "is_buyer_maker": raw.get("m", False),
            "trade_id": raw.get("a"),
        }

    @staticmethod
    def normalize_kline(raw: Dict[str, Any]) -> Dict[str, Any]:
        k = raw.get("k", {})
        return {
            "type": "kline",
            "symbol": raw.get("s", "").upper(),
            "interval": k.get("i"),
            "open": float(k.get("o", 0)),
            "high": float(k.get("h", 0)),
            "low": float(k.get("l", 0)),
            "close": float(k.get("c", 0)),
            "volume": float(k.get("v", 0)),
            "timestamp": k.get("t"),
            "is_closed": k.get("x", False),
        }

    @staticmethod
    def normalize_ticker(raw: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "type": "ticker",
            "symbol": raw.get("symbol", "").upper(),
            "last_price": float(raw.get("lastPrice", 0)),
            "volume_24h": float(raw.get("volume", 0)),
            "change_percent_24h": float(raw.get("priceChangePercent", 0)),
            "timestamp": raw.get("closeTime"),
        }
