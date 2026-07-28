# §9 Supplement — Brand Collision Strategy

**Status:** DRAFT v0.2. Decision required on external-collision strategy (§9C.4). Internal-state findings revised — see §9C.9 audit correction. Sits as a tactical supplement to §9 (Brand and Messaging v1 LOCKED 2026-05-01); does not modify locked pillars, only addresses public-surface disambiguation.
**Created:** 2026-05-17
**Last revised:** 2026-05-17 (logged-in audit correction)
**Trigger:** Public-surface audit of @coinscopeai_ revealed (a) the CoinScopeAI name competes against multiple distinct entities in SERP for the brand-name query, (b) Google's website snippet for coinscope.ai still reflects pre-PCC v2 positioning, (c) early reads suggested internal brand fragmentation across multiple FB pages and IG handles. Logged-in audit on 2026-05-17 confirmed (a) and (b) but materially reduced (c) — see §9C.9.

> **Read §9C.9 first.** It corrects assumptions baked into earlier sections about the number of owned surfaces and the degree of internal fragmentation. The external-collision recommendation (Option A) is unchanged.

---

## 9C.0 Why this exists

§9 v1 locks the messaging matrix and pillars on the assumption that "CoinScopeAI" is a recognizable, ownable brand-name handle. The May 2026 audit showed that assumption is partially wrong in practice: anyone searching the brand name encounters at least four distinct "Coinscope" entities, one of which is a tradeable token on major exchanges. This memo is the tactical layer that protects §9's positioning from being neutralized by external collision.

## 9C.1 The collision landscape

Surfaced from a `"CoinScopeAI"` SERP query on 2026-05-17:

| Entity | Surface | Distinction | Risk to us |
|---|---|---|---|
| **coinscope.ai** | Our website | Us. AI-driven capital-preservation infrastructure for crypto futures. | Sponsoring entity — we want this to win every brand-name query. |
| **coinscope.co** | Distinct platform marketed as "Trader AI" and "Ai Crypto Predictor" | Different company, same brand-stem, overlapping vertical (AI + crypto trading). | High. Steals brand-name impressions. Likely the most damaging confusion. |
| **COINSCOPE token** | A cryptocurrency listed on Coinbase, LBank, CoinMarketCap, and surfaced in the CoinDesk tag system | A tradeable asset. Has its own market cap, holders, communities, exchange listings. | Severe. Anyone Googling "CoinScope" lands on exchange pages first; reasonable people will assume we issued it. Regulatory exposure if the token is ever flagged. |
| **@coinscopecrypto** | X account | Different identity. Possibly defunct, possibly active — unverified at audit time. | Medium. Brand-handle adjacency creates impersonation surface. |
| **mycoinscope.com** | Separate website, separate purpose | Different again. | Low — adds to noise. |

The dominant collision is the **COINSCOPE token**, because (a) it has institutional surface on exchanges we would never list on (LBank), (b) ranks above us in commodity SERPs (Coinbase price page often ranks for the bare-word query), and (c) the token's existence creates an implicit "is this their token?" question that we cannot proactively answer in search snippets.

## 9C.2 Why this matters now

Three reasons it can't wait.

1. **§9 positioning depends on credibility transfer from the brand name.** The pillars (capital preservation, framework respect, methodology transparency, MENA-AI-cost-collapse alignment) are credible because they belong to a specific entity. If the brand-name search returns four entities and one is a meme-tier token, the credibility transfer breaks before the pillars are read.
2. **The validation phase has a public-narrative requirement.** PCC v2 commits us to "not production-ready" honesty through ~May 31, 2026 and likely beyond. That posture only differentiates us if the audience reaches our channels. Search confusion stops the audience at the door.
3. **Investor narrative (§15) exposure.** Any due diligence prospect — MENA family office, global VC, strategic angel — will Google the brand name before the first call. The current SERP makes that an unforced credibility loss. §15's audience-lead-force map breaks if the prospect's first impression is "which one is this?"

## 9C.3 Strategic options

Three honest options. Each has a real cost.

### Option A — Disambiguation through aggressive specificity ("the AI one")

