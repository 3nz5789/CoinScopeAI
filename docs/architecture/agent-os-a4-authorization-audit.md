# CoinScopeAI Agent OS — Revised A4-v1 Design

## Final local implementation record

**Status:** A4-v1 is present on current `main` at `4bfae940d2ec373ee7c63d65819361cc8eafd41e` within the approved ten-file boundary. This document records deterministic process-local behavior; it does not claim durable persistence, crash recovery, database backing, production readiness, or authorization to deploy.

**Historical implementation record:** The earlier local baseline and uncommitted branch are retained as historical/reported provenance: `main` at `29001d119c3e21908b25432688c1e1dbf719b066` and branch `agent-os/a4-authorization-audit`.

**Approved behavior:** server-owned, tenant-scoped authorization; immutable exact-scope grants; TTL no greater than 600 seconds; terminal lifecycle `ACTIVE → CONSUMED | REVOKED | EXPIRED`; deterministic in-memory atomic semantics; monotonic tenant/workspace revocation epochs; tenant-scoped idempotency; safe replay; cross-tenant non-disclosure; append-only whitelist-redacted audit metadata.

**A3 constraint:** A3 capture remains disabled. The implemented local A4-v1 boundary cannot record, materialize, store, scan, replay, execute, call an API or worker, or touch connectors, wallets, exchanges, testnet, live, cloud, or external systems. During A4-v1 validation, worker commands, `agent-demo`, API/server startup, recorder commands, replay commands, and stream commands are explicitly prohibited.

## 1. Exact A4-v1 implementation boundary

The implemented A4-v1 boundary is exactly the following ten paths. No path outside this union is part of the implementation.

| Path | Implemented responsibility |
|---|---|
| `agent_os/persistence/authorization_contracts.py` | Immutable request, grant, decision, revocation, status, and reason-code contracts. |
| `agent_os/persistence/authorization_ports.py` | Protocol-only server-owned authority and audit interfaces. |
| `agent_os/persistence/authorization_memory.py` | Deterministic process-local authority with injectable clock and serialized mutation semantics. |
| `agent_os/persistence/audit_contracts.py` | Immutable append-only audit-event contract and closed event vocabulary. |
| `agent_os/persistence/audit_redaction.py` | Whitelist-only projections for ordinary review and security review. |
| `tests/agent_os/test_authorization_contracts.py` | Contract, canonicalization, enum, validation, and round-trip tests. |
| `tests/agent_os/test_authorization_memory.py` | State, issue, consume, revoke, expiry, replay, and failure tests. |
| `tests/agent_os/test_authorization_security_boundaries.py` | AST/import/field and no-side-effect structural tests. |
| `tests/agent_os/test_audit_redaction.py` | Audit whitelist, forbidden-field, tenant, and serialization tests. |
| `docs/architecture/agent-os-a4-authorization-audit.md` | The approved A4-v1 architecture and operational contract. |

The following are explicitly excluded from A4-v1: `authorization_relational.py`; SQLite/PostgreSQL adapters; migrations; database creation or provisioning; object storage; encryption/KMS; capture activation; A2 material handoff; scanner, replay, runtime, risk, execution, API, worker, connector, wallet, exchange, payment, cloud, testnet, live, and external operations. No existing repository file may be edited during A4-v1 implementation except the approved new documentation path above, and only after a separate implementation authorization.

## 2. Current-main compatibility anchors

A4-v1 must reuse existing vocabulary and preserve current boundaries rather than creating a second ingress or execution path.

