# Web Scraping COVID-19 Data for Top 10 Countries Affected (Issue #31)
# https://github.com/Python-World/Python_and_the_Web/issues/31
# Contributed by @tauseefmohammed2 : https://github.com/tauseefmohammed2

# Requirements : 
# Selenium (Web Scrapping Python Library. Install : pip install selenium)
# ChromeDriver (Used for Automated Navigation to URLs, which are Provided by Selenium as Input. Download : https://chromedriver.chromium.org/downloads)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime, time, os

td = datetime.date.today()
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-minimized')

# Creating WebDriver Object
wd = webdriver.Chrome(r'C:\\Users\\TEMP\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe',options=CO)
# Replace the Above Location of chromedriver.exe with your Saved Location 

print ("Date:",td.strftime("%b-%d-%Y"))
print ("--------------------------------------------------------------------------------------------")
print ("               COVID-19 Statistics From Around the World (Top 10 Countries)                 ")
print ("--------------------------------------------------------------------------------------------")

# Using get() method to Open a URL (WHO)
wd.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
wd.implicitly_wait(wait_imp)
w_total = wd.find_element_by_id("confirmedCases")
w_death = wd.find_element_by_id("confirmedDeaths")
total_c = wd.find_element_by_id("involvedCountries")
print("WorldWide")
print("Total Cases : ", w_total.text)
print("Total Deaths : ", w_death.text)
print("-------------------------------------------------------")

# Using get() method to Open a URL (Worldometers)
wd.get("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
country_list = []
cases_list = []
deaths_list = []
continent_list = []
table =  wd.find_element_by_id("table3")
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
    if count < 11 :
        print("Country : ", lst[0])
        print("Total Cases : ", lst[1])
        print("Total Deaths : ", lst[2])
        print("-------------------------------------------------------")
    count += 1