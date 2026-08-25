import ast
from pathlib import Path

from agent_os.policy.a3_explanation import (
    ExplanationMode,
    ExplanationOutcome,
    ExplanationPolicy,
    ExplanationReasonCode,
    ExplanationRequest,
    evaluate,
)


ROOT = Path(__file__).resolve().parents[2]
A3_PATH = ROOT / "agent_os" / "policy" / "a3_explanation.py"
ALLOWED_IMPORTS = {"__future__", "dataclasses", "enum", "re", "typing"}
FORBIDDEN_IMPORTS = {
    "agent_os",
    "asyncio",
    "boto3",
    "cryptography",
    "fastapi",
    "http",
    "httpx",
    "io",
    "os",
    "pathlib",
    "requests",
    "socket",
    "sqlite3",
    "subprocess",
    "urllib",
}
FORBIDDEN_CALLS = {
    "connect",
    "consume",
    "decrypt",
    "encrypt",
    "execute",
    "load",
    "open",
    "read",
    "scan",
    "submit",
    "write",
}
FORBIDDEN_ATTRIBUTES = {
    "api",
    "capture",
    "connector",
    "database",
    "exchange",
    "filesystem",
    "kms",
    "material",
    "network",
    "order",
    "paperexecutor",
    "replay",
    "scanner",
    "storage",
    "wallet",
    "worker",
}


def test_imports_and_calls_are_pure() -> None:
    tree = ast.parse(A3_PATH.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                module = alias.name.split(".", 1)[0]
                assert module in ALLOWED_IMPORTS
                assert module not in FORBIDDEN_IMPORTS
        if isinstance(node, ast.ImportFrom) and node.level == 0:
            module = (node.module or "").split(".", 1)[0]
            assert module in ALLOWED_IMPORTS
            assert module not in FORBIDDEN_IMPORTS
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
            assert name not in FORBIDDEN_CALLS
        if isinstance(node, ast.Attribute):
            assert node.attr.lower() not in FORBIDDEN_ATTRIBUTES


def test_source_has_no_prohibited_vocabularies_or_activation_fields() -> None:
    source = A3_PATH.read_text(encoding="utf-8")
    assert "ALLOWED" not in source
    assert "allowed" not in source
    for forbidden in (
        "provider_label",
        "model_name",
        "prompt",
        "raw_output",
        "safe_summary",
        "capture_enabled",
        "PaperExecutor",
        "ReplayEngine",
        "StrategyDocument(",
        "RiskDecision(",
        "ExecutionRequest(",
        "AgentRiskGate(",
    ):
        assert forbidden not in source


def test_safe_output_has_exact_categorical_key_set() -> None:
    item = ExplanationRequest(
        request_correlation_digest="b" * 64,
        source_digest="a" * 64,
        policy_version=ExplanationPolicy().policy_version,
        mode=ExplanationMode.PAPER,
        canonical_state_ref_digests=("c" * 64,),
        canonical_reference_kinds=("strategy",),
        provenance_digest="d" * 64,
        requested_explanation_kind="strategy_summary",
        candidate_content_categories=("advisory_summary",),
        content_markers=("summary",),
    )
    result = evaluate(item)
    assert result.outcome is ExplanationOutcome.NON_ACTIONABLE_ACCEPTED
    assert result.reason_code is ExplanationReasonCode.REQUEST_VALID
    output = result.to_dict()
    assert set(output) == {
        "request_correlation_digest",
        "source_digest",
        "policy_version",
        "mode",
        "canonical_state_ref_digests",
        "provenance_digest",
        "outcome",
        "reason_code",
        "requires_human_review",
    }
    assert output["requires_human_review"] is True
    serialized = repr(output)
    for forbidden in (
        "prompt",
        "raw_output",
        "provider_label",
        "model_name",
        "safe_summary",
        "private_key",
        "seed_phrase",
        "symbol",
        "leverage",
        "order",
    ):
        assert forbidden not in serialized


def test_policy_has_exact_reference_and_marker_limits() -> None:
    policy = ExplanationPolicy()
    assert policy.max_references == 5
    assert policy.max_markers == 16
    assert policy.explanation_kinds == (
        "missing_evidence",
        "paper_result_summary",
        "provenance_summary",
        "review_summary",
        "risk_rationale",
        "strategy_summary",
    )


def test_non_paper_inputs_never_become_accepted() -> None:
    base = dict(
        request_correlation_digest="b" * 64,
        source_digest="a" * 64,
        policy_version=ExplanationPolicy().policy_version,
        canonical_state_ref_digests=("c" * 64,),
        canonical_reference_kinds=("strategy",),
        provenance_digest="d" * 64,
        requested_explanation_kind="strategy_summary",
        candidate_content_categories=("advisory_summary",),
        content_markers=("summary",),
    )
    for mode in (ExplanationMode.TESTNET, ExplanationMode.LIVE, ExplanationMode.UNKNOWN):
        result = evaluate(ExplanationRequest(mode=mode, **base))
        assert result.outcome is ExplanationOutcome.DENIED
        assert result.reason_code is ExplanationReasonCode.MODE_NON_PAPER
