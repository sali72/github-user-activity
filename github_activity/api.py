"""Module for interacting with the GitHub API."""

import urllib.request
import urllib.error
import json
from typing import Dict, List, Any

# Import our simple cache functions
from github_activity.cache import get as cache_get, set as cache_set


def fetch_user_events(username: str) -> List[Dict[str, Any]]:
    """
    Fetch the recent GitHub events for a user.
    
    Args:
        username: GitHub username
        
    Returns:
        List of events as dictionaries
        
    Raises:
        ValueError: If the username is invalid or the API request fails
    """
    # Try to get data from cache first
    cached_data = cache_get(username)
    if cached_data is not None:
        return cached_data
    
    # If not in cache, fetch from GitHub API
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        "User-Agent": "GitHub-User-Activity-CLI",
        "Accept": "application/vnd.github.v3+json",
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                events = json.loads(response.read().decode("utf-8"))
                
                # Store in cache for future requests
                cache_set(username, events)
                
                return events
            else:
                raise ValueError(f"Failed to fetch events: HTTP {response.status}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f"User '{username}' not found.")
        else:
            raise ValueError(f"API request failed: {e.reason}")
    except urllib.error.URLError as e:
        raise ValueError(f"Connection error: {e.reason}")
    except json.JSONDecodeError:
        raise ValueError("Invalid response from GitHub API.") 