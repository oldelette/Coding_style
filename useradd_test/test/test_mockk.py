"""unittest_example_code"""
import unittest
from unittest import mock
from src.useradd import run_sudo_command,check,cmd_list


class TestSsh(unittest.TestCase):
    """class TestCase"""

    def setUp(self):
        """before setting"""

    def tearDown(self):
        """after test setting"""

    def test_cmdsuccess(self):
        """test1"""
        mock_success_value = 1
        run_sudo_command = mock.Mock(return_value=mock_success_value)
        #assert check(1) == 1
        self.assertEqual(check(1),True)

    def test_cmderror(self):
        """test2"""
        mock_success_value = 0
        run_sudo_command = mock.Mock(return_value=mock_success_value)
        #assert check(0) == 0
        self.assertEqual(check(0),False)

    def test_cmdlist(self):
        self.assertEqual(len(cmd_list()),3)
        #self.assertNotEqual(len(cmd_list()),0)

if __name__ == "__main__":
    unittest.main()
