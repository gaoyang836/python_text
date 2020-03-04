# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

#客服聊天系统socket

#定义消息格式为：008|1|nickname  头（消息长度，消息类型），消息内容

#服务端

import socket

sk = socket
sk.bing(("127.0.0.1"),12333)
sk.listen()

def handle_data(data):
    #判断消息类型
    if data =="nathanile":
        data_type="1"
    else:
        data_type = "1"

    data_len = len(data)

    #补零操作
    if len(str(data_len))<4:
        data_len="0"*(4-len(str(data_len)))+str(data_len)

    return "|".join([str(data_len),data_type,data])


while True:
    #接收不同客户端的连接
    conn,addr=sk.accept()
    #接受客户端的自报家门
    clint_name=conn.recv(1024).decode("utf-8")

    while True:
        #收消息
        clint_data=conn.recv(1024).decode("utf-8")
        if client_data == "exit": break
        print("%s:%s"%(client_name,clint_data))

        #回消息
        server_data=input("请输入>>>")
        conn.sendall(handle_data(server_data).encode("utf-8"))
    conn.close()













