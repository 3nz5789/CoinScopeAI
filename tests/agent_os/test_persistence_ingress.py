from dataclasses import FrozenInstanceError, replace

import pytest

from agent_os.persistence.contracts import (
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
    ReceiptStatus,
    ScannerVerdict,
    ScannerVerdictStatus,
    SourceKind,
    TransitionContext,
    TransitionReason,
    TrustedSupplier,
    TenantContext,
)
from agent_os.persistence.ingress import (
    _classify_idempotency,
    _preflight_supplier,
    advance_state,
    redact_receipt,
    validate_artifact_identity,
    validate_capability,
    validate_ingress_metadata,
    validate_provenance,
    validate_scanner_verdict,
)

NOW = 1_700_000_000
DIGEST = "a" * 64
CONTEXT = TenantContext(tenant_id="tenant-a", context_id="ctx-a")
POLICY = CanonicalJsonPolicy()


def identity(**overrides: object) -> IngressIdentity:
    values: dict[str, object] = {
        "tenant_id": "tenant-a",
        "actor_id": "actor-a",
        "request_id": "request-a",
        "idempotency_key": "idem-a",
        "capability_id": "cap-a",
        "nonce_id": "nonce-a",
    }
    values.update(overrides)
    return IngressIdentity(**values)


def capability(**overrides: object) -> CapabilityMetadata:
    values: dict[str, object] = {
        "capability_id": "cap-a",
        "tenant_id": "tenant-a",
        "supplier": TrustedSupplier.FIXTURE_TEST_INGRESS_V1,
        "purpose": IngressPurpose.FIXTURE_TEST_INGRESS,
        "consumer": CapabilityConsumer.INGRESS_COORDINATOR_V1,
        "nonce_id": "nonce-a",
        "issued_at": NOW - 30,
        "expires_at": NOW + 870,
    }
    values.update(overrides)
    return CapabilityMetadata(**values)


def provenance(**overrides: object) -> IngressProvenance:
    values: dict[str, object] = {
        "supplier": TrustedSupplier.FIXTURE_TEST_INGRESS_V1,
        "source_kind": SourceKind.SYNTHETIC_FIXTURE,
        "purpose": IngressPurpose.FIXTURE_TEST_INGRESS,
        "recording_id": "recording-a",
        "artifact_role": ArtifactRole.FIXTURE_METADATA,
        "schema_id": "fixture-schema-v1",
        "canonicalization_profile": "canonical-json.v1",
        "policy_version": POLICY.policy_version,
        "retention_class": "fixture-ephemeral-v1",
    }
    values.update(overrides)
    return IngressProvenance(**values)


def artifact(**overrides: object) -> ArtifactIdentity:
    values: dict[str, object] = {
        "content_digest": DIGEST,
        "raw_size_bytes": 128,
        "canonical_size_bytes": 96,
        "media_type": "application/json",
        "canonicalization_profile": "canonical-json.v1",
        "schema_id": "fixture-schema-v1",
        "policy_version": POLICY.policy_version,
    }
    values.update(overrides)
    return ArtifactIdentity(**values)


def binding(**overrides: object) -> IngressBinding:
    values: dict[str, object] = {
        "identity": identity(),
        "provenance": provenance(),
        "artifact": artifact(),
    }
    values.update(overrides)
    return IngressBinding(**values)


def scanner(**overrides: object) -> ScannerVerdict:
    values: dict[str, object] = {
        "status": ScannerVerdictStatus.ACCEPTED,
        "scanner_profile": "fixture-scanner-v1",
        "scanner_version": "1.0",
        "content_digest": DIGEST,
        "canonical_size_bytes": 96,
        "tenant_id": "tenant-a",
        "purpose": IngressPurpose.FIXTURE_TEST_INGRESS,
        "observed_at": NOW - 60,
        "expires_at": NOW + 840,
    }
    values.update(overrides)
    return ScannerVerdict(**values)


def transition_context(
    *,
    binding_value: IngressBinding | None = None,
    policy: CanonicalJsonPolicy = POLICY,
    scanner_value: ScannerVerdict | None = None,
    now: int = NOW,
) -> TransitionContext:
    selected_binding = binding_value or binding()
    return TransitionContext(
        tenant=CONTEXT,
        capability=capability(),
        policy=policy,
        binding=selected_binding,
        now=now,
        scanner=scanner_value,
    )


