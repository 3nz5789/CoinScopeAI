from agent_os.contracts import NodeKind
from agent_os.runtime import AgentGraph, draft_from_prompt


def test_complete_prompt_becomes_valid_paper_graph() -> None:
    document = draft_from_prompt(
        "Every 1h long BTCUSDT when funding is negative with risk 1% and stop loss 2%"
    )

    validation = AgentGraph(document).validate()

    assert validation.valid is True
    assert document.mode == "paper"
    assert document.missing_fields == []
    assert {node.kind for node in document.nodes} == set(NodeKind)


def test_incomplete_prompt_reports_missing_fields_without_invention() -> None:
    document = draft_from_prompt("Watch BTCUSDT")

    assert "conditions" in document.missing_fields
    assert "entry" in document.missing_fields
    assert "risk_rules" in document.missing_fields
    assert "exit_rules" in document.missing_fields
    assert AgentGraph(document).validate().valid is False


def test_graph_rejects_non_paper_mode() -> None:
    document = draft_from_prompt(
        "Every 1h long BTCUSDT when funding is negative with risk 1% and stop loss 2%"
    )
    document.mode = "live"

    validation = AgentGraph(document).validate()

    assert validation.valid is False
    assert "Phase 1 only permits paper mode" in validation.errors
