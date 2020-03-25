# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

import requests

#传参

# 请求头参数
dict1={'Content-Type':'application/json'}

# 请求体参数
payload={
    "action":"add_course_json",
    "data": {
        "name":"初中化学442",
        "desc":"初中化学课程",
        "display_idx":4
    }
}

# 发起post请求
r=requests.post(r'http://127.0.0.1:80/api/mgr/sq_mgr/',headers=dict1,data=payload)

# 打印响应结果
print(r.json())






