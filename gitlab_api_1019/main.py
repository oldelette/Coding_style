import subprocess
import gitlab
import os

from func import Quality
from config import *

import argparse


def get_parser():
    parser = argparse.ArgumentParser(description="my description")
    parser.add_argument(
        '-u',"--URL", default="https://gitlab.com", type=str, help="gitlab website URL"
    )
    parser.add_argument(
        '-i',"--ID", default="30157467", type=int, help="the scan project ID"
    )
    parser.add_argument(
        '-t',"--token",
        default="q3pndvPbWNtTj-gEuJ3w",
        type=str,
        help="your own private token",
    )
    parser.add_argument(
        '-b',"--branch", default="main", type=str, help="the scan project branch"
    )
    parser.add_argument('-g','--gitpath', default='src/', type=str,help="the scan project directory")
    parser.add_argument('-d','--pydir', default='Check_python/', type=str,help="local of python file location")
    return parser


def main():
    method = Quality()
    parser = get_parser()
    args = parser.parse_args()
    # print(args.URL,args.ID)
    #gl = gitlab.Gitlab(url, privatet)
    gl = gitlab.Gitlab(args.URL, args.token)
    project = gl.projects.get(args.ID)
    # print(project)

    blob_list = []
    items = project.repository_tree(path=args.gitpath, ref=args.branch)
    for unit in items:
        if unit["type"] == "blob":
            blob_list.append(unit["name"])
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
    ind = 0
    for pfile in python_list:
        raw_content = project.files.raw(
            file_path=args.gitpath + python_list[ind], ref=args.branch
        )
        # print(raw_content)
        fw = open(args.pydir + python_list[ind], "wb")
        fw.write(raw_content)
        fw.close()
        ind += 1

    # check list: pylint -> flake8 ->black
    state = method.coding_style(python_list)

    """Black revise and Commit back to Gitlab"""
#    for bla in python_list:
#        sta = method.black(py_dir + bla)
#        file_content = open(py_dir + bla).read()
#        # print(file_content)
#        if not sta:
#            print("Ready to revise code and commit: ", bla)
#            file_check = project.files.get(
#                file_path=gitlab_path + bla, ref=branch_check
#            )
#            file_check.content = file_content
#            file_check.save(
#                branch=branch_check, commit_message="Update error file: " + bla
#            )
#        else:
#            print("Not need to revise code: ", bla)

    commits = project.commits.list(ref_name=branch_check)
    print("Latest commit id:", commits[0].id)
    print("Latest commit user:", commits[0].committer_name)

    """Get user ID"""
    try:
        users = gl.users.list(search=commits[0].committer_name)
        user_id = users[0].id
        print("Committer user ID:  ", user_id)
    except:
        print("Committer user ID not found")
        user_id = 0

    """Current user"""
    """
    gl.auth()
    current_user = gl.user
    print(current_user)
    """

    """Create Issues"""
    # issues = gl.issues.list(state='opened')
    # print(issues[0].iid)
    """ 
    if user_id!=0:
        issue = project.issues.create({'title': 'revise code','assignee_id':user_id,'description': 'Please check coding style'})
        issues = gl.issues.list(state='opened')
        print("Success create new Issue, Issue ID: ",issues[0].iid)
    """


if __name__ == "__main__":
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
