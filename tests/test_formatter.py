"""Tests for the formatter module."""

from github_activity.formatter import format_event


def test_format_push_event():
    """Test formatting a PushEvent."""
    event = {
        "type": "PushEvent",
        "actor": {"login": "octocat"},
        "repo": {"name": "octocat/Hello-World"},
        "payload": {"commits": [{}, {}, {}]},
    }
    result = format_event(event)
    assert result == "- Pushed 3 commit(s) to octocat/Hello-World"


def test_format_create_event():
    """Test formatting a CreateEvent."""
    event = {
        "type": "CreateEvent",
        "actor": {"login": "octocat"},
        "repo": {"name": "octocat/Hello-World"},
        "payload": {"ref_type": "branch", "ref": "feature/new-feature"},
    }
    result = format_event(event)
    assert result == "- Created branch 'feature/new-feature' in octocat/Hello-World"


def test_format_watch_event():
    """Test formatting a WatchEvent."""
    event = {
        "type": "WatchEvent",
        "actor": {"login": "octocat"},
        "repo": {"name": "microsoft/vscode"},
    }
    result = format_event(event)
    assert result == "- Starred microsoft/vscode"


def test_unknown_event():
    """Test formatting an unknown event type."""
    event = {
        "type": "UnknownEvent",
        "actor": {"login": "octocat"},
        "repo": {"name": "octocat/Hello-World"},
    }
    result = format_event(event)
    assert result == "- UnknownEvent on octocat/Hello-World"
