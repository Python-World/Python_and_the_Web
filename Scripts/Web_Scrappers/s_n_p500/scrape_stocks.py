import requests
import pprint
from bs4 import BeautifulSoup


english_wiki_endpoint = "https://en.wikipedia.org/w/api.php"

params = {
    "action" : "parse",
    "format" : "json",
    "page" : "List of S&P 500 companies",
    "prop" : "text",
}

response = requests.get(english_wiki_endpoint, params=params)
soup = BeautifulSoup(response.content, "lxml")
symbols = set()
for item in soup.find_all("tr")[:501]:
    cells = item.find_all("td")[:2]
    try:
        symbol, company = cells[0].a.text, cells[1].a.text
    except:
        continue
    tupl = (symbol, company)
    symbols.add(tupl) 


for tupl in sorted(symbols, key=lambda x:x[1]):
    print(tupl)
print(len(symbols))