# 10 — Phase 1 Decision Register

**Scope:** Decisions that block Phase 1 exit for MARKET, ICP, POSITIONING, BRAND, PRODUCT, TRUST, RISK *(BRAND added 2026-05-04 via Path B charter amendment)*. Anything pricing-final, channel, or fundraising belongs to Phase 2/3/4 registers.

**Convention:** Decision IDs use the workstream prefix (M / I / P / B / Pr / Tr / R) plus a number. Once `LOCKED`, the decision is mirrored into `_decisions/decision-log.md` and a memory file is patched per `feedback_risk_threshold_reconciliation` if it touches risk thresholds.

---

## A. MARKET

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **M-1** | Pick the category | Sets trust contract, comparison set, pricing ceiling | A "AI trading intelligence platform" / B "Automated crypto futures system" / C "Trader OS" / D "Institutional-grade signal/risk platform" | **A** for P1; preserve room to grow into D for Desk Full v2 | Founder | end-May 2026 | Positioning sentence (P-1), copy across all surfaces | OPEN |
| **M-2** | Reject the other three on the record | Prevents quiet drift across the rejected shelves | Reject B, C, D / reject only B and C / reject none | Reject B (overpromises automation), C (low pricing power), D (premature without track record) | Strategy CoS | with M-1 | Comparison table; sales enablement | OPEN |
| **M-3** | "Institutional-grade" allowed in P1 copy? | Strong claim, easy to mis-trigger regulatory attention | Allow / Disallow until Desk Preview cohort closes | **Disallow in P1** | Founder + counsel | with M-1 | Anti-claim list, copy review | OPEN |
| **M-4** | "AI" as a leading word in P1 hero | "AI" is positioning oxygen and poison | Allow / Disallow / Allow only paired with verifiable mechanism | Allow only paired with mechanism (regime classifier, confidence score, risk gate) | Founder | with M-1 | Hero copy, taglines | OPEN |

---

## B. ICP

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **I-1** | Lock P1 primary persona | Drives copy, dashboard defaults, support, pricing tier defaulting | Omar / Karim / Layla | **Omar (P1)** | Founder | end-May 2026 | Almost everything in Phase 1 + 2 | OPEN |
| **I-2** | Karim posture in P1 | Prevents quiet feature drift toward Karim's depth ask | Welcomed-no-changes / build-API-now / exclude | Welcomed in cohort, no copy/UX changes | Founder | with I-1 | Product MOSCOW; Phase 2 charter input | OPEN |
| **I-3** | Layla posture in P1 | Avoids premature Desk Full v2 promises | Public single-line / waitlist / silent | Public single line: "Desk plans for small books open in 2027." | Founder | with I-1 | About page; Phase 5 input | OPEN |
| **I-4** | Cohort gate (must-haves) | Cohort signal fidelity hinges on selectivity | proposed gate / looser / stricter | Proposed: ≥6mo crypto futures, journaling habit, testnet OK, signed disclosure, daily check-in | Founder | end-May 2026 | Cohort recruiting, validation signal | OPEN |
| **I-5** | Auto-disqualifiers | Leaks contaminate cohort signal | proposed list / looser | Day-one beginners, US residents, copy-trade-only seekers, testnet refusers | Founder | with I-4 | Signup form logic | OPEN |

---

## C. POSITIONING

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **P-1** | Lock the positioning sentence | Every external surface sources from this | D1 (risk-first) / D2 (execution-flavoured) / D3 (evidence-led / cohort-led) | **D1 hero · D3 about/docs** | Founder | early-Jun 2026 | Surface variant table; bot intro; X / LinkedIn | OPEN |
| **P-2** | Lock the anti-claim list | Defensive; survives copy edits | The four / a different four / fewer than four | The four (no P&L · no automation promise · no "institutional-grade" · no "production-ready") | Founder + counsel | with P-1 | Copy review across all surfaces; counsel posture | OPEN |
| **P-3** | Tagline pairs allowed in P1 | Cross-surface consistency | "Trade Smarter With AI" + "Trade Smarter" / different / single tagline | The pair, per Scoopy custom-instructions | Founder | with P-1 | Tagline rules MD; surface variants | OPEN |
| **P-4** | Reserved phrasing for risk numbers | Prevents drift between numbers and disclaimer | proposed phrase / different / variable | Always pair with: *"Testnet only. 30-day validation phase. No real capital."* during P0/P1 | Founder | with P-1 | Every public surface that mentions a token | OPEN |

