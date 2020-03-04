# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

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

print(handle_data("haha"))