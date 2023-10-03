# Author : @Rajdeep-Ray

import csv
import json

import requests
from bs4 import BeautifulSoup

c = 0
total = 0
myList = []

for s in range(1, 8):
    s = str(s)

    # Using get() method to Open the URL
    URL = str("https://www.rocketlaunch.live/?page=" + s)
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, "html.parser")
    soup.find("div", id="upcoming_launches_header").decompose()
    f = soup.find_all("h4")
    f1 = soup.find_all("div", {"class": "launch_date rlt_date"})
    f2 = soup.find_all("div", {"class": "rlt-provider"})
    f3 = soup.find_all("div", {"class": "rlt-location"})

    for j in range(1, len(f), 2):
        total += 1
        myData = {}

        # get vehicle type
        myData["vehicle"] = f[j].a.text

        # get mission name
        myData["mission"] = f[j - 1].a.text

        print("Vehicle :", f[j].a.text)
        print("Mission :", f[j - 1].a.text)

        if c < len(f1):
            # get lauch date
            myData["launch"] = f1[c].a.text

            # get provider/org name
            myData["provider"] = f2[c].a.text

            # get launch location
            myData["location"] = f3[c].text.strip().replace("\n", ", ")

            print("Launch Date :", f1[c].a.text)
            print("Provider :", f2[c].a.text)
            print("Location :", f3[c].text.strip().replace("\n", ", "))
            print("Data :", myData)

        else:
            c = 0

        myList.append(myData)
        print()
        c += 1

# Prints the total number of results
print("Total Results :", total)


# Create json file
with open("Scripts/Web_Scrappers/Rocket-Schedule/result.json", "w") as outfile:
    json.dump(myList, outfile)
print("JSON File created!")


# Create csv file
resultFile = open("Scripts/Web_Scrappers/Rocket-Schedule/Result-file.csv", "w")

# create the csv writer object
csv_writer = csv.writer(resultFile)

isHeader = False
for emp in myList:
    if not isHeader:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        isHeader = True

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

resultFile.close()
print("CSV File created!")
