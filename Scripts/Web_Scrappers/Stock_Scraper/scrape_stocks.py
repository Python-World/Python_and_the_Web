import os
import sys
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path

import requests
import yfinance
from bs4 import BeautifulSoup

WIKI_ENDPOINT = "https://en.wikipedia.org/w/api.php"


@contextmanager
def suppress_console():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def fetch_ticker_names():
    params = {
        "action": "parse",
        "format": "json",
        "page": "List of S&P 500 companies",
        "prop": "text",
    }
    response = requests.get(WIKI_ENDPOINT, params=params)
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
    return list(symbols)


def fetch_daily_data_for_ticker(symbol):
    end_date = datetime.today()
    start_date = end_date - timedelta(weeks=12)
    return yfinance.download(
        symbol, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    )


if __name__ == "__main__":
    tickers = fetch_ticker_names()
    if input(">>> Save Data to Drive? ").lower() in ["y", "yes"]:
        Path("CSVs").mkdir(parents=True, exist_ok=True)
        for i, (symbol, company) in enumerate(tickers, start=1):
            with suppress_console():
                data = fetch_daily_data_for_ticker(symbol)
                data.to_csv(f"CSVs\\{symbol}.csv")
            print(f"File#{i} saved", end="\r")
        print("\nFiles scraped and downloaded!")
