"""A4-v1 append-only, metadata-only audit contracts."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AuditEventType(str, Enum):
    AUTH_ISSUED = "AUTH_ISSUED"
    AUTH_CONSUME_ACCEPTED = "AUTH_CONSUME_ACCEPTED"
    AUTH_CONSUME_REJECTED = "AUTH_CONSUME_REJECTED"
    AUTH_REVOKED = "AUTH_REVOKED"
    AUTH_EXPIRED = "AUTH_EXPIRED"
    AUTH_IDEMPOTENCY_REPLAY = "AUTH_IDEMPOTENCY_REPLAY"
    AUTH_IDEMPOTENCY_CONFLICT = "AUTH_IDEMPOTENCY_CONFLICT"
    AUTH_ACCESS_DENIED = "AUTH_ACCESS_DENIED"


class AuditOutcome(str, Enum):
    ACCEPTED = "accepted"
    DENIED = "denied"
    REPLAYED = "replayed"
    CONFLICT = "conflict"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    tenant_id: str
    workspace_id: str
    event_type: AuditEventType
    event_version: int
    occurred_at: int
    sequence: int
    actor_digest: str
    grant_id: str | None
    request_digest: str
    scope_digest: str | None
    policy_version: str | None
    revocation_epoch: int
    outcome: AuditOutcome
    reason_code: str | None
    correlation_digest: str | None
    event_digest: str

    def __post_init__(self) -> None:
        if not isinstance(self.event_type, AuditEventType):
            raise TypeError("audit_event_type_invalid")
        if not isinstance(self.outcome, AuditOutcome):
            raise TypeError("audit_outcome_invalid")

    def to_dict(self) -> dict[str, object]:
        return {
            "event_id": self.event_id,
            "tenant_id": self.tenant_id,
            "workspace_id": self.workspace_id,
            "event_type": self.event_type.value,
            "event_version": self.event_version,
            "occurred_at": self.occurred_at,
            "sequence": self.sequence,
            "actor_digest": self.actor_digest,
            "grant_id": self.grant_id,
            "request_digest": self.request_digest,
            "scope_digest": self.scope_digest,
            "policy_version": self.policy_version,
            "revocation_epoch": self.revocation_epoch,
            "outcome": self.outcome.value,
            "reason_code": self.reason_code,
            "correlation_digest": self.correlation_digest,
            "event_digest": self.event_digest,
        }


@dataclass(frozen=True)
class RedactedAuditEvent:
    event_id: str
    event_type: AuditEventType
    event_version: int
    occurred_at: int
    sequence: int
    grant_id: str | None
    scope_digest: str | None
    policy_version: str | None
    revocation_epoch: int
    outcome: AuditOutcome
    reason_code: str | None
    correlation_digest: str | None

    def __post_init__(self) -> None:
        if not isinstance(self.event_type, AuditEventType):
            raise TypeError("redacted_audit_event_type_invalid")
        if not isinstance(self.outcome, AuditOutcome):
            raise TypeError("redacted_audit_outcome_invalid")

    def to_dict(self) -> dict[str, object]:
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "event_version": self.event_version,
            "occurred_at": self.occurred_at,
            "sequence": self.sequence,
            "grant_id": self.grant_id,
            "scope_digest": self.scope_digest,
            "policy_version": self.policy_version,
            "revocation_epoch": self.revocation_epoch,
            "outcome": self.outcome.value,
            "reason_code": self.reason_code,
            "correlation_digest": self.correlation_digest,
        }
