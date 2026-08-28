/**
 * Cloudflare API Type Definitions
 */

export interface CloudflareErrorResponse {
  success: false;
  errors: Array<{
    code: number;
    message: string;
  }>;
  messages: string[];
  result: null;
}

export interface CloudflareSuccessResponse<T> {
  success: true;
  errors: [];
  messages: [];
  result: T;
}

export type CloudflareResponse<T> =
  | CloudflareSuccessResponse<T>
  | CloudflareErrorResponse;

// DNS Record Types
export interface DNSRecord {
  id: string;
  type: string;
  name: string;
  content: string;
  ttl: number;
  proxied: boolean;
  proxiable?: boolean;
  comment?: string;
  tags?: string[];
  created_on?: string;
  modified_on?: string;
}

export interface CreateDNSRecordRequest {
  type: string;
  name: string;
  content: string;
  ttl?: number;
  priority?: number;
  proxied?: boolean;
  comment?: string;
  tags?: string[];
}

export interface UpdateDNSRecordRequest {
  type?: string;
  name?: string;
  content?: string;
  ttl?: number;
  proxied?: boolean;
  comment?: string;
  tags?: string[];
}

// Zone Types
export interface Zone {
  id: string;
  name: string;
  status: string;
  paused: boolean;
  type: string;
  nameservers: string[];
  original_nameservers: string[];
  created_on: string;
  modified_on: string;
  account?: {
    id: string;
    name: string;
  };
}

// Tool Parameters
export interface CreateRecordParams {
  zone_id: string;
  type: "A" | "AAAA" | "CNAME" | "MX" | "TXT" | "SRV" | "NS";
  name: string;
  content: string;
  ttl?: number;
  proxied?: boolean;
  comment?: string;
}

export interface UpdateRecordParams {
  zone_id: string;
  record_id: string;
  type?: string;
  name?: string;
  content?: string;
  ttl?: number;
  proxied?: boolean;
  comment?: string;
}

export interface ListRecordsParams {
  zone_id: string;
  type?: string;
  name?: string;
  page?: number;
  per_page?: number;
}

export interface DeleteRecordParams {
  zone_id: string;
  record_id: string;
}

export interface GetZoneParams {
  zone_id: string;
}

export interface CheckPropagationParams {
  domain: string;
  nameserver?: string;
}

// Tool Response Types
export interface ToolResponse {
  success: boolean;
  message: string;
  data?: any;
  error?: string;
}
