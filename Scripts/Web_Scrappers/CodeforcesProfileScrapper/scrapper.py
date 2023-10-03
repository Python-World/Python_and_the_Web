import sys
from datetime import datetime

import requests


class UserNotFoundError(Exception):
    pass


def user_info(handles):
    if type(handles) is str:
        handles = [handles]
    url = "https://codeforces.com/api/user.info"
    params = {"handles": ";".join(handles)}
    with requests.get(url=url, params=params) as r:
        d = r.json()
        if d["status"] == "OK":
            return d["result"]
        raise UserNotFoundError(d["comment"])


def main():
    if len(sys.argv) > 1:
        handles = sys.argv[1:]
    else:
        handles = input("[+] Handles (space-separated): ").split()

    for user in user_info(handles):
        print("-" * 50)
        for key in [
            "handle",
            "rating",
            "rank",
            "maxRating",
            "maxRank",
            "contribution",
            "friendOfCount",
        ]:
            print(f"[*] {key:23}: {user[key]}")
        print(
            f"[*] lastOnlineTimeSeconds  : {datetime.utcfromtimestamp(int(user['lastOnlineTimeSeconds']))}"
        )
        print(
            f"[*] registrationTimeSeconds: {datetime.utcfromtimestamp(int(user['registrationTimeSeconds']))}"
        )


if __name__ == "__main__":
    main()
