#!/bin/bash

# Simple script to start Redis in Docker

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Start Redis container
echo "Starting Redis in Docker..."
docker run --name redis -p 6379:6379 -d --rm redis:alpine

echo "Redis started on localhost:6379"
echo "To stop Redis: docker stop redis" 