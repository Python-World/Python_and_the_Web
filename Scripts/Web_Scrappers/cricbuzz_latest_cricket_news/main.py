import re
import time

import requests as rq
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
print("Fetching Request")
r = rq.get("https://www.cricbuzz.com/cricket-news", headers=header)
time.sleep(1)
print("Parsing the page")
soup = BeautifulSoup(r.content, "html.parser")
main_div = soup.find_all(
    "div",
    attrs={"class": re.compile("cb-col cb-col-100 cb-lst-itm cb-lst-itm-lg")},
)
links = []
intro = []
time = []
typ = []
heading = []
print("Processing News")
for s in main_div:
    links.append("https://www.cricbuzz.com" + s.a["href"])
    s1 = s.find("div", attrs={"class": re.compile("cb-nws-intr")})
    intro.append(s1.text)
    s2 = s.find("div", attrs={"class": re.compile("cb-nws-time")})
    typ.append(s2.text)
    s3 = s.find("span", attrs={"class": re.compile("cb-nws-time")})
    time.append(s3.text)
    s4 = s.find(
        "h2", attrs={"class": re.compile("cb-nws-hdln cb-font-18 line-ht24")}
    )
    heading.append(s4.text)
l = len(heading)
with open("out.txt", "w") as file:
    for i in range(l):
        file.write(typ[i] + "\n")
        file.write(heading[i] + "\n")
        file.write(intro[i] + "\n")
        file.write("Ref: " + links[i] + "\n")
        file.write("Posted: " + time[i] + "\n\n")
file.close()
print("Your News is ready in 'out.txt'")
