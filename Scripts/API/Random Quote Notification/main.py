# Random Quote Desktop Notification
# Author: Rogue Halo
# Date: 1st October 2020
# ---------------------------------
# Imports
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from plyer import notification


# Sub-Routines
def fetch():  # This gets the quote from the API and turns it into the quote to be displayed
    quoteSite = requests.get("http://api.quotable.io/random")
    quoteJson = quoteSite.json()
    quote = quoteJson["content"] + "\n- " + quoteJson["author"]
    if len(quote) > 256:
        fetch()
    else:
        return quote


def display(quote):  # Uses the plyer module to display the quote
    notification.notify(
        title="Random Quote",
        message=quote,
        app_name="Random Quote",
        app_icon="icon.ico",
        timeout=10,
        toast=False,
    )


# Main Program
def task():  # This puts it all together
    quote = fetch()
    display(quote)


if __name__ == "__main__":
    task()  # So that it prints a quote without waiting for the interval
    scheduler = BlockingScheduler()  # Creates a scheduler
    scheduler.add_job(
        task, "interval", hours=1
    )  # Sets the interval, you may change this to your preferences
    scheduler.start()  # Starts scheduler
