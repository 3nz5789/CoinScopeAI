"""Binance REST client for historical and snapshot market data."""
from __future__ import annotations
import logging
from typing import Any, Dict, List, Optional
import requests
from coinscope_trading_engine.core.config import BinanceConfig, EngineConfig

logger = logging.getLogger(__name__)

class BinanceRESTClient:
    def __init__(self, config: Optional[BinanceConfig] = None) -> None:
        self.config = config or EngineConfig.from_env().binance
        self._session = requests.Session()
        self._base_url = self.config.base_url

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self._base_url}{path}"
        response = self._session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def ping(self) -> bool:
        try:
            self._get("/api/v3/ping")
            return True
        except Exception as exc:
            logger.warning("[BinanceREST] Ping failed: %s", exc)
            return False

    def get_order_book(self, symbol: str, limit: int = 100) -> Dict[str, Any]:
        return self._get("/api/v3/depth", {"symbol": symbol.upper(), "limit": limit})

    def get_recent_trades(self, symbol: str, limit: int = 100) -> List[Dict[str, Any]]:
        return self._get("/api/v3/trades", {"symbol": symbol.upper(), "limit": limit})

    def get_klines(self, symbol: str, interval: str = "1m", limit: int = 100) -> List[List[Any]]:
        return self._get("/api/v3/klines", {"symbol": symbol.upper(), "interval": interval, "limit": limit})

    def get_exchange_info(self) -> Dict[str, Any]:
        return self._get("/api/v3/exchangeInfo")
