#!/usr/bin/env node
"use strict";

/**
 * Browser Agent CLI
 * =================
 * Lightweight Playwright wrapper for headless browser automation.
 *
 * Usage:
 *   node browser_agent.js '{"action":"navigate","url":"https://example.com"}'
 *   node browser_agent.js '{"action":"extract_text","url":"https://example.com"}'
 *   node browser_agent.js '{"action":"screenshot","url":"https://example.com","output":"/tmp/page.png"}'
 *   node browser_agent.js '{"action":"click","url":"https://example.com","selector":"button#submit"}'
 *   node browser_agent.js '{"action":"fill","url":"https://example.com","selector":"input[name=q]","value":"hello"}'
 *   node browser_agent.js '{"action":"evaluate","url":"https://example.com","script":"document.title"}'
 *
 * Output is always JSON to stdout.
 */

const { chromium } = require("playwright");

function fail(message, extra = {}) {
  console.log(JSON.stringify({ ok: false, error: message, ...extra }, null, 2));
  process.exit(1);
}

function ok(payload) {
  console.log(JSON.stringify({ ok: true, ...payload }, null, 2));
}

async function run(config) {
  const action = config.action || "navigate";
  const url = config.url;
  if (!url) fail("missing 'url' in config");

  const headless = config.headless !== false;
  const browser = await chromium.launch({ headless });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    userAgent:
      config.userAgent ||
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
  });
  const page = await context.newPage();

  try {
    const response = await page.goto(url, {
      waitUntil: config.waitUntil || "networkidle",
      timeout: config.timeout || 30000,
    });

    if (action === "navigate") {
      ok({
        url: page.url(),
        title: await page.title(),
        status: response ? response.status() : null,
      });
    } else if (action === "extract_text") {
      const text = await page.locator("body").innerText({ timeout: 5000 });
      ok({ url: page.url(), title: await page.title(), text: text.trim() });
    } else if (action === "screenshot") {
      const output = config.output || "tools/browser/screenshot.png";
      await page.screenshot({
        path: output,
        fullPage: config.fullPage !== false,
      });
      ok({ url: page.url(), title: await page.title(), screenshot: output });
    } else if (action === "click") {
      if (!config.selector) fail("missing 'selector' for click action");
      await page.locator(config.selector).click({ timeout: config.timeout || 10000 });
      await page.waitForLoadState("networkidle");
      ok({ url: page.url(), title: await page.title(), clicked: config.selector });
    } else if (action === "fill") {
      if (!config.selector) fail("missing 'selector' for fill action");
      if (config.value === undefined) fail("missing 'value' for fill action");
      await page.locator(config.selector).fill(String(config.value));
      ok({ url: page.url(), title: await page.title(), filled: config.selector });
    } else if (action === "evaluate") {
      if (!config.script) fail("missing 'script' for evaluate action");
      const result = await page.evaluate((script) => eval(script), config.script);
      ok({ url: page.url(), title: await page.title(), result });
    } else {
      fail(`unknown action: ${action}`);
    }
  } catch (err) {
    fail(err.message, { stack: err.stack });
  } finally {
    await browser.close();
  }
}

async function main() {
  const raw = process.argv[2];
  if (!raw) fail("usage: node browser_agent.js '<json-config>'");

  let config;
  try {
    config = JSON.parse(raw);
  } catch (err) {
    fail(`invalid JSON: ${err.message}`);
  }

  await run(config);
}

main().catch((err) => fail(err.message, { stack: err.stack }));
