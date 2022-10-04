# Developed By Parth Maniar
# https://github.com/officialpm

# import libs

import os
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if not os.path.exists("problems"):  # create problems folder if not exists
    os.makedirs("problems")

options = webdriver.ChromeOptions()
options.add_argument("headless")  # headless chrome option


def scrapeCodeChef(code):
    try:
        url = f"https://www.codechef.com/problems/{code}"
        browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=options
        )  # install and open chrome driver
        print("[OPENING] - ", code)
        browser.get(url)  # open CodeChef Problem  URL
        print("[SCRAPING] - ", code)
        soup = BeautifulSoup(
            browser.page_source, features="html.parser"
        )  # parse page source
        head = soup.find_all(["h1"])  # find all h1 tags
        body = soup.find_all(
            ["p", "h3", "ul", "pre"]
        )  # find all p, h3, ul, pre tags
        with open("problems/" + url[34:] + ".txt", "a") as f:  # open .txt file
            f.write(head[1].text[:-7] + "\n")  # write title
            for i in range(8, len(body) - 18):
                f.write(body[i].text + "\n")  # write body
        print(f"[FINISHED] - File saved - problems/{code}.txt")
    except Exception:
        print("Cannot Find CodeChef Problem! - " + code)
        sys.exit(0)


if __name__ == "__main__":
    try:
        code = sys.argv[1]
    except Exception:
        print(
            "Please Enter A CodeChef Problem Code as a",
            "Command-Line Argument!",
        )
        sys.exit(0)
    scrapeCodeChef(code)
