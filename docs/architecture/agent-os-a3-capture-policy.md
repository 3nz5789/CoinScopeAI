# A3 Design — PaperRun Recording-Capture Eligibility and Authorization Policy

**Project:** CoinScopeAI Agent OS
**Design scope:** Policy-only, read-only design against `main`
**Historical inspected baseline:** `fa8f841a6a0f92144c435242a9e11a7739383d7b`; current canonical `main` is `4bfae940d2ec373ee7c63d65819361cc8eafd41e`. This record describes the distinct disabled A3 capture-policy capability and must not be relabeled as the future AI explanation policy.
**Clone:** `/home/ubuntu/readonly-clones/coinscopeai-a3-20260825T115247Z`
**Repository:** `https://github.com/3nz5789/CoinScopeAI.git`
**Prepared by:** Manus AI

## 1. Executive decision

A3 should define a **pure eligibility and authorization policy**, not a recording implementation. Its only responsibility is to assess whether a future PaperRun recording-capture request is structurally complete, tenant- and lineage-bound, within a closed allowlist, and supported by valid human-authorization evidence. It may return a categorical decision and safe digest-only provenance, but it must not inspect market material, invoke A2, toggle `PAPERRUN_RECORDING_CAPTURE_V1`, create storage, create a manifest or repository receipt, schedule replay, or reach any order or external boundary. The approved current policy permits only `synthetic_fixture_metadata_v1`; even when all eligibility and human-authorization metadata validates, the deterministic result is `A3_CAPTURE_DISABLED`.

The design follows the current Agent OS pattern: **Prompt → Graph → Risk gate → Paper fill → Journal/review**. A3 is deliberately positioned before any future capture activation and outside both material handling and execution. The current repository already contains the disabled supplier vocabulary and A1/A2 gates, but no authorized capture activation path was found on the inspected commit.

## 2. Repository baseline verification

The one authorized fresh clone was created at the timestamped path shown above. Read-only verification produced the following result:

| Check | Result | Evidence |
|---|---|---|
| Clone path | Verified | `/home/ubuntu/readonly-clones/coinscopeai-a3-20260825T115247Z` |
| Remote | Verified | `https://github.com/3nz5789/CoinScopeAI.git` |
| Branch | Verified | `main` |
| HEAD | Verified | `fa8f841a6a0f92144c435242a9e11a7739383d7b` |
| Worktree | Clean | `git status --porcelain=v1 --branch` reported only `## main...origin/main` |
| Main ref | Verified | `refs/heads/main` resolves to the expected commit |
| Required commit object | Verified | `git cat-file -t ...` returned `commit` |
| Ancestry | Verified | `git merge-base --is-ancestor` succeeded |
| Object integrity | No errors observed | `git fsck --full --no-progress` produced no error output |
| Phase 1 paths | Present | `agent_os/`, `services/agent_worker/main.py`, `services/market_data/streams/cli.py`, `services/paper_trading/safety.py`, architecture documentation, and tests |
| A1 paths | Present | `agent_os/persistence/contracts.py`, `ingress.py`, `ports.py` |
| A2 path | Present | `agent_os/persistence/material.py` and focused A2 tests |

The commit history identifies the exact prerequisites: `fa2b8717` introduced the Phase 1 scaffold, `064b7ea3` added metadata-only ingress contracts, and the inspected HEAD `fa8f841a` added the private in-memory material boundary.

### Capture-disabled finding

`TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1` exists as a closed vocabulary member in `agent_os/persistence/contracts.py:16-20`, and is mapped to PaperRun recording purpose/source/role in `agent_os/persistence/ingress.py:40-50`. It is **not enabled**: `_preflight_supplier()` rejects it at `agent_os/persistence/ingress.py:140-148`, and A2’s `_supplier_preflight()` rejects it before any source inspection at `agent_os/persistence/material.py:238-249` and `649-664`. The repository has no separate feature-flag implementation or capture activation path connected to Agent OS; the disabled behavior is enforced by the closed supplier gate. The existing stream CLI exposes a separate recorder/replay command surface (`services/market_data/streams/cli.py:88-160` and `160-224`), but no A3 or Agent OS path invokes it.

## 3. Existing contracts and boundaries

### 3.1 A1 supplier, identity, and provenance gates

A1 is metadata-only. `CanonicalJsonPolicy`, `TenantContext`, capability metadata, identity, provenance, artifact identity, and scanner verdict are immutable dataclasses in `agent_os/persistence/contracts.py:119-177`, `143-177`, `180-227`, `230-279`, and `282-295`. The contracts explicitly describe metadata rather than material operations; `IngressState` is labelled metadata-only at `contracts.py:58-67`, and scanner verdict metadata says no scanner is invoked by A1 at `contracts.py:254-256`.

