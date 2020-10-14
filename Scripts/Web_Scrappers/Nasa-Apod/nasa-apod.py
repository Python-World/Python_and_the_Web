# Downloads Nasa's Astronomy Pic Of The Day and set it as the Desktop Background
import ctypes
import os
import re
import requests
import wget

DIR = os.path.expanduser('~/Pictures/Astronomy Pic Of The Day')
base_url = 'https://apod.nasa.gov/apod/'

# Create the directory in which we will keep the Pics
try:
	os.makedirs(DIR)
except FileExistsError:
	pass

# Scrap the Image url
pattern = '<a href="(.*)">\s<IMG [\w\W]*></a>'
with requests.get(base_url) as r:
	image_url = re.search(pattern, r.text).group(1)
	image_url = base_url + image_url
print(f"[DOWNLOADING]: {image_url}")

# Download the image, skip if already downloaded
#if not os.path.exists(os.path.join(DIR, )):
filename = wget.download(image_url, out=DIR)
print(f"saved to {filename}")

# Set the wallpaper (https://stackoverflow.com/a/46504228)
ctypes.windll.user32.SystemParametersInfoW(20, 0, filename, 0)
