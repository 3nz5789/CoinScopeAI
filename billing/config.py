"""
CoinScopeAI Billing — Pricing Configuration
============================================
Canonical Track B pricing tiers. Price IDs are created in Stripe Dashboard
(Test Mode) and set as environment variables.

Tier           Monthly     Annual (20% off)
────────────────────────────────────────────
Free           $0/mo       $0/yr
Trader         $79/mo      $948/yr
Desk Preview   $399/mo     $4,788/yr
Desk Full      $1,199/mo   $14,388/yr

All amounts in USD cents for Stripe API.
"""

import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PriceConfig:
    tier: str
    display_name: str
    monthly_usd: int          # in cents
    annual_usd: int           # in cents
    monthly_price_id: str     # Stripe Price ID (from env)
    annual_price_id: str      # Stripe Price ID (from env)
    most_popular: bool = False
    features: list = field(default_factory=list)


# ── Canonical Plan Registry ───────────────────────────────────────────────────

PLANS: dict[str, PriceConfig] = {
    "free": PriceConfig(
        tier="free",
        display_name="Free",
        monthly_usd=0,
        annual_usd=0,
        monthly_price_id=os.getenv("STRIPE_PRICE_FREE_MONTHLY", ""),
        annual_price_id=os.getenv("STRIPE_PRICE_FREE_ANNUAL", ""),
        features=[
            "3 pairs monitored",
            "4h scan interval",
            "5 alerts per day",
            "Telegram alerts",
            "Trade journal (7 days)",
            "Basic risk gate",
        ],
    ),
    "trader": PriceConfig(
        tier="trader",
        display_name="Trader",
        monthly_usd=7900,
        annual_usd=75840,  # 20% annual discount
        monthly_price_id=os.getenv("STRIPE_PRICE_TRADER_MONTHLY", ""),
        annual_price_id=os.getenv("STRIPE_PRICE_TRADER_ANNUAL", ""),
        most_popular=True,
        features=[
            "25 pairs monitored",
            "1h scan interval",
            "50 alerts per day",
            "ML regime detection (v3)",
            "Telegram + email alerts",
            "Trade journal (unlimited)",
            "Backtesting engine",
            "Kelly position sizing",
            "Walk-forward validation",
        ],
    ),
    "desk_preview": PriceConfig(
        tier="desk_preview",
        display_name="Desk Preview",
        monthly_usd=39900,
        annual_usd=383040,  # 20% annual discount
        monthly_price_id=os.getenv("STRIPE_PRICE_DESK_PREVIEW_MONTHLY", ""),
        annual_price_id=os.getenv("STRIPE_PRICE_DESK_PREVIEW_ANNUAL", ""),
        features=[
            "Unlimited pairs",
            "15min scan interval",
            "Unlimited alerts",
            "Multi-exchange (Binance, Bybit, OKX, Hyperliquid)",
            "CVD + whale flow signals",
            "API access (full engine)",
            "TradingView webhooks",
            "Alpha decay monitoring",
            "Up to 5 seats",
            "Priority support",
        ],
    ),
    "desk_full": PriceConfig(
        tier="desk_full",
        display_name="Desk Full",
        monthly_usd=119900,
        annual_usd=1151040,  # 20% annual discount
        monthly_price_id=os.getenv("STRIPE_PRICE_DESK_FULL_MONTHLY", ""),
        annual_price_id=os.getenv("STRIPE_PRICE_DESK_FULL_ANNUAL", ""),
        features=[
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
}


def get_price_id(tier: str, interval: str) -> str:
    """
    Return the Stripe Price ID for a given tier + billing interval.

    Args:
        tier:     "free" | "trader" | "desk_preview" | "desk_full"
        interval: "monthly" | "annual"

    Raises:
        ValueError if tier unknown or Price ID not configured.
    """
    plan = PLANS.get(tier.lower())
    if not plan:
        raise ValueError(f"Unknown tier '{tier}'. Valid: {list(PLANS.keys())}")

    price_id = plan.monthly_price_id if interval == "monthly" else plan.annual_price_id

    if not price_id:
        raise ValueError(
            f"Stripe Price ID for {tier}/{interval} not configured. "
            f"Set STRIPE_PRICE_{tier.upper()}_{interval.upper()} in .env"
        )

    return price_id


def list_plans() -> list[dict]:
    """Serialisable plan list for the /billing/plans endpoint."""
    result = []
    for plan in PLANS.values():
        result.append({
            "tier": plan.tier,
            "display_name": plan.display_name,
            "most_popular": plan.most_popular,
            "monthly_usd_cents": plan.monthly_usd,
            "annual_usd_cents": plan.annual_usd,
            "monthly_usd": plan.monthly_usd / 100,
            "annual_usd": plan.annual_usd / 100,
            "annual_savings_pct": 20,
            "features": plan.features,
            "price_ids_configured": {
                "monthly": bool(plan.monthly_price_id),
                "annual": bool(plan.annual_price_id),
            },
        })
    return result
