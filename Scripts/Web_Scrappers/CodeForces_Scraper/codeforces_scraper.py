import sys

import requests
from bs4 import BeautifulSoup


def get_problem_statement(problem_code):
    """
    This function takes a Codeforces problem code as input and
    scrapes the problem statement from the site and returns
    the parsed problem statement.

    Args:
        problem_code (string): CodeForces Problem Code
    Returns:
        problem_statement (string): CodeForces Problem
    """
    problem_number = problem_code[:-1]
    problem_letter = problem_code[-1]
    URL = f"https://codeforces.com/problemset/problem/\
        {problem_number}/{problem_letter}"
    try:
        page = requests.get(URL)
        if not page:
            raise Exception(page.status_code)
    except Exception as e:
        print("Cannot Find CodeForces Problem!" + str(e))
        sys.exit(0)
    soup = BeautifulSoup(page.content, "html.parser")
    soup.find("div", class_="header").decompose()
    problem_statement_div = soup.find("div", class_="problem-statement")
    response = problem_statement_div.text.replace("$$$", "")
    return response


def to_txt(problem_code, problem):
    """
    Takes A Problem Code & Its Appropriate Parsed CodeForces Problem And
    Prints It To A Text File.
    """
    with open(problem_code + ".txt", "w") as output_file:
        output_file.writelines(problem)


if __name__ == "__main__":
    try:
        problem_code = sys.argv[1]
    except Exception:
        print(
            "Please Enter A CodeForces Problem Code as a",
            "Command-Line Argument!",
        )
        sys.exit(0)
    problem = get_problem_statement(problem_code)
    to_txt(problem_code, problem)
    print(
        f"Problem {problem_code} Successfully Scraped And Saved To",
        f"{problem_code}.txt",
    )
