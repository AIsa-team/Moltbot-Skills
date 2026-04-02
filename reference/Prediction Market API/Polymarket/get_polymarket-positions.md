---
title: Positions
excerpt: Fetches all Polymarket positions for a proxy wallet address with market info and redemption status.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-positions
hidden: false
---
Positions fetches all active Polymarket positions held by a specific proxy wallet address. Returns positions with a balance of at least 10,000 shares (0.01 normalized), along with detailed market information including title, status, outcome labels, and redemption eligibility.

**Best for:** Portfolio tracking, monitoring wallet holdings, identifying redeemable positions, analyzing wallet exposure across markets.

**Endpoint:** `GET /polymarket/positions/wallet/{wallet_address}`

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/positions/wallet/0x1234567890abcdef1234567890abcdef12345678?limit=100" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns a `wallet_address` field, a `positions` array containing position objects with fields such as token ID, condition ID, title, shares (raw and normalized), redeemable status, market/event slugs, outcome label, winning outcome, and market status. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination.
