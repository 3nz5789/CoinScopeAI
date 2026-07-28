"""
CoinScopeAI Billing Module
Stripe webhook handler, subscription state, and billing notifications.

Stores
──────
  SubscriptionStore      — SQLite-backed (sync), kept for local dev / tests
  PgSubscriptionStore    — asyncpg-backed (async), used in production (VPS)

Entitlements
────────────
  Entitlements           — frozen dataclass, one per customer
  TIER_ENTITLEMENTS      — static lookup dict (mirrors DB seed)
  tier_rank / is_upgrade / is_downgrade — comparison helpers
"""

from .entitlements import (
    TIER_ENTITLEMENTS,
    Entitlements,
    is_downgrade,
    is_upgrade,
    tier_rank,
)
from .models import (
    BillingInterval,
    CheckoutSessionData,
    InvoiceData,
    SubscriptionChangeData,
    SubscriptionRecord,
    SubscriptionStatus,
    SubscriptionTier,
    WebhookEventRecord,
)
from .pg_subscription_store import PgSubscriptionStore
from .subscription_store import SubscriptionStore

__all__ = [
    # Models
    "SubscriptionTier",
    "SubscriptionStatus",
    "BillingInterval",
    "SubscriptionRecord",
    "WebhookEventRecord",
    "CheckoutSessionData",
    "SubscriptionChangeData",
    "InvoiceData",
    # Stores
    "SubscriptionStore",
    "PgSubscriptionStore",
    # Entitlements
    "Entitlements",
    "TIER_ENTITLEMENTS",
    "tier_rank",
    "is_upgrade",
    "is_downgrade",
]
