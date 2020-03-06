#提取每一行log的文件类型(扩展名)和大小

log='''fadfsag.jpg\t2415\tfaiongvapnpgangp\nfadfsag.jpg\t2415\tfaiongvapnpgangp'''

#按\n把日志文件按行切成列表
linesList = log.split('\n')

#去除前后空字符串
del linesList[0],linesList[-1]
#resList = []
resList = {}
#取每一行的内容文件类型和大小
for line in linesList:
    temp = line.split('\t')
    ftype = temp[0].split('.')[1].strip()
    fsize = int(temp[1].strip())
    #统计用字典
    if ftype in resList:
        resList[ftype]+= fsize
    else:
        resList[ftype] = fsize
#相同文件统计
# # [[类型1，大小1],[],[]]
#     inFlag = 0 #普通变量。表示不在resList
#
# #首先判断该类型在不在结果列表里面
#     for one in resList:
#         if ftype ==one[0]:#满足表示改类型存在
#             one[1]+=fsize
#             inFlag=1  #表示该类型添加成功
#             break
#
#     if inFlag == 0 :   #如果不存在就加到列表里
#         resList.append([ftype,fsize])


'''
优化:
统计用字典
读log文件
'''


