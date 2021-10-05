import subprocess
import gitlab
import os
import time

from config import *

gl = gitlab.Gitlab(url, privatet)
start_time = time.time()

def get_issue(pro_id):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")
    project = gl.projects.get(pro_id)
    issues = project.issues.list()
    #print(issues)
    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")


def main():
    #projects = gl.projects.list(owned=True)
    projects = gl.projects.list()
    #print(projects[0])
    pro_len=len(projects)
    print(pro_len)


    for pro in projects:
        #get_issue(pro)
        #project = gl.projects.get(pro)
        #print(pro.id)
        get_issue(pro.id)
    
    

if __name__ == '__main__':
    main()

