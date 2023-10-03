import argparse

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


def create_and_share_sheet(user_mail, spreadsheet_name, csv_file):
    client = auth_user()
    sh = client.create(spreadsheet_name)
    worksheet = sh.worksheet("Sheet1")

    # Read from the csv file mentioned in the command.
    df = pd.read_csv(csv_file)
    col = df.columns
    # Define the column headings based on the our csv file.
    end = ord("A") + len(col) - 1
    cell_range = "A1:" + chr(end) + "1"

    # Define cells
    cell_list = worksheet.range(cell_range)
    i = 0
    for cell in cell_list:
        cell.value = col[i]
        i += 1

    # Write these column headings to the worksheet
    worksheet.update_cells(cell_list)

    # Convert rest of the dataframe to numpy object. (Use pandas version 1.0.3 strictly for this to work!)
    df = df.to_numpy().tolist()

    # Write data from numpy object to the worksheet
    for i in range(2, len(df) + 2):
        pos = "A" + str(i) + ":" + chr(end) + str(i)
        cell_list = worksheet.range(pos)
        val = df[i - 2]
        j = 0
        for cell in cell_list:
            cell.value = val[j]
            j += 1
            worksheet.update_cells(cell_list)

    # Share the created spreadsheet with the receiver.
    sh.share(user_mail, perm_type="user", role="writer")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="generate and share google sheet for give csv"
    )
    parser.add_argument(
        "-mail",
        help="Enter the email id of the community admin",
        dest="mail_id",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-csv",
        help="Enter path of csv file",
        dest="csv",
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

    community_admin = args.mail_id
    csv_file = args.csv
    spreadsheet_name = args.ss_name

    create_and_share_sheet(community_admin, spreadsheet_name, csv_file)
