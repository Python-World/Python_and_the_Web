import argparse
import csv
import json
import sys

import requests


def call_api(handle):
    # API url
    base_url = "https://codeforces.com/api/user.rating?handle="
    # Append the user
    url = base_url + handle
    # Send request
    r = requests.get(url)
    raw = r.json()
    # Parse response
    response = json.dumps(raw["result"])

    return response


# Check how many arguments were supplied
if len(sys.argv) > 3:
    print("Too many arguments.")
    sys.exit(1)

# Create parser
parser = argparse.ArgumentParser(
    description="Scrape user ratings from codeforce."
)
# Add argument for users
parser.add_argument(
    "-u",
    "--users",
    type=str,
    help="Comma separated list of users to gather ratings for.",
)

# Parse arguments
args = parser.parse_args()
users = args.users

# Split the users by commas
u_list = users.split(",")

# Perform this for each user
for u in u_list:
    # Call API and parse the response
    raw_response = call_api(u)
    parsed_data = json.loads(raw_response)

    # Set the filename and the columns
    csv_name = u + ".csv"
    csv_columns = [
        "contestId",
        "contestName",
        "handle",
        "rank",
        "ratingUpdateTimeSeconds",
        "oldRating",
        "newRating",
    ]

    # Write to file
    with open(csv_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for data in parsed_data:
            writer.writerow(data)
