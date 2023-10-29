#!/usr/bin/python3
"""
0-subs
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    ueries the Reddit API and returns the number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = get(url, headers=agent).json()

    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0