| Existing anchor | Current-main constraint to preserve |
|---|---|
| `agent_os/persistence/contracts.py:9–20` | Existing policy/supplier vocabulary includes `TrustedSupplier.PAPERRUN_RECORDING_CAPTURE_V1`; its presence does not activate capture. |
| `agent_os/persistence/contracts.py:143–199` | `TenantContext`, `CapabilityMetadata`, and `IngressIdentity` establish tenant, actor, request, idempotency, and nonce concepts. |
| `agent_os/persistence/contracts.py:202–227` | `IngressProvenance` carries explicit policy and retention metadata without a source locator. |
| `agent_os/persistence/contracts.py:342–434` | `RedactedIngressReceipt` and `IngressReceipt.to_redacted()` establish whitelist-only safe projections. |
| `agent_os/persistence/ingress.py:187–247` | Tenant and capability validation is server-boundary vocabulary; tenant mismatch must fail closed. |
| `agent_os/persistence/ingress.py:578–638` | Binding comparison already defines tenant-scoped idempotency match/conflict and non-disclosing cross-tenant behavior. |
| `agent_os/persistence/material.py:448–526` | A2 provides the precedent for consumer-bound, single-use, expiry-aware invalidation; A4-v1 must not invoke or extend it. |
| `agent_os/policy/a3_capture.py:368–527` | A3 evaluates metadata only and returns `A3_CAPTURE_DISABLED` for otherwise-valid capture evidence. |
| `agent_os/policy/a3_capture.py:530–555` | A3 lifecycle transition helper is pure and must remain unchanged. |
| `tests/agent_os/test_persistence_security_boundaries.py:128–265` | Current persistence package is structurally prohibited from storage, network, process, and side-effecting capability calls. |

## 3. Contracts and API surfaces

The following Python-level contracts are implemented in the approved A4-v1 files. Names are intentionally scoped to those files.

### 3.1 Contract vocabulary

```text
AuthorizationStatus = ACTIVE | CONSUMED | REVOKED | EXPIRED
AuthorizationOutcome = ACCEPTED | DENIED | REPLAYED | CONFLICT
AuthorizationReason =
  INVALID_REQUEST | TENANT_SCOPE_DENIED | AUTHORITY_DENIED
  | POLICY_MISMATCH | SCOPE_MISMATCH | NOT_YET_VALID | EXPIRED
  | REVOKED | ALREADY_CONSUMED | IDEMPOTENCY_CONFLICT
  | AUTHORITY_UNAVAILABLE | AUDIT_WRITE_FAILED

AuditEventType =
  AUTH_ISSUED | AUTH_CONSUME_ACCEPTED | AUTH_CONSUME_REJECTED
  | AUTH_REVOKED | AUTH_EXPIRED | AUTH_IDEMPOTENCY_REPLAY
  | AUTH_IDEMPOTENCY_CONFLICT | AUTH_ACCESS_DENIED
```

All contracts are immutable dataclasses or closed enums. IDs are opaque validated identifiers. Digests are lowercase SHA-256 strings. Timestamps are non-negative integers supplied by the injected clock inside the authority; caller timestamps are not authoritative.

### 3.2 Proposed request and result shapes

| Contract | Required fields | Safe behavior |
|---|---|---|
| `AuthorizationScope` | `tenant_id`, `workspace_id`, `agent_id`, `agent_version`, `strategy_digest`, `paper_account_id`, `account_mode`, `connector_id`, `venue_id`, sorted `assets`, `source_kind`, `source_id`, `data_classification`, `policy_version` | Canonicalized and hashed; no raw prompt, strategy source, provider payload, material, secret, or sensitive PnL. |
| `AuthorizationIntent` | `scope`, `authority_type`, `actor_id`, `request_digest`, `idempotency_key`, `requested_at` | Input to the server-owned authority; actor and tenant are checked against server context. |
| `AuthorizationGrant` | `grant_id`, tenant/workspace binding, authority subject digest, `scope_digest`, `policy_version`, `issued_at`, `expires_at`, nonce digest, `revocation_epoch`, `status` | Internal immutable grant view; never exposes raw authority evidence. |
| `ConsumeRequest` | tenant context, `grant_id`, `scope_digest`, `policy_version`, consume idempotency key, request digest | Exact scope and policy must match; only the authority may consume. |
| `AuthorizationDecision` | `decision_id`, outcome, reason, `grant_id` or opaque decision reference, scope digest, policy version, expiry, recheck-required flag | Safe projection; no tenant/workspace/account raw identifiers in ordinary output unless a separately authorized internal view requires them. |
| `RevocationRequest` | tenant context, grant or workspace target, reason code, actor digest, request/idempotency metadata | Monotonic; cannot restore a terminal grant. |

