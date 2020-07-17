# -*-coding:utf-8 -*-
import requests
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn


class SchoolClassLib:
    url="http://ci.ytesting.com/api/3school/school_classes"


    def list_school_class(self,gradeid=None):
        if gradeid !=None:
            parames={
                'vcode':g_vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            parames={
                'vcode':g_vcode,
                'action':'list_classes_by_schoolgrade',
            }

        response=requests.get(self.url,parames=parames)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)  #indent=2缩进等于二
        return bodyDict

    #加参数idSaveName，获取返回id
    def add_school_class(self,gradeid,name,studentlimit,idSaveName=None):
        payload={
            'vcode':g_vcode,
            'action':'add',
            'grade':int(gradeid),
            'name':name,
            'studentlimit':int(studentlimit),
        }

        response=requests.post(self.url,data=payload)
        bodyDict=response.json()
        pprint(bodyDict,indent=2)

        #idSaveName传值时，需要获取并保存
        if idSaveName:
            BuiltIn().set_global_variable('${%s}'%idSaveName,bodyDict['id'])

        return bodyDict



    def modify_school_class(self,classid,newname,newstudentlimit):
        payload={
            'vcode':g_vcode,
            'action':'modify',
            'name':newname,
            'studentlimit':int(newstudentlimit)
        }

        url='{}/{}'.format(self.url,classid)

        response=requests.put(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict



    def delete_school_class(self,classid):
        payload={
            'vcode':g_vcode,
        }

        url='{}/{}'.format(self.rl,classid)

        response=requests.delete(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict

    def delete_all_school_class(self):
        #列出所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)

        #删除列出的所有班级
        for one in rd['relist']:
            self.delete_school_class(one['id'])

        rd = self.list_school_class()
        pprint(rd, indent=2)

        #仍有班级，报异常
        if rd['retlist']!=[]:
            raise Exception("cannnot delete all school classes!")

        def classlist_should_contain(self,
                                     classlist,classname,
                                     gradename,invitecode,
                                     studentlimit,studentnumber,
                                     classid,expecttimes=1):
            item={
                "name":classname,
                "grade_name":gradename,
                "invitecode":invitecode,
                "studentlimit":int(studentlimit),
                "studentnumber":int(studentnumber),
                "id":classid,
                "classlist":[]
            }

            #检验出现次数
            occurTimes = classlist.count(item)

            #抛异常
            if item not in classlist:
                raise Exception('班级列表中不存在该班级')

            assert occurTimes in int(expecttimes),\
                f'班级列表包含了{occurTimes}次指定信息，' \
                f'期望包含{expecttimes}次！'
