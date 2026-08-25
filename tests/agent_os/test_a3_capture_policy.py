from __future__ import annotations

import hashlib
import json

import pytest

from agent_os.policy.a3_capture import (
    AuthorityType,
    CaptureDecision,
    CaptureLifecycle,
    CapturePolicy,
    CaptureReasonCode,
    CaptureRequest,
    HumanAuthorizationEvidence,
    binding_digest,
    evaluate,
    normalize_assets,
    transition,
)

NOW = 1_700_000_000
POLICY = CapturePolicy(
    policy_version="a3-policy-v1",
    allowed_venues=("binance",),
    allowed_assets=("BTCUSDT", "ETHUSDT"),
)


def request(**changes: object) -> CaptureRequest:
    values: dict[str, object] = {
        "request_id": "request-opaque-1",
        "idempotency_key": "idem-opaque-1",
        "tenant_id": "tenant-internal-1",
        "workspace_id": "workspace-internal-1",
        "agent_id": "agent-1",
        "agent_version": "v1",
        "strategy_digest": "a" * 64,
        "paper_account_id": "paper-account-1",
        "account_mode": "paper",
        "connector_id": "paper",
        "venue_id": "binance",
        "assets": ("ethusdt", "BTCUSDT"),
        "source_kind": "synthetic_fixture",
        "source_id": "fixture-source-1",
        "data_classification": "synthetic_fixture_metadata_v1",
        "requested_at": NOW,
        "requested_by": "workspace-owner-1",
        "policy_version": POLICY.policy_version,
    }
    values.update(changes)
    return CaptureRequest(**values)  # type: ignore[arg-type]


def authorization_for(item: CaptureRequest, **changes: object) -> HumanAuthorizationEvidence:
    try:
        scope = binding_digest(item)
    except ValueError:
        scope = "c" * 64
    values: dict[str, object] = {
        "authority_type": AuthorityType.WORKSPACE_OWNER,
        "authority_id": "owner-opaque-1",
        "decision_id": "decision-opaque-1",
        "approved_at": NOW,
        "expires_at": NOW + 600,
        "scope_digest": scope,
        "evidence_digest": "b" * 64,
        "single_use_nonce": "nonce-opaque-1",
        "revocation_epoch": 1,
    }
    values.update(changes)
    return HumanAuthorizationEvidence(**values)  # type: ignore[arg-type]


def test_valid_metadata_is_always_capture_disabled_and_safe_output_is_opaque() -> None:
    item = request()
    result = evaluate(item, (authorization_for(item),), POLICY, now=NOW + 1)
    assert result.state is CaptureLifecycle.EVALUATED
    assert result.decision.outcome is CaptureDecision.DENIED
    assert result.decision.reason_code is CaptureReasonCode.CAPTURE_DISABLED
    assert result.decision.recheck_required is True
    output = result.to_dict()
    assert "request_id" not in output
    assert "tenant_id" not in output
    assert "workspace_id" not in output
    assert "paper_account_id" not in output
    assert output["decision_id"].startswith("a3d-")


