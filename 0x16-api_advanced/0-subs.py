#!/usr/bin/python3
"""
Module for retrieving the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
   """
   Returns the number of subscribers for a given subreddit.
   If the subreddit is invalid, returns 0.
   """
   url = f"https://www.reddit.com/r/{subreddit}/about.json"
   headers = {"User-Agent": "Mozilla/5.0"}

   try:
       response = requests.get(url, headers=headers, allow_redirects=False)
       response.raise_for_status()
   except requests.exceptions.HTTPError:
       return 0

   data = response.json()

   if "data" in data and "subscribers" in data["data"]:
       return data["data"]["subscribers"]
   else:
       return 0
