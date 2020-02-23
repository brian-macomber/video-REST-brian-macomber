import tweepy
import flask
from flask import request, send_file
from datetime import datetime, timedelta
from PIL import Image, ImageDraw

# import matplotlib.pyplot as plt
# import matplotlib.image as img

import textwrap

import os

from secret import consumer_key
from secret import consumer_key_secret
from secret import access_token
from secret import access_token_secret

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# function to remove any tweet png files from the previous run
# needed so it does not prompt user to overwrite previous file
def cleanFiles():
    for curr_file in os.listdir():
        if curr_file.endswith(".mp4") or curr_file.endswith(".mp4"):
            os.remove(curr_file)


def get_Tweets(screen_name):
    # handling authentiation using tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # actually creates interface to call twitter api
    api = tweepy.API(auth, wait_on_rate_limit=True)

    timeline = api.user_timeline(screen_name=screen_name, count=100,
            exclude_replies=True, include_rts=1)

    today = datetime.now()

    currTweets = []

    for tweet in timeline:
        # check if tweet was within the last 24 hours
        if today - timedelta(hours=24) <= tweet.created_at <= today:
            # wrapper function for tweets goes here
            wrapped_tweet = textwrap.wrap(tweet.text, width=40)
            currTweets.append(wrapped_tweet)

    return currTweets


def tweet_2_image(tweet_list):
    image_dims = (400, 250)
    tweet_no = 1

    for tweet in tweet_list:
        curr_image = Image.new('RGB', image_dims, color='black')
        image = ImageDraw.Draw(curr_image)

        # draws text onto image - iterate through lines of the wrapped tweet
        i = 0
        for line in tweet:
            image.text((50, 100 + i), line.encode('utf-8'), fill=(255, 255, 255))
            i = i + 10

        img_name = "tweet_" + str(tweet_no) + ".png"
        curr_image.save(img_name)

        tweet_no = tweet_no + 1

        # im = img.imread('test_image.png')
        # plt.imshow(im)
        # plt.show()


# *********** Uncomment here to run on localhost ****************
# once functional - it will go to this localhost
@app.route('/', methods=['GET'])
def homepage():
    html = "<h1>Brian Macomber Video API - EC500</h1>"
    return html


@app.route('/tweets', methods=['GET'])
def user_api():

    cleanFiles()

    if 'user' in request.args:
        username = request.args['user']
    else:
        username = "overwatchleague"

    tweets = get_Tweets(username)
    tweet_2_image(tweets)

    # create video using ffmpeg
    os.system("ffmpeg -r 30 -f image2  -s 400x250 -i tweet_%d.png -vcodec libx264\
        -crf 25 -pix_fmt yuv420p -filter:v \"setpts=50.0*PTS\" tweet_video.mp4")

    return send_file("tweet_video.mp4")


app.run()


# if __name__ == "__main__":
#     tweets = get_Tweets("overwatchleague")
#     tweet_2_image(tweets)

#     # create video using ffmpeg
#     os.system("ffmpeg -r 30 -f image2  -s 400x250 -i tweet_%d.png -vcodec libx264\
#          -crf 25 -pix_fmt yuv420p -filter:v \"setpts=25.0*PTS\" tweet_video.mp4")

#     #need to delete previous pics and videos before it runs each time **
