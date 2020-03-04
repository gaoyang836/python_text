# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

#两个不同编码格式的文件合并，并打印内容，提示用户输入新文件名字

#文件夹路径
path=r"d:/"

#初始化一个空字符串
newStr=''

#打开第一个文件utf8编码.txt
with open(path+"/utf8编码.txt",'r',encoding='utf-8') as f:
    newStr = f.read() +/n  #把文件内容加到newStr
#打开第二个文件gbk编码.txt
with open(path+"/gbk编码.txt",'r',encoding='gbk') as f:
    newStr = f.read() +/n #把文件内容加到newStr

print(newStr)

#输入文件名
new_file_name=input("请输入新文件名:")
#生成新文件
with open(path+"/%s",%new_file_name,'w',encoding='utf-8') as f:
    f.write(newStr)











