"""Protocol-only A4-v1 authority and audit interfaces."""

from __future__ import annotations

from typing import Protocol

from .audit_contracts import AuditEvent, RedactedAuditEvent
from .authorization_contracts import (
    AuthorizationDecision,
    AuthorizationIntent,
    ConsumeRequest,
    RedactedAuthorizationView,
    RevocationRequest,
    ServerAuthorizationContext,
)


class HumanAuthorizationAuthority(Protocol):
    def issue(
        self,
        server_context: ServerAuthorizationContext,
        intent: AuthorizationIntent,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def consume(
        self,
        server_context: ServerAuthorizationContext,
        request: ConsumeRequest,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def revoke(
        self,
        server_context: ServerAuthorizationContext,
        request: RevocationRequest,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def inspect(
        self,
        server_context: ServerAuthorizationContext,
        grant_id: str,
        *,
        now: int,
    ) -> RedactedAuthorizationView | None: ...


class AppendOnlyAuditSink(Protocol):
    def append(self, event: AuditEvent) -> None: ...

    def list_redacted(
        self,
        tenant_id: str,
        *,
        workspace_id: str | None = None,
    ) -> tuple[RedactedAuditEvent, ...]: ...
