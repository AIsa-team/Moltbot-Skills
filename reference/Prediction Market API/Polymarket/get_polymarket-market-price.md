---
title: Market Price
excerpt: Fetches the current or historical market price for a market by token ID.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-market-price
hidden: false
---
Market Price fetches the current or historical price for a Polymarket market identified by its token ID. When the `at_time` parameter is omitted, it returns the most real-time price available. When `at_time` is provided, it returns the historical market price at that specific timestamp.

**Best for:** Real-time price lookups, historical price snapshots, building price charts, tracking market sentiment over time.

**Endpoint:** `GET /polymarket/market-price/{token_id}`

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/market-price/19701256321759583954581192053894521654935987478209343000964756587964612528044?at_time=1762164600" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns a `price` field (a number between 0 and 1 representing the market probability) and an `at_time` field (Unix timestamp in seconds) indicating the point in time for which the price was fetched.
