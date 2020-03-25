# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

#调取列出课程接口
import requests
import pprint

#发送请求
payload={'action':'list_course','pagenum':'1','pagesize':'20'}
r = requests.get(r'http://127.0.0.1:80/api/mgr/sq_mgr/',params=payload)
#r = requests.get(r'http://127.0.0.1:80/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')

#获取响应
res=r.json()
pprint.pprint(res)


