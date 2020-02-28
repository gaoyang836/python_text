# author:gaoyang time:2020-02-28
'''
33面向对象作业
1.先找所有对象  #类
   房间
   老虎
   羊
2.对象关系组网
'''

#创建房间给编号，动物
class Room:
    def __init__(self,inNum,inAnimal):  #实例属性
        self.num=inNum
        self.animal=inAnimal

#定义老虎类
class Tiger:
    classname = '老虎'                    # 静态属性，本质是一个变量
    def __init__(self,inweight=200):     # 实例属性，self调用时自动传入
        self.weight = inweight

    def roar(self):                  # 实例方法
        print("wow")
        self.weight -= 5

    def feed(self, food):
        if food == '肉':
            print('喂食正确，体重增加10斤')
            self.weight += 10
        else:
            print('喂食错误，体重减10斤')
            self.weight -= 10

#定义羊类
class Sheep:
    classname = '羊'                # 静态属性，本质是一个变量
    def __init__(self,inweight=100):     # 实例属性，self调用时自动传入
        self.weight = inweight

    def roar(self):                  # 实例方法
        print("mie")
        self.weight -= 5

    def feed(self, food):
        if food == '草':
            print('喂食正确，体重增加10斤')
            self.weight += 10
        else:
            print('喂食错误，体重减10斤')
            self.weight -= 10


#游戏初始化操作，创建十个房间的实例

from random import randint
roomList=[]      # 每一个元素是 房间实例
for one in range(1,11):   # 十次
    if randint (0,1) == 1:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)   # 房间实例
    roomList.append(room)

#开始游戏
import time
startTime = time.time()  #开始时间
while True:
    curTime = time.time()  #一直计时
    if curTime-startTime >180:
        print('游戏时间到，游戏结束')
        #显示每个房间的动物和体重
        for one in roomList:
            print('当前房间编号:{},动物是:{},体重是:{}斤'.format(one.num,one.animal.className,one.animal.weight))
        break
    #随机给房间号
    roomNum= randint(0,9) #int
    roomObject=roomList[roomNum] #随机房间号对应的房间实例

    # 提示
    # print('当前房间号：{}'.format(rootNum))
    # answer=input('是否选择敲门：(y/n)?')
    answer=input('当前房间号：{},是否选择敲门：(y/n)?'.format(roomNum+1))

    # 用户敲门，调叫方法，后面喂食，不敲门直接喂食
    if answer =='y':
        roomObject.animal.roar()

    # 喂食
    food = input('请投喂食物：(肉/草)？').strip( )
    roomObject.animal.feed(food)




