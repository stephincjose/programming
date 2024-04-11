import pymongo
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://stephincjose:vALrfi92MCJ3g16I@cluster0.jh2zpzm.mongodb.net/")



db = cluster["test"]

collection = db["test"]
post = {"_id":0 , "name": "tim", "score":5}
collection.insert_one(post)


 