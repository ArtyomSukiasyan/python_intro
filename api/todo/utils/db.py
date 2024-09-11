from pymongo import MongoClient


def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.todo_app_db

    return db
