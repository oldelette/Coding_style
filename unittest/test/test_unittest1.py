"""unittest_example_code"""
import unittest
from src.calc import add, substract


class TestCal(unittest.TestCase):
    """class TestCase"""

    def setUp(self):
        """before test setting"""
        self.num1 = 10
        self.num2 = 4

    def tearDown(self):
        """after test setting"""

    def test_add(self):
        """test1"""
        result = add(self.num1, self.num2)
        self.assertEqual(result, 14)

    def test_sub(self):
        """test2"""
        result = substract(self.num1, self.num2)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
