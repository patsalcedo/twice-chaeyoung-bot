import tweepy
import logging
from configapi import create_api
import json

logging.basicConfig(lovel=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()


    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.create_favorite(tweet.id)
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
                pass
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                except Exception as e:
                    logger.error("Error on fav and retweet", exc_info=True)
                    pass

    def on_error(self, status):
        logger.error(status)
