/**
 * Cloudflare MCP Server Constants
 * Configuration for Cloudflare API integration
 */

export const CLOUDFLARE_API_BASE_URL = "https://api.cloudflare.com/client/v4";

export const DEFAULT_TIMEOUT_MS = 30000;

export const DNS_RECORD_TYPES = {
  A: "A",
  AAAA: "AAAA",
  CNAME: "CNAME",
  MX: "MX",
  TXT: "TXT",
  NS: "NS",
  SOA: "SOA",
  SRV: "SRV",
} as const;

export const PROXY_STATUS = {
  PROXIED: "proxied",
  DNS_ONLY: "dns_only",
} as const;

export const TTL_OPTIONS = {
  AUTO: 1,
  ONE_HOUR: 3600,
  SIX_HOURS: 21600,
  ONE_DAY: 86400,
  ONE_WEEK: 604800,
  ONE_MONTH: 2592000,
} as const;

// CoinScopeAI Domain Configuration
export const COINSCOPE_DOMAINS = {
  ZONE: "coinscope.ai",
  API: "api.coinscope.ai",
  APP: "app.coinscope.ai",
  DASHBOARD: "dashboard.coinscope.ai",
  DEFAULT_IP: "16.171.152.142",
} as const;

// Environment variable keys
export const ENV_KEYS = {
  API_TOKEN: "CLOUDFLARE_API_TOKEN",
  ACCOUNT_ID: "CLOUDFLARE_ACCOUNT_ID",
  ZONE_ID: "CLOUDFLARE_ZONE_ID",
} as const;
