---
title: Trade History
excerpt: Fetches historical trade data with optional filtering by market, condition, token, time range, and user wallet address.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-orders
hidden: false
---
Trade History fetches order data from Polymarket with optional filtering by market, condition, token, time range, and user wallet address. Returns orders that match either primary or secondary token IDs for markets. If no filters are provided, it returns the latest trades happening in real time.

**Best for:** Analyzing trading activity, tracking specific wallet addresses, monitoring real-time trades, building trade history for a market.

**Endpoint:** `GET /polymarket/orders`

> **Note:** Only one of `market_slug`, `token_id`, or `condition_id` can be provided per request.

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/orders?market_slug=bitcoin-up-or-down-july-25-8pm-et&limit=50" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns an `orders` array containing trade objects with fields such as token ID, side (BUY/SELL), shares, price, transaction hash, timestamp, and user/taker wallet addresses. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination through large result sets.
