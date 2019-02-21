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
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())