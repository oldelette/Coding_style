# -*- coding: utf-8 -*-
__Author__ = "gavin"
__Date__ = '2021/09/27 09:10'

"""
gitlab 經常使用到的api
DOC_URL: http://python-gitlab.readthedocs.io/en/stable/
LOCAL_PATH: C:\Python36\Lib\site-packages\gitlab
"""

import gitlab

url = 'https://gitlab.com/ssp19960710/0902.git'
token = 'sQasQTVXrKscrFVLtZXR'

# 登入
gl = gitlab.Gitlab(url,token)

# ---------------------------------------------------------------- #
# 獲取第一頁project
projects = gl.projects.list()
# 獲取所有的project
projects = gl.projects.list(all=True)
# ---------------------------------------------------------------- #

#print(projects)

# ---------------------------------------------------------------- #
# 獲取所有project的name,id
#for p in gl.projects.list(all=True,as_list=False):
#  print(p.name,p.id)
# ---------------------------------------------------------------- #

"""

# ---------------------------------------------------------------- #
# 獲取第一頁project的name,id
for p in gl.projects.list(page=1):
  print(p.name,p.id)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 通過指定id 獲取 project 物件
project = gl.projects.get(501)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 查詢專案
projects = gl.projects.list(search='keyword')
# ---------------------------------------------------------------- #

# ---------------------------------------------------------------- #
# 建立一個專案
project = gl.projects.create({'name':'project1'})
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 獲取公開的專案
projects = gl.projects.list(visibility='public') # public,internal or private
# ---------------------------------------------------------------- #


# 獲取 project 物件是以下操作的基礎


# ---------------------------------------------------------------- #
# 通過指定project物件獲取該專案的所有分支
branches = project.branches.list()
print(branches)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 獲取指定分支的屬性
branch = project.branches.get('master')
print(branch)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 建立分支
branch = project.branches.create({'branch_name': 'feature1','ref': 'master'})
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 刪除分支
project.branches.delete('feature1')
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 分支保護/取消保護
branch.protect()
branch.unprotect()
# ---------------------------------------------------------------- #





# ---------------------------------------------------------------- #
# 獲取指定專案的所有tags
tags = project.tags.list()

# 獲取某個指定tag 的資訊
tags = project.tags.list('1.0')

# 建立一個tag
tag = project.tags.create({'tag_name':'1.0','ref':'master'})

# 設定tags 說明:
tag.set_release_description('awesome v1.0 release')

# 刪除tags
project.tags.delete('1.0')
# or
tag.delete()

# ---------------------------------------------------------------- #
# 獲取所有commit info
commits = project.commits.list()
for c in commits:
  print(c.author_name,c.message,c.title)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 獲取指定commit的info
commit = project.commits.get('e3d5a71b')
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 獲取指定專案的所有merge request
mrs = project.mergerequests.list()
print(mrs)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 獲取 指定mr info
mr = project.mergerequests.get(mr_id)
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 建立一個merge request
mr = project.mergerequests.create({'source_branch':'cool_feature','target_branch':'master','title':'merge cool feature',})
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 更新一個merge request 的描述
mr.description = 'New description'
mr.save()
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 開關一個merge request (close or reopen):
mr.state_event = 'close' # or 'reopen'
mr.save()
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# Delete a MR:
project.mergerequests.delete(mr_id)
# or
mr.delete()
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# Accept a MR:
mr.merge()
# ---------------------------------------------------------------- #


# ---------------------------------------------------------------- #
# 指定條件過濾 所有的merge request
# state: state of the MR. It can be one of all,merged,opened or closed
# order_by: sort by created_at or updated_at
# sort: sort order (asc or desc)
mrs = project.mergerequests.list(state='merged',sort='asc') # all,opened or closed
# ---------------------------------------------------------------- #



# ---------------------------------------------------------------- #
# 建立一個commit
data = {
  'branch_name': 'master',# v3
  'commit_message': 'blah blah blah','actions': [
    {
      'action': 'create','file_path': 'blah','content': 'blah'
    }
  ]
}
commit = project.commits.create(data)
# ---------------------------------------------------------------- #



# ---------------------------------------------------------------- #
# Compare two branches,tags or commits:
result = project.repository_compare('develop','feature-20180104')
print(result)
# get the commits

for commit in result['commits']:
  print(commit)
#
# get the diffs
for file_diff in result['diffs']:
  print(file_diff)
# ---------------------------------------------------------------- #





# ---------------------------------------------------------------- #
# get the commits
for commit in result['commits']:
  print(commit)
#
# get the diffs
for file_diff in result['diffs']:
  print(file_diff)
# ---------------------------------------------------------------- #

"""
