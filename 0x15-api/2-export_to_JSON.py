#!/usr/bin/python3
"""Script that sends a get request to a REST API"""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/users"
    url = URL + "/" + user_id

    res = requests.get(url)
    username = res.json().get('username')

    link = url + "/todos"
    res = requests.get(link)
    tasks = res.json()

    data = {user_id: []}
    for task in tasks:
        data[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump(data, filename)
