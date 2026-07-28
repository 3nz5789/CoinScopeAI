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
    sample_count: int = 3,
    consensus_threshold_pct: float = 50.0,
    timeout: int = 300,
) -> dict:
    """
    Generate a Kronos-based signal for a single symbol using multi-sample
    consensus to reduce stochastic noise.

    Parameters
    ----------
    sample_count : int
        Number of independent Kronos forecasts to run (1-20).
    consensus_threshold_pct : float
        Minimum percentage of samples that must agree for a non-NEUTRAL signal.
        Default 66.7% means at least 2 of 3 samples must agree.

    Returns a dict with keys:
        symbol      : str
        direction   : "LONG" | "SHORT" | "NEUTRAL"
        score       : float  (0.0 – 100.0, based on consensus strength)
        strength    : "WEAK" | "MODERATE" | "STRONG"
        forecast    : list of forecast candles
        consensus   : dict with count/pct details
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
        "sample_count": sample_count,
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
            "consensus": {},
            "error": result["error"],
            "timestamp": time.time(),
        }

    consensus_pct = float(result.get("consensus_pct", 0.0))
    majority_dir = result.get("direction", "NEUTRAL")

    # Only accept the majority direction if it meets the consensus threshold
    if consensus_pct >= consensus_threshold_pct and majority_dir in ("LONG", "SHORT"):
        direction = majority_dir
    else:
        direction = "NEUTRAL"

    # Score is directly the consensus percentage (already 0-100)
    score = consensus_pct

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
        "consensus": {
            "direction": majority_dir,
            "count": result.get("consensus_count", 0),
            "total": result.get("total_samples", 0),
            "pct": consensus_pct,
            "breakdown": result.get("counts", {}),
        },
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

    async def scan(
        self,
        symbol: str,
        sample_count: int = 3,
        consensus_threshold_pct: float = 50.0,
    ) -> ScannerResult:
        """
        Run multiple Kronos forecasts and emit a single ScannerHit only when
        the samples reach consensus.
        """
        # Offload the blocking subprocess call to a thread so the async event
        # loop is not frozen while the model downloads / infers.
        signal = await asyncio.to_thread(
            generate_kronos_signal,
            symbol=symbol,
            sample_count=sample_count,
            consensus_threshold_pct=consensus_threshold_pct,
        )

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

        consensus = signal.get("consensus", {})
        majority = consensus.get("direction", "NEUTRAL")
        count = consensus.get("count", 0)
        total = consensus.get("total", 0)

        hit = ScannerHit(
            scanner=self.name,
            symbol=symbol,
            direction=SignalDirection(direction),
            strength=strength,
            score=score,
            reason=(
                f"Kronos consensus {direction} | "
                f"{count}/{total} samples ({score:.1f}%) | "
                f"breakdown={consensus.get('breakdown', {})}"
            ),
            metadata={
                "forecast": signal.get("forecast", []),
                "consensus": consensus,
            },
        )
        return ScannerResult(scanner=self.name, symbol=symbol, hits=[hit])


# ── CLI smoke-test ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    sig = generate_kronos_signal(symbol="BTCUSDT", sample_count=3)
    print(json.dumps(sig, indent=2, default=str))
