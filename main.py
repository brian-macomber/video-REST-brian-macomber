import flask
from flask import request, send_file

from config import q

import threading

from media_utility import MediaUtility

from threadFunction import runProcess


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def homepage():
    html = "<h1>Brian Macomber Video API - EC500</h1>"
    return html


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

    #  add the username to the queue here
    q.put(username)

    # wait until all threads are done before returning the video
    q.join()

    # need some way to check if process is not done yet
    # if process not done yet
    #   return html that says video is being made
    # else
    #   send video files
    return send_file("tweet_video.mp4")


if __name__ == "__main__":
    # this is based on the number of cores in the machine running this
    numThreads = 4

    threadList = []

    # create 4 threads
    for index in range(numThreads):
        # in args is where i will send data for each thread - daemon so itll run in the background
        thread_worker = threading.Thread(
            target=runProcess,
            daemon=True)
        threadList.append(thread_worker)

    # starts the threads
    for thread in threadList:
        thread.start()

    app.run()
