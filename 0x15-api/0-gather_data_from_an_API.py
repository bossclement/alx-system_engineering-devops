#!/usr/bin/python3
"""script that sends a get request to a REST API"""


import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/users"
    link = URL + "/" + employeeId

    response = requests.get(link)
    employeeName = response.json().get('name')

    tdlink = link + "/todos"
    response = requests.get(tdlink)
    todos = response.json()
    done = 0
    done_tasks = []

    for task in todos:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with todos({}/{}):"
          .format(employeeName, done, len(todos)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
