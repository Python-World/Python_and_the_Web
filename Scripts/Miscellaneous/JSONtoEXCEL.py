import json
import pandas as pd
with open('./save_to_excel.json') as json_file:
    data = json.load(json_file)
df = pd.DataFrame(data)
df.to_excel('./exported_json_data.xlsx')