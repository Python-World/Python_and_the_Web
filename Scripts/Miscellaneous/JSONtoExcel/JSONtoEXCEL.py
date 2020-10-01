#Script to convert JSON file to .xlsx file(Excel).
#Requirements : 
# Pandas (Data Manipulation Library. Install : pip install pandas)

#  Importing Pandas and json
import json
import pandas as pd
# Importing the data from a file using the load method
with open('./sampleData.json') as json_file:
    data = json.load(json_file)
# Creating a dataframe
df = pd.DataFrame(data)
df.to_excel('./exported_json_data.xlsx')