Keep the name. Win the search through specificity, schema, and disambiguation copy on every surface. Treat the `-AI` suffix as the differentiator and reinforce it everywhere — title tags, schema.org Organization markup, social bios, alt text, anchor text in inbound links, and every external mention requested through PR or partnerships.

**Cost:** SEO work over 6-12 months. Always carries residual confusion against the token, which we cannot delist. Defensive forever.

**Benefit:** No brand equity loss. §9 pillars stay intact. Cheapest in cash terms.

**Honest risk:** If the COINSCOPE token ever rugs or gets delisted under suspicious circumstances, we eat reputational shrapnel even though we are unrelated.

### Option B — Suffix-shift rebrand

Rename to something that still includes "CoinScope" but adds a structural differentiator users will recognize. Candidates:
- *CoinScopeAI Capital* (institutional signal)
- *CoinScopeAI Engine* (the actual product)
- *CoinScope Discipline* (the value proposition as the name)
- *CSAI* as a short-form mark for cited contexts
A suffix-shift preserves most existing brand equity (Notion DBs, Linear teams, GitHub repos, internal handles all stay), changes only the public-facing name.

**Cost:** Asset re-issue across logos, social handles (where available — most likely the `_capital` / `_engine` / `_discipline` variants are open), domain hygiene, all marketing collateral, possibly investor decks (§15). Lost compounding on existing brand mentions.

**Benefit:** Decisive separation. Future search competes on the new mark, which we can own cleanly.

**Honest risk:** The new mark may not stick. If we suffix-shift twice, we've abandoned brand equity twice.

### Option C — Full rename

A new mark with no overlap. Example only (not a recommendation): *Discipline.fi*, *Preserve Capital*, *Gate Trade*. Mark must be available across `.com`, social handles, and not collide with existing crypto projects.

**Cost:** Maximum. Full asset overhaul. Lost mention compounding. Investor narrative reset. Re-introducing the company to existing prospects.

**Benefit:** Cleanest long-term outcome if executed before mass marketing scales.

**Honest risk:** The validation phase is the wrong moment to rename. The brand isn't large enough for the rename to be costly, but it's also small enough that the rename itself becomes a one-off marketing moment with no compounding audience.

## 9C.4 Recommendation

**Option A (aggressive disambiguation), executed immediately, with a contingency to revisit at the end of validation phase.**

Reasoning:
- The validation phase is not the right moment for a rename. Capital and attention are scarce; ship the engine and the SLO stack first.
- The collision is bounded. The COINSCOPE token is the worst case but we are not the issuer; clear schema and disambiguation copy materially reduce the conflation risk.
- Option A is reversible — we can suffix-shift later if the disambiguation work hits a ceiling. The reverse is not true.
- §9 pillars are designed to compound over time; restart cost is higher than disambiguation cost.

**Decision gate to revisit:** Q4 2026 (post-validation phase). If at that point the brand search still consistently surfaces the token above us, or any of the look-alike platforms surface confusion in customer interviews, escalate to Option B.

## 9C.5 Tactical execution plan — Option A

If the recommendation is accepted, the following tasks form the execution checklist. Each is small; together they form the disambiguation moat.

### 9C.5.1 On-site (coinscope.ai)

| Task | Owner | Deliverable |
|---|---|---|
| Update site title tag from current to: *"CoinScopeAI — AI-driven capital-preservation infrastructure for crypto futures"* | Web | New `<title>` |
| Update meta description to match §9 v1 hero copy (Set Alpha) | Web | New `<meta name="description">` |
| Add schema.org Organization JSON-LD with: name, alternateName ("CSAI"), url, sameAs (X, LinkedIn, Threads, IG, YouTube, Telegram, Discord, GitHub), founder, foundingDate, description matching §9 hero copy | Web | JSON-LD block in `<head>` |
| Add a one-line disambiguation note in the footer: *"CoinScopeAI is an independent platform. We are not affiliated with the COINSCOPE token or any other 'Coinscope'-named platform."* | Web | Footer update |
| Add a `/not-the-token` or `/disambiguation` page that surfaces in search for confusion queries | Web | New page |
| Confirm rel=canonical is set on every page | Web | Audit pass |

