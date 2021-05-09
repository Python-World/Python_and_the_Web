#!/usr/bin/env python3
import re


def main():
    print("Enter the name of the input file: ")
    file = str(input())
    return print_emails(get_emails(file))
    # Can add os.path functionality


def get_emails(filename: str):
    """Function to return list of email matches found in filename passed"""
    with open(filename, "r") as file:
        emails = []
        for line in file:
            # em = re.find('\S+@\S+\.\S+',line)
            # print(em)
            regex = re.match(
                r"\S+@\S+\.\S+", line
            )  # Creates a match object for a correct match
            if regex:  # if match exists
                emails.append(regex.group(0))  # extracts the text of the match

        return emails


def print_emails(emails):
    """Simple printing function"""
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