---

## D. BRAND

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **B-1** | Lock the Brand Strategy Summary | Anchors every downstream BRAND task; the seed for content / partnerships / press | Sign as drafted / revise / defer | **Sign as drafted** after first founder pass | Founder | early-Jun 2026 | Voice + tone, trust pillars, visual rules, patternbook | OPEN |
| **B-2** | Voice-tier boundary in writer guide | Codification of Scoopy product-tier vs social-tier rules for external writers | Codify as proposed / collapse tiers / add a third tier | **Codify as proposed** (product-tier no emoji / declarative; social-tier never inside product); *no new tier* | Founder | with B-1 | Voice + tone guidelines | OPEN |
| **B-3** | Number of trust pillars | 3–5 cardinality for marketing-readable pillars | 3 / 4 / 5 / >5 | **4** (recommended); reads neither thin nor as feature list | Founder | with B-1 | Trust + credibility pillars MD | OPEN |
| **B-4** | Founder Profile Messaging ownership (BRAND vs TRUST) | Strict overlap with TRUST T-9; double ownership produces two bios | BRAND owns both / TRUST owns both / split (BRAND messaging, TRUST page) | **Split — BRAND owns messaging, TRUST owns page artifact**; one canonical bio | Founder | early-Jun 2026 | Founder Profile Messaging (BRAND); TRUST T-9 page | OPEN |
| **B-5** | App-to-Marketing audit collapse with POSITIONING audit | Strict overlap with POSITIONING NEXT audit; running twice produces conflicting findings | Run separately / collapse into joint audit / drop one | **Collapse into one joint audit pass** owned jointly by BRAND + POSITIONING | Founder + Strategy CoS | mid-Jun 2026 | BRAND audit task; POSITIONING audit task | OPEN |
| **B-6** | Visual treatment lock vs A/B test | A/B testing fintech-conventional vs CSAI-tuned visuals during P0 cohort | Lock current / A/B during cohort / defer A/B to Phase 2 | **Lock current treatment for Phase 1**; queue A/B as Phase 2 input | Founder | with B-1 | Visual messaging rules; cohort landing page | OPEN |
| **B-7** | Founder-led distribution surface list | Which surfaces are in-scope for founder-led distribution in P1 | X / LinkedIn / Telegram / podcasts / press / all | **X + LinkedIn + Telegram + podcasts** in P1; press behind Phase-3 PR kit (LATER) | Founder | early-Jun 2026 | Social profile copy pack; community standards | OPEN |

---

## E. PRODUCT

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **Pr-1** | Lock the P1 MOSCOW | Anchors Jun–Jul 2026 build | proposed / wider / narrower | Proposed MOSCOW (see `04-product.md`) | Founder + Eng lead | early-Jun 2026 | Engineering load, cohort offer | OPEN |
| **Pr-2** | Manual override audit log on /journal as a Must | Omar daily loop hinges on it | Must / Should / Won't | **Must** | Founder | with Pr-1 | Engine extension; cohort-readiness checklist | OPEN |
| **Pr-3** | Daily digest as Should | Reduces alert fatigue; useful for retention | Should / Could / Won't | **Should** — ship if cohort week-2 feedback supports | Founder | mid-Jun 2026 | Telegram + dashboard surfaces | OPEN |
| **Pr-4** | Free-tier limits | Free must demonstrate the gate, not substitute Trader | Top 10 + 15-min delay / different / unrestricted / no Free | Top 10 + 15-min delay | Founder | with Pr-1 | Funnel design; conversion rate | OPEN |
| **Pr-5** | Real-capital go decision per cohort member after §8 Phase 1 opens | Manual or batch | Manual / batch / hybrid | **Manual, per-user, no batch** | Founder + Risk owner | before §8 Phase 1 opens | Real-capital approval runbook | OPEN |

