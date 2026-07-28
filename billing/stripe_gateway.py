"""
billing/stripe_gateway.py — CoinScopeAI Stripe Billing Gateway
================================================================
FastAPI router exposing billing endpoints.

Endpoints
---------
  GET  /billing/plans                — list all pricing tiers
  GET  /billing/subscription         — current subscription state
  POST /billing/checkout             — create a Stripe Checkout session
  POST /billing/portal               — create a Stripe Customer Portal session
  POST /billing/webhook              — Stripe webhook receiver (raw body, no auth)

Subscription state is persisted in a local JSON sidecar file so it survives
restarts without requiring a database migration.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
import time

from fastapi import APIRouter, Depends, HTTPException
import stripe

from billing.models import (
    PLAN_CATALOGUE,
    CheckoutRequest,
    CheckoutResponse,
    PlanInfo,
    PortalRequest,
    PortalResponse,
    SubscriptionInfo,
    SubscriptionStatus,
    SubscriptionTier,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Stripe SDK initialisation
# ---------------------------------------------------------------------------

def _init_stripe() -> bool:
    """Configure the Stripe SDK if credentials are available. Returns True on success."""
    secret_key = os.getenv("STRIPE_SECRET_KEY", "")
    if not secret_key:
        logger.warning("STRIPE_SECRET_KEY not set — billing endpoints will return 503")
        return False
    stripe.api_key = secret_key
    logger.info("Stripe SDK initialised (test_mode=%s)", secret_key.startswith("sk_test_"))
    return True


_STRIPE_READY = _init_stripe()

# ---------------------------------------------------------------------------
# Subscription state sidecar (simple JSON persistence)
# ---------------------------------------------------------------------------

_STATE_FILE = Path(__file__).parent / "subscription_state.json"


def _load_state() -> dict:
    if _STATE_FILE.exists():
        try:
            return json.loads(_STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def _save_state(state: dict) -> None:
    _STATE_FILE.write_text(json.dumps(state, indent=2))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _price_id_for_tier(tier: SubscriptionTier, cycle: str = "monthly") -> str:
    """Look up the Stripe Price ID for a tier + billing cycle.

    Accepts env vars in the form:
      * STRIPE_PRICE_<TIER>_<INTERVAL>
    """
    cycle = (cycle or "monthly").lower()
    interval = "ANNUAL" if cycle in ("annual", "yearly", "year") else "MONTHLY"
    tier_env = tier.value.upper()
    price_id = os.getenv(f"STRIPE_PRICE_{tier_env}_{interval}", "")
    if not price_id:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Price ID for tier '{tier.value}' ({cycle}) not configured. "
                "Run scripts/setup_stripe_test_products.py and add the "
                "STRIPE_PRICE_*_MONTHLY / _ANNUAL lines from its output to .env."
            ),
        )
    return price_id


def _require_stripe() -> None:
    """Dependency: raise 503 if Stripe is not configured."""
    if not _STRIPE_READY:
        raise HTTPException(
            status_code=503,
            detail="Stripe billing is not configured. Set STRIPE_SECRET_KEY in .env.",
        )


def _enriched_catalogue() -> list[PlanInfo]:
    """Return plan catalogue enriched with monthly price IDs from config."""
    result = []
    for plan in PLAN_CATALOGUE:
        price_id = os.getenv(f"STRIPE_PRICE_{plan.tier.value.upper()}_MONTHLY", "")
        enriched = plan.model_copy(update={"price_id": price_id})
        result.append(enriched)
    return result


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/billing", tags=["Billing"])


# ── GET /billing/plans ────────────────────────────────────────────────────

@router.get("/plans", response_model=list[PlanInfo], summary="List pricing plans")
async def list_plans() -> list[PlanInfo]:
    """
    Returns the four CoinScopeAI pricing tiers with descriptions and feature lists.
    No authentication required.
    """
    return _enriched_catalogue()


# ── GET /billing/subscription ─────────────────────────────────────────────

@router.get(
    "/subscription",
    response_model=SubscriptionInfo,
    summary="Get current subscription status",
)
async def get_subscription() -> SubscriptionInfo:
    """
    Returns the current subscription state from the local sidecar file.
    If no subscription exists, returns status=none.
    """
    state = _load_state()
    if not state:
        return SubscriptionInfo(status=SubscriptionStatus.NONE)

    # Optionally re-validate against Stripe API if state is stale (>5 min)
    last_checked = state.get("last_checked", 0)
    sub_id       = state.get("subscription_id")

    if sub_id and _STRIPE_READY and (time.time() - last_checked > 300):
        try:
            sub    = stripe.Subscription.retrieve(sub_id)
            state.get("tier")
            state.update({
                "status":               sub.status,
                "current_period_end":   sub.current_period_end,
                "cancel_at_period_end": sub.cancel_at_period_end,
                "last_checked":         int(time.time()),
            })
            _save_state(state)
        except stripe.StripeError as exc:
            logger.warning("Could not refresh subscription from Stripe: %s", exc)

    return SubscriptionInfo(
        status               = SubscriptionStatus(state.get("status", "none")),
        tier                 = SubscriptionTier(state["tier"]) if state.get("tier") else None,
        customer_id          = state.get("customer_id"),
        subscription_id      = state.get("subscription_id"),
        current_period_end   = state.get("current_period_end"),
        cancel_at_period_end = state.get("cancel_at_period_end", False),
    )


# ── POST /billing/checkout ────────────────────────────────────────────────

@router.post(
    "/checkout",
    response_model=CheckoutResponse,
    summary="Create a Stripe Checkout session",
    dependencies=[Depends(_require_stripe)],
)
async def create_checkout(body: CheckoutRequest) -> CheckoutResponse:
    """
    Creates a Stripe Checkout session for the requested plan tier.

    Returns a ``checkout_url`` — redirect the user's browser to this URL
    to complete payment. On success Stripe redirects to BILLING_SUCCESS_URL;
    on cancel to BILLING_CANCEL_URL.
    """
    price_id = _price_id_for_tier(body.tier, cycle=body.cycle or "monthly")

    try:
        # Look up or create Stripe customer
        customers = stripe.Customer.search(
            query=f"email:'{body.customer_email}'"
        )
        if customers.data:
            customer_id = customers.data[0].id
            logger.info("Reusing Stripe customer %s for %s", customer_id, body.customer_email)
        else:
            customer = stripe.Customer.create(
                email = body.customer_email,
                name  = body.customer_name or "",
                metadata = {"source": "coinscopeai"},
            )
            customer_id = customer.id
            logger.info("Created Stripe customer %s for %s", customer_id, body.customer_email)

        success_url = os.getenv(
            "BILLING_SUCCESS_URL",
            "http://localhost:8080/billing_success.html?session_id={CHECKOUT_SESSION_ID}",
        )
        cancel_url = os.getenv(
            "BILLING_CANCEL_URL",
            "http://localhost:8080/pricing.html",
        )

        session = stripe.checkout.Session.create(
            customer           = customer_id,
            payment_method_types = ["card"],
            line_items         = [{"price": price_id, "quantity": 1}],
            mode               = "subscription",
            success_url        = success_url,
            cancel_url         = cancel_url,
            metadata           = {
                "tier":   body.tier.value,
                "source": "coinscopeai_engine",
            },
        )

        logger.info(
            "Checkout session created | tier=%s customer=%s session=%s",
            body.tier.value, customer_id, session.id,
        )
        return CheckoutResponse(checkout_url=session.url, session_id=session.id)

    except stripe.StripeError as exc:
        logger.error("Stripe checkout error: %s", exc)
        raise HTTPException(status_code=502, detail=f"Stripe error: {exc.user_message}")


# ── POST /billing/portal ──────────────────────────────────────────────────

@router.post(
    "/portal",
    response_model=PortalResponse,
    summary="Create a Stripe Customer Portal session",
    dependencies=[Depends(_require_stripe)],
)
async def create_portal(body: PortalRequest) -> PortalResponse:
    """
    Creates a Stripe Customer Portal session so the user can manage their
    subscription, update payment method, or cancel.
    """
    try:
        customers = stripe.Customer.search(
            query=f"email:'{body.customer_email}'"
        )
        if not customers.data:
            raise HTTPException(
                status_code=404,
                detail=f"No Stripe customer found for email: {body.customer_email}",
            )

        portal_return_url = os.getenv(
            "BILLING_PORTAL_RETURN_URL",
            "http://localhost:8080/account.html",
        )
        portal = stripe.billing_portal.Session.create(
            customer   = customers.data[0].id,
            return_url = portal_return_url,
        )
        logger.info("Portal session created for %s", body.customer_email)
        return PortalResponse(portal_url=portal.url)

    except stripe.StripeError as exc:
        logger.error("Stripe portal error: %s", exc)
        raise HTTPException(status_code=502, detail=f"Stripe error: {exc.user_message}")

