#!/usr/bin/python3
""" module for checking top ten reddit posts """
import requests


def top_ten(subreddit):
    """ function to get top ten posts in a subreddit """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for i in range(min(10, len(posts))):
                print(posts[i]['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(f"An error occurred: {e}")
        print(None)