def receipt(**overrides: object) -> IngressReceipt:
    values: dict[str, object] = {
        "receipt_id": "receipt-a",
        "binding": binding(),
        "state": IngressState.METADATA_READY,
        "status": ReceiptStatus.METADATA_READY,
        "occurred_at": NOW,
        "scanner": scanner(),
    }
    values.update(overrides)
    return IngressReceipt(**values)


def test_policy_and_contracts_are_immutable_and_stable() -> None:
    assert POLICY.to_dict()["max_raw_size_bytes"] == 8_388_608
    assert POLICY.to_dict()["scanner_validity_seconds"] == 900
    assert identity().to_dict()["idempotency_key"] == "idem-a"
    assert artifact().to_dict()["content_digest"] == DIGEST
    with pytest.raises(FrozenInstanceError):
        POLICY.media_type = "text/plain"  # type: ignore[misc]


def test_paperrun_supplier_is_disabled_before_metadata_validation() -> None:
    assert _preflight_supplier(TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1).error is (
        IngressErrorCode.SUPPLIER_DISABLED
    )
    result = validate_ingress_metadata(
        identity(),
        capability(supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1),
        provenance(supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1),
        artifact(content_digest="not-a-digest"),
        CONTEXT,
        POLICY,
        now=NOW,
    )
    assert result.valid is False
    assert result.error is IngressErrorCode.SUPPLIER_DISABLED


def test_fixture_supplier_requires_exact_purpose_source_and_role() -> None:
    assert validate_provenance(provenance(), POLICY).valid
    assert (
        validate_provenance(
            provenance(purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS), POLICY
        ).error
        is IngressErrorCode.SUPPLIER_PURPOSE_MISMATCH
    )
    assert (
        validate_provenance(provenance(source_kind=SourceKind.PAPER_RUN_RECORDING), POLICY).error
        is IngressErrorCode.SUPPLIER_SOURCE_MISMATCH
    )
    assert (
        validate_provenance(
            provenance(artifact_role=ArtifactRole.PAPER_RUN_RECORDING), POLICY
        ).error
        is IngressErrorCode.ARTIFACT_ROLE_MISMATCH
    )


def test_identity_capability_and_expiry_are_fail_closed() -> None:
    assert validate_capability(capability(), identity(), CONTEXT, now=NOW).valid
    assert (
        validate_capability(
            capability(capability_id="other-cap"), identity(), CONTEXT, now=NOW
        ).error
        is IngressErrorCode.CAPABILITY_MISMATCH
    )
    assert (
        validate_capability(capability(expires_at=NOW), identity(), CONTEXT, now=NOW).error
        is IngressErrorCode.CAPABILITY_EXPIRED
    )
    assert (
        validate_capability(capability(issued_at=NOW + 1), identity(), CONTEXT, now=NOW).error
        is IngressErrorCode.CAPABILITY_INVALID
    )
    assert (
        validate_capability(
            capability(consumer="wrong-consumer"), identity(), CONTEXT, now=NOW
        ).error
        is IngressErrorCode.WRONG_CONSUMER
    )
    assert (
        validate_capability(capability(tenant_id="tenant-b"), identity(), CONTEXT, now=NOW).error
        is IngressErrorCode.TENANT_SCOPE_DENIED
    )


def test_supplied_artifact_metadata_is_validated_without_content_operations() -> None:
    assert validate_artifact_identity(artifact(), provenance(), POLICY).valid
    assert (
        validate_artifact_identity(artifact(content_digest="A" * 64), provenance(), POLICY).error
        is IngressErrorCode.DIGEST_METADATA_INVALID
    )
    assert (
        validate_artifact_identity(artifact(raw_size_bytes=8_388_609), provenance(), POLICY).error
        is IngressErrorCode.SIZE_METADATA_INVALID
    )
    assert (
        validate_artifact_identity(
            artifact(media_type="application/octet-stream"), provenance(), POLICY
        ).error
        is IngressErrorCode.POLICY_MISMATCH
    )


def test_scanner_verdict_must_match_binding_and_freshness() -> None:
    assert validate_scanner_verdict(scanner(), binding(), POLICY, now=NOW).valid
    assert (
        validate_scanner_verdict(scanner(content_digest="b" * 64), binding(), POLICY, now=NOW).error
        is IngressErrorCode.SCANNER_VERDICT_MISMATCH
    )
    assert (
        validate_scanner_verdict(scanner(observed_at=NOW - 901), binding(), POLICY, now=NOW).error
        is IngressErrorCode.SCANNER_VERDICT_STALE
    )
    assert (
        validate_scanner_verdict(
            scanner(status=ScannerVerdictStatus.REJECTED), binding(), POLICY, now=NOW
        ).error
        is IngressErrorCode.SCANNER_VERDICT_INVALID
    )


