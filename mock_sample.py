"""2021/11/17 unittest_example_code"""
import unittest
import gitlab
from gitlabb import GitlabFunction
from unittest import mock
from unittest.mock import MagicMock

class Project:
    class projects:
        def get(self):
            return Get
class Get:
    def repository_tree(self,myurl,mytoken):
        return 0

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
    
    """method1"""
    @mock.patch("gitlab.Gitlab")
    def test_con_success(self,mock_gitlab):
        """connected success"""
        mock_gitlab.return_value = Project()
        with mock.patch.object(Project, "projects", mock_gitlab):
            suc = GitlabFunction("", "", "", "", "", "")
            self.assertTrue(suc.connect_state)
    
    """method2"""
    #def test_con_success(self):
    #    """connected success"""
    #    mock_cursor = MagicMock(spec= self.FakeCursor)
    #    with mock.patch.object(gitlab, "Gitlab", mock_cursor):
    #        suc = GitlabFunction("", "", "", "", "", "")
    #        self.assertTrue(suc.connect_state)        

    def test_con_failed(self):
        """connected failed"""
        mock_gitlab_projects_get = MagicMock(
            side_effect=gitlab.GitlabAuthenticationError
        )
        with mock.patch.object(gitlab, "Gitlab", mock_gitlab_projects_get):
            get = GitlabFunction("", "", "", "", "", "")
            self.assertFalse(get.connect_state)
    
    @mock.patch("gitlab.Gitlab")
    def test_tree_list(self,mock_gitlab):
        items = [{'id': '5449ff610798d0b0065646cb4407a299257f4119', 'name': 'src', 'type': 'tree', 'path': 'src', 'mode': '040000'}, {'id': 'b14e2a93c1b7d787166b087eb789ea927d59a76e', 'name': 'test', 'type': 'tree', 'path': 'test', 'mode': '040000'}]
        tree_list = ['src','test']
        mock_gitlab.return_value = Project()
        mock_project_repository_tree = MagicMock(return_value = items)
        
        with mock.patch.object(Get,"repository_tree",mock_project_repository_tree):
            mytest = GitlabFunction("","","","","","")
            test_list = mytest.get_tree_list("","")
        self.assertEqual(test_list,tree_list)

if __name__ == "__main__":
    unittest.main()
