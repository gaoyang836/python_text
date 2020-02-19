#mysqlclient
import mysqldb
#连接数据库
conn=mysqldb.connot(
    host='ip',
    post='3306',
    user='123',
    passwd='123',
    db='uu',
    charset='utf8'
)
#创建游标数据，为了传递sql语句
c=conn.cursor()
#执行sql语句
c.execute('select * from user')

#插入百万数据
for x in range(10000000):
c.execute(f"insert into user(name,'sx',display) values('测试{x+1}'，'ceshi',6)")
#返回查询结果的第一行
row=c.fetchone()
print(row)
#返回所有数据
rows=c.fetchall
print(rows)

for i in range(c.rowcount):
    row = c.fetchone()
    print(row)
#分组查询
for i in range(c.rowcount):
    row = c.fetchmany(100)
    print(row)
#修改数据后要执行commit
conn.commit()
#关闭数据库服务
conn.close()