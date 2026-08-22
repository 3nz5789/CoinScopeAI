# CoinScopeAI Agent OS — Phase 1 Architecture

**Status:** Phase‑1 scaffold implemented on the `agent-os/phase1-scaffold` branch.

**Scope:** Establish a simple, modular VS-Code-style monorepo seam for prompt-to-graph strategy work, deterministic replay, mandatory risk evaluation, and paper execution. This phase does not place live orders or create mainnet wallet paths.

## 1. Product boundary

CoinScopeAI is evolving from a regime-aware scanner and paper-trading system into an **AI-as-a-Service Agent OS** for crypto traders. The Phase‑1 workflow is:

> **Prompt → Graph → Inspect → Risk gate → Paper fill → Journal/review**

The current P0 engine, market-data services, paper-trading safety implementation, and dashboard remain in place. The new `agent_os/` package is a bounded context that introduces stable contracts and entry points without moving or rewriting active P0 modules.

The implementation deliberately keeps parsing deterministic and draft-oriented. A future language-model parser can sit behind the same strategy-document contract, but no model call is required to run the Phase‑1 demo and no language-model decision is placed on the execution hot path. This follows the existing repository decision to keep LLM calls off the hot path.[^1]

## 2. Layered architecture

### 2.1 Data layer

The data layer provides normalized events to both live adapters and deterministic replay. Agent runtime code consumes `MarketDataPort`, not provider-specific clients.

| Area | Phase‑1 responsibility | Current implementation |
|---|---|---|
| Market feeds | Normalize ticker, trade, order-book, funding, liquidation, open-interest, and candle events | The existing `services/market_data/streams/` subsystem remains the data-plane implementation.[^2] |
| On-chain feeds | Reserve a provider-neutral port for chain observations | Contract deferred; no production chain dependency is introduced |
| Research feeds | Reserve a provider-neutral port for news and research metadata | Contract deferred; no research provider is required for the scaffold |
| Event transport | Preserve event-time, receive-time, provider, sequence, and provenance | `MarketEvent` and `EventSource` support fixture/replay/live provenance labels |
| Data quality | Expose provider state and freshness explicitly | `DataStatus` reports state, freshness, last event time, and message |

Live and replay inputs should have the same normalized shape. The existing stream CLI already supports record, replay, download, and status operations; Phase 1 wraps that command surface rather than creating a second replay engine.[^3]

### 2.2 Agent runtime

The runtime owns strategy representation and orchestration. It does not own exchange credentials or provider order writes.

| Component | Responsibility |
|---|---|
| `StrategyDocument` | Portable source of truth for prompt, graph nodes, code/spec preview, version, mode, lifecycle, and missing fields |
| `AgentGraph` | Validates required schedule, market, condition, entry, risk, and exit nodes |
| `SkillRegistry` | Registers explicit runtime capabilities; unknown Skills fail rather than being guessed |
| `draft_from_prompt` | Deterministically creates an editable paper-mode draft and reports missing fields |
| `AgentRunner` | Inspects a graph against fixture/replay events and emits observations; it does not create execution requests |
| Simulation contracts | Reserve result envelopes for replay/backtest metrics, equity, trades, assumptions, and paper sessions |

A draft can expose placeholder nodes so the UX can show what remains to be specified. However, `AgentGraph.validate()` also checks `missing_fields`; an incomplete prompt is blocked and cannot proceed to a paper fill.

The initial lifecycle is:

```text
draft → backtest_ready → backtest_passed → paper_ready → paper_armed
                                                ↓
                                      live_review_required
```

The scaffold only implements the draft and paper-safe portions of this lifecycle. Live review is represented as a future state, not an enabled capability.[^4]

### 2.3 Risk and execution layer

Every strategy or execution request must cross the Agent OS risk boundary, including paper requests:

```text
Strategy graph or caller
        ↓
RiskCheckRequest / ExecutionRequest
        ↓
AgentRiskGate.evaluate(...)
        ↓
Existing paper-trading SafetyGate
        ↓
PaperExecutor only
        ↓
Simulated fill / journal event
```

`AgentRiskGate` delegates order validation to the existing `services.paper_trading.safety.SafetyGate`, which is the current non-bypassable safety boundary. The existing safety implementation checks kill switch state first, applies hardcoded and configurable limits, records rejection reasons, and fails closed when state is uncertain.[^5]

