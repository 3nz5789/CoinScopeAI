# Secondary ICPs

**Status:** Wave 1 · v1 · 2026-05-07
**Disclaimer:** Validation phase active. Testnet only. No real capital. v0.[X]

This file classifies the segments CoinScopeAI will **serve but not lead with**, the segments to **defer**, and the segments to **reject**. It exists to absorb GTM pressure: when a non-primary segment shows up with money or interest, this file is what the founder reads before saying yes or no.

---

## 1. Secondary segment classification

| Class | Treatment | Examples |
|---|---|---|
| **Strategic secondary** | Served in P1; not led with; sustained content investment in P2 | P3 Layla — Solo PM ($200k–$1M aggregate book) |
| **Watch-list secondary** | Served when they arrive; light content investment; not a P1 acquisition target | P2 Karim — Engineer Trader (Trader → Desk Preview pathway) |
| **Served-not-led** | Served at Trader tier when they self-arrive; no marketing investment | Prop-firm-funded traders (locked secondary in v1) |
| **Deferred** | Not targeted in P0–P5; revisit only on documented condition | See §7 |
| **Rejected (anti-personas)** | Filtered at signup; explicitly out of scope | See §8 |

This classification is consistent with locked v1 §3.0: locked primary ICP is disciplined retail futures trader $5k–$250k MENA + global EN; locked secondary is prop-firm-funded; locked anti-ICPs are US retail, sub-$5k accounts, copy-traders/signal-buyers, and fund LPs.

---

## 2. Strategic secondary — P3 Layla, Solo PM

### Who they are (compressed)

A solo portfolio manager — formal or informal — running a $200k–$1M aggregate book that mixes own capital and a small partner/family/close-circle book. Often UAE/MENA-resident; sometimes global-EN. Already disciplined; the defining feature is *scale and book complexity*, not origin (per locked v1 §3.1 cut axis). Buys institutional-grade discipline without institutional overhead.

Default tier path: **Desk Preview $399/mo → Desk Full v2 $1,199/mo + per-seat ($149 or $249) at P5.**

Full persona card lives at `business-plan/03-icp-segmentation.md` §3.2 Persona 3.

### Why they are secondary, not primary

Three reasons, ordered by how strongly each applies:

1. **The Desk Preview value-delivery surface is partial.** Multi-account view, advanced gates, and read API land at P1 close per the locked phase plan. Leading with a segment that needs the partial surface is a quality-bar mismatch.
2. **Solo-PM evaluation cycles are longer.** P1 Omar evaluates in 2–6 weeks; P3 Layla evaluates over months and wants documented evidence (cohort data, audit-grade journal samples). A 30-day validation phase + 60-day P1 cohort is too short to produce the evidence Layla wants on first contact.
3. **P3 Layla rewards arrival, not pursuit.** Founder-led distribution into a methodology cohort produces P1 Omar referrals into P3 Layla relationships organically. Active acquisition into P3 Layla burns founder time without a cohort-data asset to point to.

### Why they are *strategically* secondary, not watch-list

P3 Layla is the single segment that:
- Anchors the Desk Full v2 economics at P5 (the $1,199 + per-seat tier exists because of them)
- Disproportionately validates the MENA-built and MENA-rooted positioning (Force 3)
- Provides the multi-account use-cases that exercise Desk Preview before Desk Full v2 launch

So while P3 Layla is **not the P1 acquisition target**, they are also **not a passive segment**. Sustained content investment at the Desk-Preview-and-up surface — long-form posts on multi-account discipline, audit-grade journaling, MENA family-office context — should run through P1 and P2.

### Risks of leading with P3 Layla too early

- **Quality-bar miss.** Desk Preview surface is partial through P1 close; leading with Layla shows the partial surface to the most demanding audience, the one most likely to defer or churn.
- **Anti-overclaim risk on "institutional-grade" phrasing.** Layla is the segment where "institutional-grade" matters most, and where misuse of the phrase is most damaging. The Desk Full v2 product needed to substantiate the phrase does not exist yet.
- **Regulatory friction.** Solo-PM operating an informal partner book sits in a fuzzy regulatory zone in many jurisdictions. CoinScopeAI does not advise on fund formation; Desk-tier marketing copy must not position the product as a fund-formation alternative (carried from locked v1 §3.0).
- **Pricing pressure.** Desk Preview at $399 may face anchor-shopping if Layla evaluates against Bloomberg-tier vendors and finds CoinScopeAI underspecified at this stage.

### What needs to be true before prioritizing P3 Layla

