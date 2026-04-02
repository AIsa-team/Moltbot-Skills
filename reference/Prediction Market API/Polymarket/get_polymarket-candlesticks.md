---
title: Candlesticks
excerpt: Fetches historical candlestick data for a market identified by condition ID over a specified interval.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-candlesticks
hidden: false
---
Candlesticks fetches historical OHLC (open, high, low, close) candlestick data for a Polymarket market identified by its condition ID. Data is returned over a specified time range at configurable intervals (1-minute, 1-hour, or 1-day). Each candlestick includes price data, volume, open interest, and bid/ask spreads.

**Best for:** Building price charts, technical analysis, tracking market volatility, visualizing price movements over time.

**Endpoint:** `GET /polymarket/candlesticks/{condition_id}`

> **Note:** There are range limits per interval: 1-minute intervals support a maximum range of 1 week, 1-hour intervals support 1 month, and 1-day intervals support 1 year.

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/candlesticks/0x6876ac2b6174778c973c118aac287c49057c4d5360f896729209fe985a2c07fb?start_time=1640995200&end_time=1672531200&interval=1440" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns a `candlesticks` array where each element is a tuple of a candlestick data array and token metadata. Each candlestick data object contains OHLC prices (in both raw and dollar values), volume, open interest, and yes-side bid/ask spreads. The token metadata includes the token ID and outcome label (e.g., "Yes", "No").
