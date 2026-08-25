from __future__ import annotations

import json
import pickle
import pytest

from agent_os.persistence.contracts import (
    ArtifactIdentity,
    ArtifactRole,
    CapabilityConsumer,
    CapabilityMetadata,
    CanonicalJsonPolicy,
    IngressBinding,
    IngressIdentity,
    IngressPurpose,
    IngressProvenance,
    SourceKind,
    TenantContext,
    TrustedSupplier,
)
from agent_os.persistence.material import (
    FIXTURE_SCHEMA_V1,
    LEASE_LIFETIME_SECONDS_V1,
    MAX_CONTAINER_ENTRIES_V1,
    MAX_DEPTH_V1,
    MAX_RAW_SIZE_BYTES_V1,
    MAX_TOTAL_NODES_V1,
    LeaseStatus,
    MaterialCoordinator,
    MaterialErrorCode,
    MaterialState,
)

NOW = 1_700_000_000
CONTEXT = TenantContext(tenant_id="tenant-a", context_id="context-a")
POLICY = CanonicalJsonPolicy()
CONSUMER = object()
CANONICAL = '{"items":[{"id":"alpha","value":"one"}],"schema":"fixture-material-v1"}'
SOURCE = ' { "schema" : "fixture-material-v1", "items" : [ { "value" : "one", "id" : "alpha" } ] } '
RAW_SIZE = len(SOURCE.encode("utf-8"))
CANONICAL_SIZE = len(CANONICAL.encode("utf-8"))
DIGEST = "5e6f1e64321631325e2b5f127e5c2be929496d72666026ff240edc2b0d9befc7"


class ExplodingString(str):
    def encode(self, *args: object, **kwargs: object) -> bytes:
        raise AssertionError("source inspection reached disabled supplier")


class Consumer:
    pass


def identity(**overrides: object) -> IngressIdentity:
    values: dict[str, object] = {
        "tenant_id": "tenant-a",
        "actor_id": "actor-a",
        "request_id": "request-a",
        "idempotency_key": "idempotency-a",
        "capability_id": "capability-a",
        "nonce_id": "nonce-a",
    }
    values.update(overrides)
    return IngressIdentity(**values)


def capability(**overrides: object) -> CapabilityMetadata:
    values: dict[str, object] = {
        "capability_id": "capability-a",
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
        "raw_size_bytes": RAW_SIZE,
        "canonical_size_bytes": CANONICAL_SIZE,
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


def prepare(
    coordinator: MaterialCoordinator | None = None,
    *,
    source: str = SOURCE,
    binding_value: IngressBinding | object = binding(),
    tenant: TenantContext = CONTEXT,
    capability_value: CapabilityMetadata | object = capability(),
    policy: CanonicalJsonPolicy = POLICY,
    consumer: object = CONSUMER,
    now: int = NOW,
):
    selected = coordinator or MaterialCoordinator()
    return selected.prepare(
        source,
        tenant=tenant,
        binding=binding_value,  # type: ignore[arg-type]
        capability=capability_value,  # type: ignore[arg-type]
        policy=policy,
        consumer=consumer,
        now=now,
    )


def test_valid_fixture_is_canonicalized_and_leased_with_safe_receipt() -> None:
    coordinator = MaterialCoordinator()
    result = prepare(coordinator)

    assert result.accepted
    assert result.error is None
    assert result.lease is not None
    assert result.lease.status is LeaseStatus.ACTIVE
    assert coordinator.state is MaterialState.LEASE_ISSUED
    assert coordinator.state_history == (
        MaterialState.CREATED,
        MaterialState.CAPABILITY_VALIDATED,
        MaterialState.SOURCE_BOUND,
        MaterialState.RAW_SIZE_VALIDATED,
        MaterialState.PARSED,
        MaterialState.SCHEMA_VALIDATED,
        MaterialState.CANONICALIZED,
        MaterialState.CANONICAL_SIZE_VALIDATED,
        MaterialState.DIGESTED,
        MaterialState.RECEIPT_READY,
        MaterialState.LEASE_ISSUED,
    )
    assert result.receipt is not None
    safe = result.receipt.to_dict()
    assert safe["content_digest"] == DIGEST
    assert safe["raw_size_bytes"] == RAW_SIZE
    assert safe["canonical_size_bytes"] == CANONICAL_SIZE
    assert safe["lease_status"] == "active"
    assert "lease" not in safe
    assert "source" not in safe
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
        "lease_status",
        "content_digest",
        "raw_size_bytes",
        "canonical_size_bytes",
        "issued_at",
        "lease_expires_at",
        "consumed_at",
        "disposed_at",
        "error",
    }


