import tweepy
import logging
from configapi import create_api
from followback import follow_back
from constantretweets import official_acc_updates
from favretweetstream import FavRetweetListener
from favretweetsearch import search_chaeyoung
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    # keywords = ["chaeyoung","son chaeyoung", "채영"]
    # tweets_listener = FavRetweetListener(api)
    # stream = tweepy.Stream(api.auth, tweets_listener)
    # stream.filter(track=keywords, languages=["en"])

    while True:
        # follow_back(api)
        official_acc_updates(api, "JYPETWICE")
        official_acc_updates(api, "misayeon")
        search_chaeyoung(api)
        logger.info("Waiting...")
        time.sleep(30) # follow_back method is called every 60s to check for new followers.


if __name__ == "__main__":
    main()