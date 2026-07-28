#!/usr/bin/env python3
"""
Adds the GitHub MCP server to ~/.claude.json.
Run: python3 add_github_mcp.py
It will prompt you to paste the token — no shell quoting issues.
"""
import json, pathlib, sys

config_path = pathlib.Path.home() / ".claude.json"

print("Paste your GitHub PAT (ghp_...) and press Enter:")
pat = input().strip()

if not pat.startswith("ghp_"):
    print(f"ERROR: Token should start with 'ghp_', got: {pat[:10]}...")
    sys.exit(1)

with open(config_path) as f:
    config = json.load(f)

if "mcpServers" not in config:
    config["mcpServers"] = {}

config["mcpServers"]["github"] = {
    "type": "http",
    "url": "https://api.githubcopilot.com/mcp",
    "headers": {
        "Authorization": f"Bearer {pat}"
    }
}

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print(f"✅ Done. Token stored: {pat[:10]}...{pat[-4:]}")
print("Run: claude mcp list")
