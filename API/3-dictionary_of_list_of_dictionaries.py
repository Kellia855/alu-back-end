#!/usr/bin/python3

"""
Script that fetches an employee's TODO list and exports it to JSON.
"""

import requests
import json


def fetch_all_tasks_and_export() -> None:
    """
    Fetch all users and their tasks, and export to todo_all_employees.json
    """
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_resp = requests.get(users_url)
    users_resp.raise_for_status()
    users = users_resp.json()

    # Prepare structure for export
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch todos for this user
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todos_resp = requests.get(todos_url)
        todos_resp.raise_for_status()
        todos = todos_resp.json()

        # Build list of tasks
        task_list = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in todos]

        # Add to main dictionary
        all_tasks[str(user_id)] = task_list

    # Write to JSON file
    with open("todo_all_employees.json", "w", encoding='utf-8') as json_file:
        json.dump(all_tasks, json_file, indent=4)

    print("Exported all tasks to todo_all_employees.json")


if __name__ == "__main__":
    fetch_all_tasks_and_export()
