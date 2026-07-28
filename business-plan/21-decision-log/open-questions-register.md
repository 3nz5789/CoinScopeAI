# Open Questions Register

## How to read this register

Open questions are **upstream** of decisions. A question moves to the Leadership Decision Register only once it has enough evidence to choose between options. Until then, it sits here with:

- **Question:** the question itself, sharply phrased.
- **Why it matters:** the cost of leaving it unanswered.
- **Decision affected:** which row in `leadership-decision-register.md` it unblocks.
- **Who answers:** owner (sometimes single, sometimes "data + owner").
- **Evidence / input needed:** what would let this question close.
- **Urgency:** `High` (this 90 days), `Medium` (next 90 days), `Low` (later phase).
- **Status:** `OPEN` / `IN REVIEW` / `ANSWERED` / `DEFERRED`.

Today's date for urgency anchoring: **2026-05-08**.

---

## A. Product maturity

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QA-01 | What is the current PCC v2 G3 state, and how many consecutive stable days does it have? | Anchors P1 narrow-ship timing; gates the entire 30-60-90 plan | H-01 (P1 ship date) | Founder + Engineering | Engine telemetry trailing 30 days | High | OPEN |
| QA-02 | Are there unexplained kill-switch trips in the last 14 days that are not yet root-caused? | Unexplained trips block claims of stability | H-01 | Founder | Trip log review | High | OPEN |
| QA-03 | Is the replay days corpus at the ≥20 minimum and currently passing all regression tests? | Replay corpus gates launch readiness | M2 launch readiness | Founder + Engineering | Engine repo CI status | High | OPEN |
| QA-04 | Are runbooks at ≥80% coverage of likely incident classes? | Trust readiness gate for M2 | C-04, M2 trust readiness | Founder | Manual audit | High | OPEN |
| QA-05 | Has the activation flow (`12-onboarding-and-activation`) been measured against real cohort data, or only against assumption? | Lock activation definition only on real data | D-01 | Founder | Cohort analytics | High | OPEN |

---

## B. Pricing validation

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QB-01 | Will validation cohort users convert to Trader $79/mo at the upper or lower end of the 1–7% conversion band? | Unknown until first cohort runs; load-bearing for monetization thesis | F-04, H-01 | Founder + cohort data | First paid cohort over 30 days | High | OPEN |
| QB-02 | Is the price gap Trader $79 → Desk Preview $399 too wide (cannibalizing) or too narrow (collapsing)? | Determines whether Preview is a real bridge SKU | B-02 | Founder + early Trader feedback | First 90 days of Trader feedback + Preview pre-interest | Medium | OPEN |
| QB-03 | What willingness-to-pay signal exists for $1,199/mo + per-seat at fund-tier? | Anchors Desk Full v2 launch criteria | B-02, H-03 | Founder + fund-tier conversations | Direct conversations with 5+ fund-tier candidates | Low (P5 horizon) | OPEN |
| QB-04 | What does Stripe blended take-rate actually come out to for MENA + global EN once live? | Margin honesty in financial model | F-05 | Founder + Stripe live data | First 30 days of paid transactions | High | OPEN |
| QB-05 | Are there refund-pattern signals in the Trader cohort that suggest pricing mismatch vs trust mismatch? | Different root causes need different responses | B-03 | Founder + cohort data | First paid cohort with refund tagging | Medium | OPEN |

---

## C. GTM proof

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QC-01 | Is founder-led content actually driving signups at a rate worth the time investment? | Without proof, founder time on content is a hidden cost | E-01 | Founder + signup attribution | 90 days of content + signup attribution | High | OPEN |
| QC-02 | Does MENA-targeted content perform differently from global EN content? | Drives whether E-03 splits or unifies | E-03 | Founder + content analytics | Side-by-side content tests | Medium | OPEN |
| QC-03 | Do trust-driven prospects find us via search, community, or referral? | Channel mix shapes content posture | E-01, E-03 | Founder + signup origin | Onboarding question + analytics | High | OPEN |
| QC-04 | What's the realistic CAC (in founder hours) per activated free user, and per paid signup? | Required before ever activating paid acquisition | E-02 | Founder + time tracking | Founder hours log + signup data | Medium | OPEN |
| QC-05 | Are any partnership opportunities (data providers, communities, niche newsletters) worth pursuing pre-P3? | Founder time is finite; partnerships can amplify | New partnership decision rows | Founder | Direct outreach / inbound | Medium | OPEN |

---