The canonical scope digest uses sorted object keys, compact UTF-8 JSON, and normalized/sorted assets, matching `agent_os/policy/a3_capture.py:211–221` and `280–316`. Derived digests are excluded from the input being hashed. `scope_digest` binds the full scope, including `tenant_id`, `workspace_id`, `policy_version`, paper mode, paper connector, venue, assets, source, and classification.

### 3.3 Proposed protocol surface

```text
class HumanAuthorizationAuthority(Protocol):
    def issue(
        self,
        server_context: ServerAuthorizationContext,
        intent: AuthorizationIntent,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def consume(
        self,
        server_context: ServerAuthorizationContext,
        request: ConsumeRequest,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def revoke(
        self,
        server_context: ServerAuthorizationContext,
        request: RevocationRequest,
        *,
        now: int,
    ) -> AuthorizationDecision: ...

    def inspect(
        self,
        server_context: ServerAuthorizationContext,
        grant_id: str,
    ) -> RedactedAuthorizationView: ...
```

The authority is server-owned: `ServerAuthorizationContext` is created by the caller’s trusted boundary in a future integration, not reconstructed from client fields. A4-v1 does not implement authentication, API routes, or external identity providers; tests use explicit typed contexts and deterministic actors only.

The audit port is separate and metadata-only:

```text
class AppendOnlyAuditSink(Protocol):
    def append(self, event: AuditEvent) -> None: ...

    def list_redacted(
        self,
        tenant_id: str,
        *,
        workspace_id: str | None = None,
    ) -> tuple[RedactedAuditEvent, ...]: ...
```

A4-v1’s in-memory sink is process-local and bounded by test/runtime construction. It is not a durable audit store and must be labeled development-only.

## 4. Deterministic in-memory data model

`authorization_memory.py` owns an in-memory aggregate with explicit tenant partitions:

```text
MemoryAuthorizationState:
  grants: dict[(tenant_id, grant_id), AuthorizationGrant]
  issue_idempotency: dict[(tenant_id, idempotency_key), StoredDecision]
  consume_idempotency: dict[(tenant_id, grant_id, idempotency_key), StoredDecision]
  revocation_epochs: dict[(tenant_id, workspace_id | None), int]
  audit_events: list[AuditEvent]
  next_sequence: dict[tenant_id, int]
```

The implementation uses an injected deterministic clock and one in-process lock or equivalent serialized critical section for all grant-state, epoch, idempotency, and audit mutations. The state is process-local, non-durable, non-exportable except through redacted views, and never accepts raw material or credentials.

Issue validates the server context, exact scope, policy version, authority role, TTL, and idempotency. It computes a new expiry no later than `issued_at + 600` seconds. The server-owned authority, not the caller, supplies the actual issue time and initial revocation epoch.

## 5. Atomic consume and revoke semantics in memory

A4-v1 emulates atomicity by holding the same critical section across validation, conditional state transition, idempotency write, audit append, and return-value capture. No callback, network call, filesystem write, or user code is invoked while mutating state.

| Operation | Ordered critical-section behavior |
|---|---|
| Issue | Validate tenant/context → canonicalize scope → check idempotency → verify role/policy/TTL → create `ACTIVE` grant → append `AUTH_ISSUED` → store decision → return only after all steps succeed. |
| Consume | Check tenant and consume-idempotency key → exact grant/scope/policy match → compare injected `now` and current epoch → require `ACTIVE` → set `CONSUMED` → append accepted event → store replay result → return. |
| Revoke | Check tenant/idempotency → locate grant without cross-tenant disclosure → increment applicable epoch → set `REVOKED` if active → append `AUTH_REVOKED` → store result → return. |
| Expiry | At each issue/consume/inspect operation, if `now >= expires_at`, transition `ACTIVE → EXPIRED` and append one `AUTH_EXPIRED` event. Expiry is terminal and cannot be reversed. |

