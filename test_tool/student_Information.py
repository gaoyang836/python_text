#获取学生信息
# 格式 marry,20;Jack,19;
info =input('请输入学生信息')

tempList= info.split(';')
del tempList[-1] #去除最后一个空字符串
#每一个元素是一个学生信息
for one in tempList:
    name = one.split(',')[0].strip()
    age = one.split(',')[1].strip()
    print('{:<20}:{:0>2};'.format(name,age))  #格式化输出

'''
优化：
用户输入判断，；
年龄int
'''