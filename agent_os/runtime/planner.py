"""Draft-only prompt planner for the Agent OS.

This is intentionally deterministic. A future LLM-assisted parser can replace it
behind the same contract, but it must preserve missing-field reporting and remain
off the execution hot path.
"""

from __future__ import annotations

import re

from agent_os.contracts import NodeKind, StrategyDocument, StrategyLifecycle

from .graph import node

_SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT")


def draft_from_prompt(prompt: str, name: str = "prompt-draft") -> StrategyDocument:
    """Compile a natural-language prompt into a safe, paper-mode draft."""
    normalized = prompt.strip()
    if not normalized:
        raise ValueError("prompt must not be empty")

    lower = normalized.lower()
    missing: list[str] = []
    nodes = []

    cadence_match = re.search(r"\b(?:every\s+)?(\d+\s*[mhd]|hourly|daily)\b", lower)
    cadence = cadence_match.group(1) if cadence_match else "not specified"
    if cadence == "not specified":
        missing.append("cadence")
    nodes.append(node(NodeKind.SCHEDULE, "Schedule", cadence, 1, "blue"))

    symbol = next((candidate for candidate in _SYMBOLS if candidate[:3].lower() in lower), None)
    if symbol is None:
        missing.append("market")
        market_detail = "Market not specified"
    else:
        market_detail = f"{symbol} perpetual"
    nodes.append(node(NodeKind.MARKET, "Market", market_detail, 1, "mint"))

    has_condition = any(
        token in lower for token in ("when", "if", "funding", "rsi", "ema", "volume", "<", ">")
    )
    if not has_condition:
        missing.append("conditions")
        condition_detail = "Condition not specified"
    else:
        condition_detail = "Condition retained from prompt; review before arming"
    nodes.append(node(NodeKind.CONDITION, "Conditions", condition_detail, 1, "amber"))

    has_entry = any(token in lower for token in ("long", "short", "buy", "sell", "enter"))
    if not has_entry:
        missing.append("entry")
        entry_detail = "Entry direction not specified"
    else:
        entry_detail = "Entry intent retained from prompt"
    nodes.append(node(NodeKind.ENTRY, "Entry", entry_detail, 1, "mint"))

    has_risk = any(
        token in lower for token in ("risk", "stop", "leverage", "daily loss", "drawdown")
    )
    if not has_risk:
        missing.append("risk_rules")
        risk_detail = "Risk rules required before paper arming"
    else:
        risk_detail = "Risk rules retained from prompt; canonical gate required"
    nodes.append(node(NodeKind.RISK, "Risk gate", risk_detail, 1, "coral"))

    has_exit = any(token in lower for token in ("exit", "take profit", "stop loss", "close"))
    if not has_exit:
        missing.append("exit_rules")
        exit_detail = "Exit rules required before paper arming"
    else:
        exit_detail = "Exit rules retained from prompt"
    nodes.append(node(NodeKind.EXIT, "Exit", exit_detail, 1, "coral"))

    code = "# Phase-1 draft; execution remains paper-only\n" + "# " + normalized
    return StrategyDocument(
        name=name,
        prompt=normalized,
        nodes=nodes,
        code=code,
        mode="paper",
        lifecycle=StrategyLifecycle.DRAFT,
        missing_fields=missing,
    )