The supplier gate is the first control. `ingress.py:_preflight_supplier()` at lines `140-148` rejects the PaperRun capture supplier and accepts only the synthetic fixture supplier. Capability validation at `ingress.py:207-247` checks the closed supplier/purpose/consumer vocabulary, tenant identity, nonce, time bounds, and capability-to-identity match. Provenance validation at `ingress.py:250-280` binds supplier, source kind, purpose, artifact role, schema, canonicalization profile, policy version, and non-reserved retention class. Artifact validation at `ingress.py:283-306` binds digest, sizes, media type, schema, canonicalization, and policy version.

`validate_ingress_metadata()` at `ingress.py:424-457` performs the ordered metadata checks and requires capability supplier/purpose to match provenance. Scanner validation is supplied-evidence validation only: `validate_scanner_verdict()` at `ingress.py:350-385` checks accepted status, digest and size match, tenant and purpose match, freshness, validity, and expiry; it does not invoke a scanner. Transition evidence is similarly supplied metadata at `ingress.py:460-509`. `advance_state()` at `ingress.py:512-575` enforces allowed transitions, reasons, timestamps, and terminal behavior without performing a named operation.

The safe A1 receipt projection is whitelist-only. `RedactedIngressReceipt` is defined at `contracts.py:342-391`; `IngressReceipt.to_redacted()` at `contracts.py:394-434` exposes only approved metadata including a digest, sizes, typed provenance, scanner metadata, state, status, and error. Idempotency comparison is tenant-scoped and binding-complete in `ingress.py:578-638`; it returns create, idempotency-match, or conflict outcomes and is not a storage implementation. The future receipt ports are deliberately protocol-only in `agent_os/persistence/ports.py:1-32`.

### 3.2 A2 fixture-only material admission and lease boundary

A2’s module-level contract states that it is private, bounded, in-process material handling for synthetic fixtures only and provides no persistence, scanner, replay, runtime, execution, API, or external-system behavior (`agent_os/persistence/material.py:1-8`). The only public content ingress is the exact built-in `str` accepted by `MaterialCoordinator.prepare()`.

Supplier preflight precedes source inspection and coordinator mutation. `_supplier_preflight()` at `material.py:238-249` rejects `PAPERRUN_RECORDING_CAPTURE_V1`; `MaterialCoordinator.prepare()` at `material.py:649-694` repeats this first, rejects disposed/reused coordinators and invalid metadata, and then calls the A1 metadata validator. Only after those checks does it inspect the source string, enforce UTF-8 and raw-size limits, parse/canonicalize the fixture schema, enforce canonical size, compute a SHA-256 digest, and compare it with supplied artifact metadata (`material.py:696-750`).

The retained value is a private canonical buffer. `_PrivateCanonicalMaterial` at `material.py:336-373` has no public methods, refuses serialization, and zeroes/clears its buffer on disposal. `MaterialLease` is a single-use, consumer-bound, non-serializable internal handoff (`material.py:376-408`). Its only public surface is `status`, `consume`, and `cancel`; `consume()` at `material.py:448-514` verifies status, clock, consumer identity, expiry, callback shape, callback completion, and disposal before consuming and disposing the material. `cancel()` at `material.py:516-526` invalidates the lease and disposes retained material. `MaterialCoordinator.dispose()` at `material.py:782-815` invalidates active leases and explicitly has no record-deletion surface.

The A2 security tests make the boundary executable. `tests/agent_os/test_persistence_security_boundaries.py:14-37` restricts imports and forbids network, filesystem, database, subprocess, KMS, and external dependencies; `:38-113` forbids sensitive fields and capability names; `:128-180` checks the exact production path union and disallows side-effecting calls; `:183-220` proves that private material has no extraction methods and that the lease API is only `cancel`, `consume`, and `status`; and `:222-245` proves the receipt ports are protocol declarations without concrete bodies. Behavioral lease and disposal tests are in `tests/agent_os/test_persistence_material.py:346-498`.

### 3.3 Phase 1 PaperRun, risk, and paper-execution boundaries

The architecture contract defines the Phase 1 workflow and separates data, runtime, risk/execution, and UX at `docs/architecture/agent-os-phase1.md:7-15` and `:17-56`. The risk/execution flow is explicitly `RiskCheckRequest / ExecutionRequest → AgentRiskGate → existing SafetyGate → PaperExecutor → simulated fill/journal event` at `:58-94`.

