#在一个list中，删掉偶数，只保留奇数
# def is_odd(n):
#     return n%2==1

# print(list(filter(is_odd,[1,12,7,54,19,26,47,19,120,11,321])))

# #把一个序列中的空字符串删掉
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,['A','','B',None,'c',''])))

#用filter求素数
# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n
# def _not_divisible(n):
#     return lambda x:x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it = filter(_not_divisible(n),it)
# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break

#练习
def is_palindrome(n):
    # return str(n) == str(n)[::-1]
    # return n == int(str(n)[::-1])
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')