# ONBOARDING — Signup-to-Exchange-Connection Flow

**Task:** `[DOC] ONBOARDING — Signup-to-Exchange-Connection Flow`
**Type:** NOW
**Owner:** Design + Eng + Founder
**Status:** DRAFT v0.1 — step-by-step spec + branching rules
**Anchored to:** `01-first-time-user-journey.md` gates 1–3; §6.5 Free Scope B (account-verified); §3.5 sub-$5k branch; memory `project_jurisdictional` (US-blocked, UAE sole prop); PCC v2 §8 (testnet-first); Scoopy custom instructions (Binance Testnet only currently); `_packaging/05-packaging-friction-review.md` Class C anti-patterns.
**Feeds decisions:** **On-1**, **On-4**, **On-5**.

---

## 1. The flow at-a-glance

The signup-to-exchange-connection flow has **9 explicit steps** (each a UI state) plus **4 branching rules**. Steps are ordered; branching rules are evaluated at the indicated step. A user must pass every step (with appropriate branching) to reach `signup.exchange_connected` (F-2).

```
[1] Region check
    ├─ US/blocked → END (region-block copy)
    └─ Allowed →
[2] Signup form (email + password)
[3] Email verification link
[4] Welcome page + exchange-connect intro
[5] Exchange selection (Binance USDT-M only at P1)
[6] Testnet vs mainnet toggle
[7] API key entry (read-only scope explanation)
[8] API key validation + account-balance read
[9] Branch evaluation:
    ├─ Account size <$5k → Sub-$5k branch UI
    └─ Account size ≥$5k → Standard onboarding
        → F-2 instrumented → proceed to first-value (gate 4)
```

---

## 2. Step-by-step spec

### Step 1 — Region check (pre-signup)

**State:** Before any account creation friction.

**Implementation:** IP-based geolocation hint at landing-page CTA click. Not a hard block at the network level (server-side validation happens at signup form submit), but a UX preview that prevents wasted onboarding time.

**Allowed regions (P1):** UAE / MENA / EU / global EN markets (per Phase 1 jurisdictional posture).

**Blocked regions (P1):** US (federal). Specific other jurisdictions added per memory `project_jurisdictional` updates.

**UX:**

- Allowed: continue to Step 2 silently.
- Blocked: render copy "CoinScopeAI is not currently available in your region." + brief explanation + "Be notified when we expand" email-capture (optional).

**Anti-patterns avoided:**

- Letting US user complete signup, then blocking at exchange-connect (Class C — region restrictions discovered post-onboarding).
- Showing region-restricted pricing without disclosing restriction.

**Server-side enforcement:** Signup endpoint validates region against IP + (REQUIRED INPUT — Eng confirm) any user-claimed country. Region falsification at this step is acceptable user agency; we don't add KYC at v1 to enforce.

### Step 2 — Signup form

**State:** Post region-check.

**Fields:**

- Email (required)
- Password (required, min 12 chars per security baseline; REQUIRED INPUT — confirm baseline)
- "I agree to the [Terms of Service] and [Privacy Policy]" checkbox (required)
- Optional: country self-select (defaults to IP-detected region)

**Not on the form:**

- Marketing opt-in checkbox at signup. Per `_pricing/02` Principle 4 (anti-pressure) — opt-in is offered post-activation, not at the friction-laden signup moment.
- Persona self-classification. (Phase 1 ICP `Persona Fit Scoring Model` will eventually instrument this elsewhere; not at signup.)
- Phone number. (Not required for v1; Telegram bot handles 2FA-style notifications post-signup if user opts in.)

**Brand voice:** product-tier — terse, technical, declarative. Form labels are functional ("Email," "Password"), not encouraging ("Join the community!"). Per Scoopy custom instructions.

### Step 3 — Email verification

**State:** Post signup-form submit.

**Implementation:** Magic-link via email (no 6-digit code). Link expires in 24 hours.

**UX:**

- Confirmation page: "Check [email] for a verification link."
- Email content: subject line "Verify your CoinScopeAI account"; body is single-paragraph functional + the link. No marketing copy. Per Scoopy product-tier register.
- Click → account marked email-verified → `signup.email_verified` event fires → redirect to Step 4.
- Resend: button on confirmation page, rate-limited to 1 per minute.

