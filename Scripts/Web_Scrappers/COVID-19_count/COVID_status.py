import requests
from bs4 import BeautifulSoup


def scrape_data():
    # scraping the data using requests and BeautifulSoup modules
    response = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


scrapedData = scrape_data()


def headers():
    # getting the headers from the scrape_data() function
    heading = scrapedData.find("thead").get_text()
    return heading.split("\n")


def total_cases():
    # getting only total cases, total newCases, totaldeath, new deaths and total recoverd.
    # Displaying the data in a list format.
    data = scrapedData.find(class_="total_row_body").get_text()
    keys = headers()
    value = data.split("\n")
    return [(f"{k}:{v}") for k, v in dict(zip(keys, value)).items()][3:10]


def all_countries_status():
    # getting the data of all the individual countries.
    # Displaying the data in list of dictionary format.
    countries_data = scrapedData.find(
        id="main_table_countries_today").tbody.find_all("tr")
    values = [d.get_text().split("\n")[1:9] for d in countries_data]
    keys = headers()[2:9]
    return [(dict(zip(keys, i))) for i in values][8:]


def status_based_on_countries():
    # Displays the data of a cuntry, after the user enters the name.
    country_name = input("enter country name: ").lower()
    for i in all_countries_status():
        if i["Country,Other"].lower() == country_name:
            return i


print(total_cases())
for i in all_countries_status():
    print(i)
print(status_based_on_countries())
