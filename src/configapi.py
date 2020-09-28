import tweepy
from tweepy import OAuthHandler
import logging
import os
from os.path import join, dirname
from dotenv import load_dotenv

logger = logging.getLogger()

def create_api():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_key = os.environ.get("CONSUMER_KEY") # creates environmental variables
    api_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('alg')
    except Exception as e:
        logger.error("Error during auth", exc_info=True)
        raise e
    logger.info("API created!")
    return api