1. Desk Preview value-delivery surface (multi-account · advanced gates · read API) at full quality bar — target P1 close
2. Audit-grade journal samples available as published artifacts (anonymized cohort data acceptable)
3. P0 validation passed and the production-ready posture is closer to substantiated
4. Counsel-confirmed framing for Solo-PM marketing copy (no fund-formation language)
5. At least 1–2 P1 Omar → P3 Layla referrals observed in P1 cohort data

When 3 of 5 are true, promote P3 Layla from strategic secondary to **co-primary** at P2. **DECISION NEEDED** at P1 mid-cohort review.

---

## 3. Watch-list secondary — P2 Karim, Engineer Trader

### Who they are (compressed)

A quant-curious software engineer (often mid-level or senior) trading perps part-time. Trader → Desk Preview pathway over time. Buys programmable risk and clean APIs over signal feeds. Force 2 alignment specifically (AI cost-collapse — they are themselves Force 2 evidence).

Default tier path: **Trader $79/mo → Desk Preview $399/mo over time.**

Full persona card at `business-plan/03-icp-segmentation.md` §3.2 Persona 2.

### Why they are secondary

- **Pricing constraint.** P2 Karim is doing the math on "build vs. buy." Trader-tier pricing must compete with "six months of personal build time" (locked v1 §3.0 carry-forward concern). Acquisition cycles are slower because the buy decision is rational rather than pain-driven.
- **Acquisition channel mismatch in P1.** Karim's channels are HN, applied-quant Twitter, GitHub, and engineering Substacks. Founder-led distribution into these channels is feasible but lower-leverage than methodology-cohort channels in P1.
- **Long-tail upgrade.** Karim's value comes from the eventual Trader → Desk Preview upgrade and the read-API use case, both of which mature beyond P1.

### Why they are watch-list, not strategic

Karim arrives organically through:
- Founder content that demonstrates engine architecture and math transparency
- Open posts about CoinScopeAI's development discipline
- API documentation quality (when read API ships at Desk Preview)

Active acquisition into Karim's segment would require an engineering content motion that is high-cost and low-priority during validation. **Light content investment in P1; revisit channel strategy at P2 charter.**

### Risks of leading with P2 Karim

- **Build-instead-of-buy risk.** Karim may treat CoinScopeAI as architectural inspiration rather than a purchase. Conversion rate from "interested engineer" to "paid Trader" is likely lower than P1 Omar's discovery → paid rate.
- **Feature-creep pressure.** Karim asks for API surface, custom integrations, and configurability that exceed what Trader tier can support. Risk of over-investing in features that migrate up to Desk Preview without commensurate revenue.
- **Voice mismatch.** P2 Karim is comfortable with terse, declarative product-tier voice — but engineering content in their channels often requires a different mode (architecture posts, decision rationales) that pulls founder time away from validation.

### What needs to be true before prioritizing P2 Karim

1. Desk Preview read API documented and shipped (P1 close)
2. At least one engineering-content artifact published (architecture decision record, position-sizing math explainer)
3. P0 validation passed; Trader tier has cohort data behind it
4. Founder time is available for engineering-channel content motion

When 3 of 4 are true, elevate to **strategic secondary** at P2. **DECISION NEEDED** at P2 charter.

---

## 4. Served-not-led — Prop-firm-funded traders

Locked v1 secondary persona. Treated as **served-not-led**:

- They self-arrive at Trader tier; the product fits their workflow (capital-preservation rules are exactly what a prop firm enforces externally)
- No marketing investment in P1 or P2
- Anti-overclaim posture extends — never imply that CoinScopeAI helps a trader pass a prop-firm evaluation faster
- Watch for cohort signal: if prop-firm-funded traders represent >10% of P1 paid users, revisit their classification at P2 charter

