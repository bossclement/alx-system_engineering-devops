#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    link = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(link)
    users = res.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = link + '/todos/'
        res = requests.get(url)
        tasks = res.json()
        data[user_id] = []
        for task in tasks:
            data[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
