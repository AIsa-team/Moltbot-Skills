# OpenClaw Twitter 🐦

Twitter/X read APIs and **OAuth-based posting** for autonomous agents. Powered by AIsa.

## Installation

```bash
export AISA_API_KEY="your-key"
```

## Quick Start

```bash
# Read: user + search
python scripts/twitter_client.py user-info --username elonmusk
python scripts/twitter_client.py search --query "AI agents"
python scripts/twitter_client.py trends

# Post: OAuth relay
python scripts/twitter_client.py authorize --open-browser
python scripts/twitter_client.py post --text "Hello"
python scripts/twitter_client.py post --text "Long thread in reply mode" --type reply
python scripts/twitter_client.py post --text "Reply to this tweet" --in-reply-to-tweet-id "1888888888888888888"
```

## Features

- **Read**: User info, tweets, search, trends, followers, lists, communities, Spaces, etc.
- **Post**: Browser OAuth via `POST /twitter/auth_twitter` and `POST /twitter/post_twitter` with `Authorization: Bearer $AISA_API_KEY`. The client also keeps `aisa_api_key` in the JSON body for compatibility. `type=quote|reply` controls how long posts chain into a thread, and `in_reply_to_tweet_id` can attach the thread to a specific external tweet (no cookies, no proxy, no password).


## Get API Key

Sign up at [aisa.one](https://aisa.one)

## Links

- [ClawHub](https://www.clawhub.com/aisa-one/openclaw-twitter)
- [API Reference](https://docs.aisa.one/reference/)
