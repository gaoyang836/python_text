# author:gaoyang time:2020-02-27
# 从一个文件读取数据，整理格式按id进行统计

'''
1.提取数据：学生id，课程id，签到时间，格式('2017-03-24 11:55:09',271,131)，
--1 打开文件 with open('') as fo:
--2 读取文件内容--多行（有换行符）fo.read().splitlines()
    返回值是一个列表，每一个元素是一行的内容
--3 对每一行进行操作：for line in lines: 遍历
--4 替换无效的字符 格式 2017-03-24 11:55:09,271,131，
--5 切割 line.split(',')--返回值是一个列表-四个元素，只取前三个
--6 验证
2.按要求排版--统计
--1 stuDict={'lessonid':lessonid,'checkintime':checkintime}
--2 统计
3.打印

'''

fileDir = 'd:\\0005_1.txt'
def putInfoToDict(fileName):
    resDict={}
    with open(fileName) as fo:
        lines = fo.read().splitlines() #list
        for line in lines:
            #处理无效字符
            line = line.replace("(",'').replace(")",'').replace("'",'').replace('\t','')
            temp = line.split(',')
            checkTime = temp[0].strip()
            lessonId = int(temp[1].strip())
            useId = int(temp[2].strip())

            stuDict = {'lessonid': lessonId, 'checkintime': checkTime}

            #统计
            if useId  not in resDict:
                resDict[useId]=[stuDict]
            else:
                resDict[useId].append(stuDict)
    return(resDict)

import pprint
pprint.pprint(putInfoToDict(fileDir))