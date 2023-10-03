#!/usr/bin/python3

import re
import time

import extracter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def getPlaystoreReviews(app_id):
    # url of the playstore with application_id
    url = (
        "https://play.google.com/store/apps/details?id="
        + app_id
        + "&showAllReviews=true"
    )

    browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    browser.get(url)
    time.sleep(1)

    # get body content to click buttons
    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 400

    path1 = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span'
    path2 = "/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span"
    path3 = "/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span"

    # Scroll web page to get data
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)

        if (no_of_pagedowns - 1) % 12 == 0:
            for path in [path1, path2, path3]:
                try:
                    python_button = browser.find_elements_by_xpath(path)[0]
                    python_button.click()
                except IndexError:
                    elem.send_keys(Keys.PAGE_UP)

        if (no_of_pagedowns - 1) % 25 == 0:
            for path in [path1, path2, path3]:
                try:
                    elem.send_keys(Keys.PAGE_UP)
                    python_button = browser.find_elements_by_xpath(path)[0]
                    python_button.click()
                except IndexError:
                    pass

        no_of_pagedowns -= 1

    # Now that the page is fully scrolled, grab the source code.

    print("Gathering source information")
    source_data = browser.page_source
    time.sleep(1)
    print("Parsing source data")
    soup = BeautifulSoup(source_data, "html.parser")
    time.sleep(1)

    print("Getting source information..")
    time.sleep(1)

    # Revirew main div
    review_divs = soup.find("div", {"jsname": "fk8dgd"})
    print("Gathering reviews information")
    time.sleep(1)
    # Find each review div elements
    reviews = review_divs.findAll("div", {"jscontroller": "H6eOGe"})

    print("Gathering Reviews")
    print("\t=============Reviews=============")
    review_count = 0
    # Iterate through each review get all feilds of comments
    for div in reviews:
        review_count += 1
        user = div.find("span", {"class": "X43Kjb"})
        user = user.text.encode("unicode-escape").decode("utf-8")
        rating = div.find("div", {"class", "pf5lIe"})
        rating = rating.find("div", {"aria-label": re.compile("Rated")})
        rating = str(rating.get("aria-label"))
        rating = rating[6]
        review = div.find("span", {"jsname": "fbQN7e"})
        review = review.text.encode("unicode-escape").decode("utf-8")
        if review == "":
            review = div.find("span", {"jsname": "bN97Pc"})
            review = review.text
        content = {
            "Sno": review_count,
            "User": user,
            "Rating": rating,
            "Review": review,
        }

        print("{} {}".format(review_count, review[0:150]))
        extracter.writecsv(app_id, content)

    browser.close()


def main():
    infile = input("Enter file name: ")
    # for each application id get the application reviews
    with open(infile, "r") as file:
        while 1:
            application_id = file.readline()
            if not application_id:
                break
            getPlaystoreReviews(application_id)


if __name__ == "__main__":
    main()
