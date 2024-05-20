#!/usr/bin/python3
"""
This script exports data in the CSV format
"""
import sys
import csv
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

    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for todo in todos:
        row = [
            todo['userId'],
            user_data['username'],
            str(todo['completed']),
            todo['title']
        ]
        csv_data.append(row)

    csv_file = f"{employee_id}.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f"\nTasks exported to '{csv_file}'")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
