"""
Kronos Signal Source
====================
Bridge between the CoinScopeAI engine and the isolated Kronos research
environment. Runs Kronos forecasts in a subprocess so torch/huggingface stay
out of the main engine venv.

Output formats
--------------
- ``generate_kronos_signal()`` returns a plain dict suitable for logging or
  ad-hoc consumption.
- ``KronosScanner`` implements ``BaseScanner`` and emits ``ScannerHit`` objects
  that plug directly into ``ConfluenceScorer``.

If the research venv or model is missing, both interfaces fail gracefully and
return neutral/empty results rather than crashing the engine.
"""

from __future__ import annotations

import asyncio
import json
import logging
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

# Allow running this file directly (python coinscope_trading_engine/signals/kronos_signal.py)
# while still supporting relative imports.
if __name__ == "__main__" and __package__ is None:
    __package__ = "coinscope_trading_engine.signals"
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ..scanner.base_scanner import BaseScanner, HitStrength, ScannerHit, ScannerResult, SignalDirection

logger = logging.getLogger(__name__)


def _resolve_venv_python() -> Path:
    # kronos_signal.py is at coinscope_trading_engine/signals/kronos_signal.py
    # parents[2] gives the repository root.
    return Path(__file__).resolve().parents[2] / "research" / "kronos" / ".venv-kronos" / "bin" / "python"


def _resolve_wrapper_path() -> Path:
    return Path(__file__).resolve().parents[2] / "research" / "kronos" / "_forecast_wrapper.py"


def _run_kronos_subprocess(config: dict, timeout: int = 120) -> dict:
    """
    Run the Kronos forecast in the isolated research venv.

    Returns the parsed JSON summary dict, or a dict with an ``error`` key on
    failure. This keeps torch/huggingface out of the main engine venv.
    """
    venv_python = _resolve_venv_python()
    wrapper = _resolve_wrapper_path()

    if not venv_python.exists():
        return {"error": f"Kronos venv not found at {venv_python}"}
    if not wrapper.exists():
        return {"error": f"Kronos wrapper not found at {wrapper}"}

    payload = json.dumps(config, default=str)
    cmd = [str(venv_python), str(wrapper), payload]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"error": f"Kronos forecast timed out after {timeout}s"}
    except Exception as exc:  # pragma: no cover
        return {"error": f"failed to spawn Kronos process: {exc}"}

    if result.returncode != 0:
        stderr = result.stderr.strip() or "unknown error"
        return {"error": f"Kronos forecast failed: {stderr}"}

    try:
        return json.loads(result.stdout.splitlines()[-1])
    except json.JSONDecodeError as exc:
        return {"error": f"could not parse Kronos output: {exc}", "raw": result.stdout}


def generate_kronos_signal(
    symbol: str = "BTCUSDT",
    interval: str = "5m",
    lookback: int = 120,
    pred_len: int = 12,
    model: str = "NeoQuasar/Kronos-mini",
    tokenizer: str = "NeoQuasar/Kronos-Tokenizer-base",
    max_context: int = 2048,
    timeout: int = 120,
) -> dict:
    """
    Generate a Kronos-based signal for a single symbol.

    Returns a dict with keys:
        symbol      : str
        direction   : "LONG" | "SHORT" | "NEUTRAL"
        score       : float  (0.0 – 100.0, higher = stronger conviction)
        strength    : "WEAK" | "MODERATE" | "STRONG"
        forecast    : list of forecast candles
        error       : str or None
        timestamp   : float
    """
    config = {
        "symbol": symbol,
        "interval": interval,
        "lookback": lookback,
        "pred_len": pred_len,
        "model": model,
        "tokenizer": tokenizer,
        "max_context": max_context,
        "temperature": 1.0,
        "top_p": 0.9,
        "sample_count": 1,
    }

    result = _run_kronos_subprocess(config, timeout=timeout)

    if "error" in result:
        logger.warning("Kronos signal unavailable: %s", result["error"])
        return {
            "symbol": symbol,
            "direction": "NEUTRAL",
            "score": 0.0,
            "strength": "WEAK",
            "forecast": [],
            "error": result["error"],
            "timestamp": time.time(),
        }

    direction = result.get("direction", "NEUTRAL")
    first_close = float(result.get("first_forecast_close", 0.0))
    last_close = float(result.get("last_forecast_close", 0.0))

    # Map price change magnitude to a 0-100 score
    if first_close > 0 and direction in ("LONG", "SHORT"):
        pct_change = abs(last_close - first_close) / first_close
        # Scale: 0.1% move -> 25, 0.5% -> 70, capped at 100
        score = min(pct_change * 2500 * 100, 100.0)
    else:
        score = 0.0

    if score >= 70.0:
        strength = "STRONG"
    elif score >= 45.0:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return {
        "symbol": symbol,
        "direction": direction,
        "score": round(score, 2),
        "strength": strength,
        "forecast": result.get("forecast", []),
        "error": None,
        "timestamp": time.time(),
    }


class KronosScanner(BaseScanner):
    """
    Scanner adapter that surfaces Kronos forecasts as ScannerHits.

    Because Kronos runs in a separate venv, this scanner is deliberately
    best-effort: if the venv or model is missing, it returns an empty result
    rather than crashing the engine.
    """

    def __init__(
        self,
        cache=None,
        rest=None,
        name: Optional[str] = None,
    ) -> None:
        # Kronos does not use the shared cache or REST client, but we keep the
        # BaseScanner contract by passing None values.
        super().__init__(cache=cache, rest=rest, name=name)

    async def scan(self, symbol: str) -> ScannerResult:
        """
        Run a Kronos forecast and emit a single ScannerHit for the dominant
        direction, if any.
        """
        # Offload the blocking subprocess call to a thread so the async event
        # loop is not frozen while the model downloads / infers.
        signal = await asyncio.to_thread(generate_kronos_signal, symbol=symbol)

        if signal.get("error"):
            return ScannerResult(
                scanner=self.name,
                symbol=symbol,
                error=signal["error"],
            )

        direction = signal.get("direction", "NEUTRAL")
        if direction == "NEUTRAL":
            return ScannerResult(scanner=self.name, symbol=symbol, hits=[])

        score = signal.get("score", 0.0)
        strength = (
            HitStrength.STRONG if score >= 70.0
            else HitStrength.MEDIUM if score >= 45.0
            else HitStrength.WEAK
        )

        hit = ScannerHit(
            scanner=self.name,
            symbol=symbol,
            direction=SignalDirection(direction),
            strength=strength,
            score=score,
            reason=f"Kronos {direction} bias | score={score:.1f} | strength={strength.value}",
            metadata={
                "forecast": signal.get("forecast", []),
            },
        )
        return ScannerResult(scanner=self.name, symbol=symbol, hits=[hit])


# ── CLI smoke-test ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    sig = generate_kronos_signal()
    print(json.dumps(sig, indent=2, default=str))
