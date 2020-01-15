import json
import os
import pandas as pd
from pymongo import MongoClient

def import_csvfile(filepath):
 mng_client = MongoClient('mongodb+srv://analytics:<password>@removeduplicates-od9at.mongodb.net/test?retryWrites=true&w=majority') # replace host
 mng_db = mng_client['restaurants_db']
 collection_name = 'restaurants'
 db_cm = mng_db[collection_name]
 cdir = os.path.dirname(__file__)
 file_res = os.path.join(cdir, filepath)
 data = pd.read_csv(file_res)
 data_json = json.loads(data.to_json(orient='records'))
 i = 0
 for data in data_json:
     i = i + 1
     business = {"value": i}
     db_cm.insert_one(data)