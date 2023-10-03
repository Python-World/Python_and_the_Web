import getpass
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Sign in and validation part
print("Please sign in to your LinkedIn Account:")
u = input("Email or phone number: ")
p = getpass.getpass("Password: ")
print("Validating...")
chrome_options = Options()
chrome_options.add_argument("--window-size=1360,768")
chrome_options.add_argument("headless")
driver = webdriver.Chrome(
    "./chromedriver", options=chrome_options
)  # Can replace this path with your chromedriver path
driver.get("https://www.linkedin.com")
unme = driver.find_element_by_id("session_key")
passw = driver.find_element_by_id("session_password")
unme.send_keys(u)
passw.send_keys(p)
passw.send_keys(Keys.ENTER)
cond = True
time.sleep(2)
if (
    driver.title == "LinkedIn Login, Sign in | LinkedIn"
    or driver.title == "LinkedIn: Log In or Sign Up"
):
    print("Invalid Username or Password")
    print("The program will now exit")
    driver.quit()
    cond = False
if cond is True:
    time.sleep(2)
    print("Fetching Info (This might take a while)...")
    body = driver.find_element_by_tag_name("body")
    for i in range(50):
        body.send_keys(Keys.CONTROL, Keys.END)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    print("Done")
    # Fetching Posts
    divs = soup.find_all(
        "div",
        attrs={
            "class": re.compile(
                "feed-shared-update-v2 feed-shared-update-v2--minimal-padding full-height relative feed-shared-update-v2--e2e artdeco-card ember-view"
            )
        },
    )
    ctr = 0
    authors = []
    sdesc = []
    timestamp = []
    posts = []
    print("Fetching the latest posts for you...")
    for d in divs:
        author = d.find(
            "div",
            attrs={"class": re.compile("feed-shared-actor__meta relative")},
        )
        content = d.find(
            "div",
            attrs={
                "class": re.compile(
                    "feed-shared-update-v2__description-wrapper ember-view"
                )
            },
        )
        try:
            name = author.find("span", attrs={"dir": "ltr"})
            adesc = author.find(
                "span",
                attrs={
                    "class": "feed-shared-actor__description t-12 t-normal t-black--light"
                },
            )
            added = author.find("span", attrs={"class": "visually-hidden"})
            post = content.find("span", attrs={"dir": "ltr"})
            n = name.text
            ad = added.text
            ads = adesc.text
            po = post.text
        except AttributeError:
            continue
        authors.append(n)
        sdesc.append(ads)
        timestamp.append(ad)
        posts.append(po)
    if len(authors) == 0:
        # Bots can be caught by linkedin website if used very frequently
        print("Oops! Seems the the bot has crashed due to over-usage :(")
        print("Please try after 10 mins.")
        cond = False
    if cond is True:
        print("Done")
        print("Choose the post you want to see :")
        for i in range(len(authors)):
            print(
                "\t"
                + str(i + 1)
                + ". "
                + authors[i]
                + ". Added: "
                + timestamp[i]
            )
        ans = "y"
        while ans == "y":
            ch = int(input("Enter your choice: "))
            if ch > len(authors) or ch < 1:
                print("Invalid Choice.")
            else:
                print(authors[ch - 1])
                print("Posted: " + timestamp[ch - 1])
                print("Author Description: " + sdesc[ch - 1])
                print(posts[ch - 1])
            ans = input("Want to see other posts? (y/n) ")
            print("")
        print("Thank You")
