#map例子

# def f(x):
#     return x * x

# r=map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

#列表生成式
# print([n*n for n in [1,2,3,4,5,6,7,8,9]])

#基础写法
# def f(x):
#     return x * x 

# L = [ ]
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

#insert(结果顺序就乱了)
# def f(x):
#     return x * x 

# L = [ ]
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.insert(1,f(n))
# print(L)

# extend把f(n)变为列表
# def f(x):
#     return x * x 

# L = [ ]
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.extend([f(n)])
# print(L)

# extend把f(n)变为字典
# def f(x):
#     return x * x 

# L = [ ]
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.extend({f(n}])
# print(L)

#list转化为字符串
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce
# from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,[1,3,5,7,9]))

# from functools import reduce
# # def fn(x,y):
# #     return x*10+y
# # char2num函数中参数s,按照键找到对应值返回
# #(通过map把一个整的字符串迭代单个的字符串）
# def char2num(s):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     print(digits[s])
#     return digits[s]
# # print(reduce(fn,map(char2num,'13579')))
# print(map(char2num,'13579'))

# from functools import reduce
# DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def char2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

#练习

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# def normalize(name):
#     return name.capitalize()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

#编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce

# def prod(x,y):
#     return x*y 
# print(reduce(prod,[3, 5, 7, 9]))

#编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce

# def prod(L):
#     def fn(x,y):
#         return x*y 
#     return reduce(fn,L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

# def str2float(s):
#     def fn(x,y):
#         return x*10+y
#     n=s.index('.')
#     s1=list(map(int,[x for x in s[:n]]))
#     s2=list(map(int,[x for x in s[n+1:]]))
#     return reduce(fn,s1)+reduce(fn,s2)/(10**len(s2))#乘幂

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

#用filter求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while true：
        n=next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n<1000:
        print(n)
    else:
        break

