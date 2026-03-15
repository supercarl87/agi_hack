#!/usr/bin/env python3
"""
Script to post a tweet thread to X/Twitter

Prerequisites:
1. Install tweepy: pip install tweepy
2. Get API credentials from https://developer.twitter.com/
3. Set environment variables:
   - TWITTER_API_KEY
   - TWITTER_API_SECRET
   - TWITTER_ACCESS_TOKEN
   - TWITTER_ACCESS_SECRET
   - TWITTER_BEARER_TOKEN (for v2 API)

Usage:
    python post_to_twitter.py
"""

import os
import tweepy
import time

# Tweet thread content
tweets = [
    # Tweet 1 (Main)
    """🚀 Just watched an incredible conversation with Peter Steinberger, creator of OpenClaw - the open-source AI agent that exploded to 160K+ GitHub stars overnight.

Here's why it's reshaping how we think about AI agents and the future of software 🧵

https://www.youtube.com/watch?v=4uzGDAoNOZc""",

    # Tweet 2
    """The secret? OpenClaw runs LOCALLY on your computer, not in the cloud.

This gives it access to EVERYTHING you have access to - your files, APIs, smart home devices, forgotten data.

It's not an app. It's a friend with superpowers. 🤖""",

    # Tweet 3
    """The "holy f*ck" moment:

Peter sent a voice message while walking. He hadn't built voice support.

10 seconds later, the bot replied.

How? It taught itself: detected the audio format → used ffmpeg → found an OpenAI key → transcribed with curl

Pure creative problem-solving. 🧠""",

    # Tweet 4
    """Peter's prediction: 80% of apps will disappear.

Why need MyFitnessPal when your agent already tracks what you eat?
Why need a to-do app when it just remembers?

"Every app that manages data could be managed better by agents."

Only apps with sensors survive. 📱→🤖""",

    # Tweet 5
    """The shift happening now:

Everyone chased "god intelligence" (one super-smart AI)

But what's emerging is "swarm intelligence" (specialized agents working together)

Just like humans: alone we struggle, together we build iPhones and go to space. 🐝""",

    # Tweet 6
    """Your agent memories become more sensitive than your search history.

OpenClaw stores everything locally as markdown files.

No vendor lock-in. No data silos.

You own your data. Your memories. Your digital soul. 🔐""",

    # Tweet 7
    """Coming soon:

→ Your bot books restaurants by negotiating with the restaurant's bot
→ Bots hire humans for IRL tasks
→ Specialized bots for work, personal life, relationships

We're moving from human-to-bot to bot-to-bot interactions. 🤝""",

    # Tweet 8
    """Peter's philosophy:

✗ No MCP headaches - just converted them to CLIs
✗ No git worktrees - multiple repo checkouts
✗ No complex tooling - keep it simple

"Humans don't manually call MCPs. We use CLIs. That's the future."

Simplicity scales. 🎯""",

    # Tweet 9
    """Perhaps most inspiring:

This breakthrough came from "a loner from some tiny country far away from Silicon Valley."

Not from a big tech lab. From one person scratching their own itch.

The future is being built by independent hackers. 🌍""",

    # Tweet 10
    """Key takeaways:

1. Local execution unlocks true agent power
2. Coding models = creative problem-solving
3. 80% of apps are obsolete
4. Data ownership > model quality
5. Swarm intelligence > god intelligence
6. Innovation comes from anywhere

Watch full convo 👇""",

    # Tweet 11 (Final)
    """The hedonic treadmill is real:

Each new model becomes the baseline. Yesterday's "OMG amazing" is tomorrow's "meh, not good enough."

But what remains constant? Your data, your memories, your local control.

Full summary available in the repo!"""
]


def post_thread_v2():
    """Post thread using Twitter API v2"""
    # Initialize v2 client
    client = tweepy.Client(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
        consumer_key=os.getenv('TWITTER_API_KEY'),
        consumer_secret=os.getenv('TWITTER_API_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
    )

    print("Starting to post thread...")
    previous_tweet_id = None

    for i, tweet_text in enumerate(tweets, 1):
        try:
            # Post tweet (first tweet or reply to previous)
            if previous_tweet_id is None:
                response = client.create_tweet(text=tweet_text)
                print(f"✓ Posted tweet {i}/{len(tweets)}")
            else:
                response = client.create_tweet(
                    text=tweet_text,
                    in_reply_to_tweet_id=previous_tweet_id
                )
                print(f"✓ Posted reply {i}/{len(tweets)}")

            previous_tweet_id = response.data['id']

            # Small delay to avoid rate limits
            if i < len(tweets):
                time.sleep(2)

        except Exception as e:
            print(f"✗ Error posting tweet {i}: {e}")
            return False

    print(f"\n✓ Successfully posted thread of {len(tweets)} tweets!")
    print(f"View thread: https://twitter.com/i/web/status/{tweets[0].data['id']}")
    return True


def main():
    # Check for required environment variables
    required_vars = [
        'TWITTER_API_KEY',
        'TWITTER_API_SECRET',
        'TWITTER_ACCESS_TOKEN',
        'TWITTER_ACCESS_SECRET',
        'TWITTER_BEARER_TOKEN'
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        print("Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease set these variables and try again.")
        print("\nTo get credentials:")
        print("1. Go to https://developer.twitter.com/")
        print("2. Create a project and app")
        print("3. Generate API keys and access tokens")
        print("4. Set environment variables:")
        print("   export TWITTER_API_KEY='your_key'")
        print("   export TWITTER_API_SECRET='your_secret'")
        print("   export TWITTER_ACCESS_TOKEN='your_token'")
        print("   export TWITTER_ACCESS_SECRET='your_token_secret'")
        print("   export TWITTER_BEARER_TOKEN='your_bearer_token'")
        return False

    print(f"Preparing to post thread of {len(tweets)} tweets...")
    print("\nFirst tweet preview:")
    print("-" * 60)
    print(tweets[0][:200] + "..." if len(tweets[0]) > 200 else tweets[0])
    print("-" * 60)

    confirm = input("\nProceed with posting? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Cancelled.")
        return False

    return post_thread_v2()


if __name__ == "__main__":
    main()
