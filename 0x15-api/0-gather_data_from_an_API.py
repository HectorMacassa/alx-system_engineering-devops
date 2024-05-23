#!/usr/bin/python3
"""
Module to retrieve and display the TODO list progress of an employee.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and prints the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise an exception for HTTP errors

        user_data = user_response.json()
        employee_name = user_data.get('name')

        todos_url =
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Raise an exception for HTTP errors

        todos_data = todos_response.json()
        total_tasks = len(todos_data)
        done_tasks = [todo for todo in todos_data if todo.get('completed')]
        number_of_done_tasks = len(done_tasks)

        print(
            f"Employee {employee_name} is done with tasks
            ({number_of_done_tasks}/{total_tasks}): ")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print(f"An error occurred while making the HTTP request: {e}")
    except KeyError as e:
        print(f"Unexpected data format in response: missing key {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
