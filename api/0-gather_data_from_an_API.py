#!/usr/bin/python3
"""Return TODO list progress for a given employee ID using a REST API."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    done_tasks = [task.get("title") for task in todos
                  if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    for title in done_tasks:
        print("\t {}".format(title))