### 9C.5.2 Social bios — every owned channel

Standardize bio opening across all channels:

> *"CoinScopeAI — AI-driven capital-preservation infrastructure for crypto futures. Independent platform. Not affiliated with any 'Coinscope'-named token."*

Channel-specific length variants are acceptable (Twitter 160 chars, Instagram 150, etc.); the *independent platform* clause is non-negotiable on every bio.

### 9C.5.3 External mentions / PR

Every press mention, podcast intro, conference bio, and partnership announcement uses the full mark "CoinScopeAI" on first reference, never "Coinscope" abbreviated. Provide partners with a one-paragraph standard bio and a logo that includes the `-AI` suffix visually (locked alongside Pillar 1 typography decisions in §16 if §16 covers this; otherwise propose adding here).

### 9C.5.4 Internal hygiene

| Surface | Current | After |
|---|---|---|
| Notion workspace name | (verify) | "CoinScopeAI" |
| Linear team name | "CoinScopeAI–MVP" | (already correct) |
| GitHub org / repo | `3nz5789/CoinScopeAI`, `3nz5789/CoinScopeAI_v2` | (already correct) |
| Stripe entity | "CoinScopeAI, LLC" (acct `1TT23P…`) | (already correct, post-rotation) |
| Email signatures | (audit) | "CoinScopeAI" |
| Telegram bot | `@ScoopyAI_bot` | (separate handle, fine) |

The internal hygiene is mostly already aligned; this column documents the audit.

### 9C.5.5 Schema markup specifics

