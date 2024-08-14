#!/usr/bin/python3
""" module to count words in a subreddit recursively """
import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list):
    """ does the actual counting """


    def fetch_posts(subreddit, after=None):
        """ fetches posts """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        params = {'after': after} if after else {}
        try:
            response = requests.get(url, headers=headers, params=params, allow_redirects=False)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    
    def process_titles(titles, keywords):
        """ processes the titles """
        keyword_counts = defaultdict(int)
        keyword_patterns = {re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE): word for word in keywords}

        for title in titles:
            for pattern, word in keyword_patterns.items():
                keyword_counts[word] += len(pattern.findall(title))

        return keyword_counts

    def recurse(subreddit, keywords, after=None, titles=[]):
        """ goes through the words """
        data = fetch_posts(subreddit, after)
        if data:
            posts = data.get('data', {}).get('children', [])
            if posts:
                titles.extend(post['data']['title'] for post in posts)
                after = data.get('data', {}).get('after')
                if after:
                    return recurse(subreddit, keywords, after, titles)
                else:
                    keyword_counts = process_titles(titles, keywords)
                    sorted_counts = sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        if count > 0:
                            print(f"{word.lower()}: {count}")
            else:
                return
        else:
            return
    
    # Ensure the word_list is a list of unique lowercase keywords
    word_list = list(set(word.lower() for word in word_list))
    recurse(subreddit, word_list)
