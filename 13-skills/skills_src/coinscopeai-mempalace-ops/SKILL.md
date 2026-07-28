---
name: coinscopeai-mempalace-ops
description: MemPalace Operations for Scoopy. Use this skill to understand the wing taxonomy, hall types, storage rules, query patterns, CLI commands, session start protocol, async writes, and retention policies for the MemPalace system.
---

# MemPalace Operations for Scoopy

This document outlines the operational procedures for Scoopy's interaction with the MemPalace system.

## Wing Taxonomy
The MemPalace system uses a single ChromaDB collection (`mempalace_drawers`) organized into specialized wings:
- `wing_project`: Confirmed decisions, milestones, lessons (Permanent)
- `wing_user`: User identity, preferences, feedback (Permanent)
- `wing_agents`: Subtask outcomes, agent facts, discoveries (Permanent)
- `wing_assets`: Dashboard URLs, repos, API keys, Stripe config (Permanent)
- `wing_dev`: Architecture decisions, conventions, bug fixes (Permanent)
- `wing_agent`: Cross-agent shared context, task outcomes (180 days)
- `wing_system`: Engine lifecycle, config changes, deployments (180 days)
- `wing_models`: ML training runs, param changes, snapshots (180 days)
- `wing_trading`: Trade signals, entries, exits, analysis (90 days)
- `wing_risk`: Risk gate checks, drawdowns, kill switch (90 days)
- `wing_scanner`: Pattern setups, performance, configs (90 days)

## Hall Types
Data within wings is further categorized into halls:
- `hall_facts`: Confirmed decisions, specs, and user preferences.
- `hall_events`: Subtask outcomes, deployments, and system lifecycle events.
- `hall_discoveries`: Lessons learned, architectural choices, and bug fixes.

## Storage Rules
The following rules dictate where specific types of information are stored:
- **Decisions:** `hall_facts`
- **Outcomes:** `hall_events`
- **Lessons:** `hall_discoveries`

## Query Patterns
MemPalace supports various query patterns to retrieve context:
- **By Wing:** Filter results to a specific wing (e.g., `wing_project`).
- **By Keyword:** Search for specific terms within the stored content.
- **By Time Range:** Retrieve events or decisions within a specific timeframe.

## CLI Commands
The primary interface for MemPalace operations is the `scoopy_cli.py` script:
- `python -m memory search`: Retrieve context based on keywords, wings, and rooms.
- `python -m memory store`: Add new facts, events, or decisions to the system.
- `python -m memory prune`: Execute the weekly or monthly maintenance routines.

## Session Start Protocol
Every new session must begin with a mandatory memory load sequence:
1. **Wake-up:** Load L0 (Identity) and L1 (Essential Story) context.
2. **Query L2/L3:** Retrieve active project phase, recent decisions, open tasks, user preferences, and asset inventory.
3. **Check Health:** Verify the memory system status and pending event queue.

## Async Writes and Batching
All `add` commands are non-blocking. Writes are enqueued to a background writer thread and batched:
- **Flush Interval:** Every 5 seconds or 50 events.
- **Idempotency:** Filing the same content twice is a safe no-op, updating the existing drawer.

## Retention Policies
MemPalace enforces automated pruning based on the wing's retention policy:
- **Permanent:** `wing_project`, `wing_user`, `wing_agents`, `wing_assets`, `wing_dev`
- **180 Days:** `wing_agent`, `wing_system`, `wing_models`
- **90 Days:** `wing_trading`, `wing_risk`, `wing_scanner`
- **Exempt Rooms:** `lessons`, `architecture`, `conventions`, `knowledge` are never pruned, regardless of the wing's retention policy.
