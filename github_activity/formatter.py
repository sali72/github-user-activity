"""Module for formatting GitHub event data."""

from typing import Dict, List, Any


def format_event(event: Dict[str, Any]) -> str:
    """
    Format a GitHub event into a human-readable string.
    
    Args:
        event: Event dictionary from GitHub API
        
    Returns:
        Formatted string describing the event
    """
    event_type = event.get("type", "Unknown")
    repo = event.get("repo", {}).get("name", "Unknown repository")
    
    if event_type == "PushEvent":
        commits = event.get("payload", {}).get("commits", [])
        return f"- Pushed {len(commits)} commit(s) to {repo}"
    
    elif event_type == "CreateEvent":
        ref_type = event.get("payload", {}).get("ref_type", "Unknown")
        ref = event.get("payload", {}).get("ref", "")
        if ref:
            return f"- Created {ref_type} '{ref}' in {repo}"
        else:
            return f"- Created {ref_type} in {repo}"
    
    elif event_type == "IssuesEvent":
        action = event.get("payload", {}).get("action", "Unknown")
        issue_number = event.get("payload", {}).get("issue", {}).get("number", "?")
        return f"- {action.capitalize()} issue #{issue_number} in {repo}"
    
    elif event_type == "IssueCommentEvent":
        action = event.get("payload", {}).get("action", "Unknown")
        issue_number = event.get("payload", {}).get("issue", {}).get("number", "?")
        return f"- {action.capitalize()} comment on issue #{issue_number} in {repo}"
    
    elif event_type == "PullRequestEvent":
        action = event.get("payload", {}).get("action", "Unknown")
        pr_number = event.get("payload", {}).get("pull_request", {}).get("number", "?")
        return f"- {action.capitalize()} pull request #{pr_number} in {repo}"
    
    elif event_type == "WatchEvent":
        return f"- Starred {repo}"
    
    elif event_type == "ForkEvent":
        return f"- Forked {repo}"
    
    else:
        return f"- {event_type} on {repo}"


def format_events(events: List[Dict[str, Any]]) -> List[str]:
    """
    Format a list of GitHub events into human-readable strings.
    
    Args:
        events: List of events from GitHub API
        
    Returns:
        List of formatted strings
    """
    return [format_event(event) for event in events]


def display_events(events: List[Dict[str, Any]], username: str) -> None:
    """
    Display formatted GitHub events in the terminal.
    
    Args:
        events: List of events from GitHub API
        username: GitHub username
    """
    if not events:
        print(f"No recent activity found for user '{username}'.")
        return
    
    formatted_events = format_events(events)
    print(f"Recent activity for GitHub user '{username}':")
    print()
    for event in formatted_events:
        print(event) 