If audit append fails, the entire in-memory mutation is rolled back to the pre-operation snapshot and returns `AUDIT_WRITE_FAILED`. A4-v1’s test sink may inject this failure. A successful consume or revoke is therefore never returned without its corresponding audit event.

Consume and revoke on the same active grant are serialized by the same lock. The operation that enters the critical section first wins; the other observes `CONSUMED` or `REVOKED`. This is deterministic for a given scheduling order and does not claim wall-clock ordering.

Revocation epochs are monotonic per tenant/workspace key. A grant records the issue epoch. Consume requires the current epoch to equal the grant’s recorded epoch. Epoch increments are never decremented, and a revoked or expired grant is never reactivated; a new authorization must be issued.

### 5.1 Explicit transition table

| Operation | Preconditions | State/epoch mutation | Audit mutation | Safe result |
|---|---|---|---|---|
| Issue new | Valid server context, exact scope, approved authority, TTL 1–600, no conflicting idempotency record | Create `ACTIVE` grant at current epoch | Append `AUTH_ISSUED` | `ACCEPTED` |
| Issue replay | Same tenant, operation, idempotency key, request digest, scope digest, and policy version as a committed issue | None | None | Original decision as `REPLAYED` |
| Issue conflict | Same tenant/idempotency key with any changed request, scope, or policy digest | None | Append only if the design elects to audit the rejected attempt; never mutate grant | `CONFLICT` / `IDEMPOTENCY_CONFLICT` |
| Consume accepted | Grant is `ACTIVE`, exact scope/policy match, `now < expires_at`, current epoch equals issue epoch | `ACTIVE → CONSUMED` | Append exactly one `AUTH_CONSUME_ACCEPTED` | `ACCEPTED` |
| Consume replay | Same tenant/grant/consume idempotency key and identical request digest as committed consume | None | None | Original decision as `REPLAYED` |
| Consume duplicate | Grant is already `CONSUMED` and consume key differs | None | Append `AUTH_CONSUME_REJECTED` if rejection auditing is enabled | `DENIED / ALREADY_CONSUMED` |
| Expire | Grant is `ACTIVE` and `now ≥ expires_at` during issue, consume, or inspect | `ACTIVE → EXPIRED` | Append exactly one `AUTH_EXPIRED` | `DENIED / EXPIRED` |
| Revoke active | Authorized server context and grant is `ACTIVE` | Increment applicable epoch and set `ACTIVE → REVOKED` | Append exactly one `AUTH_REVOKED` | `ACCEPTED` |
| Revoke terminal | Grant is `CONSUMED`, `REVOKED`, or `EXPIRED` | None; epoch policy must be explicit and must not reopen grant | Append a bounded rejected-revocation event only if configured | Terminal denial |
| Any audit failure | Any operation that would mutate grant, epoch, or idempotency state | Roll back all operation state | No partial event remains in the in-memory aggregate | `DENIED / AUDIT_WRITE_FAILED` |

The consume/revoke race is serialized by the same critical section. Exactly one terminal transition wins; the other reads the terminal state. The audit event and idempotency result belong to the winning operation only. No transition invokes A3, A2, a recorder, a scanner, replay, runtime, execution, API, worker, or external code.

## 6. Idempotency and cross-tenant behavior

Issue replay requires the same tenant, operation, idempotency key, canonical request digest, policy version, and scope digest. The same tuple returns the original safe decision with outcome `REPLAYED`; a changed digest, scope, policy, or operation returns `IDEMPOTENCY_CONFLICT`.

Consume replay requires the same tenant, grant, scope digest, policy version, consume idempotency key, and request digest. A committed accepted consume replays the original decision without another state transition or audit event. A different consume key after commitment returns `ALREADY_CONSUMED`.

All state maps are keyed with tenant identity. A request from another tenant receives a generic `TENANT_SCOPE_DENIED` or `AUTHORITY_DENIED` result and cannot distinguish absent, active, consumed, revoked, or expired records belonging to another tenant. No cross-tenant audit event is returned.

## 7. Audit contracts and redaction schema

`audit_contracts.py` defines an immutable `AuditEvent` containing only bounded metadata:

