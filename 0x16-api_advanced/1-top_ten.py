#!/usr/bin/python3
"""This module provides a function to print the titles of the first 10 hot
posts listed for a given subreddit on Reddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch hot posts from.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        response = requests.get(url, headers={"User-Agent": "mozilla/5.0"})
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(None)
        return

    if response.url != url:
        print(None)
        return

    data = response.json()
    children = data["data"]["children"]

    if not children:
        print("No hot posts found.")
        return

    for child in children:
        print(child["data"]["title"])
