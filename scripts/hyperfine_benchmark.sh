#!/bin/bash

# Check if we're in the project root directory
if [ ! -f "pyproject.toml" ]; then
    echo "Error: Please run this script from the project root directory"
    echo "Current directory: $(pwd)"
    exit 1
fi

# Check if hyperfine is installed
if ! command -v hyperfine &> /dev/null; then
    echo "Hyperfine is not installed. Installing..."
    if command -v cargo &> /dev/null; then
        cargo install hyperfine
    else
        echo "Please install Rust and Cargo first, then run: cargo install hyperfine"
        exit 1
    fi
fi

# Parse command line arguments
SAVE_RESULTS=false
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --save) SAVE_RESULTS=true ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

# Test parameters
WARMUP=3 # Number of practice runs to stabilize the system (CPU frequency, caches, etc.)
MIN_RUNS=10 # Minimum number of measurements needed for statistical significance
MAX_RUNS=50 # Maximum number of measurements if more are needed for statistical significance
USERNAME="tiangolo" # GitHub username to test with

# Create benchmarks directory if saving results
if [ "$SAVE_RESULTS" = true ]; then
    mkdir -p benchmarks
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    RESULTS_FILE="benchmarks/benchmark_${TIMESTAMP}.json"
fi

echo "=== Running GitHub Activity CLI Benchmark with Hyperfine ==="
echo "Running from project root directory: $(pwd)"
echo "Using module directly: python -m github_activity"
if [ "$SAVE_RESULTS" = true ]; then
    echo "Results will be saved to $RESULTS_FILE"
    echo "Note: Consider adding benchmarks/ to .gitignore if this is a public repository"
fi

# Benchmark with different limits
echo -e "\n=== Benchmarking with different limits ==="
if [ "$SAVE_RESULTS" = true ]; then
    hyperfine \
        --warmup $WARMUP \
        --min-runs $MIN_RUNS \
        --max-runs $MAX_RUNS \
        --style full \
        --shell bash \
        --export-json "$RESULTS_FILE" \
        "python -m github_activity $USERNAME --limit 5" \
        "python -m github_activity $USERNAME --limit 10" \
        "python -m github_activity $USERNAME --limit 20" \
        "python -m github_activity $USERNAME --limit 50"
else
    hyperfine \
        --warmup $WARMUP \
        --min-runs $MIN_RUNS \
        --max-runs $MAX_RUNS \
        --style full \
        --shell bash \
        "python -m github_activity $USERNAME --limit 5" \
        "python -m github_activity $USERNAME --limit 10" \
        "python -m github_activity $USERNAME --limit 20" \
        "python -m github_activity $USERNAME --limit 50"
fi 