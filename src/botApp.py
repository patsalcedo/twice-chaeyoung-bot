import tweepy
import logging
from configapi import create_api
from followback import follow_back
from constantretweets import official_acc_updates
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    while True:
        follow_back(api)
        official_acc_updates(api, "JYPETWICE")
        official_acc_updates(api, "misayeon")
        logger.info("Waiting...")
        time.sleep(10) # follow_back method is called every 60s to check for new followers.


if __name__ == "__main__":
    main()