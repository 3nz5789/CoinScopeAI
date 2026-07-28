# Jobs to Be Done

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file maps the **jobs CoinScopeAI is hired to do**, by category and by segment. JTBD is framed in the buyer's voice — what they are trying to accomplish, and what they are trying to feel — not in the product's voice. The pattern across all jobs: *enforce the discipline I have already built; do not replace it.*

Jobs are grouped into five categories:

1. **Functional jobs** — what the buyer is trying to *do*
2. **Emotional jobs** — what the buyer is trying to *feel* (or stop feeling)
3. **Risk-reduction jobs** — what the buyer is trying to *prevent*
4. **Workflow jobs** — what the buyer is trying to *integrate or replace* in their day
5. **Team / collaboration jobs** — what the buyer is trying to *coordinate* (relevant from Desk Preview onward)

Each job is tagged with its primary segment(s) where useful: **[P1]** P1 Omar (primary), **[P2]** P2 Karim, **[P3]** P3 Layla.

---

## 1. Functional jobs

### F1 — Enforce my position-sizing math automatically [P1, P2, P3]

> *"I already do this math by hand. Run it for me, transparently, every time, and refuse to arm a position that violates it."*

The product does this via the position sizer wired against the user's configured drawdown, daily-loss, and heat thresholds. Math transparency (formula + inputs + output) is non-negotiable for P1 Omar.

### F2 — Gate trades against my drawdown and daily-loss rules [P1, P2, P3]

> *"When I am near my daily-loss limit, I should not be able to enter a new position. The decision should be removed from the moment of weakness."*

The risk gate fires before order arming, returning the explicit gate that fired (e.g., "exposure cap reached", "daily loss within threshold").

### F3 — Classify the regime so I know whether my system applies [P1, P2, P3]

> *"My breakout strategy is dangerous in a Volatile regime. Tell me what regime we're in, with confidence, and I'll skip the setups that don't fit."*

v3 ML regime classifier produces Trending / Mean-Reverting / Volatile / Quiet labels with confidence, surfaced on every signal.

### F4 — Surface only the signals that match my framework [P1, P2]

> *"Don't show me 50 setups. Show me the ones with confluence at the regime I'm in, and tell me which gate would fire if I tried to enter."*

The scanner ranks setups by confluence score; the gate result is shown alongside the signal so the user knows in advance whether the trade can be armed.

### F5 — Maintain a clean, R-multiple-tagged journal [P1, P3]

> *"My journal is in spreadsheets and Notion. It is painful to maintain and worse to read. I want a journal that captures what I trade, why, what gate fired or didn't, and the R-multiple result."*

Performance + journal endpoints carry this. Rule-violation tagging is a P1 Omar priority.

### F6 — Watch multiple accounts at once [P3]

> *"My partner book and my own book have different risk envelopes. I need to see them side by side without juggling exchange dashboards."*

Multi-account view at Desk Preview; per-seat scaling at Desk Full v2.

### F7 — Get programmatic access to gate state, regime, and signals [P2, P3]

> *"I want to read my CoinScopeAI state from a script and combine it with my own indicators. Don't make me scrape your dashboard."*

Read API at Desk Preview; documented payloads on `/scan`, `/risk-gate`, `/regime/{symbol}`, `/performance`, `/journal`.

### F8 — Receive 24/7 alerts that don't drown me [P1, P2, P3]

> *"I sleep, I work, I have a life. Alert me when something matters; don't alert me 40 times a day."*

Telegram alerts with canonical payload; rate limit, dedup, grouping per `alerting-and-user-experience` skill.

### F9 — Configure the engine to my own thresholds [P1, P2, P3]

> *"My drawdown rule is 8%, not 10%. My max heat is 60%, not 80%. Don't make me work around your defaults — let me configure mine."*

Risk thresholds in the engine are surfaced as defaults; user-configurable per-account.

---

## 2. Emotional jobs

### E1 — Stop dreading the moment of order placement [P1, P2, P3]

> *"I don't want to debate myself before every trade. I want a system that resolves the debate for me."*

The risk gate is the structural answer to this. Rejected trades come with the gate that fired, not with a debate.

### E2 — Sleep through volatile sessions [P1, P3]

> *"Last cycle I sat at 3 a.m. watching my book. I want a tool that gates and alerts so I can stop doing that."*

24/7 monitoring; canonical alerts; gated entries; daily-loss halts.

### E3 — Feel respected by the tools I use [P1, P2, P3]

> *"Most crypto products talk down to me. I want a tool that writes like the canon I read — Van Tharp, Schwager, Tharp's R-multiples — and assumes I know the math."*

Product-tier voice (terse, declarative, data-led). No marketing fluff in-product.

### E4 — Feel I am not gambling [P1, P3]

> *"I have built a system. I am not a gambler. The tool I use should not be branded like a casino."*

Anti-overclaim brand voice; no "10x your account" language; no leaderboards; no casino aesthetic.

