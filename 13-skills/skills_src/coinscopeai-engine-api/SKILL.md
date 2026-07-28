---
name: coinscopeai-engine-api
description: CoinScopeAI Engine API Reference. Use this skill to understand the endpoints, request/response formats, mock data fallback behavior, and supported symbols for the CoinScopeAI trading engine.
---

# CoinScopeAI Engine API Reference

This document provides the API reference for the CoinScopeAI trading engine.

## Base URL
The engine runs locally at: `http://localhost:8001`

## Authentication
No authentication is required for any of the endpoints.

## Supported Symbols
The engine currently supports the following symbols:
- BTCUSDT
- ETHUSDT
- SOLUSDT
- BNBUSDT
- XRPUSDT

## Endpoints

### 1. Scan Market Signals
- **Endpoint:** `GET /scan`
- **Description:** Scans the market for trading signals across supported symbols.
- **Example Request:** `GET http://localhost:8001/scan`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": [
      {
        "symbol": "BTCUSDT",
        "signal": "BUY",
        "confidence": 0.85,
        "timestamp": "2026-04-09T10:00:00Z"
      }
    ]
  }
  ```

### 2. Performance Metrics
- **Endpoint:** `GET /performance`
- **Description:** Retrieves the current performance metrics of the trading engine.
- **Example Request:** `GET http://localhost:8001/performance`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": {
      "total_trades": 150,
      "win_rate": 0.65,
      "profit_factor": 1.5,
      "current_drawdown": 0.02
    }
  }
  ```

### 3. Trade Journal
- **Endpoint:** `GET /journal`
- **Description:** Retrieves the historical trade journal.
- **Example Request:** `GET http://localhost:8001/journal`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": [
      {
        "trade_id": "12345",
        "symbol": "ETHUSDT",
        "side": "LONG",
        "entry_price": 3000.50,
        "exit_price": 3100.00,
        "pnl": 99.50,
        "timestamp": "2026-04-08T15:30:00Z"
      }
    ]
  }
  ```

### 4. Risk Gate Status
- **Endpoint:** `GET /risk-gate`
- **Description:** Checks the current status of the risk management gates.
- **Example Request:** `GET http://localhost:8001/risk-gate`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": {
      "daily_loss_limit_hit": false,
      "drawdown_limit_hit": false,
      "kill_switch_armed": false
    }
  }
  ```

### 5. Position Sizing
- **Endpoint:** `GET /position-size`
- **Description:** Calculates the recommended position size based on current risk parameters.
- **Example Request:** `GET http://localhost:8001/position-size?symbol=SOLUSDT`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": {
      "symbol": "SOLUSDT",
      "recommended_size_usdt": 500.00,
      "leverage": 5
    }
  }
  ```

### 6. Market Regime Detection
- **Endpoint:** `GET /regime/{symbol}`
- **Description:** Detects the current market regime for a specific symbol.
- **Example Request:** `GET http://localhost:8001/regime/BTCUSDT`
- **Example Response:**
  ```json
  {
    "status": "success",
    "data": {
      "symbol": "BTCUSDT",
      "regime": "trending",
      "confidence": 0.92
    }
  }
  ```

## Bundled Scripts

### Health Check
Run `bash scripts/health_check.sh` to check all 6 endpoints and get a status summary (UP / DOWN / MOCK). Accepts an optional base URL argument: `bash scripts/health_check.sh http://localhost:8001`

## Mock Data Fallback Behavior
When the engine is unreachable (e.g., before the VPS deployment is complete), the dashboard will automatically fall back to using mock data. This is indicated by an amber "MOCK DATA" badge on the UI. The mock data ensures the dashboard remains functional for demonstration and development purposes, simulating realistic responses for all endpoints.
