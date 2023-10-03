import re

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
r = rq.get("https://www.thecricketmonthly.com/", headers=header)
soup = BeautifulSoup(r.content, "html.parser")
main_sec = soup.find(
    "section", attrs={"class": re.compile("col-lhs lhs_content")}
)
article = main_sec.find_all(
    "article", attrs={"class": re.compile("col-1-1 module")}
)
about = []
link = []
summary = []
print("Fetching Latest Articles...")
for a in article:
    tag = a.find("h1")
    about.append(tag.text)
    link.append("https://www.thecricketmonthly.com" + tag.a["href"])
    tag = a.find("p")
    summary.append(tag.text)
print("Done!")

main_sec = soup.find("ul", attrs={"class": re.compile("writer-ul")})
li = main_sec.find_all("li")
linkauth = []
auth = []
headline = []
subhead = []
print("Fetching articles of top Writers...")
for l in li:
    linkauth.append(l.a["href"])
    spn = l.find("span", attrs={"class": re.compile("wname")})
    auth.append(spn.text)
    headline.append(l.a.text)
    spn = l.find("span", attrs={"class": re.compile("subheadline")})
    subhead.append(spn.text)
print("Done!")

print("Processing Data...")
la = {"About": about, "Short Summary": summary, "Further Reading": link}
tw = {
    "Writer": auth,
    "Headline": headline,
    "Sub-headline": subhead,
    "Further Reading": linkauth,
}
latest_articles = pd.DataFrame.from_dict(la)
top_writers = pd.DataFrame.from_dict(tw)
print("Publishing csv...")
top_writers.to_csv("Articles from Top Writers.csv", index=False)
latest_articles.to_csv("Latest Articles from Cricket Monthly.csv", index=False)
print(
    "Your output can be found in form of two files 'Articles from Top Writers.csv' and 'Latest Articles from Cricket Monthly.csv'"
)
