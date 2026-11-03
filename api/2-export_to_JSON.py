#!/usr/bin/python3
"""Export all TODO tasks of a given employee to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    username = user.get("username")
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
