from datetime import datetime, timedelta
import requests
import yfinance
import pandas as pd
from bs4 import BeautifulSoup


WIKI_ENDPOINT = "https://en.wikipedia.org/w/api.php"

def fetch_ticker_names():
    params = {
        "action" : "parse",
        "format" : "json",
        "page" : "List of S&P 500 companies",
        "prop" : "text",
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
    return yfinance.download(symbol, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    tickers = fetch_ticker_names()
    data = pd.DataFrame()
    for symbol, company in tickers:
        data = fetch_daily_data_for_ticker(symbol)
        data.to_csv(f"{symbol}.csv")