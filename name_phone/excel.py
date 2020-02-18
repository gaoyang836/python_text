# 对excel的操作
import xlrd
import xlwt
# import xlrdwriter
import requests

# 打开excle
xl = xlrd.open_workbook(r'D:\file\data.xlsx')
# print(xl.read())

# 通过索引获取工作表
table = xl.sheets()[0]
print(table)

# 获取一共多少行
rows = table.nrows
print(rows)

# 获取第一行的内容,索引从0开始
row = table.row_values(0)
print(row)

# 获取第一列的整列的内容
col = table.col_values(0)
print(col)

 # 获取单元格值，第几行第几个，索引从0开始
data = table.cell(3, 0).value
print(data)


'''写入excel文件'''
import xlwt

# 创建excel文件
xl = xlwt.Workbook(r'D:\test.xlsx')

# 添加sheet
sheet = xl.add_worksheet('sheet1')

# 往单元格cell添加数据,索引写入
sheet.write_string(0, 0, 'username')

# 位置写入
sheet.write_string('B1', 'password')

# 设置单元格宽度大小
sheet.set_column('A:B', 30)

# 关闭文件
xl.close()