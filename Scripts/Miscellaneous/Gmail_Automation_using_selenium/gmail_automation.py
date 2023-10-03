"""
This script automate the gmail login process and
Sending first mail from your inbox and send to the
sender's Email id

Note: Please create `details.ini` in same Directory
(check README.md for more Details)

"""

import configparser
import time

from bs4 import BeautifulSoup

# import essential libraries
from selenium import webdriver


def main():
    # --------------credintials reading-----------!
    config = configparser.ConfigParser()
    config.read("details.ini")

    username_for_email = config.get("login_details", "username_for_email")
    password_for_email = config.get("login_details", "password_for_email")
    sending_email_add = config.get("login_details", "sending_email_add")
    driverpath = config.get("login_details", "driverpath")

    # driver path for chrome
    driver = webdriver.Chrome(driverpath)
    driver.maximize_window()
    driver.get(config.get("login_details", "url_path"))

    # email username

    try:
        mark1 = 0
        elem = driver.find_element_by_id("identifierId")
        elem.send_keys(username_for_email)
        mark1 = 1
    except AttributeError as exception:
        if mark1 == 0:
            driver.refresh()
            time.sleep(2)
            elem = driver.find_element_by_id("identifierId")
            elem.send_keys(username_for_email)
        print("exception has been  thown--> " + str(exception))

    # paste username in username bar
    try:
        mark2 = 0
        next_btn_for_email = driver.find_element_by_id("identifierNext")
        next_btn_for_email.click()
        mark2 = 1
        time.sleep(5)

    except AttributeError as exception:
        if mark2 == 0:
            driver.refresh()
            time.sleep(3)
            driver.find_element_by_id("identifierNext").click()
            time.sleep(3)
        print("exception thrown : " + str(exception))

    # paste Password in password bar
    try:
        mark3 = 0
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password_for_email)
        mark3 = 1
    except AttributeError as exception:
        if mark3 == 0:
            driver.find_element_by_name("password").send_keys(
                password_for_email
            )
        print("exception has been  thown--> " + str(exception))
        # driver.refresh()

    # clcik submit button
    try:
        mark4 = 0
        next_btn_for_password = driver.find_element_by_id("passwordNext")
        next_btn_for_password.click()
        mark4 = 1
        time.sleep(5)
    except AttributeError as exception:
        if mark4 == 0:
            driver.refresh()
            time.sleep(3)
            driver.find_element_by_id("passwordNext").click()

        print("exception has been  thown---> " + str(exception))

        # driver.refresh()

    time.sleep(8)
    html_code = driver.page_source
    soup = BeautifulSoup(html_code, "html.parser")
    table_obj_code = soup.findAll("table", attrs={"id": ":34"})

    # selection of grid to pick first email
    try:
        mark5 = 0
        for elem in table_obj_code:
            tr_obj = elem.findAll("tr")

        for tr in tr_obj:
            p = driver.find_element_by_id(":3e")
            print("object found ", tr)
        p.click()
        mark5 = 1
    except AttributeError as exception:
        if mark5 == 0:
            driver.refresh()
            time.sleep(4)
            for elem in table_obj_code:
                tr_obj = elem.findAll("tr")

            for tr in tr_obj:
                p = driver.find_element_by_id(":3e")
            p.click()
        print("exception has been  thown--> " + str(exception))
        print("grid of emails not found due to slow internet !")

    next_soup = BeautifulSoup(driver.page_source, "html.parser")

    # picking first mail and opening send panel
    try:
        mark6 = 0
        class_obj = next_soup.findAll("div", attrs={"class": "amn"})
        for i in class_obj:
            print("object found ", i)
            pq = driver.find_element_by_class_name("bkG")
            pq.click()
        mark6 = 1
    except AttributeError as exception:
        if mark6 == 0:
            class_obj = next_soup.findAll("div", attrs={"class": "amn"})
            for i in class_obj:
                pq = driver.find_element_by_class_name("bkG")
                pq.click()

        print("exception has been  thown--> " + str(exception))

        # driver.refresh()

    third_soup = BeautifulSoup(driver.page_source, "html.parser")

    filed = third_soup.findAll("table", attrs={"class": "GS"})

    # click Send button
    try:
        flag = 0
        for i in filed:
            # pasting sender's email id
            driver.find_element_by_class_name("vO").send_keys(
                sending_email_add
            )
            flag = 1
            succ = driver.find_element_by_class_name("btA")

            # send mail
            succ.click()
            time.sleep(1)
    except AttributeError as exception:
        if flag == 0:
            driver.refresh()
            time.sleep(4)
            driver.find_element_by_class_name("vO").send_keys(
                sending_email_add
            )
            driver.find_element_by_class_name("btA").click()

        else:
            driver.find_element_by_class_name("btA").click()

        print("button not clicked succesfully! " + str(exception))
    driver.refresh()

    print("process finished")
    driver.quit()


# driver function
if __name__ == "__main__":
    main()
