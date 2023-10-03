import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from yaspin import yaspin

language = "python"
URL = "https://summerofcode.withgoogle.com/organizations/"
organization_list = []


class Organization:
    def __init__(self, name, irc, org_page, tech_stack, count):
        self.name = name
        self.irc = irc
        self.org_page = org_page
        self.tech_stack = tech_stack
        self.count = count

    def __str__(self):
        return self.name + "count= " + str(self.count)

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count


def language_filter(tech_stack_list):
    for tech_stack in tech_stack_list:
        if language in tech_stack:
            return True
    return False


def check_previous():
    for year in range(2016, 2020):
        archive_url = (
            "https://summerofcode.withgoogle.com/archive/"
            + str(year)
            + "/organizations/"
        )

        response = requests.get(archive_url)
        soup = BeautifulSoup(response.content, "html.parser")
        orgs = soup.find_all("li", {"class": "organization-card__container"})

        for org in orgs:
            name = org["aria-label"]
            for organization in organization_list:
                if organization.name.strip() == name.strip():
                    organization.count += 1
                    # link = org.find("a",{"class":"organization-card__link"})["href"].split('/')[-2]
                    # print(archive_url + str(link))


def print_list():
    table = Table(title="G-soc orgs")
    table.add_column("S.No", justify="right", style="cyan")
    table.add_column("Org-name", style="magenta")
    table.add_column("Count", style="white")
    table.add_column("IRC", style="red", width=20)
    table.add_column("Org Link", style="blue", width=20)
    table.add_column("Tech stack", justify="right", style="green")
    index = 1
    for organization in sorted(organization_list, reverse=True):
        tech = ""
        for t in organization.tech_stack:
            tech = tech + " " + t
        table.add_row(
            str(index),
            str(organization.name),
            str(organization.count),
            str(organization.irc),
            str(organization.org_page),
            str(tech),
        )
        index += 1
    Console().print(table)
    x = 1
    while x != -1:
        x = int(
            input(
                "Enter the index no. for getting complete links(-1 to quit): "
            )
        )
        if x == -1:
            continue
        org_x = sorted(organization_list, reverse=True)[x - 1]
        try:
            print("Name: " + org_x.name)
            print("IRC: " + org_x.irc)
            print("Organisation Link: " + org_x.org_page)
            print("Tech Stack: " + (" ").join(org_x.tech_stack))
            print("Count: " + str(org_x.count))
            print("===========================================\n")
        except:
            print(
                "Organisation is missing some value. Kindly check on GSoc Website"
            )


headers = {
    "authority": "summerofcode.withgoogle.com",
    "accept": "application/json, text/plain, */*",
    "x-content-type-options": "nosniff",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://summerofcode.withgoogle.com/organizations/",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}
page_no = 1
org_index = 1
language = str(input("Enter the language you want to filter out: "))

try:
    with yaspin(text="Loading current orgs", color="yellow") as spinner:
        while True:
            params = (
                ("page", str(page_no)),
                ("page_size", "48"),
            )
            page_no += 1

            response = requests.get(
                "https://summerofcode.withgoogle.com/api/program/current/organization/",
                headers=headers,
                params=params,
            )
            json_data = None

            json_data = response.json()

            for index in range(len(json_data["results"])):
                if language_filter(
                    json_data["results"][index]["technology_tags"]
                ):
                    name = json_data["results"][index]["name"]
                    tech_stack = json_data["results"][index]["technology_tags"]
                    irc = json_data["results"][index]["irc_channel"]
                    org_page = URL + str(json_data["results"][index]["id"])
                    count = 1
                    current_org = Organization(
                        name, irc, org_page, tech_stack, count
                    )
                    organization_list.append(current_org)

            if json_data["results"] == []:
                break

    spinner.ok("✅ ")
    with yaspin(
        text="Counting previous year selection", color="yellow"
    ) as spinner:
        check_previous()
    spinner.ok("✅ ")
    print_list()

except Exception as e:
    print(e)

finally:
    print("Script ran successfully!")
