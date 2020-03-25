# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

import requests

#传参

# 请求头参数
dict1={'Content-Type':'application/x-www-form-urlencoded'}
# 请求体参数
payload={'action':'delete_course','id':1522}


# 发起put请求
r=requests.delete(r'http://127.0.0.1:80/api/mgr/sq_mgr/', data=payload,headers=dict1)

# 打印响应结果
print(r.json())
#print(r.text)






