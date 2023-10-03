# Script to convert JSON file to .xlsx file(Excel).
# Requirements :
# Pandas (Data Manipulation Library. Install : pip install pandas)

#  Importing Pandas and json
import json
import os

from pandas import DataFrame


# Importing the data from a file using the load method
def convert(inp_json_file: str) -> None:
    """Simple function to convert any .json file to a xlsx file of any name"""
    with open(inp_json_file) as json_file:
        data = json.load(json_file)
        #  Creating a dataframe
        df = DataFrame(data)
        out_xlsx_file = inp_json_file[:-4] + "xlsx"
        df.to_excel(out_xlsx_file)


if __name__ == "__main__":
    convert(
        os.path.join(
            (os.path.abspath(".")),
            "Python_and_the_web\Scripts\Miscellaneous\JSONtoExcel\sampleData.json",
        )
    )
