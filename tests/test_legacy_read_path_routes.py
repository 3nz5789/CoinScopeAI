from __future__ import annotations

import sys
import types
from dataclasses import dataclass
from datetime import datetime, timezone
from types import SimpleNamespace

import pandas as pd
import pytest
from fastapi import HTTPException

import engine.api as api
from engine.monitoring.legacy_read_path_metrics import ReadPathMetricOutcome


@dataclass
class RecordingMetrics:
    requests: list[tuple] 
    dependencies: list[tuple]
    sources: list[tuple]

    def observe_request(self, *args):
        self.requests.append(args)
        return True

    def observe_dependency(self, *args):
        self.dependencies.append(args)
        return True

    def observe_regime_source(self, *args):
        self.sources.append(args)
        return True


@pytest.fixture
def recording_metrics(monkeypatch):
    collector = RecordingMetrics([], [], [])
    monkeypatch.setattr(api, "legacy_read_metrics", collector)
    monkeypatch.setattr(api.time, "time", lambda: 123.0)
    return collector


class FakeExchange:
    def __init__(self, rows):
        self.rows = rows
        self.calls = []

    def fetch_ohlcv(self, symbol, timeframe, limit):
        self.calls.append((symbol, timeframe, limit))
        return self.rows


def _bars(count: int = 60):
    return [
        [i * 60_000, 100.0 + i, 101.0 + i, 99.0 + i, 100.5 + i, 10.0]
        for i in range(count)
    ]


def _prediction():
    return SimpleNamespace(
        symbol="BTCUSDT",
        label="Trending",
        confidence=0.75,
        state_probs=[0.75, 0.1, 0.1, 0.05],
        state_labels=["Trending", "Mean-Reverting", "Volatile", "Quiet"],
        model_version="v1",
        trained_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        val_accuracy=0.8,
    )


@pytest.mark.asyncio
async def test_scan_success_preserves_response_shape_and_emits_one_request(monkeypatch, recording_metrics):
    class FakeOrchestrator:
        def __init__(self, pairs):
            assert pairs == ["BTC/USDT"]

        def run_scan(self):
            return [{"symbol": "BTC/USDT", "signal": "LONG"}]

    fake_module = types.ModuleType("engine.core.master_orchestrator")
    fake_module.CoinScopeOrchestrator = FakeOrchestrator
    monkeypatch.setitem(sys.modules, "engine.core.master_orchestrator", fake_module)

    response = await api.scan("BTC/USDT")

    assert response == {
        "signals": [{"symbol": "BTC/USDT", "signal": "LONG"}],
        "active_count": 1,
        "total_scanned": 1,
        "timestamp": 123.0,
    }
    assert len(recording_metrics.requests) == 1
    route, outcome, duration, error = recording_metrics.requests[0]
    assert route == "/scan"
    assert outcome is ReadPathMetricOutcome.FRESH
    assert duration >= 0
    assert error is None
    assert recording_metrics.dependencies == []


@pytest.mark.asyncio
async def test_scan_exception_and_observer_failure_preserve_http_behavior(monkeypatch):
    class FakeOrchestrator:
        def __init__(self, pairs):
            pass

        def run_scan(self):
            raise ValueError("scan failed")

    fake_module = types.ModuleType("engine.core.master_orchestrator")
    fake_module.CoinScopeOrchestrator = FakeOrchestrator
    monkeypatch.setitem(sys.modules, "engine.core.master_orchestrator", fake_module)

    class FailingMetrics:
        def observe_request(self, *args):
            raise RuntimeError("metrics failed")

        def observe_dependency(self, *args):
            raise RuntimeError("metrics failed")

        def observe_regime_source(self, *args):
            raise RuntimeError("metrics failed")

    monkeypatch.setattr(api, "legacy_read_metrics", FailingMetrics())

    with pytest.raises(HTTPException) as exc_info:
        await api.scan("BTC/USDT")
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "scan failed"


@pytest.mark.asyncio
async def test_regime_primary_preserves_body_and_records_exchange_model_and_source(
    monkeypatch, recording_metrics
):
    exchange = FakeExchange(_bars(2))
    fake_ccxt = types.ModuleType("ccxt")
    fake_ccxt.binance = lambda options: exchange
    monkeypatch.setitem(sys.modules, "ccxt", fake_ccxt)
    monkeypatch.setattr(api.regime_predictor, "predict", lambda symbol, frame: _prediction())

    response = await api.get_regime("btc-usdt")

    assert response == {
        "symbol": "BTCUSDT",
        "label": "Trending",
        "confidence": 0.75,
        "state_probs": [0.75, 0.1, 0.1, 0.05],
        "state_labels": ["Trending", "Mean-Reverting", "Volatile", "Quiet"],
        "source": "hmm_regime_v1",
        "model_version": "v1",
        "trained_at": "2026-01-01T00:00:00+00:00",
        "val_accuracy": 0.8,
        "price": 101.5,
        "timestamp": 123.0,
    }
    assert exchange.calls == [("BTC/USDT", "1h", 500)]
    assert len(recording_metrics.requests) == 1
    assert recording_metrics.requests[0][0:2] == ("/regime/{symbol}", ReadPathMetricOutcome.FRESH)
    assert [item[0] for item in recording_metrics.dependencies] == ["exchange", "model"]
    assert recording_metrics.sources == [("/regime/{symbol}", "hmm_regime_v1")]


