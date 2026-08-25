# ADR-0003: Future LLM and AI Explanation Capability Must Remain Off the Trade-Decision Hot Path

- **Status:** Approved design constraints for a future capability; no explanation capability is presently implemented by this ADR.
- **Date:** 2026-08-25
- **Scope:** CoinScopeAI Agent OS and the existing signal, risk, execution, and review boundaries.

## Decision

CoinScopeAI establishes the following constraints for any future AI or language-model explanation capability. If such a capability is separately designed and approved, its output may summarize already-authoritative strategy, risk, review, paper-execution, or provenance information. It must not authorize, generate, mutate, route, size, submit, cancel, withdraw, or execute a trade.

Under this future-capability constraint, AI output must not be permitted to become a `StrategyDocument`, `RiskDecision`, `ExecutionRequest`, authorization grant, order instruction, or human approval. Actionable strategy and execution state must remain owned by the deterministic strategy, graph, risk, and execution contracts. Any actionable request must remain subject to the existing canonical risk and execution controls; this ADR does not establish an AI explanation contract or prove that those controls enforce arbitrary future AI output.

Any future model/provider integration must remain off the trade-decision hot path. A future implementation must not grant explanation logic direct exchange, wallet, connector, persistence, capture, replay, API, worker, or order capability. A future explanation contract must be designed to fail closed or return a non-actionable result for malformed, stale, contradictory, unsupported, secret-shaped, or authority-bearing data. It must not change strategy, risk-decision, execution-request, authorization, account-mode, connector, venue, asset, quantity, leverage, entry, exit, or lifecycle state.

These are constraints on a future capability, not claims that the capability presently exists. This ADR does not make AI output currently advisory-only by runtime enforcement, does not establish that explanation logic currently exists, does not establish that human review is currently required for explanation results, and does not establish that fail-closed explanation validation is currently enforced.

## Context

The current Agent OS workflow is **Prompt → Graph → Risk gate → Paper fill → Journal/review**. Existing evidence is limited to deterministic planning, canonical risk and execution controls, and hot-path import isolation. The current planner is deterministic and draft-oriented. The current AgentRiskGate rejects unsupported or unsafe requests and delegates to the canonical safety boundary. The current PaperExecutor independently re-checks risk before creating a simulated paper fill. These are existing controls for their canonical inputs and behavior; they are not evidence that a future AI explanation contract is implemented or that arbitrary AI output is already prevented from influencing all downstream paths.

The repository also contains a distinct A3 capture-policy evaluator that is disabled and metadata-only, plus an A4 authority/audit control plane that is process-local and in-memory. Neither surface is an AI explanation capability, a model/provider adapter, durable persistence, or permission to activate capture or external behavior.

## Future-capability constraints

A future explanation capability must be advisory by design and must consume only already-authoritative, explicitly supplied information. It must not create authoritative strategy, risk, execution, authorization, or human-approval objects. Any future model/provider output must be treated as untrusted until a separately approved contract validates its representation, provenance, scope, and safety properties.

A future implementation must use a structured, categorical output representation for v1. Deterministic UI copy may be generated elsewhere from approved categorical fields. A future implementation must combine structured-field validation with a deliberately conservative detector for authority/action language and secret-shaped content. Detection uncertainty must fail closed or produce a non-actionable result. Provider or model identity must be omitted from the v1 contract until a separately approved adapter exists. Human review must be required on every future explanation result, including accepted, denied, and quarantined outcomes.

These requirements are approved design constraints only. They do not assert that the corresponding fields, detector, review workflow, adapter, or runtime enforcement currently exists.

## Existing controls and evidence limits

The following are **existing controls** in the current repository: deterministic prompt-to-draft planning; canonical `AgentRiskGate` evaluation; paper-only Agent OS execution; and `PaperExecutor`’s independent risk re-check before a simulated fill. Existing evidence also includes tests and boundary checks for the relevant canonical paths, including hot-path import isolation.

The following remain **unimplemented future capability**: a formal AI explanation contract; any model/provider adapter; comprehensive validation of AI-generated content; a mandatory explanation review workflow; and runtime enforcement that arbitrary AI output cannot authorize, generate, mutate, route, size, submit, cancel, withdraw, or execute trades.

The current A3 capture policy is a separate **existing disabled capability** and must remain distinct from this future AI explanation boundary. The current A4 authority/audit surface is an **existing process-local/in-memory capability** and must not be represented as durable, recoverable, database-backed, or production-ready by this ADR.

## Consequences

This decision provides a design boundary for evaluating a future explanation capability without introducing one. It preserves deterministic contracts as the intended source of actionable authority and preserves the current paper-first and risk-gated architecture. It also makes clear that documentation of the boundary cannot substitute for implementation evidence.

Any future model/provider adapter or explanation runtime requires a separately approved design, exact implementation path union, implementation approval, deterministic tests, security-boundary tests, and evidence review. No such approval is granted by this ADR.

## Verification status

- **Existing control:** Deterministic planning, canonical AgentRiskGate behavior, PaperExecutor’s independent risk re-check, paper-only Agent OS execution, and hot-path import isolation are present in the current repository.
- **Approved design decision:** The constraints in this ADR apply to any future AI/LLM explanation capability, including structured/categorical v1 output, conservative lexical screening plus structured validation, no provider/model identity in v1, and mandatory human review on every future explanation result.
- **Unimplemented:** The AI explanation contract, explanation logic, model/provider adapter, explanation review workflow, fail-closed explanation validator, and comprehensive runtime enforcement of this ADR.
- **Historical/reported:** Older branch, checkout, local-worktree, and milestone records remain historical evidence and must not be read as current implementation status.

This ADR is a design decision and evidence anchor only. It is not an adapter implementation, model/provider integration, persistence feature, capture permit, review workflow, or proof of comprehensive runtime enforcement.
