#!/usr/bin/python3
""" module for recursively querying reddit """
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ funcition to get hot list of subreddits """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            if posts:
                for post in posts:
                    hot_list.append(post['data']['title'])

                after = data['data'].get('after')

                if after:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
