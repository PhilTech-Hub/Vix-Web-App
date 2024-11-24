from pymongo import MongoClient
from config import Config

def get_database():
    client = MongoClient(Config.MONGO_URI)
    return client.vix_db
