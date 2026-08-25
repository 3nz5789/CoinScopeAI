"""A4-v1 immutable authorization contracts.

This module is metadata-only. It contains no persistence, network, runtime,
recording, material, scanner, replay, execution, or external capability.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
import re
from typing import Final

MAX_TTL_SECONDS: Final[int] = 600
MIN_TTL_SECONDS: Final[int] = 1
PAPER_MODE: Final[str] = "paper"
PAPER_CONNECTOR: Final[str] = "paper"
_IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}$")
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


class AuthorityType(str, Enum):
    WORKSPACE_OWNER = "WORKSPACE_OWNER"
    TRADING_RISK_REVIEWER = "TRADING_RISK_REVIEWER"
    DATA_REVIEWER = "DATA_REVIEWER"


class AuthorizationStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CONSUMED = "CONSUMED"
    REVOKED = "REVOKED"
    EXPIRED = "EXPIRED"


class AuthorizationOutcome(str, Enum):
    ACCEPTED = "ACCEPTED"
    DENIED = "DENIED"
    REPLAYED = "REPLAYED"
    CONFLICT = "CONFLICT"


class AuthorizationReason(str, Enum):
    INVALID_REQUEST = "INVALID_REQUEST"
    TENANT_SCOPE_DENIED = "TENANT_SCOPE_DENIED"
    AUTHORITY_DENIED = "AUTHORITY_DENIED"
    POLICY_MISMATCH = "POLICY_MISMATCH"
    SCOPE_MISMATCH = "SCOPE_MISMATCH"
    NOT_YET_VALID = "NOT_YET_VALID"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    ALREADY_CONSUMED = "ALREADY_CONSUMED"
    IDEMPOTENCY_CONFLICT = "IDEMPOTENCY_CONFLICT"
    AUTHORITY_UNAVAILABLE = "AUTHORITY_UNAVAILABLE"
    AUDIT_WRITE_FAILED = "AUDIT_WRITE_FAILED"


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
        "utf-8", "strict"
    )


def digest_value(value: object) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def valid_identifier(value: object) -> bool:
    return isinstance(value, str) and _IDENTIFIER.fullmatch(value) is not None


def valid_digest(value: object) -> bool:
    return isinstance(value, str) and _DIGEST.fullmatch(value) is not None


def normalize_assets(assets: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    if not isinstance(assets, (tuple, list)) or not assets:
        raise ValueError("invalid_assets")
    if any(type(asset) is not str or not asset for asset in assets):
        raise ValueError("invalid_assets")
    normalized = tuple(sorted(asset.upper() for asset in assets))
    if len(set(normalized)) != len(normalized) or any(
        not valid_identifier(asset) or "*" in asset or "?" in asset for asset in normalized
    ):
        raise ValueError("invalid_assets")
    return normalized


@dataclass(frozen=True)
class ServerAuthorizationContext:
    tenant_id: str
    workspace_id: str
    actor_id: str
    authority_type: AuthorityType

    def to_dict(self) -> dict[str, object]:
        return {
            "tenant_id": self.tenant_id,
            "workspace_id": self.workspace_id,
            "actor_id": self.actor_id,
            "authority_type": self.authority_type.value,
        }


@dataclass(frozen=True)
class AuthorizationScope:
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

    def normalized(self) -> "AuthorizationScope":
        return AuthorizationScope(
            self.tenant_id,
            self.workspace_id,
            self.agent_id,
            self.agent_version,
            self.strategy_digest,
            self.paper_account_id,
            self.account_mode,
            self.connector_id,
            self.venue_id,
            normalize_assets(self.assets),
            self.source_kind,
            self.source_id,
            self.data_classification,
            self.policy_version,
        )

    def to_dict(self) -> dict[str, object]:
        value = self.normalized()
        return {
            "account_mode": value.account_mode,
            "agent_id": value.agent_id,
            "agent_version": value.agent_version,
            "assets": value.assets,
            "connector_id": value.connector_id,
            "data_classification": value.data_classification,
            "paper_account_id": value.paper_account_id,
            "policy_version": value.policy_version,
            "source_id": value.source_id,
            "source_kind": value.source_kind,
            "strategy_digest": value.strategy_digest,
            "tenant_id": value.tenant_id,
            "venue_id": value.venue_id,
            "workspace_id": value.workspace_id,
        }

    def scope_digest(self) -> str:
        return digest_value(self.to_dict())


@dataclass(frozen=True)
class AuthorizationIntent:
    scope: AuthorizationScope
    authority_type: AuthorityType
    idempotency_key: str
    request_digest: str
    ttl_seconds: int
    requested_at: int

    def request_payload(self) -> dict[str, object]:
        return {
            "authority_type": self.authority_type.value,
            "idempotency_key": self.idempotency_key,
            "scope": self.scope.to_dict(),
            "ttl_seconds": self.ttl_seconds,
            "requested_at": self.requested_at,
        }

    def computed_request_digest(self) -> str:
        return digest_value(self.request_payload())


@dataclass(frozen=True)
class AuthorizationGrant:
    grant_id: str
    scope: AuthorizationScope
    authority_subject_digest: str
    scope_digest: str
    policy_version: str
    issued_at: int
    expires_at: int
    nonce_digest: str
    revocation_epoch: int
    status: AuthorizationStatus = AuthorizationStatus.ACTIVE


@dataclass(frozen=True)
class AuthorizationDecision:
    decision_id: str
    outcome: AuthorizationOutcome
    reason: AuthorizationReason | None
    grant_id: str | None
    scope_digest: str | None
    policy_version: str | None
    expires_at: int | None
    status: AuthorizationStatus | None
    recheck_required: bool = True

    def to_dict(self) -> dict[str, object]:
        return {
            "decision_id": self.decision_id,
            "outcome": self.outcome.value,
            "reason": self.reason.value if self.reason else None,
            "grant_id": self.grant_id,
            "scope_digest": self.scope_digest,
            "policy_version": self.policy_version,
            "expires_at": self.expires_at,
            "status": self.status.value if self.status else None,
            "recheck_required": True,
        }


@dataclass(frozen=True)
class ConsumeRequest:
    grant_id: str
    scope_digest: str
    policy_version: str
    idempotency_key: str
    request_digest: str

    def request_payload(self) -> dict[str, object]:
        return {
            "grant_id": self.grant_id,
            "idempotency_key": self.idempotency_key,
            "policy_version": self.policy_version,
            "scope_digest": self.scope_digest,
        }

    def computed_request_digest(self) -> str:
        return digest_value(self.request_payload())


@dataclass(frozen=True)
class RevocationRequest:
    grant_id: str
    reason: AuthorizationReason
    idempotency_key: str
    request_digest: str

    def request_payload(self) -> dict[str, object]:
        return {
            "grant_id": self.grant_id,
            "idempotency_key": self.idempotency_key,
            "reason": self.reason.value,
        }

    def computed_request_digest(self) -> str:
        return digest_value(self.request_payload())


@dataclass(frozen=True)
class RedactedAuthorizationView:
    grant_id: str
    scope_digest: str
    policy_version: str
    status: AuthorizationStatus
    issued_at: int
    expires_at: int
    revocation_epoch: int

    def to_dict(self) -> dict[str, object]:
        return {
            "grant_id": self.grant_id,
            "scope_digest": self.scope_digest,
            "policy_version": self.policy_version,
            "status": self.status.value,
            "issued_at": self.issued_at,
            "expires_at": self.expires_at,
            "revocation_epoch": self.revocation_epoch,
        }
