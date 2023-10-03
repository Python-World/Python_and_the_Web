import json

import bs4
import requests
from tqdm import tqdm

BASE_URL = "https://projecteuler.net/archives;page="
N_PAGES = 15
data = {}

ids = []
problems = []

for n in tqdm(range(1, N_PAGES + 1)):
    page = requests.get(BASE_URL + str(n)).content

    src = bs4.BeautifulSoup(page, "html.parser")

    # get outermost container
    main_div = src.find("div", id="content").find(
        "div", id="problems_table_page"
    )

    # get table including problems
    table = main_div.find("table", id="problems_table")

    # get all table data
    td = table.findAll("td")

    # extract problem number and text
    ids.extend([str(i.text) for i in td if i.has_attr("class")])
    problems.extend([str(i.find("a").text) for i in td if i.find("a")])

data = dict(zip(ids, problems))

# dump into json file
with open("Project Euler problem statements.json", "w") as f:
    json.dump(data, f)
print("Data dumped")
