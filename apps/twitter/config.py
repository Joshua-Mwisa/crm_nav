import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "EQqK3RmbbFD0uFcR7nVebzU3p"
    consumer_secret = "ISlMZ4tmKrUJBIn6YsDqRR8aSpRANa7i1J4UN38liNKgK3m7ib"
    access_token = "1371532600112734215-xmhdWNOoQP1ec7LuRxWNBm2owCCHKI"
    access_token_secret = "Q9ayJzTvZyN9wZVwZgxGnHxVupnou5JIE55VYpKQZDGq0"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api