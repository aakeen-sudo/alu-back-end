#!/usr/bin/python3
"""Export all TODO tasks of a given employee to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = int(sys.argv[1])

    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()

    username = user.get("username")
    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])
