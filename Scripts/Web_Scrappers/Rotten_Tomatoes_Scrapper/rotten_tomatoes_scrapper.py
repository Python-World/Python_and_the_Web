#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup


def get_movie_ratings(movie):
    """
    This function takes the movie name as input and scraps
    the rating information from the rottentomatoes.
    """
    movie = (movie.lower()).replace(" ", "_")
    URL = "https://www.rottentomatoes.com/m/" + movie
    try:
        page = requests.get(URL)
        if not page:
            raise Exception(page.status_code)
    except Exception as e:
        print("Cannot Find Movie!" + str(e))
        sys.exit(0)
    soup = BeautifulSoup(page.content, "html.parser")

    ratings = soup.find_all("span", class_="mop-ratings-wrap__percentage")
    critic = soup.find_all(
        "p", class_="mop-ratings-wrap__text mop-ratings-wrap__text--concensus"
    )

    print("Critic Consensus: ", (critic[0].get_text()).strip())
    print()
    print("TOMATOMETER: ", (ratings[0].get_text()).strip())
    print("AUDIENCE SCORE: ", (ratings[1].get_text()).strip())

    return 1


if __name__ == "__main__":
    try:
        movie = sys.argv[1]
    except Exception:
        print(
            "Please Enter a Movie Name In Single Quotes In The Command Line!"
        )
        sys.exit(0)
    movie = get_movie_ratings(movie)
