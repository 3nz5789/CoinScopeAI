"""Pure A3 PaperRun recording-capture eligibility policy.

This module evaluates supplied metadata only.  It does not import or invoke
material handling, ingress coordination, recording, replay, storage, runtime,
risk, execution, API, worker, or external systems.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import re
from typing import Any, Final

MAX_APPROVAL_TTL_SECONDS: Final[int] = 600
ELIGIBLE_CLASSIFICATION: Final[str] = "synthetic_fixture_metadata_v1"
PAPER_MODE: Final[str] = "paper"
PAPER_CONNECTOR: Final[str] = "paper"

_IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")
_WILDCARD = frozenset({"*", "?"})


class CaptureLifecycle(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    EVALUATED = "EVALUATED"
    APPROVED_FOR_FUTURE_CAPTURE = "APPROVED_FOR_FUTURE_CAPTURE"
    DENIED = "DENIED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


class CaptureDecision(str, Enum):
    APPROVED_FOR_FUTURE_CAPTURE = "APPROVED_FOR_FUTURE_CAPTURE"
    DENIED = "DENIED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


class AuthorityType(str, Enum):
    WORKSPACE_OWNER = "WORKSPACE_OWNER"
    TRADING_RISK_REVIEWER = "TRADING_RISK_REVIEWER"
    DATA_REVIEWER = "DATA_REVIEWER"


class CaptureReasonCode(str, Enum):
    REQUEST_INVALID = "A3_REQUEST_INVALID"
    POLICY_MISSING = "A3_POLICY_MISSING"
    POLICY_MISMATCH = "A3_POLICY_MISMATCH"
    TENANT_BINDING_MISMATCH = "A3_TENANT_BINDING_MISMATCH"
    WORKSPACE_BINDING_MISMATCH = "A3_WORKSPACE_BINDING_MISMATCH"
    AGENT_BINDING_MISMATCH = "A3_AGENT_BINDING_MISMATCH"
    STRATEGY_DIGEST_MISMATCH = "A3_STRATEGY_DIGEST_MISMATCH"
    PAPER_ACCOUNT_INVALID = "A3_PAPER_ACCOUNT_INVALID"
    CONNECTOR_NOT_PAPER = "A3_CONNECTOR_NOT_PAPER"
    LIVE_OR_TESTNET_DENIED = "A3_LIVE_OR_TESTNET_DENIED"
    VENUE_NOT_ALLOWLISTED = "A3_VENUE_NOT_ALLOWLISTED"
    ASSET_NOT_ALLOWLISTED = "A3_ASSET_NOT_ALLOWLISTED"
    SOURCE_NOT_ALLOWLISTED = "A3_SOURCE_NOT_ALLOWLISTED"
    CLASSIFICATION_NOT_ALLOWLISTED = "A3_CLASSIFICATION_NOT_ALLOWLISTED"
    AUTHORITY_NOT_ALLOWLISTED = "A3_AUTHORITY_NOT_ALLOWLISTED"
    AUTH_EVIDENCE_INVALID = "A3_AUTH_EVIDENCE_INVALID"
    AUTH_SCOPE_MISMATCH = "A3_AUTH_SCOPE_MISMATCH"
    AUTH_NOT_YET_VALID = "A3_AUTH_NOT_YET_VALID"
    AUTH_EXPIRED = "A3_AUTH_EXPIRED"
    AUTH_REVOKED = "A3_AUTH_REVOKED"
    AUTH_ALREADY_CONSUMED = "A3_AUTH_ALREADY_CONSUMED"
    IDEMPOTENCY_CONFLICT = "A3_IDEMPOTENCY_CONFLICT"
    PROVENANCE_INVALID = "A3_PROVENANCE_INVALID"
    UNKNOWN_STATE = "A3_UNKNOWN_STATE"
    CAPTURE_DISABLED = "A3_CAPTURE_DISABLED"
    INTERNAL_POLICY_UNAVAILABLE = "A3_INTERNAL_POLICY_UNAVAILABLE"


@dataclass(frozen=True)
class CapturePolicy:
    """Immutable supplied policy; capture activation is intentionally absent."""

    policy_version: str
    allowed_venues: tuple[str, ...]
    allowed_assets: tuple[str, ...]
    allowed_source_kinds: tuple[str, ...] = ("synthetic_fixture",)
    allowed_classifications: tuple[str, ...] = (ELIGIBLE_CLASSIFICATION,)
    max_ttl_seconds: int = MAX_APPROVAL_TTL_SECONDS
    require_single_use: bool = True
    require_revocation_check: bool = True


@dataclass(frozen=True)
class CaptureRequest:
    """Internal request metadata; request_id is never emitted by safe output."""

    request_id: str
    idempotency_key: str
    tenant_id: str
    workspace_id: str
    agent_id: str
    agent_version: str
    strategy_digest: str
    paper_account_id: str
    account_mode: str
    connector_id: str
    venue_id: str
    assets: tuple[str, ...]
    source_kind: str
    source_id: str
    data_classification: str
    requested_at: int
    requested_by: str
    policy_version: str

    def __repr__(self) -> str:
        return "<CaptureRequest internal-only>"


@dataclass(frozen=True)
class HumanAuthorizationEvidence:
    """Supplied metadata evidence; authentication is a later boundary."""

    authority_type: AuthorityType
    authority_id: str
    decision_id: str
    approved_at: int
    expires_at: int
    scope_digest: str
    evidence_digest: str
    single_use_nonce: str
    revocation_epoch: int
    revoked: bool = False
    consumed: bool = False

    def __repr__(self) -> str:
        return "<HumanAuthorizationEvidence internal-only>"


@dataclass(frozen=True)
class CaptureBinding:
    """Exact request scope used for canonical digesting."""

    tenant_id: str
    workspace_id: str
    agent_id: str
    agent_version: str
    strategy_digest: str
    paper_account_id: str
    account_mode: str
    connector_id: str
    venue_id: str
    assets: tuple[str, ...]
    source_kind: str
    source_id: str
    data_classification: str
    policy_version: str
    authorization_scope_digest: str

    def __repr__(self) -> str:
        return "<CaptureBinding internal-only>"


@dataclass(frozen=True)
class SafeCaptureDecision:
    """Whitelist-only output; raw request, tenant, workspace, and account IDs omit."""

    decision_id: str
    binding_digest: str
    provenance_digest: str
    policy_version: str
    outcome: CaptureDecision
    reason_code: CaptureReasonCode | None
    expires_at: int | None
    single_use: bool
    revocable: bool
    recheck_required: bool = True

    def to_dict(self) -> dict[str, object]:
        return {
            "decision_id": self.decision_id,
            "binding_digest": self.binding_digest,
            "provenance_digest": self.provenance_digest,
            "policy_version": self.policy_version,
            "outcome": self.outcome.value,
            "reason_code": self.reason_code.value if self.reason_code else None,
            "expires_at": self.expires_at,
            "single_use": self.single_use,
            "revocable": self.revocable,
            "recheck_required": True,
        }


@dataclass(frozen=True)
class CaptureEvaluation:
    """Internal evaluation with a safe public projection."""

    request_id: str
    state: CaptureLifecycle
    decision: SafeCaptureDecision

    def __repr__(self) -> str:
        return f"<CaptureEvaluation state={self.state.value!r} decision={self.decision!r}>"

    def to_dict(self) -> dict[str, object]:
        value = self.decision.to_dict()
        value["state"] = self.state.value
        return value


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8", "strict")


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _valid_identifier(value: object) -> bool:
    return isinstance(value, str) and _IDENTIFIER.fullmatch(value) is not None


def _valid_digest(value: object) -> bool:
    return isinstance(value, str) and _DIGEST.fullmatch(value) is not None


def _valid_policy_allowlist(value: object, *, asset: bool = False) -> bool:
    if not isinstance(value, (tuple, list)) or not value:
        return False
    if not all(isinstance(item, str) for item in value):
        return False
    if asset:
        try:
            normalized = normalize_assets(value)
        except ValueError:
            return False
        return tuple(value) == normalized
    normalized = tuple(item.strip().lower() for item in value)
    return (
        tuple(value) == normalized
        and len(set(normalized)) == len(normalized)
        and all(
            _valid_identifier(item) and not any(mark in item for mark in _WILDCARD)
            for item in normalized
        )
    )


def _validate_policy(policy: CapturePolicy) -> CaptureReasonCode | None:
    if not _valid_identifier(policy.policy_version):
        return CaptureReasonCode.POLICY_MISMATCH
    if (
        not isinstance(policy.max_ttl_seconds, int)
        or isinstance(policy.max_ttl_seconds, bool)
        or policy.max_ttl_seconds <= 0
        or policy.max_ttl_seconds > MAX_APPROVAL_TTL_SECONDS
    ):
        return CaptureReasonCode.POLICY_MISMATCH
    if policy.allowed_classifications not in (
        (ELIGIBLE_CLASSIFICATION,),
        [ELIGIBLE_CLASSIFICATION],
    ):
        return CaptureReasonCode.POLICY_MISMATCH
    if policy.allowed_source_kinds not in (("synthetic_fixture",), ["synthetic_fixture"]):
        return CaptureReasonCode.POLICY_MISMATCH
    if not _valid_policy_allowlist(policy.allowed_venues):
        return CaptureReasonCode.POLICY_MISMATCH
    if not _valid_policy_allowlist(policy.allowed_assets, asset=True):
        return CaptureReasonCode.POLICY_MISMATCH
    if policy.require_single_use is not True or policy.require_revocation_check is not True:
        return CaptureReasonCode.POLICY_MISMATCH
    return None


def normalize_assets(assets: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    """Normalize asset identifiers and reject empty, duplicate, or wildcard values."""
    if not isinstance(assets, (tuple, list)) or not assets:
        raise ValueError(CaptureReasonCode.ASSET_NOT_ALLOWLISTED.value)
    normalized = tuple(sorted(str(asset).upper() for asset in assets))
    if any(
        not _valid_identifier(asset) or asset in _WILDCARD or asset == "" for asset in normalized
    ) or len(set(normalized)) != len(normalized):
        raise ValueError(CaptureReasonCode.ASSET_NOT_ALLOWLISTED.value)
    return normalized


def binding_digest(request: CaptureRequest, authorization_scope_digest: str | None = None) -> str:
    """Hash exact canonical binding metadata, excluding all derived digest fields.

    ``authorization_scope_digest`` is accepted for call-site compatibility but is
    intentionally excluded: evidence.scope_digest must equal this digest, so
    including it would create a circular digest definition.
    """
    assets = normalize_assets(request.assets)
    value = {
        "account_mode": request.account_mode,
        "agent_id": request.agent_id,
        "agent_version": request.agent_version,
        "assets": assets,
        "connector_id": request.connector_id,
        "data_classification": request.data_classification,
        "paper_account_id": request.paper_account_id,
        "policy_version": request.policy_version,
        "source_id": request.source_id,
        "source_kind": request.source_kind,
        "strategy_digest": request.strategy_digest,
        "tenant_id": request.tenant_id,
        "venue_id": request.venue_id,
        "workspace_id": request.workspace_id,
    }
    return _digest(value)


def provenance_digest(request: CaptureRequest, binding: str) -> str:
    """Hash digest-only provenance metadata without including derived digest fields."""
    value = {
        "binding": binding,
        "classification": request.data_classification,
        "policy_version": request.policy_version,
        "source_id": request.source_id,
        "source_kind": request.source_kind,
    }
    return _digest(value)


def _decision_id(request: CaptureRequest, binding: str, now: int) -> str:
    return "a3d-" + _digest({"binding": binding, "now": now, "request": request.request_id})[:32]


def _base_decision(
    request: CaptureRequest,
    policy: CapturePolicy,
    now: int,
    outcome: CaptureDecision,
    reason: CaptureReasonCode | None,
    *,
    expires_at: int | None = None,
    binding: str = "0" * 64,
) -> SafeCaptureDecision:
    return SafeCaptureDecision(
        decision_id=_decision_id(request, binding, now),
        binding_digest=binding,
        provenance_digest=provenance_digest(request, binding) if binding != "0" * 64 else "0" * 64,
        policy_version=policy.policy_version,
        outcome=outcome,
        reason_code=reason,
        expires_at=expires_at,
        single_use=True,
        revocable=True,
    )


def _invalid(
    request: CaptureRequest, policy: CapturePolicy, now: int, reason: CaptureReasonCode
) -> CaptureEvaluation:
    return CaptureEvaluation(
        request.request_id,
        CaptureLifecycle.EVALUATED,
        _base_decision(request, policy, now, CaptureDecision.DENIED, reason),
    )


def evaluate(
    request: CaptureRequest,
    authorizations: tuple[HumanAuthorizationEvidence, ...],
    policy: CapturePolicy,
    *,
    now: int,
    revoked_epochs: tuple[int, ...] = (),
) -> CaptureEvaluation:
    """Evaluate supplied metadata only; valid A3 v1 requests end disabled."""
    if (
        not isinstance(request, CaptureRequest)
        or not isinstance(policy, CapturePolicy)
        or not isinstance(now, int)
        or isinstance(now, bool)
        or now < 0
    ):
        safe_request = (
            request
            if isinstance(request, CaptureRequest)
            else CaptureRequest(
                "invalid",
                "invalid",
                "invalid",
                "invalid",
                "invalid",
                "invalid",
                "0" * 64,
                "invalid",
                "invalid",
                "invalid",
                "invalid",
                ("INVALID",),
                "invalid",
                "invalid",
                "invalid",
                0,
                "invalid",
                "invalid",
            )
        )
        safe_policy = (
            policy if isinstance(policy, CapturePolicy) else CapturePolicy("invalid", (), ())
        )
        return _invalid(
            safe_request,
            safe_policy,
            now if isinstance(now, int) and not isinstance(now, bool) and now >= 0 else 0,
            CaptureReasonCode.REQUEST_INVALID,
        )
    policy_error = _validate_policy(policy)
    if policy_error is not None:
        return _invalid(request, policy, now, policy_error)
    if (
        not _valid_identifier(request.request_id)
        or not _valid_identifier(request.idempotency_key)
        or not _valid_identifier(request.requested_by)
    ):
        return _invalid(request, policy, now, CaptureReasonCode.REQUEST_INVALID)
    if not _valid_identifier(request.tenant_id) or not _valid_identifier(request.workspace_id):
        return _invalid(
            request,
            policy,
            now,
            (
                CaptureReasonCode.TENANT_BINDING_MISMATCH
                if not _valid_identifier(request.tenant_id)
                else CaptureReasonCode.WORKSPACE_BINDING_MISMATCH
            ),
        )
    if not all(
        _valid_identifier(value)
        for value in (
            request.agent_id,
            request.agent_version,
            request.paper_account_id,
            request.venue_id,
            request.source_kind,
            request.source_id,
            request.policy_version,
        )
    ):
        return _invalid(request, policy, now, CaptureReasonCode.REQUEST_INVALID)
    if not _valid_digest(request.strategy_digest):
        return _invalid(request, policy, now, CaptureReasonCode.STRATEGY_DIGEST_MISMATCH)
    if request.policy_version != policy.policy_version:
        return _invalid(request, policy, now, CaptureReasonCode.POLICY_MISMATCH)
    if request.account_mode in {"live", "testnet"}:
        return _invalid(request, policy, now, CaptureReasonCode.LIVE_OR_TESTNET_DENIED)
    if request.account_mode != PAPER_MODE:
        return _invalid(request, policy, now, CaptureReasonCode.PAPER_ACCOUNT_INVALID)
    if request.connector_id != PAPER_CONNECTOR:
        return _invalid(request, policy, now, CaptureReasonCode.CONNECTOR_NOT_PAPER)
    try:
        assets = normalize_assets(request.assets)
    except ValueError:
        return _invalid(request, policy, now, CaptureReasonCode.ASSET_NOT_ALLOWLISTED)
    if request.venue_id not in policy.allowed_venues:
        return _invalid(request, policy, now, CaptureReasonCode.VENUE_NOT_ALLOWLISTED)
    if any(asset not in policy.allowed_assets for asset in assets):
        return _invalid(request, policy, now, CaptureReasonCode.ASSET_NOT_ALLOWLISTED)
    if request.source_kind not in policy.allowed_source_kinds:
        return _invalid(request, policy, now, CaptureReasonCode.SOURCE_NOT_ALLOWLISTED)
    if (
        request.data_classification != ELIGIBLE_CLASSIFICATION
        or request.data_classification not in policy.allowed_classifications
    ):
        return _invalid(request, policy, now, CaptureReasonCode.CLASSIFICATION_NOT_ALLOWLISTED)
    if not isinstance(authorizations, tuple) or not authorizations:
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_EVIDENCE_INVALID)
    owner = [
        item
        for item in authorizations
        if isinstance(item, HumanAuthorizationEvidence)
        and item.authority_type is AuthorityType.WORKSPACE_OWNER
    ]
    if len(owner) != 1:
        return _invalid(request, policy, now, CaptureReasonCode.AUTHORITY_NOT_ALLOWLISTED)
    evidence = owner[0]
    if (
        not all(
            _valid_identifier(value)
            for value in (evidence.authority_id, evidence.decision_id, evidence.single_use_nonce)
        )
        or not _valid_digest(evidence.scope_digest)
        or not _valid_digest(evidence.evidence_digest)
        or not isinstance(evidence.revocation_epoch, int)
        or isinstance(evidence.revocation_epoch, bool)
        or evidence.revocation_epoch < 0
    ):
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_EVIDENCE_INVALID)
    if evidence.approved_at > now:
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_NOT_YET_VALID)
    if (
        evidence.expires_at <= evidence.approved_at
        or evidence.expires_at - evidence.approved_at > MAX_APPROVAL_TTL_SECONDS
        or evidence.expires_at - evidence.approved_at > policy.max_ttl_seconds
        or evidence.expires_at <= now
    ):
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_EXPIRED)
    if evidence.revoked or evidence.revocation_epoch in revoked_epochs:
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_REVOKED)
    if evidence.consumed:
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_ALREADY_CONSUMED)
    binding = binding_digest(request, evidence.scope_digest)
    if evidence.scope_digest != binding:
        return _invalid(request, policy, now, CaptureReasonCode.AUTH_SCOPE_MISMATCH)
    provenance = provenance_digest(request, binding)
    decision = SafeCaptureDecision(
        decision_id=_decision_id(request, binding, now),
        binding_digest=binding,
        provenance_digest=provenance,
        policy_version=policy.policy_version,
        outcome=CaptureDecision.DENIED,
        reason_code=CaptureReasonCode.CAPTURE_DISABLED,
        expires_at=evidence.expires_at,
        single_use=True,
        revocable=True,
        recheck_required=True,
    )
    return CaptureEvaluation(request.request_id, CaptureLifecycle.EVALUATED, decision)


_ALLOWED_TRANSITIONS: Final[dict[CaptureLifecycle, frozenset[CaptureLifecycle]]] = {
    CaptureLifecycle.DRAFT: frozenset({CaptureLifecycle.SUBMITTED, CaptureLifecycle.CANCELLED}),
    CaptureLifecycle.SUBMITTED: frozenset({CaptureLifecycle.EVALUATED, CaptureLifecycle.CANCELLED}),
    CaptureLifecycle.EVALUATED: frozenset(
        {
            CaptureLifecycle.APPROVED_FOR_FUTURE_CAPTURE,
            CaptureLifecycle.DENIED,
            CaptureLifecycle.EXPIRED,
            CaptureLifecycle.CANCELLED,
        }
    ),
    CaptureLifecycle.APPROVED_FOR_FUTURE_CAPTURE: frozenset(
        {CaptureLifecycle.EXPIRED, CaptureLifecycle.CANCELLED}
    ),
    CaptureLifecycle.DENIED: frozenset(),
    CaptureLifecycle.EXPIRED: frozenset(),
    CaptureLifecycle.CANCELLED: frozenset(),
}


def transition(current: CaptureLifecycle, target: CaptureLifecycle) -> bool:
    """Return whether a pure lifecycle transition is legal; perform no transition."""
    if not isinstance(current, CaptureLifecycle) or not isinstance(target, CaptureLifecycle):
        return False
    return target in _ALLOWED_TRANSITIONS.get(current, frozenset())
