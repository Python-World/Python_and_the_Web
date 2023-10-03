import csv

import requests
from bs4 import BeautifulSoup

# Method for Scrapping the RottenTomatoes site and storing the list of top 100 movies of a particular genre in csv file


def search_with_genre(genre):
    # Creating the file name (for CSV file) same as input provided
    filename = genre

    # Formatting the genre variable for use
    genre = genre.replace("&", "")
    genre = (genre.lower()).replace(" ", "_")

    url = (
        "https://www.rottentomatoes.com/top/bestofrt/top_100_"
        + genre
        + "_movies"
    )

    # Requesting and storing the contents of desired webpage in "soup" variable
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    # Finding all the contents stored in the table format
    find_contents = soup.find(attrs={"class": "table"})

    if find_contents is None:
        print("\nError - Can't find the movies of genre you are looking for!")

        # If input genre is not found then providing the user with a list of valid genres from which user can choose

        print("Try using these GENRES:")
        genre_list = [
            "Action & Adventure",
            "Animation",
            "Art House & International",
            "Classics",
            "Comedy",
            "Documentary",
            "Drama",
            "Horror",
            "Kids & Family",
            "Musical & Performing Arts",
            "Mystery & Suspense",
            "Romance",
            "Science Fiction & Fantasy",
            "Special Interest",
            "Sports & Fitness",
            "Television",
            "Western",
        ]
        for i in genre_list:
            print(i)

    else:
        rows = find_contents.find_all("tr")

        # Creating a csv file and storing the movie information in it
        # If a file already exists the program overwrites its contents

        with open(filename + ".csv", "w") as csv_file:
            writer = csv.writer(csv_file)

            # Initializing the first row with the column title

            writer.writerow(["Rank", "Rating", "Title", "No of Reviews"])

            # Iterating all the rows of the scrapped contents and storing them in desired csv file

            for row in range(1, 101):
                dataset = rows[row].find_all("td")
                rank = dataset[0].text.replace(".", "")
                rating = (
                    dataset[1].find(attrs={"class": "tMeterScore"}).text[1:]
                )
                title = (
                    dataset[2]
                    .find("a", attrs={"class": "unstyled articleLink"})
                    .text.replace(" ", "")
                )
                reviews = dataset[3].text
                writer.writerow([rank, rating, title, reviews])


# Taking the input from the user and searching for movies of particular genre
print("Enter the genre of the movies you are looking for: ")
genre = input()
search_with_genre(genre)
