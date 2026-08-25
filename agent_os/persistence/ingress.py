"""Pure A1 metadata validation and receipt coordination vocabulary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from .contracts import (
    ArtifactIdentity,
    ArtifactRole,
    CapabilityConsumer,
    CapabilityMetadata,
    CanonicalJsonPolicy,
    IngressBinding,
    IngressErrorCode,
    IngressIdentity,
    IngressPurpose,
    IngressProvenance,
    IngressReceipt,
    IngressState,
    ReceiptCommitOutcome,
    ReceiptCommitResult,
    RedactedIngressReceipt,
    ScannerVerdict,
    ScannerVerdictStatus,
    SourceKind,
    StateTransition,
    StateTransitionResult,
    TransitionContext,
    TransitionReason,
    TrustedSupplier,
    TenantContext,
)

PAPERRUN_DISABLED_ERROR: Final[IngressErrorCode] = IngressErrorCode.SUPPLIER_DISABLED
_RESERVED_RETENTION_CLASSES: Final[frozenset[str]] = frozenset(
    {"", "reserved", "unspecified", "unknown"}
)

_SUPPLIER_PURPOSE: Final[dict[TrustedSupplier, IngressPurpose]] = {
    TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1: IngressPurpose.PAPERRUN_RECORDING_INGRESS,
    TrustedSupplier.FIXTURE_TEST_INGRESS_V1: IngressPurpose.FIXTURE_TEST_INGRESS,
}
_SUPPLIER_SOURCE: Final[dict[TrustedSupplier, SourceKind]] = {
    TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1: SourceKind.PAPER_RUN_RECORDING,
    TrustedSupplier.FIXTURE_TEST_INGRESS_V1: SourceKind.SYNTHETIC_FIXTURE,
}
_SUPPLIER_ROLE: Final[dict[TrustedSupplier, ArtifactRole]] = {
    TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1: ArtifactRole.PAPER_RUN_RECORDING,
    TrustedSupplier.FIXTURE_TEST_INGRESS_V1: ArtifactRole.FIXTURE_METADATA,
}
_ALLOWED_TRANSITIONS: Final[dict[IngressState, frozenset[IngressState]]] = {
    IngressState.METADATA_RECEIVED: frozenset(
        {IngressState.CANONICAL_METADATA_DECLARED, IngressState.REJECTED}
    ),
    IngressState.CANONICAL_METADATA_DECLARED: frozenset(
        {IngressState.SCANNER_VERDICT_DECLARED, IngressState.REJECTED}
    ),
    IngressState.SCANNER_VERDICT_DECLARED: frozenset(
        {IngressState.METADATA_READY, IngressState.METADATA_QUARANTINED}
    ),
}
_TRANSITION_REASONS: Final[dict[tuple[IngressState, IngressState], TransitionReason]] = {
    (
        IngressState.METADATA_RECEIVED,
        IngressState.CANONICAL_METADATA_DECLARED,
    ): TransitionReason.METADATA_ACCEPTED,
    (IngressState.METADATA_RECEIVED, IngressState.REJECTED): TransitionReason.VALIDATION_REJECTED,
    (
        IngressState.CANONICAL_METADATA_DECLARED,
        IngressState.SCANNER_VERDICT_DECLARED,
    ): TransitionReason.SCANNER_VERDICT_DECLARED,
    (
        IngressState.CANONICAL_METADATA_DECLARED,
        IngressState.REJECTED,
    ): TransitionReason.VALIDATION_REJECTED,
    (
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_READY,
    ): TransitionReason.METADATA_READY,
    (
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_QUARANTINED,
    ): TransitionReason.METADATA_QUARANTINED,
}
_UNSAFE_QUARANTINE_STATUSES: Final[frozenset[ScannerVerdictStatus]] = frozenset(
    {
        ScannerVerdictStatus.REJECTED,
        ScannerVerdictStatus.INDETERMINATE,
        ScannerVerdictStatus.UNKNOWN,
        ScannerVerdictStatus.ERROR,
    }
)


@dataclass(frozen=True)
class IngressValidation:
    """Typed result for a metadata-only ingress preflight."""

    valid: bool
    error: IngressErrorCode | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "valid": self.valid,
            "error": self.error.value if self.error else None,
        }


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _valid_identifier(value: object, *, max_length: int = 128) -> bool:
    if not isinstance(value, str) or not value or len(value) > max_length:
        return False
    if not value.isprintable() or "/" in value or "\\" in value or "://" in value:
        return False
    return True


def _valid_policy_identifier(value: object) -> bool:
    return _valid_identifier(value, max_length=64)


def _valid_digest(value: object) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    return all(character in "0123456789abcdef" for character in value)


def _error(error: IngressErrorCode) -> IngressValidation:
    return IngressValidation(valid=False, error=error)


def valid() -> IngressValidation:
    return IngressValidation(valid=True)


def _preflight_supplier(supplier: TrustedSupplier) -> IngressValidation:
    """Return the stable A1 supplier decision before any coordinator outcome."""
    if not isinstance(supplier, TrustedSupplier):
        return _error(IngressErrorCode.SUPPLIER_DISABLED)
    if supplier is TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1:
        return _error(PAPERRUN_DISABLED_ERROR)
    if supplier is TrustedSupplier.FIXTURE_TEST_INGRESS_V1:
        return valid()
    return _error(IngressErrorCode.SUPPLIER_DISABLED)


def validate_policy(policy: CanonicalJsonPolicy) -> IngressValidation:
    if not isinstance(policy, CanonicalJsonPolicy):
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if not _valid_policy_identifier(policy.policy_version):
        return _error(IngressErrorCode.POLICY_MISMATCH)
    numeric_policy_values = (
        policy.max_raw_size_bytes,
        policy.max_canonical_size_bytes,
        policy.scanner_freshness_seconds,
        policy.scanner_validity_seconds,
    )
    if not all(_is_int(value) for value in numeric_policy_values):
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.media_type != "application/json":
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.canonicalization_profile != "canonical-json.v1":
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.max_raw_size_bytes != 8_388_608:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.max_canonical_size_bytes != 8_388_608:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.scanner_freshness_seconds != 900:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if policy.scanner_validity_seconds != 900:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    return valid()


def validate_tenant_context(context: TenantContext) -> IngressValidation:
    if not isinstance(context, TenantContext):
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    if not _valid_identifier(context.tenant_id) or not _valid_identifier(context.context_id):
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    return valid()


def validate_identity(identity: IngressIdentity, context: TenantContext) -> IngressValidation:
    if not isinstance(identity, IngressIdentity):
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    if not validate_tenant_context(context).valid:
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    values = (
        identity.tenant_id,
        identity.actor_id,
        identity.request_id,
        identity.idempotency_key,
        identity.capability_id,
        identity.nonce_id,
    )
    if not all(_valid_identifier(value) for value in values):
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    if identity.tenant_id != context.tenant_id:
        return _error(IngressErrorCode.TENANT_SCOPE_DENIED)
    return valid()


def validate_capability(
    capability: CapabilityMetadata,
    identity: IngressIdentity,
    context: TenantContext,
    *,
    now: int,
) -> IngressValidation:
    """Validate only capability metadata; the capability value itself is not authorization."""
    if not isinstance(capability, CapabilityMetadata):
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    supplier_result = _preflight_supplier(capability.supplier)
    if not supplier_result.valid:
        return supplier_result
    if not isinstance(capability.purpose, IngressPurpose):
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if capability.consumer is not CapabilityConsumer.INGRESS_COORDINATOR_V1:
        return _error(IngressErrorCode.WRONG_CONSUMER)
    if not validate_identity(identity, context).valid:
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if not _is_int(now) or now < 0:
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if not _valid_identifier(capability.capability_id):
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if not _valid_identifier(capability.tenant_id) or capability.tenant_id != context.tenant_id:
        return _error(IngressErrorCode.TENANT_SCOPE_DENIED)
    if not _valid_identifier(capability.nonce_id):
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if not _is_int(capability.issued_at) or not _is_int(capability.expires_at):
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if capability.expires_at <= capability.issued_at or capability.issued_at > now:
        return _error(IngressErrorCode.CAPABILITY_INVALID)
    if capability.expires_at <= now:
        return _error(IngressErrorCode.CAPABILITY_EXPIRED)
    if (
        capability.capability_id != identity.capability_id
        or capability.nonce_id != identity.nonce_id
    ):
        return _error(IngressErrorCode.CAPABILITY_MISMATCH)
    if capability.purpose is not _SUPPLIER_PURPOSE[capability.supplier]:
        return _error(IngressErrorCode.SUPPLIER_PURPOSE_MISMATCH)
    return valid()


def validate_provenance(
    provenance: IngressProvenance,
    policy: CanonicalJsonPolicy,
) -> IngressValidation:
    if not isinstance(provenance, IngressProvenance):
        return _error(IngressErrorCode.SUPPLIER_SOURCE_MISMATCH)
    supplier_result = _preflight_supplier(provenance.supplier)
    if not supplier_result.valid:
        return supplier_result
    if not validate_policy(policy).valid:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if provenance.purpose is not _SUPPLIER_PURPOSE.get(provenance.supplier):
        return _error(IngressErrorCode.SUPPLIER_PURPOSE_MISMATCH)
    if provenance.source_kind is not _SUPPLIER_SOURCE.get(provenance.supplier):
        return _error(IngressErrorCode.SUPPLIER_SOURCE_MISMATCH)
    if provenance.artifact_role is not _SUPPLIER_ROLE.get(provenance.supplier):
        return _error(IngressErrorCode.ARTIFACT_ROLE_MISMATCH)
    if not _valid_identifier(provenance.recording_id):
        return _error(IngressErrorCode.IDENTIFIER_INVALID)
    if not _valid_policy_identifier(provenance.schema_id):
        return _error(IngressErrorCode.IDENTIFIER_INVALID)
    if provenance.canonicalization_profile != policy.canonicalization_profile:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if provenance.policy_version != policy.policy_version:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if (
        not _valid_policy_identifier(provenance.retention_class)
        or provenance.retention_class.lower() in _RESERVED_RETENTION_CLASSES
    ):
        return _error(IngressErrorCode.RETENTION_CLASS_INVALID)
    return valid()


def validate_artifact_identity(
    artifact: ArtifactIdentity,
    provenance: IngressProvenance,
    policy: CanonicalJsonPolicy,
) -> IngressValidation:
    if not isinstance(artifact, ArtifactIdentity):
        return _error(IngressErrorCode.DIGEST_METADATA_INVALID)
    provenance_result = validate_provenance(provenance, policy)
    if not provenance_result.valid:
        return provenance_result
    if not _valid_digest(artifact.content_digest):
        return _error(IngressErrorCode.DIGEST_METADATA_INVALID)
    sizes = (artifact.raw_size_bytes, artifact.canonical_size_bytes)
    if not all(_is_int(size) and 0 < size <= 8_388_608 for size in sizes):
        return _error(IngressErrorCode.SIZE_METADATA_INVALID)
    if artifact.media_type != policy.media_type:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if artifact.canonicalization_profile != provenance.canonicalization_profile:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if artifact.schema_id != provenance.schema_id:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    if artifact.policy_version != policy.policy_version:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    return valid()


def _valid_binding_shape(binding: object) -> bool:
    return (
        isinstance(binding, IngressBinding)
        and isinstance(binding.identity, IngressIdentity)
        and isinstance(binding.provenance, IngressProvenance)
        and isinstance(binding.artifact, ArtifactIdentity)
    )


def _validate_scanner_verdict_shape(
    verdict: ScannerVerdict,
    policy: CanonicalJsonPolicy,
) -> IngressValidation:
    if not isinstance(verdict, ScannerVerdict):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not isinstance(verdict.status, ScannerVerdictStatus):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not _valid_policy_identifier(verdict.scanner_profile):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not _valid_policy_identifier(verdict.scanner_version):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not _valid_digest(verdict.content_digest):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not _is_int(verdict.canonical_size_bytes) or not (
        0 < verdict.canonical_size_bytes <= policy.max_canonical_size_bytes
    ):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not _valid_identifier(verdict.tenant_id):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not isinstance(verdict.purpose, IngressPurpose):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if (
        not _is_int(verdict.observed_at)
        or not _is_int(verdict.expires_at)
        or verdict.observed_at < 0
        or verdict.expires_at <= verdict.observed_at
    ):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    return valid()


def validate_scanner_verdict(
    verdict: ScannerVerdict,
    binding: IngressBinding,
    policy: CanonicalJsonPolicy,
    *,
    now: int,
) -> IngressValidation:
    """Validate supplied accepted scanner-result metadata; no scanner is invoked."""
    if not isinstance(binding, IngressBinding) or not _valid_binding_shape(binding):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not validate_policy(policy).valid:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    shape_result = _validate_scanner_verdict_shape(verdict, policy)
    if not shape_result.valid:
        return shape_result
    if verdict.status is not ScannerVerdictStatus.ACCEPTED:
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if verdict.content_digest != binding.artifact.content_digest:
        return _error(IngressErrorCode.SCANNER_VERDICT_MISMATCH)
    if verdict.canonical_size_bytes != binding.artifact.canonical_size_bytes:
        return _error(IngressErrorCode.SCANNER_VERDICT_MISMATCH)
    if verdict.tenant_id != binding.identity.tenant_id:
        return _error(IngressErrorCode.TENANT_SCOPE_DENIED)
    if verdict.purpose is not binding.provenance.purpose:
        return _error(IngressErrorCode.SCANNER_VERDICT_MISMATCH)
    if not _is_int(now) or now < 0:
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if verdict.observed_at > now:
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if now - verdict.observed_at > policy.scanner_freshness_seconds:
        return _error(IngressErrorCode.SCANNER_VERDICT_STALE)
    if verdict.expires_at - verdict.observed_at > policy.scanner_validity_seconds:
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if verdict.expires_at <= now:
        return _error(IngressErrorCode.SCANNER_VERDICT_STALE)
    return valid()


def _validate_quarantine_verdict(
    verdict: ScannerVerdict,
    binding: IngressBinding,
    policy: CanonicalJsonPolicy,
    *,
    now: int,
) -> IngressValidation:
    """Accept only typed unsafe verdict metadata for a logical quarantine disposition."""
    if not isinstance(binding, IngressBinding) or not _valid_binding_shape(binding):
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if not validate_policy(policy).valid:
        return _error(IngressErrorCode.POLICY_MISMATCH)
    shape_result = _validate_scanner_verdict_shape(verdict, policy)
    if not shape_result.valid:
        return shape_result
    if verdict.tenant_id != binding.identity.tenant_id:
        return _error(IngressErrorCode.TENANT_SCOPE_DENIED)
    if verdict.purpose is not binding.provenance.purpose:
        return _error(IngressErrorCode.SCANNER_VERDICT_MISMATCH)
    if not _is_int(now) or now < 0 or verdict.observed_at > now:
        return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
    if verdict.status in _UNSAFE_QUARANTINE_STATUSES:
        return valid()
    if verdict.content_digest != binding.artifact.content_digest:
        return valid()
    if verdict.canonical_size_bytes != binding.artifact.canonical_size_bytes:
        return valid()
    if now - verdict.observed_at > policy.scanner_freshness_seconds:
        return valid()
    if verdict.expires_at - verdict.observed_at > policy.scanner_validity_seconds:
        return valid()
    if verdict.expires_at <= now:
        return valid()
    return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)


def validate_ingress_metadata(
    identity: IngressIdentity,
    capability: CapabilityMetadata,
    provenance: IngressProvenance,
    artifact: ArtifactIdentity,
    context: TenantContext,
    policy: CanonicalJsonPolicy,
    *,
    now: int,
    scanner: ScannerVerdict | None = None,
) -> IngressValidation:
    """Validate supplied control metadata only; no content-dependent operation occurs."""
    if not isinstance(provenance, IngressProvenance):
        return _error(IngressErrorCode.SUPPLIER_SOURCE_MISMATCH)
    supplier_result = _preflight_supplier(provenance.supplier)
    if not supplier_result.valid:
        return supplier_result
    checks = (
        validate_identity(identity, context),
        validate_capability(capability, identity, context, now=now),
        validate_provenance(provenance, policy),
        validate_artifact_identity(artifact, provenance, policy),
    )
    for check in checks:
        if not check.valid:
            return check
    if capability.supplier is not provenance.supplier:
        return _error(IngressErrorCode.CAPABILITY_MISMATCH)
    if capability.purpose is not provenance.purpose:
        return _error(IngressErrorCode.SUPPLIER_PURPOSE_MISMATCH)
    if scanner is not None:
        binding = IngressBinding(identity=identity, provenance=provenance, artifact=artifact)
        return validate_scanner_verdict(scanner, binding, policy, now=now)
    return valid()


def _validate_transition_context(context: TransitionContext) -> IngressValidation:
    """Validate the typed coordinator context before any state or outcome decision."""
    if not isinstance(context, TransitionContext):
        return _error(IngressErrorCode.STATE_TRANSITION_INVALID)
    if not _valid_binding_shape(context.binding):
        return _error(IngressErrorCode.IDENTITY_INCOMPLETE)
    if not _is_int(context.now) or context.now < 0:
        return _error(IngressErrorCode.STATE_TRANSITION_INVALID)
    return validate_ingress_metadata(
        context.binding.identity,
        context.capability,
        context.binding.provenance,
        context.binding.artifact,
        context.tenant,
        context.policy,
        now=context.now,
        scanner=None,
    )


def _validate_transition_evidence(
    target: IngressState,
    context: TransitionContext,
) -> IngressValidation:
    """Require supplied metadata evidence; never perform the named operation."""
    if target is IngressState.CANONICAL_METADATA_DECLARED:
        return validate_policy(context.policy)
    if target is IngressState.SCANNER_VERDICT_DECLARED:
        if context.scanner is None:
            return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
        return _validate_scanner_verdict_shape(context.scanner, context.policy)
    if target is IngressState.METADATA_READY:
        if context.scanner is None:
            return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
        return validate_scanner_verdict(
            context.scanner,
            context.binding,
            context.policy,
            now=context.now,
        )
    if target is IngressState.METADATA_QUARANTINED:
        if context.scanner is None:
            return _error(IngressErrorCode.SCANNER_VERDICT_INVALID)
        return _validate_quarantine_verdict(
            context.scanner,
            context.binding,
            context.policy,
            now=context.now,
        )
    return valid()


def advance_state(
    current: IngressState,
    target: IngressState,
    reason: TransitionReason | None,
    *,
    context: TransitionContext,
    occurred_at: int,
    previous_occurred_at: int | None = None,
) -> StateTransitionResult:
    """Coordinate a metadata-only transition; aborted is a logical disposition only."""
    context_result = _validate_transition_context(context)
    safe_state = current if isinstance(current, IngressState) else IngressState.METADATA_RECEIVED
    if not context_result.valid:
        return StateTransitionResult(False, safe_state, error=context_result.error)
    if not isinstance(current, IngressState) or not isinstance(target, IngressState):
        return StateTransitionResult(
            False, safe_state, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    if not isinstance(reason, TransitionReason):
        return StateTransitionResult(
            False, current, error=IngressErrorCode.TRANSITION_REASON_REQUIRED
        )
    if not _is_int(occurred_at) or occurred_at < 0:
        return StateTransitionResult(
            False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    if previous_occurred_at is not None and (
        not _is_int(previous_occurred_at) or occurred_at < previous_occurred_at
    ):
        return StateTransitionResult(
            False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    if target is IngressState.METADATA_ABORTED and current not in {
        IngressState.REJECTED,
        IngressState.METADATA_QUARANTINED,
        IngressState.METADATA_ABORTED,
    }:
        if reason is not TransitionReason.METADATA_ABORTED:
            return StateTransitionResult(
                False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
            )
        transition = StateTransition(current, target, reason, occurred_at)
        return StateTransitionResult(True, target, transition=transition)
    if current in {
        IngressState.REJECTED,
        IngressState.METADATA_QUARANTINED,
        IngressState.METADATA_ABORTED,
    }:
        return StateTransitionResult(
            False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    if target not in _ALLOWED_TRANSITIONS.get(current, frozenset()):
        return StateTransitionResult(
            False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    if _TRANSITION_REASONS.get((current, target)) is not reason:
        return StateTransitionResult(
            False, current, error=IngressErrorCode.STATE_TRANSITION_INVALID
        )
    evidence_result = _validate_transition_evidence(target, context)
    if not evidence_result.valid:
        return StateTransitionResult(False, current, error=evidence_result.error)
    transition = StateTransition(current, target, reason, occurred_at)
    return StateTransitionResult(True, target, transition=transition)


def _binding_key(binding: IngressBinding) -> tuple[object, ...]:
    identity = binding.identity
    provenance = binding.provenance
    artifact = binding.artifact
    return (
        identity.tenant_id,
        identity.actor_id,
        identity.request_id,
        identity.idempotency_key,
        identity.capability_id,
        identity.nonce_id,
        provenance.supplier,
        provenance.source_kind,
        provenance.purpose,
        provenance.recording_id,
        provenance.artifact_role,
        provenance.schema_id,
        provenance.canonicalization_profile,
        provenance.policy_version,
        provenance.retention_class,
        artifact.content_digest,
        artifact.raw_size_bytes,
        artifact.canonical_size_bytes,
        artifact.media_type,
        artifact.canonicalization_profile,
        artifact.schema_id,
        artifact.policy_version,
    )


def _classify_idempotency(
    existing: IngressReceipt | None,
    incoming: IngressReceipt,
    context: TenantContext,
) -> ReceiptCommitResult:
    """Private pure retry classification; not a public ingress coordinator."""
    if not isinstance(incoming, IngressReceipt) or not _valid_binding_shape(incoming.binding):
        return ReceiptCommitResult(None, IngressErrorCode.IDENTITY_INCOMPLETE)
    incoming_supplier = _preflight_supplier(incoming.binding.provenance.supplier)
    if not incoming_supplier.valid:
        return ReceiptCommitResult(None, incoming_supplier.error)
    if existing is not None:
        if not isinstance(existing, IngressReceipt) or not _valid_binding_shape(existing.binding):
            return ReceiptCommitResult(None, IngressErrorCode.IDENTITY_INCOMPLETE)
        existing_supplier = _preflight_supplier(existing.binding.provenance.supplier)
        if not existing_supplier.valid:
            return ReceiptCommitResult(None, existing_supplier.error)
    if not validate_tenant_context(context).valid:
        return ReceiptCommitResult(None, IngressErrorCode.TENANT_SCOPE_DENIED)
    incoming_identity = incoming.binding.identity
    if incoming_identity.tenant_id != context.tenant_id:
        return ReceiptCommitResult(None, IngressErrorCode.TENANT_SCOPE_DENIED)
    if existing is None:
        return ReceiptCommitResult(ReceiptCommitOutcome.CREATED, receipt=None)
    if existing.binding.identity.tenant_id != context.tenant_id:
        return ReceiptCommitResult(None, IngressErrorCode.TENANT_SCOPE_DENIED)
    if existing.binding.identity.idempotency_key != incoming_identity.idempotency_key:
        return ReceiptCommitResult(ReceiptCommitOutcome.CREATED, receipt=None)
    if _binding_key(existing.binding) == _binding_key(incoming.binding):
        return ReceiptCommitResult(ReceiptCommitOutcome.IDEMPOTENCY_MATCHED, receipt=existing)
    return ReceiptCommitResult(ReceiptCommitOutcome.CONFLICT, IngressErrorCode.IDEMPOTENCY_CONFLICT)


def redact_receipt(receipt: IngressReceipt) -> RedactedIngressReceipt:
    """Return the immutable safe whitelist projection and nothing else."""
    return receipt.to_redacted()
