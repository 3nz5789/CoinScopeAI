#!/usr/bin/env python3
"""
Kronos × Binance integration script.

Fetches recent Binance Futures klines for a symbol, formats them into the
Kronos predictor input schema, loads a Kronos model from Hugging Face, and
emits an OHLCV forecast.

This script is intentionally self-contained and runs in its own virtual
environment (see requirements.txt) so that the heavy torch/huggingface
dependencies do not leak into the main CoinScopeAI engine venv.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import requests

# ── Add vendored Kronos source to the path ────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[2]
KRONOS_ROOT = REPO_ROOT / "external" / "Kronos"
if str(KRONOS_ROOT) not in sys.path:
    sys.path.insert(0, str(KRONOS_ROOT))

from model import Kronos, KronosPredictor, KronosTokenizer  # noqa: E402

# ── Defaults ──────────────────────────────────────────────────────────────
DEFAULT_SYMBOL = "BTCUSDT"
DEFAULT_INTERVAL = "5m"          # K-line interval
DEFAULT_LOOKBACK = 120           # historical candles fed to Kronos (<=512 for small/base)
DEFAULT_PRED_LEN = 12            # candles to forecast
DEFAULT_MODEL = "NeoQuasar/Kronos-small"
DEFAULT_TOKENIZER = "NeoQuasar/Kronos-Tokenizer-base"
DEFAULT_HF_CACHE = str(REPO_ROOT / ".cache" / "kronos")

# Binance endpoints (testnet by default to avoid rate limits / accidents)
BINANCE_REST_URL = os.getenv("BINANCE_REST_URL", "https://demo-fapi.binance.com")


def fetch_klines(
    symbol: str,
    interval: str,
    limit: int,
    end_time: datetime | None = None,
) -> pd.DataFrame:
    """
    Fetch Binance Futures klines and return a DataFrame.

    Columns follow the Kronos predictor convention:
        open, high, low, close, volume, amount, timestamps
    """
    url = f"{BINANCE_REST_URL}/fapi/v1/klines"
    params: dict = {"symbol": symbol.upper(), "interval": interval, "limit": limit}
    if end_time is not None:
        params["endTime"] = int(end_time.timestamp() * 1000)

    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    if not data:
        raise ValueError(f"No klines returned for {symbol} @ {interval}")

    # Binance kline fields:
    # 0 open_time, 1 open, 2 high, 3 low, 4 close, 5 volume,
    # 6 close_time, 7 quote_asset_volume, 8 trades, ...
    df = pd.DataFrame(
        data,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "amount",
            "trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore",
        ],
    )

    numeric_cols = ["open", "high", "low", "close", "volume", "amount"]
    df[numeric_cols] = df[numeric_cols].astype(float)
    df["timestamps"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)

    return df[["open", "high", "low", "close", "volume", "amount", "timestamps"]]


def build_forecast_timestamps(
    last_timestamp: pd.Timestamp,
    pred_len: int,
    interval: str,
) -> pd.Series:
    """Generate future timestamps matching the requested prediction length."""
    # Map common Binance intervals to pandas offsets
    interval_map = {
        "1m": "1min",
        "3m": "3min",
        "5m": "5min",
        "15m": "15min",
        "30m": "30min",
        "1h": "1h",
        "2h": "2h",
        "4h": "4h",
        "6h": "6h",
        "8h": "8h",
        "12h": "12h",
        "1d": "1d",
        "3d": "3d",
        "1w": "1W",
    }
    freq = interval_map.get(interval, interval)
    future = pd.date_range(
        start=last_timestamp + pd.Timedelta(freq),
        periods=pred_len,
        freq=freq,
        tz="UTC",
    )
    return pd.Series(future)


def run_forecast(args: argparse.Namespace) -> pd.DataFrame:
    """End-to-end Kronos forecast on Binance futures data."""
    os.environ.setdefault("HF_HOME", args.hf_cache)
    os.environ.setdefault("HUGGINGFACE_HUB_CACHE", args.hf_cache)

    print(f"Fetching {args.lookback} klines for {args.symbol} @ {args.interval}")
    df = fetch_klines(args.symbol, args.interval, args.lookback)
    print(f"  Range: {df['timestamps'].iloc[0]} → {df['timestamps'].iloc[-1]}")

    print(f"Loading tokenizer: {args.tokenizer}")
    tokenizer = KronosTokenizer.from_pretrained(args.tokenizer, cache_dir=args.hf_cache)

    print(f"Loading model: {args.model}")
    model = Kronos.from_pretrained(args.model, cache_dir=args.hf_cache)

    predictor = KronosPredictor(model, tokenizer, max_context=args.max_context)

    y_timestamp = build_forecast_timestamps(
        df["timestamps"].iloc[-1], args.pred_len, args.interval
    )

    print(f"Running forecast for {args.pred_len} candles...")
    pred_df = predictor.predict(
        df=df[["open", "high", "low", "close", "volume", "amount"]],
        x_timestamp=df["timestamps"],
        y_timestamp=y_timestamp,
        pred_len=args.pred_len,
        T=args.temperature,
        top_p=args.top_p,
        sample_count=args.sample_count,
    )

    pred_df.insert(0, "timestamp", y_timestamp.values)
    return pred_df


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Kronos price forecasts on Binance Futures data."
    )
    parser.add_argument("--symbol", default=DEFAULT_SYMBOL, help="Binance futures symbol")
    parser.add_argument("--interval", default=DEFAULT_INTERVAL, help="K-line interval")
    parser.add_argument("--lookback", type=int, default=DEFAULT_LOOKBACK, help="Historical candles")
    parser.add_argument("--pred-len", type=int, default=DEFAULT_PRED_LEN, help="Candles to forecast")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="HuggingFace model name")
    parser.add_argument("--tokenizer", default=DEFAULT_TOKENIZER, help="HuggingFace tokenizer name")
    parser.add_argument("--max-context", type=int, default=512, help="Model context length")
    parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature")
    parser.add_argument("--top-p", type=float, default=0.9, help="Nucleus sampling top-p")
    parser.add_argument("--sample-count", type=int, default=1, help="Forecast paths to average")
    parser.add_argument("--hf-cache", default=DEFAULT_HF_CACHE, help="HuggingFace cache directory")
    parser.add_argument("--output", default="", help="Optional CSV path to save predictions")
    args = parser.parse_args()

    pred_df = run_forecast(args)

    print("\nForecast:")
    print(pred_df.head(args.pred_len).to_string(index=False))

    # Compute a naive directional signal for downstream use
    last_close = float(pred_df["close"].iloc[-1])
    first_close = float(pred_df["close"].iloc[0])
    direction = "LONG" if last_close > first_close else "SHORT" if last_close < first_close else "NEUTRAL"
    print(f"\nKronos directional bias: {direction} ({first_close:.2f} → {last_close:.2f})")

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        pred_df.to_csv(out_path, index=False)
        print(f"\nSaved predictions to {out_path}")

    # Emit a JSON summary that the engine could consume
    summary = {
        "model": args.model,
        "symbol": args.symbol,
        "interval": args.interval,
        "pred_len": args.pred_len,
        "direction": direction,
        "last_forecast_close": round(last_close, 4),
        "first_forecast_close": round(first_close, 4),
        "forecast": json.loads(pred_df.to_json(orient="records", date_format="iso")),
    }
    print("\nJSON summary:")
    print(json.dumps(summary, indent=2, default=str))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
