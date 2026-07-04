"""Unit tests for application."""

from application import TestMe


def test_server():
    """Test take_five method."""
    assert TestMe().take_five() == 5


def test_port():
    """Test application port."""
    assert TestMe().port() == 8000
