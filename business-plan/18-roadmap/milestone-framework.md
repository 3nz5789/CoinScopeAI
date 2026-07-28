# Milestone Framework

## 1. Why we frame milestones explicitly

A milestone framework prevents the most common roadmap failure mode: **declaring something done when it isn't.** Every milestone in CoinScopeAI's roadmap has explicit gate criteria. If those criteria aren't met, the milestone isn't reached, regardless of how the calendar reads.

Milestones are categorized into four readiness families:

1. **Launch readiness** — can we ship?
2. **Trust readiness** — should we ship at the trust level we're claiming?
3. **Monetization readiness** — can we charge?
4. **Support / ops readiness** — can we operate this safely after shipping?

A phase transition (P0→P1, P1→P2, etc.) requires all four families to clear. Skipping any one family is how trust posture quietly degrades.

## 2. Strategic milestones (top-level)

Aligned with `06-product-strategy` phase map:

| Milestone | Phase | Definition | Canonical date target |
|---|---|---|---|
| **M1 — Validation cohort completion** | P0 close | ≥70% of validation cohort completes 30-day window with no incident-driven termination | Late May / early Jun 2026 |
| **M2 — P1 narrow-ship** | P1 entry | Trader $79/mo SKU live with first defensible paid customer flow | Jun–Jul 2026 |
| **M3 — P1 stabilization** | P1 close | First paid cohort D30 retention in band; refund rate <2% MRR; no P1 incidents | Aug 2026 |
| **M4 — P2 vendor expansion** | P2 entry | Bybit integration shipped + at least one additional data feed | Aug–Sep 2026 |
| **M5 — Desk Preview activation** | P2 mid | Desk Preview $399/mo SKU live with first paid customer | Sep–Oct 2026 |
| **M6 — P3 scale + first FT hire** | P3 entry | First full-time hire onboarded; KPI ownership transition complete | Late 2026 / early 2027 |
| **M7 — Compliance posture upgrade** | P3 mid | Audit-grade exports, role-based access scaffolding, DPA refresh | Q1 2027 |
| **M8 — Desk Full v2 launch** | P5 entry | Per-seat economics live; first multi-seat customer | Mar–May 2027 |
| **M9 — Real-capital authorization** | Independent of phase | §8 Capital Cap criteria fully met; explicit founder authorization | Not date-driven; criteria-driven |

**Ordering:** M1 → M2 → M3 → M4 → M5 → M6 → M7 → M8. M9 floats; it has no calendar slot. M9 is not assumed for any monetization milestone.

## 3. Launch readiness milestones

What must be true to ship anything user-facing.

| Criterion | Required for | Validation |
|---|---|---|
| Engine telemetry stable for ≥10 days | M2 | No unexplained kill-switch trips, no drift events, no rollback events |
| Replay days corpus ≥20 historical days | M2 | All replay days pass regression tests |
| Connector-health 100% green for ≥14 days | M2 | `coinscope-connector-health` artifact |
| Backups verified within trailing 30 days | M2 | Manual restore test |
| Monitoring coverage ≥90% on critical paths | M2 | Manual audit |
| Deploy failure rate ≤10% | M2 | CI logs |
| Stripe end-to-end tested (signup, billing, refund flow) | M2 | Test transactions in MENA + global EN currencies |
| Public disclosure language consistent across surfaces | M2 | Cross-surface audit |

**Failure mode:** declaring launch-ready while one or more above are absent. This is the most common and most damaging roadmap mistake at our stage.

## 4. Trust readiness milestones

What must be true at the trust level before claiming a launch.

| Criterion | Required for | Validation |
|---|---|---|
| PCC v2 G3 stable for ≥30 days | M2 | Engine logs |
| Risk Gate visible in user-facing surfaces | M2 | UI audit |
| Kill-switch trip transparency: every trip explainable in user-facing language | M2 | Trip log review |
| Override events logged and reviewable | M2 | Engine telemetry + user dashboard |
| Refund/credit playbook published internally | M2 | Document review |
| Disclosure language: "Testnet only. 30-day validation phase. No real capital." consistent on every surface | M2 | Surface audit |
| Trust Ops contractor *or* explicit deferral with reason | M3 | Hire decision logged |
| First incident postmortem complete (or "none" explicitly logged) | M3 | Incident log |
| Public-facing transparency artifact decision made | M3 | Decision-log entry |

**Failure mode:** trust readiness collapsed into launch readiness. They are separate. A product can be launch-ready and not trust-ready. The reverse is rare but possible.

## 5. Monetization readiness milestones

What must be true before charging any user.

| Criterion | Required for | Validation |
|---|---|---|
| All Launch readiness criteria met | M2 | §3 above |
| All Trust readiness criteria met for the relevant tier | M2 (Trader), M5 (Preview), M8 (Full v2) | §4 above |
| Tier configured in Stripe with correct currencies | M2 | Stripe config audit |
| Refund/credit playbook published (Trader-scope at M2; multi-tier at M5; Desk Full v2-scope at M8) | M2/M5/M8 | Playbook review |
| Bookkeeping contractor active OR explicit defer | M3 | Role activation |
| Vendor cost / revenue measured and within target band | M3 | First month of bills |
| Cohort retention measured for the prior cohort | M5 (uses M3's cohort), M8 (uses M5's cohort) | Cohort data |
| Tier cannibalization risk analyzed for new tier | M5 (Preview vs Trader), M8 (Full v2 vs Preview) | Mix-shift analysis |

