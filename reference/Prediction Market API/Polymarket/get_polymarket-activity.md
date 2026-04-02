---
title: Activity
excerpt: Fetches trading activity data including merges, splits, and redeems with optional filtering by user, market, and time range.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-activity
hidden: false
---
Activity fetches on-chain trading activity from Polymarket with optional filtering by user wallet, market, condition, and time range. Returns activity records including MERGES, SPLITS, and REDEEMS, which represent the different types of position management operations on the platform.

**Best for:** Tracking wallet activity, monitoring position changes, analyzing redemption patterns, auditing on-chain trading operations.

**Endpoint:** `GET /polymarket/activity`

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/activity?user=0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b&limit=50" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns an `activities` array containing activity objects with fields such as side (MERGE/SPLIT/REDEEM), shares, price, transaction hash, timestamp, and user wallet address. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination through large result sets.
