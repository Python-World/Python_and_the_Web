import csv

from bs4 import BeautifulSoup
from selenium import webdriver


# Method to scrape and store DevFest Schedule in csv file
def devfest_schedule():
    url = "https://devfestindia.com/schedule"

    # Running the driver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Change the driver_path to where your chrome driver is installed
    driver_path = "/Users/pc/Desktop/Rough/DevFest_India_2020_Schedule/chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # Requesting the desired webpage through selenium Chrome driver
    driver.get(url)
    select_page_2 = "/html/body/div/div/div[3]/main/div/div[1]/div/div/header/div[2]/div/div/div[2]/div/a[2]"
    select_page_3 = "/html/body/div/div/div[3]/main/div/div[1]/div/div/header/div[2]/div/div/div[2]/div/a[3]"
    driver.find_element_by_xpath(select_page_2).click()
    driver.find_element_by_xpath(select_page_3).click()

    # Storing the entire devfest schedule webpage in html variable
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "lxml")

    day_wise_schedule = soup.find_all("div", attrs={"class": "v-window-item"})

    with open("devfest_schedule.csv", "w") as csv_file:
        writer = csv.writer(csv_file)

        # Initializing the first row with the column title
        writer.writerow(["Name of Event", "Date", "Timings", "Tag", "Author"])

        starting_date = 16
        for schedule in day_wise_schedule:
            events = schedule.find_all(
                "div",
                attrs={
                    "class": "row pa-0 my-0 align-center justify-center row-border-white"
                },
            )
            for event in events:
                event_details = event.find(
                    "div", attrs={"class": "py-3 ma-1 fill-height"}
                )
                event_timings = event.find(
                    "div",
                    attrs={"class": "text-right my-0 py-0 col-md-2 col-3"},
                ).find_all("p")

                event_name = event_details.find("p").text
                event_date = "October " + str(starting_date)
                event_time = (
                    event_timings[0].text.replace(" ", "")
                    + "-"
                    + event_timings[1].text
                    + " "
                    + event_timings[2].text.replace(" ", "")
                )
                event_tag = event_details.find(
                    "span",
                    attrs={
                        "class": "mt-2 mr-2 v-chip v-chip--label v-chip--no-color theme--light v-size--small"
                    },
                ).text
                authors = event_details.find_all(
                    "span",
                    attrs={
                        "class": "mt-2 mr-2 v-chip v-chip--label v-chip--no-color v-chip--outlined theme--light v-size--small"
                    },
                )
                event_authors = ""
                for author in authors:
                    event_authors = (
                        event_authors + author.text.replace(" ", "") + "  "
                    )

                # Adding each event to csv file
                writer.writerow(
                    [
                        event_name,
                        event_date,
                        event_time,
                        event_tag,
                        event_authors,
                    ]
                )

            starting_date = starting_date + 1


if __name__ == "__main__":
    # Scraping the DevFest India 2020 Schedule and storing it in csv file
    devfest_schedule()
    print("devfest_schedule.csv file has been generated")
