import flask
from flask import send_file, jsonify
from flask_restful import Api, Resource, request

import config

import threading

from media_utility import MediaUtility
from twitter_utility import TwitterUtility

from threadFunction import runProcess


app = flask.Flask(__name__)
app.config["DEBUG"] = True

api = Api(app)


class HomePage(Resource):
    def get(self):
        html = "<h1>Brian Macomber Video API - EC500</h1>"
        return html


class Processes(Resource):
    def get(self):
        return jsonify(config.queuedJobs)


class User_API(Resource):
    def get(self):

        # clears pictures and videos from prior call
        media = MediaUtility()
        media.media_cleanup()

        # uses overwatchleague twitter if none found in url
        try:
            username = request.args['user']
        except Exception:
            html = "<h1>Please specify a user in the URL arguments</h1>"
            return html

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

            # wait until queue is empty before returning the video
            config.q.join()

            media.png_cleanup()

            return send_file(f"{username}_tweet_video.mp4")


api.add_resource(HomePage, '/')
api.add_resource(Processes, '/processes')
api.add_resource(User_API, '/tweets')


if __name__ == "__main__":
    # this is based on the number of cores in the machine running this
    numThreads = 4

    threadList = []

    for i in range(numThreads):
        # creating the thread
        thread_worker = threading.Thread(
            target=runProcess,
            daemon=True)
        threadList.append(thread_worker)

    # starts the threads
    for thread in threadList:
        thread.start()

    app.run(host="0.0.0.0")