def test_valid_ingress_metadata_requires_all_explicit_bindings() -> None:
    result = validate_ingress_metadata(
        identity(),
        capability(),
        provenance(),
        artifact(),
        CONTEXT,
        POLICY,
        now=NOW,
        scanner=scanner(),
    )
    assert result.valid
    assert (
        validate_ingress_metadata(
            identity(tenant_id="tenant-b"),
            capability(),
            provenance(),
            artifact(),
            CONTEXT,
            POLICY,
            now=NOW,
        ).error
        is IngressErrorCode.TENANT_SCOPE_DENIED
    )
    assert (
        validate_ingress_metadata(
            identity(),
            capability(),
            provenance(supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1),
            artifact(),
            CONTEXT,
            POLICY,
            now=NOW,
        ).error
        is IngressErrorCode.SUPPLIER_DISABLED
    )
    assert (
        validate_ingress_metadata(
            identity(),
            capability(),
            provenance(),
            artifact(),
            CONTEXT,
            replace(POLICY, scanner_freshness_seconds=True),
            now=NOW,
        ).error
        is IngressErrorCode.POLICY_MISMATCH
    )


def test_state_machine_requires_typed_metadata_evidence() -> None:
    first = advance_state(
        IngressState.METADATA_RECEIVED,
        IngressState.CANONICAL_METADATA_DECLARED,
        TransitionReason.METADATA_ACCEPTED,
        context=transition_context(),
        occurred_at=NOW,
    )
    assert first.accepted and first.state is IngressState.CANONICAL_METADATA_DECLARED

    declared = advance_state(
        first.state,
        IngressState.SCANNER_VERDICT_DECLARED,
        TransitionReason.SCANNER_VERDICT_DECLARED,
        context=transition_context(scanner_value=scanner()),
        occurred_at=NOW + 1,
        previous_occurred_at=NOW,
    )
    assert declared.accepted and declared.state is IngressState.SCANNER_VERDICT_DECLARED

    ready = advance_state(
        declared.state,
        IngressState.METADATA_READY,
        TransitionReason.METADATA_READY,
        context=transition_context(scanner_value=scanner()),
        occurred_at=NOW + 2,
        previous_occurred_at=NOW + 1,
    )
    assert ready.accepted and ready.state is IngressState.METADATA_READY

    assert (
        advance_state(
            IngressState.METADATA_READY,
            IngressState.METADATA_RECEIVED,
            TransitionReason.METADATA_ACCEPTED,
            context=transition_context(scanner_value=scanner()),
            occurred_at=NOW + 3,
        ).error
        is IngressErrorCode.STATE_TRANSITION_INVALID
    )
    assert (
        advance_state(
            IngressState.SCANNER_VERDICT_DECLARED,
            IngressState.METADATA_READY,
            TransitionReason.METADATA_READY,
            context=transition_context(),
            occurred_at=NOW + 3,
        ).error
        is IngressErrorCode.SCANNER_VERDICT_INVALID
    )
    assert (
        advance_state(
            IngressState.REJECTED,
            IngressState.CANONICAL_METADATA_DECLARED,
            TransitionReason.METADATA_ACCEPTED,
            context=transition_context(),
            occurred_at=NOW + 3,
        ).error
        is IngressErrorCode.STATE_TRANSITION_INVALID
    )


def test_metadata_quarantine_requires_typed_unsafe_verdict() -> None:
    rejected = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_QUARANTINED,
        TransitionReason.METADATA_QUARANTINED,
        context=transition_context(scanner_value=scanner(status=ScannerVerdictStatus.REJECTED)),
        occurred_at=NOW,
    )
    assert rejected.accepted and rejected.state is IngressState.METADATA_QUARANTINED

    stale = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_QUARANTINED,
        TransitionReason.METADATA_QUARANTINED,
        context=transition_context(scanner_value=scanner(observed_at=NOW - 901)),
        occurred_at=NOW,
    )
    assert stale.accepted

    unsafe_missing = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_QUARANTINED,
        TransitionReason.METADATA_QUARANTINED,
        context=transition_context(),
        occurred_at=NOW,
    )
    assert unsafe_missing.error is IngressErrorCode.SCANNER_VERDICT_INVALID