def test_only_the_exact_built_in_str_is_accepted() -> None:
    subclass_result = prepare(source=ExplodingString(SOURCE))
    assert not subclass_result.accepted
    assert subclass_result.error is MaterialErrorCode.INPUT_TYPE_INVALID

    surrogate_result = prepare(source='{"schema":"fixture-material-v1","items":[]}\ud800')
    assert not surrogate_result.accepted
    assert surrogate_result.error is MaterialErrorCode.INVALID_ENCODING

    custom_object_result = prepare(source=object())  # type: ignore[arg-type]
    assert not custom_object_result.accepted
    assert custom_object_result.error is MaterialErrorCode.INPUT_TYPE_INVALID


def test_disabled_paperrun_supplier_is_first_and_does_not_mutate_coordinator() -> None:
    paper_binding = binding(
        provenance=provenance(
            supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1,
            source_kind=SourceKind.PAPER_RUN_RECORDING,
            purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS,
            artifact_role=ArtifactRole.PAPER_RUN_RECORDING,
        )
    )
    coordinator = MaterialCoordinator()
    result = prepare(
        coordinator,
        source=ExplodingString("not JSON"),
        binding_value=paper_binding,
        capability_value=capability(
            supplier=TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1,
            purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS,
        ),
    )

    assert not result.accepted
    assert result.error is MaterialErrorCode.SUPPLIER_DISABLED
    assert result.receipt is None
    assert result.lease is None
    assert coordinator.state is MaterialState.CREATED
    assert coordinator.state_history == (MaterialState.CREATED,)


@pytest.mark.parametrize(
    ("changed_binding", "expected"),
    [
        (binding(identity=identity(tenant_id="tenant-b")), MaterialErrorCode.TENANT_SCOPE_DENIED),
        (
            binding(identity=identity(capability_id="other-capability")),
            MaterialErrorCode.CAPABILITY_INVALID,
        ),
        (
            binding(provenance=provenance(purpose=IngressPurpose.PAPERRUN_RECORDING_INGRESS)),
            MaterialErrorCode.PROVENANCE_INVALID,
        ),
        (
            binding(artifact=artifact(media_type="application/octet-stream")),
            MaterialErrorCode.POLICY_INVALID,
        ),
    ],
)
def test_a1_identity_provenance_and_policy_mismatches_fail_closed(
    changed_binding: IngressBinding,
    expected: MaterialErrorCode,
) -> None:
    result = prepare(binding_value=changed_binding)
    assert not result.accepted
    assert result.error is expected
    assert result.lease is None
    assert result.receipt is None


def test_raw_limit_is_checked_before_json_parsing() -> None:
    source = "x" * (MAX_RAW_SIZE_BYTES_V1 + 1)
    result = prepare(source=source)
    assert not result.accepted
    assert result.error is MaterialErrorCode.RAW_SIZE_EXCEEDED
    assert result.receipt is not None
    assert result.receipt.raw_size_bytes == MAX_RAW_SIZE_BYTES_V1 + 1


def test_canonical_limit_is_checked_before_retained_buffer_allocation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import agent_os.persistence.material as material_module

    monkeypatch.setattr(material_module, "MAX_CANONICAL_SIZE_BYTES_V1", CANONICAL_SIZE - 1)
    result = prepare()
    assert not result.accepted
    assert result.error is MaterialErrorCode.CANONICAL_SIZE_EXCEEDED
    assert result.lease is None


