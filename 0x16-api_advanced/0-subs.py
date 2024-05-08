#!/usr/bin/python3

"""
This module contains a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if successful, 0 otherwise.
    """
    if not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
    except KeyError as e:
        print(f"KeyError: {e}")
        return 0
