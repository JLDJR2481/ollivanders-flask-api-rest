from pymongo import MongoClient
from mongoengine import *
import os
import json

# Cliente para conectarse de forma remota con variable de entorno URI. Debe existir en el archivo .env

cliente = MongoClient(os.environ.get('URI'))
database = cliente["ollivanders"]
collection = database["inventario"]

@staticmethod
def initdb():
    with open('docs/inventario.json') as f:
        inventory = json.load(f)["inventory"]

    collection.insert_many(inventory)

@staticmethod
def drop_collection():
    database.drop_collection("inventario")


