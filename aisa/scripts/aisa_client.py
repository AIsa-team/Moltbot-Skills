#!/usr/bin/env python3
"""
OpenClaw Starter Kit - AIsa API Client
Powered by AIsa (https://aisa.one)

Unified API access for autonomous agents.

Usage:
    python aisa_client.py twitter user-info --username <username>
    python aisa_client.py twitter tweets --username <username> [--count <n>]
    python aisa_client.py twitter search --query <query> [--count <n>]
    python aisa_client.py twitter detail --tweet-id <id>
    python aisa_client.py twitter trends
    python aisa_client.py search web --query <query> [--count <n>]
    python aisa_client.py search scholar --query <query> [--count <n>]
    python aisa_client.py news --query <query> [--count <n>]
    python aisa_client.py llm complete --model <model> --prompt <prompt>
    python aisa_client.py llm chat --model <model> --messages <json>
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from typing import Any, Dict, Optional


class AIsaClient:
    """OpenClaw Starter Kit - AIsa API Client for unified access to AI-native data sources."""
    
    BASE_URL = "https://api.aisa.one/apis/v1"
    LLM_BASE_URL = "https://api.aisa.one/v1"
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the client with an API key."""
        self.api_key = api_key or os.environ.get("AISA_API_KEY")
        if not self.api_key:
            raise ValueError(
                "AISA_API_KEY is required. Set it via environment variable or pass to constructor."
            )
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make an HTTP request to the AIsa API."""
        url = f"{self.BASE_URL}{endpoint}"
        
        if params:
            query_string = urllib.parse.urlencode(
                {k: v for k, v in params.items() if v is not None}
            )
            url = f"{url}?{query_string}"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "OpenClaw-Starter-Kit/1.0"
        }
        
        request_data = None
        if data:
            request_data = json.dumps(data).encode("utf-8")
        
        # For POST requests without body, send empty JSON
        if method == "POST" and request_data is None:
            request_data = b"{}"
        
        req = urllib.request.Request(url, data=request_data, headers=headers, method=method)
        
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                return {"success": False, "error": {"code": str(e.code), "message": error_body}}
        except urllib.error.URLError as e:
            return {"success": False, "error": {"code": "NETWORK_ERROR", "message": str(e.reason)}}
    
    # ==================== Twitter Read APIs ====================

    def twitter_user_info(self, username: str) -> Dict[str, Any]:
        """Get Twitter user information by username."""
        return self._request("GET", "/twitter/user/info", params={"userName": username})

    def twitter_user_about(self, username: str) -> Dict[str, Any]:
        """Get user profile about (account country, verification, username changes)."""
        return self._request("GET", "/twitter/user_about", params={"userName": username})

    def twitter_batch_user_info(self, user_ids: str) -> Dict[str, Any]:
        """Batch get user info by comma-separated user IDs."""
        return self._request("GET", "/twitter/user/batch_info_by_ids", params={"userIds": user_ids})

    def twitter_user_tweets(self, username: str, cursor: str = None) -> Dict[str, Any]:
        """Get latest tweets from a specific user."""
        return self._request("GET", "/twitter/user/last_tweets", params={"userName": username, "cursor": cursor})

    def twitter_user_mentions(self, username: str, cursor: str = None) -> Dict[str, Any]:
        """Get mentions of a user."""
        return self._request("GET", "/twitter/user/mentions", params={"userName": username, "cursor": cursor})

    def twitter_followers(self, username: str, cursor: str = None) -> Dict[str, Any]:
        """Get user followers."""
        return self._request("GET", "/twitter/user/followers", params={"userName": username, "cursor": cursor})

    def twitter_followings(self, username: str, cursor: str = None) -> Dict[str, Any]:
        """Get user followings."""
        return self._request("GET", "/twitter/user/followings", params={"userName": username, "cursor": cursor})

    def twitter_verified_followers(self, user_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get verified followers of a user (requires user_id, not username)."""
        return self._request("GET", "/twitter/user/verifiedFollowers", params={"user_id": user_id, "cursor": cursor})

    def twitter_check_follow(self, source: str, target: str) -> Dict[str, Any]:
        """Check follow relationship between two users."""
        return self._request("GET", "/twitter/user/check_follow_relationship", params={
            "source_user_name": source, "target_user_name": target
        })

    def twitter_user_search(self, keyword: str, cursor: str = None) -> Dict[str, Any]:
        """Search for Twitter users by keyword."""
        return self._request("GET", "/twitter/user/search", params={"query": keyword, "cursor": cursor})

    def twitter_search(self, query: str, query_type: str = "Latest", cursor: str = None) -> Dict[str, Any]:
        """Search for tweets (Advanced Search)."""
        return self._request("GET", "/twitter/tweet/advanced_search", params={
            "query": query, "queryType": query_type, "cursor": cursor
        })

    def twitter_tweet_detail(self, tweet_ids: str) -> Dict[str, Any]:
        """Get detailed information about tweets by IDs (comma-separated)."""
        return self._request("GET", "/twitter/tweets", params={"tweet_ids": tweet_ids})

    def twitter_tweet_replies(self, tweet_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get replies to a tweet."""
        return self._request("GET", "/twitter/tweet/replies", params={"tweetId": tweet_id, "cursor": cursor})

    def twitter_tweet_quotes(self, tweet_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get quotes of a tweet."""
        return self._request("GET", "/twitter/tweet/quotes", params={"tweetId": tweet_id, "cursor": cursor})

    def twitter_tweet_retweeters(self, tweet_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get retweeters of a tweet."""
        return self._request("GET", "/twitter/tweet/retweeters", params={"tweetId": tweet_id, "cursor": cursor})

    def twitter_tweet_thread(self, tweet_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get the full thread context of a tweet."""
        return self._request("GET", "/twitter/tweet/thread_context", params={"tweetId": tweet_id, "cursor": cursor})

    def twitter_article(self, tweet_id: str) -> Dict[str, Any]:
        """Get article content by tweet ID."""
        return self._request("GET", "/twitter/article", params={"tweet_id": tweet_id})

    def twitter_trends(self, woeid: int = 1) -> Dict[str, Any]:
        """Get current Twitter trending topics by WOEID (1 = worldwide)."""
        return self._request("GET", "/twitter/trends", params={"woeid": woeid})

    def twitter_list_members(self, list_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get members of a Twitter list."""
        return self._request("GET", "/twitter/list/members", params={"list_id": list_id, "cursor": cursor})

    def twitter_list_followers(self, list_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get followers of a Twitter list."""
        return self._request("GET", "/twitter/list/followers", params={"list_id": list_id, "cursor": cursor})

    def twitter_community_info(self, community_id: str) -> Dict[str, Any]:
        """Get community info by ID."""
        return self._request("GET", "/twitter/community/info", params={"community_id": community_id})

    def twitter_community_members(self, community_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get community members."""
        return self._request("GET", "/twitter/community/members", params={"community_id": community_id, "cursor": cursor})

    def twitter_community_moderators(self, community_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get community moderators."""
        return self._request("GET", "/twitter/community/moderators", params={"community_id": community_id, "cursor": cursor})

    def twitter_community_tweets(self, community_id: str, cursor: str = None) -> Dict[str, Any]:
        """Get community tweets."""
        return self._request("GET", "/twitter/community/tweets", params={"community_id": community_id, "cursor": cursor})

    def twitter_community_search(self, query: str, cursor: str = None) -> Dict[str, Any]:
        """Search tweets from all communities."""
        return self._request("GET", "/twitter/community/get_tweets_from_all_community", params={"query": query, "cursor": cursor})

    def twitter_space_detail(self, space_id: str) -> Dict[str, Any]:
        """Get Space detail by ID."""
        return self._request("GET", "/twitter/spaces/detail", params={"space_id": space_id})

    # ==================== Twitter Write APIs (V2 - requires login_cookies) ====================

    def twitter_login(self, username: str, email: str, password: str, proxy: str, totp_secret: str = None) -> Dict[str, Any]:
        """Login to Twitter account. Returns login_cookies for write operations.

        WARNING: Credentials are sent to the AIsa API server for authentication.
        """
        data = {
            "user_name": username,
            "email": email,
            "password": password,
            "proxy": proxy
        }
        if totp_secret:
            data["totp_secret"] = totp_secret
        return self._request("POST", "/twitter/user_login_v2", data=data)

    def twitter_create_tweet(self, login_cookies: str, text: str, proxy: str,
                             reply_to_tweet_id: str = None) -> Dict[str, Any]:
        """Create a tweet (requires login_cookies from twitter_login)."""
        data = {
            "login_cookies": login_cookies,
            "tweet_text": text,
            "proxy": proxy
        }
        if reply_to_tweet_id:
            data["reply_to_tweet_id"] = reply_to_tweet_id
        return self._request("POST", "/twitter/create_tweet_v2", data=data)

    def twitter_like(self, login_cookies: str, tweet_id: str, proxy: str) -> Dict[str, Any]:
        """Like a tweet."""
        return self._request("POST", "/twitter/like_tweet_v2", data={
            "login_cookies": login_cookies, "tweet_id": tweet_id, "proxy": proxy
        })

    def twitter_unlike(self, login_cookies: str, tweet_id: str, proxy: str) -> Dict[str, Any]:
        """Unlike a tweet."""
        return self._request("POST", "/twitter/unlike_tweet_v2", data={
            "login_cookies": login_cookies, "tweet_id": tweet_id, "proxy": proxy
        })

    def twitter_retweet(self, login_cookies: str, tweet_id: str, proxy: str) -> Dict[str, Any]:
        """Retweet a tweet."""
        return self._request("POST", "/twitter/retweet_tweet_v2", data={
            "login_cookies": login_cookies, "tweet_id": tweet_id, "proxy": proxy
        })

    def twitter_delete_tweet(self, login_cookies: str, tweet_id: str, proxy: str) -> Dict[str, Any]:
        """Delete a tweet."""
        return self._request("POST", "/twitter/delete_tweet_v2", data={
            "login_cookies": login_cookies, "tweet_id": tweet_id, "proxy": proxy
        })

    def twitter_follow(self, login_cookies: str, user_id: str, proxy: str) -> Dict[str, Any]:
        """Follow a user."""
        return self._request("POST", "/twitter/follow_user_v2", data={
            "login_cookies": login_cookies, "user_id": user_id, "proxy": proxy
        })

    def twitter_unfollow(self, login_cookies: str, user_id: str, proxy: str) -> Dict[str, Any]:
        """Unfollow a user."""
        return self._request("POST", "/twitter/unfollow_user_v2", data={
            "login_cookies": login_cookies, "user_id": user_id, "proxy": proxy
        })

    def twitter_send_dm(self, login_cookies: str, user_id: str, text: str, proxy: str) -> Dict[str, Any]:
        """Send a direct message to a user."""
        return self._request("POST", "/twitter/send_dm_to_user", data={
            "login_cookies": login_cookies, "user_id": user_id, "text": text, "proxy": proxy
        })
    
    # ==================== Search APIs ====================
    
    def search_web(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """Perform a web search (POST method)."""
        return self._request("POST", "/scholar/search/web", params={
            "query": query,
            "max_num_results": max_results
        })
    
    def search_scholar(self, query: str, max_results: int = 10, year_from: int = None, year_to: int = None) -> Dict[str, Any]:
        """Search academic papers and scholarly content (POST method)."""
        params = {
            "query": query,
            "max_num_results": max_results
        }
        if year_from:
            params["as_ylo"] = year_from
        if year_to:
            params["as_yhi"] = year_to
        return self._request("POST", "/scholar/search/scholar", params=params)
    
    def search_smart(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """Perform intelligent search combining web and academic results."""
        return self._request("POST", "/scholar/search/mixed", params={
            "query": query,
            "max_num_results": max_results
        })
    
    # ==================== News API ====================
    
    def news(self, ticker: str, count: int = 10) -> Dict[str, Any]:
        """Get company news by stock ticker."""
        return self._request("GET", "/financial/news", params={"ticker": ticker, "limit": count})
    
    # ==================== LLM APIs ====================
    
    def _llm_request(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make an HTTP request to the AIsa LLM API (different base URL)."""
        url = f"{self.LLM_BASE_URL}{endpoint}"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "OpenClaw-Starter-Kit/1.0"
        }
        
        request_data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, data=request_data, headers=headers, method="POST")
        
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                return {"success": False, "error": {"code": str(e.code), "message": error_body}}
        except urllib.error.URLError as e:
            return {"success": False, "error": {"code": "NETWORK_ERROR", "message": str(e.reason)}}
    
    def llm_complete(self, model: str, prompt: str, **kwargs) -> Dict[str, Any]:
        """Generate a completion using the specified LLM model."""
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            **kwargs
        }
        return self._llm_request("/chat/completions", data)
    
    def llm_chat(self, model: str, messages: list, **kwargs) -> Dict[str, Any]:
        """Perform a chat completion with message history."""
        data = {
            "model": model,
            "messages": messages,
            **kwargs
        }
        return self._llm_request("/chat/completions", data)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="OpenClaw Starter Kit - Unified API access for autonomous agents (Powered by AIsa)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s twitter user-info --username elonmusk
    %(prog)s twitter search --query "AI agents" --count 10
    %(prog)s search web --query "latest AI news"
    %(prog)s search scholar --query "transformer architecture"
    %(prog)s llm complete --model gpt-4 --prompt "Explain quantum computing"
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="API category")
    
    # Twitter commands
    twitter_parser = subparsers.add_parser("twitter", help="Twitter/X API operations")
    twitter_sub = twitter_parser.add_subparsers(dest="action", help="Twitter action")

    # ---- User Read Commands ----
    p = twitter_sub.add_parser("user-info", help="Get user information")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("user-about", help="Get user profile about")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("batch-users", help="Batch get users by IDs")
    p.add_argument("--user-ids", required=True, help="Comma-separated user IDs")

    p = twitter_sub.add_parser("tweets", help="Get user's latest tweets")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("mentions", help="Get user mentions")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("followers", help="Get user followers")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("followings", help="Get user followings")
    p.add_argument("--username", "-u", required=True)

    p = twitter_sub.add_parser("verified-followers", help="Get verified followers")
    p.add_argument("--user-id", required=True, help="User ID (not username)")

    p = twitter_sub.add_parser("check-follow", help="Check follow relationship")
    p.add_argument("--source", required=True, help="Source username")
    p.add_argument("--target", required=True, help="Target username")

    # ---- Search & Discovery ----
    p = twitter_sub.add_parser("search", help="Advanced tweet search")
    p.add_argument("--query", "-q", required=True)
    p.add_argument("--type", "-t", choices=["Latest", "Top"], default="Latest")

    p = twitter_sub.add_parser("user-search", help="Search for users")
    p.add_argument("--query", "-q", required=True)

    p = twitter_sub.add_parser("trends", help="Get trending topics")
    p.add_argument("--woeid", "-w", type=int, default=1)

    # ---- Tweet Detail Commands ----
    p = twitter_sub.add_parser("detail", help="Get tweets by IDs")
    p.add_argument("--tweet-ids", required=True, help="Comma-separated tweet IDs")

    p = twitter_sub.add_parser("replies", help="Get tweet replies")
    p.add_argument("--tweet-id", required=True)

    p = twitter_sub.add_parser("quotes", help="Get tweet quotes")
    p.add_argument("--tweet-id", required=True)

    p = twitter_sub.add_parser("retweeters", help="Get tweet retweeters")
    p.add_argument("--tweet-id", required=True)

    p = twitter_sub.add_parser("thread", help="Get tweet thread context")
    p.add_argument("--tweet-id", required=True)

    p = twitter_sub.add_parser("article", help="Get article by tweet ID")
    p.add_argument("--tweet-id", required=True)

    # ---- List Commands ----
    p = twitter_sub.add_parser("list-members", help="Get list members")
    p.add_argument("--list-id", required=True)

    p = twitter_sub.add_parser("list-followers", help="Get list followers")
    p.add_argument("--list-id", required=True)

    # ---- Community Commands ----
    p = twitter_sub.add_parser("community-info", help="Get community info")
    p.add_argument("--community-id", required=True)

    p = twitter_sub.add_parser("community-members", help="Get community members")
    p.add_argument("--community-id", required=True)

    p = twitter_sub.add_parser("community-moderators", help="Get community moderators")
    p.add_argument("--community-id", required=True)

    p = twitter_sub.add_parser("community-tweets", help="Get community tweets")
    p.add_argument("--community-id", required=True)

    p = twitter_sub.add_parser("community-search", help="Search all community tweets")
    p.add_argument("--query", "-q", required=True)

    p = twitter_sub.add_parser("space-detail", help="Get Space detail")
    p.add_argument("--space-id", required=True)

    # ---- Write Commands (require login_cookies + proxy) ----
    p = twitter_sub.add_parser("login", help="Login to Twitter account")
    p.add_argument("--username", "-u", required=True)
    p.add_argument("--email", "-e", required=True)
    p.add_argument("--password", "-p", required=True)
    p.add_argument("--proxy", required=True)
    p.add_argument("--totp-secret", help="2FA TOTP secret key")

    p = twitter_sub.add_parser("post", help="Create a tweet")
    p.add_argument("--cookies", required=True, help="login_cookies from login")
    p.add_argument("--text", "-t", required=True)
    p.add_argument("--proxy", required=True)
    p.add_argument("--reply-to", help="Tweet ID to reply to")

    p = twitter_sub.add_parser("like", help="Like a tweet")
    p.add_argument("--cookies", required=True)
    p.add_argument("--tweet-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("unlike", help="Unlike a tweet")
    p.add_argument("--cookies", required=True)
    p.add_argument("--tweet-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("retweet", help="Retweet a tweet")
    p.add_argument("--cookies", required=True)
    p.add_argument("--tweet-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("delete-tweet", help="Delete a tweet")
    p.add_argument("--cookies", required=True)
    p.add_argument("--tweet-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("follow", help="Follow a user")
    p.add_argument("--cookies", required=True)
    p.add_argument("--user-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("unfollow", help="Unfollow a user")
    p.add_argument("--cookies", required=True)
    p.add_argument("--user-id", required=True)
    p.add_argument("--proxy", required=True)

    p = twitter_sub.add_parser("send-dm", help="Send a direct message")
    p.add_argument("--cookies", required=True)
    p.add_argument("--user-id", required=True)
    p.add_argument("--text", "-t", required=True)
    p.add_argument("--proxy", required=True)
    
    # Search commands
    search_parser = subparsers.add_parser("search", help="Search API operations")
    search_sub = search_parser.add_subparsers(dest="action", help="Search type")
    
    # search web
    web_search = search_sub.add_parser("web", help="Web search")
    web_search.add_argument("--query", "-q", required=True, help="Search query")
    web_search.add_argument("--count", "-c", type=int, default=10, help="Max results (up to 100)")
    
    # search scholar
    scholar_search = search_sub.add_parser("scholar", help="Academic paper search")
    scholar_search.add_argument("--query", "-q", required=True, help="Search query")
    scholar_search.add_argument("--count", "-c", type=int, default=10, help="Max results (up to 100)")
    scholar_search.add_argument("--year-from", type=int, help="Publication year lower bound")
    scholar_search.add_argument("--year-to", type=int, help="Publication year upper bound")
    
    # search smart
    smart_search = search_sub.add_parser("smart", help="Smart search (web + academic)")
    smart_search.add_argument("--query", "-q", required=True, help="Search query")
    smart_search.add_argument("--count", "-c", type=int, default=10, help="Max results")
    
    # News commands
    news_parser = subparsers.add_parser("news", help="Company news by ticker")
    news_parser.add_argument("--ticker", "-t", required=True, help="Stock ticker (e.g., AAPL)")
    news_parser.add_argument("--count", "-c", type=int, default=10, help="Number of results")
    
    # LLM commands
    llm_parser = subparsers.add_parser("llm", help="LLM API operations")
    llm_sub = llm_parser.add_subparsers(dest="action", help="LLM action")
    
    # llm complete
    complete = llm_sub.add_parser("complete", help="Generate completion")
    complete.add_argument("--model", "-m", required=True, help="Model name (e.g., gpt-4, claude-3)")
    complete.add_argument("--prompt", "-p", required=True, help="Prompt text")
    complete.add_argument("--max-tokens", type=int, help="Maximum tokens to generate")
    complete.add_argument("--temperature", type=float, help="Sampling temperature")
    
    # llm chat
    chat = llm_sub.add_parser("chat", help="Chat completion")
    chat.add_argument("--model", "-m", required=True, help="Model name")
    chat.add_argument("--messages", required=True, help="JSON array of messages")
    chat.add_argument("--max-tokens", type=int, help="Maximum tokens to generate")
    chat.add_argument("--temperature", type=float, help="Sampling temperature")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        client = AIsaClient()
    except ValueError as e:
        print(json.dumps({"success": False, "error": {"code": "AUTH_ERROR", "message": str(e)}}))
        sys.exit(1)
    
    result = None
    
    # Execute the appropriate command
    if args.command == "twitter":
        act = args.action
        # User read commands
        if act == "user-info":
            result = client.twitter_user_info(args.username)
        elif act == "user-about":
            result = client.twitter_user_about(args.username)
        elif act == "batch-users":
            result = client.twitter_batch_user_info(args.user_ids)
        elif act == "tweets":
            result = client.twitter_user_tweets(args.username)
        elif act == "mentions":
            result = client.twitter_user_mentions(args.username)
        elif act == "followers":
            result = client.twitter_followers(args.username)
        elif act == "followings":
            result = client.twitter_followings(args.username)
        elif act == "verified-followers":
            result = client.twitter_verified_followers(args.user_id)
        elif act == "check-follow":
            result = client.twitter_check_follow(args.source, args.target)
        # Search & Discovery
        elif act == "search":
            result = client.twitter_search(args.query, args.type)
        elif act == "user-search":
            result = client.twitter_user_search(args.query)
        elif act == "trends":
            result = client.twitter_trends(args.woeid)
        # Tweet detail commands
        elif act == "detail":
            result = client.twitter_tweet_detail(args.tweet_ids)
        elif act == "replies":
            result = client.twitter_tweet_replies(args.tweet_id)
        elif act == "quotes":
            result = client.twitter_tweet_quotes(args.tweet_id)
        elif act == "retweeters":
            result = client.twitter_tweet_retweeters(args.tweet_id)
        elif act == "thread":
            result = client.twitter_tweet_thread(args.tweet_id)
        elif act == "article":
            result = client.twitter_article(args.tweet_id)
        # List commands
        elif act == "list-members":
            result = client.twitter_list_members(args.list_id)
        elif act == "list-followers":
            result = client.twitter_list_followers(args.list_id)
        # Community commands
        elif act == "community-info":
            result = client.twitter_community_info(args.community_id)
        elif act == "community-members":
            result = client.twitter_community_members(args.community_id)
        elif act == "community-moderators":
            result = client.twitter_community_moderators(args.community_id)
        elif act == "community-tweets":
            result = client.twitter_community_tweets(args.community_id)
        elif act == "community-search":
            result = client.twitter_community_search(args.query)
        elif act == "space-detail":
            result = client.twitter_space_detail(args.space_id)
        # Write commands (V2 - require login_cookies + proxy)
        elif act == "login":
            result = client.twitter_login(args.username, args.email, args.password, args.proxy, getattr(args, "totp_secret", None))
        elif act == "post":
            result = client.twitter_create_tweet(args.cookies, args.text, args.proxy, getattr(args, "reply_to", None))
        elif act == "like":
            result = client.twitter_like(args.cookies, args.tweet_id, args.proxy)
        elif act == "unlike":
            result = client.twitter_unlike(args.cookies, args.tweet_id, args.proxy)
        elif act == "retweet":
            result = client.twitter_retweet(args.cookies, args.tweet_id, args.proxy)
        elif act == "delete-tweet":
            result = client.twitter_delete_tweet(args.cookies, args.tweet_id, args.proxy)
        elif act == "follow":
            result = client.twitter_follow(args.cookies, args.user_id, args.proxy)
        elif act == "unfollow":
            result = client.twitter_unfollow(args.cookies, args.user_id, args.proxy)
        elif act == "send-dm":
            result = client.twitter_send_dm(args.cookies, args.user_id, args.text, args.proxy)
        else:
            twitter_parser.print_help()
            sys.exit(1)
    
    elif args.command == "search":
        if args.action == "web":
            result = client.search_web(args.query, args.count)
        elif args.action == "scholar":
            year_from = getattr(args, 'year_from', None)
            year_to = getattr(args, 'year_to', None)
            result = client.search_scholar(args.query, args.count, year_from, year_to)
        elif args.action == "smart":
            result = client.search_smart(args.query, args.count)
        else:
            search_parser.print_help()
            sys.exit(1)
    
    elif args.command == "news":
        result = client.news(args.ticker, args.count)
    
    elif args.command == "llm":
        kwargs = {}
        if hasattr(args, "max_tokens") and args.max_tokens:
            kwargs["max_tokens"] = args.max_tokens
        if hasattr(args, "temperature") and args.temperature is not None:
            kwargs["temperature"] = args.temperature
        
        if args.action == "complete":
            result = client.llm_complete(args.model, args.prompt, **kwargs)
        elif args.action == "chat":
            try:
                messages = json.loads(args.messages)
            except json.JSONDecodeError:
                print(json.dumps({"success": False, "error": {"code": "INVALID_JSON", "message": "Invalid JSON in --messages"}}))
                sys.exit(1)
            result = client.llm_chat(args.model, messages, **kwargs)
        else:
            llm_parser.print_help()
            sys.exit(1)
    
    # Output result
    if result:
        # Handle encoding for Windows console
        output = json.dumps(result, indent=2, ensure_ascii=False)
        try:
            print(output)
        except UnicodeEncodeError:
            # Fallback to ASCII-safe output
            print(json.dumps(result, indent=2, ensure_ascii=True))
        sys.exit(0 if result.get("success", True) else 1)


if __name__ == "__main__":
    main()
