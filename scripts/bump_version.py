#!/usr/bin/env python
"""
Version bumping script.
Usage: python scripts/bump_version.py [major|minor|patch]
"""

import re
import sys
from pathlib import Path

def bump_version(version_type):
    """Bump the version in __init__.py."""
    init_file = Path("github_activity/__init__.py")
    content = init_file.read_text()
    
    # Extract current version
    match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if not match:
        print("Error: Could not find version string in github_activity/__init__.py")
        return False
    
    current_version = match.group(1)
    major, minor, patch = map(int, current_version.split('.'))
    
    # Bump version
    if version_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif version_type == "minor":
        minor += 1
        patch = 0
    elif version_type == "patch":
        patch += 1
    else:
        print(f"Error: Unknown version type '{version_type}'. Use 'major', 'minor', or 'patch'.")
        return False
    
    new_version = f"{major}.{minor}.{patch}"
    new_content = re.sub(
        r'__version__ = ["\']([^"\']+)["\']',
        f'__version__ = "{new_version}"',
        content
    )
    
    # Write updated version
    init_file.write_text(new_content)
    print(f"Updated version from {current_version} to {new_version}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["major", "minor", "patch"]:
        print("Usage: python scripts/bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    if not bump_version(sys.argv[1]):
        sys.exit(1) 