from __future__ import annotations

import ast
from pathlib import Path

from agent_os.policy.a3_capture import (
    CaptureRequest,
    CapturePolicy,
    HumanAuthorizationEvidence,
    AuthorityType,
    binding_digest,
    evaluate,
)

ROOT = Path(__file__).resolve().parents[2]
A3_PATH = ROOT / "agent_os" / "policy" / "a3_capture.py"
ALLOWED_IMPORTS = {"__future__", "dataclasses", "enum", "hashlib", "json", "re", "typing"}
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
FORBIDDEN_NAMES = {
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


def test_a3_imports_and_calls_are_pure() -> None:
    tree = ast.parse(A3_PATH.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert all(alias.name.split(".", 1)[0] in ALLOWED_IMPORTS for alias in node.names)
        if isinstance(node, ast.ImportFrom) and node.level == 0:
            assert (node.module or "").split(".", 1)[0] in ALLOWED_IMPORTS
        if isinstance(node, ast.Call):
            name = (
                node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
            )
            assert name not in FORBIDDEN_CALLS
        if isinstance(node, ast.Attribute):
            assert node.attr.lower() not in FORBIDDEN_NAMES


def test_a3_source_has_no_activation_field_or_capture_activation_symbol() -> None:
    source = A3_PATH.read_text()
    assert "capture_enabled" not in source
    assert "PAPERRUN_RECORDING_CAPTURE_V1" not in source
    assert "MaterialCoordinator" not in source
    assert "PaperExecutor" not in source
    assert "ReplayEngine" not in source


def test_safe_output_excludes_raw_request_and_account_identity() -> None:
    item = CaptureRequest(
        "request-1",
        "idem-1",
        "tenant-1",
        "workspace-1",
        "agent-1",
        "v1",
        "a" * 64,
        "paper-account-1",
        "paper",
        "paper",
        "binance",
        ("BTCUSDT",),
        "synthetic_fixture",
        "fixture-1",
        "synthetic_fixture_metadata_v1",
        100,
        "owner-1",
        "policy-v1",
    )
    policy = CapturePolicy("policy-v1", ("binance",), ("BTCUSDT",))
    auth = HumanAuthorizationEvidence(
        AuthorityType.WORKSPACE_OWNER,
        "authority-1",
        "decision-1",
        100,
        200,
        binding_digest(item),
        "b" * 64,
        "nonce-1",
        1,
    )
    output = evaluate(item, (auth,), policy, now=101).to_dict()
    serialized = repr(output)
    for forbidden in ("request_id", "tenant_id", "workspace_id", "paper_account_id"):
        assert forbidden not in output
    for raw in ("request-1", "tenant-1", "workspace-1", "paper-account-1"):
        assert raw not in serialized
    assert output["recheck_required"] is True


def test_internal_metadata_exports_are_documented_and_not_safe_output() -> None:
    source = A3_PATH.read_text()
    documentation = (ROOT / "docs" / "architecture" / "agent-os-a3-capture-policy.md").read_text()
    assert "internal-only" in source
    assert "internal-only" in documentation
    assert "request_id, decision_id" not in documentation
    assert "safe receipt may expose only opaque request ID" not in documentation
    assert "opaque decision ID" in documentation
    assert "decision_id" in documentation
    assert "binding_digest" in documentation
    assert "recheck_required" in documentation