`MarketEvent` uses explicit `DataProvenance.FIXTURE`, `REPLAY`, or `LIVE` values in `agent_os/contracts/market.py:20-43`. `AgentRunner` is observation-only: its contract at `agent_os/runtime/runner.py:30-35` says it emits observations rather than execution requests, and `inspect()` at `:41-59` blocks incomplete graphs and otherwise consumes the supplied source into observations. Phase 1 guidance allows fixture/replay provenance and rejects live inputs for the relevant replay/paper paths.

`RiskCheckRequest` defaults to paper mode and the logical `paper` connector at `agent_os/contracts/risk.py:21-36`; `AgentRiskGate.evaluate()` at `agent_os/risk/gate.py:66-120` rejects incomplete identity, non-paper modes, non-paper connectors, non-allowlisted symbols, and invalid order parameters before delegating to the canonical `SafetyGate`. `PaperExecutor.submit()` at `agent_os/execution/paper.py:30-77` re-evaluates risk and appends only an in-memory `PaperFill`; the fill has no exchange order identifier (`paper.py:13-24`).

The API’s declared Phase 1 surface is draft, risk evaluation, paper orders, and paper session. Its application description explicitly says live execution is disabled (`agent_os/api/app.py:39-47`); health reports paper mode, no live order placement, and no mainnet wallets (`app.py:73-82`); risk status reports `live_keys_locked: True` (`app.py:111-117`); and the only order route is `/paper/orders`, which reaches the in-memory paper executor (`app.py:120-146`). The worker is deterministic and fixture-based at `services/agent_worker/main.py:17-50`, with `live_order_placement: False`.

### 3.4 Existing approval, policy, audit, feature-flag, and observability patterns

The existing repository patterns are **fail-closed policy and safe metadata telemetry**, not an A3 authorization implementation. Policy versions are explicit in A1 (`contracts.py:9-13`) and Phase 1 risk (`agent_os/contracts/risk.py:33-35`). Audit identifiers and typed reasons are returned by the risk contract (`risk.py:53-69`) and built by the gate (`gate.py:51-64`). Kill-switch-first and fail-closed safety are delegated to the canonical P0 `SafetyGate` (`gate.py:18-20`, `:103-120`; architecture doc `:76-94`). Health and risk status expose categorical mode and lock state without credentials (`api/app.py:73-82`, `:111-117`).

The current A1/A2 receipt vocabulary is a useful precedent: typed enums, immutable contracts, explicit tenant binding, idempotency metadata, digest-only identity, categorical outcomes, and whitelist projections. However, `MetadataReceiptPort` remains a future protocol with no adapter (`agent_os/persistence/ports.py:15-24`), and there is no durable audit store, feature-flag service, or authorization repository on this baseline. A3 must preserve that distinction rather than imply persistence or activation.

## 4. A3 policy-only definition

### 4.1 Responsibility and non-responsibility

A3 is a **pure function over supplied metadata**:

```text
request metadata + human authorization evidence + policy snapshot + now
    → categorical eligibility decision + digest-only safe provenance
```

A3 may validate shapes, enum values, exact bindings, timestamps, digest syntax, policy version, and whitelist membership. It may compute a digest over already-supplied metadata if the future contract explicitly defines canonical serialization, but it must never accept or inspect raw recording bytes. A3 must not import or call A1 ingress coordination, A2 material handling, recorder/replay engines, storage, encryption/KMS, API clients, workers, connectors, wallets, exchanges, payments, or order/paper-fill code.

“Approved for future capture” means **authorization to a future, separately implemented capture operation**, not permission to capture now. The only positive decision name is `APPROVED_FOR_FUTURE_CAPTURE`, and it must carry `recheck_required: true`. Under the current disabled policy, this positive state is unreachable and the evaluator returns `A3_CAPTURE_DISABLED` instead. The result must never be rendered as recorded, stored, replayable, executed, secure, encrypted, or production-ready.

### 4.2 Proposed immutable metadata model

The smallest coherent future A3 contract should contain the following immutable, metadata-only values. Exact names are proposed and require approval before implementation.

