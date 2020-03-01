from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["DEBUG"] = True

api = Api(app)

# The request will be based on the twitter username
#    (what each process is recognized by)

# need a separate class for each url in my api


# class to interact with twitter
class twitterVideoAPI(Resource):
    def GET(self, username):
        pass

    def POST(self, username):
        pass

    def PUT(self, username):
        pass

    def PATCH(self, username):
        pass

    def DELETE(self, username):
        pass


# shows all the processes going on in the servers
class processesCheck():
    def __init__(self):
        pass

    def get(self):
        pass


api.add_resource(twitterVideoAPI, "/tweets/<string:username>", endpoint="user")
api.add_resource(processesCheck, "/processes>", endpoint="user")


if __name__ == "__main__":
    app.run()
