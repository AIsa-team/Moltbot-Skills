---
name: openclaw-starter-kit
description: "Replace 100+ API keys with one. Instant access to LLMs, Twitter, YouTube, LinkedIn, Finance, Tavily & Scholar data. Enterprise stability for your local agent."
homepage: https://openclaw.ai
metadata: {"openclaw":{"emoji":"🦞","requires":{"bins":["curl","python3"],"env":["AISA_API_KEY"]},"primaryEnv":"AISA_API_KEY"}}
---

# OpenClaw Starter Kit 🦞

**The definitive starting point for autonomous agents. Powered by AIsa.**

One API key. All the data sources your agent needs.

## 🔥 What Can You Do?

### Morning Briefing (Scheduled)
```
"Send me a daily briefing at 8am with:
- My portfolio performance (NVDA, TSLA, BTC)
- Twitter trends in AI
- Top news in my industry"
```

### Competitor Intelligence
```
"Monitor @OpenAI - alert me on new tweets, news mentions, and paper releases"
```

### Investment Research
```
"Full analysis on NVDA: price trends, insider trades, analyst estimates, 
SEC filings, and Twitter sentiment"
```

### Startup Validation
```
"Research the market for AI writing tools - find competitors, 
Twitter discussions, and academic papers on the topic"
```

### Crypto Whale Alerts
```
"Track large BTC movements and correlate with Twitter activity"
```

## AIsa vs bird

| Feature | AIsa ⚡ | bird 🐦 |
|---------|---------|---------|
| Auth method | API Key (simple) | Browser cookies (complex) |
| Read Twitter | ✅ | ✅ |
| Post/Like/Retweet | ✅ (via login) | ✅ |
| Web Search | ✅ | ❌ |
| Scholar Search | ✅ | ❌ |
| News/Financial | ✅ | ❌ |
| LLM Routing | ✅ | ❌ |
| Server-friendly | ✅ | ❌ |
| Cost | Pay-per-use | Free |

**Use AIsa when**: Server environment, need search/scholar APIs, prefer simple API key setup.
**Use bird when**: Local machine with browser, need free access, complex Twitter interactions.

## Quick Start

```bash
export AISA_API_KEY="your-key"
```

## Core Capabilities

### Twitter/X Data (Read)

```bash
# Get user info
curl "https://api.aisa.one/apis/v1/twitter/user/info?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Advanced tweet search
curl "https://api.aisa.one/apis/v1/twitter/tweet/advanced_search?query=AI+agents&queryType=Latest" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get trending topics (worldwide)
curl "https://api.aisa.one/apis/v1/twitter/trends?woeid=1" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

### Twitter/X Post (Write)

> **Warning**: Write operations require logging in first to get `login_cookies`. All write endpoints also require a `proxy` parameter. Use responsibly to avoid rate limits or account suspension.

```bash
# Step 1: Login (returns login_cookies for subsequent calls)
curl -X POST "https://api.aisa.one/apis/v1/twitter/user_login_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "user_name": "myaccount",
    "email": "me@example.com",
    "password": "xxx",
    "proxy": "http://user:pass@ip:port",
    "totp_secret": "optional-2fa-secret"
  }'

# Step 2: Use login_cookies from login response for all write operations

# Create a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/create_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies-from-login>", "tweet_text": "Hello from OpenClaw!", "proxy": "http://user:pass@ip:port"}'

# Like a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/like_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "tweet_id": "1234567890", "proxy": "http://user:pass@ip:port"}'
```

### Search (Web + Academic)

```bash
# Web search
curl -X POST "https://api.aisa.one/apis/v1/scholar/search/web?query=AI+frameworks&max_num_results=10" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Academic/scholar search
curl -X POST "https://api.aisa.one/apis/v1/scholar/search/scholar?query=transformer+models&max_num_results=10" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Smart search (web + academic combined)
curl -X POST "https://api.aisa.one/apis/v1/scholar/search/smart?query=machine+learning&max_num_results=10" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

### Financial News

```bash
# Company news by ticker
curl "https://api.aisa.one/apis/v1/financial/news?ticker=AAPL&limit=10" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

### LLM Routing (OpenAI Compatible)

```bash
curl -X POST "https://api.aisa.one/v1/chat/completions" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "Hello"}]}'
```

Supported models: GPT-4, Claude-3, Gemini, Qwen, Deepseek, Grok, and more.

## Python Client

```bash
# Twitter Read
python3 {baseDir}/scripts/aisa_client.py twitter user-info --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter user-about --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter tweets --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter mentions --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter followers --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter followings --username elonmusk
python3 {baseDir}/scripts/aisa_client.py twitter search --query "AI agents"
python3 {baseDir}/scripts/aisa_client.py twitter user-search --query "AI researcher"
python3 {baseDir}/scripts/aisa_client.py twitter trends --woeid 1
python3 {baseDir}/scripts/aisa_client.py twitter detail --tweet-ids 1895096451033985024
python3 {baseDir}/scripts/aisa_client.py twitter replies --tweet-id 1895096451033985024
python3 {baseDir}/scripts/aisa_client.py twitter community-info --community-id 1708485837274263614

# Twitter Write (requires login first, returns login_cookies)
python3 {baseDir}/scripts/aisa_client.py twitter login --username myaccount --email me@example.com --password xxx --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/aisa_client.py twitter post --cookies "<login_cookies>" --text "Hello!" --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/aisa_client.py twitter like --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/aisa_client.py twitter retweet --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"

# Search
python3 {baseDir}/scripts/aisa_client.py search web --query "latest AI news"
python3 {baseDir}/scripts/aisa_client.py search scholar --query "LLM research"
python3 {baseDir}/scripts/aisa_client.py search smart --query "machine learning"

# News
python3 {baseDir}/scripts/aisa_client.py news --ticker AAPL

# LLM
python3 {baseDir}/scripts/aisa_client.py llm complete --model gpt-4 --prompt "Explain quantum computing"
```

## Pricing

| API | Cost |
|-----|------|
| Twitter query | ~$0.0004 |
| Twitter post/like | ~$0.001 |
| Web search | ~$0.001 |
| Scholar search | ~$0.002 |
| News | ~$0.001 |
| LLM | Token-based |

Every response includes `usage.cost` and `usage.credits_remaining`.

## Error Handling

Errors return JSON with `error` field:

```json
{
  "error": "Invalid API key",
  "code": 401
}
```

Common error codes:
- `401` - Invalid or missing API key
- `402` - Insufficient credits
- `429` - Rate limit exceeded
- `500` - Server error

## Get Started

1. Sign up at [aisa.one](https://aisa.one)
2. Get your API key
3. Add credits (pay-as-you-go)
4. Set environment variable: `export AISA_API_KEY="your-key"`

## Full API Reference

See [API Reference](https://github.com/AIsa-team/Openclaw-Starter-Kit/blob/main/skills/aisa/references/api-reference.md) for complete endpoint documentation.