def test_assets_are_normalized_and_digest_is_canonical() -> None:
    item = request()
    assert normalize_assets(("ethusdt", "BTCUSDT")) == ("BTCUSDT", "ETHUSDT")
    assert binding_digest(item) == binding_digest(request(assets=("BTCUSDT", "ETHUSDT")))
    expected_value = {
        "account_mode": "paper",
        "agent_id": "agent-1",
        "agent_version": "v1",
        "assets": ("BTCUSDT", "ETHUSDT"),
        "connector_id": "paper",
        "data_classification": "synthetic_fixture_metadata_v1",
        "paper_account_id": "paper-account-1",
        "policy_version": "a3-policy-v1",
        "source_id": "fixture-source-1",
        "source_kind": "synthetic_fixture",
        "strategy_digest": "a" * 64,
        "tenant_id": "tenant-internal-1",
        "venue_id": "binance",
        "workspace_id": "workspace-internal-1",
    }
    expected = hashlib.sha256(
        json.dumps(
            expected_value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()
    assert binding_digest(item) == expected


@pytest.mark.parametrize(
    ("field", "value", "reason"),
    [
        (
            "data_classification",
            "raw_provider_payload_v1",
            CaptureReasonCode.CLASSIFICATION_NOT_ALLOWLISTED,
        ),
        ("account_mode", "live", CaptureReasonCode.LIVE_OR_TESTNET_DENIED),
        ("account_mode", "testnet", CaptureReasonCode.LIVE_OR_TESTNET_DENIED),
        ("connector_id", "binance", CaptureReasonCode.CONNECTOR_NOT_PAPER),
        ("venue_id", "unknown", CaptureReasonCode.VENUE_NOT_ALLOWLISTED),
        ("assets", ("*",), CaptureReasonCode.ASSET_NOT_ALLOWLISTED),
        ("source_kind", "live", CaptureReasonCode.SOURCE_NOT_ALLOWLISTED),
    ],
)
def test_default_deny_for_disallowed_bindings(
    field: str, value: object, reason: CaptureReasonCode
) -> None:
    item = request(**{field: value})
    result = evaluate(item, (authorization_for(item),), POLICY, now=NOW + 1)
    assert result.decision.reason_code is reason


def test_default_deny_for_scope_digest_mismatch() -> None:
    item = request()
    result = evaluate(item, (authorization_for(item, scope_digest="c" * 64),), POLICY, now=NOW + 1)
    assert result.decision.reason_code is CaptureReasonCode.AUTH_SCOPE_MISMATCH


def test_expired_revoked_and_consumed_are_deterministic() -> None:
    item = request()
    assert (
        evaluate(item, (authorization_for(item),), POLICY, now=NOW + 601).decision.reason_code
        is CaptureReasonCode.AUTH_EXPIRED
    )
    assert (
        evaluate(
            item, (authorization_for(item, revoked=True),), POLICY, now=NOW + 1
        ).decision.reason_code
        is CaptureReasonCode.AUTH_REVOKED
    )
    assert (
        evaluate(
            item, (authorization_for(item, consumed=True),), POLICY, now=NOW + 1
        ).decision.reason_code
        is CaptureReasonCode.AUTH_ALREADY_CONSUMED
    )
    assert (
        evaluate(
            item, (authorization_for(item),), POLICY, now=NOW + 1, revoked_epochs=(1,)
        ).decision.reason_code
        is CaptureReasonCode.AUTH_REVOKED
    )


def test_ttl_cannot_exceed_ten_minutes() -> None:
    item = request()
    result = evaluate(item, (authorization_for(item, expires_at=NOW + 601),), POLICY, now=NOW + 1)
    assert result.decision.reason_code is CaptureReasonCode.AUTH_EXPIRED


def test_lifecycle_is_forward_only_and_terminal() -> None:
    assert transition(CaptureLifecycle.DRAFT, CaptureLifecycle.SUBMITTED)
    assert transition(CaptureLifecycle.SUBMITTED, CaptureLifecycle.EVALUATED)
    assert transition(CaptureLifecycle.EVALUATED, CaptureLifecycle.DENIED)
    assert transition(CaptureLifecycle.EVALUATED, CaptureLifecycle.APPROVED_FOR_FUTURE_CAPTURE)
    assert transition(CaptureLifecycle.APPROVED_FOR_FUTURE_CAPTURE, CaptureLifecycle.CANCELLED)
    assert not transition(CaptureLifecycle.DENIED, CaptureLifecycle.DRAFT)
    assert not transition(CaptureLifecycle.EVALUATED, CaptureLifecycle.DRAFT)
    assert not transition("DRAFT", CaptureLifecycle.SUBMITTED)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "changes",
    [
        {"policy_version": ""},
        {"max_ttl_seconds": 601},
        {"max_ttl_seconds": 0},
        {"max_ttl_seconds": "600"},
        {"allowed_classifications": ("raw_provider_payload_v1",)},
        {"allowed_classifications": None},
        {"allowed_source_kinds": ("PAPERRUN_RECORDING_CAPTURE_V1",)},
        {"allowed_source_kinds": None},
        {"allowed_venues": None},
        {"allowed_venues": ("*",)},
        {"allowed_venues": ()},
        {"allowed_venues": ("binance", "binance")},
        {"allowed_assets": None},
        {"allowed_assets": ("*",)},
        {"allowed_assets": ()},
        {"allowed_assets": ("BTCUSDT", "BTCUSDT")},
        {"allowed_assets": ("btcusdt",)},
        {"require_single_use": False},
        {"require_revocation_check": False},
    ],
)
def test_invalid_policy_is_categorical_default_deny(changes: dict[str, object]) -> None:
    item = request()
    policy_values = {
        "policy_version": POLICY.policy_version,
        "allowed_venues": POLICY.allowed_venues,
        "allowed_assets": POLICY.allowed_assets,
    }
    policy_values.update(changes)
    invalid_policy = CapturePolicy(**policy_values)  # type: ignore[arg-type]
    result = evaluate(item, (authorization_for(item),), invalid_policy, now=NOW + 1)
    assert result.decision.outcome is CaptureDecision.DENIED
    assert result.decision.reason_code is CaptureReasonCode.POLICY_MISMATCH


@pytest.mark.parametrize(
    "changes",
    [
        {"request_id": ""},
        {"idempotency_key": ""},
        {"tenant_id": ""},
        {"workspace_id": ""},
        {"agent_id": ""},
        {"agent_version": ""},
        {"strategy_digest": "not-a-digest"},
        {"paper_account_id": ""},
        {"venue_id": "unknown"},
        {"assets": ()},
        {"source_kind": "PAPERRUN_RECORDING_CAPTURE_V1"},
        {"source_id": ""},
        {"data_classification": "raw_provider_payload_v1"},
        {"policy_version": "other-policy"},
        {"requested_by": ""},
    ],
)
def test_each_request_binding_mismatch_denies_deterministically(changes: dict[str, object]) -> None:
    item = request(**changes)
    result_one = evaluate(item, (authorization_for(item),), POLICY, now=NOW + 1)
    result_two = evaluate(item, (authorization_for(item),), POLICY, now=NOW + 1)
    assert result_one.decision.outcome is CaptureDecision.DENIED
    assert result_one.decision.reason_code is not CaptureReasonCode.CAPTURE_DISABLED
    assert result_one.decision.reason_code is result_two.decision.reason_code


def test_full_default_safe_output_and_repr_redaction() -> None:
    item = request()
    evidence = authorization_for(item)
    result = evaluate(item, (evidence,), POLICY, now=NOW + 1)
    output_text = repr(result.to_dict())
    safe_repr_text = repr(result)
    decision_repr_text = repr(result.decision)
    for raw in (
        item.request_id,
        item.tenant_id,
        item.workspace_id,
        item.paper_account_id,
        item.requested_by,
        item.idempotency_key,
        evidence.authority_id,
        evidence.decision_id,
        evidence.single_use_nonce,
        evidence.evidence_digest,
        item.source_id,
    ):
        assert raw not in output_text
        assert raw not in safe_repr_text
        assert raw not in decision_repr_text
    with pytest.raises(ValueError, match="A3_ASSET_NOT_ALLOWLISTED") as error:
        normalize_assets(("*",))
    assert item.source_id not in str(error.value)


@pytest.mark.parametrize(
    "changes",
    [
        {"allowed_venues": "binance"},
        {"allowed_assets": "BTCUSDT"},
        {"allowed_source_kinds": "synthetic_fixture"},
        {"allowed_classifications": "synthetic_fixture_metadata_v1"},
    ],
)
def test_scalar_policy_allowlists_fail_closed(changes: dict[str, object]) -> None:
    item = request()
    policy_values = {
        "policy_version": POLICY.policy_version,
        "allowed_venues": POLICY.allowed_venues,
        "allowed_assets": POLICY.allowed_assets,
    }
    policy_values.update(changes)
    invalid_policy = CapturePolicy(**policy_values)  # type: ignore[arg-type]
    result = evaluate(item, (authorization_for(item),), invalid_policy, now=NOW + 1)
    assert result.decision.outcome is CaptureDecision.DENIED
    assert result.decision.reason_code is CaptureReasonCode.POLICY_MISMATCH
