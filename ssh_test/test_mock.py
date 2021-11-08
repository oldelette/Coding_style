"""unittest_example_code"""
import unittest
from my_ssh import SSH                                                                               
from unittest import mock 
from unittest.mock import MagicMock

class TestCal(unittest.TestCase):
    """class TestCase"""

    def setUp(self):
        """before test setting"""
        self.num1 = 10

    def test_connect_success(self):
        """test connect"""
        ssh_connecnt = MagicMock()
        #result = 
        #self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
