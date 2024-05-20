#!/usr/bin/python3
"""
This script exports data in the JSON format
"""
import sys
import json
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for a given employee ID.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    print(f"Employee {employee_name} is done with "
          f"tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

    json_data = {
        "USER_ID": employee_id,
        "USERNAME": user_data['username'],
        "TASKS": []
    }
    for todo in todos:
        task = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_data['username']
        }
        json_data["TASKS"].append(task)

    json_file = f"{employee_id}.json"
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"\nTasks exported to '{json_file}'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
