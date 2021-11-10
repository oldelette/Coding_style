import gitlab                                                                                        
from gitlabb import GitlabFunction

def main():
    URL = 'https://gitlab.com'
    Token = 'q3pndvPbWNtTj-gEuJ3w'
    ID = 29664532
    
    gl = gitlab.Gitlab(URL, Token)
    project = gl.projects.get(ID)
    
    mygit = GitlabFunction(URL,ID,Token,"","","")
    tree = mygit.get_tree_list("","main")
    print(tree)

if __name__ == "__main__":
    main()
