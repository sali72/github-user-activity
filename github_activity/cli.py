"""Command-line interface for GitHub User Activity."""

import sys
import argparse
from typing import List, Optional

from github_activity import __version__
from github_activity.api import fetch_user_events
from github_activity.formatter import display_events


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Args:
        args: List of command-line arguments
        
    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="Fetch and display recent activity of a GitHub user."
    )
    
    parser.add_argument(
        "username",
        help="GitHub username"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=10,
        help="Limit the number of events to display (default: 10)"
    )
    
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        args: List of command-line arguments
        
    Returns:
        Exit code
    """
    try:
        parsed_args = parse_args(args)
        username = parsed_args.username
        limit = parsed_args.limit
        
        events = fetch_user_events(username)
        display_events(events[:limit], username)
        
        return 0
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main()) 