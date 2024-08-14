#!/usr/bin/python3
""" module for checking number of subs in a subreddit """
import requests


def number_of_subscribers(subreddit):
    """funciton to check number of subs in a subreddit """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
