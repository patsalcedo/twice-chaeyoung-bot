import tweepy
import os
import logging

logger = logging.getLogger()


def create_api():
    api_key = os.getenv("CONSUMER_KEY") # creates environmental variables
    api_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error during auth", exc_info=True)
        raise e
    logger.info("API created!")
    return api
