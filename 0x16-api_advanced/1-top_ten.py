#!/usr/bin/python3
"""
This module provides a function to print the titles of the first 10 hot
posts listed for a given subreddit on Reddit using the Reddit API.
"""
import requests
from requests.utils import requote_uri


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch hot posts from.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(None)
            return
        else:
            raise e

    if response.is_redirect:
        redirect_url = requote_uri(response.headers['Location'])
        if redirect_url != url:
            print(None)
            return

    try:
        data = response.json()
    except ValueError:
        print("Error parsing JSON response")
        return

    children = data.get("data", {}).get("children", [])
    if not children:
        print("No hot posts found.")
        return

    for child in children:
        post_data = child.get("data", {})
        title = post_data.get("title", "No title found")
        print(title)
