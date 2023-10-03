import os
import re
import webbrowser

import requests
from bs4 import BeautifulSoup


def scrape(http_response):
    bsoup = BeautifulSoup(http_response.text, "html.parser")
    image_tags = bsoup.find_all("img")
    urls = [img["src"] for img in image_tags]
    img = urls[0].split("/")[-1]
    for url in urls:
        filename = re.search(r"/([\w_-]+[.](jpg|gif|png))$", url)
        with open(filename.group(1), "wb") as f:
            if "http" not in url:
                url = "{}{}".format(url_path, url)
            http_response = requests.get(url)
            f.write(http_response.content)
    return img


if __name__ == "__main__":
    nasa_url = "https://apod.nasa.gov/apod/astropix.html"
    url_path = nasa_url.replace("astropix.html", "")
    http_response = requests.get(nasa_url)
    img = scrape(http_response)
    img_loc = os.path.join(os.getcwd() + "/" + img)
    # comment the 2 lines below if you want to use this in linux
    img_loc = img_loc.replace("/mnt/c", "C:")
    img_loc = img_loc.replace("/", "\\")
    webbrowser.open(img_loc)
