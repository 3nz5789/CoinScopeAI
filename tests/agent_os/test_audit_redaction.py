import pytest

from agent_os.persistence.audit_contracts import AuditEvent, AuditEventType, AuditOutcome
from agent_os.persistence.audit_redaction import redact_audit_event
from agent_os.persistence.authorization_contracts import digest_value
from agent_os.persistence.authorization_memory import InMemoryAuditSink

DIGEST = "a" * 64


def event(tenant="tenant-1", workspace="workspace-1"):
    payload = {
        "event_id": "event-1",
        "tenant_id": tenant,
        "workspace_id": workspace,
        "event_type": AuditEventType.AUTH_ISSUED,
        "event_version": 1,
        "occurred_at": 100,
        "sequence": 1,
        "actor_digest": DIGEST,
        "grant_id": "grant-1",
        "request_digest": DIGEST,
        "scope_digest": DIGEST,
        "policy_version": "policy-v1",
        "revocation_epoch": 0,
        "outcome": AuditOutcome.ACCEPTED,
        "reason_code": None,
        "correlation_digest": DIGEST,
    }
    return AuditEvent(**payload, event_digest=digest_value(payload))


def test_redaction_is_whitelist_only():
    result = redact_audit_event(event())
    data = result.to_dict()
    assert set(data) == {
        "event_id",
        "event_type",
        "event_version",
        "occurred_at",
        "sequence",
        "grant_id",
        "scope_digest",
        "policy_version",
        "revocation_epoch",
        "outcome",
        "reason_code",
        "correlation_digest",
    }
    assert "tenant_id" not in data
    assert "actor_digest" not in data
    assert "request_digest" not in data


def test_enum_fields_serialize_and_raw_strings_fail_closed():
    serialized = event().to_dict()
    assert serialized["event_type"] == "AUTH_ISSUED"
    assert serialized["outcome"] == "accepted"
    invalid_type = event()
    object.__setattr__(invalid_type, "event_type", "AUTH_ISSUED")
    with pytest.raises(TypeError, match="audit_event_type_invalid"):
        invalid_type.__post_init__()
    invalid_outcome = event()
    object.__setattr__(invalid_outcome, "outcome", "accepted")
    with pytest.raises(TypeError, match="audit_outcome_invalid"):
        invalid_outcome.__post_init__()


def test_redaction_rejects_invalid_or_forbidden_shapes():
    invalid = event()
    object.__setattr__(invalid, "actor_digest", "not-a-digest")
    with pytest.raises(ValueError):
        redact_audit_event(invalid)


def test_audit_sink_lists_only_requested_tenant_and_workspace():
    sink = InMemoryAuditSink()
    sink.append(event("tenant-1", "workspace-1"))
    other = event("tenant-2", "workspace-2")
    object.__setattr__(other, "event_id", "event-2")
    object.__setattr__(other, "event_digest", digest_value(other.to_dict()))
    sink.append(other)
    assert len(sink.list_redacted("tenant-1", workspace_id="workspace-1")) == 1
    assert sink.list_redacted("tenant-1", workspace_id="workspace-2") == ()
    assert len(sink.list_redacted("tenant-2")) == 1
