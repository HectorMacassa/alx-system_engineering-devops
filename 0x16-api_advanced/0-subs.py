#!/usr/bin/python3
"""
Module for querying the number of subscribers on a subreddit.

This module provides a function to retrieve the number of subscribers
for a given subreddit using the Reddit API.
"""
import requests
from requests.exceptions import RequestException


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the given subreddit.
             Returns 0 if an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except RequestException:
        return 0
    else:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
