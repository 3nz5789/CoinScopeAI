"""CoinScopeAI Data Pipeline package."""
from coinscope_trading_engine.data.binance_rest import BinanceRESTClient
from coinscope_trading_engine.data.binance_websocket import BinanceWebSocketClient
from coinscope_trading_engine.data.cache_manager import CacheManager
from coinscope_trading_engine.data.data_normalizer import DataNormalizer
from coinscope_trading_engine.data.market_stream import MarketStream

__all__ = [
    "BinanceRESTClient",
    "BinanceWebSocketClient", 
    "CacheManager",
    "DataNormalizer",
    "MarketStream",
]
