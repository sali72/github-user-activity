#!/bin/bash
# Script to automate the release process

set -e

# Check if a version type is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 [major|minor|patch|current]"
    exit 1
fi

VERSION_TYPE=$1

# Ensure we're on the main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "Error: Must be on main branch to create a release."
    exit 1
fi

# Ensure working directory is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "Error: Working directory is not clean. Commit or stash changes first."
    exit 1
fi

# Pull latest changes
echo "Pulling latest changes from remote..."
git pull origin main

# Get current version
CURRENT_VERSION=$(grep -oP '__version__ = "\K[^"]+' github_activity/__init__.py)

# Bump version or use current
if [ "$VERSION_TYPE" = "current" ]; then
    NEW_VERSION=$CURRENT_VERSION
    echo "Using current version: $NEW_VERSION"
else
    echo "Bumping $VERSION_TYPE version..."
    python scripts/bump_version.py $VERSION_TYPE
    NEW_VERSION=$(grep -oP '__version__ = "\K[^"]+' github_activity/__init__.py)
    
    # Commit version change
    git add github_activity/__init__.py
    git commit -m "Bump version to $NEW_VERSION"
fi

# Create tag
git tag -a "v$NEW_VERSION" -m "Release v$NEW_VERSION"

# Push changes and tag
echo "Pushing changes and tag to remote..."
git push origin main
git push origin "v$NEW_VERSION"

echo "Release v$NEW_VERSION created and pushed."
echo "GitHub Actions will now:"
echo "1. Run tests"
echo "2. Build the package"
echo "3. Create a GitHub release"
echo "4. Publish to PyPI (if configured)"
echo
echo "Check the progress at: https://github.com/$(git config --get remote.origin.url | sed -E 's/.*github.com[:\/](.*)(\.git)?/\1/')/actions" 