---

## F. TRUST

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **Tr-1** | Lock MVTS at 7 signals | Defines paid-acquisition floor | 5 / 7 (proposed) / 10 / different mix | **7** — T-1, T-2, T-3, T-4, T-6, T-8, T-11 | Founder | end-May 2026 | Paid acquisition timing; ops load | OPEN |
| **Tr-2** | Hard gate on paid acquisition | Most expensive mistake in P1 is paying before MVTS | Hard gate / soft gate / case-by-case | **Hard gate — non-negotiable in Phase 1** | Founder | with Tr-1 | Marketing budget timing | OPEN |
| **Tr-3** | Cohort transparency page format | Public signal fidelity | Single page / multi-page / blog | Single page; cohort cap, methodology, exit memo placeholder | Founder | early-Jun 2026 | Trust + ICP signaling | OPEN |
| **Tr-4** | Where to publish PCC v2 public summary | Findability of trust signal | docs.coinscope.ai / `/methodology/risk-gate` / blog | DECISION NEEDED — recommend `docs.coinscope.ai/methodology/risk-gate` | Founder | early-Jun 2026 | Cross-link from hero, Telegram, X bio | OPEN |
| **Tr-5** | Vendor disclosure depth (T-12) | Optional in MVTS but trust-cheap | Ship in P1 / defer to P2 | **Ship in P1** | Founder | end-Jun 2026 | TRUST T-12 + RISK posture | OPEN |
| **Tr-6** | Status page provider | Build vs buy | Statuspage.io / OSS / roll our own | **Buy** (Statuspage.io or OSS equivalent); do not roll our own | Ops | end-May 2026 | Engineering load avoided | OPEN |

---

## G. RISK

| ID | Topic | Why it matters | Options | Recommendation | Owner | Deadline | Downstream impact | Status |
|---|---|---|---|---|---|---|---|---|
| **R-1** | Lock canonical risk-token table | Single source of truth across engine, copy, docs, prompt, memory | Lock as proposed / different values / split tokens by tier | **Lock as proposed** (10x · 10% · 5% · 5 · 80%) | Founder | mid-May 2026 | Every public surface; engine config | OPEN |
| **R-2** | Lock risk-state claim allowance matrix | Operational guardrail | Lock as proposed / different / no matrix | **Lock as proposed** with counsel pre-review on Validation + Narrow Ship rows | Founder + counsel | end-May 2026 | Copy review; sales enablement | OPEN |
| **R-3** | Real-capital approval flow: manual or batch | Consistency with §8 promise | Manual per-user / batch / hybrid | **Manual, per-user, no batch** | Founder | before §8 Phase 1 opens | Real-Capital Approval Runbook | OPEN |
| **R-4** | Vendor incident comms cadence | Trust signal speed | 15-min status / 30-min status / hourly | Status page within 15 min; Telegram cohort alert within 30 min | Ops + Founder | early-Jun 2026 | Vendor incident templates | OPEN |
| **R-5** | Public publication of PCC v2 summary | Visibility of the gate | Yes by P0 invite-out / yes later / no | **Yes by P0 invite-out** | Founder | early-Jun 2026 | TRUST T-2 | OPEN |
| **R-6** | Downgrade runbook authority | Avoids ad-hoc decisions under pressure | Founder unilateral / founder + Eng lead / committee | Founder may downgrade unilaterally; upgrade requires founder + Eng lead + counsel where copy changes | Founder | with R-2 | Downgrade Runbook v1 | OPEN |

---

## How to use this register

- A row stays `OPEN` until the recommendation is either accepted or replaced. When accepted: change status to `LOCKED`, mirror the entry into `_decisions/decision-log.md`, and patch the relevant Phase 1 scaffold doc.
- A row may be moved to `DEFERRED` only with a reason and a phase pointer (e.g., "deferred to Phase 2 charter — need cohort exit memo first").
- Decision IDs are durable. Once locked, they may be referenced from product code, copy, runbooks, or the master prompt.
