from concurrent.futures import ThreadPoolExecutor

from agent_os.persistence.authorization_contracts import (
    AuthorityType,
    AuthorizationIntent,
    AuthorizationOutcome,
    AuthorizationReason,
    ConsumeRequest,
    RevocationRequest,
    ServerAuthorizationContext,
)
from agent_os.persistence.authorization_memory import (
    InMemoryAuditSink,
    InMemoryAuthorizationAuthority,
)

DIGEST = "a" * 64


def scope(assets=("BTCUSDT", "ETHUSDT")):
    from agent_os.persistence.authorization_contracts import AuthorizationScope

    return AuthorizationScope(
        tenant_id="tenant-1",
        workspace_id="workspace-1",
        agent_id="agent-1",
        agent_version="v1",
        strategy_digest=DIGEST,
        paper_account_id="paper-account-1",
        account_mode="paper",
        connector_id="paper",
        venue_id="binance",
        assets=assets,
        source_kind="synthetic_fixture",
        source_id="fixture-1",
        data_classification="synthetic_fixture_metadata_v1",
        policy_version="policy-v1",
    )


def context(tenant="tenant-1", workspace="workspace-1", actor="actor-1"):
    return ServerAuthorizationContext(tenant, workspace, actor, AuthorityType.WORKSPACE_OWNER)


def issue(authority, *, tenant="tenant-1", key="issue-1", ttl=10, now=100):
    base = AuthorizationIntent(scope(), AuthorityType.WORKSPACE_OWNER, key, DIGEST, ttl, now)
    intent = AuthorizationIntent(
        base.scope,
        base.authority_type,
        base.idempotency_key,
        base.computed_request_digest(),
        ttl,
        now,
    )
    return authority.issue(context(tenant), intent, now=now)


def consume_request(decision, key="consume-1"):
    base = ConsumeRequest(
        decision.grant_id, decision.scope_digest, decision.policy_version, key, DIGEST
    )
    return ConsumeRequest(
        base.grant_id,
        base.scope_digest,
        base.policy_version,
        base.idempotency_key,
        base.computed_request_digest(),
    )


def revoke_request(decision, key="revoke-1"):
    base = RevocationRequest(decision.grant_id, AuthorizationReason.REVOKED, key, DIGEST)
    return RevocationRequest(
        base.grant_id, base.reason, base.idempotency_key, base.computed_request_digest()
    )


def test_issue_consume_replay_and_single_use():
    authority = InMemoryAuthorizationAuthority()
    issued = issue(authority)
    assert issued.outcome is AuthorizationOutcome.ACCEPTED
    replay = issue(authority)
    assert replay.outcome is AuthorizationOutcome.REPLAYED
    consumed = authority.consume(context(), consume_request(issued), now=101)
    assert consumed.outcome is AuthorizationOutcome.ACCEPTED
    replayed = authority.consume(context(), consume_request(issued), now=102)
    assert replayed.outcome is AuthorizationOutcome.REPLAYED
    duplicate = authority.consume(context(), consume_request(issued, "consume-2"), now=102)
    assert duplicate.reason is AuthorizationReason.ALREADY_CONSUMED
    assert len(authority.audit_sink.events) == 2


def test_invalid_assets_return_categorical_fail_closed_denial():
    authority = InMemoryAuthorizationAuthority()
    invalid_scope = scope((123,))
    intent = AuthorizationIntent(
        invalid_scope,
        AuthorityType.WORKSPACE_OWNER,
        "invalid-assets",
        DIGEST,
        10,
        100,
    )
    result = authority.issue(context(), intent, now=100)
    assert result.outcome is AuthorizationOutcome.DENIED
    assert result.reason is AuthorizationReason.INVALID_REQUEST
    assert result.grant_id is None
    assert not authority.audit_sink.events


def test_idempotency_conflict_and_cross_tenant_non_disclosure():
    authority = InMemoryAuthorizationAuthority()
    issued = issue(authority)
    conflict_base = AuthorizationIntent(
        scope(), AuthorityType.WORKSPACE_OWNER, "issue-1", DIGEST, 11, 100
    )
    conflict = AuthorizationIntent(
        conflict_base.scope,
        conflict_base.authority_type,
        conflict_base.idempotency_key,
        conflict_base.computed_request_digest(),
        11,
        100,
    )
    result = authority.issue(context(), conflict, now=100)
    assert result.reason is AuthorizationReason.IDEMPOTENCY_CONFLICT
    foreign = authority.consume(context("tenant-2"), consume_request(issued), now=101)
    assert foreign.reason is AuthorizationReason.TENANT_SCOPE_DENIED
    assert foreign.grant_id is None


def test_revoke_invalidates_and_increments_epoch():
    authority = InMemoryAuthorizationAuthority()
    issued = issue(authority)
    revoked = authority.revoke(context(), revoke_request(issued), now=101)
    assert revoked.outcome is AuthorizationOutcome.ACCEPTED
    denied = authority.consume(context(), consume_request(issued), now=102)
    assert denied.reason is AuthorizationReason.REVOKED
    assert authority.inspect(context(), issued.grant_id, now=102).status.value == "REVOKED"


def test_expiry_is_terminal_and_audited():
    authority = InMemoryAuthorizationAuthority()
    issued = issue(authority, ttl=1)
    expired = authority.consume(context(), consume_request(issued), now=101)
    assert expired.reason is AuthorizationReason.EXPIRED
    assert authority.inspect(context(), issued.grant_id, now=101).status.value == "EXPIRED"
    assert [event.event_type.value for event in authority.audit_sink.events] == [
        "AUTH_ISSUED",
        "AUTH_EXPIRED",
    ]


def test_audit_failure_rolls_back_issue_and_consume():
    sink = InMemoryAuditSink()
    authority = InMemoryAuthorizationAuthority(sink)
    sink.fail_next = True
    failed_issue = issue(authority)
    assert failed_issue.reason is AuthorizationReason.AUDIT_WRITE_FAILED
    assert not sink.events
    issued = issue(authority, key="issue-2")
    sink.fail_next = True
    failed_consume = authority.consume(context(), consume_request(issued), now=101)
    assert failed_consume.reason is AuthorizationReason.AUDIT_WRITE_FAILED
    assert authority.inspect(context(), issued.grant_id, now=101).status.value == "ACTIVE"
    assert len(sink.events) == 1


def test_concurrent_consumers_have_one_winner():
    authority = InMemoryAuthorizationAuthority()
    issued = issue(authority)

    def consume(index):
        return authority.consume(context(), consume_request(issued, f"consume-{index}"), now=101)

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(consume, (1, 2)))
    assert sum(result.outcome is AuthorizationOutcome.ACCEPTED for result in results) == 1
    assert sum(result.reason is AuthorizationReason.ALREADY_CONSUMED for result in results) == 1
    assert (
        len(
            [
                event
                for event in authority.audit_sink.events
                if event.event_type.value == "AUTH_CONSUME_ACCEPTED"
            ]
        )
        == 1
    )
