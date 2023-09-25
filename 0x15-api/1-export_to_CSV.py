#!/usr/bin/python3
"""Script that sends a get request to a REST API"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/users"
    link = URL + "/" + user_id

    res = requests.get(link)
    username = res.json().get('username')

    dourl = link + "/todos"
    res = requests.get(dourl)
    tasks = res.json()

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
