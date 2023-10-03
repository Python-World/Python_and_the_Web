import datetime
import os
import re

import requests

DIR = os.path.expanduser("~/Pictures/Dilbert/")
# Create the directory in which we will keep the Pics
try:
    os.makedirs(DIR)
except FileExistsError:
    pass

print("Downloading Latest Dilbert... Hold On...")

# Step-1: Scrap the image url (I used regex, you can also use BeautifulSoup). BTW BeautifulSoup is an overkill for this simple task
today = datetime.date.today()
url = "https://dilbert.com/strip/" + today.isoformat()
regex = '"image": "(.*)",'

with requests.get(url) as r:
    r.raise_for_status()  # raise an error if something unexpected occured
    image_url = re.search(regex, r.text).group(1)
    print(image_url)


# Step-2: Download the image and save it in the current directory
filename = os.path.join(DIR, "Dilbert " + today.isoformat() + ".png")
with requests.get(image_url) as r:  # request the image
    r.raise_for_status()
    with open(filename, "wb") as f:  # open the file for writing
        f.write(r.content)  # save the contents of image


# Step-3: Open the image file with the default image viewer
os.startfile(
    filename
)  # this acts like double-clicking the file in Explorer. see help(os.startfile)
