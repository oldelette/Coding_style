import subprocess
import gitlab
import os

from func import *
from config import *


def main():
    gl = gitlab.Gitlab(url, privatet)
    project = gl.projects.get(project_ID)
    # print(project)

    blob_list = []
    items = project.repository_tree(path='src/', ref='main')
    for unit in items:
        if unit['type'] == 'blob':
            blob_list.append(unit['name'])
    print("blob list: ", blob_list)

    """ Filter the python file from blob"""

    python_list = []
    for blo in blob_list:
        if blo[-3:] == ".py":
            python_list.append(blo)
    print("python list: ", python_list)

    if os.path.isdir(py_dir) == False:
        os.mkdir(py_dir)

    """ Get the file on local dir"""
    """
    ind=0
    for pfile in python_list:
	raw_content = project.files.raw(file_path=gitlab_path+python_list[ind], ref='main')
	#print(raw_content)
	fw=open(py_dir+python_list[ind],"wb")
	fw.write(raw_content)
	fw.close()
	ind+=1
    """
    # check list: pylint -> flake8 ->black
    #state = coding_style(python_list)
    """Black revise and Commit back to Gitlab"""
    """
    for bla in python_list:
	sta=black(py_dir+bla)
	file_content = open(py_dir+bla).read()
	#print(file_content)
	if not sta:
	    print("Ready to revise code and commit: ", bla)
	    file_check = project.files.get(file_path=gitlab_path+bla, ref="main")
	    file_check.content = file_content
	    file_check.save(branch="main",commit_message='Update error file: '+bla)
		
	else:
	    print("Not need to revise code: ",bla)
    """

    commits = project.commits.list(ref_name="main")
    print("Latest commit id:", commits[0].id)
    print("Latest commit user:", commits[0].committer_name)

    """Get user ID"""
    try:
        users = gl.users.list(search=commits[0].committer_name)
        print("Committer user ID:  ", users[0].id)
    except:
        print("Committer user ID not found")

    """Current user"""
    """
    gl.auth()
    current_user = gl.user
    print(current_user)
    """

    """Create Issues"""
    #issues = gl.issues.list(state='opened')
    # print(issues)
    #issue = project.issues.create({'title': 'testbug','assignee_id':9636470,'description': 'python-gitlab.'})


if __name__ == '__main__':
    main()


""" Get a file"""
"""
f = project.files.get(file_path=gitlab_path, ref="main")
fout = open("sample.txt", "wb")
fout.write(f.decode())
fout.close()
"""

"""
full_path=path+"maxline.py"
flag = black(full_path)
#print(full_path)
#print(flag)
file_content = open(full_path).read()
"""

"""
if flag:
    print("no need recommit to repo")
else:
"""

"""Update a file"""
"""
file_check = project.files.get(file_path="maxline.py", ref="main")
file_check.content = file_content
file_check.save(branch="main",commit_message='Update error file')
"""


"""Create a new file"""
"""
commit_file = project.files.create(
    {
        "file_path": "testfile.txt",
        "branch": "main",
        "content": file_content,
        "author_email": "mcleezs@tsmc.com",
        "author_name": "mcleezs",
        "commit_message": "Create testfile",
    }
)
"""

