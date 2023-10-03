import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

LEAGUE_CODE = {
    "BSA": {"code": 2013, "name": "Brazilian First Division"},
    "BL": {"code": 2002, "name": "Bundesliga"},  # Bundesliga
    "ECL": {
        "code": 2016,
        "name": "English Championship",
    },  # English Championship
    "ERD": {"code": 2003, "name": "Eredivisie"},  # Eredivisie [Dutch]
    "L1": {"code": 2015, "name": "Ligue 1"},  # Ligue 1
    "SPA": {"code": 2014, "name": "La Liga"},  # La Liga
    "PPL": {
        "code": 2017,
        "name": "Portugese first division",
    },  # Portugese First Dvision
    "PL": {"code": 2021, "name": "Premier League"},  # Premier League
    "SA": {"code": 2019, "name": "Serie A"},  # Serie A
}

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.football-data.org/v2/"
HEADER = {"X-Auth-Token": str(API_KEY)}


def print_standings(league_id):
    league_code = league_id.get("code")
    resource = f"competitions/{league_code}/standings"
    api_url = API_URL + resource
    r = requests.get(api_url, headers=HEADER)
    obj = r.json()

    str_re = (
        "\nLEAGUE: "
        + str(obj["competition"]["name"])
        + " " * (75 - 2 - 8 - 10 - len(str(obj["competition"]["name"])))
        + "MATCHDAY: "
        + str(obj["season"]["currentMatchday"])
        + "\n"
    )
    str_re += "╔════╤════════════════════════════════════╤════╤════╤════╤════╤═════╤═════╗\n"
    str_re += "║ SN │                TEAM                │ M  │ W  │ D  │ L  │ PTS │ GD  ║\n"
    str_re += "╠════╪════════════════════════════════════╪════╪════╪════╪════╪═════╪═════╣\n"
    for team in obj["standings"][0]["table"]:
        text = (
            "║ %-2d │ %-34s │ %-2d │ %-2d │ %-2d │ %-2d │ %-3d │ %+-3d ║\n"
            % (
                team["position"],
                team["team"]["name"][:34],
                team["playedGames"],
                team["won"],
                team["draw"],
                team["lost"],
                team["points"],
                team["goalDifference"],
            )
        )

        str_re += text

    str_re += "╚════╧════════════════════════════════════╧════╧════╧════╧════╧═════╧═════╝"

    print(str_re)


if __name__ == "__main__":
    try:
        # If API key is not stored
        if API_KEY is None or API_KEY == "YOUR_KEY_HERE":
            print(
                'This script requires a free API key from https://www.football-data.org/ for stats!\
                \nGet a free API Key and store it in the .env file in place of "YOUR_KEY_HERE"'
            )
            sys.exit(1)

        arg = sys.argv[1]

        if arg in ["--help", "-h"]:
            print("List of leagues and the codes: ")
            for sno, key in enumerate(LEAGUE_CODE.keys()):
                print(
                    "%2d. %-30s %s" % (sno + 1, LEAGUE_CODE[key]["name"], key)
                )
            sys.exit(0)

        league_id = LEAGUE_CODE.get(arg)
        if league_id is None:
            print(
                "Invalid League Code!\nrun: python3 main.py --help | -h to get list of league codes"
            )

        print_standings(league_id)

    # When no arguments are passed to the script
    except IndexError:
        print(
            "Invalid Usage!\nrun: python3 main.py [league-code]\
            \nrun: python3 main.py --help | -h to get list of league codes"
        )
