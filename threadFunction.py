from twitter_utility import TwitterUtility
from media_utility import MediaUtility

from config import q


def runProcess():

    # get from queue - can recieve username here
    username = q.get()

    media = MediaUtility()
    twitter = TwitterUtility()

    auth_exception = twitter.get_auth("keys")

    if auth_exception:
        return auth_exception

    tweets = twitter.get_tweets(username)
    if not tweets:
        html = "<h1>User has no tweets within the past 24 hours,\
                 try another user.</h1>"
        return html

    # error case for undefined user
    elif isinstance(tweets, str):
        return tweets

    media.tweet_2_image(tweets)
    media.create_video()

    # run task done for the thread here
    q.task_done()
