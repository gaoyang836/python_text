
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
# print(calc(1,2))    

# from conf import conf

# # conf={'s':1}
# def sum(a,b):
#     s=a+b
#     return s
 
# if __name__=='__main__':
#     print(sum(1,2))
#     # print(conf['s'])
        
# def person(name,age,**kw):
#     print(name,age,kw)

# def person(name,age):
#     print(name,age)


# person('2','2')
    
# def person(name,age,**kw):
#     print('name:', name, 'age:',age,' other:',kw)

# # person('gaoyang',23)
# # person('gaoyang',23,city='shijiazhuang')
# person('gaoyang',23,city='shijiazhuang',job='ceshi')

# def person(name,age,*,city,job):
#     print(name,age,city,job)

# person('gaoyang',24,city=‘shijiazhuang’,job='ceshi')

# def person(name,age,*city,job):
#     print(name,age,city,job)

# person('gaoyang',24,‘shijiazhuang’,job='ceshi')

# def person(name,age,*,city='shijiazhuang',job):
#     print(name,age,city,job)

# person('gaoyang',23,job='ceshi')

# def person(name,age,*,city,job='ceshi'):
#     print(name,age,city,job)

# person('gaoyang',23,city='shijiazhuang')


# def person(name,age,*,city='shijiazhuang',job='ceshi'):
#     print(name,age,city,job)

# person('gaoyang',23)

# def f1(a,b,c=0,*args,**kw)
#     print('a=',a,'b=',b,'c=',c,'args=',aegs,'kw=',kw)
   
def product(*args):
    s=1
    for x in args:
        s=s*x
    print(s) 
     
product(2,4,3,5)

def product(*args):
    n=len(args)
    s=1
    i=0
    while i<n:
        s=s*args[i]
        i=i+1
    print(s)
     
product(3,4,2,5)

