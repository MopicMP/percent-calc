"""Tests for percent-calc."""

import pytest
from percent_calc import calc


class TestCalc:
    """Test suite for calc."""

    def test_basic(self):
        """Test basic usage."""
        result = calc("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            calc("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = calc(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
