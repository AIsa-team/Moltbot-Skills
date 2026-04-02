---
title: Wallet
excerpt: Fetches wallet information by EOA address, proxy address, or user handle, with optional trading metrics.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-wallet
hidden: false
---
Wallet fetches Polymarket wallet information by providing either an EOA (Externally Owned Account) address, a proxy wallet address, or a user handle. Returns the associated EOA, proxy, wallet type, handle, pseudonym, and profile image. Optionally includes trading metrics such as total volume, number of trades, and unique markets traded when `with_metrics=true`.

**Best for:** Looking up wallet identities, resolving handles to addresses, retrieving user profiles, analyzing wallet trading performance.

**Endpoint:** `GET /polymarket/wallet`

> **Note:** Exactly one of `eoa`, `proxy`, or `handle` must be provided per request.

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/wallet?handle=satoshi&with_metrics=true" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns wallet identity fields including `eoa`, `proxy`, `wallet_type`, `handle`, `pseudonym`, and `image`. When `with_metrics=true` is set, a `wallet_metrics` object is also included with total volume, total trades, total markets, highest volume day, and counts for merges, splits, conversions, and redemptions.
