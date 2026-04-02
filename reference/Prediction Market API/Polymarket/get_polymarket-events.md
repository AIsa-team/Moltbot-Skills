---
title: Events
excerpt: List events (groups of related markets) on Polymarket with filtering by category and status.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-events
hidden: false
---
Events fetches groups of related prediction markets from Polymarket. Events aggregate multiple markets under a single topic (e.g., "Presidential Election 2024" contains multiple candidate markets). Returns events ordered by total volume (most popular first), with optional filtering by event slug, tags, and status.

**Best for:** Browsing prediction market categories, finding related markets grouped by topic, tracking high-volume event clusters.

**Endpoint:** `GET /polymarket/events`

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/events?tags=politics&status=open&include_markets=true&limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns an `events` array containing event objects with fields such as title, status, volume, tags, and market count. When `include_markets=true` is set, each event includes a nested `markets` array with its associated markets. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination.