Bake into the site template:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "CoinScopeAI",
  "alternateName": ["CSAI"],
  "url": "https://coinscope.ai",
  "logo": "https://coinscope.ai/[logo-url]",
  "description": "AI-driven capital-preservation infrastructure for crypto futures.",
  "foundingDate": "2026",
  "founders": [{"@type": "Person", "name": "Mohammed Abu Anzeh"}],
  "sameAs": [
    "https://twitter.com/[handle]",
    "https://www.linkedin.com/company/[handle]",
    "https://www.threads.com/@coinscopeai_",
    "https://www.instagram.com/coinscopeai_",
    "https://www.facebook.com/[id]",
    "https://www.youtube.com/@CoinScopeAI",
    "https://github.com/3nz5789/CoinScopeAI",
    "https://t.me/[handle]"
  ],
  "disambiguatingDescription": "CoinScopeAI is an independent AI-driven infrastructure platform. Not affiliated with the COINSCOPE cryptocurrency token, coinscope.co, mycoinscope.com, or any other 'Coinscope'-named project."
}
```

The `disambiguatingDescription` field is the explicit Google-supported pattern for entities that collide on name; it earns rich-result surfacing of the disambiguation in many cases.

### 9C.5.6 Search-result-aware copy

Wherever a piece of copy could surface in a Google snippet (homepage, About, /not-the-token, blog post H1s), structure the first 155 chars to (a) name the entity unambiguously and (b) include one of the §9 v1 hero phrases so the snippet doubles as positioning. Example for the homepage:

> "CoinScopeAI is AI-driven capital-preservation infrastructure for crypto futures. Independent platform — not a token, not a signal group, not affiliated with similarly-named projects. Built for traders who already have a framework."

That opens with the entity, the value proposition, and the disambiguation in one breath. The brand-check skill in `coinscopeai-social-channels` plugin should pre-flight any new social post intended to surface in search against this template.

## 9C.6 Risks and counterarguments

| Risk | Mitigation |
|---|---|
| The token's holders attack us publicly for "stealing" their name. | Unlikely (we predate the rebrand of the engine to AI-positioning, and they are a token with a different audience). If it happens, we have the `disambiguatingDescription` and footer note as evidence of good-faith separation. |
| Our disambiguation copy reads as defensive / weak. | Tonal calibration. "Independent platform. Not affiliated with similarly-named projects." is matter-of-fact. Do not editorialize. |
| Option A doesn't move the needle and we suffix-shift in 6 months anyway. | The disambiguation work is not wasted — schema markup, on-site copy, and bio standardization all carry forward into any future name. |
| Suffix `-AI` becomes a liability if regulators tighten on AI claims. | Monitor; the validation-phase posture ("not production-ready") and absence of guaranteed-return claims pre-empts most AI-claim regulatory exposure. Revisit if circumstances change. |

## 9C.7 What this memo does NOT decide

- Logo or visual mark changes — out of scope; refer to §16 brand assets if/when that section exists.
- Pricing or tier renaming — locked in §6.6 / Track B.
- Communication of the disambiguation to existing customers — handled separately by §10 (operations) if customer-facing comms are required.
- Whether to actively contest the coinscope.co naming with cease-and-desist or trademark filings — separate legal track; this memo recommends evaluating but does not commit.

## 9C.8 Decision required

The operator to confirm Option A and authorize the §9C.5 execution checklist. Once confirmed, the new state belongs in `_decisions/decision-log.md` as a top-line entry dated 2026-05-17.

---

## 9C.9 Audit correction — internal state (added 2026-05-17, post logged-in audit)

The earlier sections of this memo, written before a logged-in audit was possible, implied a more fragmented internal brand state than actually exists. Anonymous fetchers had returned partial signals — a Facebook page named "Coin$cope" with a `coinscopeai2024` Instagram link in its About section, a second Facebook URL with different ID digits, a Threads archive of off-brand posts — that suggested multiple competing brand surfaces under our control. A logged-in pass corrected the picture. The truth is materially simpler than the earlier framing implied.

### 9C.9.1 Surface-by-surface state (verified)

| Surface | Followers | Last activity | Bio | Verified state |
|---|---|---|---|---|
| FB page `61558636955562` | 24 | Cover updated 2026-04-18 | On-brand: *"AI-driven quantitative research for crypto markets. Rule-based models, published methodology, ongoing validation. Not investment advice."* | Page name is "Coin$cope" (with dollar sign — typo from original setup, not a deliberate sub-brand). Linked to `@coinscopeai_` at the platform-connection level. About-section Instagram link is stale, pointing at non-existent `coinscopeai2024`. |
| FB URL `277949255409326` | — | — | — | **Redirects to the page above.** Same page, just an older URL format. There are not two FB pages. |
| IG `@coinscopeai_` | 5 | Unknown precisely (logged-in pass did not deep-fetch the grid) | On-brand: *"Institutional-grade AI for crypto futures. ML signals · risk-gated · regime-aware. Capital preservation first. Testnet · …"* | 23 posts in archive. Address in Amman, Jordan 11194. Connected to the Coin$cope FB page and "1 more." Confirmed by logged-in nav. |
| IG `@coinscopeai2024` | n/a | n/a | n/a | **Does not exist.** Instagram returns "Sorry, this page isn't available." The handle either was renamed to `@coinscopeai_` at some point, or was a typo that never resolved. The reference in the FB About section is a broken link. |
| Threads `@coinscopeai_` | 1 | **2024-11-10** (~18 months stale at audit time) | On-brand: *"Institutional-grade AI for crypto futures. ML signals · risk-gated sizing · regime-aware. Capital preservation first. Profit second. Every trade gat[ed]…"* | 4 visible posts from 2024-09-28 through 2024-11-10. Voice in posts is pre-PCC-v2 hype (memecoin promotion, return promises, urgency, price predictions). Onboarding prompt "Finish your profile" still shows — the profile was never fully completed. |
| YouTube `@CoinScopeAI` | 1 subscriber | 1 video uploaded ever | On-brand: *"CoinScopeAI is an institutional-grade, AI-driven quant trading system for crypto futures — built to give individual traders the discipline of a quant desk."* | Description points at `app.coinscope.ai`. Channel is essentially greenfield. |

**Total reach across all owned surfaces: ~31 followers/subscribers combined.** CoinScopeAI has not yet meaningfully launched on social. This is greenfield, not a "recover from messy archive" situation.

### 9C.9.2 What the audit collapsed

| Earlier assumption | Verified reality |
|---|---|
| Two Facebook pages under our control | One page (the second URL redirects to the first) |
| Two Instagram handles requiring migration | One handle (`coinscopeai2024` does not exist) |
| "Coin$cope" is a sub-brand or deliberate stylization | Page-name typo, operator has confirmed it should be fixed |
| Brand mark fragmentation across surfaces | All surfaces use "CoinScopeAI" in their bios and connected-account labels |
| Off-brand post archive across multiple channels | Off-brand archive limited to 4 Threads posts from Sep–Nov 2024 |
| Internal fragmentation as a major problem | Cosmetic only — five operator fixes, total time ~10 minutes |

The external-collision findings (§9C.1, §9C.2, §9C.4) are unchanged. The recommendation in §9C.4 (Option A — aggressive disambiguation, no rename) still stands.

### 9C.9.3 Revised operator-only checklist

These five fixes, all operator-action (MCP cannot perform them as they fall under "modifying security/account settings" — explicit-permission class). Operator confirmed on 2026-05-17 that the page is owned within a Meta Business Manager account (`business_id=488076572006371`, `asset_id=277949255409326`), which informs the menu paths below — the page is a business asset, not a personal profile, so name changes route through the Business Suite review queue.

**Summary:**

| # | Surface | Action | Tool | Expected time |
|---|---|---|---|---|
| 1 | FB page | Rename "Coin$cope" → "CoinScopeAI" | Meta Business Suite | 2 min (then Meta review ~few days) |
| 2 | FB page | Fix stale Instagram references (platform connection + public About link) | Meta Business Suite + Business Settings | 3 min |
| 3 | Threads | Delete the 4 posts from 2024-09-28 through 2024-11-10 | Threads app/web (not in BM) | 2 min |
| 4 | Threads | Complete the "Finish your profile" onboarding (profile photo, first new post) | Threads app/web | 5 min |
| 5 | Website (coinscope.ai) | Update `<title>` and `<meta name="description">` to match PCC v2 hero copy per §9 v1 | Web CMS / code repo | Owner-dependent |

Items 1–2 are inside Meta. Items 3–4 are inside Threads (Meta-owned but separately tooled). Item 5 is the marketing site. Item 5 remains the highest-leverage single fix: Google's SERP snippet is what every prospect sees first, and it currently advertises a positioning we no longer hold.

#### 9C.9.3.1 Where each fix lives — Meta surface split

Meta has split tooling and the menu paths matter:

- **Business Manager / Meta Business Suite** (`business.facebook.com`) — for Facebook page and Instagram business-account management. Used for fixes #1 and #2.
- **Threads** (`threads.com` or the app) — Threads is Meta-owned but does not yet expose post management or onboarding through Business Manager. Used for fixes #3 and #4.
- **Web CMS / code repository** — outside Meta entirely. Used for fix #5.

#### 9C.9.3.2 Fix #1 detail — page rename via Meta Business Suite

1. From the Business Manager URL the operator confirmed (`business.facebook.com/latest/home?asset_id=277949255409326`), click the grid icon (top-left) → **Meta Business Suite**.
2. Confirm the page selector (top-left of Business Suite) shows the Coin$cope page. Switch to it if not.
3. Left sidebar → **Settings** (gear, usually bottom of sidebar).
4. **Business assets → Pages → [Coin$cope]**.
5. **Page info → Name → edit to `CoinScopeAI` → Save**.

**Notes:**

- Meta queues the rename for review. Approval is typically a few days; occasionally immediate.
- Meta caps how often a page name can be changed per year. Type carefully on the first try.
- If the exact menu path differs (Meta UI drifts), the keyword to search inside Business Suite settings is "Page name" or "Page info." The control always lives under page-asset settings, never under business-account settings.

#### 9C.9.3.3 Fix #2 detail — Instagram references (two sub-fixes)

**2a. Platform-level Instagram connection** (controls cross-posting, message routing, ad integration, API access):

1. `business.facebook.com/settings`.
2. Left sidebar → **Accounts → Instagram accounts**.
3. Verify `@coinscopeai_` is listed and that it is the only Instagram asset connected to the Coin$cope page (per the operator's earlier screenshot, this is already the platform-level connection — this step is just verification).
4. If `@coinscopeai2024` appears anywhere as a stale connected asset, remove it. (Likely absent since that handle no longer exists, but worth confirming.)

**2b. Publicly-displayed Instagram link in the page About section** (what humans see when visiting `facebook.com/[page]`):

1. Meta Business Suite → page selector showing the Coin$cope page.
2. Settings → **Page info → Contact and basic info** (or the "Other accounts" / "Social links" subsection — exact label varies by Business Suite version).
3. Locate the **Instagram** field — currently displays `coinscopeai2024`.
4. Change to `coinscopeai_` → Save.

**Both 2a and 2b matter:** 2a fixes the underlying platform link used by APIs and Meta's own routing. 2b fixes what visitors see on the public page. The audit found 2b broken (link points at a non-existent handle); 2a is already correct per the operator's screenshot.

#### 9C.9.3.4 Fix #3 detail — Threads post deletion

Threads does not currently expose post management through Business Manager. Do this in the Threads app or at `threads.com`:

1. Sign in to Threads as `@coinscopeai_`.
2. Profile → scroll to each of the four target posts:
   - 2024-11-10 — Arabic Trump/BTC post (`#cryptocurrency #bitcoins #makemoney`)
   - 2024-10-01 — Memecoin promotion (NEIRO, KENDU, ROOST, BULL; `#MemeCoins #ToTheMoon`)
   - 2024-09-29 — Bitcoin $64,500 prediction (`#BitcoinAnalysis #CryptoMarket`)
   - 2024-09-28 — Crypto investment hype ($TAO, $Rio, $Velo; `#CryptocurrencyInvestment #CryptoTips`)
