---
title: Markets
excerpt: Find markets on Polymarket using various filters including the ability to search.
api:
  file: polymarket-openapi.json
  operationId: get_polymarket-markets
hidden: false
---
Markets fetches prediction market data from Polymarket with optional filtering and search functionality. Supports filtering by market slug, condition ID, token ID, or tags, as well as fuzzy search across market titles and descriptions. Returns markets ordered by volume (most popular first) when filters are applied, or by start time (most recent first) when no filters are provided.

**Best for:** Discovering prediction markets, filtering by topic or status, searching for specific events, tracking market volume and outcomes.

**Endpoint:** `GET /polymarket/markets`

### Example

```bash
curl -X GET "https://api.aisa.one/apis/v1/polymarket/markets?search=bitcoin&status=open&limit=5" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

### Response

The response returns a `markets` array containing market objects with details such as title, status, volume, sides/outcomes, and timing information. A `pagination` object is also included with `has_more` and `pagination_key` fields for cursor-based pagination through large result sets.
