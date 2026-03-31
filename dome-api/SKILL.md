---
name: dome-api
description: Interacts with the Dome API for prediction market data (Polymarket, Kalshi) and matching markets. Use when you need to fetch prediction market data, prices, or orderbook information using the AIsa proxy endpoint.
---

# Dome API Skill

This skill provides a Python client to interact with the Dome API, which offers comprehensive access to prediction market data across platforms like Polymarket and Kalshi.

**Important Note**: The API base URL has been configured to use the AIsa proxy endpoint: `https://api.aisa.one/apis/v1`.

## Capabilities

The Dome API provides access to:
1. **Polymarket Data**: Markets, Events, Trade History, Orderbooks, Activity, Market Prices, Candlesticks, Positions, Wallet Info, and PnL.
2. **Kalshi Data**: Markets, Trade History, Market Prices, and Orderbooks.
3. **Matching Markets**: Find equivalent markets across different prediction market platforms for sports events.
4. **Order Router**: Place orders on Polymarket with server-side execution.

## Bundled Resources

- `scripts/client.py`: A comprehensive Python client class (`DomeAPIClient`) that implements all major REST endpoints of the Dome API.

## Usage Instructions

To use the Dome API, import the `DomeAPIClient` from the bundled script.

```python
import sys
import os

# Add the scripts directory to the path so we can import the client
sys.path.append('/home/ubuntu/skills/dome-api/scripts')
from client import DomeAPIClient

# Initialize the client (API key is optional for some public endpoints)
client = DomeAPIClient(api_key="your_api_key_here")

# Example: Get Polymarket market price
market_price = client.get_polymarket_market_price("19701256321759583954581192053894521654935987478209343000964756587964612528044")
print(f"Price: {market_price.get('price')}")

# Example: Search for Kalshi markets
kalshi_markets = client.get_kalshi_markets(search="bitcoin", limit=5)
```

### Key Endpoints Available in the Client

#### Polymarket
- `get_polymarket_markets()`: Find markets with various filters.
- `get_polymarket_events()`: List events.
- `get_polymarket_orders()`: Fetch historical trade data.
- `get_polymarket_orderbooks()`: Fetch historical orderbook snapshots.
- `get_polymarket_activity()`: Fetch activity data.
- `get_polymarket_market_price()`: Get current or historical market price.
- `get_polymarket_candlesticks()`: Fetch historical candlestick data.
- `get_polymarket_positions()`: Fetch positions for a wallet.
- `get_polymarket_wallet()`: Fetch wallet info.
- `get_polymarket_wallet_pnl()`: Fetch realized PnL for a wallet.

#### Kalshi
- `get_kalshi_markets()`: Find markets.
- `get_kalshi_trades()`: Fetch historical trade data.
- `get_kalshi_market_price()`: Get current market price.
- `get_kalshi_orderbooks()`: Fetch historical orderbook snapshots.

#### Matching Markets
- `get_matching_sports()`: Find equivalent sports markets.
- `get_matching_sport_by_date()`: Find equivalent sports markets by date.

#### Order Router
- `place_order()`: Place an order on Polymarket via Dome infrastructure.

## Websockets

Dome API also provides real-time data streaming through WebSocket connections at `wss://ws.domeapi.io/<API_KEY>`.
You can subscribe to orders filtered by users, condition IDs, or market slugs.
