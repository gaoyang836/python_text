# -*-coding:utf-8 -*-

from robot.api.logger import console   #在控制台引用

def check_score(score):
    if int(score) >= 60:
        print("恭喜你及格了")
        console("恭喜你及格了")
    else:
        print("回去复习吧！")
        console("回去复习吧！")




