# #匿名函数
# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

# #赋值
# f=lambda x:x*x
# print(f(5))

# #在返回值
# def build(x,y):
#     return lambda:x*x+y*y
# f=build(2,3)
# print(f())

#练习
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
