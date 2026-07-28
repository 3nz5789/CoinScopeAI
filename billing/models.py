"""
Billing Models — Pydantic schemas for subscription state and webhook events.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict

try:
    import email_validator  # noqa: F401  # force runtime availability check
    from pydantic import EmailStr
except ImportError:
    EmailStr = str  # type: ignore


class SubscriptionTier(str, Enum):
    FREE = "free"
    TRADER = "trader"
    DESK_PREVIEW = "desk_preview"
    DESK_FULL = "desk_full"
    UNKNOWN = "unknown"


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    PAST_DUE = "past_due"
    CANCELED = "canceled"
    TRIALING = "trialing"
    INCOMPLETE = "incomplete"
    UNPAID = "unpaid"


class BillingInterval(str, Enum):
    MONTHLY = "month"
    ANNUAL = "year"


class SubscriptionRecord(BaseModel):
    """Full subscription state stored in DB."""
    customer_id: str
    email: Optional[str] = None
    stripe_subscription_id: str
    tier: SubscriptionTier
    status: SubscriptionStatus
    interval: BillingInterval
    current_period_end: Optional[datetime] = None
    cancel_at_period_end: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(use_enum_values=True)


class WebhookEventRecord(BaseModel):
    """Idempotency record for processed webhook events."""
    event_id: str            # Stripe event ID (evt_xxx)
    event_type: str
    processed_at: datetime
    customer_id: Optional[str] = None
    subscription_id: Optional[str] = None


class CheckoutSessionData(BaseModel):
    """Extracted data from checkout.session.completed."""
    session_id: str
    customer_id: str
    subscription_id: str
    email: Optional[str] = None
    tier: SubscriptionTier
    interval: BillingInterval


class SubscriptionChangeData(BaseModel):
    """Data extracted from subscription update/delete events."""
    subscription_id: str
    customer_id: str
    tier: SubscriptionTier
    status: SubscriptionStatus
    interval: BillingInterval
    current_period_end: Optional[datetime] = None
    cancel_at_period_end: bool = False


class InvoiceData(BaseModel):
    """Data extracted from invoice events."""
    invoice_id: str
    customer_id: str
    subscription_id: Optional[str] = None
    amount_paid: int       # In cents
    currency: str
    status: str            # 'paid' | 'open' | 'uncollectible'
    next_payment_attempt: Optional[datetime] = None


# ---------------------------------------------------------------------------
# API request/response schemas (used by billing.stripe_gateway)
# ---------------------------------------------------------------------------

class CheckoutRequest(BaseModel):
    tier:             SubscriptionTier
    customer_email:   EmailStr  # type: ignore[valid-type]
    customer_name:    Optional[str] = None
    cycle:            Optional[str] = "monthly"   # "monthly" | "annual"
    success_url:      Optional[str] = None
    cancel_url:       Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "tier": "trader",
                "customer_email": "trader@example.com",
                "customer_name": "Mohammed A.",
                "cycle": "monthly",
            }
        }


class PortalRequest(BaseModel):
    customer_email: EmailStr  # type: ignore[valid-type]

    class Config:
        json_schema_extra = {
            "example": {"customer_email": "trader@example.com"}
        }


class CheckoutResponse(BaseModel):
    checkout_url: str
    session_id:   str


class PortalResponse(BaseModel):
    portal_url: str


class SubscriptionInfo(BaseModel):
    status:              SubscriptionStatus
    tier:                Optional[SubscriptionTier] = None
    customer_id:         Optional[str]      = None
    subscription_id:     Optional[str]      = None
    current_period_end:  Optional[int]      = None   # Unix timestamp
    cancel_at_period_end: bool              = False


class WebhookResponse(BaseModel):
    received: bool = True


# ---------------------------------------------------------------------------
# Plan catalogue (used by the dashboard billing endpoints)
# ---------------------------------------------------------------------------

class PlanInfo(BaseModel):
    tier:        SubscriptionTier
    name:        str
    price_usd:   float
    description: str
    features:    list[str]
    price_id:    str = ""              # filled at runtime from settings


PLAN_CATALOGUE: list[PlanInfo] = [
    PlanInfo(
        tier        = SubscriptionTier.FREE,
        name        = "Free",
        price_usd   = 0.0,
        description = "Try CoinScopeAI with a limited scanner and basic alerts.",
        features    = [
            "3 trading pairs",
            "4h scan interval",
            "5 alerts per day",
            "Telegram alerts",
            "7-day trade journal",
            "Basic risk gate",
        ],
    ),
    PlanInfo(
        tier        = SubscriptionTier.TRADER,
        name        = "Trader",
        price_usd   = 79.0,
        description = "For active individual traders who want full signal coverage.",
        features    = [
            "25 trading pairs",
            "1h scan interval",
            "50 alerts per day",
            "ML regime detection v3",
            "Telegram + email alerts",
            "Unlimited trade journal",
            "Backtesting engine",
            "Kelly position sizing",
            "Walk-forward validation",
        ],
    ),
    PlanInfo(
        tier        = SubscriptionTier.DESK_PREVIEW,
        name        = "Desk Preview",
        price_usd   = 399.0,
        description = "For prop desks ready to preview the full multi-exchange engine.",
        features    = [
            "Unlimited trading pairs",
            "15min scan interval",
            "Unlimited alerts",
            "V3 LightGBM ML signals",
            "API key access (REST)",
            "Multi-exchange coverage",
            "CVD + whale flow signals",
            "TradingView webhooks",
            "Alpha decay monitoring",
            "Up to 5 seats",
            "Priority support",
        ],
    ),
    PlanInfo(
        tier        = SubscriptionTier.DESK_FULL,
        name        = "Desk Full",
        price_usd   = 1199.0,
        description = "Institutional grade — for desks and fund managers.",
        features    = [
            "Everything in Desk Preview",
            "5min scan interval",
            "Higher API rate limits",
            "Up to 25 seats",
            "White-label dashboard",
            "Dedicated onboarding",
            "Custom regime tuning",
            "SLA support",
        ],
    ),
]
