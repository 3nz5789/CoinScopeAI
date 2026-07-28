#!/usr/bin/env python3
"""
Internal wrapper used by the CoinScopeAI engine to call Kronos in its isolated
research venv. Reads a JSON config from argv[1], runs the forecast, and prints
a JSON summary to stdout.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from forecast_binance import build_summary, run_forecast_dict  # noqa: E402


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"error": "missing config JSON"}), file=sys.stderr)
        return 1

    try:
        config = json.loads(sys.argv[1])
    except json.JSONDecodeError as exc:
        print(json.dumps({"error": f"invalid JSON: {exc}"}), file=sys.stderr)
        return 1

    pred_df = run_forecast_dict(config)
    summary = build_summary(pred_df, config)
    print(json.dumps(summary, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
