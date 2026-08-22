from agent_os.contracts import ExecutionMode, ExecutionRequest
from agent_os.data import EventSource, btcusdt_fixture
from agent_os.execution import PaperExecutor
from agent_os.risk import AgentRiskGate
from agent_os.runtime import AgentRunner, AgentGraph, draft_from_prompt


def test_runtime_consumes_fixture_events_with_provenance() -> None:
    document = draft_from_prompt(
        "Every 1h long BTCUSDT when funding is negative with risk 1% and stop loss 2%"
    )
    result = AgentRunner(EventSource(btcusdt_fixture())).inspect(document)

    assert result.status == "ready"
    assert result.events_seen == 3
    assert result.observations[0]["provenance"] == "fixture"


def test_paper_executor_records_only_simulated_fill() -> None:
    executor = PaperExecutor(AgentRiskGate())
    result = executor.submit(
        ExecutionRequest(
            request_id="paper-1",
            idempotency_key="paper-idem-1",
            actor_id="test-actor",
            connector_id="paper",
            mode=ExecutionMode.PAPER,
            symbol="BTCUSDT",
            side="BUY",
            quantity=0.01,
            price=40_000.0,
            leverage=1,
        )
    )

    assert result["status"] == "filled"
    assert result["fill"]["mode"] == "paper"
    assert "exchange_order_id" not in result["fill"]
    assert len(executor.fills) == 1


def test_incomplete_graph_creates_no_execution_request() -> None:
    document = draft_from_prompt("Watch BTCUSDT")
    result = AgentRunner(EventSource(btcusdt_fixture())).inspect(document)

    assert result.status == "blocked"
    assert result.events_seen == 0
    assert AgentGraph(document).validate().valid is False
