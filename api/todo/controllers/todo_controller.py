from models.todo import Todo
from utils.db import get_db

db = get_db()
todos_collection = db.todos


def get_all_todos():
    return list(todos_collection.find({}))
