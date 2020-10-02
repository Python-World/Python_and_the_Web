#This program prints the latest news headlines.

import requests
import json
from bs4 import BeautifulSoup

api_key = "a38d9a5560114809bad1ba8be8df849c"
#The news is fetched from the below API
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey='+api_key)


head = requests.get(url)

headline = head.json()


final = headline['articles']
length = len(final)



for i in range(length):
       print('..........................................')
       print(final[i]['title'])