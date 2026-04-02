"""Example unit test."""
import pytest


@pytest.mark.unit
def test_basic_addition():
    """Test basic addition works correctly."""
    assert 1 + 1 == 2


@pytest.mark.unit
def test_list_contains():
    """Test list membership check."""
    colors = ["red", "green", "blue"]
    assert "green" in colors
    assert "yellow" not in colors


@pytest.mark.unit
def test_string_operations():
    """Test string operations."""
    text = "Hello, World!"
    assert text.upper() == "HELLO, WORLD!"
    assert text.startswith("Hello")