| Contract | Required fields and constraints | Purpose |
|---|---|---|
| `CaptureEligibilityRequest` | `request_id`, `idempotency_key`, `tenant_id`, `workspace_id`, `agent_id`, `agent_version`, `strategy_digest`, `paper_account_id`, `venue_id`, `asset_allowlist`, `source_class`, `data_classification`, `requested_at`, `requested_by`, `policy_version` | Binds one request to one tenant, workspace, agent/version, paper account, venue, asset set, source, classification, actor, and policy. |
| `AgentVersionBinding` | `agent_id`, immutable `agent_version`, `strategy_digest`, `graph_digest`, optional `risk_policy_version`, `assumptions_digest` | Prevents approval drift between the reviewed agent and future capture target. The version and digests must be supplied metadata, never loaded from source. |
| `PaperAccountBinding` | `paper_account_id`, `account_mode = paper`, `connector_id = paper`, `account_policy_version`, `live_keys_locked = true` | Ensures the target is a logical paper account and not a live/testnet account or credential-bearing connector. |
| `VenueAssetBinding` | `venue_id` from a closed venue allowlist, non-empty canonical `asset_allowlist`, no wildcard, no unlisted symbols, `market_scope` such as spot/futures if approved | Prevents approval from being broadened to another venue, market, or asset. Asset values must be normalized and sorted before digesting. |
| `SourceBinding` | `source_kind` from a closed future capture-source vocabulary, `source_id` or `recording_id` only as an opaque identifier, `source_digest` optional but syntax-checked, no URL/path/locator/raw payload | Carries digest-only provenance and prevents source substitution without exposing a source location. |
| `ClassificationBinding` | `data_classification` must be exactly `synthetic_fixture_metadata_v1`; `classification_policy_version` is required | Makes the currently permitted data class explicit and reviewable. Unknown, missing, non-synthetic, and future classifications deny. |
| `HumanAuthorizationEvidence` | `authority_type`, opaque `authority_id`, opaque `decision_id`, `approved_at`, `expires_at`, `scope_digest`, `evidence_digest`, `single_use_nonce`, `revocation_epoch`, `reason_code`; future non-synthetic classes require both workspace-owner and designated risk/data-reviewer evidence | Represents evidence of authorization without storing the approval text, credentials, prompt, secret, or sensitive journal/PnL content. |
| `A3PolicySnapshot` | `policy_version`, `allowed_authority_types`, `allowed_source_classes`, `allowed_classifications = [synthetic_fixture_metadata_v1]`, `allowed_venues`, `allowed_assets`, `max_ttl_seconds = 600`, `require_single_use = true`, `require_revocation_check = true` | Immutable policy input for deterministic evaluation. A3 has no activation field or capability and unconditionally returns `A3_CAPTURE_DISABLED` after otherwise-valid predicates pass. |

The request must bind **all** of `tenant_id`, `workspace_id`, `agent_id`, immutable `agent_version`, `strategy_digest`, `paper_account_id`, `venue_id`, exact normalized `asset_allowlist`, `source_kind/source_id`, `data_classification`, `policy_version`, actor, request identity, and time window. A missing or mismatched binding is a denial, not a partial approval. The current allowed classification is exactly `synthetic_fixture_metadata_v1`; future non-synthetic classifications require workspace-owner plus designated risk/data-reviewer authority and a separately approved policy version.

### 4.3 Human-authorization evidence vocabulary

A3 recognizes only a closed vocabulary. The approved current governance model uses workspace-owner authority for the eligible synthetic metadata class. Any future non-synthetic class requires **both** workspace-owner authority and a designated risk/data reviewer; that future class remains denied until its classification and activation policy are separately approved. Proposed authority types are:

| Authority type | Meaning | Default status |
|---|---|---|
| `WORKSPACE_OWNER` | Workspace owner explicitly authorizes the exact scope | Approved authority for the current synthetic metadata policy |
| `TRADING_RISK_REVIEWER` | Designated risk reviewer authorizes the paper-only capture scope | Required as one half of future non-synthetic dual control |
| `DATA_REVIEWER` | Designated data reviewer authorizes classification and retention scope | Required as the designated reviewer role for future non-synthetic classes |
| `COMPLIANCE_REVIEWER` | Designated compliance/data-governance reviewer authorizes classification and retention scope | Future role mapping only; not a substitute until defined |
| `SYSTEM_POLICY` | Server policy attestation that the request is within a pre-approved category | Never sufficient alone for human authorization or capture capability |

Evidence must contain a server-recognized authority identifier, decision identifier, exact scope digest, approval time, expiry time, single-use nonce, and a revocation epoch/version. A free-text “approved” field, client-provided boolean, bearer token, capability value, or UI confirmation alone is not authorization. A3 should not validate signatures or decrypt evidence in this policy-only slice; a future security boundary must define how server-owned evidence is authenticated without exposing secrets to A3.

### 4.4 Eligibility predicates

A3 evaluates every predicate below, but A3 v1 unconditionally returns `A3_CAPTURE_DISABLED` after predicates 1–8 pass. A future activation milestone must introduce its own audited capability outside A3 before `APPROVED_FOR_FUTURE_CAPTURE` can be considered:

