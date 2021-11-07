import gitlab

URL = "https://gitlab.com"
token = "q3pndvPbWNtTj-gEuJ3w"
ID = 29301882

gl = gitlab.Gitlab(URL,token)
project = gl.projects.get(ID)
#print(project)

issues = project.issues.list()
#issue = project.issues.get(5)
#print(issue)


issue = project.issues.create(
        {   
            "title": "Automation Test",
            "description": "This is not a drill",
            "due_date": "2021-11-07",
            "milestone_id": 2,
            "assignee_ids": [user.id for user in project.members.list()]                             
        }   
    )
