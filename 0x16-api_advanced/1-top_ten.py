#!/usr/bin/python3
""" Function that return top ten posts on a subreddit."""
import requests

def top_ten(subreddit):
    """ fetches the title of the top to hettest posts. """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
         "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/binini_)"
    }
    params = {
          "limit": 10
    }

    response = response.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404;
           print("None")
           return
    result = response.json().get("data")\
    [print(c.get("data").get("title")) for c in result.get("children")]
