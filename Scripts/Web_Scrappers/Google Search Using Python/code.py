# We will be using the search() function from the googlesearch module.
from googlesearch import search


def query_finder(query):
    for item in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(item)


if __name__ == "__main__":
    query = input(
        "Enter your query : "
    )  # This is the text that you want to search for.
    query_finder(query)
