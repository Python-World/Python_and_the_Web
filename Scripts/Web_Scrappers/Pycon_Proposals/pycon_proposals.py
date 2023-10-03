import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def scrape_divs():
    """This function scrapes all the proposal elements and stores them
    in a list.
    """
    response = requests.get("https://in.pycon.org/cfp/2020/proposals/")
    soup = bs(response.content, "html.parser")
    mydivs = soup.findAll("div", {"class": "col-sm-11 col-xs-12"})
    return mydivs


def selected_proposals(mydivs, df_columns):
    """This function takes the list of selected proposal elements from the
       scarpe_divs function as well as a list of columns and stores the value
       of the elements in a csv file.
    Args:
        mydivs (list): List of proposal elements
        df_columns (list): List of column names
    """
    final = {}
    for i, div in enumerate(mydivs[:43]):
        title = div.text
        titlex = title.split("\n")
        test_list = list(filter(lambda x: x != "", titlex))
        no_of_votes = test_list[2]
        no_of_messages = test_list[0]
        title = test_list[4]
        tag1 = test_list[5]
        tag2 = test_list[7]
        author = test_list[11].strip()
        date = test_list[14].strip()
        final[i] = [
            no_of_votes,
            no_of_messages,
            title,
            tag1,
            tag2,
            author,
            date,
        ]

    df1 = pd.DataFrame.from_dict(final, orient="index")
    df1.columns = df_columns
    df1.to_csv("selected_proposals.csv")


def total_proposals(mydivs, df_columns):
    """This function takes the list of total proposal elements from the scarpe_divs
       function as well as a list of columns and stores the value of the
       elements in a csv file.
    Args:
        mydivs (list): List of proposal elements
        df_columns (list): List of column names
    """
    final_two = {}
    for i, div in enumerate(mydivs[43:]):
        title = div.text
        titlex = title.split("\n")
        test_list = list(filter(lambda x: x != "", titlex))
        no_of_votes = test_list[2]
        no_of_messages = test_list[0]
        title = test_list[4]
        tag1 = test_list[6]
        tag2 = test_list[8]
        author = test_list[12].strip()
        date = test_list[15].strip()
        final_two[i] = [
            no_of_votes,
            no_of_messages,
            title,
            tag1,
            tag2,
            author,
            date,
        ]
    df2 = pd.DataFrame.from_dict(final_two, orient="index")
    df2.columns = df_columns
    df2.to_csv("total_proposals.csv")


if __name__ == "__main__":
    df_columns = [
        "Votes",
        "Messages",
        "Title",
        "Tag1",
        "Tag2",
        "Author",
        "Date",
    ]
    mydivs = scrape_divs()
    selected_proposals(mydivs, df_columns)
    total_proposals(mydivs, df_columns)
    print("The proposals have been saved successfully!!!")
