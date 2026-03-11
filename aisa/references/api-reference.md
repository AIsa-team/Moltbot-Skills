# OpenClaw Starter Kit - API Reference

**Powered by AIsa**

Complete API documentation based on [docs.aisa.one](https://docs.aisa.one/reference/).

## Base URL

```
https://api.aisa.one/apis/v1
```

## Authentication

All requests require a Bearer token:

```
Authorization: Bearer YOUR_AISA_API_KEY
```

---

## Twitter/X APIs

### Read Endpoints (GET)

| Endpoint | Description | Key Params |
|----------|-------------|------------|
| `/twitter/user/info` | Get user profile | `userName` |
| `/twitter/user_about` | Get user profile about | `userName` |
| `/twitter/user/batch_info_by_ids` | Batch get users by IDs | `userIds` |
| `/twitter/user/last_tweets` | Get user's recent tweets | `userName`, `cursor` |
| `/twitter/user/mentions` | Get user mentions | `userName`, `cursor` |
| `/twitter/user/followers` | Get user followers | `userName`, `cursor` |
| `/twitter/user/followings` | Get user followings | `userName`, `cursor` |
| `/twitter/user/verifiedFollowers` | Get verified followers | `user_id`, `cursor` |
| `/twitter/user/check_follow_relationship` | Check follow relationship | `source_user_name`, `target_user_name` |
| `/twitter/user/search` | Search users by keyword | `query`, `cursor` |
| `/twitter/tweet/advanced_search` | Advanced tweet search | `query`, `queryType` (Latest/Top), `cursor` |
| `/twitter/tweets` | Get tweets by IDs | `tweet_ids` (comma-separated) |
| `/twitter/tweet/replies` | Get tweet replies | `tweetId`, `cursor` |
| `/twitter/tweet/quotes` | Get tweet quotes | `tweetId`, `cursor` |
| `/twitter/tweet/retweeters` | Get tweet retweeters | `tweetId`, `cursor` |
| `/twitter/tweet/thread_context` | Get tweet thread context | `tweetId`, `cursor` |
| `/twitter/article` | Get article by tweet | `tweet_id` |
| `/twitter/trends` | Get trending topics | `woeid` (1=worldwide) |
| `/twitter/list/members` | Get list members | `list_id`, `cursor` |
| `/twitter/list/followers` | Get list followers | `list_id`, `cursor` |
| `/twitter/community/info` | Get community info | `community_id` |
| `/twitter/community/members` | Get community members | `community_id`, `cursor` |
| `/twitter/community/moderators` | Get community moderators | `community_id`, `cursor` |
| `/twitter/community/tweets` | Get community tweets | `community_id`, `cursor` |
| `/twitter/community/get_tweets_from_all_community` | Search all community tweets | `query`, `cursor` |
| `/twitter/spaces/detail` | Get Space detail | `space_id` |

### Write Endpoints (POST)

| Endpoint | Description | Key Params |
|----------|-------------|------------|
| `/twitter/user_login_v2` | Login to account | `user_name`, `email`, `password`, `proxy`, `totp_secret` |
| `/twitter/create_tweet_v2` | Create a tweet | `login_cookies`, `tweet_text`, `proxy`, `reply_to_tweet_id`?, `media_ids`? |
| `/twitter/upload_media_v2` | Upload media (multipart) | `file`, `login_cookies`, `proxy` |
| `/twitter/like_tweet_v2` | Like a tweet | `login_cookies`, `tweet_id`, `proxy` |
| `/twitter/unlike_tweet_v2` | Unlike a tweet | `login_cookies`, `tweet_id`, `proxy` |
| `/twitter/retweet_tweet_v2` | Retweet | `login_cookies`, `tweet_id`, `proxy` |
| `/twitter/delete_tweet_v2` | Delete a tweet | `login_cookies`, `tweet_id`, `proxy` |
| `/twitter/follow_user_v2` | Follow a user | `login_cookies`, `user_id`, `proxy` |
| `/twitter/unfollow_user_v2` | Unfollow a user | `login_cookies`, `user_id`, `proxy` |
| `/twitter/send_dm_to_user` | Send a direct message | `login_cookies`, `user_id`, `text`, `proxy` |

---

## Search APIs

### POST /scholar/search/web

Web search with structured results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search query |
| max_num_results | integer | No | Max results (1-100, default 10) |
| as_ylo | integer | No | Year lower bound |
| as_yhi | integer | No | Year upper bound |

### POST /scholar/search/scholar

Academic paper search.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search query |
| max_num_results | integer | No | Max results (1-100, default 10) |
| as_ylo | integer | No | Year lower bound |
| as_yhi | integer | No | Year upper bound |

### POST /scholar/search/smart

Intelligent search combining web and academic results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search query |
| max_num_results | integer | No | Max results |

---

## Tavily APIs

### POST /tavily/search

Tavily search integration.

### POST /tavily/extract

Extract content from URLs.

### POST /tavily/crawl

Crawl web pages.

---

## Financial APIs

### GET /financial/news/company

Company news by ticker.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ticker | string | Yes | Stock ticker (e.g., AAPL) |
| limit | integer | No | Number of articles |

### Other Financial Endpoints

- `/financial/stock/prices` - Historical stock prices
- `/financial/financial_statements/*` - Income, balance, cash flow
- `/financial/company/facts` - Company facts by CIK
- `/financial/search/stock` - Stock screener

---

## LLM APIs (OpenAI Compatible)

Base URL for LLM: `https://api.aisa.one/v1`

### POST /v1/chat/completions

OpenAI-compatible chat completions.

```json
{
  "model": "gpt-4",
  "messages": [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Hello!"}
  ],
  "max_tokens": 1000,
  "temperature": 0.7
}
```

**Supported Models:**

| Provider | Models |
|----------|--------|
| OpenAI | gpt-4, gpt-4-turbo, gpt-3.5-turbo |
| Anthropic | claude-3-opus, claude-3-sonnet, claude-3-haiku |
| Google | gemini-pro, gemini-ultra |
| Alibaba | qwen-* |
| Deepseek | deepseek-* |
| xAI | grok-* |

---

## Error Handling

```json
{
  "error": "error message",
  "code": 400,
  "details": "additional info"
}
```

---

## Full Documentation

For complete API documentation including all endpoints:
- [AIsa API Reference](https://docs.aisa.one/reference/)
- [Documentation Index](https://docs.aisa.one/llms.txt)