1. The request is a well-typed immutable metadata object with valid opaque request ID, idempotency key, actor, timestamps, and policy version.
2. Tenant, workspace, agent, version, strategy digest, paper account, venue, asset allowlist, source, classification, and authorization scope are all present and mutually consistent.
3. `account_mode` is exactly `paper`, `connector_id` is exactly `paper`, and live keys are explicitly locked. `testnet` and `live` are denied.
4. Venue, asset, market scope, source class, and data classification are all members of closed allowlists. The data classification must be exactly `synthetic_fixture_metadata_v1`; wildcards, empty sets, unknown values, provider-specific expansions, and caller-invented values are denied.
5. The immutable agent/version and strategy/graph digests in the request equal the digests in the human evidence scope.
6. The approval is issued by an allowed authority, is not from the future, has a maximum TTL of 600 seconds, has a valid single-use nonce, and has not been revoked or consumed according to the later server authority implementation. Future non-synthetic classes require both workspace-owner and designated risk/data-reviewer evidence.
7. The approval’s `scope_digest` equals the canonical SHA-256 digest of the exact request binding and policy version.
8. No unknown, contradictory, stale, malformed, or unavailable policy/evidence field is present.
9. If predicates 1–8 pass, return `A3_CAPTURE_DISABLED`; never return a positive decision in A3 v1.

No individual “pass” predicate can override a failed predicate. The implementation should evaluate in a deterministic order and return a single categorical result with stable reason codes, while keeping detailed internal diagnostics out of ordinary output.

### 4.5 Default-deny reason codes

The reason code vocabulary must be closed and versioned. Proposed codes are:

| Code | Denial condition |
|---|---|
| `A3_REQUEST_INVALID` | Request shape, type, identifier, or timestamp invalid |
| `A3_POLICY_MISSING` | No server-owned policy snapshot supplied |
| `A3_POLICY_MISMATCH` | Policy version or policy values do not match |
| `A3_TENANT_BINDING_MISMATCH` | Tenant/workspace/evidence tenant binding differs |
| `A3_WORKSPACE_BINDING_MISMATCH` | Workspace differs or is absent |
| `A3_AGENT_BINDING_MISMATCH` | Agent identity or immutable version differs |
| `A3_STRATEGY_DIGEST_MISMATCH` | Strategy/graph/assumptions digest differs |
| `A3_PAPER_ACCOUNT_INVALID` | Account is not explicitly paper-only |
| `A3_CONNECTOR_NOT_PAPER` | Connector is not exactly logical `paper` |
| `A3_LIVE_OR_TESTNET_DENIED` | Live or testnet mode, key, wallet, or order capability appears |
| `A3_VENUE_NOT_ALLOWLISTED` | Venue is absent or not allowlisted |
| `A3_ASSET_NOT_ALLOWLISTED` | Asset set is absent, wildcarded, or not allowlisted |
| `A3_SOURCE_NOT_ALLOWLISTED` | Source class is unknown or not approved |
| `A3_CLASSIFICATION_NOT_ALLOWLISTED` | Data classification is unknown or not approved |
| `A3_AUTHORITY_NOT_ALLOWLISTED` | Authority type or authority identity is not approved |
| `A3_AUTH_EVIDENCE_INVALID` | Required decision, nonce, scope, or evidence digest is invalid |
| `A3_AUTH_SCOPE_MISMATCH` | Evidence does not bind the exact request |
| `A3_AUTH_NOT_YET_VALID` | Approval timestamp is in the future |
| `A3_AUTH_EXPIRED` | Approval TTL or expiry has passed |
| `A3_AUTH_REVOKED` | Revocation state invalidates the approval |
| `A3_AUTH_ALREADY_CONSUMED` | Single-use approval was already consumed |
| `A3_IDEMPOTENCY_CONFLICT` | Same idempotency key maps to different scope/digest |
| `A3_PROVENANCE_INVALID` | Digest-only provenance is malformed or incomplete |
| `A3_UNKNOWN_STATE` | Lifecycle or prior state is unknown |
| `A3_CAPTURE_DISABLED` | Future capture capability is not enabled by a separately approved activation milestone |
| `A3_INTERNAL_POLICY_UNAVAILABLE` | Required server policy/evidence state is unavailable |

The absence of a reason from the vocabulary is itself a contract error and must fail closed. `A3_CAPTURE_DISABLED` is important: even an eligible request must not authorize actual capture while the future activation milestone remains disabled.

### 4.6 Safe categorical decision and receipt

The decision must be a discriminated, whitelist-only value:

```text
A3Decision =
  { decision: "DENIED", reason_code: <closed code>, policy_version,
    decision_id, binding_digest, recheck_required: true }
  | { decision: "APPROVED_FOR_FUTURE_CAPTURE", policy_version,
      decision_id, binding_digest, provenance_digest,
      expires_at, single_use: true, revocable: true, recheck_required: true }
  | { decision: "EXPIRED", reason_code: "A3_AUTH_EXPIRED", ...,
      recheck_required: true }
  | { decision: "CANCELLED", reason_code: "A3_AUTH_REVOKED", ...,
      recheck_required: true }
```

