"""Private, bounded, in-process material handling for synthetic fixtures only.

This module deliberately does not provide persistence, scanner, replay, runtime,
execution, API, or external-system behavior.  The only public content ingress is
an exact built-in ``str`` accepted by ``MaterialCoordinator.prepare``.  Material
is retained only in a private non-serializable object until a single internal
consumer callback completes or the owner disposes it.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from dataclasses import dataclass, replace
from enum import Enum
from typing import Callable, Final, NoReturn

from .contracts import (
    ArtifactRole,
    CapabilityMetadata,
    CanonicalJsonPolicy,
    IngressBinding,
    IngressErrorCode,
    IngressPurpose,
    IngressProvenance,
    IngressState,
    MAX_SIZE_BYTES_V1,
    SourceKind,
    TenantContext,
    TrustedSupplier,
)
from .ingress import validate_ingress_metadata

MAX_RAW_SIZE_BYTES_V1: Final[int] = MAX_SIZE_BYTES_V1
MAX_CANONICAL_SIZE_BYTES_V1: Final[int] = MAX_SIZE_BYTES_V1
MAX_DEPTH_V1: Final[int] = 32
MAX_CONTAINER_ENTRIES_V1: Final[int] = 4_096
MAX_TOTAL_NODES_V1: Final[int] = 100_000
LEASE_LIFETIME_SECONDS_V1: Final[int] = 60
FIXTURE_SCHEMA_V1: Final[str] = "fixture-material-v1"

_ALLOWED_ROOT_FIELDS: Final[frozenset[str]] = frozenset({"schema", "items"})
_ALLOWED_ITEM_FIELDS: Final[frozenset[str]] = frozenset({"id", "value"})
_SAFE_TOKEN = re.compile(r"^[a-z0-9][a-z0-9_.:-]{0,63}$")


class MaterialState(str, Enum):
    """Internal in-memory lifecycle labels only."""

    CREATED = "created"
    CAPABILITY_VALIDATED = "capability_validated"
    SOURCE_BOUND = "source_bound"
    RAW_SIZE_VALIDATED = "raw_size_validated"
    PARSED = "parsed"
    SCHEMA_VALIDATED = "schema_validated"
    CANONICALIZED = "canonicalized"
    CANONICAL_SIZE_VALIDATED = "canonical_size_validated"
    DIGESTED = "digested"
    RECEIPT_READY = "receipt_ready"
    LEASE_ISSUED = "lease_issued"
    CONSUMER_HANDOFF = "consumer_handoff"
    CONSUMER_COMPLETED = "consumer_completed"
    DISPOSED = "disposed"
    REJECTED = "rejected"
    ABORTED = "aborted"


class LeaseStatus(str, Enum):
    ACTIVE = "active"
    CONSUMING = "consuming"
    CONSUMED = "consumed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"
    FAILED = "failed"
    DISPOSED = "disposed"


class MaterialErrorCode(str, Enum):
    SUPPLIER_DISABLED = "supplier_disabled"
    SUPPLIER_UNSUPPORTED = "supplier_unsupported"
    BINDING_INVALID = "binding_invalid"
    TENANT_SCOPE_DENIED = "tenant_scope_denied"
    IDENTITY_INVALID = "identity_invalid"
    CAPABILITY_INVALID = "capability_invalid"
    PROVENANCE_INVALID = "provenance_invalid"
    POLICY_INVALID = "policy_invalid"
    ARTIFACT_METADATA_INVALID = "artifact_metadata_invalid"
    INPUT_TYPE_INVALID = "input_type_invalid"
    INVALID_ENCODING = "invalid_encoding"
    RAW_SIZE_EXCEEDED = "raw_size_exceeded"
    JSON_INVALID = "json_invalid"
    DUPLICATE_KEY = "duplicate_key"
    NON_FINITE_NUMBER = "non_finite_number"
    STRUCTURE_LIMIT_EXCEEDED = "structure_limit_exceeded"
    SCHEMA_INVALID = "schema_invalid"
    CANONICAL_SIZE_EXCEEDED = "canonical_size_exceeded"
    ARTIFACT_MISMATCH = "artifact_mismatch"
    CONSUMER_INVALID = "consumer_invalid"
    CLOCK_INVALID = "clock_invalid"
    COORDINATOR_DISPOSED = "coordinator_disposed"
    WRONG_CONSUMER = "wrong_consumer"
    LEASE_EXPIRED = "lease_expired"
    LEASE_ALREADY_USED = "lease_already_used"
    LEASE_CANCELLED = "lease_cancelled"
    LEASE_DISPOSED = "lease_disposed"
    CONSUMER_FAILED = "consumer_failed"
    COORDINATOR_ALREADY_USED = "coordinator_already_used"


@dataclass(frozen=True)
class MaterialReceipt:
    """Whitelist-only safe metadata; it never contains material or a lease."""

    receipt_id: str
    request_id: str
    supplier: TrustedSupplier
    source_kind: SourceKind
    purpose: IngressPurpose
    artifact_role: ArtifactRole
    schema_id: str
    canonicalization_profile: str
    policy_version: str
    state: MaterialState
    lease_status: LeaseStatus | None
    content_digest: str | None
    raw_size_bytes: int | None
    canonical_size_bytes: int | None
    issued_at: int | None
    lease_expires_at: int | None
    consumed_at: int | None
    disposed_at: int | None
    error: MaterialErrorCode | None

    def to_dict(self) -> dict[str, object]:
        """Return only explicitly approved safe fields."""
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
            "lease_status": self.lease_status.value if self.lease_status else None,
            "content_digest": self.content_digest,
            "raw_size_bytes": self.raw_size_bytes,
            "canonical_size_bytes": self.canonical_size_bytes,
            "issued_at": self.issued_at,
            "lease_expires_at": self.lease_expires_at,
            "consumed_at": self.consumed_at,
            "disposed_at": self.disposed_at,
            "error": self.error.value if self.error else None,
        }


@dataclass(frozen=True)
class MaterialResult:
    """Categorical operation result; ``to_dict`` intentionally omits the lease."""

    accepted: bool
    error: MaterialErrorCode | None = None
    receipt: MaterialReceipt | None = None
    lease: "MaterialLease | None" = None

    def to_dict(self) -> dict[str, object]:
        return {
            "accepted": self.accepted,
            "error": self.error.value if self.error else None,
            "receipt": self.receipt.to_dict() if self.receipt else None,
        }


class _DuplicateKey(ValueError):
    pass


class _NonFiniteNumber(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKey
        result[key] = value
    return result


def _reject_non_finite(value: str) -> object:
    del value
    raise _NonFiniteNumber


def _is_clock(value: object) -> bool:
    return type(value) is int and value >= 0


def _is_safe_consumer(value: object) -> bool:
    return value is not None and not isinstance(value, (str, int, float, bool))


def _map_a1_error(error: IngressErrorCode | None) -> MaterialErrorCode:
    if error is IngressErrorCode.SUPPLIER_DISABLED:
        return MaterialErrorCode.SUPPLIER_DISABLED
    if error is IngressErrorCode.TENANT_SCOPE_DENIED:
        return MaterialErrorCode.TENANT_SCOPE_DENIED
    if error in {IngressErrorCode.IDENTITY_INCOMPLETE, IngressErrorCode.IDENTIFIER_INVALID}:
        return MaterialErrorCode.IDENTITY_INVALID
    if error in {
        IngressErrorCode.CAPABILITY_INVALID,
        IngressErrorCode.CAPABILITY_EXPIRED,
        IngressErrorCode.CAPABILITY_MISMATCH,
        IngressErrorCode.WRONG_CONSUMER,
    }:
        return MaterialErrorCode.CAPABILITY_INVALID
    if error in {
        IngressErrorCode.SUPPLIER_PURPOSE_MISMATCH,
        IngressErrorCode.SUPPLIER_SOURCE_MISMATCH,
        IngressErrorCode.ARTIFACT_ROLE_MISMATCH,
        IngressErrorCode.RETENTION_CLASS_INVALID,
    }:
        return MaterialErrorCode.PROVENANCE_INVALID
    if error is IngressErrorCode.POLICY_MISMATCH:
        return MaterialErrorCode.POLICY_INVALID
    if error is IngressErrorCode.DIGEST_METADATA_INVALID:
        return MaterialErrorCode.ARTIFACT_METADATA_INVALID
    if error is IngressErrorCode.SIZE_METADATA_INVALID:
        return MaterialErrorCode.ARTIFACT_METADATA_INVALID
    return MaterialErrorCode.BINDING_INVALID


def _supplier_preflight(binding: object) -> MaterialErrorCode | None:
    """Inspect only trusted metadata; this function must precede source inspection."""
    if not isinstance(binding, IngressBinding):
        return MaterialErrorCode.BINDING_INVALID
    provenance = binding.provenance
    if not isinstance(provenance, IngressProvenance):
        return MaterialErrorCode.BINDING_INVALID
    if provenance.supplier is TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1:
        return MaterialErrorCode.SUPPLIER_DISABLED
    if provenance.supplier is TrustedSupplier.FIXTURE_TEST_INGRESS_V1:
        return None
    return MaterialErrorCode.SUPPLIER_UNSUPPORTED


def _validate_structure(value: object) -> MaterialErrorCode | None:
    stack: list[tuple[object, int]] = [(value, 0)]
    nodes = 0
    while stack:
        current, depth = stack.pop()
        nodes += 1
        if nodes > MAX_TOTAL_NODES_V1 or depth > MAX_DEPTH_V1:
            return MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED
        if type(current) is dict:
            if len(current) > MAX_CONTAINER_ENTRIES_V1:
                return MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED
            for key, child in current.items():
                if type(key) is not str:
                    return MaterialErrorCode.SCHEMA_INVALID
                stack.append((child, depth + 1))
        elif type(current) is list:
            if len(current) > MAX_CONTAINER_ENTRIES_V1:
                return MaterialErrorCode.STRUCTURE_LIMIT_EXCEEDED
            stack.extend((child, depth + 1) for child in current)
        elif type(current) is float and not math.isfinite(current):
            return MaterialErrorCode.NON_FINITE_NUMBER
        elif type(current) not in {str, int, float, bool, type(None)}:
            return MaterialErrorCode.SCHEMA_INVALID
    return None


def _validate_schema(value: object) -> MaterialErrorCode | None:
    if type(value) is not dict or set(value) != _ALLOWED_ROOT_FIELDS:
        return MaterialErrorCode.SCHEMA_INVALID
    if value.get("schema") != FIXTURE_SCHEMA_V1:
        return MaterialErrorCode.SCHEMA_INVALID
    items = value.get("items")
    if type(items) is not list or len(items) > MAX_CONTAINER_ENTRIES_V1:
        return MaterialErrorCode.SCHEMA_INVALID
    for item in items:
        if type(item) is not dict or set(item) != _ALLOWED_ITEM_FIELDS:
            return MaterialErrorCode.SCHEMA_INVALID
        identifier = item.get("id")
        item_value = item.get("value")
        if (
            type(identifier) is not str
            or type(item_value) is not str
            or _SAFE_TOKEN.fullmatch(identifier) is None
            or _SAFE_TOKEN.fullmatch(item_value) is None
        ):
            return MaterialErrorCode.SCHEMA_INVALID
    return None


def _parse_and_canonicalize(raw_text: str) -> tuple[bytes, bytes, MaterialErrorCode | None]:
    try:
        parsed = json.loads(
            raw_text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_non_finite,
        )
    except _DuplicateKey:
        return b"", b"", MaterialErrorCode.DUPLICATE_KEY
    except _NonFiniteNumber:
        return b"", b"", MaterialErrorCode.NON_FINITE_NUMBER
    except (json.JSONDecodeError, RecursionError, ValueError, TypeError):
        return b"", b"", MaterialErrorCode.JSON_INVALID

    structure_error = _validate_structure(parsed)
    if structure_error is not None:
        return b"", b"", structure_error
    schema_error = _validate_schema(parsed)
    if schema_error is not None:
        return b"", b"", schema_error

    try:
        canonical_text = json.dumps(
            parsed,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        canonical_octets = canonical_text.encode("utf-8", "strict")
    except (UnicodeError, ValueError, TypeError, RecursionError):
        return b"", b"", MaterialErrorCode.JSON_INVALID
    return raw_text.encode("utf-8", "strict"), canonical_octets, None


class _PrivateCanonicalMaterial:
    """Opaque retained canonical representation owned by one coordinator."""

    __slots__ = (
        "_canonical_buffer",
        "_content_digest",
        "_raw_size_bytes",
        "_canonical_size_bytes",
        "_disposed",
    )

    def __init__(
        self,
        canonical_buffer: bytearray,
        content_digest: str,
        raw_size_bytes: int,
        canonical_size_bytes: int,
    ) -> None:
        self._canonical_buffer = canonical_buffer
        self._content_digest = content_digest
        self._raw_size_bytes = raw_size_bytes
        self._canonical_size_bytes = canonical_size_bytes
        self._disposed = False

    def __repr__(self) -> str:
        state = "disposed" if self._disposed else "held"
        return f"_PrivateCanonicalMaterial(state={state})"

    def __reduce__(self) -> NoReturn:
        raise TypeError("material_not_serializable")

    def _dispose(self) -> None:
        if self._disposed:
            return
        for index in range(len(self._canonical_buffer)):
            self._canonical_buffer[index] = 0
        self._canonical_buffer.clear()
        self._disposed = True


class MaterialLease:
    """Single-use, consumer-bound, non-serializable internal handoff lease."""

    __slots__ = (
        "_material",
        "_consumer",
        "_expires_at",
        "_status",
        "_coordinator",
    )

    def __init__(
        self,
        held_value: _PrivateCanonicalMaterial,
        consumer: object,
        expires_at: int,
        coordinator: "MaterialCoordinator",
    ) -> None:
        self._material = held_value
        self._consumer = consumer
        self._expires_at = expires_at
        self._status = LeaseStatus.ACTIVE
        self._coordinator = coordinator

    def __repr__(self) -> str:
        return f"MaterialLease(status={self._status.value})"

    def __reduce__(self) -> NoReturn:
        raise TypeError("lease_not_serializable")

    @property
    def status(self) -> LeaseStatus:
        return self._status

    def _safe_result(
        self,
        *,
        accepted: bool,
        error: MaterialErrorCode | None,
        state: MaterialState,
        now: int | None = None,
        consumed: bool = False,
    ) -> MaterialResult:
        self._coordinator._transition(state)
        if consumed:
            self._status = LeaseStatus.CONSUMED
        receipt = self._coordinator._update_receipt(
            state=state,
            lease_status=self._status,
            error=error,
            consumed_at=now if consumed else None,
            disposed_at=now if state in {MaterialState.DISPOSED, MaterialState.ABORTED} else None,
        )
        return MaterialResult(accepted=accepted, error=error, receipt=receipt)

    def _invalidate(
        self,
        status: LeaseStatus,
        error: MaterialErrorCode,
        *,
        now: int | None = None,
        disposed_state: MaterialState = MaterialState.ABORTED,
    ) -> MaterialResult:
        self._status = status
        self._material._dispose()
        return self._safe_result(
            accepted=False,
            error=error,
            state=disposed_state,
            now=now,
        )

    def consume(
        self,
        consumer: object,
        callback: Callable[[object], object],
        *,
        now: int,
    ) -> MaterialResult:
        """Invoke the internal consumer exactly once without returning material."""
        if self._status is not LeaseStatus.ACTIVE:
            error = (
                MaterialErrorCode.LEASE_ALREADY_USED
                if self._status is LeaseStatus.CONSUMED
                else MaterialErrorCode.LEASE_DISPOSED
            )
            return MaterialResult(False, error, self._coordinator._current_receipt())
        if not _is_clock(now):
            return self._invalidate(LeaseStatus.FAILED, MaterialErrorCode.CLOCK_INVALID)
        if consumer is not self._consumer:
            return self._invalidate(
                LeaseStatus.FAILED,
                MaterialErrorCode.WRONG_CONSUMER,
                now=now,
            )
        if now >= self._expires_at:
            return self._invalidate(LeaseStatus.EXPIRED, MaterialErrorCode.LEASE_EXPIRED, now=now)
        if not callable(callback):
            return self._invalidate(
                LeaseStatus.FAILED,
                MaterialErrorCode.CONSUMER_INVALID,
                now=now,
            )

        self._status = LeaseStatus.CONSUMING
        self._coordinator._transition(MaterialState.CONSUMER_HANDOFF)
        try:
            callback_result = callback(self._material)
        except Exception:
            return self._invalidate(
                LeaseStatus.FAILED,
                MaterialErrorCode.CONSUMER_FAILED,
                now=now,
            )
        if self._status is not LeaseStatus.CONSUMING or self._coordinator._disposed:
            return MaterialResult(
                False,
                MaterialErrorCode.COORDINATOR_DISPOSED,
                self._coordinator._current_receipt(),
            )
        if callback_result is not None:
            return self._invalidate(
                LeaseStatus.FAILED,
                MaterialErrorCode.CONSUMER_FAILED,
                now=now,
            )

        self._material._dispose()
        self._status = LeaseStatus.CONSUMED
        self._coordinator._transition(MaterialState.CONSUMER_COMPLETED)
        self._coordinator._transition(MaterialState.DISPOSED)
        receipt = self._coordinator._update_receipt(
            state=MaterialState.DISPOSED,
            lease_status=LeaseStatus.CONSUMED,
            error=None,
            consumed_at=now,
            disposed_at=now,
        )
        return MaterialResult(True, None, receipt)

    def cancel(self, *, now: int) -> MaterialResult:
        """Invalidate the lease and dispose retained material without a callback."""
        if self._status is not LeaseStatus.ACTIVE:
            return MaterialResult(
                False,
                MaterialErrorCode.LEASE_ALREADY_USED,
                self._coordinator._current_receipt(),
            )
        if not _is_clock(now):
            return self._invalidate(LeaseStatus.FAILED, MaterialErrorCode.CLOCK_INVALID)
        return self._invalidate(LeaseStatus.CANCELLED, MaterialErrorCode.LEASE_CANCELLED, now=now)


class MaterialCoordinator:
    """Own one bounded material operation entirely in process memory."""

    __slots__ = (
        "_state",
        "_history",
        "_receipt_counter",
        "_receipt",
        "_lease",
        "_disposed",
    )

    def __init__(self) -> None:
        self._state = MaterialState.CREATED
        self._history: list[MaterialState] = [MaterialState.CREATED]
        self._receipt_counter = 0
        self._receipt: MaterialReceipt | None = None
        self._lease: MaterialLease | None = None
        self._disposed = False

    @property
    def state(self) -> MaterialState:
        return self._state

    @property
    def state_history(self) -> tuple[MaterialState, ...]:
        return tuple(self._history)

    def _transition(self, state: MaterialState) -> None:
        if self._state is state:
            return
        self._state = state
        self._history.append(state)

    def _current_receipt(self) -> MaterialReceipt | None:
        return self._receipt

    def _update_receipt(
        self,
        *,
        state: MaterialState,
        lease_status: LeaseStatus | None,
        error: MaterialErrorCode | None,
        consumed_at: int | None = None,
        disposed_at: int | None = None,
    ) -> MaterialReceipt | None:
        if self._receipt is None:
            return None
        self._receipt = replace(
            self._receipt,
            state=state,
            lease_status=lease_status,
            error=error,
            consumed_at=consumed_at if consumed_at is not None else self._receipt.consumed_at,
            disposed_at=disposed_at if disposed_at is not None else self._receipt.disposed_at,
        )
        return self._receipt

    def _next_receipt(
        self,
        binding: IngressBinding,
        policy: CanonicalJsonPolicy,
        *,
        state: MaterialState,
        lease_status: LeaseStatus | None,
        error: MaterialErrorCode | None,
        raw_size_bytes: int | None = None,
        canonical_size_bytes: int | None = None,
        content_digest: str | None = None,
        issued_at: int | None = None,
        lease_expires_at: int | None = None,
    ) -> MaterialReceipt:
        self._receipt_counter += 1
        provenance = binding.provenance
        identity = binding.identity
        receipt = MaterialReceipt(
            receipt_id=f"material-receipt-{self._receipt_counter}",
            request_id=identity.request_id,
            supplier=provenance.supplier,
            source_kind=provenance.source_kind,
            purpose=provenance.purpose,
            artifact_role=provenance.artifact_role,
            schema_id=provenance.schema_id,
            canonicalization_profile=policy.canonicalization_profile,
            policy_version=policy.policy_version,
            state=state,
            lease_status=lease_status,
            content_digest=content_digest,
            raw_size_bytes=raw_size_bytes,
            canonical_size_bytes=canonical_size_bytes,
            issued_at=issued_at,
            lease_expires_at=lease_expires_at,
            consumed_at=None,
            disposed_at=None,
            error=error,
        )
        self._receipt = receipt
        return receipt

    def _reject(
        self,
        error: MaterialErrorCode,
        *,
        binding: IngressBinding | None = None,
        policy: CanonicalJsonPolicy | None = None,
        raw_size_bytes: int | None = None,
    ) -> MaterialResult:
        self._transition(MaterialState.REJECTED)
        if binding is None or policy is None:
            return MaterialResult(False, error, None)
        receipt = self._next_receipt(
            binding,
            policy,
            state=MaterialState.REJECTED,
            lease_status=None,
            error=error,
            raw_size_bytes=raw_size_bytes,
        )
        return MaterialResult(False, error, receipt)

    def prepare(
        self,
        source: str,
        *,
        tenant: TenantContext,
        binding: IngressBinding,
        capability: CapabilityMetadata,
        policy: CanonicalJsonPolicy,
        consumer: object,
        now: int,
    ) -> MaterialResult:
        """Validate, canonicalize, and lease one synthetic fixture in memory."""
        supplier_error = _supplier_preflight(binding)
        if supplier_error is not None:
            # This is intentionally before source inspection and coordinator mutation.
            return MaterialResult(False, supplier_error, None)
        if self._disposed:
            return MaterialResult(False, MaterialErrorCode.COORDINATOR_DISPOSED, None)
        if self._state is not MaterialState.CREATED or self._receipt is not None:
            return MaterialResult(
                False,
                MaterialErrorCode.COORDINATOR_ALREADY_USED,
                self._current_receipt(),
            )
        if not _is_safe_consumer(consumer):
            return self._reject(MaterialErrorCode.CONSUMER_INVALID)
        if not _is_clock(now):
            return self._reject(MaterialErrorCode.CLOCK_INVALID)
        if not isinstance(binding, IngressBinding):
            return self._reject(MaterialErrorCode.BINDING_INVALID)
        if not isinstance(policy, CanonicalJsonPolicy):
            return self._reject(MaterialErrorCode.POLICY_INVALID)

        metadata_result = validate_ingress_metadata(
            binding.identity,
            capability,
            binding.provenance,
            binding.artifact,
            tenant,
            policy,
            now=now,
        )
        if not metadata_result.valid:
            return self._reject(_map_a1_error(metadata_result.error))
        self._transition(MaterialState.CAPABILITY_VALIDATED)
        self._transition(MaterialState.SOURCE_BOUND)

        if type(source) is not str:
            return self._reject(
                MaterialErrorCode.INPUT_TYPE_INVALID, binding=binding, policy=policy
            )
        try:
            raw_octets = source.encode("utf-8", "strict")
        except UnicodeError:
            return self._reject(MaterialErrorCode.INVALID_ENCODING, binding=binding, policy=policy)
        raw_size_bytes = len(raw_octets)
        if raw_size_bytes <= 0 or raw_size_bytes > MAX_RAW_SIZE_BYTES_V1:
            return self._reject(
                MaterialErrorCode.RAW_SIZE_EXCEEDED,
                binding=binding,
                policy=policy,
                raw_size_bytes=raw_size_bytes,
            )
        self._transition(MaterialState.RAW_SIZE_VALIDATED)

        raw_octets, canonical_octets, parse_error = _parse_and_canonicalize(source)
        del raw_octets
        if parse_error is not None:
            return self._reject(
                parse_error,
                binding=binding,
                policy=policy,
                raw_size_bytes=raw_size_bytes,
            )
        self._transition(MaterialState.PARSED)
        self._transition(MaterialState.SCHEMA_VALIDATED)
        self._transition(MaterialState.CANONICALIZED)
        canonical_size_bytes = len(canonical_octets)
        if canonical_size_bytes <= 0 or canonical_size_bytes > MAX_CANONICAL_SIZE_BYTES_V1:
            return self._reject(
                MaterialErrorCode.CANONICAL_SIZE_EXCEEDED,
                binding=binding,
                policy=policy,
                raw_size_bytes=raw_size_bytes,
            )
        self._transition(MaterialState.CANONICAL_SIZE_VALIDATED)

        content_digest = hashlib.sha256(canonical_octets).hexdigest()
        expected = binding.artifact
        if (
            content_digest != expected.content_digest
            or raw_size_bytes != expected.raw_size_bytes
            or canonical_size_bytes != expected.canonical_size_bytes
        ):
            del canonical_octets
            return self._reject(
                MaterialErrorCode.ARTIFACT_MISMATCH,
                binding=binding,
                policy=policy,
                raw_size_bytes=raw_size_bytes,
            )
        self._transition(MaterialState.DIGESTED)

        material = _PrivateCanonicalMaterial(
            bytearray(canonical_octets),
            content_digest,
            raw_size_bytes,
            canonical_size_bytes,
        )
        del canonical_octets
        self._transition(MaterialState.RECEIPT_READY)
        expires_at = now + LEASE_LIFETIME_SECONDS_V1
        receipt = self._next_receipt(
            binding,
            policy,
            state=MaterialState.RECEIPT_READY,
            lease_status=LeaseStatus.ACTIVE,
            error=None,
            raw_size_bytes=raw_size_bytes,
            canonical_size_bytes=canonical_size_bytes,
            content_digest=content_digest,
            issued_at=now,
            lease_expires_at=expires_at,
        )
        self._lease = MaterialLease(material, consumer, expires_at, self)
        self._transition(MaterialState.LEASE_ISSUED)
        lease_receipt = self._update_receipt(
            state=MaterialState.LEASE_ISSUED,
            lease_status=LeaseStatus.ACTIVE,
            error=None,
        )
        return MaterialResult(True, None, lease_receipt, self._lease)

    def dispose(self, *, now: int) -> MaterialResult:
        """Dispose the whole in-memory operation; no record deletion surface exists."""
        if not _is_clock(now):
            return MaterialResult(False, MaterialErrorCode.CLOCK_INVALID, self._receipt)
        if self._disposed:
            return MaterialResult(True, None, self._receipt)
        self._disposed = True
        if self._lease is not None and self._lease.status in {
            LeaseStatus.ACTIVE,
            LeaseStatus.CONSUMING,
        }:
            self._lease._status = LeaseStatus.DISPOSED
            self._lease._material._dispose()
            self._transition(MaterialState.DISPOSED)
            receipt = self._update_receipt(
                state=MaterialState.DISPOSED,
                lease_status=LeaseStatus.DISPOSED,
                error=None,
                disposed_at=now,
            )
            return MaterialResult(True, None, receipt)
        if self._state not in {
            MaterialState.REJECTED,
            MaterialState.ABORTED,
            MaterialState.DISPOSED,
        }:
            self._transition(MaterialState.DISPOSED)
        receipt = self._update_receipt(
            state=self._state,
            lease_status=self._lease.status if self._lease else None,
            error=self._receipt.error if self._receipt else None,
            disposed_at=now if self._receipt else None,
        )
        return MaterialResult(True, None, receipt)
