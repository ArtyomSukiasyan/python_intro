import json


def validate_todo_data(data):
    try:
        todo_data = json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        return False, "Invalid JSON format"

    if 'title' not in todo_data or type(todo_data['title']) != str:
        return False, "'title' is required and must be a string"

    if 'description' not in todo_data or type(todo_data['title']) != str:
        return False, "'description' is required and must be a string"

    if 'status' in todo_data and todo_data['status'] not in ['pending', 'completed']:
        return False, "'status' must be either 'pending' or 'completed'"

    return True, None
