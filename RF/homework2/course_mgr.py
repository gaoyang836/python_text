# -*-coding:utf-8 -*-
import requests

def listCourse():
    resp = requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
    courses=resp.json()['retlist']

    return  [c['name'] for c in courses]
