from datetime import datetime, timedelta
from pathlib import Path
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
    # first 500 cells which are the S&P500
    for item in soup.find_all("tr")[:501]:
        # first cell is symbol, second is company name
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

def save_to_drive(filename, dataframe):
    out_file = f"{filename}.csv"
    out_dir = Path("CSVs")
    out_dir.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(out_dir / out_file)

if __name__ == "__main__":
    tickers = fetch_ticker_names()
    with open("available_tickers.txt", "w") as ticker_f:
        for symbol, name in tickers:
            ticker_f.write(f"{symbol}, {name}\n")
    if input(">>> Save to drive: ").lower() in ("y", "yes"):
        for symbol, _ in tickers:
            data = fetch_daily_data_for_ticker(symbol)
            save_to_drive(symbol, data)