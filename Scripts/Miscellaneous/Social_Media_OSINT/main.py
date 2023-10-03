import re

import requests
from bs4 import BeautifulSoup


# Define Colors
class colors:
    GREEN = "\033[92m"
    STOP = "\033[0m"
    RED = "\033[31m"


class CheckUsername:
    def __init__(self, username):
        self.username = username
        self.check_profile()

    # search for all the links with the username provided. If it returns a 404, then the username is not available else it is available
    def check_profile(self):
        links = ["instagram", "facebook", "github"]
        for link in links:
            if link == links[1]:
                temp_url = f"https://{link}.com/{self.username.rstrip('_')}"
            else:
                temp_url = f"https://{link}.com/{self.username}"
            response = requests.get(temp_url)
            soup = BeautifulSoup(response.content, "lxml")
            if response.status_code == 404 or soup.findAll(
                text=re.compile("Sorry, this page isn't available.")
            ):
                print(
                    colors.RED
                    + "\u2716"
                    + f"{link.capitalize()} account not found!"
                    + colors.STOP
                )
            else:
                print(
                    colors.GREEN
                    + "\u2713"
                    + f"{link.capitalize()} account found!"
                    + colors.STOP
                )


def main():
    username = input("Enter the username: ")
    CheckUsername(username)


if __name__ == "__main__":
    main()
