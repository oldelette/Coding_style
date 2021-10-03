""" Gitlab API  code"""
from func import *
from config import *


def main():
    gl = gitlab.Gitlab(url, privatet)
    project = gl.projects.get(project_ID)
    # print(project)

    blob_list = []
    items = project.repository_tree(path=gitlab_path, ref=branch_check)
    for unit in items:
        if unit["type"] == "blob":
            blob_list.append(unit["name"])
    print("blob list: ", blob_list)

    """Filter the python file from blob"""
    """
    python_list = []
    for blo in blob_list:
        if blo[-3:] == ".py":
            python_list.append(blo)
    print("python list: ", python_list)

    if os.path.isdir(py_dir) == False:
        os.mkdir(py_dir)
    """

    """Get the file on local dir"""
    """
    ind=0
    for pfile in python_list:
	raw_content = project.files.raw(file_path=gitlab_path+python_list[ind], ref=branch_check)
	#print(raw_content)
	fw=open(py_dir+python_list[ind],"wb")
	fw.write(raw_content)
	fw.close()
	ind+=1
    """
    # check list: pylint -> flake8 ->black
    # state = coding_style(python_list)
    """Black revise and Commit back to Gitlab"""
    """
    for bla in python_list:
	sta=black(py_dir+bla)
	file_content = open(py_dir+bla).read()
	#print(file_content)
	if not sta:
	    print("Ready to revise code and commit: ", bla)
	    file_check = project.files.get(file_path=gitlab_path+bla, ref=branch_check)
	    file_check.content = file_content
	    file_check.save(branch=branch_check,commit_message='Update error file: '+bla)
	else:
	    print("Not need to revise code: ",bla)
    """

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

    if user_id != 0:
        issue = project.issues.create(
            {
                "title": "revise code",
                "assignee_id": user_id,
                "description": "Please check coding style",
            }
        )
        issues = gl.issues.list(state="opened")
        print("Success create new Issue, Issue ID: ", issues[0].iid)


if __name__ == "__main__":
    main()
