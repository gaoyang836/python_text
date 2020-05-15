# -*-coding:utf-8 -*-
# author:gaoyang time:2020-05-15

'''
先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。

http://cn.python-requests.org/zh_CN/latest/user/quickstart.html

然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容

http://mirrors.163.com/centos/6/isos/x86_64/README.txt
http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt

主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
'''

import requests
import threading

url1 = 'http://mirrors.163.com/centos/build/rpmcompare5.pl.txt'
url2 = 'http://mirrors.163.com/centos/6.9/isos/x86_64/0_README.txt'

newStr ="" #初始化字符串
r=threading.Lock()

def foo(url):
    r.acquire()
    global newStr
    newStr += requests.get(url).text
    r.release()

t1 = threading.Thread(target=foo,args=(url1,))
t2 = threading.Thread(target=foo,args=(url2,))
t1.start()
t2.start()
t1.join()
t2.join()

with open("./readme89.txt","w",encoding="utf-8")as f:
    f.write(newStr)

#-------------------------------------------------------------
# # coding=utf8
# import requests
# import threading
#
# urls = [
# 'http://mirrors.163.com/centos/build/rpmcompare5.pl.txt',
# 'http://mirrors.163.com/centos/6.9/isos/x86_64/0_README.txt',
# ]
#
# # 对应urls 依次存储网页文件内容, 先创建同样个数的元素占位
# fileContentList = [None for one in urls]
#
# # 锁对象，用来控制访问 fileContentList
# lock = threading.Lock()
#
# def thread_entry(idx,url):
#     print('thread #%s start' % idx)
#     r = requests.get(url)
#
#     # 注意上面的代码不应该放在获取锁的代码中
#     lock.acquire()
#     # 注意 r.text的类型是unicode，可以在文档中查到
#     fileContentList[idx] = r.text
#     lock.release()
#
#     print('thread #%s end' % idx)
#
#
# if __name__ == '__main__':
#     print('main thread start.')
#
#     threadpool = []
#
#     for idx,url in enumerate(urls):
#         t = threading.Thread(target=thread_entry,
#                           args=(idx,url))
#         t.start()
#         threadpool.append(t)
#
#     # 等所有 线程结束
#     for t in threadpool:
#         t.join()
#
#     # 所有线程结束后，所有内容都获取到了，合并内容
#     mergeTxt = '\n\n----------------------\n\n'.join(fileContentList)
#     print(mergeTxt)