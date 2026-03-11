---
name: Twitter Command Center (Search + Post)
description: "Search X (Twitter) in real time, extract relevant posts, and publish tweets/replies instantly—perfect for social listening, engagement, and rapid content ops."
homepage: https://openclaw.ai
metadata: {"openclaw":{"emoji":"🐦","requires":{"bins":["curl","python3"],"env":["AISA_API_KEY"]},"primaryEnv":"AISA_API_KEY"}}
---

# OpenClaw Twitter 🐦

**Twitter/X data access and automation for autonomous agents. Powered by AIsa.**

One API key. Full Twitter intelligence.

## 🔥 What Can You Do?

### Monitor Influencers
```
"Get Elon Musk's latest tweets and notify me of any AI-related posts"
```

### Track Trends
```
"What's trending on Twitter worldwide right now?"
```

### Social Listening
```
"Search for tweets mentioning our product and analyze sentiment"
```

### Automated Engagement
```
"Like and retweet posts from @OpenAI that mention GPT-5"
```

### Competitor Intel
```
"Monitor @anthropic and @GoogleAI - alert me on new announcements"
```

## Quick Start

```bash
export AISA_API_KEY="your-key"
```

## Core Capabilities

### Read Operations (No Login Required)

#### User Endpoints

```bash
# Get user info
curl "https://api.aisa.one/apis/v1/twitter/user/info?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user profile about (account country, verification, username changes)
curl "https://api.aisa.one/apis/v1/twitter/user_about?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Batch get user info by IDs
curl "https://api.aisa.one/apis/v1/twitter/user/batch_info_by_ids?userIds=44196397,123456" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user's latest tweets
curl "https://api.aisa.one/apis/v1/twitter/user/last_tweets?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user mentions
curl "https://api.aisa.one/apis/v1/twitter/user/mentions?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user followers
curl "https://api.aisa.one/apis/v1/twitter/user/followers?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user followings
curl "https://api.aisa.one/apis/v1/twitter/user/followings?userName=elonmusk" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get user verified followers (requires user_id, not userName)
curl "https://api.aisa.one/apis/v1/twitter/user/verifiedFollowers?user_id=44196397" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Check follow relationship between two users
curl "https://api.aisa.one/apis/v1/twitter/user/check_follow_relationship?source_user_name=elonmusk&target_user_name=BillGates" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Search users by keyword
curl "https://api.aisa.one/apis/v1/twitter/user/search?query=AI+researcher" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

#### Tweet Endpoints

```bash
# Advanced tweet search (queryType is required: Latest or Top)
curl "https://api.aisa.one/apis/v1/twitter/tweet/advanced_search?query=AI+agents&queryType=Latest" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Search top tweets
curl "https://api.aisa.one/apis/v1/twitter/tweet/advanced_search?query=AI+agents&queryType=Top" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get tweets by IDs (comma-separated)
curl "https://api.aisa.one/apis/v1/twitter/tweets?tweet_ids=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get tweet replies
curl "https://api.aisa.one/apis/v1/twitter/tweet/replies?tweetId=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get tweet quotes
curl "https://api.aisa.one/apis/v1/twitter/tweet/quotes?tweetId=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get tweet retweeters
curl "https://api.aisa.one/apis/v1/twitter/tweet/retweeters?tweetId=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get tweet thread context (full conversation thread)
curl "https://api.aisa.one/apis/v1/twitter/tweet/thread_context?tweetId=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get article by tweet ID
curl "https://api.aisa.one/apis/v1/twitter/article?tweet_id=1895096451033985024" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

#### Trends, Lists, Communities & Spaces

