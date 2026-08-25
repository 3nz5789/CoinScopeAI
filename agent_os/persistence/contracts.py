"""Immutable A1 metadata contracts for future ingress coordination."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

POLICY_VERSION_V1: Final[str] = "canonical-json-policy-v1"
MEDIA_TYPE_V1: Final[str] = "application/json"
CANONICALIZATION_V1: Final[str] = "canonical-json.v1"
MAX_SIZE_BYTES_V1: Final[int] = 8_388_608
SCANNER_WINDOW_SECONDS_V1: Final[int] = 900


class TrustedSupplier(str, Enum):
    """Server-created supplier identities approved by A1."""

    PAPERRUN_RECORDING_CAPTURE_V1 = "PAPERRUN_RECORDING_CAPTURE_V1"
    FIXTURE_TEST_INGRESS_V1 = "FIXTURE_TEST_INGRESS_V1"


class IngressPurpose(str, Enum):
    """Explicit purposes bound to the trusted supplier vocabulary."""

    PAPERRUN_RECORDING_INGRESS = "paperrun_recording_ingress"
    FIXTURE_TEST_INGRESS = "fixture_test_ingress"


class SourceKind(str, Enum):
    """Safe provenance categories represented by A1 metadata."""

    PAPER_RUN_RECORDING = "paper_run_recording"
    SYNTHETIC_FIXTURE = "synthetic_fixture"


class ArtifactRole(str, Enum):
    """Manifest-declared roles allowed by the two A1 supplier categories."""

    PAPER_RUN_RECORDING = "paper_run_recording"
    FIXTURE_METADATA = "fixture_metadata"


class CapabilityConsumer(str, Enum):
    """Closed consumer vocabulary for future server-owned coordination."""

    INGRESS_COORDINATOR_V1 = "ingress_coordinator_v1"


class ScannerVerdictStatus(str, Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    INDETERMINATE = "indeterminate"
    UNKNOWN = "unknown"
    ERROR = "error"


class IngressState(str, Enum):
    """Metadata-only lifecycle labels; no value asserts a material operation."""

    METADATA_RECEIVED = "metadata_received"
    CANONICAL_METADATA_DECLARED = "canonical_metadata_declared"
    SCANNER_VERDICT_DECLARED = "scanner_verdict_declared"
    METADATA_READY = "metadata_ready"
    REJECTED = "rejected"
    METADATA_QUARANTINED = "metadata_quarantined"
    METADATA_ABORTED = "metadata_aborted"


class TransitionReason(str, Enum):
    METADATA_ACCEPTED = "metadata_accepted"
    VALIDATION_REJECTED = "validation_rejected"
    SCANNER_VERDICT_DECLARED = "scanner_verdict_declared"
    METADATA_READY = "metadata_ready"
    METADATA_QUARANTINED = "metadata_quarantined"
    METADATA_ABORTED = "metadata_aborted"


class ReceiptStatus(str, Enum):
    """Safe metadata receipt statuses; none asserts storage or execution."""

    METADATA_READY = "metadata_ready"
    IDEMPOTENCY_MATCHED = "idempotency_matched"
    REJECTED = "rejected"
    METADATA_QUARANTINED = "metadata_quarantined"


class ReceiptCommitOutcome(str, Enum):
    CREATED = "created"
    IDEMPOTENCY_MATCHED = "idempotency_matched"
    CONFLICT = "conflict"


class IngressErrorCode(str, Enum):
    IDENTITY_INCOMPLETE = "identity_incomplete"
    IDENTIFIER_INVALID = "identifier_invalid"
    CAPABILITY_INVALID = "capability_invalid"
    CAPABILITY_EXPIRED = "capability_expired"
    CAPABILITY_MISMATCH = "capability_mismatch"
    WRONG_CONSUMER = "wrong_consumer"
    SUPPLIER_DISABLED = "supplier_disabled"
    SUPPLIER_PURPOSE_MISMATCH = "supplier_purpose_mismatch"
    SUPPLIER_SOURCE_MISMATCH = "supplier_source_mismatch"
    ARTIFACT_ROLE_MISMATCH = "artifact_role_mismatch"
    POLICY_MISMATCH = "policy_mismatch"
    RETENTION_CLASS_INVALID = "retention_class_invalid"
    DIGEST_METADATA_INVALID = "digest_metadata_invalid"
    SIZE_METADATA_INVALID = "size_metadata_invalid"
    SCANNER_VERDICT_INVALID = "scanner_verdict_invalid"
    SCANNER_VERDICT_STALE = "scanner_verdict_stale"
    SCANNER_VERDICT_MISMATCH = "scanner_verdict_mismatch"
    STATE_TRANSITION_INVALID = "state_transition_invalid"
    TRANSITION_REASON_REQUIRED = "transition_reason_required"
    TENANT_SCOPE_DENIED = "tenant_scope_denied"
    IDEMPOTENCY_CONFLICT = "idempotency_conflict"
    METADATA_ABORTED = "metadata_aborted"


@dataclass(frozen=True)
class CanonicalJsonPolicy:
    """Versioned policy metadata; it performs no content operation."""

    policy_version: str = POLICY_VERSION_V1
    media_type: str = MEDIA_TYPE_V1
    canonicalization_profile: str = CANONICALIZATION_V1
    max_raw_size_bytes: int = MAX_SIZE_BYTES_V1
    max_canonical_size_bytes: int = MAX_SIZE_BYTES_V1
    scanner_freshness_seconds: int = SCANNER_WINDOW_SECONDS_V1
    scanner_validity_seconds: int = SCANNER_WINDOW_SECONDS_V1

    def to_dict(self) -> dict[str, object]:
        return {
            "policy_version": self.policy_version,
            "media_type": self.media_type,
            "canonicalization_profile": self.canonicalization_profile,
            "max_raw_size_bytes": self.max_raw_size_bytes,
            "max_canonical_size_bytes": self.max_canonical_size_bytes,
            "scanner_freshness_seconds": self.scanner_freshness_seconds,
            "scanner_validity_seconds": self.scanner_validity_seconds,
        }


@dataclass(frozen=True)
class TenantContext:
    """Tenant context supplied by a future server-owned boundary."""

    tenant_id: str
    context_id: str

    def to_dict(self) -> dict[str, object]:
        return {"tenant_id": self.tenant_id, "context_id": self.context_id}


@dataclass(frozen=True)
class CapabilityMetadata:
    """Opaque capability metadata; the value is not an authorization mechanism."""

    capability_id: str
    tenant_id: str
    supplier: TrustedSupplier
    purpose: IngressPurpose
    consumer: CapabilityConsumer
    nonce_id: str
    issued_at: int
    expires_at: int

    def to_dict(self) -> dict[str, object]:
        return {
            "capability_id": self.capability_id,
            "tenant_id": self.tenant_id,
            "supplier": self.supplier.value,
            "purpose": self.purpose.value,
            "consumer": self.consumer.value,
            "nonce_id": self.nonce_id,
            "issued_at": self.issued_at,
            "expires_at": self.expires_at,
        }


@dataclass(frozen=True)
class IngressIdentity:
    """Correlation fields bound to one tenant and one future capability."""

    tenant_id: str
    actor_id: str
    request_id: str
    idempotency_key: str
    capability_id: str
    nonce_id: str

    def to_dict(self) -> dict[str, object]:
        return {
            "tenant_id": self.tenant_id,
            "actor_id": self.actor_id,
            "request_id": self.request_id,
            "idempotency_key": self.idempotency_key,
            "capability_id": self.capability_id,
            "nonce_id": self.nonce_id,
        }


@dataclass(frozen=True)
class IngressProvenance:
    """Explicit source and policy metadata with no source locator."""

    supplier: TrustedSupplier
    source_kind: SourceKind
    purpose: IngressPurpose
    recording_id: str
    artifact_role: ArtifactRole
    schema_id: str
    canonicalization_profile: str
    policy_version: str
    retention_class: str

    def to_dict(self) -> dict[str, object]:
        return {
            "supplier": self.supplier.value,
            "source_kind": self.source_kind.value,
            "purpose": self.purpose.value,
            "recording_id": self.recording_id,
            "artifact_role": self.artifact_role.value,
            "schema_id": self.schema_id,
            "canonicalization_profile": self.canonicalization_profile,
            "policy_version": self.policy_version,
            "retention_class": self.retention_class,
        }


@dataclass(frozen=True)
class ArtifactIdentity:
    """Supplied artifact identity metadata; no identity is derived here."""

    content_digest: str
    raw_size_bytes: int
    canonical_size_bytes: int
    media_type: str
    canonicalization_profile: str
    schema_id: str
    policy_version: str

    def to_dict(self) -> dict[str, object]:
        return {
            "content_digest": self.content_digest,
            "raw_size_bytes": self.raw_size_bytes,
            "canonical_size_bytes": self.canonical_size_bytes,
            "media_type": self.media_type,
            "canonicalization_profile": self.canonicalization_profile,
            "schema_id": self.schema_id,
            "policy_version": self.policy_version,
        }


@dataclass(frozen=True)
class ScannerVerdict:
    """Supplied scanner-result metadata; no scanner is invoked by A1."""

    status: ScannerVerdictStatus
    scanner_profile: str
    scanner_version: str
    content_digest: str
    canonical_size_bytes: int
    tenant_id: str
    purpose: IngressPurpose
    observed_at: int
    expires_at: int

    def to_dict(self) -> dict[str, object]:
        return {
            "status": self.status.value,
            "scanner_profile": self.scanner_profile,
            "scanner_version": self.scanner_version,
            "content_digest": self.content_digest,
            "canonical_size_bytes": self.canonical_size_bytes,
            "tenant_id": self.tenant_id,
            "purpose": self.purpose.value,
            "observed_at": self.observed_at,
            "expires_at": self.expires_at,
        }


@dataclass(frozen=True)
class IngressBinding:
    """Complete immutable binding used for tenant-scoped idempotency comparison."""

    identity: IngressIdentity
    provenance: IngressProvenance
    artifact: ArtifactIdentity

    def to_dict(self) -> dict[str, object]:
        return {
            "identity": self.identity.to_dict(),
            "provenance": self.provenance.to_dict(),
            "artifact": self.artifact.to_dict(),
        }


@dataclass(frozen=True)
class TransitionContext:
    """Typed supplied metadata required by the public transition coordinator."""

    tenant: TenantContext
    capability: CapabilityMetadata
    policy: CanonicalJsonPolicy
    binding: IngressBinding
    now: int
    scanner: ScannerVerdict | None = None


@dataclass(frozen=True)
class StateTransition:
    from_state: IngressState
    to_state: IngressState
    reason: TransitionReason
    occurred_at: int

    def to_dict(self) -> dict[str, object]:
        return {
            "from_state": self.from_state.value,
            "to_state": self.to_state.value,
            "reason": self.reason.value,
            "occurred_at": self.occurred_at,
        }


@dataclass(frozen=True)
class StateTransitionResult:
    accepted: bool
    state: IngressState
    transition: StateTransition | None = None
    error: IngressErrorCode | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "accepted": self.accepted,
            "state": self.state.value,
            "transition": self.transition.to_dict() if self.transition else None,
            "error": self.error.value if self.error else None,
        }


@dataclass(frozen=True)
class RedactedIngressReceipt:
    """Whitelist-only receipt intended for review or ordinary output."""

    receipt_id: str
    request_id: str
    supplier: TrustedSupplier
    source_kind: SourceKind
    purpose: IngressPurpose
    artifact_role: ArtifactRole
    schema_id: str
    canonicalization_profile: str
    policy_version: str
    state: IngressState
    status: ReceiptStatus
    content_digest: str | None
    raw_size_bytes: int | None
    canonical_size_bytes: int | None
    scanner_status: ScannerVerdictStatus | None
    scanner_profile: str | None
    scanner_version: str | None
    scanner_observed_at: int | None
    scanner_expires_at: int | None
    occurred_at: int
    error: IngressErrorCode | None

    def to_dict(self) -> dict[str, object]:
        return {
            "receipt_id": self.receipt_id,
            "request_id": self.request_id,
            "supplier": self.supplier.value,
            "source_kind": self.source_kind.value,
            "purpose": self.purpose.value,
            "artifact_role": self.artifact_role.value,
            "schema_id": self.schema_id,
            "canonicalization_profile": self.canonicalization_profile,
            "policy_version": self.policy_version,
            "state": self.state.value,
            "status": self.status.value,
            "content_digest": self.content_digest,
            "raw_size_bytes": self.raw_size_bytes,
            "canonical_size_bytes": self.canonical_size_bytes,
            "scanner_status": self.scanner_status.value if self.scanner_status else None,
            "scanner_profile": self.scanner_profile,
            "scanner_version": self.scanner_version,
            "scanner_observed_at": self.scanner_observed_at,
            "scanner_expires_at": self.scanner_expires_at,
            "occurred_at": self.occurred_at,
            "error": self.error.value if self.error else None,
        }


@dataclass(frozen=True)
class IngressReceipt:
    """Internal metadata receipt with a binding-derived safe projection."""

    receipt_id: str
    binding: IngressBinding
    state: IngressState
    status: ReceiptStatus
    occurred_at: int
    scanner: ScannerVerdict | None = None
    error: IngressErrorCode | None = None

    def to_redacted(self) -> RedactedIngressReceipt:
        artifact = self.binding.artifact
        scanner = self.scanner
        return RedactedIngressReceipt(
            receipt_id=self.receipt_id,
            request_id=self.binding.identity.request_id,
            supplier=self.binding.provenance.supplier,
            source_kind=self.binding.provenance.source_kind,
            purpose=self.binding.provenance.purpose,
            artifact_role=self.binding.provenance.artifact_role,
            schema_id=self.binding.provenance.schema_id,
            canonicalization_profile=self.binding.provenance.canonicalization_profile,
            policy_version=self.binding.provenance.policy_version,
            state=self.state,
            status=self.status,
            content_digest=artifact.content_digest,
            raw_size_bytes=artifact.raw_size_bytes,
            canonical_size_bytes=artifact.canonical_size_bytes,
            scanner_status=scanner.status if scanner else None,
            scanner_profile=scanner.scanner_profile if scanner else None,
            scanner_version=scanner.scanner_version if scanner else None,
            scanner_observed_at=scanner.observed_at if scanner else None,
            scanner_expires_at=scanner.expires_at if scanner else None,
            occurred_at=self.occurred_at,
            error=self.error,
        )

    def to_dict(self) -> dict[str, object]:
        return self.to_redacted().to_dict()


@dataclass(frozen=True)
class ReceiptCommitResult:
    """Typed logical outcome for a future idempotent metadata operation."""

    outcome: ReceiptCommitOutcome | None
    error: IngressErrorCode | None = None
    receipt: IngressReceipt | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "outcome": self.outcome.value if self.outcome else None,
            "error": self.error.value if self.error else None,
            "receipt": self.receipt.to_dict() if self.receipt else None,
        }
