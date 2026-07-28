"""High-level market stream that orchestrates WebSocket + REST for live data."""
from __future__ import annotations
import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional
from coinscope_trading_engine.data.binance_rest import BinanceRESTClient
from coinscope_trading_engine.data.binance_stream_adapter import BinanceStreamAdapter
from coinscope_trading_engine.data.cache_manager import CacheManager

logger = logging.getLogger(__name__)

class MarketStream:
    def __init__(self, rest_client=None, stream_adapter=None, cache=None) -> None:
        self.rest = rest_client or BinanceRESTClient()
        self.adapter = stream_adapter or BinanceStreamAdapter()
        self.cache = cache or CacheManager()
        self._handlers: List[Callable] = []
        self._running = False

    def add_handler(self, handler: Callable) -> None:
        self._handlers.append(handler)

    async def _on_event(self, event: Dict[str, Any]) -> None:
        symbol = event.get("symbol", "UNKNOWN")
        event_type = event.get("type", "unknown")
        self.cache.set(f"stream:{symbol}:{event_type}", event, ttl=30)
        
        for handler in self._handlers:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler(event)
                else:
                    handler(event)
            except Exception as exc:
                logger.warning("[MarketStream] Handler error: %s", exc)

    async def subscribe_symbol(self, symbol: str) -> None:
        self.adapter.subscribe_depth(symbol)
        self.adapter.subscribe_trades(symbol)
        self.adapter.subscribe_klines(symbol)
        logger.info("[MarketStream] Subscribed to %s", symbol.upper())

    async def start(self) -> None:
        self._running = True
        self.adapter._on_depth = self._on_event
        self.adapter._on_trade = self._on_event
        self.adapter._on_kline = self._on_event
        await self.adapter.start()

    async def stop(self) -> None:
        self._running = False
        await self.adapter.stop()
        logger.info("[MarketStream] Stopped.")
