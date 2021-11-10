import gitlab
from dataclasses import dataclass

@dataclass
class GitlabFunction:

    myurl: str 
    myid: str 
    mytoken: str 
    outpath: str 
    outfile: str 
    pydir: str 

    def __post_init__(self):
        self.connect_state = None

        try:
            self.project = gitlab.Gitlab(self.myurl,self.mytoken).projects.get(self.myid)
            self.connect_state = True
            print("Auth")
        except gitlab.GitlabGetError:
            print("ID error")
            self.connect_state = False
        except gitlab.GitlabAuthenticationError:
            print("token error")
            self.connect_state = False

    def get_tree_list(self,mypath:str,branch:str):
        items = self.project.repository_tree(path=mypath,ref=branch)
        tree_list = []
        for ind,value in enumerate(items):
            if items[ind]['type'] == 'tree':
                tree_list.append(value['name'])
            ind += 1
        return tree_list
