# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-16

import requests
from config import HOST
# 用户登录
def login(username,password):
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": username,
        "password": password
    }
    r = requests.post(f'{HOST}/api/mgr/loginReq', headers=dict1, data=payload)

    return r.json()







