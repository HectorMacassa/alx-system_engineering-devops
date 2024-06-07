#!/usr/bin/python3
"""This module provides a function to recursively fetch hot article titles
from a given subreddit on Reddit using the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches the titles of hot articles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch hot articles from.
        hot_list (list, optional): The list to store the hot article titles.
            Default is None.
        after (str, optional): The fullname of the last item in the previous
            batch of results.

    Returns:
        list or None: A list of hot article titles if the subreddit exists,
            otherwise None.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, params=params,
                                headers={"User-Agent": "mozilla/5.0"})
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return None

    if response.url != url:
        return None

    data = response.json()
    children = data["data"]["children"]

    if not children:
        return hot_list

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data["data"].get("after")
    if after:
        hot_list = recurse(subreddit, hot_list, after)

    return hot_list
