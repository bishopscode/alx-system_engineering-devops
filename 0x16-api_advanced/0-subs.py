#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int or None: The number of subscribers if successful, None otherwise.
    """
    if not isinstance(subreddit, str):
        raise ValueError("Subreddit must be a string")

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise HTTPError for bad status codes
        data = response.json()
        return data.get('data', {}).get('subscribers')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except KeyError as e:
        print(f"KeyError: {e}")
        return None

# Example usage:
# print(number_of_subscribers("python"))  # Uncomment this line to test the function
