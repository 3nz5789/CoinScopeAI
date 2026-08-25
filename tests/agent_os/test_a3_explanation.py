import json

import pytest

from agent_os.policy.a3_explanation import (
    ExplanationMode,
    ExplanationOutcome,
    ExplanationPolicy,
    ExplanationReasonCode,
    ExplanationRequest,
    ExplanationState,
    evaluate,
    transition,
)


POLICY = ExplanationPolicy()


def digest(char: str) -> str:
    return char * 64


def request(**changes: object) -> ExplanationRequest:
    values: dict[str, object] = {
        "request_correlation_digest": digest("b"),
        "source_digest": digest("a"),
        "policy_version": POLICY.policy_version,
        "mode": ExplanationMode.PAPER,
        "canonical_state_ref_digests": (digest("c"),),
        "canonical_reference_kinds": ("strategy",),
        "provenance_digest": digest("d"),
        "requested_explanation_kind": "strategy_summary",
        "candidate_content_categories": ("advisory_summary",),
        "content_markers": ("summary",),
        "source_is_stale": False,
        "source_is_contradictory": False,
    }
    values.update(changes)
    return ExplanationRequest(**values)  # type: ignore[arg-type]


def test_valid_paper_result_is_non_actionable_and_requires_review() -> None:
    result = evaluate(request(), POLICY)
    assert result.outcome is ExplanationOutcome.NON_ACTIONABLE_ACCEPTED
    assert result.reason_code is ExplanationReasonCode.REQUEST_VALID
    assert result.requires_human_review is True
    output = result.to_dict()
    assert output["outcome"] == "non_actionable_accepted"
    assert output["reason_code"] == "request_valid"
    assert output["requires_human_review"] is True
    assert "prompt" not in output
    assert "raw_output" not in output
    assert "provider_label" not in output
    assert "model_name" not in output
    assert "safe_summary" not in output
    assert json.dumps(output, sort_keys=True)


def test_repeated_evaluation_is_deterministic() -> None:
    item = request()
    assert evaluate(item, POLICY).to_dict() == evaluate(item, POLICY).to_dict()


@pytest.mark.parametrize("mode", [ExplanationMode.TESTNET, ExplanationMode.LIVE, ExplanationMode.UNKNOWN])
def test_non_paper_modes_are_denied(mode: ExplanationMode) -> None:
    result = evaluate(request(mode=mode), POLICY)
    assert result.outcome is ExplanationOutcome.DENIED
    assert result.reason_code is ExplanationReasonCode.MODE_NON_PAPER


@pytest.mark.parametrize(
    ("kind", "reference_kind"),
    [
        ("strategy_summary", "strategy"),
        ("risk_rationale", "risk"),
        ("review_summary", "review"),
        ("paper_result_summary", "paper_execution"),
        ("provenance_summary", "provenance"),
        ("missing_evidence", "strategy"),
    ],
)
def test_all_explanation_kind_reference_mappings_are_accepted(
    kind: str, reference_kind: str
) -> None:
    result = evaluate(
        request(
            requested_explanation_kind=kind,
            canonical_reference_kinds=(reference_kind,),
        ),
        POLICY,
    )
    assert result.outcome is ExplanationOutcome.NON_ACTIONABLE_ACCEPTED
    assert result.reason_code is ExplanationReasonCode.REQUEST_VALID


@pytest.mark.parametrize(
    "changes",
    [
        {"canonical_state_ref_digests": ()},
        {"canonical_reference_kinds": ()},
        {"canonical_reference_kinds": ("review",)},
        {"canonical_reference_kinds": ("strategy", "strategy")},
        {
            "canonical_state_ref_digests": (digest("c"), digest("c")),
            "canonical_reference_kinds": ("strategy", "risk"),
        },
        {"canonical_state_ref_digests": ("A" * 64,)},
        {"canonical_state_ref_digests": ("z" * 64,)},
        {
            "canonical_state_ref_digests": tuple(digest(c) for c in "abcdef"),
            "canonical_reference_kinds": (
                "strategy",
                "risk",
                "review",
                "paper_execution",
                "provenance",
                "strategy",
            ),
        },
    ],
)
def test_invalid_or_duplicate_references_are_denied(changes: dict[str, object]) -> None:
    result = evaluate(request(**changes), POLICY)
    assert result.outcome is ExplanationOutcome.DENIED
    assert result.reason_code in {
        ExplanationReasonCode.REFERENCE_MISSING,
        ExplanationReasonCode.REFERENCE_INVALID,
    }


