"""Deterministic process-local A4-v1 authorization authority.

The implementation is deliberately metadata-only and process-local. It does
not import or invoke storage, network, subprocess, runtime, capture, scanner,
replay, execution, API, worker, connector, wallet, exchange, or external code.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import threading
from typing import Callable, Mapping, NamedTuple

from .audit_contracts import AuditEvent, AuditEventType, AuditOutcome, RedactedAuditEvent
from .audit_redaction import redact_audit_event
from .authorization_contracts import (
    MAX_TTL_SECONDS,
    MIN_TTL_SECONDS,
    PAPER_CONNECTOR,
    PAPER_MODE,
    AuthorizationDecision,
    AuthorizationGrant,
    AuthorizationIntent,
    AuthorizationOutcome,
    AuthorizationReason,
    AuthorizationScope,
    AuthorizationStatus,
    ConsumeRequest,
    RedactedAuthorizationView,
    RevocationRequest,
    ServerAuthorizationContext,
    digest_value,
    valid_digest,
    valid_identifier,
)


@dataclass(frozen=True)
class _StoredDecision:
    request_digest: str
    scope_digest: str | None
    policy_version: str | None
    decision: AuthorizationDecision


class _RollbackSnapshot(NamedTuple):
    grants: dict[tuple[str, str], AuthorizationGrant]
    issue_idempotency: dict[tuple[str, str], _StoredDecision]
    consume_idempotency: dict[tuple[str, str, str], _StoredDecision]
    revoke_idempotency: dict[tuple[str, str], _StoredDecision]
    epochs: dict[tuple[str, str], int]
    sequences: dict[str, int]
    audit_events: tuple[AuditEvent, ...]


class InMemoryAuditSink:
    """Append-only metadata sink with deterministic failure injection for tests."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []
        self.fail_next = False

    def append(self, event: AuditEvent) -> None:
        if self.fail_next:
            self.fail_next = False
            raise RuntimeError("audit_append_failed")
        if (
            self._events
            and event.sequence <= self._events[-1].sequence
            and event.tenant_id == self._events[-1].tenant_id
        ):
            raise ValueError("audit_sequence_not_monotonic")
        if any(existing.event_id == event.event_id for existing in self._events):
            raise ValueError("audit_event_duplicate")
        self._events.append(event)

    def list_redacted(
        self,
        tenant_id: str,
        *,
        workspace_id: str | None = None,
    ) -> tuple[RedactedAuditEvent, ...]:
        if not valid_identifier(tenant_id):
            raise ValueError("tenant_invalid")
        if workspace_id is not None and not valid_identifier(workspace_id):
            raise ValueError("workspace_invalid")
        return tuple(
            redact_audit_event(event)
            for event in self._events
            if event.tenant_id == tenant_id
            and (workspace_id is None or event.workspace_id == workspace_id)
        )

    @property
    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(self._events)

    def _replace_events(self, events: tuple[AuditEvent, ...]) -> None:
        self._events = list(events)


