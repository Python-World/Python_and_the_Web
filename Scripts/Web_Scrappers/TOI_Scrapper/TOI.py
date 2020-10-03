import requests as req
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

def scrapper(category):
    res = req.get("https://timesofindia.indiatimes.com/topic/" +category+"/news").text
    data = bs(res,'html.parser')
    news = data.find_all(class_="article")
    df=[['Title','Link']]
    for i in range(0,len(news)):
        df.append([news[i].find(class_="title").text.strip('\n'),"https://timesofindia.indiatimes.com"+news[i].a['href']])
    df = pd.DataFrame(df)
    scrap = df.to_string()
    np.savetxt('TOI.txt',df.values,'%s')
    
if __name__ == "__main__":
    category = input().strip()
    scrapper(category)
    print("Times Of India Articles Scrapped")