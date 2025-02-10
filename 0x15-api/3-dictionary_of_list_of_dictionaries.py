#!/usr/bin/python3
"""
Script that retrieves TODO lists for all employees and exports to JSON format.

This module makes HTTP requests to fetch information and TODO items for all
employees, then exports the combined data to a single JSON file.

Usage:
    python3 todo_all_employees.py

The script will create a JSON file named todo_all_employees.json with all tasks
from all employees.
"""
import json
import requests


def get_all_employees_todo():
    """Fetch and export TODO data for all employees to JSON format.

    Returns:
        None: Exports data to todo_all_employees.json
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all employees
    employees_response = requests.get(f"{base_url}/users")
    if employees_response.status_code != 200:
        print("Error: Could not fetch employees")
        return

    employees = employees_response.json()

    # Dictionary to store all tasks
    all_tasks = {}

    # Fetch todos for each employee
    for employee in employees:
        employee_id = str(employee.get('id'))
        username = employee.get('username', 'unknown')

        # Get todos for the current employee
        todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        if todos_response.status_code != 200:
            print(f"Error: Could not fetch TODOs for employee {employee_id}")
            continue

        todos = todos_response.json()

        # Format tasks for the current employee
        employee_tasks = [
            {
                "username": username,
                "task": todo.get('title', 'No title available'),
                "completed": todo.get('completed', False)
            }
            for todo in todos
        ]

        # Add to the main dictionary
        all_tasks[employee_id] = employee_tasks

    # Export to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    get_all_employees_todo()
