import tweepy
import configparser
from datetime import datetime, timedelta
import textwrap


# import pdb; pdb.set_trace()


class TwitterUtility():

    def get_auth(self, path_name):
        config = configparser.ConfigParser()
        config.read(path_name)

        # handling authentiation using tweepy
        try:
            auth = tweepy.OAuthHandler(
                config.get("auth", "consumer_key"),
                config.get("auth", "consumer_secret"))
            auth.set_access_token(
                config.get("auth", "access_token"),
                config.get("auth", "access_secret"))

            # this will throw the error if authentication is incorrect
            auth.get_username()

            # actually creates interface to call twitter api
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
            return None

        except tweepy.error.TweepError:
            html = "<h1>There was a problem with authentication,\
                 check your keys</h1>"
            return html

    def get_tweets(self, screen_name):
        try:
            timeline = self.api.user_timeline(
                screen_name=screen_name,
                count=20,
                exclude_replies=True,
                include_rts=1)

            today = datetime.now()

            currTweets = []

            for tweet in timeline:
                # check if tweet was within the last 24 hours
                if today - timedelta(hours=24) <= tweet.created_at <= today:
                    currTweets.append(tweet)

            return currTweets
        except tweepy.error.TweepError:
            html = "<h1>User doesn't exist, try a real user</h1>"
            return html
