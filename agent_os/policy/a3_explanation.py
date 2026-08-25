"""Pure deterministic boundary for a future AI explanation capability.

This module accepts categorical metadata only. It consumes caller-supplied
opaque references, performs pure local checks, and returns closed policy
results without external effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re
from typing import Final


_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_IDENTIFIER = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
_POLICY_VERSION = "a3-explanation-v1"
_MAX_REFERENCES = 5
_MAX_MARKERS = 16
_MAX_MARKER_LENGTH = 64
_ZERO_DIGEST = "0" * 64


class ExplanationMode(str, Enum):
    PAPER = "paper"
    TESTNET = "testnet"
    LIVE = "live"
    UNKNOWN = "unknown"


class ExplanationOutcome(str, Enum):
    NON_ACTIONABLE_ACCEPTED = "non_actionable_accepted"
    DENIED = "denied"
    QUARANTINED = "quarantined"


class ExplanationReasonCode(str, Enum):
    REQUEST_INVALID = "request_invalid"
    REQUEST_VALID = "request_valid"
    POLICY_MISMATCH = "policy_mismatch"
    SOURCE_MISSING = "source_missing"
    SOURCE_DIGEST_INVALID = "source_digest_invalid"
    PROVENANCE_INVALID = "provenance_invalid"
    REFERENCE_MISSING = "reference_missing"
    REFERENCE_INVALID = "reference_invalid"
    EXPLANATION_KIND_UNSUPPORTED = "explanation_kind_unsupported"
    MODE_NON_PAPER = "mode_non_paper"
    SOURCE_STALE = "source_stale"
    SOURCE_CONTRADICTORY = "source_contradictory"
    CATEGORY_INVALID = "category_invalid"
    AUTHORITY_LANGUAGE = "authority_language"
    SECRET_SHAPED_CONTENT = "secret_shaped_content"
    LEXICAL_UNCERTAINTY = "lexical_uncertainty"
    UNSUPPORTED_CONTENT = "unsupported_content"


class ExplanationState(str, Enum):
    RECEIVED = "received"
    NON_ACTIONABLE_ACCEPTED = "non_actionable_accepted"
    DENIED = "denied"
    QUARANTINED = "quarantined"


_EXPLANATION_KINDS: Final[tuple[str, ...]] = (
    "missing_evidence",
    "paper_result_summary",
    "provenance_summary",
    "review_summary",
    "risk_rationale",
    "strategy_summary",
)
_CANONICAL_REFERENCE_KINDS: Final[frozenset[str]] = frozenset(
    {"strategy", "risk", "review", "paper_execution", "provenance"}
)
_REQUIRED_REFERENCE_KIND: Final[dict[str, str]] = {
    "strategy_summary": "strategy",
    "risk_rationale": "risk",
    "review_summary": "review",
    "paper_result_summary": "paper_execution",
    "provenance_summary": "provenance",
    "missing_evidence": "strategy",
}
_CATEGORICAL_CONTENT: Final[frozenset[str]] = frozenset(
    {"advisory_summary", "uncertainty", "missing_evidence"}
)
_MARKER_TOKENS: Final[frozenset[str]] = frozenset(
    {"summary", "rationale", "uncertainty", "missing_evidence", "provenance"}
)
_AUTHORITY_WORDS: Final[frozenset[str]] = frozenset(
    {
        "authorize",
        "authorized",
        "approve",
        "approval",
        "cancel",
        "execute",
        "executed",
        "order",
        "route",
        "size",
        "submit",
        "trade",
        "withdraw",
    }
)
_SECRET_SHAPES: Final[tuple[re.Pattern[str], ...]] = (
    re.compile(r"(?:api[_-]?key|private[_-]?key|seed[_-]?phrase|bearer)"),
    re.compile(r"\bsk-[a-z0-9_-]{8,}\b"),
)


@dataclass(frozen=True)
class ExplanationPolicy:
    """Immutable policy metadata for categorical explanation evaluation."""

    policy_version: str = _POLICY_VERSION
    explanation_kinds: tuple[str, ...] = _EXPLANATION_KINDS
    max_references: int = _MAX_REFERENCES
    max_markers: int = _MAX_MARKERS


@dataclass(frozen=True)
class ExplanationRequest:
    """Typed metadata request containing no generated prose."""

    request_correlation_digest: str
    source_digest: str
    policy_version: str
    mode: ExplanationMode
    canonical_state_ref_digests: tuple[str, ...]
    canonical_reference_kinds: tuple[str, ...]
    provenance_digest: str
    requested_explanation_kind: str
    candidate_content_categories: tuple[str, ...] = ("advisory_summary",)
    content_markers: tuple[str, ...] = ()
    source_is_stale: bool = False
    source_is_contradictory: bool = False


@dataclass(frozen=True)
class ExplanationEvaluation:
    """Closed categorical result that cannot authorize an action."""

    request_correlation_digest: str
    source_digest: str
    policy_version: str
    mode: ExplanationMode
    canonical_state_ref_digests: tuple[str, ...]
    provenance_digest: str
    outcome: ExplanationOutcome
    reason_code: ExplanationReasonCode
    requires_human_review: bool = True

    def to_dict(self) -> dict[str, object]:
        return {
            "request_correlation_digest": self.request_correlation_digest,
            "source_digest": self.source_digest,
            "policy_version": self.policy_version,
            "mode": self.mode.value,
            "canonical_state_ref_digests": list(self.canonical_state_ref_digests),
            "provenance_digest": self.provenance_digest,
            "outcome": self.outcome.value,
            "reason_code": self.reason_code.value,
            "requires_human_review": True,
        }


def _valid_digest(value: object) -> bool:
    return isinstance(value, str) and _DIGEST.fullmatch(value) is not None


def _valid_identifier(value: object) -> bool:
    return isinstance(value, str) and _IDENTIFIER.fullmatch(value) is not None


def _invalid_result(
    request: object, policy: ExplanationPolicy, reason: ExplanationReasonCode
) -> ExplanationEvaluation:
    mode = (
        request.mode
        if isinstance(request, ExplanationRequest) and isinstance(request.mode, ExplanationMode)
        else ExplanationMode.UNKNOWN
    )
    correlation = (
        request.request_correlation_digest
        if isinstance(request, ExplanationRequest)
        and _valid_digest(request.request_correlation_digest)
        else _ZERO_DIGEST
    )
    source = (
        request.source_digest
        if isinstance(request, ExplanationRequest) and _valid_digest(request.source_digest)
        else _ZERO_DIGEST
    )
    provenance = (
        request.provenance_digest
        if isinstance(request, ExplanationRequest) and _valid_digest(request.provenance_digest)
        else _ZERO_DIGEST
    )
    version = (
        policy.policy_version
        if isinstance(policy, ExplanationPolicy) and _valid_identifier(policy.policy_version)
        else "invalid-policy"
    )
    return ExplanationEvaluation(
        request_correlation_digest=correlation,
        source_digest=source,
        policy_version=version,
        mode=mode,
        canonical_state_ref_digests=(),
        provenance_digest=provenance,
        outcome=ExplanationOutcome.DENIED,
        reason_code=reason,
    )


def _result(
    request: ExplanationRequest,
    outcome: ExplanationOutcome,
    reason: ExplanationReasonCode,
) -> ExplanationEvaluation:
    return ExplanationEvaluation(
        request_correlation_digest=request.request_correlation_digest,
        source_digest=request.source_digest,
        policy_version=request.policy_version,
        mode=request.mode,
        canonical_state_ref_digests=request.canonical_state_ref_digests,
        provenance_digest=request.provenance_digest,
        outcome=outcome,
        reason_code=reason,
    )


def _valid_policy(policy: ExplanationPolicy) -> bool:
    return (
        isinstance(policy, ExplanationPolicy)
        and policy.policy_version == _POLICY_VERSION
        and _valid_identifier(policy.policy_version)
        and policy.explanation_kinds == _EXPLANATION_KINDS
        and isinstance(policy.max_references, int)
        and not isinstance(policy.max_references, bool)
        and 1 <= policy.max_references <= _MAX_REFERENCES
        and isinstance(policy.max_markers, int)
        and not isinstance(policy.max_markers, bool)
        and 1 <= policy.max_markers <= _MAX_MARKERS
    )


def _authority_or_secret_reason(value: str) -> ExplanationReasonCode | None:
    normalized = value.lower()
    if any(pattern.search(normalized) for pattern in _SECRET_SHAPES):
        return ExplanationReasonCode.SECRET_SHAPED_CONTENT
    if any(word in normalized.split() for word in _AUTHORITY_WORDS):
        return ExplanationReasonCode.AUTHORITY_LANGUAGE
    return None


def _category_reason(categories: object) -> ExplanationReasonCode | None:
    if not isinstance(categories, tuple) or not categories:
        return ExplanationReasonCode.CATEGORY_INVALID
    saw_authority = False
    for category in categories:
        if not isinstance(category, str) or not category or category != category.lower():
            return ExplanationReasonCode.CATEGORY_INVALID
        specific = _authority_or_secret_reason(category)
        if specific is ExplanationReasonCode.SECRET_SHAPED_CONTENT:
            return specific
        if specific is ExplanationReasonCode.AUTHORITY_LANGUAGE:
            saw_authority = True
        elif category == "secret_shaped":
            return ExplanationReasonCode.SECRET_SHAPED_CONTENT
        elif category == "authority_language":
            saw_authority = True
        elif category not in _CATEGORICAL_CONTENT:
            return ExplanationReasonCode.UNSUPPORTED_CONTENT
    if saw_authority:
        return ExplanationReasonCode.AUTHORITY_LANGUAGE
    return None


def _marker_reason(markers: object, maximum: int) -> ExplanationReasonCode | None:
    if not isinstance(markers, tuple) or len(markers) > maximum:
        return ExplanationReasonCode.LEXICAL_UNCERTAINTY
    for marker in markers:
        if not isinstance(marker, str) or not marker or len(marker) > _MAX_MARKER_LENGTH:
            return ExplanationReasonCode.LEXICAL_UNCERTAINTY
        specific = _authority_or_secret_reason(marker)
        if specific is not None:
            return specific
        if marker != marker.lower() or marker != marker.strip() or marker not in _MARKER_TOKENS:
            return ExplanationReasonCode.LEXICAL_UNCERTAINTY
    return None


def _reference_reason(
    request: ExplanationRequest, policy: ExplanationPolicy
) -> ExplanationReasonCode | None:
    refs = request.canonical_state_ref_digests
    kinds = request.canonical_reference_kinds
    if not isinstance(refs, tuple) or not isinstance(kinds, tuple) or not refs:
        return ExplanationReasonCode.REFERENCE_MISSING
    if len(refs) != len(kinds) or len(refs) > policy.max_references:
        return ExplanationReasonCode.REFERENCE_INVALID
    if len(set(refs)) != len(refs) or len(set(kinds)) != len(kinds):
        return ExplanationReasonCode.REFERENCE_INVALID
    if not all(_valid_digest(value) for value in refs):
        return ExplanationReasonCode.REFERENCE_INVALID
    if not all(isinstance(value, str) and value in _CANONICAL_REFERENCE_KINDS for value in kinds):
        return ExplanationReasonCode.REFERENCE_INVALID
    required = _REQUIRED_REFERENCE_KIND.get(request.requested_explanation_kind)
    if required is None:
        return ExplanationReasonCode.EXPLANATION_KIND_UNSUPPORTED
    if required not in kinds:
        return ExplanationReasonCode.REFERENCE_MISSING
    return None


def evaluate(
    request: ExplanationRequest, policy: ExplanationPolicy | None = None
) -> ExplanationEvaluation:
    """Return a deterministic categorical boundary result for metadata only."""
    effective_policy = policy if policy is not None else ExplanationPolicy()
    if not _valid_policy(effective_policy) or not isinstance(request, ExplanationRequest):
        return _invalid_result(request, effective_policy, ExplanationReasonCode.REQUEST_INVALID)
    if request.policy_version != effective_policy.policy_version:
        return _invalid_result(request, effective_policy, ExplanationReasonCode.POLICY_MISMATCH)
    if not _valid_digest(request.request_correlation_digest):
        return _invalid_result(request, effective_policy, ExplanationReasonCode.REQUEST_INVALID)
    if not _valid_digest(request.source_digest):
        return _invalid_result(request, effective_policy, ExplanationReasonCode.SOURCE_DIGEST_INVALID)
    if not _valid_digest(request.provenance_digest):
        return _invalid_result(request, effective_policy, ExplanationReasonCode.PROVENANCE_INVALID)
    if request.requested_explanation_kind not in effective_policy.explanation_kinds:
        return _invalid_result(request, effective_policy, ExplanationReasonCode.EXPLANATION_KIND_UNSUPPORTED)
    if not isinstance(request.mode, ExplanationMode) or request.mode is not ExplanationMode.PAPER:
        return _invalid_result(request, effective_policy, ExplanationReasonCode.MODE_NON_PAPER)
    if not isinstance(request.source_is_stale, bool) or request.source_is_stale:
        return _invalid_result(request, effective_policy, ExplanationReasonCode.SOURCE_STALE)
    if not isinstance(request.source_is_contradictory, bool) or request.source_is_contradictory:
        return _invalid_result(request, effective_policy, ExplanationReasonCode.SOURCE_CONTRADICTORY)
    reference_reason = _reference_reason(request, effective_policy)
    if reference_reason is not None:
        return _invalid_result(request, effective_policy, reference_reason)
    category_reason = _category_reason(request.candidate_content_categories)
    marker_reason = _marker_reason(request.content_markers, effective_policy.max_markers)
    for priority_reason in (
        ExplanationReasonCode.SECRET_SHAPED_CONTENT,
        ExplanationReasonCode.AUTHORITY_LANGUAGE,
    ):
        if category_reason is priority_reason or marker_reason is priority_reason:
            return _result(request, ExplanationOutcome.QUARANTINED, priority_reason)
    if category_reason is not None:
        return _result(request, ExplanationOutcome.QUARANTINED, category_reason)
    if marker_reason is not None:
        return _result(request, ExplanationOutcome.QUARANTINED, marker_reason)
    return _result(
        request,
        ExplanationOutcome.NON_ACTIONABLE_ACCEPTED,
        ExplanationReasonCode.REQUEST_VALID,
    )


_TRANSITIONS: Final[dict[ExplanationState, frozenset[ExplanationState]]] = {
    ExplanationState.RECEIVED: frozenset(
        {
            ExplanationState.NON_ACTIONABLE_ACCEPTED,
            ExplanationState.DENIED,
            ExplanationState.QUARANTINED,
        }
    ),
    ExplanationState.NON_ACTIONABLE_ACCEPTED: frozenset(),
    ExplanationState.DENIED: frozenset(),
    ExplanationState.QUARANTINED: frozenset(),
}


def transition(current: ExplanationState, target: ExplanationState) -> bool:
    """Permit only one forward transition from received to a terminal state."""
    if not isinstance(current, ExplanationState) or not isinstance(target, ExplanationState):
        return False
    return target in _TRANSITIONS.get(current, frozenset())


__all__ = [
    "ExplanationEvaluation",
    "ExplanationMode",
    "ExplanationOutcome",
    "ExplanationPolicy",
    "ExplanationReasonCode",
    "ExplanationRequest",
    "ExplanationState",
    "evaluate",
    "transition",
]
