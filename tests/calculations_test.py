# System Modules
import sys
import os
import pytest
import pytest

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)
    def test_area_of_circle_negative_radius():
        """Test area_of_circle with a negative radius should raise ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            area_of_circle(-1)


    def test_get_nth_fibonacci_negative():
        """Test get_nth_fibonacci with negative n should raise ValueError."""
        with pytest.raises(ValueError, match="n cannot be negative"):
            get_nth_fibonacci(-5)


    def test_area_of_circle_large_radius():
        """Test area_of_circle with a large radius."""
        radius = 100
        result = area_of_circle(radius)
        assert abs(result - (math.pi * 100 ** 2)) < 1e-5


    def test_get_nth_fibonacci_two():
        """Test get_nth_fibonacci with n=2."""
        assert get_nth_fibonacci(2) == 1


    def test_get_nth_fibonacci_five():
        """Test get_nth_fibonacci with n=5."""
        assert get_nth_fibonacci(5) == 5
