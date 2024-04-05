import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://stephinjosec:<passsword1>@cluster0.xpbeg9b.mongodb.net/")

db = cluster["test"]

collection = db["test"]
post = {"_id":0 , "name": "tim", "score":5}

collection.insert_one(post)

 