The actual implementation should use enums rather than free strings. The safe receipt may expose only opaque decision ID, binding digest, provenance digest, policy version, categorical outcome/reason, expiry/TTL metadata, `single_use: true`, `revocable: true`, and `recheck_required: true`. It must not expose raw request IDs or raw tenant, workspace, paper-account, actor, capability, nonce, idempotency, authorization-evidence, or other account references. It must not expose material, raw payloads, prompts, strategy source, API keys, private keys, wallet seeds, provider locators, unrestricted PnL/journal details, or external order IDs.

`binding_digest` and `provenance_digest` are SHA-256 over canonical JSON with sorted keys, UTF-8 encoding, compact separators, normalized and lexicographically sorted assets, and **no derived digest fields** included in the hashed object. The digest domain must be explicit and versioned. A digest must never be treated as proof that content was captured, stored, scanned, encrypted, or replayable.

## 5. Pure A3 lifecycle

The lifecycle is a metadata state machine with no side effects:

```text
DRAFT → SUBMITTED → EVALUATED → APPROVED_FOR_FUTURE_CAPTURE
                         ├──────→ DENIED
                         ├──────→ EXPIRED
                         └──────→ CANCELLED
```

| State | Meaning | Allowed next states | Side-effect rule |
|---|---|---|---|
| `DRAFT` | Locally assembled, incomplete or editable request metadata | `SUBMITTED`, `CANCELLED` | No eligibility claim; no material access |
| `SUBMITTED` | Immutable request and evidence envelope received for evaluation | `EVALUATED`, `CANCELLED` | No activation or persistence implied |
| `EVALUATED` | Pure policy evaluation completed with a categorical result | `APPROVED_FOR_FUTURE_CAPTURE`, `DENIED`, `EXPIRED`, `CANCELLED` | Evaluation itself cannot consume authorization or create a record |
| `APPROVED_FOR_FUTURE_CAPTURE` | Exact future capture scope is eligible under a future enabled policy | `EXPIRED`, `CANCELLED` | Display-only authorization, always `recheck_required: true`; unreachable while capture is disabled |
| `DENIED` | Default-deny result with stable reason code, including `A3_CAPTURE_DISABLED` | Terminal | No retry mutation; a new request may be drafted |
| `EXPIRED` | Supplied clock shows the approval/evaluation window elapsed | Terminal | Deterministic evaluation outcome; no background transition or capture/storage/replay consequence |
| `CANCELLED` | Supplied revocation metadata shows the request/approval was revoked or cancelled | Terminal | Deterministic evaluation outcome; no background transition or repository operation |

Terminal states are non-resumable. Re-evaluation after expiry, cancellation, revocation, or consumption requires a new opaque request ID/idempotency scope and new human evidence; it must not mutate the old result. `EXPIRED` and `CANCELLED` are deterministic outcomes based only on supplied `now` and revocation metadata; A3 starts no timer, worker, callback, or background transition. `APPROVED_FOR_FUTURE_CAPTURE` must be treated as a **display and handoff eligibility state only** until a separately designed capture activation milestone exists.

A pure transition function should accept `(current_state, target_state, request_metadata, evidence, policy, now, transition_reason)` and return either a new immutable state transition or a categorical rejection. It must require explicit transition reasons, reject backward or skipped transitions, reject future timestamps and stale approvals, and never call another subsystem.

## 6. Non-interference proof

The following proof obligations are design invariants for A3 and must be tested structurally after implementation:

| Forbidden effect | Why no A3 state can perform it |
|---|---|
| Access material | A3 accepts metadata-only contracts; it has no source/raw-payload/material field and must not import `agent_os.persistence.material`. A2 remains behind its own supplier-first `prepare()` boundary. |
| Invoke A2 lease handling | A3 exposes no `MaterialLease`, `consume`, `cancel`, or coordinator dependency. The policy function has no callback or consumer handoff. |
| Activate `PAPERRUN_RECORDING_CAPTURE_V1` | The supplier is denied by A1/A2 on the baseline; A3 has no feature-flag write, activation method, or capture adapter. Eligibility is explicitly future-only. |
| Create storage | A3 has no filesystem, database, object-store, repository, migration, or event-publisher dependency. The existing A1 receipt port is protocol-only. |
| Create a manifest | A3 returns a digest-only projection, not an artifact manifest and not a material identity. No raw/canonical bytes or storage locator is accepted. |
| Create a receipt repository entry | A3 returns an in-memory categorical result only. Future persistence must be separately approved and is not part of A3. |
| Create a replay task | A3 does not import `ReplayEngine`, stream replay, worker scheduling, or task queues. `APPROVED_FOR_FUTURE_CAPTURE` does not mean replayable. |
| Create an order intent | A3 does not import `RiskCheckRequest`, `ExecutionRequest`, `AgentRiskGate`, or `PaperExecutor`; it only verifies a paper-account binding as metadata. |
| Create a paper fill | A3 cannot call `PaperExecutor.submit()` and has no ledger/fill dependency. |
| Make an external call | A3 must be standard-library-only policy code with no network, connector, wallet, exchange, payment, cloud, subprocess, or worker imports. |

