/**
 * Zone Tools - Get zone info, verify DNS propagation
 */

import { CloudflareClient } from "../cloudflareClient.js";
import { GetZoneParams, CheckPropagationParams, ToolResponse } from "../types.js";
import { promisify } from "util";
import { execFile as execFileCallback } from "child_process";

const execFile = promisify(execFileCallback);

export class ZoneTools {
  constructor(private client: CloudflareClient) {}

  /**
   * cloudflare_get_zone_info
   * Get zone details including nameservers and configuration
   */
  async getZoneInfo(params: GetZoneParams): Promise<ToolResponse> {
    try {
      const zone = await this.client.getZone(params.zone_id);

      return {
        success: true,
        message: "Zone information retrieved successfully",
        data: {
          id: zone.id,
          name: zone.name,
          status: zone.status,
          type: zone.type,
          paused: zone.paused,
          nameservers: zone.nameservers,
          original_nameservers: zone.original_nameservers,
          created_on: zone.created_on,
          modified_on: zone.modified_on,
        },
      };
    } catch (error) {
      return {
        success: false,
        message: "Failed to get zone information",
        error: error instanceof Error ? error.message : String(error),
      };
    }
  }

  /**
   * cloudflare_check_dns_propagation
   * Check if DNS records have propagated globally
   * Uses nslookup to query different nameservers
   */
  async checkPropagation(params: CheckPropagationParams): Promise<ToolResponse> {
    try {
      const domain = params.domain;
      const nameservers = [
        params.nameserver || "8.8.8.8", // Google DNS
        "1.1.1.1", // Cloudflare DNS
        "208.67.222.222", // OpenDNS
      ];

      const results: Record<string, any> = {};

      for (const ns of nameservers) {
        try {
          // Use nslookup to query specific nameserver
          const { stdout } = await execFile("nslookup", [domain, ns]);

          // Parse the response to extract IP addresses
          const ipMatch = stdout.match(/Address:?\s+([0-9.]+)/g);
          results[ns] = ipMatch
            ? ipMatch.map((m) => m.replace("Address: ", "").trim())
            : ["No A record found"];
        } catch (error) {
          results[ns] = {
            error: "Query failed",
            message: error instanceof Error ? error.message : "Unknown error",
          };
        }
      }

      // Check if all nameservers return the same result
      const allResults = Object.values(results).flat();
      const uniqueResults = new Set(allResults.filter((r) => typeof r === "string"));
      const isPropagated = uniqueResults.size <= 1;

      return {
        success: true,
        message: isPropagated
          ? "DNS record has propagated globally"
          : "DNS record is propagating (may take up to 48 hours)",
        data: {
          domain,
          propagated: isPropagated,
          results,
          propagation_status: isPropagated ? "Complete" : "In progress",
          check_time: new Date().toISOString(),
        },
      };
    } catch (error) {
      return {
        success: false,
        message: "Failed to check DNS propagation",
        error: error instanceof Error ? error.message : String(error),
      };
    }
  }

  /**
   * cloudflare_get_account_info
   * Get Cloudflare account information
   */
  async getAccountInfo(): Promise<ToolResponse> {
    try {
      const account = await this.client.getAccount();

      return {
        success: true,
        message: "Account information retrieved successfully",
        data: {
          account_id: account.id,
          account_name: account.name,
        },
      };
    } catch (error) {
      return {
        success: false,
        message: "Failed to get account information",
        error: error instanceof Error ? error.message : String(error),
      };
    }
  }
}
