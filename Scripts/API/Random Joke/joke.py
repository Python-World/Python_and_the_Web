#!/bin/env python3
import sys

import requests
import typer
from colored import attr, fg

app = typer.Typer()
rst = attr("reset")  # reset colors

JOKE_TWO_PARTS = f"""{fg(40) + attr("bold") + attr("dim")}Setup: {rst + fg(202)}{{setup}}
{fg(40) + attr("bold") + attr("dim")}Delivery: {rst + fg(202)}{{delivery}}"""

JOKE_SINGLE = (
    f"""{fg(40) + attr("bold") + attr("dim")}Joke: {rst + fg(202)}{{joke}}"""
)

DEFAULT_FORMAT = f"""{fg(46) + attr("bold") + attr("dim")}Category: {rst + fg(214)}{{category}}
{fg(46) + attr("bold") + attr("dim")}Type: {rst + fg(214)}{{type}}

{{joke}}{rst}"""

ERROR_MSG = f"{fg(124) + attr('bold')}\u2718 Error: {{error_message}}"


@app.command(
    help=f"""
This script will use {fg("yellow")}JokeAPI{rst} ({fg("light_blue")}https://sv443.net/jokeapi/v2/{rst}) to get jokes.

You can specify the {fg("green_1")}category{rst} or {fg("spring_green_1")}theme to avoid{rst}.

{fg("light_yellow") + attr("bold")}Note{rst} that the categories and the themes are comma 
separated and case insensitive like in {attr("dim")}./joke.py --category dArk,pUn{rst} 
or {attr("dim")}./joke.py --exclude nSfW,RaCiSt{rst}
\n\n{rst}\n\n
{fg("green_1")}Categories available (comma separated):

    Any (default)
    Miscellaneous
    Programming
    Dark
    Pun{rst}

{fg("spring_green_1")}Themes to exclude (comma separated):

    Nsfw
    Religious
    Political
    Racist
    Sexist{rst}
"""
)
def main(category: str = "Any", exclude: str = ""):
    res = requests.get(
        "https://sv443.net/jokeapi/v2/joke/" + category,
        params={"blacklistFlags": exclude},
    ).json()

    if res["error"]:
        print(
            ERROR_MSG.format(
                error_message=rst + fg(9) + res["additionalInfo"]
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    else:
        print(
            DEFAULT_FORMAT.format(
                category=res["category"],
                type=res["type"],
                joke=JOKE_TWO_PARTS.format(
                    setup=res["setup"], delivery=res["delivery"]
                )
                if res["type"] == "twopart"
                else JOKE_SINGLE.format(joke=res["joke"]),
            )
        )


if __name__ == "__main__":
    app()
