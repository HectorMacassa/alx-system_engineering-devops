#!/usr/bin/python3
"""
This script exports data in the JSON format
"""
import json
import requests


def export_all_tasks_to_json():
    """
    Retrieves all tasks from all employees and exports them to a JSON file.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    todo_data = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        todo_data[user_id] = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            todo_data[user_id].append(task)

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        json.dump(todo_data, file, indent=4)

    print(f"All tasks exported to '{json_file}'")


if __name__ == "__main__":
    export_all_tasks_to_json()
