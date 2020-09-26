import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def scrape_tablerows():
    """This function scrapes the tablerows related to our target elements.
       Our target element here are the events of hactoberfest.

    Returns:
        tablerows[list]: A list of tablerows of our taget elements.
    """
    hacktoberfest_events_url = "https://hacktoberfest.digitalocean.com/events"
    response = requests.get(hacktoberfest_events_url)
    soup = bs(response.content, 'html.parser')
    mydivs = soup.findAll("tbody", {"class": "list"})
    tablerows = mydivs[0].findAll("tr")
    return tablerows


def hacktoberfest_events(tablerows):
    """This function takes the list of tablerows as input and performs
       scraping of required elements as well as stores the scraped data
       into a csv file.

    Args:
        tablerows (list): Lis of tablerows of the target elements.
    """
    events = {}
    for i, tablerow in enumerate(tablerows):
        location = tablerow.find("td", {"class": "location"}).text
        link = tablerow.find("a")['href']
        name = tablerow.find("td", {"class": "event_name"}).text.strip()
        date = tablerow.find("td", {"class": "date is-hidden"}).text.strip()
        events[i] = [name, date, location, link]
    df1 = pd.DataFrame.from_dict(events, orient='index')
    df1.columns = ['Name', 'Date', 'Location', 'Link']
    df1.to_csv('hacktoberfest_events.csv')


if __name__ == "__main__":
    tablerows = scrape_tablerows()
    hacktoberfest_events(tablerows)
    print("The events have been stored successfully")
