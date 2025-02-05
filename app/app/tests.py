"""
 sample tests
 """
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """test the calc Module"""
    def test_add_numbers(self):
        """Test the adding numbers togather"""
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_multiply_numbers(self):
        """multiply x and y and return result."""
        res = calc.multiply(2,4)
        self.assertEqual(res,8)
