"""Binance WebSocket client for real-time market data streams."""
from __future__ import annotations
import asyncio
import json
import logging
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

class BinanceWebSocketClient:
    def __init__(self, base_url: str = "wss://stream.binance.com:9443", on_message: Optional[Callable] = None) -> None:
        self.base_url = base_url
        self.streams: list[str] = []
        self._on_message = on_message
        self._ws = None
        self._running = False
        self._task: Optional[asyncio.Task] = None

    def subscribe(self, stream: str) -> None:
        if stream not in self.streams:
            self.streams.append(stream)

    async def start(self) -> None:
        if not self.streams:
            return
        self._running = True
        self._task = asyncio.create_task(self._run_loop())

    async def stop(self) -> None:
        self._running = False
        if self._task and not self._task.done():
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass

    async def _run_loop(self) -> None:
        while self._running:
            try:
                await self._connect_and_listen()
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                logger.warning("[BinanceWS] Error: %s. Reconnecting in 5s...", exc)
                await asyncio.sleep(5.0)

    async def _connect_and_listen(self) -> None:
        try:
            import websockets
        except ImportError:
            logger.error("[BinanceWS] pip install websockets")
            await asyncio.sleep(10.0)
            return
        
        stream_path = "/".join(self.streams)
        url = f"{self.base_url}/ws/{stream_path}"
        
        async with websockets.connect(url) as ws:
            self._ws = ws
            async for message in ws:
                if not self._running:
                    break
                try:
                    payload = json.loads(message)
                    if self._on_message:
                        if asyncio.iscoroutinefunction(self._on_message):
                            await self._on_message(payload)
                        else:
                            self._on_message(payload)
                except json.JSONDecodeError:
                    pass
