import requests
from bs4 import BeautifulSoup

# Constants like the contest page link and contest data headers
CONTEST_PAGE = "https://www.codechef.com/contests/"
HEADERS = ["CODE", "NAME", "START", "END"]

# Get the output file name
OUTPUT_FILE = input("Please specify the output filename (.txt or .csv): ")
print(f"Scraping {CONTEST_PAGE}...")

# Get the contest page's source and pass it to BeautifulSoup
response = requests.get(CONTEST_PAGE)
soup = BeautifulSoup(response.content, "html.parser")

# Locate the tables for 'Present' and 'Future' contests
contest_tables = soup.find_all("table", class_="dataTable")[0:-1]

# Scrape the data from inside the tables like contest code, name,
# start and end date
contest_data = []
for table in contest_tables:
    contests = []
    for contest in table.tbody.find_all("tr"):
        row_elems = contest.find_all("td")
        contests.append([elem.get_text().strip() for elem in row_elems])
    contest_data.append(contests)

print(f"Writing data to {OUTPUT_FILE}...")
# Write the scraped data to the specified output file as a CSV
with open(OUTPUT_FILE, "w+") as csv:
    csv.write("CodeChef Contests (Present and Upcoming)\n")
    for contest_type, contests in zip(
        ["Current Contests", "Future Contests"], contest_data
    ):
        csv.write("\n")
        csv.write(contest_type + "\n")
        csv.write(", ".join(HEADERS) + "\n")
        for contest in contests:
            csv.write(", ".join(contest) + "\n")
