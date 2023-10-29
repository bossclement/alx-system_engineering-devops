#!/usr/bin/python3

"""
1-top_ten
"""

from requests import get


def top_ten(subreddit):
    """
    unction that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    res = get(url, headers=agent, params=params).json()

    try:
        data = res.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