3. For each: three-dot menu → **Delete** → confirm.

Each post violates one or more brand-check BLOCK rules per `13-skills/skills_src/coinscopeai-social-channels/skills/brand-check/references/brand-rules.md` (delivered via the social plugin shipped 2026-05-17). Leaving them up contradicts every channel bio.

#### 9C.9.3.5 Fix #4 detail — Threads onboarding completion

Also in the Threads app/web. The audit found the "Finish your profile" card still visible on the @coinscopeai_ profile, indicating the original migration to PCC v2 voice never completed the onboarding flow.

Outstanding items on the onboarding card (per the 2026-05-17 capture):

- Add bio — *already done; clarify if the card is stale or if a longer bio is being requested*
- Create thread — first new post, on-brand, drafted via the plugin's `draft-post` skill
- Follow 10 profiles — surface CoinScopeAI's actual peer group (researchers, builders, anti-hype voices), not generic "crypto influencer" follow lists
- Add profile photo — confirm the logo asset is the canonical mark (also relevant once §9C.5.3 brand-asset standardization lands)

#### 9C.9.3.6 Fix #5 detail — website meta description

Outside Meta. Wherever `coinscope.ai` is hosted (Next.js / WordPress / Webflow / static / etc.), update the `<title>` and `<meta name="description">` tags in the marketing site's `<head>`.