Phase‑1 policy is explicit:

| Control | Phase‑1 behavior |
|---|---|
| Default mode | `paper` |
| Testnet order submission | Disabled from Agent OS entry points; existing P0 testnet code is not changed by this scaffold |
| Live order placement | No implementation or route |
| Mainnet wallets | No implementation or route |
| Withdrawals | No implementation; future connectors must default to withdrawals disabled |
| Connector | Only the logical `paper` connector is accepted by `AgentRiskGate` |
| Symbol allowlist | BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, and XRPUSDT |
| Risk state | Delegated to the canonical `SafetyGate` |
| Unknown, invalid, or stale state | Reject; never guess |
| Audit metadata | Request ID, idempotency key, actor, mode, policy version, and typed reasons; no secrets |
| Paper fills | In-memory simulated fills with no exchange order ID |

The risk and execution contracts keep decision logic separate from provider integration. `PaperExecutor.submit()` re-evaluates the request through the risk gate instead of trusting a caller-provided approval.

### 2.4 UX layer

The existing React dashboard remains at `apps/dashboard/`. Phase 1 exposes backend contracts that a future Agent Studio route can render without duplicating business logic.

| Surface | Contract or state to display |
|---|---|
| Agent Studio | Prompt, strategy document, graph nodes, missing fields, lifecycle, and `mode: paper` |
| Dashboard | `/health`, `/risk/status`, paper session state, and data/replay provenance |
| Journal | Strategy version, decision, risk result, simulated fill, and review metadata |
| Learning hub | Future template/course metadata linking into replay and paper sandboxes |
| Safety language | “Paper mode,” “Keys locked,” “Risk gate required,” “Replay complete,” and “Live execution disabled” |

A frontend may stage and display a request, but it cannot claim an order executed unless a responsible backend adapter confirms it. Secrets, exchange credentials, private keys, and wallet seed phrases must not appear in source, fixtures, browser storage, logs, or screenshots.[^6]

## 3. Repository structure

The canonical repository remains a single multi-folder monorepo. Phase 1 adds only the following bounded context and worker entry point; existing P0 directories are not renamed or duplicated.

```text
CoinScopeAI/
├── agent_os/
│   ├── contracts/
│   │   ├── strategy.py       # StrategyDocument, StrategyNode, lifecycle
│   │   ├── market.py         # MarketEvent, DataStatus, provenance
│   │   ├── risk.py           # RiskCheckRequest, RiskDecision, modes
│   │   ├── execution.py      # ExecutionRequest, ConnectorSummary
│   │   ├── simulation.py     # SimulationRun, PaperSession, metrics
│   │   └── journal.py        # JournalEvent
│   ├── data/
│   │   ├── ports.py          # MarketDataPort, EventSource
│   │   └── fixtures.py       # Deterministic BTCUSDT fixture stream
│   ├── runtime/
│   │   ├── graph.py          # AgentGraph and validation
│   │   ├── skills.py         # Skill and SkillRegistry
│   │   ├── planner.py        # Deterministic prompt-to-draft planner
│   │   └── runner.py         # Replay/fixture inspection runner
│   ├── risk/gate.py          # AgentRiskGate facade over P0 SafetyGate
│   ├── execution/
│   │   ├── ports.py          # ExecutionPort protocol
│   │   └── paper.py          # Risk-gated simulated fills
│   └── api/app.py            # FastAPI entry point and Phase-1 routes
├── services/agent_worker/
│   └── main.py               # One deterministic paper cycle
├── tests/agent_os/
│   ├── conftest.py
│   ├── test_graph.py
│   ├── test_risk_gate_boundary.py
│   └── test_paper_execution.py
├── apps/dashboard/           # Existing React dashboard, unchanged
├── services/market_data/     # Existing recorder/replay subsystem
├── services/paper_trading/   # Existing canonical safety boundary
├── docs/architecture/
│   └── agent-os-phase1.md
├── Makefile                  # Phase-1 dev, worker, test, replay commands
└── pyproject.toml            # Agent OS test/coverage/tooling scope
```

### Entry points

The API is importable as `agent_os.api.app:app`. The worker is runnable as `python3 -m services.agent_worker.main`. The `make replay` target invokes `services.market_data.streams.cli replay`, preserving the existing recorder/replay implementation. The root Makefile’s default test and type-check paths now target the actual repository layout instead of the removed `coinscope_trading_engine` tree.

