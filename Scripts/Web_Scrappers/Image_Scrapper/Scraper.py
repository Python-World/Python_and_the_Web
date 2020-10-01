import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import os

url="https://www.creativeshrimp.com/top-30-artworks-of-beeple.html"

source_code=requests.get(url)

plain_text=source_code.text

soup=BeautifulSoup(plain_text)


for link in soup.find_all("a",{"class":"lightbox"}):
    href=link.get('href')
    print(href)
    
    img_name=random.randrange(1,500)
    
    full_name=str(img_name)+".jpg"
    
    urllib.request.urlretrieve(href,full_name)
    print("Loop Break")
