#!/usr/bin/python3
"""
Script that queries number of subscribers on subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