**Anti-patterns avoided:**

- Auto-redirecting to dashboard before email verification (creates orphan accounts).
- Pre-populating account features before verification (confuses Free Scope B definition).

### Step 4 — Welcome page + exchange-connect intro

**State:** Post email-verify, pre exchange-connect.

**Purpose:** Tell the user, in one screen, what they're about to do and why. Anti-overclaim discipline applied.

**Content:**

```
Welcome to CoinScopeAI.

To activate your Free account, connect a Binance USDT-M futures account 
with a read-only API key. We use this to:

  • Verify your account exists and read your account balance.
  • Show you the demo-trade gate decisions on your account context.

We never:

  • Place orders.
  • Execute trades.
  • Withdraw funds.
  • Access funds in any way.

Testnet only. 30-day validation phase. No real capital.

[Continue to exchange connect]
```

**Brand voice:** product-tier — declarative, evidence-led. The "We never" block is the load-bearing trust signal at this step.

**No upsell.** No "Upgrade to Trader for live trading" CTA on this page. Conversion comes after first-value, not before.

### Step 5 — Exchange selection

**State:** Post welcome.

**P1 reality:** Binance USDT-M only.

**UX:**

- Single option visible: "Binance USDT-M Futures" with logo + "Selected."
- Other venues shown as "Bybit — coming Aug 2026" / "Other venues — coming Q4 2026" (per memory `project_phased_rollout` P2 phase).
- Disabled state is explicit; no false-promise of immediate availability.

**Anti-pattern avoided:** Listing venues as "available" that aren't actually integrated yet.

### Step 6 — Testnet vs mainnet toggle

**State:** Post exchange selection.

**Default:** Testnet selected.

**UX:**

```
[●] Connect Binance Testnet account
[ ] Connect Binance Mainnet account (read-only)

Why testnet first?
We're in our 30-day validation phase. The system runs against real market 
data but executes only on testnet. Your mainnet API key, if used, is 
read-only — we read your account balance and positions to provide 
context for demo-trade gate decisions. We never place orders.

Production Candidate Criteria v2 §8 governs when any real-capital path 
opens.
```

**Both paths are valid:**

- Testnet path: user creates a Binance Testnet account if needed (link to Binance docs); enters Testnet API key. Account size detected from testnet balance.
- Mainnet path: user enters mainnet API key (read-only scope only). Account size detected from mainnet balance for §3.5 sub-$5k branch evaluation. **System does not place orders on mainnet, ever, until PCC v2 §8 gates pass.**

**Why offer mainnet at all in validation phase?**

- §6.5 Scope B: account verification at signup, *verified exchange account at any size*. Sub-$5k branch evaluation requires reading the account-size band, which testnet doesn't represent.
- Mainnet read-only is the realistic data context for demo-trade gate decisions to be meaningful. Without it, gate decisions are abstract.
- PCC v2 §8 still governs *execution* — mainnet read is not mainnet execute. Anti-overclaim discipline preserved.

**REQUIRED INPUT — Eng confirm:** does current product implementation enforce read-only-only API key scope at the API-call level? If user enters a write-scope API key, what happens?

### Step 7 — API key entry

**State:** Post testnet/mainnet selection.

**Fields:**

- API Key (required)
- API Secret (required)
- "I confirm this API key has read-only permissions" checkbox (required for mainnet path; auto-checked for testnet)

**Inline help:**

- "How to create a read-only API key" link → Binance docs (separate tab, per anti-pattern guard against linking competitive surfaces in our own UI without provenance).
- IP-restriction recommendation: "For added security, restrict your API key to our IPs: [IP LIST]." (REQUIRED INPUT — confirm we publish a static IP allowlist for Eng-side outbound API calls.)

**Brand voice:** product-tier. Functional. No "Almost there!" social-tier copy.

### Step 8 — API key validation + account-balance read

**State:** Post API key submit.

**Implementation:** Server-side validation:

1. API key authenticates against Binance Testnet or Mainnet endpoint.
2. Account balance read — returns USD-equivalent balance for sub-$5k branch evaluation.
3. (REQUIRED INPUT — Eng confirm) optional: scan account for any open positions; if positions exist, surface them in the demo-trade gate decision view.

