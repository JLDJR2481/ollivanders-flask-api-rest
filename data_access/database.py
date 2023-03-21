from pymongo import MongoClient
from mongoengine import *
from dotenv import load_dotenv
import os
import json

load_dotenv()

class Database:
    client = MongoClient(os.environ.get("URI"))
    db = client["ollivanders"]
    collection = db["inventario"]


    @staticmethod
    def initdb():
        with open('docs/inventario.json') as f:
            inventario = json.load(f)["inventory"]
    
        Database.collection.insert_many(inventario)

    @staticmethod
    def createItem(item):
        return Database.collection.insert_one(item)

    @staticmethod
    def readItem(id):
        return Database.collection.find_one({"_id": id})

    # Updated_statement: "key" : "new_value"
    @staticmethod
    def updateItem(id, updated_statement):
        return Database.collection.update_one({"_id" : id} , {"$set": updated_statement})
    
    @staticmethod
    def deleteItem(id):
        return Database.collection.delete_one({"_id":id})

    @staticmethod
    def dropCollection():    
        Database.db.drop_collection("inventario")