### E5 — Feel I am ready for an audit (informal or formal) [P3]

> *"If a partner asks me 'why did you size this trade that way,' I should be able to point to a rule, an input, a regime, and a gate result — not a feeling."*

Audit-grade journal; rule-violation tagging; documented thresholds.

### E6 — Feel I have an edge in the parts I can control [P1, P2]

> *"I can't control the market. I can control my entries, my sizing, my exits, my discipline. I want software that makes those controllables tighter."*

Risk-first feature set; configurable gates; transparent math.

### E7 — Feel like I'm not the only one trying to do it right [P1]

> *"Most crypto Twitter is noise. It's tiring. A product whose voice is methodical and whose audience is methodical is a relief."*

Founder-led content; closed-community channels; cohort-data over performative claims.

---

## 3. Risk-reduction jobs

### R1 — Prevent overleveraged entries [P1, P2, P3]

> *"Force the leverage cap. Don't let me bypass it in a moment of conviction."*

Max leverage 10x — locked, code-level — and surfaced when composing a position.

### R2 — Prevent revenge trading [P1, P3]

> *"After a stop-out, my next trade is statistically my worst. Halt me when I've hit my daily-loss limit, and don't let me argue."*

Daily-loss limit 5% (24h rolling, halts trading) — locked.

### R3 — Prevent over-concentration in one position [P1, P3]

> *"Heat caps protect me from putting too much of my account behind a single setup."*

Position heat cap 80% — blocks new entries on that position.

### R4 — Prevent "too many things going wrong at once" [P1, P3]

> *"Three is enough. If I have three open positions and a fourth setup looks great, I should not be allowed to take it."*

Max open positions 3 — locked.

### R5 — Prevent crossing my drawdown line [P1, P2, P3]

> *"If my account has bled to within a defined distance of my drawdown line, halt new entries until I reset."*

Max drawdown 10% (account, hard stop) — locked.

### R6 — Prevent execution on stale or wrong data [P2, P3]

> *"If your data is stale or your engine is degraded, refuse to give me a signal. Don't give me a wrong one."*

Drift detection between local state and exchange truth; graceful degradation; never silent stale data (per `binance-bybit-integration-guard` skill).

### R7 — Prevent regulatory exposure from poor record-keeping [P3]

> *"My partners may want to see what I did and why. Bad records are a regulatory and relational risk."*

Audit-grade journal; documented thresholds; per-account separation.

### R8 — Prevent API-key risk [P1, P2, P3]

> *"I'm connecting an exchange API. I want to be sure scopes are minimum and there is no withdrawal scope."*

Least-privilege scopes; "no withdrawal scope ever"; explicit copy at exchange-connection step.

### R9 — Prevent vendor-outage cascades [P2, P3]

> *"If your data vendor degrades, I want to know — not be exposed to silent failure."*

Vendor failure-mode mapping; graceful degradation; explicit incident communication.

---

## 4. Workflow jobs

### W1 — Replace my manual gating spreadsheet [P1]

> *"My drawdown / daily-loss / leverage / heat checks live in a spreadsheet. It's tiring to maintain and easy to ignore at 3 a.m."*

Risk gate runs continuously, automatically, at user-configured thresholds.

### W2 — Replace my manual journal [P1, P3]

> *"My journal lives in Notion. It is incomplete. I dread maintaining it. I want it to be the byproduct of using the tool, not a separate task."*

Journal endpoint captures rule-respected trades, rule-violations, R-multiples; replaces manual journaling.

### W3 — Replace my mental regime classification [P1, P2]

> *"I look at price action and decide if it's trending or chopping. I want a label, with confidence, that doesn't depend on my mood."*

v3 ML regime classifier with confidence.

### W4 — Replace polling exchange charts every 30 minutes [P1, P3]

> *"I shouldn't have to refresh the exchange app to see what's setting up. The product should tell me."*

Scanner + canonical alerts.

### W5 — Replace ad-hoc multi-account monitoring [P3]

> *"Switching between exchange accounts to monitor partner book and my own book is wasteful and error-prone."*

Multi-account view at Desk Preview; per-seat scaling at Desk Full v2.

### W6 — Replace manual export-to-CSV for performance review [P2, P3]

> *"My monthly performance review starts with a 90-minute CSV-and-spreadsheet exercise. Surface the report; let me read it."*

Performance endpoint + Desk-grade analytics at Desk Preview.

### W7 — Integrate with my own scripts and notebooks [P2]

> *"I have my own indicators in Python. Let me read CoinScopeAI state, combine it with mine, and write the combined result."*

Read API at Desk Preview; documented payloads.

### W8 — Reduce my screen time without reducing my discipline [P1, P3]

> *"24/7 markets ate my evenings. I want to spend less time at the screen, not more."*

Always-on monitoring + canonical alerts + risk gates do this structurally.

---

## 5. Team / collaboration jobs (Desk Preview onward; primary at Desk Full v2)

### T1 — Separate per-seat permissions on a shared book [P3, post-P5]

