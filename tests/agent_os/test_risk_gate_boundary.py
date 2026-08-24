from agent_os.contracts import ExecutionMode, ExecutionRequest, RiskCheckRequest, RiskDecisionStatus
from agent_os.execution import PaperExecutor
from agent_os.risk import AgentRiskGate


def request(**overrides: object) -> RiskCheckRequest:
    values: dict[str, object] = {
        "request_id": "req-1",
        "idempotency_key": "idem-1",
        "actor_id": "test-actor",
        "symbol": "BTCUSDT",
        "side": "BUY",
        "quantity": 0.01,
        "price": 40_000.0,
        "leverage": 1,
    }
    values.update(overrides)
    return RiskCheckRequest(**values)


def execution_request(**overrides: object) -> ExecutionRequest:
    values: dict[str, object] = {
        "request_id": "req-1",
        "idempotency_key": "idem-1",
        "actor_id": "test-actor",
        "connector_id": "paper",
        "mode": ExecutionMode.PAPER,
        "symbol": "BTCUSDT",
        "side": "BUY",
        "quantity": 0.01,
        "price": 40_000.0,
        "leverage": 1,
    }
    values.update(overrides)
    return ExecutionRequest(**values)


def test_paper_request_is_approved_by_canonical_safety_gate() -> None:
    decision = AgentRiskGate().evaluate(request())

    assert decision.status is RiskDecisionStatus.APPROVED
    assert decision.mode is ExecutionMode.PAPER
    assert decision.policy_version == "phase1-paper-v1"


def test_live_and_testnet_order_modes_are_rejected_in_phase1() -> None:
    gate = AgentRiskGate()

    live = gate.evaluate(request(mode=ExecutionMode.LIVE))
    testnet = gate.evaluate(request(mode=ExecutionMode.TESTNET))

    assert live.status is RiskDecisionStatus.REJECTED
    assert testnet.status is RiskDecisionStatus.REJECTED
    assert "order_submission_disabled" in live.reasons[0]


def test_hardcoded_safety_limit_rejects_excessive_leverage() -> None:
    decision = AgentRiskGate().evaluate(request(leverage=6))

    assert decision.status is RiskDecisionStatus.REJECTED
    assert "leverage_exceeds_limit" in decision.reasons[0]


def test_kill_switch_rejects_new_entries() -> None:
    gate = AgentRiskGate()
    gate.kill_switch.activate("test-stop")

    decision = gate.evaluate(request(request_id="req-kill", idempotency_key="idem-kill"))

    assert decision.status is RiskDecisionStatus.REJECTED
    assert "kill_switch_active" in decision.reasons[0]


def test_paper_executor_rechecks_the_risk_gate_before_filling() -> None:
    gate = AgentRiskGate()
    executor = PaperExecutor(gate)
    gate.kill_switch.activate("executor-test-stop")

    result = executor.submit(execution_request())

    assert result["status"] == "rejected"
    assert result["fill"] is None
    assert executor.fills == []