class InMemoryAuthorizationAuthority:
    """Server-owned, tenant-scoped, serialized A4-v1 authority."""

    def __init__(
        self,
        audit_sink: InMemoryAuditSink | None = None,
        *,
        clock: Callable[[], int] | None = None,
    ) -> None:
        self.audit_sink = audit_sink or InMemoryAuditSink()
        self._clock = clock or (lambda: 0)
        self._lock = threading.RLock()
        self._grants: dict[tuple[str, str], AuthorizationGrant] = {}
        self._issue_idempotency: dict[tuple[str, str], _StoredDecision] = {}
        self._consume_idempotency: dict[tuple[str, str, str], _StoredDecision] = {}
        self._revoke_idempotency: dict[tuple[str, str], _StoredDecision] = {}
        self._epochs: dict[tuple[str, str], int] = {}
        self._sequences: dict[str, int] = {}

    def _now(self, now: int | None) -> int:
        value = self._clock() if now is None else now
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("clock_invalid")
        return value

    @staticmethod
    def _context_valid(context: ServerAuthorizationContext) -> bool:
        return (
            isinstance(context, ServerAuthorizationContext)
            and valid_identifier(context.tenant_id)
            and valid_identifier(context.workspace_id)
            and valid_identifier(context.actor_id)
        )

    @staticmethod
    def _scope_valid(scope: AuthorizationScope) -> bool:
        if not isinstance(scope, AuthorizationScope):
            return False
        if not all(
            valid_identifier(value)
            for value in (
                scope.tenant_id,
                scope.workspace_id,
                scope.agent_id,
                scope.agent_version,
                scope.paper_account_id,
                scope.account_mode,
                scope.connector_id,
                scope.venue_id,
                scope.source_kind,
                scope.source_id,
                scope.data_classification,
                scope.policy_version,
            )
        ):
            return False
        try:
            normalized = scope.normalized()
        except (TypeError, ValueError):
            return False
        return (
            valid_digest(scope.strategy_digest)
            and scope.account_mode == PAPER_MODE
            and scope.connector_id == PAPER_CONNECTOR
            and normalized.assets == scope.assets
        )

    @staticmethod
    def _decision(
        outcome: AuthorizationOutcome,
        reason: AuthorizationReason | None,
        *,
        decision_id: str,
        grant: AuthorizationGrant | None = None,
        policy_version: str | None = None,
        expires_at: int | None = None,
        status: AuthorizationStatus | None = None,
    ) -> AuthorizationDecision:
        return AuthorizationDecision(
            decision_id=decision_id,
            outcome=outcome,
            reason=reason,
            grant_id=grant.grant_id if grant else None,
            scope_digest=grant.scope_digest if grant else None,
            policy_version=(
                policy_version
                if policy_version is not None
                else (grant.policy_version if grant else None)
            ),
            expires_at=(
                expires_at if expires_at is not None else (grant.expires_at if grant else None)
            ),
            status=status if status is not None else (grant.status if grant else None),
        )

    @staticmethod
    def _audit_digest(payload: Mapping[str, object]) -> str:
        return digest_value(dict(payload))

    def _event(
        self,
        context: ServerAuthorizationContext,
        *,
        event_type: AuditEventType,
        occurred_at: int,
        request_digest: str,
        grant_id: str | None,
        scope_digest: str | None,
        policy_version: str | None,
        epoch: int,
        outcome: AuditOutcome,
        reason: AuthorizationReason | None,
        correlation_digest: str | None = None,
    ) -> AuditEvent:
        sequence = self._sequences.get(context.tenant_id, 0) + 1
        event_id = (
            "a4e-"
            + digest_value(
                {"tenant": context.tenant_id, "sequence": sequence, "request": request_digest}
            )[:32]
        )
        actor_digest = digest_value({"actor_id": context.actor_id})
        payload = {
            "event_id": event_id,
            "tenant_id": context.tenant_id,
            "workspace_id": context.workspace_id,
            "event_type": event_type.value,
            "event_version": 1,
            "occurred_at": occurred_at,
            "sequence": sequence,
            "actor_digest": actor_digest,
            "grant_id": grant_id,
            "request_digest": request_digest,
            "scope_digest": scope_digest,
            "policy_version": policy_version,
            "revocation_epoch": epoch,
            "outcome": outcome.value,
            "reason_code": reason.value if reason else None,
            "correlation_digest": correlation_digest,
        }
        event_digest = self._audit_digest(payload)
        return AuditEvent(
            event_id=event_id,
            tenant_id=context.tenant_id,
            workspace_id=context.workspace_id,
            event_type=event_type,
            event_version=1,
            occurred_at=occurred_at,
            sequence=sequence,
            actor_digest=actor_digest,
            grant_id=grant_id,
            request_digest=request_digest,
            scope_digest=scope_digest,
            policy_version=policy_version,
            revocation_epoch=epoch,
            outcome=outcome,
            reason_code=reason.value if reason else None,
            correlation_digest=correlation_digest,
            event_digest=event_digest,
        )

    def _append(
        self,
        context: ServerAuthorizationContext,
        **kwargs: object,
    ) -> AuditEvent:
        event = self._event(context, **kwargs)  # type: ignore[arg-type]
        self.audit_sink.append(event)
        self._sequences[context.tenant_id] = event.sequence
        return event

    def _rollback(
        self,
        grants: dict[tuple[str, str], AuthorizationGrant],
        issue: dict[tuple[str, str], _StoredDecision],
        consume: dict[tuple[str, str, str], _StoredDecision],
        revoke: dict[tuple[str, str], _StoredDecision],
        epochs: dict[tuple[str, str], int],
        sequences: dict[str, int],
    ) -> None:
        self._grants = grants
        self._issue_idempotency = issue
        self._consume_idempotency = consume
        self._revoke_idempotency = revoke
        self._epochs = epochs
        self._sequences = sequences

    def _snapshot(self) -> _RollbackSnapshot:
        return _RollbackSnapshot(
            grants=dict(self._grants),
            issue_idempotency=dict(self._issue_idempotency),
            consume_idempotency=dict(self._consume_idempotency),
            revoke_idempotency=dict(self._revoke_idempotency),
            epochs=dict(self._epochs),
            sequences=dict(self._sequences),
            audit_events=self.audit_sink.events,
        )

    def _restore(self, snapshot: _RollbackSnapshot) -> None:
        self._grants = dict(snapshot.grants)
        self._issue_idempotency = dict(snapshot.issue_idempotency)
        self._consume_idempotency = dict(snapshot.consume_idempotency)
        self._revoke_idempotency = dict(snapshot.revoke_idempotency)
        self._epochs = dict(snapshot.epochs)
        self._sequences = dict(snapshot.sequences)
        self.audit_sink._replace_events(snapshot.audit_events)

    def issue(
        self,
        server_context: ServerAuthorizationContext,
        intent: AuthorizationIntent,
        *,
        now: int | None = None,
    ) -> AuthorizationDecision:
        with self._lock:
            try:
                current = self._now(now)
            except ValueError:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if not self._context_valid(server_context) or not isinstance(
                intent, AuthorizationIntent
            ):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if (
                intent.authority_type is not server_context.authority_type
                or not self._scope_valid(intent.scope)
                or intent.scope.tenant_id != server_context.tenant_id
                or intent.scope.workspace_id != server_context.workspace_id
                or not valid_identifier(intent.idempotency_key)
                or not valid_digest(intent.request_digest)
                or intent.request_digest != intent.computed_request_digest()
                or not isinstance(intent.ttl_seconds, int)
                or isinstance(intent.ttl_seconds, bool)
                or not MIN_TTL_SECONDS <= intent.ttl_seconds <= MAX_TTL_SECONDS
            ):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            key = (server_context.tenant_id, intent.idempotency_key)
            existing = self._issue_idempotency.get(key)
            if existing is not None:
                if (
                    existing.request_digest == intent.request_digest
                    and existing.scope_digest == intent.scope.scope_digest()
                    and existing.policy_version == intent.scope.policy_version
                ):
                    return AuthorizationDecision(
                        decision_id=existing.decision.decision_id,
                        outcome=AuthorizationOutcome.REPLAYED,
                        reason=existing.decision.reason,
                        grant_id=existing.decision.grant_id,
                        scope_digest=existing.decision.scope_digest,
                        policy_version=existing.decision.policy_version,
                        expires_at=existing.decision.expires_at,
                        status=existing.decision.status,
                    )
                return self._decision(
                    AuthorizationOutcome.CONFLICT,
                    AuthorizationReason.IDEMPOTENCY_CONFLICT,
                    decision_id="a4d-conflict",
                )
            snapshot = self._snapshot()
            scope = intent.scope.normalized()
            scope_digest = scope.scope_digest()
            grant_id = (
                "a4g-"
                + digest_value(
                    {
                        "tenant": scope.tenant_id,
                        "scope": scope_digest,
                        "request": intent.request_digest,
                        "issued_at": current,
                    }
                )[:32]
            )
            nonce_digest = digest_value({"grant": grant_id, "request": intent.request_digest})
            epoch_key = (scope.tenant_id, scope.workspace_id)
            epoch = self._epochs.get(epoch_key, 0)
            grant = AuthorizationGrant(
                grant_id=grant_id,
                scope=scope,
                authority_subject_digest=digest_value({"actor": server_context.actor_id}),
                scope_digest=scope_digest,
                policy_version=scope.policy_version,
                issued_at=current,
                expires_at=current + intent.ttl_seconds,
                nonce_digest=nonce_digest,
                revocation_epoch=epoch,
            )
            decision = self._decision(
                AuthorizationOutcome.ACCEPTED,
                None,
                decision_id="a4d-" + digest_value({"grant": grant_id})[:32],
                grant=grant,
            )
            try:
                self._grants[(scope.tenant_id, grant_id)] = grant
                self._append(
                    server_context,
                    event_type=AuditEventType.AUTH_ISSUED,
                    occurred_at=current,
                    request_digest=intent.request_digest,
                    grant_id=grant_id,
                    scope_digest=scope_digest,
                    policy_version=scope.policy_version,
                    epoch=epoch,
                    outcome=AuditOutcome.ACCEPTED,
                    reason=None,
                )
                self._issue_idempotency[key] = _StoredDecision(
                    intent.request_digest, scope_digest, scope.policy_version, decision
                )
                return decision
            except Exception:
                self._restore(snapshot)
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.AUDIT_WRITE_FAILED,
                    decision_id="a4d-audit-failed",
                )

    def consume(
        self,
        server_context: ServerAuthorizationContext,
        request: ConsumeRequest,
        *,
        now: int | None = None,
    ) -> AuthorizationDecision:
        with self._lock:
            try:
                current = self._now(now)
            except ValueError:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if not self._context_valid(server_context) or not isinstance(request, ConsumeRequest):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if not all(
                (
                    valid_identifier(request.grant_id),
                    valid_digest(request.scope_digest),
                    valid_identifier(request.policy_version),
                    valid_identifier(request.idempotency_key),
                    valid_digest(request.request_digest),
                )
            ):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if request.request_digest != request.computed_request_digest():
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            key = (server_context.tenant_id, request.grant_id, request.idempotency_key)
            existing = self._consume_idempotency.get(key)
            if existing is not None:
                if (
                    existing.request_digest == request.request_digest
                    and existing.scope_digest == request.scope_digest
                    and existing.policy_version == request.policy_version
                ):
                    return AuthorizationDecision(
                        decision_id=existing.decision.decision_id,
                        outcome=AuthorizationOutcome.REPLAYED,
                        reason=existing.decision.reason,
                        grant_id=existing.decision.grant_id,
                        scope_digest=existing.decision.scope_digest,
                        policy_version=existing.decision.policy_version,
                        expires_at=existing.decision.expires_at,
                        status=existing.decision.status,
                    )
                return self._decision(
                    AuthorizationOutcome.CONFLICT,
                    AuthorizationReason.IDEMPOTENCY_CONFLICT,
                    decision_id="a4d-conflict",
                )
            grant = self._grants.get((server_context.tenant_id, request.grant_id))
            if grant is None:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.TENANT_SCOPE_DENIED,
                    decision_id="a4d-denied",
                )
            if grant.scope.workspace_id != server_context.workspace_id:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.TENANT_SCOPE_DENIED,
                    decision_id="a4d-denied",
                )
            if grant.status is AuthorizationStatus.ACTIVE and current >= grant.expires_at:
                snapshot = self._snapshot()
                expired = AuthorizationGrant(
                    **{**grant.__dict__, "status": AuthorizationStatus.EXPIRED}
                )
                try:
                    self._grants[(server_context.tenant_id, grant.grant_id)] = expired
                    self._append(
                        server_context,
                        event_type=AuditEventType.AUTH_EXPIRED,
                        occurred_at=current,
                        request_digest=request.request_digest,
                        grant_id=grant.grant_id,
                        scope_digest=grant.scope_digest,
                        policy_version=grant.policy_version,
                        epoch=grant.revocation_epoch,
                        outcome=AuditOutcome.EXPIRED,
                        reason=AuthorizationReason.EXPIRED,
                    )
                except Exception:
                    self._restore(snapshot)
                    return self._decision(
                        AuthorizationOutcome.DENIED,
                        AuthorizationReason.AUDIT_WRITE_FAILED,
                        decision_id="a4d-audit-failed",
                    )
                grant = expired
            reason = None
            if (
                grant.scope_digest != request.scope_digest
                or grant.policy_version != request.policy_version
            ):
                reason = (
                    AuthorizationReason.SCOPE_MISMATCH
                    if grant.scope_digest != request.scope_digest
                    else AuthorizationReason.POLICY_MISMATCH
                )
            elif grant.status is AuthorizationStatus.EXPIRED:
                reason = AuthorizationReason.EXPIRED
            elif grant.status is AuthorizationStatus.REVOKED:
                reason = AuthorizationReason.REVOKED
            elif grant.status is AuthorizationStatus.CONSUMED:
                reason = AuthorizationReason.ALREADY_CONSUMED
            elif (
                self._epochs.get((grant.scope.tenant_id, grant.scope.workspace_id), 0)
                != grant.revocation_epoch
            ):
                reason = AuthorizationReason.REVOKED
            if reason is not None:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    reason,
                    decision_id="a4d-denied",
                    grant=grant,
                    status=grant.status,
                )
            snapshot = self._snapshot()
            consumed = AuthorizationGrant(
                **{**grant.__dict__, "status": AuthorizationStatus.CONSUMED}
            )
            decision = self._decision(
                AuthorizationOutcome.ACCEPTED,
                None,
                decision_id="a4d-"
                + digest_value({"grant": grant.grant_id, "request": request.request_digest})[:32],
                grant=consumed,
            )
            try:
                self._grants[(server_context.tenant_id, grant.grant_id)] = consumed
                self._append(
                    server_context,
                    event_type=AuditEventType.AUTH_CONSUME_ACCEPTED,
                    occurred_at=current,
                    request_digest=request.request_digest,
                    grant_id=grant.grant_id,
                    scope_digest=grant.scope_digest,
                    policy_version=grant.policy_version,
                    epoch=grant.revocation_epoch,
                    outcome=AuditOutcome.ACCEPTED,
                    reason=None,
                )
                self._consume_idempotency[key] = _StoredDecision(
                    request.request_digest, request.scope_digest, request.policy_version, decision
                )
                return decision
            except Exception:
                self._restore(snapshot)
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.AUDIT_WRITE_FAILED,
                    decision_id="a4d-audit-failed",
                )

    def revoke(
        self,
        server_context: ServerAuthorizationContext,
        request: RevocationRequest,
        *,
        now: int | None = None,
    ) -> AuthorizationDecision:
        with self._lock:
            try:
                current = self._now(now)
            except ValueError:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if not self._context_valid(server_context) or not isinstance(
                request, RevocationRequest
            ):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            if (
                not valid_identifier(request.grant_id)
                or not valid_identifier(request.idempotency_key)
                or not valid_digest(request.request_digest)
                or request.request_digest != request.computed_request_digest()
            ):
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.INVALID_REQUEST,
                    decision_id="a4d-invalid",
                )
            key = (server_context.tenant_id, request.idempotency_key)
            existing = self._revoke_idempotency.get(key)
            if existing is not None:
                if existing.request_digest == request.request_digest:
                    return AuthorizationDecision(
                        **{**existing.decision.__dict__, "outcome": AuthorizationOutcome.REPLAYED}
                    )
                return self._decision(
                    AuthorizationOutcome.CONFLICT,
                    AuthorizationReason.IDEMPOTENCY_CONFLICT,
                    decision_id="a4d-conflict",
                )
            grant = self._grants.get((server_context.tenant_id, request.grant_id))
            if grant is None or grant.scope.workspace_id != server_context.workspace_id:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.TENANT_SCOPE_DENIED,
                    decision_id="a4d-denied",
                )
            if grant.status is not AuthorizationStatus.ACTIVE:
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    (
                        AuthorizationReason.ALREADY_CONSUMED
                        if grant.status is AuthorizationStatus.CONSUMED
                        else (
                            AuthorizationReason.REVOKED
                            if grant.status is AuthorizationStatus.REVOKED
                            else AuthorizationReason.EXPIRED
                        )
                    ),
                    decision_id="a4d-denied",
                    grant=grant,
                    status=grant.status,
                )
            snapshot = self._snapshot()
            epoch_key = (grant.scope.tenant_id, grant.scope.workspace_id)
            epoch = self._epochs.get(epoch_key, 0) + 1
            revoked = AuthorizationGrant(
                **{**grant.__dict__, "status": AuthorizationStatus.REVOKED}
            )
            decision = self._decision(
                AuthorizationOutcome.ACCEPTED,
                None,
                decision_id="a4d-"
                + digest_value({"grant": grant.grant_id, "revoke": request.request_digest})[:32],
                grant=revoked,
            )
            try:
                self._epochs[epoch_key] = epoch
                self._grants[(server_context.tenant_id, grant.grant_id)] = revoked
                self._append(
                    server_context,
                    event_type=AuditEventType.AUTH_REVOKED,
                    occurred_at=current,
                    request_digest=request.request_digest,
                    grant_id=grant.grant_id,
                    scope_digest=grant.scope_digest,
                    policy_version=grant.policy_version,
                    epoch=epoch,
                    outcome=AuditOutcome.REVOKED,
                    reason=request.reason,
                )
                self._revoke_idempotency[key] = _StoredDecision(
                    request.request_digest, grant.scope_digest, grant.policy_version, decision
                )
                return decision
            except Exception:
                self._restore(snapshot)
                return self._decision(
                    AuthorizationOutcome.DENIED,
                    AuthorizationReason.AUDIT_WRITE_FAILED,
                    decision_id="a4d-audit-failed",
                )

    def inspect(
        self,
        server_context: ServerAuthorizationContext,
        grant_id: str,
        *,
        now: int | None = None,
    ) -> RedactedAuthorizationView | None:
        with self._lock:
            current = self._now(now)
            if not self._context_valid(server_context) or not valid_identifier(grant_id):
                return None
            grant = self._grants.get((server_context.tenant_id, grant_id))
            if grant is None or grant.scope.workspace_id != server_context.workspace_id:
                return None
            if grant.status is AuthorizationStatus.ACTIVE and current >= grant.expires_at:
                snapshot = self._snapshot()
                expired = AuthorizationGrant(
                    **{**grant.__dict__, "status": AuthorizationStatus.EXPIRED}
                )
                try:
                    self._grants[(server_context.tenant_id, grant.grant_id)] = expired
                    self._append(
                        server_context,
                        event_type=AuditEventType.AUTH_EXPIRED,
                        occurred_at=current,
                        request_digest=digest_value({"inspect": grant_id}),
                        grant_id=grant.grant_id,
                        scope_digest=grant.scope_digest,
                        policy_version=grant.policy_version,
                        epoch=grant.revocation_epoch,
                        outcome=AuditOutcome.EXPIRED,
                        reason=AuthorizationReason.EXPIRED,
                    )
                    grant = expired
                except Exception:
                    self._restore(snapshot)
                    return None
            return RedactedAuthorizationView(
                grant.grant_id,
                grant.scope_digest,
                grant.policy_version,
                grant.status,
                grant.issued_at,
                grant.expires_at,
                grant.revocation_epoch,
            )
