from dataclasses import FrozenInstanceError

import pytest

from agent_os.persistence.authorization_contracts import (
    MAX_TTL_SECONDS,
    PAPER_CONNECTOR,
    PAPER_MODE,
    AuthorityType,
    AuthorizationIntent,
    AuthorizationScope,
    normalize_assets,
)

DIGEST = "a" * 64


def scope(assets=("BTCUSDT", "ETHUSDT")):
    return AuthorizationScope(
        tenant_id="tenant-1",
        workspace_id="workspace-1",
        agent_id="agent-1",
        agent_version="v1",
        strategy_digest=DIGEST,
        paper_account_id="paper-account-1",
        account_mode=PAPER_MODE,
        connector_id=PAPER_CONNECTOR,
        venue_id="binance",
        assets=assets,
        source_kind="synthetic_fixture",
        source_id="fixture-1",
        data_classification="synthetic_fixture_metadata_v1",
        policy_version="policy-v1",
    )


def test_scope_digest_is_canonical_and_asset_order_independent():
    assert scope(("ETHUSDT", "BTCUSDT")).scope_digest() == scope().scope_digest()
    assert scope().to_dict()["assets"] == ("BTCUSDT", "ETHUSDT")


def test_contracts_are_immutable_and_assets_are_finite():
    with pytest.raises(FrozenInstanceError):
        scope().tenant_id = "other"  # type: ignore[misc]
    with pytest.raises(ValueError):
        normalize_assets(("BTCUSDT", "BTCUSDT"))
    with pytest.raises(ValueError):
        normalize_assets(("*",))


@pytest.mark.parametrize(
    "assets",
    [
        (1,),
        (1.0,),
        (True,),
        (b"BTCUSDT",),
        (None,),
        (object(),),
        ("",),
        ("BTC*USDT",),
        ("BTCUSDT", "BTCUSDT"),
        ("BTC/USDT",),
        (type("StringSubclass", (str,), {})("BTCUSDT"),),
    ],
)
def test_malformed_assets_fail_closed_before_normalization(assets):
    with pytest.raises(ValueError, match="invalid_assets"):
        normalize_assets(assets)


def test_intent_digest_is_derived_from_canonical_request():
    intent = AuthorizationIntent(
        scope(), AuthorityType.WORKSPACE_OWNER, "issue-1", "0" * 64, 1, 100
    )
    corrected = AuthorizationIntent(
        intent.scope,
        intent.authority_type,
        intent.idempotency_key,
        intent.computed_request_digest(),
        intent.ttl_seconds,
        intent.requested_at,
    )
    assert corrected.request_digest == corrected.computed_request_digest()
    assert corrected.ttl_seconds <= MAX_TTL_SECONDS
