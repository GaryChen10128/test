# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:21:56 2019

@author: 180218
"""

import gitlab
# private token or personal token authentication
#gl = gitlab.Gitlab('http://10.0.0.1', private_token='JVNSESs8EwWRx5yDxM5q')
#gl = gitlab.Gitlab('http://gitlab.ideas.iii.org.tw', private_token='JLj9KwzuqNPGBmZ37VrK')
#gl = gitlab.Gitlab('http://gitlab.ideas.iii.org.tw/','ydqRAmnGkAHmnZADWfoK')
gl = gitlab.Gitlab('http://150.117.122.207:7777/',private_token='G-mrQ-Zf8P7T3bPx4rDi')
#gl = gitlab.Gitlab('http://150.117.122.207:7777/',private_token='tAGUZUvQeMxBna5ydcEe')


#gl = gitlab.Gitlab('ssh://git@gitlab.safeplayservice.ml:7778/GaryChen/iii_flywheel.git',private_token='i3zquer-YKr4u8vn6_wX')
#

# oauth token authentication
#gl = gitlab.Gitlab('http://10.0.0.1', oauth_token='my_long_token_here')
#gl = gitlab.Gitlab('http://gitlab.ideas.iii.org.tw',oauth_token='kkEaj349NTBYHM8hguAe')
#gl = gitlab.Gitlab('https://gitlab.com/',private_token='-U1XJuXSas4oyaBgx3A1')
#gl = gitlab.Gitlab('https://gitlab.com/')


#
# username/password authentication (for GitLab << 10.2)
#gl = gitlab.Gitlab('http://gitlab.ideas.iii.org.tw', email='180218', password='tp60 rm04tp60 rm04*')
#gl = gitlab.Gitlab('https://gitlab.com/', email='garychen@iii.org.tw', password='Jack0204')

# anonymous gitlab instance, read-only for public resources
#gl = gitlab.Gitlab('http://gitlab.ideas.iii.org.tw')
#gl = gitlab.Gitlab('https://gitlab.com/vurpo/')


# make an API request to create the gl.user object. This is mandatory if you
# use the username/password authentication.

#gl = gitlab.Gitlab.from_config('https://gitlab.com/vurpo/', ['/tmp/gl.cfg'])
#gl = gitlab.Gitlab.from_config('https://gitlab.com/vurpo/')
#gl = gitlab.Gitlab('https://gitlab.com/', private_token='i3zquer-YKr4u8vn6_wX')
gl.auth()
projects = gl.projects.list()
print('list of projects:')
print('id','project name')
for project in projects:
#    print(project)
    print(project.id,project.name)
import numpy as np
import base64
#y=np.array(projects)
#y[1][2]
#groups = gl.groups.get(10)
#for group in groups:
#    print(group)
p_index=10
project = gl.projects.get(p_index)
#print(project.name)
#project = gl.projects.get(10, lazy=True)  # no API call
#p = gl.projects.get(2, lazy=True)  # no API call
branches = project.branches.list()
#project.star() 

print('get into',project.name)
print('list of branches:')
i=0
for branch in branches:
    print(i,branch.name)
    i+=1
    
    
#branches[0].name
#p.branches[1].name

#branches = p.branches.lisproject.branches.delete('feature1')

#commits = project.commits.list()
branch = project.branches.get('master')
branch.commit
#statuses = commit.statuses.list()
branch.developers_can_push

commit = project.commits.get('master')
#commit?
statuses = commit.statuses.list()
#statuses[2]

deployments = project.deployments.list()
data = {
    'branch_name': 'master',  # v3
    'branch': 'master',  # v4
    'commit_message': 'blah blah blah',
    'actions': [
#        {
#            'action': 'create',
#            'file_path': 'README.rst',
##            'content': open('path/to/file.rst').read(),
#            'content': 'gg',
#
#        },
#        {
#            # Binary files need to be base64 encoded
#            'action': 'create',
#            'file_path': 'logo.png',
##            'content': base64.b64encode(open('logo.png').read()),
#            'encoding': 'base64',
#        },
        {
            # Binary files need to be base64 encoded
            'action': 'create',
            'file_path': 'git_test2.py',
#            'content': open('./git_test.py').read(),
            'content': 'chocolate',
#            'encoding': 'base64',
        }
    ]
}
x=project.commits
#x?
#commit = project.commits.create(data)
#diff = commit.diff()
#commit.refs() # all references
#commit.refs('tag') # only tags
#commit.refs('branch') # only branches
#
#diff = commit.diff()
#commit.cherry_pick(branch='target_branch')
#commit.refs() # all references
#commit.refs('tag') # only tags
#commit.refs('branch') # only branches
#commit.merge_requests()

#keys = project.keys.list()
#key = project.keys.get(10)
#key = project.keys.create({'title': 'gary key','key': open('C:/Users/180218/.ssh/id_rsa.pub').read()})
#open('C:/Users/180218/.ssh/id_rsa.pub').read()
#service = project.services.get('master')

#service = project.services.list()
#project.upload("git_test.py", filepath="./git_test.py")
#project.commit()



# 获取指定分支的属性
branch = project.branches.get('master')
print(branch.name)
# 分支保护/取消保护
branch.protect()
#branch.unprotect()
# ---------------------
#------------------------------------------- #
# 获取指定项目的所有tags
tags = project.tags.list()# 获取某个指定tag 的信息
#tags = project.tags.list('1.0')

# 创建一个tag
#tag = project.tags.create({'tag_name':'1.0', 'ref':'master'})

# 设置tags 说明:
#tag.set_release_description('awesome v1.0 release')
# ---------------------------------------------------------------- #
# 获取所有commit info
commits = project.commits.list()
for c in commits:
#    print(c)
    print(c.short_id,'|', c.author_name,'|', c.message,'|' ,c.title)


# 获取指定commit的info
commit = project.commits.get('61f75d55')

# 获取指定项目的所有merge request
mrs = project.mergerequests.list()
print(mrs)
# ---------------------------------------------------------------- #
#  创建一个merge request
mr = project.mergerequests.create({'source_branch':'master',
                                   'target_branch':'feature1',
                                   'title':'merge master feature', })
        
# 更新一个merge request 的描述
mr.description = 'New description'
mr.save()
mr.merge()
# 开关一个merge request  (close or reopen):
mr.state_event = 'close'  # or 'reopen'
mr.save()
# ---------------------------------------------------------------- #


mr.delete()
