import tweepy
from datetime import datetime, timedelta
from secret import consumer_key
from secret import consumer_key_secret
from secret import access_token
from secret import access_token_secret


def get_Tweets(screen_name):
    # handling authentiation using tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # actually creates interface to call twitter api
    api = tweepy.API(auth, wait_on_rate_limit=True)

    timeline = api.user_timeline(screen_name=screen_name, count=100,\
         exclude_replies=True, include_rts=1)

    today = datetime.now()

    currTweets = []

    for tweet in timeline:
        # check if tweet was within the last 24 hours
        if today-timedelta(hours=24) <= tweet.created_at <= today:
            currTweets.append(tweet.text)
    return currTweets


def tweet_2_image(tweet_list):
    for tweet in tweet_list:
        print(type(tweet))




if __name__ == "__main__":
    tweets = get_Tweets("overwatchleague")
    yonk = tweet_2_image(tweets)
