# System Modules
import sys
import os
import unittest
import math


# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

class TestCalculations(unittest.TestCase):
    def test_area_of_circle_positive_radius(self):
        """Test with a positive radius."""
        # Arrange
        radius = 1

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertAlmostEqual(result, math.pi, places=5)


    def test_area_of_circle_zero_radius(self):
        """Test with a radius of zero."""
        # Arrange
        radius = 0

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertEqual(result, 0)


    def test_area_of_circle_negative_radius(self):
        """Test with a negative radius to raise ValueError."""
        # Arrange
        radius = -1

        # Act & Assert
        with self.assertRaises(ValueError):
            area_of_circle(radius)


    def test_area_of_circle_float_radius(self):
        """Test with a float radius."""
        # Arrange
        radius = 2.5

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertAlmostEqual(result, math.pi * 2.5 ** 2, places=5)


    def test_area_of_circle_non_numeric(self):
        """Test with non-numeric radius to raise TypeError."""
        # Act & Assert
        with self.assertRaises(TypeError):
            area_of_circle("a")


    def test_get_nth_fibonacci_zero(self):
        """Test with n=0."""
        # Arrange
        n = 0

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 0)


    def test_get_nth_fibonacci_one(self):
        """Test with n=1."""
        # Arrange
        n = 1

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 1)


    def test_get_nth_fibonacci_ten(self):
        """Test with n=10."""
        # Arrange
        n = 10

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 55)


    def test_get_nth_fibonacci_large(self):
        """Test with a large n."""
        # Arrange
        n = 20

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 6765)


    def test_get_nth_fibonacci_negative(self):
        """Test with a negative number to raise ValueError."""
        # Arrange
        n = -1

        # Act & Assert
        with self.assertRaises(ValueError):
            get_nth_fibonacci(n)


    def test_get_nth_fibonacci_non_numeric(self):
        """Test with non-numeric n to raise TypeError."""
        # Act & Assert
        with self.assertRaises(TypeError):
            get_nth_fibonacci("a")

if __name__ == '__main__':
    unittest.main()
