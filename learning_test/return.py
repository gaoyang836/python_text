#返回函数

#一般情况
# def calc_sum(*args):
#     ax=0
#     for n in args:
#         ax=ax + n
#     return ax
# print(calc_sum(3,4,5))

# #返回求和函数
# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return sum
# f=lazy_sum(6,7,3)
# print(f())

#闭包
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs 
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())

#练习
# def createCounter():
#     s=[0]
#     def counter():
#         s[0]=s[0]+1
#         return s[0]
#     return counter

# def createCounter():
#     s=0
#     def counter():
#         nonlocal s
#         s= s + 1
#         return s
#     return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')