#从文件1读内容，计算后输出到文件2
rfiledir='d:\\file1.txt'
wfiledir='d:\\file2.txt'
#获取文件中每一行名字和工资
with open (rfiledir) as rfile,open (wfiledir,'w') as wfile:
    lines=rfile.read().splitlines()
    for line in lines:
        if line.split(';')
            temp=line.split(';')
            if temp[0].count(':')==1 and temp[1].count(':')==1
                name=temp[0].split(':')[1].strip()
                salary= temp[1].split(':')[1].strip()
                if salary.isdigit():
                    salary=int(salary)
                    #排版
                    infostr=f'name:{name:>6};salary:{salary:>6};' \
                            f'tax:{salary*0.1:>6};income:{salary*0.9:>6}'
                else:
                    infostr = 'this line salary not digit'
            else:
                infostr='this line ;is error'
        else:
            infostr='this line ;is error'
            # 写入
            wfile.write(infostr + '\n')

'''
优化:
场景，财务部小工具导出exe 用pyinstall
功能，计算工资详情
'''