def test_json_validation_rejects_malformed_duplicate_nonfinite_and_wrong_root() -> None:
    cases = {
        "not-json": MaterialErrorCode.JSON_INVALID,
        '{"schema":"fixture-material-v1","schema":"fixture-material-v1","items":[]}': MaterialErrorCode.DUPLICATE_KEY,
        '{"schema":"fixture-material-v1","items":[{"id":"alpha","value":NaN}]}': MaterialErrorCode.NON_FINITE_NUMBER,
        "[]": MaterialErrorCode.SCHEMA_INVALID,
    }
    for source, expected in cases.items():
        result = prepare(source=source)
        assert not result.accepted, source
        assert result.error is expected, source


def test_finite_schema_rejects_unknown_and_sensitive_fixture_fields() -> None:
    unknown = json.dumps(
        {"schema": FIXTURE_SCHEMA_V1, "items": [], "extra": "value"},
        separators=(",", ":"),
    )
    sensitive = json.dumps(
        {
            "schema": FIXTURE_SCHEMA_V1,
            "items": [{"id": "alpha", "value": "one", "private_key": "x"}],
        },
        separators=(",", ":"),
    )
    for source in (unknown, sensitive):
        result = prepare(source=source)
        assert not result.accepted
        assert result.error is MaterialErrorCode.SCHEMA_INVALID


def test_structure_limits_are_finite_and_fail_closed() -> None:
    deep: object = 0
    for _ in range(MAX_DEPTH_V1 + 2):
        deep = [deep]
    deep_source = json.dumps({"schema": FIXTURE_SCHEMA_V1, "items": deep}, separators=(",", ":"))
    deep_result = prepare(source=deep_source)
    assert deep_result.error is MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED

    wide = {
        "schema": FIXTURE_SCHEMA_V1,
        "items": [],
        **{f"x{n}": n for n in range(MAX_CONTAINER_ENTRIES_V1)},
    }
    wide_result = prepare(source=json.dumps(wide, separators=(",", ":")))
    assert wide_result.error is MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED

    branch: object = 0
    for _ in range(17):
        branch = [branch, branch]
    node_source = json.dumps({"schema": FIXTURE_SCHEMA_V1, "items": branch}, separators=(",", ":"))
    node_result = prepare(source=node_source)
    assert node_result.error is MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED
    assert MAX_TOTAL_NODES_V1 == 100_000


def test_digest_and_size_mismatches_never_create_a_lease() -> None:
    for changed in (
        artifact(content_digest="b" * 64),
        artifact(raw_size_bytes=RAW_SIZE + 1),
        artifact(canonical_size_bytes=CANONICAL_SIZE + 1),
    ):
        coordinator = MaterialCoordinator()
        result = prepare(coordinator, binding_value=binding(artifact=changed))
        assert not result.accepted
        assert result.error is MaterialErrorCode.ARTIFACT_MISMATCH
        assert result.lease is None
        assert coordinator.state is MaterialState.REJECTED


def test_valid_consumer_succeeds_once_and_disposes_private_buffer() -> None:
    coordinator = MaterialCoordinator()
    result = prepare(coordinator)
    assert result.lease is not None
    captured: list[object] = []

    def consumer_callback(material: object) -> None:
        captured.append(material)
        assert repr(material) == "_PrivateCanonicalMaterial(state=held)"
        assert not hasattr(material, "canonical_bytes")

    consumed = result.lease.consume(CONSUMER, consumer_callback, now=NOW + 1)
    assert consumed.accepted
    assert consumed.error is None
    assert result.lease.status is LeaseStatus.CONSUMED
    assert coordinator.state is MaterialState.DISPOSED
    assert consumed.receipt is not None
    assert consumed.receipt.state is MaterialState.DISPOSED
    assert consumed.receipt.consumed_at == NOW + 1
    assert consumed.receipt.disposed_at == NOW + 1
    assert getattr(captured[0], "_canonical_buffer") == bytearray()

    second = result.lease.consume(CONSUMER, consumer_callback, now=NOW + 2)
    assert not second.accepted
    assert second.error is MaterialErrorCode.LEASE_ALREADY_USED
    assert len(captured) == 1


