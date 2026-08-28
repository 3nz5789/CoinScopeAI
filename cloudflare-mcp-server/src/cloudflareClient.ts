/**
 * Cloudflare API Client
 * Wrapper around Cloudflare REST API v4
 */

import axios, { AxiosInstance } from "axios";
import { CLOUDFLARE_API_BASE_URL, DEFAULT_TIMEOUT_MS } from "./constants.js";
import {
  CloudflareResponse,
  DNSRecord,
  CreateDNSRecordRequest,
  UpdateDNSRecordRequest,
  Zone,
} from "./types.js";

export class CloudflareClient {
  private client: AxiosInstance;
  private apiToken: string;
  private accountId: string;

  constructor(apiToken: string, accountId: string) {
    this.apiToken = apiToken;
    this.accountId = accountId;

    this.client = axios.create({
      baseURL: CLOUDFLARE_API_BASE_URL,
      timeout: DEFAULT_TIMEOUT_MS,
      headers: {
        "Authorization": `Bearer ${apiToken}`,
        "Content-Type": "application/json",
      },
    });
  }

  /**
   * Get zone information
   */
  async getZone(zoneId: string): Promise<Zone> {
    try {
      const response = await this.client.get<CloudflareResponse<Zone>>(
        `/zones/${zoneId}`
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to get zone: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      return response.data.result;
    } catch (error) {
      throw this.handleError(error, `Failed to get zone ${zoneId}`);
    }
  }

  /**
   * List DNS records in a zone
   */
  async listDNSRecords(
    zoneId: string,
    options?: { type?: string; name?: string; page?: number; per_page?: number }
  ): Promise<{ records: DNSRecord[]; total_count: number }> {
    try {
      const params = new URLSearchParams();
      if (options?.type) params.append("type", options.type);
      if (options?.name) params.append("name", options.name);
      if (options?.page) params.append("page", options.page.toString());
      if (options?.per_page)
        params.append("per_page", options.per_page.toString());

      const response = await this.client.get<CloudflareResponse<DNSRecord[]>>(
        `/zones/${zoneId}/dns_records`,
        { params: Object.fromEntries(params) }
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to list DNS records: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      return {
        records: response.data.result,
        total_count: response.data.result.length,
      };
    } catch (error) {
      throw this.handleError(error, "Failed to list DNS records");
    }
  }

  /**
   * Get a specific DNS record
   */
  async getDNSRecord(zoneId: string, recordId: string): Promise<DNSRecord> {
    try {
      const response = await this.client.get<CloudflareResponse<DNSRecord>>(
        `/zones/${zoneId}/dns_records/${recordId}`
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to get DNS record: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      return response.data.result;
    } catch (error) {
      throw this.handleError(error, `Failed to get DNS record ${recordId}`);
    }
  }

  /**
   * Create a new DNS record
   */
  async createDNSRecord(
    zoneId: string,
    record: CreateDNSRecordRequest
  ): Promise<DNSRecord> {
    try {
      const response = await this.client.post<CloudflareResponse<DNSRecord>>(
        `/zones/${zoneId}/dns_records`,
        record
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to create DNS record: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      return response.data.result;
    } catch (error) {
      throw this.handleError(error, "Failed to create DNS record");
    }
  }

  /**
   * Update a DNS record
   */
  async updateDNSRecord(
    zoneId: string,
    recordId: string,
    record: UpdateDNSRecordRequest
  ): Promise<DNSRecord> {
    try {
      const response = await this.client.patch<CloudflareResponse<DNSRecord>>(
        `/zones/${zoneId}/dns_records/${recordId}`,
        record
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to update DNS record: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      return response.data.result;
    } catch (error) {
      throw this.handleError(error, `Failed to update DNS record ${recordId}`);
    }
  }

  /**
   * Delete a DNS record
   */
  async deleteDNSRecord(zoneId: string, recordId: string): Promise<void> {
    try {
      const response = await this.client.delete<CloudflareResponse<null>>(
        `/zones/${zoneId}/dns_records/${recordId}`
      );

      if (!response.data.success) {
        throw new Error(
          `Failed to delete DNS record: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }
    } catch (error) {
      throw this.handleError(error, `Failed to delete DNS record ${recordId}`);
    }
  }

  /**
   * Get account information
   */
  async getAccount(): Promise<{ id: string; name: string }> {
    try {
      const response = await this.client.get<
        CloudflareResponse<{ id: string; name: string }[]>
      >(`/accounts`);

      if (!response.data.success) {
        throw new Error(
          `Failed to get accounts: ${response.data.errors[0]?.message || "Unknown error"}`
        );
      }

      const account = response.data.result.find((acc) => acc.id === this.accountId);
      if (!account) {
        throw new Error(`Account ${this.accountId} not found`);
      }

      return account;
    } catch (error) {
      throw this.handleError(error, "Failed to get account information");
    }
  }

  /**
   * Error handling utility
   */
  private handleError(error: any, context: string): Error {
    if (axios.isAxiosError(error)) {
      const message = error.response?.data?.errors?.[0]?.message || error.message;
      return new Error(`${context}: ${message}`);
    }
    return error instanceof Error ? error : new Error(`${context}: Unknown error`);
  }
}
