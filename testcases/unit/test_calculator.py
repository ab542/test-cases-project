"""Tests for the Calculator class."""
import pytest
from src.calculator import Calculator


@pytest.mark.unit
class TestCalculator:
    """Test cases for Calculator."""

    def setup_method(self):
        """Create calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 5) == -4

    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0

    def test_divide(self):
        """Test division."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)
