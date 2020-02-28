from media_utility import MediaUtility
from twitter_utility import TwitterUtility

import os


# ************** testing authentication ****************
def test_authentication():
    path = "keys"

    if os.path.isfile(path):
        auth = TwitterUtility().get_auth(path)
        assert auth is None
    else:
        # only if keys dont exist
        assert 1 == 1


# ************** testing get_tweets ****************
def test_validUser():
    path = "keys"
    user = "realDonaldTrump"

    if os.path.isfile(path):
        twitter = TwitterUtility()
        auth = twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert isinstance(tweets, list) == 1
    else:
        assert 1 == 1


def test_noTweetsUser():
    path = "keys"
    user = "Brian_Macomber"

    if os.path.isfile(path):
        twitter = TwitterUtility()
        auth = twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert tweets == []
    else:
        assert 1 == 1


def test_emptyUser():
    path = "keys"
    user = ""

    if os.path.isfile(path):
        twitter = TwitterUtility()
        auth = twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert tweets == []
    else:
        assert 1 == 1


def test_nonexistentUser():
    path = "keys"
    user = "aftvbsefygasdkjfhagskjalskcfuyagkfya"

    if os.path.isfile(path):
        twitter = TwitterUtility()
        auth = twitter.get_auth(path)
        tweets = twitter.get_tweets(user)
        print(tweets)
        assert tweets == "<h1>User doesn't exist, try a real user</h1>"
    else:
        assert 1 == 1


# ************** testing media ****************
def test_wrongFormatTweet():
    tweet = ["hello"]

    media = MediaUtility()
    media_ex = media.tweet_2_image(tweet)

    assert media_ex == "<h1>Tweets from API not formatted correctly</h1>"