**Tier-by-tier rule:** each tier's monetization readiness depends on the prior tier's stability. M5 cannot launch on M2's readiness alone — it requires M3's cohort data.

**Failure mode:** activating a higher tier before validating the lower tier's monetization. This is how the financial framework becomes a fiction.

## 6. Support / ops readiness milestones

What must be true to operate the product safely after launch.

| Criterion | Required for | Validation |
|---|---|---|
| Runbook coverage ≥80% by M2; ≥90% by M4 | M2, M4 | Manual audit |
| TTFR <4 hours (business hours) consistently for ≥4 weeks | M3 | Support tool logs |
| Support tickets categorized + tagged consistently | M3 | Tagging audit |
| Connector-health artifact running daily | M2 | Artifact ops |
| Vendor budget alarms live (50/80/100%) | M2 | Vendor dashboards |
| Backup-restore test passing | M2 | Manual test |
| Incident comms stand-in nominated (in case of founder unavailability) | M3 | Decision-log entry |
| Decision-log discipline maintained for ≥4 consecutive weeks | M3 | `21-decision-log` |
| Weekly review cadence stable for ≥4 weeks | M3 | Review log |
| Monthly exec review held with full template | M3 | Review log |

**Failure mode:** treating ops readiness as "we'll harden it after launch." Hardening after a paid customer is in the system is materially harder than hardening before.

## 7. Roadmap gate criteria

A phase transition fires only when all of these are true:

| Gate | Required for | Source |
|---|---|---|
| **PCC v2 G3** | P0 → P1 | `14-risk-compliance-and-safeguards` |
| **PCC v2 G4** | P1 → P2 (in some scenarios) | `14-risk-compliance-and-safeguards` |
| **§8 Capital Cap status** | All phases — must be explicitly reviewed | `14-risk-compliance-and-safeguards` |
| **Cohort retention defensible** | P1 → P2 | First cohort D30 + D60 measurements |
| **Trust Ops activated or deferred with reason** | P1 → P2 | Decision log |
| **Vendor cost shape understood** | P1 → P2 | First full month of bills |
| **No outstanding P1 incidents without postmortem** | All transitions | Incident log |
| **Decision-log up to date** | All transitions | `21-decision-log` |

**Forward-only rule:** phase transitions move forward by default once gates are met. Backward movement (e.g., P1 → P0 because of a stability issue) is allowed and explicitly defined as a process step, not a failure. Backward movement requires a decision-log entry naming the trigger and the criteria for forward re-attempt.

## 8. Milestone review logic

| Cadence | What's reviewed |
|---|---|
| Weekly | Slippage on any active milestone in the 90-day window |
| Monthly | Full milestone status across the active phase |
| Phase-transition | All four readiness families reviewed against gate criteria |
| Quarterly | Strategic milestone re-evaluation — should any be redefined or deferred? |

**Reviewer:** Founder, with Trust Ops and Engineering contractors when active.

**Output of milestone review:**

- Status per milestone: not started / in flight / complete / blocked.
- Any milestone slipped → cause + revised target + decision-log entry.
- Any milestone declared complete → criteria validation evidence in the log.
- Any new dependency surfaced → updated in `dependency-map.md`.

## 9. Milestone inflation to avoid

Milestone inflation = declaring milestones reached on weaker evidence than the criteria require. It is the most common roadmap pathology and the hardest to catch in real time.

| Inflation pattern | Why it's tempting | Why it kills CoinScopeAI |
|---|---|---|
| **"PCC v2 G3 mostly stable"** | Pressure to ship; calendar deadline approaching | "Mostly" is not a state; the engine either is or isn't |
| **"Replay days mostly green"** | One failing replay day feels minor | The failing day is exactly the case the corpus exists to catch |
| **"Trust Ops effectively covered"** | Founder is doing it, so technically covered | "Founder doing it" is a known unsustainable state, not a coverage milestone |
| **"Refund playbook in progress"** | Nothing has gone wrong yet | The playbook exists *for* the moment something goes wrong |
| **"Real-capital authorization is on the roadmap"** | Stakeholders push for it | Real-capital authorization is not on the roadmap. It is on the gate. There is no calendar slot. |
| **"Desk Full v2 in beta"** | Showing capability to fund prospects | Desk Full v2 launches at P5 with per-seat economics; "beta" before that misframes the SKU |
| **"Compliance scope locked"** | Sounds reassuring | Compliance scope is dynamic per jurisdiction; "locked" implies a static reality that doesn't exist |
| **"Annual prepay introduced"** | Cash benefit | Annual prepay before G4 stable creates refund-wave exposure |
| **"First fund customer signed"** | Revenue legitimacy | A fund customer signed before per-seat features exist is a support burden, not a milestone |
| **"NSM trending positive"** | Reads well in a deck | NSM trend over a few weeks is noise; trend over a quarter is signal |

**Discipline:** if a milestone summary uses words like "mostly," "effectively," "in progress" where the criteria call for binary "met / not met," that is milestone inflation. Re-write or re-evaluate.

## 10. The single milestone rule that matters most

**A milestone is not reached until all four readiness families clear.** Launch + Trust + Monetization + Support/Ops, all four, with criteria documented and validation evidence logged.

If only three clear, the milestone is in flight, not complete. The fourth doesn't catch up later — it's the one that fails first when stress arrives.
