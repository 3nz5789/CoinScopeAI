# §5 Product Strategy and Packaging

**Status:** v1 LOCKED. All sub-sections committed. Downstream §6, §7, §9, §11, §13, §14, §15 draft against §5 v1.
**Last updated:** 2026-05-01 | **Patched:** 2026-05-10 (max open positions 3→5)
**Disclaimer:** Inventory is inference-based against project memory and engine/dashboard/Telegram-bot scope as documented. v1.1 refresh after a real product audit. Validation phase active; nothing labeled "production-ready" until §8 Capital Cap criteria are met.

---

## 5.0 Assumptions

- **Locked inputs:** §3 personas (P1 Methodist, P2 Engineer, P3 Solo PM); §3.6 segment matrix tier mapping (P1 → Trader, P2 → Trader+Desk power-user, P3 → Desk); §4.4 lead VP; §4.5 product-scope fence; §14 launch sequencing; phased vendor rollout (P1 narrow → P2 → P3).
- **Engine reference:** `coinscopeai-engine-api` — endpoints `/scan`, `/performance`, `/journal`, `/risk-gate`, `/position-size`, `/regime/{symbol}`.
- **Risk thresholds (locked):** max drawdown 10%, daily loss 5%, max leverage 10x, max 5 open positions, position heat cap 80%. (revised 2026-05-03 from max 3 — see decision-log `max-open-positions-revised-3-to-5`)
- **Regime labels (v3 ML):** Trending, Mean-Reverting, Volatile, Quiet.
- **Validation posture:** Binance Testnet only; no real orders; 30-day cohort active.
- **Phase-0 lock:** Tier 1 delivery surface = dashboard canonical, Telegram companion, email transactional only.
