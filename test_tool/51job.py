# author:gaoyang time:2020-03-01
#用爬虫爬取51job岗位信息，存入excel表
#用正则表达式提取数据

#写入excel
import xlwt
#创建excel文件
workBook = xlwt.Workbook(encoding='utf-8')
#在文件对象创建一个表
workSheet = workBook.add_sheet('51jobs.res')
#创建列名
colName=['职位名','公司名','工作地点','薪资','发布时间']
for col in range(0,len(colName)):
    workSheet.write(0,col,colName[col])  #行、列、内容


#模拟浏览器请求
import requests
import re

def get_webPages():
    web_url='https://search.51job.com/list/160200,000000,0000,00,9,99,%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url)
    resp.encoding = 'gbk'
    pages =re.findall('<span class="td">共(.*?)页，到第</span>',resp.text,re.S)[0]
    return int(pages)
line=1
for one in range(0,get_webPages()+1):
    #解析界面内容
    web_url=f'https://search.51job.com/list/160200,000000,0000,00,9,99,%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{one}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url)
    resp.encoding = 'gbk'
    #提取有用数据
    print(resp.request.headers) #获取请求头
    print(resp.request.body)  # 获取请求体
    print(resp.headers)  # 响应头


    info=re.findall('<div class="el">(.*?)</div>',resp.text,re.S)

    for one in info:

        temp=re.findall('<a target="_blank" title="(.*?)" href=',one,re.S)
        jobName=temp[0]
        workSheet.write(line,0,jobName)  # 行、列、内容
        companyName = temp[1]
        workSheet.write(line, 1, companyName)
        address = re.findall('<span class="t3">(.*?)</span>',one,re.S)[0]
        workSheet.write(line, 2, address)
        salary = re.findall('<span class="t4">(.*?)</span>',one,re.S)[0]
        workSheet.write(line, 3, salary)
        jobTime = re.findall('<span class="t5">(.*?)</span>',one,re.S)[0]
        workSheet.write(line, 4, jobTime)
        line += 1
#存储数据

workBook.save('d:\\51job.xls')  #存放路径



