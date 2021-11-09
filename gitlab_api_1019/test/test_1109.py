"""unittest_example_code"""
import unittest
import gitlab
from gitlabb import GitlabFunction
from unittest import mock
from unittest.mock import MagicMock


class TestClass(unittest.TestCase):
    """class TestCase"""
    class FakeCursor(object):
        NAME = 'spec'
        def __init__(self):
            self.test = ""
        def projects(self):
            return 0
    
    def setUp(self):
        """before test setting"""
    
    def test_con_success(self):
        """connected success"""
        mock_cursor = MagicMock(spec= self.FakeCursor)
        with mock.patch.object(gitlab, "Gitlab", mock_cursor):
            suc = GitlabFunction("", "", "", "", "", "")
            self.assertTrue(suc.connect_state)
            

    def test_con_failed(self):
        """connected failed"""
        mock_gitlab_projects_get = MagicMock(
            side_effect=gitlab.GitlabAuthenticationError
        )
        with mock.patch.object(gitlab, "Gitlab", mock_gitlab_projects_get):
            get = GitlabFunction("", "", "", "", "", "")
            self.assertFalse(get.connect_state)
    
    @mock.patch("gitlabb.get_tree_list")
    def test_tree_list(self):
        mock_tree_list.return_value = ['src','test']
        mytest = GitlabFunction("https://gitlab.com","q3pndvPbWNtTj-gEuJ3w",29664532,"","","")
        res = mytest.get_tree_list("","")
        #self.assertEqual()

        #mock_cursor = MagicMock(spec= self.FakeCursor)
        #with mock.patch.object(gitlab, "Gitlab", mock_cursor):
        #    myyytest = GitlabFunction("","","","","","")
        #    mock = mytest.get_tree_list("","")
        
        # self.assertEqual()


if __name__ == "__main__":
    unittest.main()
