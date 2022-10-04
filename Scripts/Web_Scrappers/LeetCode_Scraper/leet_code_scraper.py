# Author: Mahesh Bharadwaj K (https://github.com/MaheshBharadwaj)

import re
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from textwrap3 import wrap
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("headless")  # headless chrome option


class InvalidCodeException(Exception):
    """
    Invalid problem code
    """


def parse_problem_statement(problem_code: str):
    """
    This function takes a Leet Code problem code as input and
    scrapes the problem statement from the site and returns
    the parsed problem statement as a text file.

    PARAMETERS:
    -----------
        problem_code: string
            LeetCode problem code

    RETURNS:
    --------
        problem_div.text: string
            Extracted problem statement as string after removing HTML tags
    """
    URL = f"https://leetcode.com/problems/{problem_code}"
    browser = webdriver.Chrome(
        ChromeDriverManager().install(), options=options
    )  # install and open chrome driver
    browser.get(URL)
    print("[SCRAPING] - ", problem_code)
    soup = BeautifulSoup(
        browser.page_source, features="html.parser"
    )  # parse page source

    # If invalid program code, 404 page is displayed
    if soup.find("div", class_="display-404"):
        raise InvalidCodeException

    # Problem statement div
    problem_div = soup.find(
        "div", class_=re.compile(r"content\w+ question-content\w+")
    )
    return problem_div.text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Invalid Usage!\nRun: python3 leet_code_scraper.py [problem code]",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        problem_code = sys.argv[1]
        parsed_problem = parse_problem_statement(problem_code)

        with open(problem_code + ".txt", "wt") as fout:
            parsed_lines = parsed_problem.split("\n")
            for line in parsed_lines:
                if len(line) < 81:
                    print(line, file=fout)
                else:
                    wrapped_lines = wrap(
                        line, width=80
                    )  # Splitting long line into multiple lines
                    for l in wrapped_lines:
                        print(l, file=fout)

        print(
            f"Successfully scraped {problem_code} and saved as {problem_code}.py!"
        )

    except InvalidCodeException:
        print("Invalid Problem Code! Please check the problem code provided!")

    except Exception as e:
        print("Fatal: \n" + str(e))
