from PIL import Image, ImageDraw
import os


class MediaUtility():

    def tweet_2_image(self, tweet_list):
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

    def create_video(self):
        os.system("ffmpeg -r 30 -f image2  -s 400x250 -i tweet_%d.png -vcodec libx264\
         -crf 25 -pix_fmt yuv420p -filter:v \"setpts=25.0*PTS\" tweet_video.mp4")

    def media_cleanup(self):
        for curr_file in os.listdir():
            if curr_file.endswith(".png") or curr_file.endswith(".mp4"):
                os.remove(curr_file)
