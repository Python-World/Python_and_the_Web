import csv

from bs4 import BeautifulSoup
from selenium import webdriver


# Method for filtering the contents of "title" variable as "charmap" repeatedly fails to encode some characters
def filter_output(s):
    event = ""
    for i in s:
        if ord(i) >= 32 and ord(i) <= 126:
            event = event + str(i)
    return event


# Method for Scrapping top torrents from The Pirate Bay website and storing it in a csv file
def top_torrents(cat, subcat):
    # To choose the file_name of CSV File
    print("Type the file_name for the csv file:")
    file_name = str(input())

    url = "https://thepiratebay.org/search.php?q=top100:" + str(
        cat * 100 + subcat
    )

    # Running the driver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Change the driver_path to where your chrome driver is installed
    driver_path = "/Users/pc/Desktop/chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # Requesting the desired webpage through selenium Chrome driver
    driver.get(url)

    # Storing the entire Top torrents webpage in html variable
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "lxml")

    # Finding all the top torrents based on category
    torrent_list = soup.find("ol", attrs={"id": "torrents"})
    list = torrent_list.find_all("li", attrs={"class": "list-entry"})

    # Writing the scrapped torrents into csv file
    with open(file_name + ".csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "Name/Title of the file",
                "Category",
                "Link",
                "Date Uploaded",
                "File Size",
            ]
        )
        for i in list:
            title = filter_output(
                i.find(
                    "span", attrs={"class": "list-item item-name item-title"}
                ).text
            )
            category = i.find(
                "span", attrs={"class": "list-item item-type"}
            ).text
            link = (
                "https://thepiratebay.org"
                + i.find(
                    "span", attrs={"class": "list-item item-name item-title"}
                ).a["href"]
            )
            date_uploaded = i.find(
                "span", attrs={"class": "list-item item-uploaded"}
            ).text
            file_size = i.find(
                "span", attrs={"class": "list-item item-size"}
            ).text
            writer.writerow([title, category, link, date_uploaded, file_size])
    print("\n\nDesired CSV File is generated :)")


if __name__ == "__main__":
    # Scraping The Pirate Bay - Torrent Site and storing the desired category in a csv file
    print("\t\t\tTop Torrents are here!!")
    print("Select the category:")
    print(
        "\t 1. Audio\n"
        + "\t 2. Video\n"
        + "\t 3. Applications\n"
        + "\t 4. Games\n"
        + "\t 5. Porn\n"
        + "\t 6. Others"
    )
    print("For Eg - for 'Games' input is 4")
    try:
        cat = int(input())
        if cat < 1 or cat > 6:
            print("Invalid Input!")
        else:
            subcat = 0
            if cat == 6:
                print("Choose the sub-category:")
                print(
                    "\t 1. E-Books\n"
                    + "\t 2. Comics\n"
                    + "\t 3. Pictures\n"
                    + "\t 4. Covers\n"
                    + "\t 5. Physibles\n"
                    + "\t 6. Other"
                )
                print("For Eg - for 'Comics' input is 2")
                subcat = int(input())
                if subcat < 0 or subcat > 6:
                    print("Invalid Input!")
                else:
                    if subcat == 6:
                        subcat = 99

            top_torrents(cat, subcat)
    except:
        print("Error:\t Either input is invalid or connection is slow")
