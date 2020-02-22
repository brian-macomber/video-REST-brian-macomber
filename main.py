import tweepy
from secret import consumer_key
from secret import consumer_key_secret
from secret import access_token
from secret import access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

timeline = api.user_timeline(screen_name="Brian_Macomber", count=5)

for tweet in timeline:
    print(tweet.text.encode("utf-8"))