**Failure modes:**

| Failure | UX |
|---|---|
| API key invalid | "API key not recognized. Verify the key + secret are copied exactly. [Help link]" |
| API key has write permissions | "API key has trade permissions. For your safety, please create a read-only key." Block. Do not proceed. |
| API key not yet activated by Binance | "Binance is still activating your key. Try again in 30 seconds." Auto-retry once after 30s. |
| Network error | "Couldn't reach Binance. Try again." Retry button. |

**Success:** `signup.exchange_connected` event fires with `{ exchange: "binance_usdt_m", account_size_band, testnet_or_mainnet }`. Account-size band assigned per §3.

### Step 9 — Branch evaluation

**State:** Post API key validation.

**Branching logic:**

```python
if account_size_band < $5k:
    return SubFiveKBranch  # Same Free UI, "we'll be back" copy persistent
else:
    return StandardOnboarding  # Same Free UI, no special copy
```

Both branches proceed to **gate 4 (first value)**. The branch determines persistent in-product copy + KPI segmentation, not feature access.

---

## 3. The four branching rules

| # | Rule | Triggered at | Effect |
|---|---|---|---|
| 1 | **Region block** | Step 1 | END if blocked; copy + waitlist email |
| 2 | **Mainnet-vs-testnet** | Step 6 | Branch determines API endpoint + account-size source |
| 3 | **Sub-$5k branch** | Step 9 | Branch determines persistent in-product copy + KPI cohort tag |
| 4 | **Write-permission API key** | Step 8 validation | Block; user must create read-only key |

---

## 4. Sub-$5k branch UX (per On-4)

Per **On-4** option (a) — recommended:

| Element | Sub-$5k Free user sees | Standard Free user sees |
|---|---|---|
| First-value page (gate 4) | Identical: top-5 signals + regime label + demo gate | Identical |
| Persistent in-product banner | "We'll be back for you when your account crosses $5k. Trader unlocks then." (single line, top of dashboard, dismissible per session) | Not shown |
| "Notify me" CTA | "Notify me when my account reaches $5k" (opt-in, single click) | Not shown |
| Trader-tier upgrade prompts | None (no upgrade pressure per §3.5) | Standard quiet inline prompts per `_packaging/04` §3 |
| Conversion trigger | Account-balance event (account crosses $5k threshold) | Standard funnel |
| KPI cohort tag | `sub_5k` cohort | Default cohort |

**Anti-pattern guard:** sub-$5k users do NOT see different (tighter) features. NO "you're a casual trader" copy. NO paywall pressure. Same Free Scope B; different cohort framing.

---

## 5. Region-block UX (per On-5)

Per **On-5** option (a) — recommended:

**Pre-signup (Step 1):** IP geolocation hint. If US:

```
CoinScopeAI is not currently available in your region.

We're a UAE-based sole proprietorship with global English-language reach 
in MENA, Europe, and other markets. US availability is not on our 
roadmap at this time.

[Be notified if we expand]   [Learn about our methodology]
```

**No fallback:** US users cannot proceed to signup. Hard block.

**Anti-pattern avoided:**

- Letting US user complete email verification + exchange-connect, then blocking. Wastes their time and ours.
- Hiding the restriction. The pricing page should also surface the region restriction in the footer to prevent surprise.

---

## 6. API key flow (per On-1)

Per **On-1** option (a) — recommended: email + read-only Binance API key required at signup.

**Why required, not deferred:**

- §6.5 Scope B is account-verified. Deferring exchange-connect to first signal interaction breaks the Scope B definition.
- Demo-trade gate decision view (the trust demo) requires account context. Without account-connect, the gate decision is abstract.
- Sub-$5k branch instrumentation requires account-size detection. Account-size is read at exchange-connect.
- Future PCC v2 §8 gate-pass real-capital path needs the account already connected; deferring it adds friction at the most critical conversion moment.

**Why read-only:**

- We never place orders during validation phase. Read-only API key is the technical guarantee.
- Anti-overclaim discipline: claiming "we never trade for you" is credible only if the system *cannot* trade for you.
- Class C anti-pattern (auto-converting trial with card-on-file) is the analog here — write-permission API key is the equivalent of a card-on-file with broad authorization.

**Why Binance USDT-M only at P1:**

