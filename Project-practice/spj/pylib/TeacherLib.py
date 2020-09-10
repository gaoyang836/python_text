# -*-coding:utf-8 -*-
import requests
import json
from cfg import g_vcode
from pprint import pprint
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn


class TeacherLib:
    URL = "http://ci.ytesting.com/api/3school/teachers"

    # 列出老师
    def list_teacher(self,subjectid=None):

        params = {
            'vcode':g_vcode,
            'action':'search_with_pagenation',
        }
        if subjectid != None:
            params['subjectid'] = int(subjectid)


        response = requests.get(self.URL, params=params)
        bodyDict=response.json()

        pprint(bodyDict,indent=2)  #indent=2缩进等于二
        return bodyDict


    # 添加老师
    #加参数idSaveName，获取返回id
    def add_teacher(self,username,realname,phonenumber,email,idcardnumber,
                    subjectid,classlist,idSavedName=None):

        # classlist=str(classlist)
        # newclasslist=[{"id":one} for one in classlist.split(',') if one]

        payload = {
            'vcode': g_vcode,
            'action': 'add',
            'username': username,
            'realname': realname,
            'phonenumber': phonenumber,
            'email': email,
            'idcardnumber': idcardnumber,
            'subjectid': subjectid,
            #'classlist': json.dumps(newclasslist),
            'classlist': classlist
        }

        response=requests.post(self.URL,data=payload)
        bodyDict = response.json()
        pprint(bodyDict,indent=2)

        #把返回id存到全局变量中
        if idSavedName:

            BuiltIn().set_global_variable('${%s}' % idSavedName,bodyDict['id'])
            print(f"global var set: ${idSavedName}:{bodyDict['id']}")

        return bodyDict


    #修改老师
    def modify_teacher(self,teacherid,realname=None,
                       subjectid=None,classlist=None,
                       phonenumber=None,email=None,idcardnumber=None):
        payload={
            'vcode':g_vcode,
            'action':'modify',
        }
        if realname is not None:
            payload['realname'] = realname
        if subjectid is not None:
            payload['subjectid'] = subjectid
        if phonenumber is not None:
            payload['phonenumber'] = phonenumber
        if email is not None:
            payload['email'] = email
        if idcardnumber is not None:
            payload['idcardnumber'] = idcardnumber
        if classlist is not None:
            # classlist 是这种格式的字符串 "1,2,3"，需要转换为python列表
            classlist = str(classlist)
            newClassList = [{'id': oneid} for oneid in classlist.split(',') if oneid]
            payload['classlist'] = json.dumps(newClassList)


        url='{}/{}'.format(self.URL,teacherid)

        response=requests.put(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict


    #删除老师
    def delete_teacher(self,teacherid):
        payload={
            'vcode':g_vcode,
        }

        url='{}/{}'.format(self.URL,teacherid)

        response=requests.delete(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict


    #删除所有老师
    def delete_all_teachers(self):
        #列出所有班级
        rd = self.list_teacher()
        pprint(rd,indent=2)

        #删除列出的所有班级
        for one in rd['retlist']:
            self.delete_teacher(one['id'])

        rd = self.list_teacher()
        pprint(rd, indent=2)

        #仍有班级，报异常
        if rd['retlist']!=[]:
            raise Exception("cannnot delete all teachers !")


if __name__ == '__main__':
    scm = TeacherLib()

    ret1 = scm.list_teacher()
    #ret2 = scm.add_teacher('ga0','gao','15200000000','123456@qq.com','13000000000','1','[{"id":466283}]')
    # ret3 = scm.list_teacher()
    # ret4 = scm.delete_teacher(212953)
    # ret5 = scm.modify_teacher(139292,'司马中')
    # ret6 = scm.delete_all_teachers()
