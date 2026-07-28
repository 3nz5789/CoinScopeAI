# Claude Prompting Guide

**Added to CoinScopeAI knowledge base:** 2026-05-11
**Source:** Anthropic prompting best practices
**Notion:** https://www.notion.so/35d29aaf938e81bf9f67d7db563471f4
**Drive ID:** `1OsWW_OtH2RDhkYrSyp2GAdr-3LcT4CRJ` (root → drag to `15 — Agent Workforce`)
**Purpose:** Reference for crafting effective prompts when working with Claude across Scoopy sessions, business-plan work, and ops tasks.

---

## General Tips for Effective Prompting

### 1. Be Clear and Specific

Clearly state your task or question at the beginning. Provide context and details. Break complex tasks into smaller, manageable steps.

**Bad prompt:**
> "Help me with a presentation."

**Good prompt:**
> "I need help creating a 10-slide presentation for our quarterly sales meeting. The presentation should cover our Q2 sales performance, top-selling products, and sales targets for Q3. Please provide an outline with key points for each slide."

---

### 2. Use Examples

Provide examples of the kind of output you're looking for. If you want a specific format or style, show an example.

**Bad prompt:**
> "Write a professional email."

**Good prompt:**
> "I need to write a professional email to a client about a project delay. Here's a similar email I've sent before: [example]. Help me draft a new email following a similar tone and structure, but for our current situation where we're delayed by a month due to supply chain issues."

---

### 3. Encourage Thinking

For complex tasks, ask Claude to "think step-by-step" or "explain your reasoning." This leads to more accurate and detailed responses.

**Bad prompt:**
> "How can I improve team productivity?"

**Good prompt:**
> "I'm looking to improve my team's productivity. Think through this step-by-step, considering: (1) current productivity blockers, (2) potential solutions, (3) implementation challenges, (4) methods to measure improvement. For each step, provide a brief explanation of your reasoning. Then summarize at the end."

---

### 4. Iterative Refinement

If the first response isn't quite right, ask for specific modifications. Be precise about what to change.

**Bad prompt:**
> "Make it better."

**Good prompt:**
> "That's a good start, but please refine it: (1) Make the tone more casual and friendly, (2) Add a specific example of how our product has helped a customer, (3) Shorten the second paragraph to focus on benefits rather than features."

---

### 5. Leverage Claude's Knowledge

Claude has broad knowledge across many fields. Provide relevant context so the response is targeted to your needs.

**Bad prompt:**
> "What is marketing? How do I do it?"

**Good prompt:**
> "I'm developing a marketing strategy for a new eco-friendly cleaning product line. Provide an overview of current trends in green marketing, including: (1) key messaging strategies for environmentally conscious consumers, (2) effective channels for reaching this audience, (3) examples of successful green marketing campaigns, (4) potential pitfalls to avoid such as greenwashing accusations."

---

### 6. Use Role-Playing

Ask Claude to adopt a specific role or perspective when responding.

**Bad prompt:**
> "Help me prepare for a negotiation."

**Good prompt:**
> "You are a fabric supplier for my backpack manufacturing company. I'm preparing to negotiate a 10% price reduction. As the supplier, provide: (1) three potential objections to our request, (2) a counterargument from my perspective for each, (3) two alternative proposals the supplier might offer. Then switch roles and advise how I, as the buyer, can best approach this negotiation."

---

## Task-Specific Tips

### Content Creation

- **Specify your audience** — who the content is for shapes tone, vocabulary, and structure.
- **Define tone and style** — professional, casual, humorous, brand-aligned, etc.
- **Define output structure** — provide an outline or list of points to cover.

### Document Summary and Q&A

- Be specific about what aspects or sections you want summarized.
- Refer to attached documents by name.
- Ask for citations — request that Claude cites specific parts in its answers.

### Data Analysis and Visualization

- Specify the desired output format — executive summary, tables, bullet points, charts.
- Ask for recommendations, not just description.
- Suggest visualization types that would be effective.

### Brainstorming

- Use Claude to generate lists of possibilities or alternatives.
- Be specific about topics, constraints, and categories.
- Request structured formats (bullet points, numbered lists, tables) for easier reading.

---

## Troubleshooting and Minimizing Hallucinations

1. **Allow Claude to acknowledge uncertainty** — tell Claude it's okay to say it doesn't know.
2. **Break down complex tasks** — if steps are being missed, work through them one message at a time.
3. **Include all contextual information** — Claude doesn't retain information between conversations; include all necessary context each time.

---

## CoinScopeAI Application Notes

When prompting Scoopy for CoinScopeAI work, apply the above principles with these additions:

- **State your phase** (P0 / P1 / P2 etc.) and the specific section or task.
- **Reference canonical thresholds** — don't let Claude guess; quote values from the system prompt or decision-log.
- **Specify sync scope** — tell Claude which platforms need updating (Drive / Notion / Linear / GitHub).
- **Ask for assumptions upfront** — Scoopy always states assumptions before acting; prompt it to do so explicitly if needed.
- **Use the Claude Code prompt playbook** (`claude-code-prompt-playbook.md`) for engine-level tasks.

---

*Source: Anthropic prompting best practices. Added to CoinScopeAI knowledge base 2026-05-11.*
