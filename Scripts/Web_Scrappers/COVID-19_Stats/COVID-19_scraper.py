import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def makeTable(table,headers,tablefmt):
    return tabulate(table,headers=headers,tablefmt=tablefmt)


def statsFind():
    name= input("\n\n *->Enter country/state name : ").strip().lower()
    if name=="0":
        pass
    else:
        try:
            print("\nwait a sec....\n")
            url = "https://www.bing.com/search?q=covid+stats+"+name.replace(" ","+")
            header = {'User-Agent': "Chrome/6.0.472.63 Safari/534.3"}
            source = requests.get(url, headers=header)
            soup = BeautifulSoup(source.content, "lxml")
            for i in range(1,4,1):
                nameFound= soup.select_one("#b_context > li:nth-child(1) > div > div.b_tophbb.bgtopgr.bgbtopnone > div > div.covid-modList > div:nth-child({}) > div.cov_modHead > div:nth-child(1)".format(i)).text
                if nameFound=="Global cases":
                    break
                update= soup.select_one("div:nth-child({}) > div.cov_modHead > div:nth-child(2)".format(i)).text
                name= nameFound.replace(" cases","")
                ttlCase = soup.select_one("div:nth-child({}) > div:nth-child(2) > div > div.cov_cases > div:nth-child(1) > div.c_row > div:nth-child(1)".format(i)).text
                ttlDeaths = soup.select_one("div:nth-child({}) > div:nth-child(2) > div > div.cov_cases > div:nth-child(2) > div.c_row > div:nth-child(1)".format(i)).text
                ttlRecovered = soup.select_one("div:nth-child({}) > div:nth-child(2) > div > div.cov_cases > div:nth-child(3) > div.c_row > div:nth-child(1)".format(i)).text
                table=[["Country/State"," : ",name.upper(), "     ({})".format(update)], ["Total Cases"," : ",ttlCase], ["Total Deaths"," : ",ttlDeaths], ["Recovered"," : ",ttlRecovered], [], []]
                print(makeTable(table,[],"plain"))
            print("Enter 0 to terminate")
            statsFind()
        except:
            print("No country/state on list with this name, please try again or search another country/state")
            statsFind()


print("\ngetting info....\n")
url="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
header = {'User-Agent': "Chrome/6.0.472.63 Safari/534.3"}
source=requests.get(url, headers=header)
soup=BeautifulSoup(source.content, "lxml")

ttlCase= soup.select_one("tr.sorttop > th:nth-child(3)").text
ttlDeaths= soup.select_one("tr.sorttop > th:nth-child(4)").text
ttlRecovered= soup.select_one("tr.sorttop > th:nth-child(5)").text

table=[["Total cases"," : ", ttlCase], ["Total deaths"," : ", ttlDeaths], ["Total people recovered"," : ",ttlRecovered]]

print('''\n        WORLD COVID-19 stats
       ----------------------\n''')
print(makeTable(table,[],"plain")+"\n\n")

print("         Top 10 countries suffering form COVID-19")
top10=[]
header= ["Rank", "Country\nName", "Total\nCases", "Total\nDeaths", "Total\nRecovered"]
for i in range(3,13,1):
    country= soup.select_one(" tr:nth-child({}) > th:nth-child(2) > a".format(i)).text
    ttlCase= soup.select_one("tr:nth-child({}) > td:nth-child(3)".format(i)).text
    ttlDeaths = soup.select_one("tr:nth-child({}) > td:nth-child(4)".format(i)).text
    ttlRecovered = soup.select_one(" tr:nth-child({}) > td:nth-child(5)".format(i)).text
    top10.append([i-2,country,ttlCase,ttlDeaths,ttlRecovered])

print(makeTable(top10,header,"grid"))

statsFind()
print("\n\n"+makeTable("Thanks . for . using . my . COVID-19 . scraper".split(),[],"plain"))