## D. Trust readiness

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QD-01 | What % of validation cohort completes the 30-day window with no incident-driven termination? | Direct input to M1 milestone decision | M1 milestone | Founder | Cohort tracking | High | OPEN |
| QD-02 | Are users experiencing the gate as protective or as an obstacle? | Distinguishes "trust posture working" from "trust posture failing" | C-02, D-01 | Founder + cohort feedback | Direct interviews + ticket tagging | High | OPEN |
| QD-03 | Has any external party (community, journalist, regulator) signaled interest in or scrutiny of the product? | Early signal of public response posture needed | C-02 | Founder | Manual monitoring | Medium | OPEN |
| QD-04 | Is the disclosure language ("Testnet only. 30-day validation phase. No real capital.") visible on every surface a prospect can reach? | Drift here is invisible until incident | C-04 | Founder | Cross-surface audit | High | OPEN |
| QD-05 | Are override events distributed broadly, or concentrated in a few users? | Concentrated overrides may be one user; distributed may be UX problem | TRAS knob calibration (H-04) | Founder + engine telemetry | Override log review | Medium | OPEN |

---

## E. Compliance sensitivity

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QE-01 | What is the current UAE regulatory posture for crypto-derivative-related software products? | Operating jurisdiction; primary location | A-06 (already locked, posture-only) | Founder + external counsel | Counsel review | Medium | OPEN |
| QE-02 | Is the US-blocked-at-signup enforcement actually robust (IP, attestation, payment)? | If it leaks, regulatory exposure rises | A-06 enforcement | Founder + Engineering | Signup-flow audit + attestation review | High | OPEN |
| QE-03 | Will Bybit integration at P2 require any additional jurisdictional review? | Could change P2 sequencing | H-02 | Founder + counsel | Vendor compliance review | Medium | OPEN |
| QE-04 | Does the trial model (B-04) have any tax-treatment edge cases in MENA? | Affects Stripe configuration | B-04, F-05 | Founder + counsel + bookkeeping | Counsel review | Medium | OPEN |
| QE-05 | Will Desk Full v2 fund-tier customers require a more formal compliance posture (DPA, SOC 2 lite, audit-grade exports) — and at what threshold? | Anchors compliance posture upgrade timing (M7) | M7 milestone | Founder + counsel + first fund prospect conversations | Direct conversations + counsel scope | Low (P3+ horizon) | OPEN |
| QE-06 | What recordkeeping retention is required for journal/decision artifacts under UAE + MENA expectations? | Drives data architecture | Future compliance posture | Founder + counsel | Counsel review | Medium | OPEN |

---