> *"My junior should be able to see signals and journal entries; only I should be able to change risk thresholds."*

Per-seat scaling at Desk Full v2 ($149 or $249/seat). Permissions per seat — design-level until P5.

### T2 — Show partner-style read-only views [P3]

> *"My partner wants to see what's happening, not change it. A read-only seat is enough."*

Read-only seat at Desk Full v2.

### T3 — Audit who changed which threshold and when [P3]

> *"If a threshold changes, I want to know who changed it and why."*

Audit log on threshold changes — design-level until P5; **DECISION NEEDED** on first-class implementation timeline.

### T4 — Coordinate on a shared incident or position event [P3]

> *"When the engine flags a regime flip and we have positions across two accounts, we need to be on the same page."*

Telegram + dashboard surfaces; shared context per account.

### T5 — Generate partner-readable reports [P3]

> *"My monthly partner update should be 90% generated, 10% commentary."*

Desk-grade analytics + audit-grade journal at Desk Preview, formalized at Desk Full v2.

---

## 6. Jobs by segment — emphasis matrix

| Job | P1 Omar | P2 Karim | P3 Layla |
|---|---|---|---|
| F1 Position-sizing math | ●●● | ●● | ●●● |
| F2 Drawdown / daily-loss gating | ●●● | ●● | ●●● |
| F3 Regime classification | ●●● | ●● | ●● |
| F4 Confluence-ranked signals | ●●● | ●●● | ●● |
| F5 R-multiple journal | ●●● | ● | ●●● |
| F6 Multi-account view | ● | ● | ●●● |
| F7 Read API | — | ●●● | ●● |
| F8 Canonical alerts | ●●● | ●● | ●● |
| F9 Configurable thresholds | ●●● | ●●● | ●●● |
| E1 Stop dreading order placement | ●●● | ●● | ●● |
| E2 Sleep through volatility | ●●● | ●● | ●●● |
| E3 Be respected by tools | ●●● | ●●● | ●● |
| E4 Not gambling | ●●● | ●● | ●●● |
| E5 Audit-ready feel | ● | ● | ●●● |
| E6 Edge on the controllables | ●●● | ●●● | ●● |
| E7 Methodical community | ●●● | ●● | ● |
| R1–R5 Prevent breaches | ●●● | ●●● | ●●● |
| R6 Prevent stale-data execution | ●● | ●●● | ●●● |
| R7 Prevent regulatory exposure | ● | ● | ●●● |
| R8 Prevent API-key risk | ●●● | ●●● | ●●● |
| R9 Prevent vendor-outage cascades | ●● | ●●● | ●●● |
| W1 Replace gating spreadsheet | ●●● | ● | ●● |
| W2 Replace manual journal | ●●● | ● | ●●● |
| W3 Replace mental regime | ●●● | ●● | ● |
| W4 Replace exchange polling | ●●● | ●● | ●● |
| W5 Replace multi-account juggling | — | ● | ●●● |
| W6 Replace CSV-spreadsheet review | ● | ●● | ●●● |
| W7 Integrate with scripts | — | ●●● | ●● |
| W8 Less screen, same discipline | ●●● | ●● | ●●● |
| T1–T5 Team / collab | — | — | ●●● |

`●●●` primary buying motivator · `●●` secondary · `●` tertiary · `—` not material

---

## 7. Implications for the product surface

A consolidated reading of the JTBD map for `06-product-strategy/` and downstream:

- **The most-shared-across-segments jobs are F1, F2, F9, R1–R5, R8, E1.** These are the **non-negotiable surface** for any tier (including Free in some form). Quality bar here is highest.
- **The Trader-tier focus** (P1 Omar) is functional + emotional + workflow: F1, F2, F3, F4, F5, F8, F9, E1, E2, E3, W1, W2, W3, W4, W8.
- **The Desk Preview focus** (P2 Karim mature → P3 Layla) is functional + workflow: F6, F7, W5, W6, W7.
- **The Desk Full v2 focus** (P3 Layla, P5) is team / collab + audit-grade: T1, T2, T3, T4, T5, E5, R7.
- **Cross-segment pricing logic:** the Trader → Desk Preview upgrade is *workflow-driven* (multi-account, read API, advanced reporting); the Desk Preview → Desk Full v2 upgrade is *team-driven* (per-seat, audit, partner views).

---

## 8. Cross-references

- Locked v1 §3 persona cards (full): `business-plan/03-icp-segmentation.md`
- Locked v1 §4 problem and value prop: `business-plan/04-problem-value-prop.md`
- Primary ICP: `04-icp-and-segmentation/primary-icp.md`
- Secondary ICPs: `04-icp-and-segmentation/secondary-icps.md`
- Pains, triggers, WTP: `04-icp-and-segmentation/pains-triggers-wtp.md`
- Alerting design rules: `alerting-and-user-experience` skill
- Tier matrix: `01-executive-summary/business-model-summary.md` §3

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
