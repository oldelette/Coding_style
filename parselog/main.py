"""main function"""
import gitlab
import os

from libs.func import black
from libs.config import URL, PRIVATE, PROJECT_ID, BRANCH_CHECK, GITLAB_PATH, PY_DIR


def main():
    gl = gitlab.Gitlab(URL, PRIVATE)
    project = gl.projects.get(PROJECT_ID)
    # print(project)

    blob_list = []
    items = project.repository_tree(path="src/", ref=BRANCH_CHECK)
    for unit in items:
        if unit["type"] == "blob":
            blob_list.append(unit["name"])
    print("blob list: ", blob_list)

    """Filter the python file from blob"""

    python_list = []
    for blo in blob_list:
        if blo[-3:] == ".py":
            python_list.append(blo)
    print("python list: ", python_list)

    if os.path.isdir(PY_DIR) == False:
        os.mkdir(PY_DIR)

    """ Get the file on local dir"""

    ind = 0
    for pfile in python_list:
        raw_content = project.files.raw(
            file_path=GITLAB_PATH + python_list[ind], ref=BRANCH_CHECK
        )
        # print(raw_content)
        fw = open(PY_DIR + python_list[ind], "wb")
        fw.write(raw_content)
        fw.close()
        ind += 1

    # check list: pylint -> flake8 ->black
    # state = coding_style(python_list)

    """Black revise and Commit back to Gitlab"""

    for bla in python_list:
        sta = black(PY_DIR + bla)
        file_content = open(PY_DIR + bla).read()
        if not sta:
            print("Ready to revise code and commit: ", bla)
            file_check = project.files.get(
                file_path=GITLAB_PATH + bla, ref=BRANCH_CHECK
            )
            file_check.content = file_content
            file_check.save(
                branch=BRANCH_CHECK, commit_message="Update error file: " + bla
            )
        else:
            print("Not need to revise code: ", bla)

    commits = project.commits.list(ref_name=BRANCH_CHECK)
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
