from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import textwrap
import requests


class MediaUtility():

    def tweet_2_image(self, tweet_list):
        image_dims = (1280, 720)
        tweet_no = 1

        for tweet in tweet_list:

            curr_image = Image.new('RGB', image_dims, color='white')
            image = ImageDraw.Draw(curr_image)

            # wrapper function for tweets goes here
            wrapped_tweet = textwrap.wrap(tweet.text, width=80)

            # draws text onto image - iterate through lines of the wrapped tweet
            i = 0
            for line in wrapped_tweet:
                image.text(
                    (320, 200 + i),
                    line.encode('cp1252', 'ignore'),
                    fill=(0, 0, 0),
                )
                i = i + 10

            # adds picture if tweet includes an image
            if 'media' in tweet.entities:
                self.add_media(tweet, curr_image)

            img_name = "tweet_" + str(tweet_no) + ".png"
            curr_image.save(img_name)

            tweet_no = tweet_no + 1

    def add_media(self, tweet, img):
        img_url = tweet.entities["media"][0]["media_url"]
        # next two lines of code found here
        # https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
        response = requests.get(img_url)
        tweet_image = Image.open(BytesIO(response.content))

        tweet_image.thumbnail((320, 200))
        img.paste(tweet_image, (0, 0))

    def create_video(self):
        os.system("ffmpeg -r 30 -f image2  -s 1280x720 -i tweet_%d.png -vcodec libx264\
         -crf 25 -pix_fmt yuv420p -filter:v \"setpts=200.0*PTS\" tweet_video.mp4")

    def media_cleanup(self):
        for curr_file in os.listdir():
            if curr_file.endswith(".png") or curr_file.endswith(".mp4"):
                os.remove(curr_file)

    def png_cleanup(self):
        for curr_file in os.listdir():
            if curr_file.endswith(".png"):
                os.remove(curr_file)