## F. Support load

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QF-01 | What is the *actual* support time per Trader user vs the ≤30 min/mo assumption (#12)? | Drives Trust Ops contractor activation | G-01 | Founder | First paid cohort over 30 days | High | OPEN |
| QF-02 | What is the burst pattern of tickets during a market regime flip? | Capacity planning needs p95, not mean | G-01 engagement model (G-02) | Founder | First volatile market period after launch | Medium | OPEN |
| QF-03 | What share of tickets are gate-confusion vs onboarding vs billing? | Determines what KB content compounds value | C-05, D-02 | Founder | Tagged ticket dataset | High | OPEN |
| QF-04 | How long does it actually take to write a substantive KB article that resolves a recurring ticket type? | Founder time honesty | C-05 | Founder | Time tracking on KB authoring | Medium | OPEN |
| QF-05 | Are users self-serving via the KB, or are KB articles being ignored? | Validates KB ROI | KB strategy | Founder + analytics | KB pageviews + ticket-deflection data | Medium | OPEN |

---

## G. Cost structure uncertainty

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QG-01 | What is the actual top-3 vendor concentration once Trader is live? | Concentration is a structural fragility | F-02 | Founder + bookkeeping | First month of paid bills | High | OPEN |
| QG-02 | Does LLM cost scale linearly, sublinearly, or superlinearly with active users? | Margin erosion risk if superlinear | F-02 | Founder + LLM provider dashboards | First 30 days of paid usage | High | OPEN |
| QG-03 | What is the realistic monthly compute floor at P1 (one app + one engine + PG + Redis)? | Anchors fixed cost vs variable cost framing | F-02, F-03 | Founder + hosting bills | One full billing cycle | High | OPEN |
| QG-04 | Will CoinGlass pricing tier change at P2 vendor expansion volumes? | Single-source dependency on derivatives data | H-02 | Founder + vendor conversation | Direct quote from vendor | Medium | OPEN |
| QG-05 | What does the "fail-soft" behavior actually cost in compute when a vendor outage triggers degraded scanning? | Hidden cost during incidents | F-02 | Founder + replay test | Simulated outage replay | Medium | OPEN |
| QG-06 | At what active-user count does the engine VPS step-up to the next tier? | Cost discontinuity risk | F-02 | Founder + load test | Synthetic load test | Medium | OPEN |

---

## H. Hiring sequence

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QH-01 | Who are the 2–3 right candidates for the Trust Ops contractor role, and are they available? | Sourcing must be 30 days ahead of activation | G-01, G-02 | Founder | Network outreach + 1-1 conversations | High | OPEN |
| QH-02 | Who are the 2–3 right candidates for the Engineering vendor-integration contractor? | Same — sourcing ahead of activation | G-03 | Founder | Network outreach | Medium | OPEN |
| QH-03 | Is there a candidate for the optional advisor role with availability for monthly review participation? | If not, defer the role | G-05 | Founder | Direct conversation | Medium | OPEN |
| QH-04 | What does the founder *actually* spend time on weekly, by category? | Bottleneck identification depends on this | G-01, F-01 | Founder | Manual weekly time log | High | OPEN |
| QH-05 | Will the first FT hire candidate emerge from the contractor pool, or will external sourcing be needed? | Affects P3 hiring runway | G-06, role #7 | Founder | 3-month contractor performance | Low (P3 horizon) | OPEN |
| QH-06 | Are there geographic / timezone constraints from the founder's network that limit sourcing radius? | Locks search radius for first hires | G-04 | Founder | Network audit | Medium | OPEN |

---

## I. Roadmap gating

| ID | Question | Why it matters | Decision affected | Who answers | Evidence / input needed | Urgency | Status |
|---|---|---|---|---|---|---|---|
| QI-01 | What exact event resets the PCC v2 G3 30-day stability clock? | Clock-reset discipline | H-01 | Founder | Engine deploy policy | High | OPEN |
| QI-02 | Is there a defensible early signal that G3 stability is degrading before a kill-switch trip? | Early warning vs reactive | H-01 | Founder + engine telemetry | Telemetry pattern review | Medium | OPEN |
| QI-03 | What does "P1 stabilization" actually look like in measurable terms (M3)? | Gates P2 entry | H-02, M3 milestone | Founder | First Trader cohort D30 + D60 | High | OPEN |
| QI-04 | Does the validation cohort have enough heterogeneity (across Omar / Karim personas) to inform Trader-launch decisions? | Cohort representativeness | D-01, H-01 | Founder | Cohort persona breakdown | High | OPEN |
| QI-05 | What concretely changes (in the engine, the dashboard, the disclosure language) when transitioning from VCE NSM to TRAS NSM? | Smooth transition vs ragged transition | H-04 | Founder | Transition checklist | Medium | OPEN |
| QI-06 | Is there a credible scenario where P1 narrow-ship is no-go, and what signals would force it? | No-go is a real outcome, not a fallback | H-01 | Founder | Pre-mortem checklist | High | OPEN |
| QI-07 | At what point would we deliberately *roll back* a phase transition (e.g., P1 → P0)? | Backward movement is allowed, must be explicitly defined | H-05 | Founder | Roll-back criteria document | Medium | OPEN |

---

## Status summary

| Urgency | Count |
|---|---|
| High (this 90 days) | 21 |
| Medium (next 90 days) | 18 |
| Low (later phase) | 3 |
| **Total OPEN questions** | **42** |

**Top 5 highest-leverage questions** (sorted by what they unblock):

1. **QA-01** — Current PCC v2 G3 state. Unblocks H-01 and the entire 30-60-90 plan. Without this, every other "High" answer is hypothetical.
2. **QD-01** — Validation cohort 30-day completion %. Unblocks the M1 milestone decision and informs whether P1 narrow-ship is even on the table.
3. **QB-01** — Trader conversion rate signal from validation cohort. Unblocks the entire monetization thesis.
4. **QF-01** — Actual support time per Trader user. Unblocks G-01 (Trust Ops activation) timing.
5. **QG-02** — LLM cost scaling shape. Unblocks margin honesty and downstream cost framing.

Closing these five questions in the right sequence collapses most of the ambiguity in the next 90 days. Closing them in the wrong sequence (e.g., trying to answer QB-01 before QA-01) wastes effort.

---

## How to use this register

- At every weekly review: scan the High-urgency rows. If a question can be answered this week, do it; if not, confirm the evidence path is still valid.
- At every monthly exec review: full register sweep. Move ANSWERED items to the decision register, retire stale Medium/Low items if they no longer matter, add any new questions surfaced during the month.
- At every phase transition: re-baseline the urgency tags. A `Medium` question for P1 may become `High` for P2.
- When a decision is in flight in `leadership-decision-register.md`, walk this register backward to confirm there isn't an unanswered question upstream of the decision. If there is, the decision is premature.

The register is **the canonical place where we admit what we don't know yet**. Hiding ambiguity in unwritten assumptions is the failure mode this register exists to prevent.
