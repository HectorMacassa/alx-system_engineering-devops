#!/usr/bin/python3
"""
Script that retrieves an employee's TODO list and exports it to CSV format.

This module makes HTTP requests to fetch employee information and their
TODO items,then exports the data to a CSV file and displays
progress information.

Usage:
    python3 todo_csv.py <employee_id>

The script will:
    - Display TODO progress on stdout
    - Create a CSV file named USER_ID.csv with all tasks
"""
import csv
import requests
import sys


def export_todo_data(employee_id):
    """Fetch employee TODO data and export it to CSV format.

    Args:
        employee_id (int): The ID of the employee to fetch TODO data for

    Returns:
        None: Prints progress to stdout and exports data to CSV
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    if employee_response.status_code != 200:
        print(f"Error: Could not fetch employee with ID {employee_id}")
        sys.exit(1)

    employee = employee_response.json()
    employee_name = employee.get('name', 'Unknown Employee')
    username = employee.get('username', 'unknown')

    # Get todos for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch for employee with ID {employee_id}")
        sys.exit(1)

    todos = todos_response.json()

    # Calculate progress
    completed_tasks = [todo for todo in todos if todo.get('completed', False)]
    total_tasks = len(todos)
    num_completed = len(completed_tasks)

    # Display progress in required format
    print(f"Employee {employee_name} is done with "
          f"tasks({num_completed}/{total_tasks}):")

    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title', 'No title available')}")

    # Export all tasks to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                str(todo.get('completed', False)),
                todo.get('title', 'No title available')
            ])


if __name__ == "__main__":
    # Check if employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 todo_csv.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_todo_data(employee_id)
