"""Whitelist-only redaction for A4-v1 audit metadata."""

from __future__ import annotations

from .audit_contracts import AuditEvent, RedactedAuditEvent
from .authorization_contracts import valid_digest, valid_identifier


def redact_audit_event(event: AuditEvent) -> RedactedAuditEvent:
    """Project an internal event to the only fields safe for ordinary review."""
    if not isinstance(event, AuditEvent):
        raise TypeError("audit_event_invalid")
    if not valid_identifier(event.event_id) or not valid_identifier(event.tenant_id):
        raise ValueError("audit_event_identity_invalid")
    if not valid_identifier(event.workspace_id):
        raise ValueError("audit_event_workspace_invalid")
    if event.grant_id is not None and not valid_identifier(event.grant_id):
        raise ValueError("audit_event_grant_invalid")
    if not valid_digest(event.request_digest) or not valid_digest(event.event_digest):
        raise ValueError("audit_event_digest_invalid")
    if event.scope_digest is not None and not valid_digest(event.scope_digest):
        raise ValueError("audit_event_scope_digest_invalid")
    if event.correlation_digest is not None and not valid_digest(event.correlation_digest):
        raise ValueError("audit_event_correlation_invalid")
    if event.policy_version is not None and not valid_identifier(event.policy_version):
        raise ValueError("audit_event_policy_invalid")
    if not valid_digest(event.actor_digest):
        raise ValueError("audit_event_actor_invalid")
    if (
        not isinstance(event.event_version, int)
        or isinstance(event.event_version, bool)
        or event.event_version != 1
    ):
        raise ValueError("audit_event_version_invalid")
    if not isinstance(event.occurred_at, int) or event.occurred_at < 0:
        raise ValueError("audit_event_time_invalid")
    if not isinstance(event.sequence, int) or event.sequence <= 0:
        raise ValueError("audit_event_sequence_invalid")
    if not isinstance(event.revocation_epoch, int) or event.revocation_epoch < 0:
        raise ValueError("audit_event_epoch_invalid")
    return RedactedAuditEvent(
        event_id=event.event_id,
        event_type=event.event_type,
        event_version=event.event_version,
        occurred_at=event.occurred_at,
        sequence=event.sequence,
        grant_id=event.grant_id,
        scope_digest=event.scope_digest,
        policy_version=event.policy_version,
        revocation_epoch=event.revocation_epoch,
        outcome=event.outcome,
        reason_code=event.reason_code,
        correlation_digest=event.correlation_digest,
    )