The reason this segment is *not* the primary ICP, despite the workflow fit: prop-firm-funded traders use external risk frameworks (the firm's rules), and they upgrade-vs-cancel based on whether they pass evaluations and stay funded — both of which are out of CoinScopeAI's control. The cohort signal they produce is mixed.

---

## 5. Other plausible-but-not-primary segments (treatment summary)

| Segment | Treatment | Why this treatment |
|---|---|---|
| Discretionary swing/position traders | Served-not-led | Lower trade frequency = lower engagement = harder cohort signal |
| Algorithmic-only traders (full automation) | Watch-list | Need read API + automation tooling; Desk Preview pathway, not Trader |
| MENA family offices (small) | Watch-list (overlap with P3 Layla) | Acquisition through P3 Layla is more durable than direct |
| Crypto-native VCs trading own book | Served-not-led | High-trust audience but small absolute count; brand-trust premium opportunity |
| TradFi-to-crypto crossovers | Watch-list | Buy on credibility; "institutional-grade" reserved phrasing matters most here |

None of these is added to the locked persona set. They are explicitly tracked here as treatment guidance, not as new personas.

---

## 6. Deferred segments (post-P5 at earliest)

Each is deferred for explicit reasons. Each has an explicit revisit condition. Deferral is not rejection — it is sequencing.

| Deferred segment | Why deferred | Revisit condition |
|---|---|---|
| **Funds >$5M AUM** | Desk Full v2 is a P5 deliverable; fund-grade tier is post-P5 at earliest | Desk Full v2 cohort signal in P5–P6 |
| **Prop desks (firm-side, not trader-side)** | Different buyer (firm operations, not trader); requires team-grade onboarding and admin | Post-P5; only if Desk Full v2 cohort produces inbound from firms |
| **Signal resellers** | Anti-overclaim posture incompatible; CoinScopeAI does not enable signal reselling | Not planned |
| **US-domiciled retail traders** | US blocked at signup; requires US licensure decision | Counsel-confirmed US licensure path; entity restructure |
| **Beginner traders (no methodology yet)** | Not the buyer; product features assume buyer already has discipline | Not planned in current strategic frame |
| **Day-trading-as-content audiences** | Anti-overclaim risk; performative buyers, not disciplined buyers | Not planned |
| **Mobile-first traders requiring native iOS/Android app** | Not on roadmap in P0–P5 | Post-P2, only if cohort demands |
| **Multi-language UI buyers (beyond EN)** | Target geo is EN-fluent; localization is downstream | Post-P5 |
| **Affiliate/influencer-led acquisition cohorts** | No referral-with-payouts program pre-validation | Post-validation, with structured guardrails |
| **Copy-trading audiences** | Custody-free + anti-overclaim posture incompatible | Not planned |

---

## 7. Anti-personas (rejected — filtered at signup)

Locked v1 §3.0. Each is filtered, not just discouraged. These do not buy CoinScopeAI:

| Anti-persona | Reason |
|---|---|
| US-resident retail | Regulatory posture; US blocked at signup until licensure |
| Sub-$5k accounts | Tier matrix anchor; unit economics; cohort signal noise |
| Copy-traders / signal-group buyers | Vision A mismatch; product is process, not signals |
| Fund LPs (passive allocators) | CoinScopeAI is not a fund; not a fund-formation tool |
| Anyone seeking "guaranteed returns" or "10x your account" | Anti-overclaim posture; brand-voice incompatibility |
| Anyone wanting CoinScopeAI to custody capital | Custody-free posture is structural |
| Anyone seeking autonomous execution without authorization | Custody-free + anti-overclaim posture |

The filtering happens at three layers: signup geofence (US); copy and positioning (custody-free, no signals, no autonomy); pricing tier anchors (>$5k accounts implied by Trader $79 sticker).

---

## 8. Risks of broadening too early

A consolidated view of what goes wrong if the founder takes any signup that arrives:

| Risk | Mechanism | Mitigation in plan |
|---|---|---|
| Cohort signal goes muddy | Mixed personas in the 40-user P1 cap produce mixed retention/churn data; conclusions weaker | Strict primary-ICP cohort selection; secondaries served, not pursued |
| Support load spikes | Different personas need different support styles | Cohort cap of 40; product-tier voice consistent across all |
| Roadmap gets pulled across personas | Each segment requests features; founder oscillates | Locked personas + decision log + pre-mortem before prioritization changes |
| Brand voice drifts toward broadest audience | Marketing copy softens to attract non-primary segments | Brand-voice enforcement skill; locked phrasing rules |
| Pricing pressure | Mixed personas anchor pricing in the wrong place | Tier matrix locked; founder-cohort terms documented |
| Anti-overclaim discipline cracks | Pressure to convert non-primary segments produces softer language | Brand-voice review pass before any external claim |

---

## 9. Cross-references

- Locked v1 personas (full cards): `business-plan/03-icp-segmentation.md`
- Decision log: `business-plan/_decisions/decision-log.md`
- Primary ICP: `04-icp-and-segmentation/primary-icp.md`
- Strategic constraints (US block, anti-overclaim, etc.): `02-company-overview/strategic-constraints.md`
- "Do not prioritize yet" register: `01-executive-summary/strategic-priorities.md` §3
- Counsel brief: `business-plan/_data/legal/Counsel_Brief_v2.md`

---

**Footer:** Testnet only. 30-day validation phase. No real capital. v0.[X] — 2026-05-07.
