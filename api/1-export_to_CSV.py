#!/usr/bin/python3

"""
script to export employee's TODO list to a CSV file
"""
import csv
import requests
import sys



def fetch_and_export_to_csv(employee_id: int) -> None:
    """
    Fetch employee tasks from API and export them to CSV.

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
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

    print(f"Exported {len(todos)} tasks to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    fetch_and_export_to_csv(int(sys.argv[1]))
