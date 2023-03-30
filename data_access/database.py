from pymongo import MongoClient
from dotenv import load_dotenv
import os
from data_access.inventarioInicial import inventario_inicial

load_dotenv()


class Database:
    client = MongoClient(os.environ.get("URI"))
    db = client["ollivanders"]
    collection = db["inventario"]
    inventory = inventario_inicial()

    @staticmethod
    def initdb():
        Database.collection.insert_many(Database.inventory)

    @staticmethod
    def createItem(item):
        return Database.collection.insert_one(item)

    @staticmethod
    def readItem(id):
        return Database.collection.find_one({"_id": id})

    # Updated_statement: "key" : "new_value"
    @staticmethod
    def updateItem(id, updated_statement):
        return Database.collection.update_one({"_id": id}, {"$set": updated_statement})

    @staticmethod
    def deleteItem(id):
        return Database.collection.delete_one({"_id": id})

    @staticmethod
    def dropCollection():
        Database.db.drop_collection("inventario")

    @staticmethod
    def inventario():
        return list(Database.collection.find({}))