The current A2 structural test pattern is the right model: enforce exact production path/import/call boundaries and forbid sensitive field/capability names (`tests/agent_os/test_persistence_security_boundaries.py:128-180`). A3 should add an equivalent AST and runtime purity test without broadening the A2 path union until implementation is separately approved.

## 7. Smallest future implementation path union

No implementation is authorized by this design. If explicitly approved later, the smallest future path union should be:

| Path | Proposed responsibility |
|---|---|
| `agent_os/policy/a3_capture.py` | Pure immutable contracts, enums, canonical binding digest, eligibility predicates, and state transitions |
| `agent_os/policy/__init__.py` | Narrow internal-only exports; raw request/evidence/evaluation types must not be used as default output, logging, API, or telemetry payloads |
| `tests/agent_os/test_a3_capture_policy.py` | Contract, lifecycle, default-deny, digest, time, idempotency, and purity tests |
| `tests/agent_os/test_a3_capture_security_boundaries.py` | AST/import/call/field surface tests proving no A2, storage, recorder, replay, execution, or external dependency |
| `docs/architecture/agent-os-a3-capture-policy.md` | Approved policy contract, lifecycle, governance decisions, non-interference proof, and future activation prerequisites |

The implementation must **not** add an API route, worker command, feature-flag mutation, storage adapter, audit repository, scanner, recorder bridge, replay loader, connector, cloud integration, or capture activation in the A3 slice. The existing A1/A2 files should remain unchanged and reused only as documented safety context, not called from A3.

## 8. Deterministic test plan and future validation

The focused tests should cover valid paper-only metadata evaluation that still returns `A3_CAPTURE_DISABLED`; every implemented binding mismatch; exact acceptance of `synthetic_fixture_metadata_v1` and rejection of all other classifications; venue and asset wildcard rejection; live/testnet rejection; non-paper connector rejection; agent/version/strategy digest drift; invalid or future timestamps; the 600-second maximum TTL and TTL overrun; workspace-owner evidence; future dual-authority vocabulary rejection when reviewer evidence is absent; revoked and consumed evidence; expired/cancelled terminal states from supplied clock/revocation metadata; invalid backward transitions; stable reason-code serialization; canonical digest ordering with UTF-8 compact JSON and no derived digest fields; opaque safe outputs; mandatory `recheck_required: true`; and safe receipt field whitelisting.

Structural tests parse the A3 production module and reject forbidden imports/calls and activation symbols. The current test slice asserts no raw identity, authorization, source, or credential-shaped values appear in safe dictionaries, safe representations, or validation errors. Broader forbidden-boundary runtime sentinels and idempotency conflict tests remain future coverage where those boundaries are introduced.

The exact future validation sequence, to be run only after separate explicit implementation approval, is:

```bash
python3 -m pytest -q tests/agent_os/test_a3_capture_policy.py tests/agent_os/test_a3_capture_security_boundaries.py
python3 -m pytest -q tests/agent_os
make lint
make typecheck
make test
git diff --check
```

The approval review must also inspect the exact changed-path union, run a secret-like value scan, verify that `PAPERRUN_RECORDING_CAPTURE_V1` remains disabled, and confirm that no recorder/replay/exchange/wallet/connector/cloud/payment/testnet/live path was executed or added. The current task did not run those runtime or validation commands because the user authorized read-only Git/source inspection only and explicitly prohibited recorder, replay, worker, API, exchange, wallet, connector, cloud, payment, testnet, and live paths.

## 9. Required approval gates before any implementation

A future implementation requires separate explicit approval for each gate:

