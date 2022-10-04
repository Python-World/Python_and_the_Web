# Web Scraping COVID-19 Data for Top 10 Countries Affected (Issue #31)
# https://github.com/Python-World/Python_and_the_Web/issues/31
# Contributed by @tauseefmohammed2 : https://github.com/tauseefmohammed2
# 🔥 Updated by @officialpm : https://github.com/officialpm

# Requirements :
# Selenium (Web Scrapping Python Library. Install : pip install selenium)
# Pandas (Data Manipulation Library. Install : pip install pandas)

import datetime
import sys

import pandas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

wait_imp = 10
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--ignore-certificate-errors")
options.add_argument("--headless")

# Creating WebDriver Object
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def scrapeCovidStats():
    td = datetime.date.today()
    print("Date:", td.strftime("%b-%d-%Y"))
    print(
        "------------------------------------------------------------------------------"
    )
    print(
        "         COVID-19 Statistics From Around the World (Top 10 Countries)         "
    )
    print(
        "------------------------------------------------------------------------------"
    )

    # Using get() method to Open a URL (WHO)
    driver.get(
        "https://www.who.int/emergencies/diseases/novel-coronavirus-2019"
    )
    driver.implicitly_wait(wait_imp)
    w_total = driver.find_element_by_id("confirmedCases")
    w_death = driver.find_element_by_id("confirmedDeaths")
    print("WorldWide")
    print("Total Cases : ", w_total.text)
    print("Total Deaths : ", w_death.text)
    print("-------------------------------------------------------")

    # Using get() method to Open a URL (Worldometers)
    driver.get(
        "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
    )

    # Creating Empty Lists to Store Information which will be Retrieved
    country_list = []
    cases_list = []
    deaths_list = []
    continent_list = []

    table = driver.find_element_by_id("table3")
    count = 0
    for row in table.find_elements_by_xpath(".//tr"):
        if count == 0:
            count += 1
            continue
        lst = [td.text for td in row.find_elements_by_xpath(".//td")]
        country_list.append(lst[0])
        cases_list.append(lst[1])
        deaths_list.append(lst[2])
        continent_list.append(lst[3])
        if count < 11:
            print("Country : ", lst[0])
            print("Total Cases : ", lst[1])
            print("Total Deaths : ", lst[2])
            print("-------------------------------------------------------")
        count += 1

    # Closing Chrome After Extraction of Data
    driver.quit()

    # Creating a DataFrame (2D-Tabular Data Structure) using the Information Collected
    df = pandas.DataFrame(
        data={
            "Country": country_list,
            "Total Cases": cases_list,
            "Total Deaths": deaths_list,
            "Continent": continent_list,
        }
    )

    return df


# Using to_csv() Function which Dumps the Data from the DataFrame to a CSV File
if __name__ == "__main__":
    try:
        scrapedData = scrapeCovidStats()
        scrapedData.to_csv("./data.csv", sep=",", index=False)
    except Exception:
        print("Please check your internet!")
        sys.exit(1)
