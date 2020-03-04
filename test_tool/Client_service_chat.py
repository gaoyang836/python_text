# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

#客服聊天系统socket

#定义消息格式为：008|1|nickname  头（消息长度，消息类型），消息内容

my_name="tom"

import socket

sk=socket.socket()

sk.connect(('127.0.0.1',12333))

#先自报家门
sk.sendall(handle_data(my_name).encode("utf-8"))
sk.recv(1024)


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
    # 发信息
    client_data = input("请输入>>>")
    if client_data == "exit": break
    sk.sendall(handle_data(client_data).encode("utf-8"))

    #收消息
    server_data=sk.recv(1024).decode("utf-8")
    print("%s:%s"%("服务端",clint_data))




