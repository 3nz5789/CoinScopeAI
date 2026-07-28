# Phase 1 Backlog — Strategic Foundation

## Phase 1 scope

**Strategic foundation** — confirm and harden the load-bearing assumptions of the business plan so that subsequent phases can build on a defensible base. Heavy emphasis on market clarity, ICP confirmation, positioning consistency, product hardening, and the trust + risk posture that defines CoinScopeAI's category claim.

**Time horizon:** ~30 days (immediate, dependency-light work).

**Phase exit criteria:**

- ICP and positioning audited against current operating reality.
- Risk posture (PCC v2, §8 Capital Cap, kill-switch transparency) verified across surfaces.
- Replay corpus and runbook coverage at launch-readiness thresholds.
- Public claims discipline locked.

---

## Section A — Market and ICP confirmation

**[RESEARCH] MARKET — Validate addressable market thesis against current crypto-derivatives data**
- Objective: revisit `03-market-thesis` claims against current third-party market data (CoinGlass, exchange volume reports).
- Why it matters: anchors revenue ceiling logic and pricing defensibility.
- Dependency: access to current market-volume data.
- Expected output: refreshed memo with citations, in `03-market-thesis` notes.

**[RESEARCH] ICP — Re-validate Omar primary persona against validation cohort behavior**
- Objective: confirm or adjust primary-ICP framing based on cohort evidence to date.
- Why it matters: A-01 in decision register; informs activation flow priorities.
- Dependency: validation cohort behavior data.
- Expected output: persona-validation memo; any adjustments logged.

**[RESEARCH] ICP — Audit cohort heterogeneity across Omar / Karim**
- Objective: confirm cohort represents both primary and secondary personas.
- Why it matters: cohort representativeness for P1 readiness decisions.
- Dependency: cohort persona-tagging.
- Expected output: persona breakdown report.

---

## Section B — Positioning and brand voice consistency

**[DOC] POSITIONING — Audit positioning consistency across every public surface**
- Objective: confirm "Institutional-grade quant trading for individuals + funds" appears consistently and is not diluted to "AI trading bot" or similar drift.
- Why it matters: positioning drift = trust drift.
- Dependency: surface inventory.
- Expected output: surface checklist with corrections applied.

**[DOC] BRAND — Audit disclosure language ("Testnet only. 30-day validation phase. No real capital.")**
- Objective: confirm the canonical phrase appears consistently on every prospect-reachable surface.
- Why it matters: trust-readiness gate; drift here is invisible until incident.
- Dependency: list of public surfaces.
- Expected output: surface-by-surface checklist; corrections applied.

**[DOC] BRAND — Lock public-claims posture (no performance references in marketing)**
- Objective: codify the rule + rationale + examples in one document.
- Why it matters: regulatory and reputational tail; cross-ref `decision-rights.md` §6.
- Dependency: C-03.
- Expected output: brand-voice memo committed.

---

## Section C — Product hardening and risk posture

**[RISK] RISK — Audit PCC v2 G3 stability and start (or restart) the 30-day clock**
- Objective: confirm G3 readiness with consecutive-day count visible.
- Why it matters: gates everything downstream; first item in 30-60-90 plan.
- Dependency: engine telemetry trailing 30 days.
- Expected output: dated G3-state log.

**[BUILD] PRODUCT — Expand replay days corpus to ≥20 historical days**
- Objective: hit the launch-readiness threshold with regression-test pass.
- Why it matters: M2 launch-readiness gate.
- Dependency: replay tooling; engine repo CI.
- Expected output: 20+ replay days passing in CI.

**[QA] RISK — Audit kill-switch trips for unexplained / un-root-caused events**
- Objective: confirm zero unexplained trips in trailing 14 days.
- Why it matters: prerequisite to claiming engine stability.
- Dependency: trip log review.
- Expected output: audit memo; remediation tasks if any unexplained trips found.

**[OPS] RISK — Confirm real-capital authorization default = NO across all surfaces**
- Objective: ensure no surface implies otherwise.
- Why it matters: single most consequential default.
- Dependency: surface audit.
- Expected output: confirmation log.

---

## Section D — Trust readiness baseline

**[DOC] TRUST — Audit runbook coverage to ≥80% of likely incident classes**
- Objective: identify gaps; close the top 5 highest-likelihood ones.
- Why it matters: trust-readiness gate for M2.
- Dependency: incident-class taxonomy.
- Expected output: coverage % logged; gap list with owners.

**[OPS] OPERATIONS — Verify connector-health 100% green for trailing 14 days**
- Objective: confirm operational readiness.
- Why it matters: launch-readiness criterion.
- Dependency: `coinscope-connector-health` artifact.
- Expected output: 14-day green log.

**[QA] OPERATIONS — Verify backups + restore test within trailing 30 days**
- Objective: confirm a restore actually works, not just that backups run.
- Why it matters: launch-readiness criterion.
- Dependency: backup tooling; non-prod environment.
- Expected output: restore-test log.

**[QA] OPERATIONS — Audit monitoring coverage to ≥90% of critical paths**
- Objective: identify and close monitoring gaps.
- Why it matters: launch-readiness criterion.
- Dependency: critical-path inventory.
- Expected output: coverage report; alerts added where missing.

---

## Section E — Validation cohort completion

**[METRICS] METRICS — Track validation cohort 30-day completion rate**
- Objective: produce the QD-01 measurement.
- Why it matters: M1 milestone input; gates P1 readiness.
- Dependency: cohort tracking infrastructure.
- Expected output: completion % memo; per-user audit.

**[QA] PRODUCT — Run pre-mortem on P1 narrow-ship plan**
- Objective: surface failure modes before commitment.
- Why it matters: pre-mortem is mandatory before canonical risk/PCC change.
- Dependency: pre-mortem skill memory; 30-60-90 plan.
- Expected output: pre-mortem doc; top-5 risks captured.

---

## Phase 1 sequencing

```
Section C tasks (PCC v2 audit, replay corpus, kill-switch audit)
        │
        ▼
Section D tasks (runbook coverage, connector-health, backups, monitoring)
        │
        ▼
Section E tasks (cohort completion measurement, pre-mortem)
        │
        ▼
Section A + B tasks (in parallel — market/ICP/positioning audits)
```

**Critical path:** Section C → D → E. Sections A and B run in parallel and don't gate phase exit.

## Phase 1 exit gate

Phase 1 is complete when:

- [ ] PCC v2 G3 30-day clock running with ≥10 consecutive stable days.
- [ ] Replay corpus ≥20 days passing.
- [ ] Runbook coverage ≥80%.
- [ ] Connector-health green for ≥14 days.
- [ ] Backups verified.
- [ ] Monitoring ≥90%.
- [ ] Validation cohort completion measured.
- [ ] Pre-mortem complete.
- [ ] Disclosure language consistent across all surfaces.
- [ ] Public-claims posture documented.

If any of these fail, do not proceed to Phase 2 — re-baseline within Phase 1.
