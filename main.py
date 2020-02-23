import flask
from flask import request, send_file

from twitter_utility import TwitterUtility
from media_utility import MediaUtility


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# *********** Uncomment here to run on localhost ****************
# once functional - it will go to this localhost
@app.route('/', methods=['GET'])
def homepage():
    html = "<h1>Brian Macomber Video API - EC500</h1>"
    return html


@app.route('/tweets', methods=['GET'])
def user_api():

    media = MediaUtility()
    twitter = TwitterUtility()

    media.media_cleanup()

    if 'user' in request.args:
        username = request.args['user']
    else:
        username = "overwatchleague"

    auth_exception = twitter.get_auth("keys")

    if auth_exception:
        return auth_exception

    tweets = twitter.get_tweets(username)
    if tweets == -1:
        html = "<h1>User has no tweets within the past 24 hours,\
                 try another user.</h1>"
        return html
    elif tweets == -2:
        html = "<h1>User doesn't exist, try a real user</h1>"
        return html

    media.tweet_2_image(tweets)
    media.create_video()

    return send_file("tweet_video.mp4")


app.run()


# if __name__ == "__main__":

#     media = MediaUtility()
#     twitter = TwitterUtility()

#     media.media_cleanup()

#     user = "overwatchleague"

#     twitter.get_auth("keys")
#     tweets = twitter.get_tweets(user)

#     media.tweet_2_image(tweets)
#     media.create_video()