@pytest.mark.asyncio
async def test_regime_model_unavailable_uses_existing_fallback_and_records_fallback_exchange(
    monkeypatch, recording_metrics
):
    primary_exchange = FakeExchange(_bars(2))
    fallback_exchange = FakeExchange(_bars(60))
    exchanges = iter([primary_exchange, fallback_exchange])
    fake_ccxt = types.ModuleType("ccxt")
    fake_ccxt.binance = lambda options: next(exchanges)
    monkeypatch.setitem(sys.modules, "ccxt", fake_ccxt)
    monkeypatch.setattr(api.regime_predictor, "predict", lambda symbol, frame: None)

    class FakeDetector:
        def fit(self, returns, vol):
            return None

        def predict_regime(self, returns, vol):
            return {"regime": "bull", "confidence": 0.7}

    fake_detector = types.ModuleType("risk_management.hmm_regime_detector")
    fake_detector.EnsembleRegimeDetector = FakeDetector
    monkeypatch.setitem(sys.modules, "risk_management.hmm_regime_detector", fake_detector)

    response = await api.get_regime("BTC/USDT")

    assert response["source"] == "hmm_fallback"
    assert response["symbol"] == "BTCUSDT"
    assert response["timestamp"] == 123.0
    assert primary_exchange.calls == [("BTC/USDT", "1h", 500)]
    assert fallback_exchange.calls == [("BTC/USDT", "4h", 200)]
    assert len(recording_metrics.requests) == 1
    assert recording_metrics.requests[0][1] is ReadPathMetricOutcome.MODEL_UNAVAILABLE
    assert [item[0] for item in recording_metrics.dependencies] == ["exchange", "model", "exchange"]
    assert recording_metrics.sources == [("/regime/{symbol}", "hmm_fallback")]


@pytest.mark.asyncio
async def test_regime_failure_preserves_http_behavior_and_emits_one_unavailable_request(
    monkeypatch, recording_metrics
):
    class FailingExchange:
        def fetch_ohlcv(self, symbol, timeframe, limit):
            raise RuntimeError("provider failed")

    fake_ccxt = types.ModuleType("ccxt")
    fake_ccxt.binance = lambda options: FailingExchange()
    monkeypatch.setitem(sys.modules, "ccxt", fake_ccxt)

    with pytest.raises(HTTPException) as exc_info:
        await api.get_regime("BTC/USDT")
    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "provider failed"
    assert len(recording_metrics.requests) == 1
    assert recording_metrics.requests[0][1] is ReadPathMetricOutcome.UNAVAILABLE
    assert recording_metrics.requests[0][3] == "internal"


@pytest.mark.asyncio
async def test_observers_are_fail_open_for_regime_success(monkeypatch):
    monkeypatch.setattr(api.time, "time", lambda: 123.0)
    exchange = FakeExchange(_bars(2))
    fake_ccxt = types.ModuleType("ccxt")
    fake_ccxt.binance = lambda options: exchange
    monkeypatch.setitem(sys.modules, "ccxt", fake_ccxt)
    monkeypatch.setattr(api.regime_predictor, "predict", lambda symbol, frame: _prediction())

    class FailingMetrics:
        def observe_request(self, *args):
            raise RuntimeError("request metric failed")

        def observe_dependency(self, *args):
            raise RuntimeError("dependency metric failed")

        def observe_regime_source(self, *args):
            raise RuntimeError("source metric failed")

    monkeypatch.setattr(api, "legacy_read_metrics", FailingMetrics())
    response = await api.get_regime("BTC/USDT")
    assert response["source"] == "hmm_regime_v1"
    assert response["timestamp"] == 123.0


def test_routes_use_only_approved_outcomes_and_no_reserved_emission():
    assert ReadPathMetricOutcome.FRESH.value == "fresh"
    assert ReadPathMetricOutcome.MODEL_UNAVAILABLE.value == "model_unavailable"
    assert ReadPathMetricOutcome.STALE.value == "stale"
    assert ReadPathMetricOutcome.CIRCUIT_OPEN.value == "circuit_open"


@pytest.mark.asyncio
async def test_regime_normalization_failure_preserves_exception_and_observes_once(
    monkeypatch, recording_metrics
):
    def fail_normalization(symbol):
        raise ValueError("invalid symbol")

    monkeypatch.setattr(api, "_normalise_symbols", fail_normalization)

    with pytest.raises(ValueError, match="invalid symbol"):
        await api.get_regime("not-a-symbol")

    assert len(recording_metrics.requests) == 1
    route, outcome, duration, error = recording_metrics.requests[0]
    assert route == "/regime/{symbol}"
    assert outcome is ReadPathMetricOutcome.UNAVAILABLE
    assert duration >= 0
    assert error == "internal"
    assert recording_metrics.dependencies == []
    assert recording_metrics.sources == []
