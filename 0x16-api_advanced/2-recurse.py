#!/usr/bin/python3
"""
2-recurse
"""
import requests
a = None


def recurse(subreddit, hot_list=[]):
    """
    queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    global a
    agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': a}
    results = requests.get(url, params=parameters, headers=agent,
                           allow_redirects=False)

    if results.status_code == 200:
        a_d = results.json().get("data").get("after")
        if a_d is not None:
            a = a_d
            recurse(subreddit, hot_list)
        ts = results.json().get("data").get("children")
        for title_ in ts:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
