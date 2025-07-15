#!/usr/bin/python3
"""
script to fetch employee's todo list and return progress
"""

import sys
import requests


def fetch_todo_progress(employee_id):
    try:
        # Fetch employee details
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch todos for the employee
        todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Process todo list
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task.get('completed')]
        number_of_done_tasks = len(done_tasks)

        # Print summary
        print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task.get('title')}")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid JSON received.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
    else:
        fetch_todo_progress(int(sys.argv[1]))
