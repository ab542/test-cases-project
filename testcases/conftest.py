"""Pytest configuration and fixtures for the test suite."""

import pytest


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "unit: mark unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: mark integration tests"
    )
