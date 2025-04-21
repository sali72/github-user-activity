# GitHub User Activity CLI

A command-line tool to fetch and display recent activity of a GitHub user.

## Features

- Fetch recent activity of any GitHub user
- Display activity in a human-readable format
- Handle errors gracefully
- Limit the number of events displayed

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity
```

2. Install the package:
```bash
pip install .
```

3. For development (includes pytest):
```bash
pip install ".[dev]"
```

## Usage

```bash
# Display recent activity for a GitHub user
github-activity <username>

# Display only the 5 most recent events
github-activity <username> --limit 5

# Show help
github-activity --help

# Show version
github-activity --version
```

### Example

```bash
$ github-activity octocat
Recent activity for GitHub user 'octocat':

- Pushed 3 commit(s) to octocat/Hello-World
- Opened issue #123 in octocat/Hello-World
- Created branch 'feature/new-feature' in octocat/Hello-World
- Starred microsoft/vscode
```

## Development

### Requirements

- Python 3.6+

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/github-user-activity.git
cd github-user-activity

# Install in development mode with testing dependencies
pip install ".[dev]"
```

### Project Structure

This project uses modern Python packaging with `pyproject.toml` for configuration, following PEP 621 standards. No `setup.py` file is needed.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=github_activity
```

## License

MIT