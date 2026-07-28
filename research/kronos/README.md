# Kronos Research Integration

This directory contains a minimal, isolated integration between the vendored
[Kronos](https://github.com/shiyu-coder/Kronos) foundation model and Binance
Futures data. It is intended for **research and signal prototyping**, not as a
runtime dependency of the main CoinScopeAI engine.

## What it does

`forecast_binance.py`:
1. Fetches recent klines from the Binance Futures testnet (or mainnet via
   `BINANCE_REST_URL`).
2. Formats the data into the Kronos predictor schema
   (`open`, `high`, `low`, `close`, `volume`, `amount`, `timestamps`).
3. Downloads a Kronos tokenizer and model from Hugging Face.
4. Runs an autoregressive forecast for the requested number of future candles.
5. Prints a human-readable forecast and a JSON summary that can be consumed by
   downstream signal generators.

## Why a separate environment?

Kronos depends on `torch`, `huggingface_hub`, and related ML packages. These are
large and can conflict with the leaner runtime of the trading engine. Keeping
Kronos in its own venv avoids polluting `coinscope_trading_engine` dependencies.

## Setup

```bash
cd /Users/mac/Documents/Claude/Projects/CoinScopeAI/research/kronos

# Create a dedicated virtual environment
python3 -m venv .venv-kronos
source .venv-kronos/bin/activate

# Install Kronos + integration dependencies
pip install -r requirements.txt
```

The first run will download model weights from Hugging Face into
`CoinScopeAI/.cache/kronos/`.

## Usage

```bash
source .venv-kronos/bin/activate

# Default: BTCUSDT 5m, 120 candles of history, forecast 12 candles ahead
python forecast_binance.py

# Custom symbol / interval / forecast length
python forecast_binance.py \
  --symbol ETHUSDT \
  --interval 15m \
  --lookback 200 \
  --pred-len 8 \
  --model NeoQuasar/Kronos-small \
  --output forecasts/eth_15m.csv

# Use a smaller/faster model
python forecast_binance.py --model NeoQuasar/Kronos-mini --max-context 2048
```

## Output example

```
Fetching 120 klines for BTCUSDT @ 5m
  Range: 2026-07-28 10:00:00+00:00 → 2026-07-28 20:00:00+00:00
Loading tokenizer: NeoQuasar/Kronos-Tokenizer-base
Loading model: NeoQuasar/Kronos-small
Running forecast for 12 candles...

Forecast:
 timestamp                  open    high     low   close    volume    amount
2026-07-28 20:05:00+00:00 68450.1 68510.2 68390.5 68480.3  120.5     8245000.0
...

Kronos directional bias: LONG (68480.30 → 68720.50)
```

## Integration ideas for CoinScopeAI

- **Signal generator**: wrap `forecast_binance.py` in a function that returns a
  `SignalStrength` enum (`STRONG_LONG`, `LONG`, `NEUTRAL`, `SHORT`,
  `STRONG_SHORT`) based on the forecasted return over the horizon.
- **Confluence scorer**: feed the Kronos directional bias as an additional
  feature into `coinscope_trading_engine/signals/confluence_scorer.py`.
- **Backtesting**: run forecasts over historical windows and evaluate them with
  `coinscope_trading_engine/storage/trade_journal.py`.

## Notes

- The script hits the Binance **testnet** by default. Set
  `BINANCE_REST_URL=https://fapi.binance.com` for live mainnet data.
- Kronos-small/base have a max context of 512. Do not set `--lookback` above
  this unless you use Kronos-mini (2048 context) or enable truncation in the
  predictor.
- GPU inference is recommended for the base/large models; small/mini are fine
  on CPU for research.
