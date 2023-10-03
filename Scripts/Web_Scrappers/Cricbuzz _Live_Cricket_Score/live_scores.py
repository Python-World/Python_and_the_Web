import requests
from bs4 import BeautifulSoup


# Method for Scrapping the Cricbuzz and displaying live cricket match scores
def live_score():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }

    # Requesting and storing the contents of desired webpage in "soup" variable
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, "html.parser")

    # Finding all the contents of matches as per the ongoing tournaments
    tournaments = soup.find_all(
        attrs={
            "class": "cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main"
        }
    )

    # If no live matches are going on
    if len(tournaments) == 0:
        print("\n\nNo Live Matches!")

    else:
        for tournament in tournaments:
            print("\n\n", tournament.h2.text)

            # Finding all the matches of a particular tournament
            matches = tournament.find_all(
                attrs={"class": "cb-mtch-lst cb-col cb-col-100 cb-tms-itm"}
            )
            for match in matches:
                # Finding live score of a match and displaying it
                schedule = match.find_all(
                    attrs={"class": "cb-col-100 cb-col cb-schdl"}
                )

                fixtures = (
                    schedule[0].h3.text
                    + schedule[0]
                    .find("span", attrs={"class": "text-gray"})
                    .text
                )
                print("\n\t", fixtures)

                details = schedule[1].find(
                    attrs={"class": "cb-scr-wll-chvrn cb-lv-scrs-col"}
                )
                team1 = details.find(
                    "div", attrs={"class": "cb-hmscg-bat-txt"}
                )
                if team1 is not None:
                    team1_name = team1.find(
                        "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"}
                    ).text
                    team1_score = team1.find(
                        "div",
                        attrs={
                            "class": "cb-ovr-flo",
                            "style": "display:inline-block; width:140px",
                        },
                    ).text
                    print("\t\t", team1_name, team1_score)
                team2 = details.find(
                    "div", attrs={"class": "cb-hmscg-bwl-txt"}
                )
                if team2 is not None:
                    team2_name = team2.find(
                        "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"}
                    ).text
                    team2_score = team2.find(
                        "div",
                        attrs={
                            "class": "cb-ovr-flo",
                            "style": "display:inline-block; width:140px",
                        },
                    ).text
                    print("\t\t", team2_name, team2_score)

                match_status = details.find(
                    "div", attrs={"class": "cb-text-live"}
                )
                if match_status is None:
                    match_status = details.find(
                        "div", attrs={"class": "cb-text-complete"}
                    )
                match_status = match_status.text
                print("\t\t Match Status:", match_status)


if __name__ == "__main__":
    # Scraping the live cricket score and displaying it
    live_score()
