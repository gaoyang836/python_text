# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

import requests
from api_test.config import HOST


# 添加课程
def course_add (name,desc,display_idx):
    dict1={'Content-Type':'application/x-www-form-urlencoded'}
    # 请求体参数
    payload = {
        'action': 'add_course',
        'data':f'''{{"name":"{name}",
        "desc":"{desc}",
        "display_idx":"{display_idx}"}}'''
        }
    try:
        r = requests.post(f"{HOST}/api/mgr/sq_mgr/", headers=dict1, data=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '异常情况'}

# print(course_add ('大学111','excel123','1'))

# 列出课程
def course_list(pagenum,pagesize):
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload={'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
    try:
        r = requests.get(f'{HOST}/api/mgr/sq_mgr/', headers=dict1,params=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '异常情况'}
# print(course_list (1,1))

# 修改课程
def course_modify(id,name,desc,display_idx):
    dict1={'Content-Type':'application/x-www-form-urlencoded'}

    payload = {'action': 'modify_course',
               'id':'{id}',
               'newdata':'''{"name":"{name}",
                          "desc":"{desc}",
                          "display_idx":"{display_idx}"}'''
               }

    try:
        r = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=dict1, data=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '异常情况'}

# 删除课程
def course_delete(id):
    dict1={'Content-Type':'application/x-www-form-urlencoded'}

    payload={'action':'delete_course','id':id}

    try:
        r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=dict1, data=payload)
        return r.json()
    except:
        return {'retcode': 999, 'reason': '异常情况'}
# print(course_delete(1530))




