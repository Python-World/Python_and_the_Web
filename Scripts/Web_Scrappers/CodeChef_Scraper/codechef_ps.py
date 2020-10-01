import os
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if not os.path.exists("problems"):
    os.makedirs("problems")

options = webdriver.ChromeOptions()
options.add_argument("headless")


def scrapeCodeChef(code):
    try:
        url = f"https://www.codechef.com/problems/{code}"

        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        print("[OPENING] - ", code)
        browser.get(url)

        print("[SCRAPING] - ", code)
        soup = BeautifulSoup(browser.page_source, features="html.parser")

        head = soup.find_all(["h1"])
        check = soup.find_all(["p", "h3", "ul", "pre"])

        f = open("problems/" + url[34:] + ".txt", "a")
        f.write(head[1].text[:-7] + "\n")
        for i in range(8, len(check) - 18):
            f.write(check[i].text + "\n")
        f.close()

        print(f"[FINISHED] - File saved - problems/{code}.txt")    
    except Exception:
        print("Cannot Find CodeChef Problem! - " + code)
        exit(0)


if __name__ == "__main__":
    try:
        code = sys.argv[1]
    except Exception:
        print('Please Enter A CodeChef Problem Code as a',
              'Command-Line Argument!')
        exit(0)
    scrapeCodeChef(code)
