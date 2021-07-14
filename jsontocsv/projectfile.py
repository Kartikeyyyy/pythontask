import csv
import json
import pandas as pd
from pandas.io.json import json_normalize

def json_csv():

    with open('my_json_file.JSON') as data_file:
        data=json.load(data_file)
    normalized_df = pd.json_normalize(data)
    normalized_df.to_csv('my_csv_file.csv',index=False)
    return


json_csv()
