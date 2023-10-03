import glob
import os
import subprocess
import sys

from PIL import Image

# process each video in media folder
for video in glob.glob("media/*"):
    # only process videos, ignore generated images
    if "jpeg" not in video:
        # get video resolution
        try:
            cwd = os.getcwd()
            path = cwd + "/" + video
            result = subprocess.run(
                [
                    "/usr/bin/ffprobe",
                    "-v",
                    "error",
                    "-select_streams",
                    "v:0",
                    "-show_entries",
                    "stream=width,height",
                    "-of",
                    "csv=s=,:p=0",
                    path,
                ],
                check=True,
                stdout=subprocess.PIPE,
            )
        except Exception:
            print("Error running ffprobe.")
            sys.exit()

        resolution = result.stdout.decode("utf-8")
        height, width = resolution.split(",")
        height = int(height)
        width = int(width)

        # from each frame of the video, grab the center pixels and store them temporarily
        os.system(
            "ffmpeg -i "
            + video
            + ' -filter:v "crop=2:'
            + str(height)
            + ":"
            + str(width / 2)
            + ':1" -q:v 1 tmp/images-%04d.jpeg'
        )

        # define the series of images to be processed from the temp images
        series = glob.glob("tmp/*.jpeg")
        # the composite will be as wide as the number of images
        image_size = (len(series), height)
        # Create empty image
        composite = Image.new("RGB", image_size)
        pix_col = 0

        # loop through the images and fill the composite
        for tmp_img in series:
            file, ext = os.path.splitext(tmp_img)
            image = Image.open(tmp_img)
            image_strip = image.crop((0, 0, 1, height))
            composite.paste(image_strip, (pix_col, 0))
            # pix_col is used to keep track of where the 'building' of the image is, from left to right by pixels
            pix_col += 1
            image.close()
            os.remove(tmp_img)

        # save composite
        composite.save(video + "_unwrapped.jpeg", "JPEG")