Suggested copy aligned with §9 v1 hero copy (Set Alpha) and the disambiguation language from §9C.5.6:

```html
<title>CoinScopeAI — Capital-preservation infrastructure for crypto futures</title>
<meta name="description" content="AI-driven capital-preservation infrastructure for crypto futures. Rule-based models, published methodology, ongoing validation. Independent platform — not affiliated with similarly-named tokens or projects.">
```

**After deploying:**

1. Request a Google re-crawl via Search Console (URL Inspection → Request indexing) so the new snippet propagates faster than the default crawl cycle.
2. Confirm the snippet update with a fresh `site:coinscope.ai` query in incognito search after ~24-72 hours.

This is the highest-leverage single fix in the entire checklist — every prospect, journalist, and investor who Googles the brand sees this snippet first.

#### 9C.9.3.7 Bonus Business Manager cleanup (compounds; non-blocking)

While inside Business Manager for fixes #1 and #2, five minutes of additional cleanup that reinforces the §9C strategy:

| Item | Path | Reason |
|---|---|---|
| Verify page category | Meta Business Suite → Settings → Page info → Categories | Currently "Software / Internet company." Consider adding or switching to "Financial service" if regulatory positioning would benefit. |
| Verify page admin roles | Business Settings → Users → People | Confirm only intended people have admin. Remove legacy or test accounts. |
| Claim the page username (vanity URL) | Meta Business Suite → Settings → Page info → Username | Claim `@coinscopeai` (or equivalent) if available — affects the `facebook.com/coinscopeai` vanity URL. Affects §9C.5.5 schema markup `sameAs` list. |
| Business verification | Business Settings → Security Center → Business verification | If not yet completed. Useful for crypto/fintech credibility and unlocks Meta's verified-business pathways and ad-account capabilities. |
| WhatsApp Business linkage | Business Settings → Accounts → WhatsApp Accounts | The +962 7 7995 5210 number in the About is already a contact field; connecting it as a WhatsApp Business account routes inbound messages through BM Inbox and enables shared-team responses. |

