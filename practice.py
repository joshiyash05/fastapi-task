from fastapi import FastAPI
import pandas as pd
from models.charts_data import CsvData
from config.databasedetails import collections_name
from schema.schemas import individual_data,list_data
from bson import ObjectId

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/completedata")
async def root():
    finaldata = collections_name.find() 
    data = list_data(finaldata)
    return data
@app.get("/completedata/{data_info}")
async def root(data_info):
    finaldata = collections_name.find({'Chart Type':data_info})
    data = list_data(finaldata)
    return {'Chart Type':data_info,'data':data}

@app.get("/insertdata")
async def read_item():
    df = pd.read_excel('table-data.xlsx')
    records = df.to_dict(orient="records")
    collections_name.insert_many(records)
    return {"Insertion completed":("Inserted {} records into MongoDB.".format(len(records)))}