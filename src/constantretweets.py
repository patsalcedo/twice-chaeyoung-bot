import tweepy
import logging
from configapi import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def official_acc_updates(api, username):  # might have username as input param
    logger.info(f"Checking @{username}'s tweets for updates")
    tweets = api.user_timeline(id=username, count=10, include_rts=True, tweet_mode='extended')
    for tweet in tweets:
        if not tweet.favorited:
            try:
                logger.info(f"Liking @{username}'s tweet")
                api.create_favorite(tweet.id)
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
            if not tweet.retweeted:
                try:
                    logger.info(f"Retweeting @{username}'s tweet")
                    api.retweet(tweet.id)
                except Exception as e:
                    logger.error("Error on retweet", exc_info=True)