#### 9C.9.3.8 Recommended order of operations (single sitting)

1. **Threads cleanup first** (5 min) — delete the 4 old posts (Fix #3). Removes the worst public liability immediately.
2. **Website meta description** (CMS-dependent) — highest-leverage single fix. Deploy, then submit for Google re-crawl.
3. **BM page rename** (Fix #1) — kick off Meta's async review queue early so the approval lands by the time content publishes.
4. **BM Instagram link fix** (Fix #2, both 2a and 2b) — quick wins, no review queue.
5. **Bonus BM cleanup** (§9C.9.3.7) — at operator discretion.
6. **Threads onboarding completion** (Fix #4) — schedule with first new post draft.
7. **Start publishing** — bios are already on-brand across every channel; the `coinscopeai-social-channels` plugin's `draft-post` + `brand-check` skills are ready. Begin with a measured cadence per channel per `content-calendar` defaults.

### 9C.9.4 What this does not change

- The external-collision picture (coinscope.co, COINSCOPE token, brand-name collisions in SERP) is unchanged. §9C.4 Option A recommendation still stands.
- The on-site disambiguation work (§9C.5.1, §9C.5.5) — schema markup, `disambiguatingDescription`, `/not-the-token` page, footer note — is still recommended and still high-leverage.
- §9 v1 pillars are unchanged.
- The plugin `coinscopeai-social-channels` v0.1.0 (shipped 2026-05-17) is ready to use as soon as the five fixes above are complete.

### 9C.9.5 Implication for §15 (investor narrative) and §7 (GTM)

The audit confirms what §7 already assumes: validation phase is pre-launch in distribution terms. The ~31-follower count is consistent with a product still in validation — there is no narrative-cleanup needed for prospects, only narrative *construction*. Investor due-diligence Googling will hit the website snippet first; that's the one urgent fix. The social channels themselves are too small to either help or hurt at this stage; what matters is that when they start producing content, the content matches the §9 pillars from post #1.

### 9C.9.6 Self-correction note

This memo's first draft over-stated the problem. The remediation path is materially smaller than implied. Authors of subsequent supplements should run a logged-in audit before extrapolating from anonymous-fetch signals — anonymous reads of Meta and YouTube surfaces are reliable for bios and metadata, unreliable for follower counts, post archives, and platform-level account connections.

---

**Open questions for the operator before lock:**

1. Trademark status: is "CoinScopeAI" registered or in process? If yes — where? If no — is filing a near-term priority? (Affects how aggressively we can use disambiguation language without escalating into IP litigation territory.)
2. The COINSCOPE token: is there any prior contact, partnership, or shared history with the issuer that complicates a clean "not affiliated" disambiguation? Confirming a clean separation is the assumption underlying this memo.
3. Should we add a /press or /brand-assets page as part of 9C.5.1 to give external writers and journalists a single canonical source for the brand name, logo, and disambiguation language? Recommended as a small additional task with high downstream leverage.
4. (New) Confirm timing for the five §9C.9.3 fixes. Item 5 (website meta) is the urgent one. Items 1–4 can be batched together in a single 10-minute pass.
