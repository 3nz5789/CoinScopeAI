# Backend Endpoints

**Status:** current
**Last verified:** 2026-05-08 (auto-generated from `coinscope_trading_engine/api.py` + `billing/stripe_gateway.py`)
**Audience:** developers and dashboard integrators
**Related:** [`api-overview.md`](api-overview.md), [`../backend/backend-overview.md`](../backend/backend-overview.md), [`../ops/stripe-billing.md`](../ops/stripe-billing.md)

Every endpoint the engine serves. Conventions (base URL, auth, error envelope) are defined in [`api-overview.md`](api-overview.md) — this doc is the per-endpoint reference.

All endpoints are served by `coinscope_trading_engine.api:app` (FastAPI 2.0.0) on port `8001`. The Stripe billing router is mounted at `/billing/*` from `billing/stripe_gateway.py`. Open Swagger lives at <http://localhost:8001/docs>.

> **Auth posture during the validation phase:** the engine currently runs without per-caller bearer enforcement (CORS-allowed origins only). The `Authorization: Bearer …` token described in `api-overview.md` is the production target — see [`../decisions/`](../decisions/) for the cutover decision. Treat *operator-only* tags below as a documented intent, not an enforced gate.

---

## Endpoint inventory (60 routes total)

> Methods/paths below are extracted directly from the live source. If you change `api.py` or `billing/stripe_gateway.py`, re-run the verification snippet at the bottom of this file in the same PR.

### System (2)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/health` | Liveness probe — returns version + testnet flag. Always open. |
| GET | `/config` | Safe (non-secret) runtime config snapshot. |

### Account (4)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/account` | Combined account snapshot — balance + positions + permissions. |
| GET | `/account/balance` | USDT-margined balance summary. |
| GET | `/account/positions` | Open positions reported by the exchange. |
| POST | `/account/sync` | Force a full account refetch (background sync runs every 30 s otherwise). |

### Prices (3)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/prices` | Latest mark prices for the scanner universe. |
| GET | `/prices/{symbol}` | Latest mark price for a single symbol. |
| GET | `/liquidations` | Rolling forced-order buffer; `?symbol=&minutes=` filters. |

### Signals (3)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/signals` | Cached candidates from the most recent scan cycle. |
| GET | `/scan/status` | Last-cycle metadata (started/finished, count, duration). |
| POST | `/scan` | Trigger an on-demand scan. Body: `{pairs?, timeframe?, limit?}`. |

### Orders (7)

| Method | Path | Notes |
| --- | --- | --- |
| POST | `/orders` | Place a single order (operator surface). |
| POST | `/orders/close` | Close an open position. |
| POST | `/orders/bracket` | Attach SL/TP bracket via Algo Order API. |
| GET | `/orders/open` | Working orders (not yet filled or cancelled). |
| GET | `/orders/algo/open` | Open algo (SL/TP) orders. |
| DELETE | `/orders/{order_id}` | Cancel a single order; `?symbol=` required. |
| DELETE | `/orders` | Cancel all working orders for a symbol. |

### Risk (7)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/positions` | Engine view of open positions, reconciled with exchange. |
| GET | `/exposure` | Portfolio exposure summary, daily P&L, heat. |
| GET | `/circuit-breaker` | Breaker state + recent trip history. |
| POST | `/circuit-breaker/reset` | Operator: reset a tripped breaker. |
| POST | `/circuit-breaker/trip` | Operator: manually halt trading; body `{reason}`. |
| GET | `/position-size` | Preview Kelly / fixed-fractional size. Query: `symbol, entry, stop_loss, account_balance, win_rate?, avg_rr?`. |
| GET | `/correlation` | Pairwise Pearson matrix; `?symbols=`, `?timeframe=`, `?limit=`. |

### Autotrade (6)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/autotrade/status` | Power state + last evaluation result. |
| POST | `/autotrade/enable` | Arm autotrade (subject to risk-gate). |
| POST | `/autotrade/disable` | Disarm autotrade (existing positions unchanged). |
| POST | `/autotrade/config` | Hot-update gate config (LONG_ONLY, min_score, leverage, …). |
| POST | `/autotrade/test-alert` | Send a synthetic Telegram alert end-to-end. |
| GET | `/autotrade/telegram-diagnose` | Verify token + chat_id + send permissions. |

### Decisions (4)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/decisions` | Filterable decision-journal feed (jsonl + Postgres mirror). |
| GET | `/decisions/stats` | Aggregate counts by outcome / reason. |
| GET | `/decisions/per-symbol` | Per-symbol verdict timeline + pause state. |
| POST | `/decisions/unpause/{symbol}` | Operator: clear a per-symbol pause. |

### Backtest (4)

| Method | Path | Notes |
| --- | --- | --- |
| POST | `/backtest/run` | Submit a backtest job. Body includes `symbol, timeframe, lookback_days, params`. |
| GET | `/backtest/jobs` | List recent jobs with status. |
| GET | `/backtest/jobs/{job_id}` | Full job result + equity curve. |
| DELETE | `/backtest/jobs/{job_id}` | Remove a job + its artifacts. |

### Historical (4)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/historical/stats` | Row counts per symbol/timeframe in `logs/klines.sqlite`. |
| GET | `/historical/klines` | Paginated raw klines slice. |
| POST | `/historical/backfill` | Backfill missing range; body `{symbol, timeframe, start, end}`. |
| POST | `/historical/refresh` | Force the 15-minute incremental refresh now. |

