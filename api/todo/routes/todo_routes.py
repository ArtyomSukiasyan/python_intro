import json
from controllers.todo_controller import create_todo, get_all_todos, update_todo, delete_todo
from bson import json_util, ObjectId


def handle_todo_routes(path, method, data=None):
    if method == "GET":
        todos = get_all_todos()

        return json.loads(json_util.dumps(todos))

    if method == "POST":
        data_dict = json.loads(data.decode('utf-8'))
        new_todo = create_todo(data_dict)

        return json.loads(json_util.dumps(new_todo))

    if method == "PUT":
        todo_id = ObjectId(path.split('/')[-1])
        data_dict = json.loads(data.decode('utf-8'))
        updated_todo = update_todo(todo_id, data_dict)

        return json.loads(json_util.dumps(updated_todo))

    if method == "DELETE":
        todo_id = ObjectId(path.split('/')[-1])
        delete_todo(todo_id)

        return {"message": "Todo deleted"}