def test_exact_maximum_of_five_unique_references_is_supported() -> None:
    result = evaluate(
        request(
            canonical_state_ref_digests=tuple(digest(c) for c in "abcde"),
            canonical_reference_kinds=("strategy", "risk", "review", "paper_execution", "provenance"),
        ),
        POLICY,
    )
    assert result.outcome is ExplanationOutcome.NON_ACTIONABLE_ACCEPTED


@pytest.mark.parametrize(
    ("changes", "reason"),
    [
        ({"source_is_stale": True}, ExplanationReasonCode.SOURCE_STALE),
        ({"source_is_contradictory": True}, ExplanationReasonCode.SOURCE_CONTRADICTORY),
        ({"source_digest": "short"}, ExplanationReasonCode.SOURCE_DIGEST_INVALID),
        ({"provenance_digest": "short"}, ExplanationReasonCode.PROVENANCE_INVALID),
        ({"policy_version": "other-policy"}, ExplanationReasonCode.POLICY_MISMATCH),
        ({"requested_explanation_kind": "unsupported"}, ExplanationReasonCode.EXPLANATION_KIND_UNSUPPORTED),
    ],
)
def test_structural_inputs_are_denied(
    changes: dict[str, object], reason: ExplanationReasonCode
) -> None:
    result = evaluate(request(**changes), POLICY)
    assert result.outcome is ExplanationOutcome.DENIED
    assert result.reason_code is reason


@pytest.mark.parametrize(
    ("changes", "reason"),
    [
        ({"candidate_content_categories": ()}, ExplanationReasonCode.CATEGORY_INVALID),
        ({"candidate_content_categories": ("authority_language",)}, ExplanationReasonCode.AUTHORITY_LANGUAGE),
        ({"candidate_content_categories": ("secret_shaped",)}, ExplanationReasonCode.SECRET_SHAPED_CONTENT),
        ({"candidate_content_categories": ("unknown",)}, ExplanationReasonCode.UNSUPPORTED_CONTENT),
        ({"candidate_content_categories": ("advisory_summary", "unexpected")}, ExplanationReasonCode.UNSUPPORTED_CONTENT),
        ({"content_markers": ("execute",)}, ExplanationReasonCode.AUTHORITY_LANGUAGE),
        ({"content_markers": ("api_key",)}, ExplanationReasonCode.SECRET_SHAPED_CONTENT),
        ({"content_markers": ("unclassified",)}, ExplanationReasonCode.LEXICAL_UNCERTAINTY),
        ({"content_markers": (" Summary",)}, ExplanationReasonCode.LEXICAL_UNCERTAINTY),
        ({"content_markers": ("",)}, ExplanationReasonCode.LEXICAL_UNCERTAINTY),
        ({"content_markers": ("x" * 65,)}, ExplanationReasonCode.LEXICAL_UNCERTAINTY),
        ({"content_markers": tuple("summary" for _ in range(17))}, ExplanationReasonCode.LEXICAL_UNCERTAINTY),
    ],
)
def test_suspicious_or_uncertain_content_is_quarantined(
    changes: dict[str, object], reason: ExplanationReasonCode
) -> None:
    result = evaluate(request(**changes), POLICY)
    assert result.outcome is ExplanationOutcome.QUARANTINED
    assert result.reason_code is reason


def test_forward_only_state_transition() -> None:
    assert transition(ExplanationState.RECEIVED, ExplanationState.NON_ACTIONABLE_ACCEPTED)
    assert transition(ExplanationState.RECEIVED, ExplanationState.DENIED)
    assert transition(ExplanationState.RECEIVED, ExplanationState.QUARANTINED)
    assert not transition(ExplanationState.NON_ACTIONABLE_ACCEPTED, ExplanationState.RECEIVED)
    assert not transition(ExplanationState.DENIED, ExplanationState.NON_ACTIONABLE_ACCEPTED)
    assert not transition("received", ExplanationState.NON_ACTIONABLE_ACCEPTED)  # type: ignore[arg-type]


def test_invalid_policy_is_denied() -> None:
    invalid = ExplanationPolicy(policy_version="other-policy")
    result = evaluate(request(), invalid)
    assert result.outcome is ExplanationOutcome.DENIED
    assert result.reason_code is ExplanationReasonCode.REQUEST_INVALID


def test_all_outcomes_keep_human_review_true() -> None:
    for item in (
        request(),
        request(mode=ExplanationMode.LIVE),
        request(candidate_content_categories=("authority_language",)),
    ):
        assert evaluate(item, POLICY).to_dict()["requires_human_review"] is True


def test_reason_codes_are_lowercase_stable_values() -> None:
    assert all(code.value == code.value.lower() for code in ExplanationReasonCode)
    assert ExplanationReasonCode.REQUEST_VALID.value == "request_valid"
