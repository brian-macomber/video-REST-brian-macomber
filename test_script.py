from media_utility import MediaUtility
from twitter_utility import TwitterUtility

import os

'''
    Note: Tests that use the twitter api first check to see if the 'keys' file
    exists in the current directory. If the file is not present, the tests will
    pass gracefully so that the workflow upon pushings
    to github remainds intact.
'''


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
        twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert isinstance(tweets, list) == 1
    else:
        assert 1 == 1


def test_noTweetsUser():
    path = "keys"
    user = "Brian_Macomber"

    if os.path.isfile(path):
        twitter = TwitterUtility()
        twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert tweets == []
    else:
        assert 1 == 1


def test_emptyUser():
    path = "keys"
    user = ""

    if os.path.isfile(path):
        twitter = TwitterUtility()
        twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert tweets == []
    else:
        assert 1 == 1


def test_nonexistentUser():
    path = "keys"
    user = "aftvbsefygasdkjfhagskjalskcfuyagkfya"

    if os.path.isfile(path):
        twitter = TwitterUtility()
        twitter.get_auth(path)
        tweets = twitter.get_tweets(user)

        assert tweets == "<h1>User doesn't exist, try a real user</h1>"
    else:
        assert 1 == 1


# ************** testing media ****************
def test_wrongFormatTweet():
    tweet = ["hello"]

    media = MediaUtility()
    media_ex = media.tweet_2_image(tweet)

    assert media_ex == "<h1>Tweets from API not formatted correctly</h1>"


def test_emptyTweets():
    tweet = []

    media = MediaUtility()
    media_ex = media.tweet_2_image(tweet)

    assert media_ex is None


def test_removeFiles():
    testPNG = "tweet_0.png"
    testMP4 = "test.mp4"
    testFile = "test.txt"

    os.system("touch " + testPNG)
    os.system("touch " + testMP4)
    os.system("touch " + testFile)

    media = MediaUtility()
    media.media_cleanup()

    assert os.path.isfile(testPNG) is False
    assert os.path.isfile(testMP4) is False
    assert os.path.isfile(testFile) is True


def test_removeOnlyPNG():
    testPNG = "tweet_0.png"
    testMP4 = "test.mp4"
    testFile = "test.txt"

    os.system("touch " + testPNG)
    os.system("touch " + testMP4)
    os.system("touch " + testFile)

    media = MediaUtility()
    media.png_cleanup()

    assert os.path.isfile(testPNG) is False
    assert os.path.isfile(testMP4) is True
    assert os.path.isfile(testFile) is True
