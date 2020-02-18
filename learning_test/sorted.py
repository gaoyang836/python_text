# #排序
# print(sorted([36,5,-12,9,-21]))

# #按绝对值排序
# print(sorted([36,5,-12,9,-21],key=abs))

# #字符串排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))

# #反向排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#练习
#分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0][:]
    # return t[0]
L2 = sorted(L, key=by_name)
print(L2)

# #再按成绩从高到低排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[:][1]
    # return t[1]
L2 = sorted(L, key=by_score)
print(L2)


# # 二维列表的元素都是列表，想获取元素需要取两次索引
# list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# print(list[0])
# print(list[0][0])
# print(list[0][:])
# print(list[1][:])
# print(list[2][:])
# print(list[:][1])
# print(list[:][2])

print(sorted([('bob','key'), ('about', 'Zoo'), ('Credit','abs')]))