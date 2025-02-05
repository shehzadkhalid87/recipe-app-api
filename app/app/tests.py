"""
Unit tests for calculator functions.
"""

import unittest
from app.calc import add, multiply


class TestCalc(unittest.TestCase):
    """Test the calculator functions."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
