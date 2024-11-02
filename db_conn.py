# db_conn.py

from pymongo import MongoClient
from config.config import DB_HOST, DB_PORT, DATABASE, COLLECTION

client = MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}")

def conn_db():
    db = client[DATABASE]
    collections = db[COLLECTION]
    
    return db, collections

