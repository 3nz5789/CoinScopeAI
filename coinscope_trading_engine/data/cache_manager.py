"""Cache manager for persisting normalized market data."""
from __future__ import annotations
import json
import logging
from typing import Any, Dict, Optional
from coinscope_trading_engine.core.config import EngineConfig
from coinscope_trading_engine.core.redis_client import ResilientRedisClient

logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self, config: Optional[EngineConfig] = None) -> None:
        self.config = config or EngineConfig.from_env()
        self.redis = ResilientRedisClient(self.config.redis)
        self._memory: Dict[str, Any] = {}
        self._redis_ready = self.redis.connect()

    def set(self, key: str, value: Any, ttl: int = 60) -> bool:
        try:
            serialized = json.dumps(value)
        except (TypeError, ValueError):
            serialized = str(value)

        if self._redis_ready and not self.redis.is_degraded:
            try:
                return self.redis.set(key, serialized, ex=ttl)
            except Exception:
                pass
        
        self._memory[key] = value
        return True

    def get(self, key: str) -> Optional[Any]:
        if self._redis_ready and not self.redis.is_degraded:
            raw = self.redis.get(key)
            if raw is not None:
                try:
                    return json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    return raw
        return self._memory.get(key)

    def hset(self, name: str, key: str, value: Any) -> bool:
        if self._redis_ready and not self.redis.is_degraded:
            try:
                return self.redis.hset(name, key, json.dumps(value) if not isinstance(value, str) else value)
            except Exception:
                pass
        
        if name not in self._memory:
            self._memory[name] = {}
        self._memory[name][key] = value
        return True

    def hgetall(self, name: str) -> Dict[str, Any]:
        if self._redis_ready and not self.redis.is_degraded:
            raw = self.redis.hgetall(name)
            if raw:
                return {k: json.loads(v) if isinstance(v, str) else v for k, v in raw.items()}
        
        entry = self._memory.get(name)
        if isinstance(entry, dict):
            return entry
        return {}
