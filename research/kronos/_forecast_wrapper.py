#!/usr/bin/env python3
"""
Internal wrapper used by the CoinScopeAI engine to call Kronos in its isolated
research venv. Reads a JSON config from argv[1], runs the forecast one or more
times, aggregates directional consensus, and prints a JSON summary to stdout.
"""

import json
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))

from forecast_binance import build_summary, run_forecast_dict  # noqa: E402


def aggregate_directions(summaries: list[dict]) -> dict:
    """Aggregate directional votes from multiple forecast summaries."""
    directions = [s.get("direction", "NEUTRAL") for s in summaries]
    counts = Counter(directions)
    total = len(directions)
    majority_dir, majority_count = counts.most_common(1)[0]

    first_closes = [s.get("first_forecast_close") for s in summaries]
    last_closes = [s.get("last_forecast_close") for s in summaries]

    return {
        "direction": majority_dir,
        "consensus_count": majority_count,
        "total_samples": total,
        "consensus_pct": round(majority_count / total * 100, 2),
        "counts": dict(counts),
        "first_forecast_close": round(sum(first_closes) / len(first_closes), 6),
        "last_forecast_close": round(sum(last_closes) / len(last_closes), 6),
        "forecast": summaries[0].get("forecast", []),
        "all_summaries": summaries,
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"error": "missing config JSON"}), file=sys.stderr)
        return 1

    try:
        config = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"invalid JSON: {exc}"}), file=sys.stderr)
        return 1

    sample_count = int(config.get("sample_count", 1))
    sample_count = max(1, min(sample_count, 20))  # sanity cap

    summaries = []
    for i in range(sample_count):
        pred_df = run_forecast_dict(config)
        summary = build_summary(pred_df, config)
        summaries.append(summary)

    aggregated = aggregate_directions(summaries)
    aggregated["model"] = config.get("model", "NeoQuasar/Kronos-mini")
    aggregated["symbol"] = config.get("symbol", "BTCUSDT")
    aggregated["interval"] = config.get("interval", "5m")
    aggregated["pred_len"] = config.get("pred_len", 12)

    print(json.dumps(aggregated, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
