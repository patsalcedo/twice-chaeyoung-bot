import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_back(api):
    logger.info("Following back the followers of this bot")
    # this checks the followers in the account
    # [api].followers is the method to get the list of followers.
    for follower in tweepy.Cursor(api.followers).items():  # cursor handles paginated results
        if not follower.following:
            try:
                logger.info(f"Following {follower.name}")
                follower.follow() # follow() is an in-built function.
            except Exception as e:
                logger.error("Error on follow back", exc_info=True)
                pass
