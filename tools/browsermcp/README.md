# BrowserMCP Setup

This directory documents how to run the BrowserMCP server locally and connect it
to an MCP-compatible client (Claude Desktop, Cursor, VS Code, Windsurf, etc.).

## Important limitation

The cloned source at `external/browsermcp-mcp/` **cannot be built standalone**
(it depends on internal packages from the BrowserMCP monorepo). Therefore, we
run the published npm package instead.

## 1. Install the Chrome extension

BrowserMCP requires a Chrome extension to connect to your browser.

1. Open Chrome and go to the **Chrome Web Store**.
2. Search for **"BrowserMCP"** or use the link from https://docs.browsermcp.io/setup-extension
3. Click **Add to Chrome** and pin the extension.
4. Click the BrowserMCP extension icon and follow the connection prompts.

You must complete this step manually — Chrome extensions cannot be installed
programmatically.

## 2. Start the MCP server

```bash
cd tools/browsermcp
npm start
```

This runs:
```bash
npx -y @browsermcp/mcp@latest
```

The server will start and wait for a connection from the Chrome extension.

## 3. Configure your MCP client

Add this server config to your MCP-compatible client:

```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "npx",
      "args": ["-y", "@browsermcp/mcp@latest"]
    }
  }
}
```

For clients that require an absolute path:

```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "/Users/mac/.nvm/versions/node/v24.15.0/bin/npx",
      "args": ["-y", "@browsermcp/mcp@latest"]
    }
  }
}
```

## 4. Use it

Once the extension is connected and the MCP server is running, you can ask your
client to perform browser tasks like:

- "Go to https://example.com and summarize the page"
- "Click the login button and enter my credentials"
- "Take a screenshot of the dashboard"

## Notes

- BrowserMCP uses your existing Chrome profile, so you stay logged into services.
- The server runs locally; no browser data is sent to remote servers.
- This setup does **not** integrate with Kimi Code CLI directly. Kimi Code CLI
  does not load arbitrary MCP servers. Use the Playwright agent at
  `tools/browser/` if you need browser automation from Kimi Code CLI.
