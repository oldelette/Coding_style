# -*- coding: utf-8 -*-
__Author__ = "gavin"
__Date__ = '2021/09/27 09:10'

import gitlab

#url = 'https://gitlab.com/ssp19960710'
#token = 'sQasQTVXrKscrFVLtZXR'
#gl = gitlab.Gitlab(url,token,api_version='4')

gl = gitlab.Gitlab('https://gitlab.com', private_token='sQasQTVXrKscrFVLtZXR')

# ---------------------------------------------------------------- #
# 獲取第一頁project
projects = gl.projects.list()
# 獲取所有的project
#projects = gl.projects.list(all=True)

#print(projects)

#for p in gl.projects.list(page=1):
#    print("p.name: ",p.name,"p.id: ",p.id)

#project = gl.projects.get(501)

