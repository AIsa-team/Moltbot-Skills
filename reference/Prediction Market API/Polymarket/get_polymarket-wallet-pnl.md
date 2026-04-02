---
title: Wallet Profit-and-Loss
excerpt: Fetches realized profit and loss (PnL) for a wallet address over a specified time range and granularity.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-wallet-pnl
hidden: false
---
Wallet Profit-and-Loss fetches the realized PnL for a specific Polymarket wallet address over a specified time range and granularity. This tracks realized gains only, from either confirmed sells or redeems. A gain or loss is not realized until a finished market is redeemed.

**Best for:** Tracking wallet profitability, analyzing trading performance over time, building PnL dashboards, comparing realized returns across periods.

**Endpoint:** `GET /polymarket/wallet/pnl/{wallet_address}`

> **Note:** This returns realized PnL only, which differs from Polymarket's dashboard that shows historical unrealized PnL.

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/wallet/pnl/0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b?granularity=day&start_time=1726857600&end_time=1758316829" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns the `granularity`, `start_time`, `end_time`, and `wallet_address` fields, along with a `pnl_over_time` array. Each element in the array contains a `timestamp` and `pnl_to_date` value representing the cumulative realized profit and loss at that point in time.
