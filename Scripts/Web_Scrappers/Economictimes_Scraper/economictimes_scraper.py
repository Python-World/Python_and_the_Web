import datetime
import json
import sys

import lxml
import requests
from bs4 import BeautifulSoup


# Util
def datestr_to_date(datestr):
    [year, month, day] = datestr.split("-")
    return datetime.date(year=int(year), month=int(month), day=int(day))


# Reference dates
reference_date = datetime.date(2001, 1, 1)  # 2001 Jan 1
reference_date_id = 36892

if len(sys.argv) < 3:
    print("economictimes_scraper.py START_DATE END_DATE\nDate fmt: YYYY-MM-DD")
    sys.exit(1)

start_date = datestr_to_date(sys.argv[1])
end_date = datestr_to_date(sys.argv[2])
start_dateid = reference_date_id + (start_date - reference_date).days
end_dateid = reference_date_id + (end_date - reference_date).days

if (start_date - reference_date).days < 0:
    print("Error: Start date should be > than 2001-01-01")
    sys.exit(1)
if (end_date - start_date).days < 0:
    print("Error: End date should be > than Start date")
    sys.exit(1)


# Gets News article metadata from article url
def fetchNewsArticle(url):
    html = requests.get(url).content
    root = lxml.HTML(html)
    x = root.xpath("/html/body//script[@type='application/ld+json']")
    metadata = None  ## When Article does not exists (404)
    if len(x) >= 2:
        metadata = x[1].text
    return metadata


et_host = "https://economictimes.indiatimes.com"
et_date_url = "https://economictimes.indiatimes.com/archivelist/starttime-"
et_date_extension = ".cms"

fetched_data = {}

for dateid in range(start_dateid, end_dateid + 1):
    date = str(
        reference_date + datetime.timedelta(days=dateid - reference_date_id)
    )
    html = requests.get(
        "{}{}{}".format(et_date_url, dateid, et_date_extension)
    ).content
    soup = BeautifulSoup(html, "html.parser")
    fetched_data[date] = []
    for x in soup.select("#pageContent table li a"):
        print(x.text)
        article_metadata = fetchNewsArticle(et_host + x["href"])
        fetched_data[date].append(
            {
                "metadata": article_metadata,
                "title": x.text,
                "url": et_host + x["href"],
            }
        )

out_filename = "ET_NewsData_{}_{}.json".format(start_date, end_date)
with open(out_filename, "w+") as output_file:
    output_file.write(json.dumps(fetched_data, indent=2))