def test_wrong_consumer_expiry_cancellation_and_callback_failure_invalidate_lease() -> None:
    wrong_coordinator = MaterialCoordinator()
    wrong = prepare(wrong_coordinator)
    assert wrong.lease is not None
    wrong_result = wrong.lease.consume(object(), lambda _: None, now=NOW + 1)
    assert wrong_result.error is MaterialErrorCode.WRONG_CONSUMER
    assert wrong.lease.status is LeaseStatus.FAILED
    assert wrong_coordinator.state is MaterialState.ABORTED

    expired_coordinator = MaterialCoordinator()
    expired = prepare(expired_coordinator)
    assert expired.lease is not None
    expired_result = expired.lease.consume(
        CONSUMER, lambda _: None, now=NOW + LEASE_LIFETIME_SECONDS_V1
    )
    assert expired_result.error is MaterialErrorCode.LEASE_EXPIRED
    assert expired.lease.status is LeaseStatus.EXPIRED
    assert expired_coordinator.state is MaterialState.ABORTED

    cancelled_coordinator = MaterialCoordinator()
    cancelled = prepare(cancelled_coordinator)
    assert cancelled.lease is not None
    cancelled_result = cancelled.lease.cancel(now=NOW + 2)
    assert cancelled_result.error is MaterialErrorCode.LEASE_CANCELLED
    assert cancelled.lease.status is LeaseStatus.CANCELLED
    assert cancelled_coordinator.state is MaterialState.ABORTED

    failed_coordinator = MaterialCoordinator()
    failed = prepare(failed_coordinator)
    assert failed.lease is not None

    def failing_callback(_: object) -> None:
        raise RuntimeError("fixture consumer failed")

    failed_result = failed.lease.consume(CONSUMER, failing_callback, now=NOW + 3)
    assert failed_result.error is MaterialErrorCode.CONSUMER_FAILED
    assert failed.lease.status is LeaseStatus.FAILED
    assert failed_coordinator.state is MaterialState.ABORTED


def test_disposal_during_consumer_handoff_invalidates_lease() -> None:
    coordinator = MaterialCoordinator()
    result = prepare(coordinator)
    assert result.lease is not None

    def disposing_callback(_: object) -> None:
        disposal = coordinator.dispose(now=NOW + 2)
        assert disposal.accepted

    consumed = result.lease.consume(CONSUMER, disposing_callback, now=NOW + 1)
    assert not consumed.accepted
    assert consumed.error is MaterialErrorCode.COORDINATOR_DISPOSED
    assert result.lease.status is LeaseStatus.DISPOSED
    assert coordinator.state is MaterialState.DISPOSED


def test_dispose_invalidates_active_lease_and_is_idempotent() -> None:
    coordinator = MaterialCoordinator()
    result = prepare(coordinator)
    assert result.lease is not None

    disposed = coordinator.dispose(now=NOW + 4)
    assert disposed.accepted
    assert coordinator.state is MaterialState.DISPOSED
    assert result.lease.status is LeaseStatus.DISPOSED
    assert disposed.receipt is not None
    assert disposed.receipt.disposed_at == NOW + 4

    repeated = coordinator.dispose(now=NOW + 5)
    assert repeated.accepted
    assert repeated.receipt == disposed.receipt

    after = prepare(coordinator)
    assert not after.accepted
    assert after.error is MaterialErrorCode.COORDINATOR_DISPOSED


def test_private_material_and_lease_have_no_serialization_or_content_surface() -> None:
    result = prepare()
    assert result.lease is not None
    assert "lease" not in result.to_dict()
    assert repr(result.lease) == "MaterialLease(status=active)"
    assert "canonical" not in repr(result.lease).lower()
    with pytest.raises(TypeError, match="lease_not_serializable"):
        pickle.dumps(result.lease)

    public_names = {name for name in dir(result.lease) if not name.startswith("_")}
    assert public_names == {"cancel", "consume", "status"}
    assert not any(
        name in public_names
        for name in {"bytes", "export", "iterator", "mapping", "serialize", "source"}
    )


def test_failed_prepare_is_terminal_and_coordinator_cannot_be_reused() -> None:
    coordinator = MaterialCoordinator()
    failed = prepare(coordinator, source="not-json")
    assert failed.error is MaterialErrorCode.JSON_INVALID
    assert coordinator.state is MaterialState.REJECTED

    retry = prepare(coordinator)
    assert not retry.accepted
    assert retry.error is MaterialErrorCode.COORDINATOR_ALREADY_USED
