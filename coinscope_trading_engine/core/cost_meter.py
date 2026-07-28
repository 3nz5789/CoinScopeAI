"""
cost_meter.py — Per-User API Usage Tracking & Tier Ceiling Enforcement
COI-62 | P1.5 | CoinScopeAI

Tracks per-user API consumption (Claude, CoinGlass, Tradefeeds, CoinGecko)
and enforces tier-based ceilings to protect margins.

Without per-user cost tracking, unit economics drift silently.
Margins die one chatty user at a time.

Tier ceilings (monthly, approximate cost):
  Free:         $0 / mo vendor cost cap
  Trader:       $8 / mo (10% of $79 tier price — safe margin floor)
  Desk Preview: $40 / mo (10% of $399)
  Desk Full v2: $120 / mo (10% of $1,199 base)

These are soft ceilings — enforce via throttle, not hard block, to avoid
disrupting paying users. Alert operator when approaching ceiling.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Vendor(str, Enum):
    CLAUDE = "claude"
    COINGLASS = "coinglass"
    TRADEFEEDS = "tradefeeds"
    COINGECKO = "coingecko"
    BINANCE = "binance"      # free tier — track for observability, no ceiling


class Tier(str, Enum):
    FREE = "free"
    TRADER = "trader"
    DESK_PREVIEW = "desk_preview"
    DESK_FULL = "desk_full"


# Monthly soft ceilings per tier (USD cents)
TIER_MONTHLY_CEILING_CENTS: dict[Tier, int] = {
    Tier.FREE: 0,
    Tier.TRADER: 800,          # $8.00
    Tier.DESK_PREVIEW: 4000,   # $40.00
    Tier.DESK_FULL: 12000,     # $120.00
}

# Approximate cost per API call (USD cents)
VENDOR_COST_PER_CALL_CENTS: dict[Vendor, float] = {
    Vendor.CLAUDE: 0.5,        # ~$0.005 per call (Sonnet, ~1k tokens avg)
    Vendor.COINGLASS: 0.1,     # ~$0.001 per call (Pro tier, spread across calls)
    Vendor.TRADEFEEDS: 0.2,    # ~$0.002 per call
    Vendor.COINGECKO: 0.0,     # free tier — no cost
    Vendor.BINANCE: 0.0,       # free — track volume only
}


# ── Database schema (DDL) ─────────────────────────────────────────────────────

USAGE_EVENTS_DDL = """
CREATE TABLE IF NOT EXISTS usage_events (
    id              BIGSERIAL PRIMARY KEY,
    user_id         TEXT NOT NULL,
    vendor          TEXT NOT NULL,
    endpoint        TEXT NOT NULL,
    units           INTEGER NOT NULL DEFAULT 1,    -- API calls
    cost_usd_cents  INTEGER NOT NULL DEFAULT 0,    -- rounded to nearest cent
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_usage_events_user_id ON usage_events(user_id);
CREATE INDEX IF NOT EXISTS idx_usage_events_vendor  ON usage_events(vendor);
CREATE INDEX IF NOT EXISTS idx_usage_events_created ON usage_events(created_at);
"""


# ── Cost meter ─────────────────────────────────────────────────────────────────

@dataclass
class UsageEvent:
    user_id: str
    vendor: Vendor
    endpoint: str
    units: int = 1
    cost_usd_cents: int = field(init=False)

    def __post_init__(self):
        self.cost_usd_cents = round(
            self.units * VENDOR_COST_PER_CALL_CENTS.get(self.vendor, 0)
        )


class CostMeter:
    """
    Per-user API cost tracker and tier ceiling enforcer.

    Usage (wrap every vendor call):
        meter = CostMeter(db_session)
        if meter.check_ceiling(user_id="usr_123", tier=Tier.TRADER):
            result = call_claude_api(...)
            meter.record(UsageEvent(user_id="usr_123", vendor=Vendor.CLAUDE,
                                    endpoint="/v1/messages"))
        else:
            raise TierCeilingExceeded("Monthly Claude budget reached")
    """

    def __init__(self, db_session):
        self.db = db_session

    def record(self, event: UsageEvent) -> None:
        """Record a vendor API call for a user."""
        self.db.execute(
            """
            INSERT INTO usage_events (user_id, vendor, endpoint, units, cost_usd_cents)
            VALUES (:user_id, :vendor, :endpoint, :units, :cost_cents)
            """,
            {
                "user_id": event.user_id,
                "vendor": event.vendor.value,
                "endpoint": event.endpoint,
                "units": event.units,
                "cost_cents": event.cost_usd_cents,
            },
        )
        self.db.commit()

    def monthly_spend_cents(self, user_id: str) -> int:
        """Total vendor cost (USD cents) for the current calendar month."""
        row = self.db.execute(
            """
            SELECT COALESCE(SUM(cost_usd_cents), 0)
            FROM usage_events
            WHERE user_id = :user_id
              AND created_at >= date_trunc('month', NOW())
            """,
            {"user_id": user_id},
        ).fetchone()
        return int(row[0]) if row else 0

    def check_ceiling(self, user_id: str, tier: Tier) -> bool:
        """
        Returns True if user is below their tier ceiling.
        Returns False if ceiling is reached — caller should throttle.

        Free tier always returns False (no API calls allowed that cost money).
        """
        ceiling = TIER_MONTHLY_CEILING_CENTS.get(tier, 0)
        if ceiling == 0:
            return False
        spend = self.monthly_spend_cents(user_id)
        return spend < ceiling

    def approaching_ceiling(self, user_id: str, tier: Tier, threshold: float = 0.8) -> bool:
        """Returns True if user has consumed >= threshold (default 80%) of ceiling."""
        ceiling = TIER_MONTHLY_CEILING_CENTS.get(tier, 0)
        if ceiling == 0:
            return False
        spend = self.monthly_spend_cents(user_id)
        return (spend / ceiling) >= threshold

    def usage_summary(self, user_id: str, tier: Tier) -> dict:
        """Return usage summary for display in dashboard / alerts."""
        ceiling = TIER_MONTHLY_CEILING_CENTS.get(tier, 0)
        spend = self.monthly_spend_cents(user_id)

        rows = self.db.execute(
            """
            SELECT vendor, COUNT(*) as calls, SUM(cost_usd_cents) as cost
            FROM usage_events
            WHERE user_id = :user_id
              AND created_at >= date_trunc('month', NOW())
            GROUP BY vendor
            ORDER BY cost DESC
            """,
            {"user_id": user_id},
        ).fetchall()

        return {
            "user_id": user_id,
            "tier": tier.value,
            "monthly_spend_cents": spend,
            "monthly_ceiling_cents": ceiling,
            "pct_used": round(spend / ceiling * 100, 1) if ceiling > 0 else None,
            "approaching_ceiling": self.approaching_ceiling(user_id, tier),
            "by_vendor": [
                {"vendor": r[0], "calls": r[1], "cost_cents": r[2]}
                for r in rows
            ],
        }


class TierCeilingExceeded(Exception):
    """Raised when a user has consumed their monthly vendor budget."""
    pass
