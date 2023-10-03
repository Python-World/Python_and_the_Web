from bs4 import BeautifulSoup
from selenium import webdriver


# Method to find the main website from the given URL
def main_website(url):
    parts = url.split("/")
    return parts[2]


# Method to check if the keywords of scrapped link matches with the main website
def present(url, web_main):
    t = False
    for i in range(0, len(url) - len(web_main) + 1):
        if url[i : i + len(web_main)] == web_main:
            t = True
            break
    return t


# Method to check all links in a webpage and categorise them as External or Internal Links
def links(url):
    # Running the driver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # Change the driver_path to where your chrome driver is installed
    driver_path = "/Users/pc/Desktop/Rough/chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    links = ""
    try:
        # Requesting the desired webpage through selenium Chrome driver as some pages use javascripts
        driver.get(url)

        # Storing the entire webpage in html variable
        html = driver.page_source
        driver.quit()

        # Using beautiful soup to filter the scraped data
        soup = BeautifulSoup(html, "lxml")
        links = soup.find_all("a")
        web_main = main_website(url)
        internal_links = []
        external_links = []
        for link in links:
            try:
                final_url = ""
                # x is used to check the first character of the scrapped link
                x = link["href"][0:1]
                if x == "/":
                    final_url = url + link["href"]
                    internal_links.append(final_url)
                elif x == "#":
                    final_url = url + "/" + link["href"]
                    internal_links.append(final_url)
                else:
                    check = present(link["href"], web_main)
                    if check:
                        final_url = link["href"]
                        internal_links.append(final_url)
                    else:
                        final_url = link["href"]
                        external_links.append(final_url)
            except:
                print("Working on your request.......")

        # After storing the internal and external links presenting them on the console
        print("Links assosciated to the webpage: ")
        print("\n\tInternal Links :")
        if len(external_links) == 0:
            print("\t\t", "No Internal Links!")
        for i in range(1, len(internal_links) + 1):
            print("\t\t", internal_links[i - 1])

        print("\n\tExternal Links :")
        if len(external_links) == 0:
            print("\t\t", "No External Links!")
        for i in range(1, len(external_links) + 1):
            print("\t\t", external_links[i - 1])
    except:
        print("Enter a valid webpage URL!")


if __name__ == "__main__":
    url = input(
        "Enter the url of the webpage whose all links are to be grouped(As External or Internal) : "
    )
    links(url)
