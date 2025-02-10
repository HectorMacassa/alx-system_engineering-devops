#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress using REST API.

This module makes HTTP requests to fetch employee information and their TODO items,
then displays their progress in a formatted output.

Usage:
    python3 todo_progress.py <employee_id>

The script will display:
    - Employee name
    - Number of completed tasks vs total tasks
    - Titles of all completed tasks
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee to fetch TODO progress for

    Returns:
        None: Prints the progress directly to stdout
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print(f"Error: Could not fetch employee with ID {employee_id}")
        sys.exit(1)

    employee = employee_response.json()
    employee_name = employee.get('name', 'Unknown Employee')

    # Get todos for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch TODOs for employee with ID {employee_id}")
        sys.exit(1)

    todos = todos_response.json()

    # Calculate progress using get() for safe access
    completed_tasks = [todo for todo in todos if todo.get('completed', False)]
    total_tasks = len(todos)
    num_completed = len(completed_tasks)

    # Display progress in required format
    print(f"Employee {employee_name} is done with "
          f"tasks({num_completed}/{total_tasks}):")

    # Display completed task titles using get()
    for task in completed_tasks:
        print(f"\t {task.get('title', 'No title available')}")


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
