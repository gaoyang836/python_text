#装饰器
# def now():
#     print('2015-3-25')
# f=now
# f()

#now属性
# print(now.__name__)
# print(f.__name__)

#装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-3-25,345,hahah')

now()