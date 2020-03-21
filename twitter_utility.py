import tweepy
import configparser
from datetime import datetime, timedelta


# import pdb; pdb.set_trace()


class TwitterUtility():

    def get_auth(self, path_name):
        config = configparser.ConfigParser()
        config.read(path_name)
        html = "<h1>There was a problem with authentication,\
                 check your keys</h1>"

        # handling authentiation using tweepy
        auth = tweepy.OAuthHandler(
            config.get("auth", "consumer_key"),
            config.get("auth", "consumer_secret"))
        auth.set_access_token(
            config.get("auth", "access_token"),
            config.get("auth", "access_secret"))

        # actually creates interface to call twitter api
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

        # verify the credentials
        try:
            self.api.verify_credentials()
            return None
        except tweepy.error.TweepError:
            return html

        return None

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
