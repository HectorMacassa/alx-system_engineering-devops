#!/usr/bin/python3
"""This module provides a function to fetch the number of subscribers for a
given subreddit on Reddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit to fetch the subscriber count

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit
            is invalid or doesn't exist.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        # If the subreddit doesn't exist or the request fails, return 0
        return 0

    # If the response is a redirect to a search page, the subreddit doesn't
    # exist
    if response.url != url:
        return 0

    data = response.json()
    subscribers = data["data"]["subscribers"]

    return subscribers
