#!/bin/bash

# Simple benchmark script to test Redis caching
# Make sure Redis is running first (e.g., using Docker)

USERNAME="tiangolo"  # GitHub username to test

echo "Starting simple Redis caching benchmark..."
echo "Using username: $USERNAME"
echo

echo "1. First Run (No Cache):"
time python -m github_activity $USERNAME

echo
echo "2. Second Run (With Cache):"
time python -m github_activity $USERNAME

echo
echo "3. Third Run (With Cache):"
time python -m github_activity $USERNAME

echo
echo "Done! The second and third runs should be much faster if Redis is working correctly."
echo "To start Redis in Docker: docker run --name redis -p 6379:6379 -d redis:alpine" 