---
title: Orderbook History
excerpt: Fetches historical orderbook snapshots for a specific asset (token ID) over a specified time range.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-orderbooks
hidden: false
---
Orderbook History fetches historical orderbook snapshots for a specific Polymarket asset (token ID) over a specified time range. If no start and end times are provided, it returns the latest orderbook snapshot for the market. Returns snapshots of the order book including bids, asks, and market metadata.

**Best for:** Analyzing market depth, tracking bid/ask spread over time, building orderbook visualizations, monitoring liquidity.

**Endpoint:** `GET /polymarket/orderbooks`

> **Note:** All timestamps are in milliseconds. Orderbook data has history starting from October 14th, 2025. When fetching the latest orderbook (without start/end times), the `limit` and `pagination_key` parameters are ignored.

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/orderbooks?token_id=56369772478534954338683665819559528414197495274302917800610633957542171787417&start_time=1760470000000&end_time=1760480000000&limit=100" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns a `snapshots` array containing orderbook snapshot objects, each with `bids` and `asks` arrays (containing size and price), along with metadata such as asset ID, timestamp, tick size, and market condition ID. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination.
