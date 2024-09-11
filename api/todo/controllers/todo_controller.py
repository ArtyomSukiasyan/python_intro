from models.todo import Todo
from utils.db import get_db

db = get_db()
todos_collection = db.todos


def create_todo(data):
    new_todo = Todo(
        title=data.get('title'),
        description=data.get('description')
    )
    inserted_id = todos_collection.insert_one(new_todo.to_dict()).inserted_id

    return todos_collection.find_one({"_id": inserted_id})


def get_all_todos():
    return list(todos_collection.find({}))
