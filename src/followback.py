import tweepy
import logging
from configapi import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_back(api):
    logger.info("Following back the followers of this bot")
    # this checks the followers in the account
    # [api].followers is the method to get the list of followers.
    for follower in tweepy.Cursor(api.followers).items():  # cursor handles paginated results
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow() # follow() is an in-built function.
