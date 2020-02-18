import requests
from pprint import pprint
#get请求
#发送请求
res=requests.get('http://ip/url')
#查看响应
print(res.status_code)
print(res.join())
pprint(res.join(),width=30)

#post请求
requests.post(http://ip/url,data={'action':'dd_course','data':'''{
    "name":"初中"，
    "name":"初中"
}
'''
 })
#添加数据前的
list1=res.json()['retlist']

retobj=res.json()
#判断返回状态
if retobj['retcode']==0:
    print(通过)
esle:
    print(失败);

#再一次post请求
requests.post(http://ip/url,data={'action':'dd_course','data':'''{
    "name":"初中"，
    "name1":"高中"
}
'''
 })
#添加数据后的
list2=res.json()['retlist']

#取出列表2比列表1多的内容
newcourse =None

for one in list2:
    if one not in list1:
        newcourse =one
        break
#检查是否为刚添加的课程
assert newcourse!=None
assert newcourse[name]=="初中"
assert newcourse[name1]=="高中"