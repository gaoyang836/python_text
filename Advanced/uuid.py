# -*-coding:utf-8 -*-
# author:gaoyang time:2020-05-10

# 现已实现以下功能 my_log、my_name、my_shopping_mall 函数
# 要求编写装饰器，为 my_log、my_name、my_shopping_mall 函数加上认证的功能，
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# 账户名密码来自字典变量

# 补充知识: token
# token的意思是“令牌”，是服务端生成的一串字符串（这里我们可以随意指定一个字符串），
# 作为客户端进行请求的一个标识。
# 当用户第一次登录后，服务器生成一个 token 并将此 toke n返回给客户端，
# 以后客户端只需带上这个 token 来请求数据即可，无需再次带上用户名和密码

import uuid
user_dict = {
    "user1":"123",
    "user2":"123"
}
2
token=None

def auth(func):
    def wrapper(*args,**kwargs):
        global token
        if token:     # token有效
            func(*args,**kwargs)
        else:       # token无效
            userName=input('请输入你的用户名：').strip()
            passWord=input('请输入你的密码：').strip()

            # 判断用户名密码是否在user_dict字典里
            if userName in user_dict and user_dict[userName]==passWord:
                func(*args,**kwargs)
                # 生成随机字符串
                token = str(uuid.uuid4())
            else:
                print('输入的账户不存在')
    return wrapper

@auth
def my_log():
    print('this is my_log')

@auth
def my_name(name):
    print('欢迎登录',name)

@auth
def my_shopping_mall():
    print('商城购物')

while True:
    choose_num=input("1.查看日志\n2.我的信息\n3.我的商城\n请输入操作选项：")
    if choose_num == "1":
        my_log()
    elif choose_num == "2":
        my_name("张三")
    elif choose_num == "3":
        my_shopping_mall()
    # elif choose_num =="q" or choose_num == "Q":
    #     break
    else:
        print("输入不合法")