```bash
# Get trending topics (worldwide)
curl "https://api.aisa.one/apis/v1/twitter/trends?woeid=1" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get list members
curl "https://api.aisa.one/apis/v1/twitter/list/members?list_id=1585430245762441216" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get list followers
curl "https://api.aisa.one/apis/v1/twitter/list/followers?list_id=1585430245762441216" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get community info
curl "https://api.aisa.one/apis/v1/twitter/community/info?community_id=1708485837274263614" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get community members
curl "https://api.aisa.one/apis/v1/twitter/community/members?community_id=1708485837274263614" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get community moderators
curl "https://api.aisa.one/apis/v1/twitter/community/moderators?community_id=1708485837274263614" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get community tweets
curl "https://api.aisa.one/apis/v1/twitter/community/tweets?community_id=1708485837274263614" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Search tweets from all communities
curl "https://api.aisa.one/apis/v1/twitter/community/get_tweets_from_all_community?query=AI" \
  -H "Authorization: Bearer $AISA_API_KEY"

# Get Space detail
curl "https://api.aisa.one/apis/v1/twitter/spaces/detail?space_id=1dRJZlbLkjexB" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

### Write Operations (Requires Login)

> ⚠️ **Warning**: Write operations require logging in first to get `login_cookies`. All write endpoints also require a `proxy` parameter. Use responsibly to avoid rate limits or account suspension.

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
  -d '{
    "login_cookies": "<cookies-from-login>",
    "tweet_text": "Hello from OpenClaw!",
    "proxy": "http://user:pass@ip:port"
  }'

# Reply to a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/create_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "login_cookies": "<cookies-from-login>",
    "tweet_text": "Great point!",
    "reply_to_tweet_id": "1234567890",
    "proxy": "http://user:pass@ip:port"
  }'

# Upload media (multipart/form-data)
curl -X POST "https://api.aisa.one/apis/v1/twitter/upload_media_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -F "file=@image.jpg" \
  -F "login_cookies=<cookies-from-login>" \
  -F "proxy=http://user:pass@ip:port"

# Like a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/like_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "tweet_id": "1234567890", "proxy": "http://user:pass@ip:port"}'

# Unlike a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/unlike_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "tweet_id": "1234567890", "proxy": "http://user:pass@ip:port"}'

# Retweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/retweet_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "tweet_id": "1234567890", "proxy": "http://user:pass@ip:port"}'

# Delete a tweet
curl -X POST "https://api.aisa.one/apis/v1/twitter/delete_tweet_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "tweet_id": "1234567890", "proxy": "http://user:pass@ip:port"}'

# Follow a user
curl -X POST "https://api.aisa.one/apis/v1/twitter/follow_user_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "user_id": "44196397", "proxy": "http://user:pass@ip:port"}'

# Unfollow a user
curl -X POST "https://api.aisa.one/apis/v1/twitter/unfollow_user_v2" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "user_id": "44196397", "proxy": "http://user:pass@ip:port"}'

# Send a direct message
curl -X POST "https://api.aisa.one/apis/v1/twitter/send_dm_to_user" \
  -H "Authorization: Bearer $AISA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"login_cookies": "<cookies>", "user_id": "44196397", "text": "Hello!", "proxy": "http://user:pass@ip:port"}'
```

## Python Client

```bash
# User operations
python3 {baseDir}/scripts/twitter_client.py user-info --username elonmusk
python3 {baseDir}/scripts/twitter_client.py user-about --username elonmusk
python3 {baseDir}/scripts/twitter_client.py tweets --username elonmusk
python3 {baseDir}/scripts/twitter_client.py mentions --username elonmusk
python3 {baseDir}/scripts/twitter_client.py followers --username elonmusk
python3 {baseDir}/scripts/twitter_client.py followings --username elonmusk
python3 {baseDir}/scripts/twitter_client.py verified-followers --user-id 44196397
python3 {baseDir}/scripts/twitter_client.py check-follow --source elonmusk --target BillGates

# Search & Discovery
python3 {baseDir}/scripts/twitter_client.py search --query "AI agents"
python3 {baseDir}/scripts/twitter_client.py search --query "AI agents" --type Top
python3 {baseDir}/scripts/twitter_client.py user-search --query "AI researcher"
python3 {baseDir}/scripts/twitter_client.py trends --woeid 1

# Tweet operations
python3 {baseDir}/scripts/twitter_client.py detail --tweet-ids 1895096451033985024
python3 {baseDir}/scripts/twitter_client.py replies --tweet-id 1895096451033985024
python3 {baseDir}/scripts/twitter_client.py quotes --tweet-id 1895096451033985024
python3 {baseDir}/scripts/twitter_client.py retweeters --tweet-id 1895096451033985024
python3 {baseDir}/scripts/twitter_client.py thread --tweet-id 1895096451033985024

# List operations
python3 {baseDir}/scripts/twitter_client.py list-members --list-id 1585430245762441216
python3 {baseDir}/scripts/twitter_client.py list-followers --list-id 1585430245762441216

# Community operations
python3 {baseDir}/scripts/twitter_client.py community-info --community-id 1708485837274263614
python3 {baseDir}/scripts/twitter_client.py community-members --community-id 1708485837274263614
python3 {baseDir}/scripts/twitter_client.py community-tweets --community-id 1708485837274263614
python3 {baseDir}/scripts/twitter_client.py community-search --query "AI"

# Write operations (requires login first)
python3 {baseDir}/scripts/twitter_client.py login --username myaccount --email me@example.com --password xxx --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py post --cookies "<login_cookies>" --text "Hello!" --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py like --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py unlike --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py retweet --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py delete-tweet --cookies "<login_cookies>" --tweet-id 1234567890 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py follow --cookies "<login_cookies>" --user-id 44196397 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py unfollow --cookies "<login_cookies>" --user-id 44196397 --proxy "http://user:pass@ip:port"
python3 {baseDir}/scripts/twitter_client.py send-dm --cookies "<login_cookies>" --user-id 44196397 --text "Hello!" --proxy "http://user:pass@ip:port"
```

## API Endpoints Reference

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

## Pricing

| API | Cost |
|-----|------|
| Twitter read query | ~$0.0004 |
| Twitter post/like/retweet | ~$0.001 |

Every response includes `usage.cost` and `usage.credits_remaining`.

## Get Started

1. Sign up at [aisa.one](https://aisa.one)
2. Get your API key
3. Add credits (pay-as-you-go)
4. Set environment variable: `export AISA_API_KEY="your-key"`

## Full API Reference

See [API Reference](https://aisa.mintlify.app/api-reference/introduction) for complete endpoint documentation.
