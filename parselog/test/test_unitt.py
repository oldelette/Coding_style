"""unittest_example_code"""
import unittest
from libs.func import judge, black


class TestCal(unittest.TestCase):
    """class TestCase"""

    def setUp(self):
        """before test setting"""
        self.cmd1 = "ls"
        self.cmd2 = "aa"

    def tearDown(self):
        """after test setting"""

    def test_judge(self):
        """test judge"""
        res1 = judge(self.cmd1)
        res2 = judge(self.cmd2)
        self.assertTrue(res1)
        self.assertFalse(res2)


if __name__ == "__main__":
    unittest.main()
