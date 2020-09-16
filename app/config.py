from pymongo import MongoClient
from bson.json_util import dumps



mongo_client = MongoClient("mongodb://localhost:27017/")

for db in mongo_client.list_database_names():
    print(db)

db = mongo_client["coffee_app"]
machines_collection = db["machines"]
pods_collection = db["pods"]