### Intelligence (3)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/regime` | HMM market regime; query `symbol, timeframe, limit`. |
| GET | `/sentiment` | Composite sentiment score for a symbol. |
| GET | `/anomaly` | Anomaly detection report; query `symbol, timeframe, limit`. |

### Journal (5)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/journal` | Recent trade-journal entries; `?days=` (1–90, default 7). |
| GET | `/journal/{entry_id}/trace` | Full lineage for one trade — signal → gate → order → fill → close. |
| GET | `/performance` | Aggregate performance stats + scale profile. |
| GET | `/performance/equity` | Timestamped equity curve for the full journal window. |
| GET | `/performance/daily` | Today's realised P&L summary. |

### Scale (2)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/scale` | Current scaling profile (risk tier, position limits). |
| POST | `/scale/check` | Evaluate scale-up eligibility; body `{trades, sharpe}`. |

### Validation (1)

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/validate` | Walk-forward backtest over historical klines; query `symbol, timeframe, limit`. |

### Billing — Stripe (5)

Mounted from `billing/stripe_gateway.py` with prefix `/billing`.

| Method | Path | Notes |
| --- | --- | --- |
| GET | `/billing/plans` | Pricing tiers with features and amounts. |
| GET | `/billing/subscription` | Current subscription status for the authenticated customer. |
| POST | `/billing/checkout` | Create a Stripe Checkout session. Body: `{tier, customer_email, customer_name?}`. |
| POST | `/billing/portal` | Create a Stripe Customer Portal session. Body: `{customer_email}`. |
| POST | `/billing/webhook` | Stripe webhook receiver — HMAC-verified, idempotent, hidden from Swagger. |

> **Standalone billing service (port 8002):** historically there was a parallel `billing/webhook_handler.py` running on port 8002. As of 2026-05-08, the in-process router under `coinscope_trading_engine/billing/stripe_gateway.py` is the single source of truth; the standalone service has been retired. The repo-root `billing_server.py` entry point is kept for local Stripe-CLI testing only.

---

## What changed in this revision (2026-05-08)

The previous revision (2026-04-18) documented 21 endpoints organised around an aspirational `/risk-gate`, `/symbols`, `/depth/{symbol}`, `/ready`, `/kill-switch`, and `/metrics` surface that does not exist in the current `api.py`. This revision rewrites the inventory from the live source.

| Previously documented | Status today |
| --- | --- |
| `GET /ready` | **Not implemented.** Use `GET /health` for both liveness and readiness; readiness checks live in the dashboard's status panel. |
| `GET /scan` | **Wrong method/shape.** Real surface is `GET /signals` (cached) + `POST /scan` (trigger) + `GET /scan/status`. |
| `GET /risk-gate` | **Not implemented as a single endpoint.** Equivalent surface is `GET /circuit-breaker` + `GET /exposure` + `GET /decisions`. |
| `GET /position-size` (POST-style body) | **Real surface is GET with query params** (see Risk table). |
| `GET /symbols` | **Not implemented.** Scanner universe is read from `GET /config` (`scan_pairs` field). |
| `GET /depth/{symbol}` | **Not implemented.** No depth endpoint today. |
| `POST /kill-switch` | **Not implemented as a dedicated endpoint.** Kill-switch is implemented via `POST /circuit-breaker/trip` + the dashboard power button. |
| `GET /billing/me` | **Renamed.** Use `GET /billing/subscription`. |
| `GET /metrics` | **Not implemented in-process.** Prometheus metrics are exported by the standalone exporter on `:9000/metrics`. |

Newly documented surfaces (present in code, missing from previous doc):
`/account/*`, `/orders/*`, `/autotrade/*`, `/decisions/*`, `/historical/*`, `/prices/*`, `/exposure`, `/correlation`, `/journal/{entry_id}/trace`, `/scale*`, `/validate`, `/anomaly`, `/sentiment`, `/circuit-breaker/trip`.

---

## Verification snippet

When adding or removing endpoints, regenerate the inventory above by running the snippet below from the repo root and reconciling the diff. Anchor any change in the same PR that touches `api.py`.

```python
import re, pathlib

src = pathlib.Path("coinscope_trading_engine/api.py").read_text()
billing = pathlib.Path("coinscope_trading_engine/billing/stripe_gateway.py").read_text()

app_routes = re.findall(r'@app\.(get|post|put|patch|delete)\("([^"]+)".*?tags=\["([^"]+)"\]', src)
prefix_match = re.search(r'APIRouter\(\s*prefix="([^"]+)"', billing)
prefix = prefix_match.group(1) if prefix_match else ""
billing_routes = [(m, prefix + p, "Billing")
                  for m, p in re.findall(r'@router\.(get|post|put|patch|delete)\(\s*"([^"]+)"', billing)]

for m, p, t in sorted(app_routes + billing_routes, key=lambda r: (r[2], r[1])):
    print(f"{m.upper():6s} {p:50s} [{t}]")
print("TOTAL:", len(app_routes) + len(billing_routes))
```

Expected output as of 2026-05-08: **60 routes** (55 in `api.py` + 5 in `billing/stripe_gateway.py`).
