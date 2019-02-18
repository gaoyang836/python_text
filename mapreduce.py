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