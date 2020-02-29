# Twitter Video API

### Brian Macomber
#### EC500 - Building Software
#### Professor Osama Alshaykh

### Objectives:
- Using the twitter feed of a specified user, construct a daily video summarizing the user's tweets from the last 24 hours.
    - Use the twitter API along with the FFMPEG library to complete this.
- Integrate Continuous Build and Continous Integration to check if the software in each development stage passed the build process. 
- Develop a queue system such that each process is multi-threaded and the API can handle more than 1 request at once.

### Summary:
This API uses the user's twitter handle to call the user_timeline Twitter API. Each tweet in the list of tweets from the past 24 hours
is converted into an image, then all of these images are concatenated together into a video using the FFMPEG library. The API is also multi-threaded
so it can handle more than one process at once. This implmentation uses 4 threads, assuming the user's computer has 4 cores.

### How to run:
- Clone the github repository to your computer.
- Make sure the most recent version of python is installed (https://www.python.org/downloads/).
- On the command line run: (this will install all of the required dependencies to run the app).
    `pip3 install -r requirements.txt`
- Create a file called 'keys' and add the twitter keys and tokens to it in the following format:  
    `[auth]`  
    `consumer_key = ****`  
    `consumer_secret = ****`  
    `access_token = ****`  
    `access_secret = ****`  
- run: `python3 main.py` to start the application.
- To view the home-page: `http://127.0.0.1:5000/`
- To view the default video created for @overwatchleague `http://127.0.0.1:5000/tweets`
- To run with a specified user: `http://127.0.0.1:5000/tweets?user=USERNAME` (replace USERNAME with desired user)
- To view the current/past requests: `http://127.0.0.1:5000/processses`


### References:
- http://docs.tweepy.org/en/latest/auth_tutorial.html
- https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
- https://pillow.readthedocs.io/en/stable/
- https://realpython.com/intro-to-python-threading/
