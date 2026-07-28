---
name: coinscopeai-task-naming-standard
description: "Use this standard for all tasks to reduce ambiguity, avoid duplicate-looking titles, and make tasks readable even when truncated in the sidebar. This is especially important in the current CoinScopeAI workspace, where several visible task names appear repetitive and hard to distinguish at a glance."
---

# CoinScopeAI Task Naming Standard

All task titles must follow this format:

[TYPE] [AREA] — Action / Deliverable

Examples:
- [BUILD] RISK — Position Sizer v1
- [EXCHANGE] BINANCE — WebSocket Reconnect Handler
- [OPS] MARKET SCAN — Daily Run
- [DOC] OPS — Daily Market Scan Runbook
- [QA] EXECUTION — Order Lifecycle Test

## Allowed TYPE values
[BUILD], [FIX], [OPS], [DOC], [QA], [ML], [RISK], [DATA], [EXCHANGE], [UI], [RESEARCH], [INCIDENT]

## Allowed AREA values
INGEST, SENTIMENT, SIGNALS, REGIME, RISK, EXECUTION, PERF, ALERTS, DASHBOARD, REDIS, POSTGRES, BINANCE, BYBIT, OKX, HYPERLIQUID, DEVOPS, DOCS, MARKET SCAN, OPS, BILLING, PLATFORM

## Rules
1. Front-load meaning: first 3–5 words must uniquely identify the task.
2. One task = one output.
3. Do not start task titles with “How to...”
4. Use files for knowledge and runbooks; use tasks for actions and deliverables.
5. If two tasks begin with the same visible phrase in the sidebar, rename them.
6. Every task must map to a clear workstream and expected artifact.

## Templates
- [BUILD] AREA — Capability
- [FIX] AREA — Specific Failure
- [OPS] Workflow — Cadence or Date
- [DOC] AREA — Artifact Name
- [QA] AREA — Test Scope
- [ML] AREA — Model or Dataset Deliverable
- [RESEARCH] AREA — Decision Topic
- [INCIDENT] AREA — Symptom + Date
