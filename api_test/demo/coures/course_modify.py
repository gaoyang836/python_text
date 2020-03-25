# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

import requests

#传参

# 请求头参数
dict1={'Content-Type':'application/x-www-form-urlencoded'}
# 请求体参数
payload = {'action': 'modify_course',
           'id':'1522',
           'newdata':'''{"name":"初中化学",
                      "desc":"初中化学课程",
                      "display_idx":"4"}'''
           }

# 发起put请求
r=requests.put(r'http://127.0.0.1:80/api/mgr/sq_mgr/',data=payload,headers=dict1)
#
# # 打印响应结果
print(r.json())


