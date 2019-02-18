''' names = ['gaoyang', 'xinxin', 'guanglin']
    for ceshi in names:
    print(ceshi)'''

'''sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
    print(sum)'''

'''sum = 0
for x in range(101):
    sum = sum + x
    print(sum)'''

'''sum = 0
n = 99
while n>0:
    sum=sum+n
    n=n-2
    print(sum)'''

'''sum = 0
n = 1
while n<100:
    sum=sum+n
    n=n+2
    print(sum)'''

# l = ['Bart', 'Lisa', 'Adam']
# n = 0
# while n<3:
#     n=n+1
#     print('hello,',l(n))

# name = ['Bart', 'Lisa', 'Adam']  
# for x in name  :
#     print('hello,',x)

# n=1
# while n<= 100:
#     if n > 10 :
#         break
#     print(n)
#     n=n+1
#     print('end')  

n = 0
while n<10:
    n=n+1
    if n % 2 == 0:
        continue
    print(n)