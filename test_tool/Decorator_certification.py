# -*-coding:utf-8 -*-
# author:gaoyang time:2020-03-04

#用装饰器加认证功能（token）
#token:令牌，是服务端生成的一串字符串，作为客户端进行请求的一个标识,
# 当用户第一次登录后，服务器生成一个token并将token返回给客户端，
# 以后客户端登录会判断token，有token不用登录，没有token需要登陆

#按理说此处应该连接数据库表，此处用字典代替
user_dict={  #用户名密码
    'user1':'123',
    'user2':'123'
}

token=""

#定义一个装饰器
def auth(func):
    def inner(*args,**kwargs):
        global token #声明全局变量


        if token:  #有效token
            func()
        else:
            name=input("请输入用户名").strip()
            passwd= input("请输入密码").strip()

            if name in user_dict and user_dict[name]==passwd:
                token=name
                func(*args,**kwargs)
            else:
                print('用户名和密码错误')
    return inner

def my_log():
    print('this is my_log')

def my_name(name):
    print('欢迎登录',name)

def my_shopping():
    print('商城购物')

while True:
    choose_num=input("\n\n1、查看信息\n2、我的信息\n3、我的商城"
                     "\n请输入操作选项")


    if choose_num=='q' or choose_num=='Q':
        break
    elif choose_num == '1':
        my_log()
    elif choose_num == '2':
        my_name('张三')
    elif choose_num == '3':
        my_shopping()
    else:
        print('输入不合法')


#随机字符串
# import  uuid
#
# print(uuid.uuid4())
#
# for i in range(10):
#     a+=chr(random.radint(65,95))
