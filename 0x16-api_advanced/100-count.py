#!/usr/bin/python3
"""This module provides a function to recursively fetch hot article titles
from a given subreddit on Reddit and print a sorted count of given keywords.
"""
import re
import requests

def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively fetches hot article titles from a given subreddit,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to fetch hot articles from.
        word_list (list): A list of keywords to count in the article titles.
        word_count (dict, optional): A dictionary to store the keyword counts.
            Default is None.
        after (str, optional): The fullname of the last item in the previous
            batch of results.

    Returns:
        None
    """
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, params=params,
                                 headers={"User-Agent": "mozilla/5.0"})
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return

    if response.url != url:
        return

    data = response.json()
    children = data["data"]["children"]

    if not children:
        print_word_count(word_count)
        return

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            word_pattern = fr"\b{word.lower()}\b"
            word_count[word.lower()] += len(re.findall(word_pattern, title))

    after = data["data"].get("after")
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        print_word_count(word_count)

def print_word_count(word_count):
    """
    Prints the sorted word count.

    Args:
        word_count (dict): A dictionary containing the keyword counts.
    """
    sorted_words = sorted((count, word)
                           for word, count in word_count.items()
                           if count > 0)
    sorted_words.sort(key=lambda x: (-x[0], x[1]))

    for count, word in sorted_words:
        print(f"{word}: {count}")
