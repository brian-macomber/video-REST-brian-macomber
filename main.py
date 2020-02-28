import flask
from flask import request, send_file, jsonify

import config

import threading

from media_utility import MediaUtility
from twitter_utility import TwitterUtility

from threadFunction import runProcess


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def homepage():
    html = "<h1>Brian Macomber Video API - EC500</h1>"
    return html


@app.route('/processes', methods=['GET'])
def currentProcesses():
    return jsonify(config.queuedJobs)


@app.route('/tweets', methods=['GET'])
def user_api():

    # clears pictures and videos from prior call
    media = MediaUtility()
    media.media_cleanup()

    # uses overwatchleague twitter if none found in url
    if 'user' in request.args:
        username = request.args['user']
    else:
        username = "overwatchleague"

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
    #  add the username to the queue here
    else:
        # if there are no errors authenticating and getting tweets,
        # queue the video creation for that user
        job = {
            "user": username,
            "id": config.index,
            "status": "in progress"
            }

        config.queuedJobs.append(job)
        config.index += 1

        config.q.put(job)

        # waitMessage = "<h1>Your video is being created, please wait :)</h1>"
        # wait until queue is empty before returning the video
        config.q.join()

        media.png_cleanup()

        return send_file("tweet_video.mp4")


if __name__ == "__main__":
    # this is based on the number of cores in the machine running this
    numThreads = 4

    threadList = []

    # create 4 threads
    for i in range(numThreads):
        # in args is where i will send data for each thread
        # - daemon so itll run in the background
        thread_worker = threading.Thread(
            target=runProcess,
            daemon=True)
        threadList.append(thread_worker)

    # starts the threads
    for thread in threadList:
        thread.start()

    app.run()
