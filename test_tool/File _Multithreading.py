# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

#创建两个子线程，分别读取连个文件内容，主线程把文件储存成新文件

import requests,threading

newStr="" #初始化一个空字符串
lock=threading.Lock()


def foo(url):
    global newStr
    a=requests.get(url).text
    newStr+=a
    lock.release()

url1=http://mirrors.163.com/centos/6/isos/x86_64/README.txt
url2=http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt

t1=threading.Thread(target=foo,args=(url1))
t2=threading.Thread(target=foo,args=(url2))

t1.start()
t2.start()

t1.json()
t2.json()

with open('./readme89.txt','w',encoding='utf-8') as f:
    f.write(newStr)

