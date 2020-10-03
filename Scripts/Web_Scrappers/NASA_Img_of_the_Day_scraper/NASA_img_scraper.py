import re
import requests
import os
from bs4 import BeautifulSoup
import webbrowser

nasa_url = "https://apod.nasa.gov/apod/astropix.html"
url_path = nasa_url.replace("astropix.html","")

http_response = requests.get(nasa_url)

bsoup = BeautifulSoup(http_response.text, 'html.parser')
image_tags = bsoup.find_all('img')
urls = [img['src'] for img in image_tags]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(url_path, url)
        http_response = requests.get(url)
        f.write(http_response.content)
img_loc = os.path.join(os.getcwd() +'/'+ url.split('/')[-1])

#comment the 2 lines below if you want to use this in linux
img_loc = img_loc.replace('/mnt/c', 'C:')
img_loc = img_loc.replace('/', '\\')
webbrowser.open(img_loc)