## 4. Phase‑1 milestones

| Milestone | Scope | Acceptance evidence |
|---|---|---|
| 1. Agent Studio and project graph | Strategy document, deterministic draft planner, graph validation, lifecycle, missing-field reporting | A complete prompt yields a valid paper draft; an incomplete prompt is visibly blocked |
| 2. Data connectors v1 | Normalized event contracts, fixture source, provider status, replay-compatible input | The runtime consumes ordered events with explicit fixture/replay provenance |
| 3. Risk gate and wallets v1 | Risk-check contract, facade over canonical `SafetyGate`, paper account/session shape, connector summary | Paper requests are approved/rejected by the gate; live/testnet order modes and non-paper connectors reject |
| 4. Paper trading and basic dashboards | Risk-gated paper executor, simulated fill ledger, health/risk/session routes | `make agent-demo` completes graph inspection → risk evaluation → simulated fill |
| 5. Replay and verification harness | Deterministic tests, safety regression tests, Makefile integration, degraded-state coverage | `make test` passes without network credentials; `make replay` uses the existing stream replay path |

## 5. Commands and expected behavior

Run from the repository root with Python 3.11+ and the project dependencies installed.

| Command | Expected behavior |
|---|---|
| `make worker` | Prints JSON for a deterministic BTCUSDT paper cycle. It includes a valid graph, three fixture observations, an approved risk decision, one simulated fill, and `live_order_placement: false`. |
| `make agent-demo` | Alias for `make worker`. |
| `make dev-all` | Starts FastAPI on `http://127.0.0.1:8010` with live order placement and mainnet wallets disabled. |
| `curl http://127.0.0.1:8010/health` | Returns service health plus `execution_mode: paper`, `live_order_placement: false`, and `mainnet_wallets: false`. |
| `curl -X POST http://127.0.0.1:8010/agent/drafts -H 'Content-Type: application/json' -d '{"prompt":"Every 1h long BTCUSDT when funding is negative with risk 1% and stop loss 2%"}'` | Returns the strategy document, graph nodes, and a valid graph with no missing fields. |
| `make test` | Runs the repository test suite, including the Agent OS tests, without requiring live credentials. |
| `make replay DATA_DIR=./data/recordings SPEED=10` | Invokes the existing market-data replay CLI. The directory must contain recorded JSONL/JSONL.GZ stream data. |
| `make lint` | Runs Ruff and Black checks for the Phase‑1 package, worker, and tests. |
| `make typecheck` | Runs mypy against the new Agent OS package and worker. |

A draft such as `Watch BTCUSDT` should return missing fields for cadence, conditions, entry, risk rules, and exit rules. It must not produce an execution request or simulated fill.

## 6. Non-goals and follow-up boundaries

Phase 1 does not enable live orders, Binance mainnet, mainnet wallets, withdrawals, autonomous hot-path LLM decisions, production performance claims, or full migration of the current P0 engine. A future connector integration must introduce backend authorization, least-privilege scopes, explicit confirmation, idempotency, audit persistence, re-authentication, and a separately reviewed release gate.

The next recommended work is to add a persistent strategy-project model and Agent Studio route over these contracts, then connect a replay-backed simulation runner with documented fee, slippage, funding, leverage, and annualization assumptions. Only after those states are observable and tested should connector verification and testnet order adapters be considered.

## References

[^1]: [CoinScopeAI README — Architecture Decision Records](../../README.md#architecture-decision-records), especially ADR-0003 on keeping LLM calls off the hot path.
[^2]: [CoinScopeAI market-data service tree](../../services/market_data/), the existing normalized stream implementation.
[^3]: [CoinScopeAI market-data streams CLI](../../services/market_data/streams/cli.py), which already provides record, replay, download, and status commands.
[^4]: [CoinScopeAI paper-trading configuration](../../services/paper_trading/config.py), including the hardcoded testnet-only default and conservative configurable limits used by the Phase-1 facade.
[^5]: [CoinScopeAI paper-trading safety implementation](../../services/paper_trading/safety.py), the canonical fail-closed order-validation boundary.
[^6]: [CoinScopeAI project instructions and repository guidance](https://github.com/3nz5789/CoinScopeAI), applied here as repository-level security and execution constraints.
