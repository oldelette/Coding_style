import subprocess
import gitlab
import asyncio
import time

from config import *

gl = gitlab.Gitlab(url, privatet)
loop = asyncio.get_event_loop()
start_time = time.time()

async def get_issue(pro_id):
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")

    project = await loop.run_in_executor(None,gl.projects.get,pro_id)
    issues = project.issues.list()

    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")


def main():
    gl = gitlab.Gitlab(url, privatet)
    projects = gl.projects.list()
    #project = gl.projects.get(project_ID)
    #print(projects[0])
    pro_len=len(projects)
    print(pro_len)

    tasks = []
    for pro in projects:
        task = loop.create_task(get_issue(pro.id))
        tasks.append(task)
        
    loop.run_until_complete(asyncio.wait(tasks))

    
    

if __name__ == '__main__':
    main()

