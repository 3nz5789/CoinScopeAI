import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";

import { registerScanTool } from "./tools/scan.js";
import { registerPerformanceTool } from "./tools/performance.js";
import { registerJournalTool } from "./tools/journal.js";
import { registerRiskGateTool } from "./tools/risk-gate.js";
import { registerPositionSizeTool } from "./tools/position-size.js";
import { registerRegimeTool } from "./tools/regime.js";
import { ENGINE_BASE_URL } from "./constants.js";

const server = new McpServer({ name: "coinscope-mcp-server", version: "1.0.0" });

registerScanTool(server);
registerPerformanceTool(server);
registerJournalTool(server);
registerRiskGateTool(server);
registerPositionSizeTool(server);
registerRegimeTool(server);

async function runStdio(): Promise<void> {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error(`[coinscope-mcp-server] stdio transport — engine: ${ENGINE_BASE_URL}`);
}

async function runHttp(): Promise<void> {
  const app = express();
  app.use(express.json());
  app.get("/health", (_req, res) => {
    res.json({ status: "ok", server: "coinscope-mcp-server", version: "1.0.0" });
  });
  app.post("/mcp", async (req, res) => {
    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: undefined,
      enableJsonResponse: true,
    });
    res.on("close", () => transport.close());
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  });
  const port = parseInt(process.env.PORT ?? "3100", 10);
  app.listen(port, () => {
    console.error(`[coinscope-mcp-server] HTTP on :${port}/mcp — engine: ${ENGINE_BASE_URL}`);
  });
}

const transport = process.env.TRANSPORT ?? "stdio";
if (transport === "http") {
  runHttp().catch((err: unknown) => { console.error(err); process.exit(1); });
} else {
  runStdio().catch((err: unknown) => { console.error(err); process.exit(1); });
}
