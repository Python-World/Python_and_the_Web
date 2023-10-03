import argparse
import json

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def auth_user():
    # Define a authorized user with the credentials created.
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )

    client = gspread.authorize(credentials)
    return client


def get_sheet_json(spreadsheet_name, json_file):
    # Retrieve spreadsheet by name from the user's google drive.
    client = auth_user()
    sheet = client.open(spreadsheet_name).sheet1
    data = sheet.get_all_records()

    # Dump the retrieved csv file in json format.
    with open(json_file, "w") as fout:
        json.dump(data, fout, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="get data from spreadsheet in json format"
    )
    parser.add_argument(
        "-json",
        help="Enter path of json file",
        dest="json",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-spreadsheet_name",
        help="Enter name of spreadsheet",
        dest="ss_name",
        type=str,
        required=True,
    )

    args = parser.parse_args()

    spreadsheet_name = args.ss_name
    json_file = args.json

    get_sheet_json(spreadsheet_name, json_file)
