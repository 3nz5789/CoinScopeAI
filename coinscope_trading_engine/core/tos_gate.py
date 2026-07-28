"""
tos_gate.py — Terms of Service Signed Acceptance Gate
COI-60 | P1.5 | CoinScopeAI

FastAPI middleware and dependency that refuses API access to users
who have not accepted the current Terms of Service version.

Every paying tier requires ToS acceptance before the first API call.
Free tier requires ToS acceptance at signup.

ToS version is pinned in config — bump the version string to force
re-acceptance on next request.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer

# Current ToS version — bump to force re-acceptance
TOS_CURRENT_VERSION = "1.0"
TOS_URL = "https://coinscope.ai/legal/tos"


# ── Database schema (DDL) ─────────────────────────────────────────────────────

TOS_ACCEPTANCES_DDL = """
CREATE TABLE IF NOT EXISTS tos_acceptances (
    id              BIGSERIAL PRIMARY KEY,
    user_id         TEXT NOT NULL,
    tos_version     TEXT NOT NULL,
    accepted_at     TIMESTAMPTZ DEFAULT NOW(),
    ip_address      TEXT,
    user_agent      TEXT,

    CONSTRAINT uq_user_tos_version UNIQUE (user_id, tos_version)
);

CREATE INDEX IF NOT EXISTS idx_tos_user_id ON tos_acceptances(user_id);
"""


# ── ToS gate dependency ───────────────────────────────────────────────────────

class ToSGate:
    """
    FastAPI dependency that enforces ToS acceptance.

    Add to any endpoint that requires acceptance:

        @router.get("/scan")
        async def scan(user=Depends(tos_gate)):
            ...

    If the user has not accepted the current ToS version,
    returns HTTP 403 with a link to the acceptance endpoint.
    """

    def __init__(self, db_session_factory):
        self.db_session_factory = db_session_factory

    def __call__(self, request: Request):
        user_id = self._get_user_id(request)
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required",
            )

        with self.db_session_factory() as db:
            if not self._has_accepted(db, user_id):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail={
                        "error": "tos_not_accepted",
                        "message": (
                            f"You must accept Terms of Service v{TOS_CURRENT_VERSION} "
                            f"before using the API."
                        ),
                        "tos_url": TOS_URL,
                        "acceptance_endpoint": "/auth/tos/accept",
                        "current_version": TOS_CURRENT_VERSION,
                    },
                )
        return user_id

    def _get_user_id(self, request: Request) -> Optional[str]:
        """Extract user_id from request state (set by auth middleware)."""
        return getattr(request.state, "user_id", None)

    def _has_accepted(self, db, user_id: str) -> bool:
        """Check if user has accepted the current ToS version."""
        row = db.execute(
            """
            SELECT 1 FROM tos_acceptances
            WHERE user_id = :user_id AND tos_version = :version
            """,
            {"user_id": user_id, "version": TOS_CURRENT_VERSION},
        ).fetchone()
        return row is not None


class ToSAcceptanceService:
    """Service for recording ToS acceptances."""

    def __init__(self, db_session):
        self.db = db_session

    def record_acceptance(
        self,
        user_id: str,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> dict:
        """
        Record that a user has accepted the current ToS version.
        Idempotent — safe to call multiple times.
        """
        self.db.execute(
            """
            INSERT INTO tos_acceptances (user_id, tos_version, ip_address, user_agent)
            VALUES (:user_id, :version, :ip, :ua)
            ON CONFLICT (user_id, tos_version) DO NOTHING
            """,
            {
                "user_id": user_id,
                "version": TOS_CURRENT_VERSION,
                "ip": ip_address,
                "ua": user_agent,
            },
        )
        self.db.commit()

        return {
            "accepted": True,
            "tos_version": TOS_CURRENT_VERSION,
            "accepted_at": datetime.now(timezone.utc).isoformat(),
        }

    def acceptance_status(self, user_id: str) -> dict:
        """Return current acceptance status for a user."""
        row = self.db.execute(
            """
            SELECT tos_version, accepted_at
            FROM tos_acceptances
            WHERE user_id = :user_id AND tos_version = :version
            """,
            {"user_id": user_id, "version": TOS_CURRENT_VERSION},
        ).fetchone()

        if row:
            return {
                "accepted": True,
                "tos_version": row[0],
                "accepted_at": row[1].isoformat() if row[1] else None,
                "current_version": TOS_CURRENT_VERSION,
            }
        return {
            "accepted": False,
            "current_version": TOS_CURRENT_VERSION,
            "tos_url": TOS_URL,
        }