- Per memory `project_phased_rollout` — P1 narrow ship vendor stack is CCXT 4-exchange + Binance USDT-M execution. Multi-venue execution is P2 (Aug-Sep 2026).
- Listing other venues at signup as "available" violates anti-overclaim discipline.

---

## 7. Failure modes specific to this flow

- **Region check happens after signup form.** US user enters email + password, then sees the block. Class C anti-pattern. **On-5 default avoids.**
- **Write-permission API key accepted.** Breaks "we never place orders" trust signal at the technical level. **Step 8 validation blocks.**
- **Email verification skipped.** Orphan accounts; activation funnel KPIs misleading. Required.
- **Account-size band not detected.** Sub-$5k branch can't fire; §3.5 anti-persona stance fails operationally. Step 8 must read account balance.
- **Exchange-connect deferred to first signal interaction.** §6.5 Scope B broken; trust demo abstract; sub-$5k branch breaks. **On-1 default avoids.**
- **Testnet-vs-mainnet toggle hidden.** User defaults to mainnet without realizing; PCC v2 §8 anti-overclaim discipline weakened. Toggle visible at Step 6.
- **API key entry without read-only-scope confirmation checkbox.** User confirms blindly; later disputes about API permissions. Checkbox is friction-with-purpose.
- **"Almost done!" / "You're so close!" copy** in any step. Social-tier register; violates Scoopy product-tier rule.
- **Marketing opt-in checkbox at signup.** Anti-pressure violation per `_pricing/02` Principle 4. Defer to post-activation.

---

## 8. Time-to-completion targets

| Step | Target time | Anti-target |
|---|---|---|
| Step 1 (region check) | <2s | >5s = blocked or false-positive |
| Step 2 (signup form) | <60s | >5min = abandonment |
| Step 3 (email verify) | <5min wall-clock | >24h = lost |
| Step 4 (welcome) | <30s read | Skipped = trust-signal lost |
| Step 5 (exchange select) | <15s | >60s = confusion |
| Step 6 (testnet/mainnet) | <60s | >5min = decision-paralysis |
| Step 7 (API key entry) | <5min including key creation in Binance | >30min = drop-off |
| Step 8 (validation) | <10s server-side | >30s = network failure mode |
| Step 9 (branch eval) | <2s | Server-side, invisible to user |
| **Total signup → exchange-connected** | **<15 minutes target** (per `01-first-time-user-journey.md` §3) | **>24h = abandoned funnel** |

---

## 9. Anti-overclaim audit on this flow

| Surface | Audit element | Pass condition |
|---|---|---|
| Step 1 region-block copy | "Not currently available" — no "we'll be in your region soon" promise | "Not on roadmap at this time" |
| Step 4 welcome page | "We never trade / execute / withdraw" + validation disclaimer + PCC v2 §8 reference | All four present |
| Step 5 exchange selection | Other venues shown as "coming [date]" not "available" | Disabled state with date |
| Step 6 testnet/mainnet copy | PCC v2 §8 referenced; mainnet path explicitly read-only | Both present |
| Step 7 API key entry | Read-only scope checkbox required; IP-restriction recommendation | Both present |
| Step 8 validation | Write-permission API key blocked, not silently accepted | Block + clear error |
| Step 9 sub-$5k branch | "We'll be back" framing; no paywall pressure | §3.5 + `_packaging/02` §3 alignment |
| All steps | No "Almost there!" social-tier copy | Product-tier register throughout |

---

## 10. What this unlocks

- **On-1** can be marked recommended at "email + read-only Binance API key required at signup."
- **On-4** can be marked recommended at "same Free UI + persistent 'we'll be back' copy."
- **On-5** can be marked recommended at "pre-signup region check with copy."
- `[QA] ONBOARDING — Friction Audit Across Current Flow` has the canonical 9-step + 4-rule spec to audit against.
- `[DOC] ONBOARDING — First Value Experience Design` consumes the "post Step 9" handoff as its starting point.
- ONBOARDING NEXT `Onboarding Copy Pack` consumes every copy block in §2 as canonical.
- Eng has a deterministic spec with REQUIRED INPUT items called out (read-only API enforcement; static IP allowlist; password baseline; account-size detection at Step 8).
