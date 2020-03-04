# author:gaoyang time:2020-03-02
import copy
#定义一个元组，元组里面有一个列表，可以理解成内部
atuple=[1,2,3,[4,5]]
#将元组赋值给b
b = atuple
#浅拷贝
c = copy.copy(atuple)
#深拷贝
d = copy.deepcopy(atuple)
#打印每个对象的值
print ("b is {0},c is {1},d is {2}".format(b,c,d))

#改变atuple里面内嵌的列表，给列表增加一个6
atuple[3].append(6)

print ("b is {0},c is {1},d is {2}".format(b,c,d))

#改变atuple里面的列表，给列表增加一个7
atuple.append(7)

print ("b is {0},c is {1},d is {2}".format(b,c,d))


b is [1, 2, 3, [4, 5]],c is [1, 2, 3, [4, 5]],d is [1, 2, 3, [4, 5]]
b is [1, 2, 3, [4, 5, 6]],c is [1, 2, 3, [4, 5, 6]],d is [1, 2, 3, [4, 5]]
b is [1, 2, 3, [4, 5, 6], 7],c is [1, 2, 3, [4, 5, 6]],d is [1, 2, 3, [4, 5]]

