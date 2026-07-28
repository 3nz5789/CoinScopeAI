# Browser Agent

A lightweight headless browser automation CLI built on Playwright. It is
designed to be invoked by Kimi Code CLI via `Bash` so the model can perform
real browser tasks (navigation, text extraction, screenshots, form filling,
JavaScript evaluation) even though Kimi Code CLI does not load MCP servers.

## Setup

Already done by the assistant:

```bash
cd tools/browser
npm install
npx playwright install chromium
```

## Usage

```bash
cd tools/browser

# Navigate and return page metadata
node browser_agent.js '{"action":"navigate","url":"https://example.com"}'

# Extract visible text
node browser_agent.js '{"action":"extract_text","url":"https://example.com"}'

# Take a screenshot
node browser_agent.js '{"action":"screenshot","url":"https://example.com","output":"/tmp/example.png"}'

# Click an element
node browser_agent.js '{"action":"click","url":"https://example.com","selector":"button#submit"}'

# Fill a form field
node browser_agent.js '{"action":"fill","url":"https://example.com","selector":"input[name=q]","value":"hello"}'

# Evaluate JavaScript in the page context
node browser_agent.js '{"action":"evaluate","url":"https://example.com","script":"document.title"}'
```

## Notes

- Runs headless by default. Set `"headless": false` to see the browser window.
- Output is always JSON.
- If a site blocks headless Chrome, try `"userAgent": "..."` or a residential proxy.