def test_metadata_aborted_is_a_logical_coordination_disposition() -> None:
    result = advance_state(
        IngressState.METADATA_RECEIVED,
        IngressState.METADATA_ABORTED,
        TransitionReason.METADATA_ABORTED,
        context=transition_context(),
        occurred_at=NOW,
    )
    assert result.accepted
    assert result.transition is not None
    assert result.transition.to_state is IngressState.METADATA_ABORTED
    assert result.transition.reason is TransitionReason.METADATA_ABORTED


def test_same_binding_replays_and_changed_binding_conflicts() -> None:
    original = receipt()
    replay = _classify_idempotency(original, receipt(receipt_id="retry-receipt"), CONTEXT)
    assert replay.outcome.value == "idempotency_matched"
    assert replay.receipt is original
    conflict = _classify_idempotency(
        original,
        receipt(binding=binding(artifact=artifact(canonical_size_bytes=97))),
        CONTEXT,
    )
    assert conflict.outcome.value == "conflict"
    assert conflict.error is IngressErrorCode.IDEMPOTENCY_CONFLICT
    created = _classify_idempotency(None, original, CONTEXT)
    assert created.outcome.value == "created"


def test_cross_tenant_retry_is_non_disclosing_and_non_mutating() -> None:
    incoming = receipt(binding=binding(identity=identity(tenant_id="tenant-b")))
    result = _classify_idempotency(receipt(), incoming, CONTEXT)
    assert result.outcome is None
    assert result.error is IngressErrorCode.TENANT_SCOPE_DENIED
    assert result.receipt is None


def test_disabled_paperrun_cannot_yield_transition_or_receipt_outcome() -> None:
    paper_binding = binding(
        provenance=provenance(
            supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1,
            source_kind=SourceKind.PAPER_RUN_RECORDING,
            purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS,
            artifact_role=ArtifactRole.PAPER_RUN_RECORDING,
        )
    )
    paper_context = TransitionContext(
        tenant=CONTEXT,
        capability=capability(
            supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1,
            purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS,
        ),
        policy=POLICY,
        binding=paper_binding,
        now=NOW,
    )
    transition = advance_state(
        IngressState.METADATA_RECEIVED,
        IngressState.CANONICAL_METADATA_DECLARED,
        TransitionReason.METADATA_ACCEPTED,
        context=paper_context,
        occurred_at=NOW,
    )
    assert not transition.accepted
    assert transition.transition is None
    assert transition.error is IngressErrorCode.SUPPLIER_DISABLED

    result = _classify_idempotency(None, receipt(binding=paper_binding), CONTEXT)
    assert result.outcome is None
    assert result.receipt is None
    assert result.error is IngressErrorCode.SUPPLIER_DISABLED


def test_receipt_has_one_binding_artifact_source() -> None:
    assert "artifact" not in IngressReceipt.__dataclass_fields__
    safe = redact_receipt(
        receipt(binding=binding(artifact=artifact(content_digest="b" * 64)))
    ).to_dict()
    assert safe["content_digest"] == "b" * 64


def test_receipt_projection_is_whitelist_only_and_truthful() -> None:
    safe = redact_receipt(receipt()).to_dict()
    assert safe["status"] == "metadata_ready"
    assert safe["state"] == "metadata_ready"
    assert safe["request_id"] == "request-a"
    assert safe["content_digest"] == DIGEST
    assert "tenant-a" not in safe.values()
    assert "idem-a" not in safe.values()
    assert "cap-a" not in safe.values()
    assert "nonce-a" not in safe.values()
    assert "stored" not in safe.values()
    assert "uploaded" not in safe.values()
    assert "replayable" not in safe.values()
    assert set(safe) == {
        "receipt_id",
        "request_id",
        "supplier",
        "source_kind",
        "purpose",
        "artifact_role",
        "schema_id",
        "canonicalization_profile",
        "policy_version",
        "state",
        "status",
        "content_digest",
        "raw_size_bytes",
        "canonical_size_bytes",
        "scanner_status",
        "scanner_profile",
        "scanner_version",
        "scanner_observed_at",
        "scanner_expires_at",
        "occurred_at",
        "error",
    }


def test_idempotency_comparison_covers_request_binding() -> None:
    original = receipt()
    changed_request = receipt(binding=binding(identity=identity(request_id="different-request")))
    result = _classify_idempotency(original, changed_request, CONTEXT)
    assert result.outcome.value == "conflict"
    assert result.error is IngressErrorCode.IDEMPOTENCY_CONFLICT


