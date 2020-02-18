# 切片
# L = ['gao','yang','ya','ha','hu','hei']

# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)

# print(L[0:3])
# print(L[:3])
# print(L[2:4])
# print(L[-1:])
# print(L[-3:-1])
# print(L[-3:-2])
# print(L[:8:2])

# # 切元组
# print((0,1,2,3,4,5)[:4:2])
# #切字符串
# print('ABCDEFG'[::2])

#切片小练习
# def trim(s):
#     while (s[:1]==' '):
#         s=s[1:]
#     while (s[-1:]==' '):
#         s=s[:-1]
#     print(s)

# trim(' .字符串. ')

#迭代

# for ch in 'abcd':
#     print(ch)

#被弃用了？查询对象能不能迭代
# from collections import Iterable
# isinstance('abc',Iterable)

# enumerate索引元素对
# for i,value in enumerate(['a','b','c']):
#     print(i,value)

#小练习
# def findMaxMin(L):
#     if L==[ ]:
#         return None,None
#     else:
#         return max(L),min(L)

# print(findMaxMin([1,4,6,3,7]))

# def findMaxMin(L):
#     s=len(L)
#     while s==0:
#         return None,None
#     while s==1:
#         return L[0],L[0]
#     while s>1:
#         min=L[0]
#         max=L[s-1]
#         for k in L:
#             if k<min:
#                 min = k
#             elif k>max:
#                 max=k
#             return min,max

# print(findMaxMin([1,4,6,3,7]))

#列表生成式
# L=[]
# for x in range(1,11):
#     L.append(x*x)

# print(L)

# print([x*x for x in range(1,11)])

# print([x*x for x in range(1,11) if x%2==0])

# print([m+n for m in 'abc'for n in 'xyz'])

# import os 
# print([d for d in os.listdir('.')])

# d={'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#     print(k,'=',v)

# d={'x':'A','y':'B','z':'C'}
# print([k+'='+v for k,v in d.items()])
  
# L=['hello','world','ibm','apple']
# print([s.lower() for s in L])

#练习
# L=['hello','world',18,'apple',None]
# print([s.lower() for s in L if isinstance(s,str)])

#生成器

# L=[x*x for x in range(10)]
# print(L)

# g=(x*x for x in range(10))
# print(next(g))
# print(next(g))
# print(next(g))

# g=(x*x for x in range(10))
# for n in g:
#     print(n)

# def fib(max):
#     n,a,b=0,0,1
#     while n < max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# print(fib(6))

# def fib(max):
#     n,a,b=0,0,1
#     while n < max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'

# for n in fib(6):
#     print(n)

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()
# next(o)
# next(o)
# next(o)
# next(o)
  
#练习

# def triangles():
#     L=[1]
#     yield L
#     L=[1,1]
#     yield L
#     layer=3
#     while layer<11:
#         Ln=[]
#         for i in range(layer):
#             if i == 0:
#                 Ln.append(1)
#             elif i<layer-1:
#                 Ln.append(L[i-1]+L[i])
#             else:
#                 Ln.append(1)
#         yield Ln
#         L=Ln
#         layer+=1    

# for t in triangles():
#     print(t)

#迭代器
from collections import lterable
isinstnce([],lterable)
