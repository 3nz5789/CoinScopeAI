"""Phase-1 Agent OS worker entry point."""

from __future__ import annotations

import argparse
import json

from agent_os.contracts import ExecutionMode, ExecutionRequest
from agent_os.data import EventSource, btcusdt_fixture
from agent_os.execution import PaperExecutor
from agent_os.risk import AgentRiskGate
from agent_os.runtime import AgentRunner, AgentGraph, draft_from_prompt

DEFAULT_PROMPT = "Every 1h long BTCUSDT when funding is negative with risk 1% and stop loss 2%"


def run_once(prompt: str) -> dict[str, object]:
    document = draft_from_prompt(prompt, name="phase1-demo")
    graph = AgentGraph(document)
    runtime = AgentRunner(EventSource(btcusdt_fixture())).inspect(document)
    gate = AgentRiskGate()
    executor = PaperExecutor(gate)

    paper_result: dict[str, object] = {
        "status": "not_created",
        "reason": "graph_not_ready",
    }
    if graph.validate().valid:
        paper_result = executor.submit(
            ExecutionRequest(
                request_id="phase1-demo-request",
                idempotency_key="phase1-demo-idempotency",
                actor_id="local-demo",
                connector_id="paper",
                mode=ExecutionMode.PAPER,
                symbol="BTCUSDT",
                side="BUY",
                quantity=0.01,
                price=40_000.0,
                leverage=1,
            )
        )

    return {
        "mode": "paper",
        "live_order_placement": False,
        "document": document.to_dict(),
        "runtime": runtime.to_dict(),
        "paper_execution": paper_result,
        "risk_status": gate.status(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one safe Agent OS paper cycle")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    args = parser.parse_args()
    print(json.dumps(run_once(args.prompt), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
