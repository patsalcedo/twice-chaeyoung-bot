import tweepy
import logging

logging.basicConfig(lovel=logging.INFO)
logger = logging.getLogger()

def search_chaeyoung(api):
    logger.info("Searching tweets with Chaeyoung")
    for tweet in api.search(q="chaeyoung", lang="en", rpp=10):
        if not tweet.favorited:
            try:
                logger.info(f"Liking @{tweet.user.name}'s tweet")
                api.create_favorite(tweet.id)
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
            if not tweet.retweeted:
                try:
                    logger.info(f"Retweeting @{tweet.user.name}'s tweet")
                    api.retweet(tweet.id)
                except Exception as e:
                    logger.error("Error on retweet", exc_info=True)