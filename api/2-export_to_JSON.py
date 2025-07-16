#!/usr/bin/python3
"""
Script that fetches an employee's TODO list and exports it to JSON.
"""
import json
import requests
import sys


def fetch_and_export_to_json(employee_id: int) -> None:
    """
    Fetch employee tasks and export to JSON file.

    Args:
        employee_id (int): ID of the employee.
    """
    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user = user_response.json()
    username = user.get("username")

    # Fetch todos
    todos_url = (
         "https://jsonplaceholder.typicode.com/todos"
         f"?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    # Format tasks for JSON
    task_list = [{
        "task": task.get("title"),
        "completed": task.get("completed"),

        "username": username
    } for task in todos]

    # Final structure
    data = {str(employee_id): task_list}

    # Save to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Exported {len(todos)} tasks to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    fetch_and_export_to_json(int(sys.argv[1]))