| Field | A4-v1 rule |
|---|---|
| `event_id` | Opaque deterministic/test-safe ID; unique within the in-memory instance. |
| `tenant_id` / `workspace_id` | Internal isolation fields; omitted from ordinary public projection. |
| `event_type` / `event_version` | Closed enum and integer schema version. |
| `occurred_at` / `sequence` | Injected-clock time and tenant-scoped monotonic sequence. |
| `actor_digest` | Digest or opaque principal reference, never raw credentials or identity evidence. |
| `grant_id` | Opaque authorization lineage ID. |
| `request_digest` / `scope_digest` | SHA-256 digests only. |
| `policy_version` / `revocation_epoch` | Binding and governance metadata. |
| `outcome` / `reason_code` | Closed values; no free-form sensitive reason. |
| `event_digest` | Optional deterministic integrity digest over the event fields; not encryption. |

`audit_redaction.py` exposes `redact_audit_event(event)` and returns a whitelist-only `RedactedAuditEvent`. The ordinary view contains event ID, type/version, time, sequence, outcome, reason, policy version, scope digest, and bounded expiry/epoch metadata. It never contains raw prompt, strategy source, provider payload, artifact bytes, material, API key, wallet key, seed phrase, exchange credential, sensitive PnL, or unrestricted journal data. Any unknown field or serialization failure is rejected rather than passed through.

## 8. Concurrency, security, and audit tests

The exact approved test files should cover the following without invoking any excluded subsystem:

| Test file | Required cases |
|---|---|
| `test_authorization_contracts.py` | Enum closure; immutable contracts; valid/invalid identifiers and digests; canonical scope ordering; duplicate/wildcard asset rejection; TTL ≤ 600; policy-version and exact-scope digest binding; serialization round trips. |
| `test_authorization_memory.py` | Issue success; issue replay; idempotency conflict; consume once; consume replay; second-key duplicate denial; expiry; revoke; epoch increment; terminal-state rejection; wrong tenant; wrong workspace; wrong scope; wrong policy; audit failure rollback; deterministic injected-clock output. |
| `test_authorization_security_boundaries.py` | Approved production-path list; standard-library/relative imports only; no network, storage, subprocess, crypto-service, cloud, connector, wallet, exchange, API, worker, or capture calls; no raw-material/secret/sensitive-PnL fields; protocol-only port declarations where required. |
| `test_audit_redaction.py` | Exact whitelist; forbidden-field omission; malformed event rejection; stable redacted serialization; tenant-filtered listing; no raw authority evidence; append-only sequence behavior; duplicate append rejection. |

Concurrency tests should coordinate two threads or deterministic barriers against one active grant and assert exactly one accepted consume, one terminal state, one accepted-consume audit event, and no duplicate position/material/external side effect. A consume/revoke race should assert one terminal winner and a safe terminal denial for the loser. A replay test should assert byte-equivalent safe decisions and unchanged event count.

## 9. Validation evidence

The implemented A4-v1 was validated locally from `/home/ubuntu/readonly-clones/CoinScopeAI-A4-impl-20260825T130952Z` using the approved isolated validation environment. The following evidence does not authorize commit or execution outside the stated local validation boundary.

Recorded validation results:

| Check | Result |
|---|---|
| Focused A4-v1 tests | 28 passed |
| Full `tests/agent_os` | 204 passed |
| Ruff | Passed |
| Black check | Passed |
| mypy | Passed |
| `make lint` | Passed |
| `make typecheck` | Passed |
| `git diff --check` | Passed |
| Exact ten-path audit | Passed |
| Protected-path audit | Passed |
| Credential-shaped scan | Passed |
| Prohibited-capability scan | Passed |
| Broad `make test` | Blocked during unrelated wider-suite collection because `tests/test_coinscopeai.py` imports NumPy; NumPy was intentionally not installed because it is outside the approved minimal local tooling environment. This is an environment limitation outside the A4-v1 path union, not an A4-v1 implementation regression. |

