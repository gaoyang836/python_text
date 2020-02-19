import paramiko

#创建SSHClient实例对象
ssh = paramiko.SSHClient()

#创建安全策略，信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器 地址、端口、用户名密码
ssh.connect("ip",22,"user","pd")

#执行命令
#ssh.exec_command('echo "ip=192.168.1.1">cfg.py')
#生成多个文件
#for x in range(20):
#    ssh.exec_command(f'echo "ip=192.168.1.{x+1}">cfg_{x+1}.py')
 #列出关于apiteach的进程，并且没有grep的,把三个返回值，赋值给stdin,stdout,stderr
stdin,stdout,stderr=ssh.exec_command('ps -ef|grep apiteach|grep -v grep')
#读取结果
output=stdout.read().decode()
#判断结果中有没有apiteach关键字
if 'apiteach' in output:
    print("老版本运行中。。。准备杀死")
#分割读取结果
parts=output.split(' ')
#去除结果中的空字符
ps=[part for part in parts if part!='']
# 获取进程号
pid=ps[1]
#杀掉该进程
ssh.exec_command('kill -9 +pid')

#有旧的代码包删掉
ssh.exec_command('rm -f restapi-teach.zip')

#上传本地的新的代码包（有配置文件）
sftp=ssh.open_sftp()
sftp.put(r'f:\tmp\new_restapi-teach.zip','/home/stt5/new_restapi-teach.zip')
sftp.close()

#备份原来的目录
ssh.exec_command('rm -rf new_restapi-teach.back;mv new_restapi-teach new_restapi-teach.bak')

#解压安装包
ssh.exec_command('unzip new_restapi-teach.zip',printOutput=False)
print('ok')

#运行（chmod +x 给执行权限）
ssh.exec_command('cd restapi-teach;chmod +x run.sh ;dos2unix run.sh;./run.sh;sleep5)

#检查是否运行成功
ssh.exec_command('ps -ef|grep apiteach|grep -v grep')

if 'apiteach' in output:
    print("运行成功")

#接web自动化，打开网站，登录验证等