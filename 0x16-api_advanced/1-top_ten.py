#!/usr/bin/python3
"""
Module for retrieving the top 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
   """
   Prints the titles of the first 10 hot posts for a given subreddit.
   If the subreddit is invalid, prints None.
   """
   url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
   headers = {"User-Agent": "Mozilla/5.0"}

   try:
       response = requests.get(url, headers=headers, allow_redirects=False)
       response.raise_for_status()
   except requests.exceptions.HTTPError:
       # Invalid subreddit or other HTTP error
       print(None)
       return

   data = response.json()

   if "data" in data and "children" in data["data"]:
       for post in data["data"]["children"]:
           if "data" in post and "title" in post["data"]:
               print(post["data"]["title"])
   else:
       print(None)
