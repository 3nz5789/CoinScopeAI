"""Adapter that bridges Binance WebSocket stream data into the scanner pipeline."""
from __future__ import annotations
import logging
from typing import Any, Callable, Dict, Optional
from coinscope_trading_engine.data.binance_websocket import BinanceWebSocketClient
from coinscope_trading_engine.data.data_normalizer import DataNormalizer

logger = logging.getLogger(__name__)

class BinanceStreamAdapter:
    def __init__(self, ws_client=None, normalizer=None, on_depth=None, on_trade=None, on_kline=None) -> None:
        self.ws = ws_client or BinanceWebSocketClient()
        self.normalizer = normalizer or DataNormalizer()
        self._on_depth = on_depth
        self._on_trade = on_trade
        self._on_kline = on_kline
        self.ws._on_message = self._route_message

    async def _route_message(self, payload: Dict[str, Any]) -> None:
        event_type = payload.get("e", "")
        try:
            if event_type == "depthUpdate" and self._on_depth:
                self._on_depth(self.normalizer.normalize_order_book(payload))
            elif event_type == "aggTrade" and self._on_trade:
                self._on_trade(self.normalizer.normalize_trade(payload))
            elif event_type == "kline" and self._on_kline:
                self._on_kline(self.normalizer.normalize_kline(payload))
        except Exception as exc:
            logger.warning("[StreamAdapter] Error: %s", exc)

    def subscribe_depth(self, symbol: str) -> None:
        self.ws.subscribe(f"{symbol.lower()}@depth")

    def subscribe_trades(self, symbol: str) -> None:
        self.ws.subscribe(f"{symbol.lower()}@aggTrade")

    def subscribe_klines(self, symbol: str, interval: str = "1m") -> None:
        self.ws.subscribe(f"{symbol.lower()}@kline_{interval}")

    async def start(self) -> None:
        await self.ws.start()

    async def stop(self) -> None:
        await self.ws.stop()
