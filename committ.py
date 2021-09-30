import subprocess
import gitlab
import os
from func import *

project_ID = 29664532
url = "https://gitlab.com"
privatet = "sQasQTVXrKscrFVLtZXR"

path = "/home/gavin/gavin/codint_style/"

gl = gitlab.Gitlab(url, privatet)
project = gl.projects.get(project_ID)
# print(project)

""" Get a file"""
"""
f = project.files.get(file_path="aa.py", ref="main")
fout = open("sample.txt", "wb")
fout.write(f.decode())
fout.close()
"""

full_path=path+"maxline.py"
flag = black(full_path)
#print(full_path)
#print(flag)
file_content = open(full_path).read()

"""
if flag:
    print("no need recommit to repo")
else:
"""
print("--" * 20)

"""Update a file"""
file_check = project.files.get(file_path="maxline.py", ref="main")
file_check.content = file_content
file_check.save(branch="main",commit_message='Update error file')

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

# commits = project.commits.list(ref_name="main")
# print(commits)

"""
data = {
    'branch_name': 'main',
    'commit_message': 'blah blah blah',
    'actions': [
        {
            'action': 'create',
            'file_path': 'com/test',
            'content': 'blah'
        }
    ]
}
commit = project.commits.create(data)
"""