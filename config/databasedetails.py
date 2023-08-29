from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://yash:yash2003@cluster0.bovzlyd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.charts_db

collections_name = db["charts_collections"]
