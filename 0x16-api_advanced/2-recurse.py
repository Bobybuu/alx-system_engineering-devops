#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
     """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if "data" not in data or "children" not in data["data"]:
        return None

    children = data["data"]["children"]

    if not children:
        return hot_list

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data["data"]["after"]

    return recurse(subreddit, hot_list, after)