1. **A3 contract approval:** approve exact field names, enums, canonicalization, digest domain, lifecycle, reason codes, and receipt whitelist.
2. **Governance approval:** confirm the approved authority, TTL, revocation, consumption, classification, audit, and retention decisions in Section 10; no unresolved decision may be silently filled in by implementation.
3. **Policy-only implementation approval:** approve only the five-file path union above; no runtime or persistence effects.
4. **Focused validation approval:** review deterministic tests, AST boundary tests, exact diff, secret scan, and baseline failures.
5. **Capture activation design approval:** separately design recorder integration, source/data contracts, scanner boundary, storage, encryption/KMS, manifest, receipt persistence, retention, and replay handoff.
6. **Capture activation implementation approval:** separately authorize the future flag/activation path, with human confirmation, audit persistence, revocation/consumption enforcement, and rollback. `PAPERRUN_RECORDING_CAPTURE_V1` must remain disabled until this gate passes.
7. **Replay and execution approvals:** separately authorize replay loading and any paper-account integration. Live/testnet, wallets, exchanges, payments, and external execution remain outside A3.

## 10. Approved governance decisions and residual future decisions

The following decisions are approved and are no longer open for the A3 policy-only slice. Raw request IDs remain internal correlation only and are excluded from every default decision/receipt example.

| Decision | Approved rule |
|---|---|
| Eligible classification | Exactly `synthetic_fixture_metadata_v1`; all other, missing, unknown, or future classes deny |
| Authorization authority | Workspace owner for the current synthetic metadata class; workspace owner plus designated risk/data reviewer for any future non-synthetic class |
| Approval TTL | Maximum 600 seconds (10 minutes), server-enforced in the later authority implementation |
| Approval semantics | Exact-scope, single-use, revocable, and server-enforced later; every positive result requires `recheck_required: true` |
| Target account and connector | Exactly `paper` / `paper` only |
| Capture state | `PAPERRUN_RECORDING_CAPTURE_V1` remains disabled; fully validating requests return `A3_CAPTURE_DISABLED` |
| A3 side effects | None: no storage, audit repository, feature flag, API, worker, replay, scanner, runtime, risk, execution, wallet, exchange, cloud, payment, testnet, or live behavior |
| Safe output | Opaque decision ID plus binding/provenance digests only; no request ID or raw tenant/workspace/account references |
| Binding digest | SHA-256 over canonical JSON with sorted keys, UTF-8, compact separators, normalized/sorted assets, and no derived digest fields |

Residual decisions belong to later authority, capture, storage, and governance milestones: server authentication of authority evidence; the registry designating the risk/data reviewer; exact revocation/consumption authority implementation; future classification additions; future audit persistence; retention/legal-hold/deletion ownership; and the activation review that may eventually change the disabled capture policy. None may be resolved by adding behavior to A3.

Residual implementation decisions include the server mechanism for authenticating authority evidence, the registry that designates the risk/data reviewer, the exact revocation and consumption authority implementation, whether venue and asset allowlists are global or workspace-specific, whether source digests are mandatory, whether an approval may cover multiple PaperRuns, and how future classification additions are separately approved. A3 must deny until each applicable decision is represented in a versioned policy snapshot.

## References

[1]: `agent_os/persistence/contracts.py` at `fa8f841a6a0f92144c435242a9e11a7739383d7b` — A1 immutable metadata contracts, enums, identity, provenance, artifact, scanner, and redacted receipt types.
[2]: `agent_os/persistence/ingress.py` at `fa8f841a6a0f92144c435242a9e11a7739383d7b` — A1 supplier, tenant, capability, provenance, scanner, transition, idempotency, and redaction gates.
[3]: `agent_os/persistence/material.py` at `fa8f841a6a0f92144c435242a9e11a7739383d7b` — A2 fixture-only material admission, private buffer, lease, consumption, cancellation, and disposal boundary.
[4]: `tests/agent_os/test_persistence_security_boundaries.py` and `tests/agent_os/test_persistence_material.py` at the inspected baseline — A2 structural and behavioral security tests.
[5]: `docs/architecture/agent-os-phase1.md` at the inspected baseline — Phase 1 architecture, data/runtime/risk/execution/UX boundaries, lifecycle, commands, and non-goals.
[6]: `agent_os/contracts/market.py`, `agent_os/runtime/runner.py`, `agent_os/contracts/risk.py`, `agent_os/risk/gate.py`, and `agent_os/execution/paper.py` at the inspected baseline — provenance, observation-only runtime, risk facade, and in-memory simulated-fill boundary.
[7]: `agent_os/api/app.py` and `services/agent_worker/main.py` at the inspected baseline — paper-only API/health/lock telemetry and deterministic fixture worker.
[8]: `agent_os/persistence/ports.py` and `services/market_data/streams/cli.py` at the inspected baseline — design-only receipt protocols and separate recorder/replay command surface.

A3 REPOSITORY BASELINE: VERIFIED
A3 DESIGN STATUS: READY FOR FINAL REVIEW
RECOMMENDATION: DO NOT IMPLEMENT UNTIL EXPLICIT USER APPROVAL