```bash
cd /home/ubuntu/readonly-clones/CoinScopeAI-A4-impl-20260825T130952Z
python3 -m pytest -q \
  tests/agent_os/test_authorization_contracts.py \
  tests/agent_os/test_authorization_memory.py \
  tests/agent_os/test_authorization_security_boundaries.py \
  tests/agent_os/test_audit_redaction.py
python3 -m pytest -q tests/agent_os
make lint
make typecheck
make test
git diff --check
git status --short
```

The expected safety result is that tests remain metadata-only and no command enables capture or invokes recorder, scanner, replay, runtime, risk, execution, API, worker, connector, wallet, exchange, testnet, live, cloud, or external behavior. A4-v1 validation must not run `make worker`, `make agent-demo`, `make dev-all`, any API/server startup, `make replay`, any recorder or stream command, or any equivalent worker, agent-demo, server, recorder, replay, or stream entry point. Any missing future file should be reported as a not-yet-implemented baseline, not worked around by editing unrelated paths.

## 10. Separate A4-B proposal: relational persistence and migrations

A4-B is a separate future design and implementation gate. It is not part of A4-v1 and must not be implemented under this approval.

| A4-B area | Proposal requiring separate approval |
|---|---|
| Relational adapter | Add `authorization_relational.py` or an approved repository-layer location; preserve the A4-v1 ports and result semantics. |
| Schema | Tables for grants, issue/consume idempotency, revocation epochs, and append-only audit events, each tenant-keyed with immutable decision facts. |
| Isolation | Server-owned tenant context, row-level security or equivalent database-enforced predicates, role separation for tenant operators, compliance reviewers, retention administrators, and future key administrators. |
| Atomicity | Transactional conditional update/row lock for consume and revoke; audit append in the same transaction; database/server time; unique constraints for idempotency and event sequence. |
| Migration | Versioned migration with preflight, rollback/forward-repair plan, invariant checks, dual-read/dual-write decision, and no artifact bytes. Migration approval must be separate from adapter approval. |
| Retention | Approved retention classes, legal-hold table/state, deletion/tombstone policy, audit access logging, and no in-place rewrite of immutable decision facts. |
| Recovery | Backup/restore, epoch monotonicity verification, duplicate replay recovery, audit-gap detection, and database-unavailable fail-closed behavior. |
| Operations | Deployment, credentials, secrets, monitoring, alerting, and production change window; none are authorized by A4-v1. |

A4-B must also separately decide whether object-store references are introduced. If approved, object storage remains physically and logically separate from authorization/audit metadata, with its own artifact, integrity, encryption/KMS, retention, legal-hold, deletion, and replay-handoff gates.

## 11. Final implementation gate

A4-v1 is implemented locally and remains limited to the ten approved paths. It does not alter A3 and preserves `PAPERRUN_RECORDING_CAPTURE_V1` as disabled. Relational persistence, migrations, and every capability listed in the deferrals remain outside A4-v1. A4-B requires a new approval request and must not be inferred from A4-v1. The worktree remains uncommitted; commit, push, and PR actions require separate explicit approval.

## References

[1]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/agent_os/persistence/contracts.py "Current-main A1 persistence contracts"
[2]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/agent_os/persistence/ingress.py "Current-main A1 ingress validation and idempotency"
[3]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/agent_os/persistence/material.py "Current-main A2 private material boundary"
[4]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/agent_os/policy/a3_capture.py "Current-main A3 policy-only capture evaluator"
[5]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/docs/architecture/agent-os-a3-capture-policy.md "Current-main A3 architecture policy"
[6]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/tests/agent_os/test_persistence_security_boundaries.py "Current-main persistence security boundary tests"
[7]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/tests/agent_os/test_persistence_ingress.py "Current-main ingress behavior tests"
[8]: https://github.com/3nz5789/CoinScopeAI/blob/29001d119c3e21908b25432688c1e1dbf719b066/tests/agent_os/test_persistence_material.py "Current-main A2 material behavior tests"

A4-v1 IMPLEMENTATION STATUS: COMPLETE LOCALLY
COMMIT/PUSH/PR STATUS: NOT AUTHORIZED