def test_invalid_retention_and_policy_metadata_fail_closed() -> None:
    assert validate_provenance(provenance(retention_class="reserved"), POLICY).error is (
        IngressErrorCode.RETENTION_CLASS_INVALID
    )
    assert (
        validate_provenance(provenance(policy_version="other-policy"), POLICY).error
        is IngressErrorCode.POLICY_MISMATCH
    )
    assert (
        validate_ingress_metadata(
            identity(),
            capability(),
            provenance(),
            artifact(),
            CONTEXT,
            replace(POLICY, max_raw_size_bytes=1),
            now=NOW,
        ).error
        is IngressErrorCode.POLICY_MISMATCH
    )


def test_capability_and_provenance_must_share_supplier_and_purpose() -> None:
    result = validate_ingress_metadata(
        identity(),
        capability(),
        provenance(
            supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1,
            purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS,
            source_kind=SourceKind.PAPER_RUN_RECORDING,
            artifact_role=ArtifactRole.PAPER_RUN_RECORDING,
        ),
        artifact(),
        CONTEXT,
        POLICY,
        now=NOW,
    )
    assert result.error is IngressErrorCode.SUPPLIER_DISABLED


def test_scanner_rejects_invalid_size_metadata_before_binding_comparison() -> None:
    result = validate_scanner_verdict(
        scanner(canonical_size_bytes=True), binding(), POLICY, now=NOW
    )
    assert result.error is IngressErrorCode.SCANNER_VERDICT_INVALID


def test_malformed_idempotency_receipt_fails_closed() -> None:
    malformed = receipt(binding="not-a-binding")  # type: ignore[arg-type]
    result = _classify_idempotency(None, malformed, CONTEXT)
    assert result.outcome is None
    assert result.error is IngressErrorCode.IDENTITY_INCOMPLETE


def test_canonical_metadata_transition_requires_matching_policy_metadata() -> None:
    result = advance_state(
        IngressState.METADATA_RECEIVED,
        IngressState.CANONICAL_METADATA_DECLARED,
        TransitionReason.METADATA_ACCEPTED,
        context=transition_context(
            policy=replace(POLICY, canonicalization_profile="other-profile")
        ),
        occurred_at=NOW,
    )
    assert not result.accepted
    assert result.error is IngressErrorCode.POLICY_MISMATCH


def test_scanner_verdict_declaration_requires_structural_supplied_metadata() -> None:
    result = advance_state(
        IngressState.CANONICAL_METADATA_DECLARED,
        IngressState.SCANNER_VERDICT_DECLARED,
        TransitionReason.SCANNER_VERDICT_DECLARED,
        context=transition_context(scanner_value=object()),  # type: ignore[arg-type]
        occurred_at=NOW,
    )
    assert not result.accepted
    assert result.error is IngressErrorCode.SCANNER_VERDICT_INVALID


@pytest.mark.parametrize(
    "unsafe_scanner",
    [
        scanner(status=ScannerVerdictStatus.REJECTED),
        scanner(status=ScannerVerdictStatus.INDETERMINATE),
        scanner(status=ScannerVerdictStatus.UNKNOWN),
        scanner(status=ScannerVerdictStatus.ERROR),
        scanner(content_digest="b" * 64),
    ],
)
def test_metadata_quarantine_accepts_only_typed_unsafe_verdicts(
    unsafe_scanner: ScannerVerdict,
) -> None:
    result = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_QUARANTINED,
        TransitionReason.METADATA_QUARANTINED,
        context=transition_context(scanner_value=unsafe_scanner),
        occurred_at=NOW,
    )
    assert result.accepted
    assert result.state is IngressState.METADATA_QUARANTINED


def test_metadata_ready_rejects_stale_or_mismatched_supplied_verdict() -> None:
    stale = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_READY,
        TransitionReason.METADATA_READY,
        context=transition_context(scanner_value=scanner(observed_at=NOW - 901)),
        occurred_at=NOW,
    )
    assert stale.error is IngressErrorCode.SCANNER_VERDICT_STALE

    mismatch = advance_state(
        IngressState.SCANNER_VERDICT_DECLARED,
        IngressState.METADATA_READY,
        TransitionReason.METADATA_READY,
        context=transition_context(scanner_value=scanner(content_digest="b" * 64)),
        occurred_at=NOW,
    )
    assert mismatch.error is IngressErrorCode.SCANNER_VERDICT_MISMATCH
