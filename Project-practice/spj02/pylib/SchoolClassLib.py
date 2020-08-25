# -*-coding:utf-8 -*-
import requests
from cfg import g_vcode
from pprint import pprint
from robot.api import logger

class SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    # 列出班级
    def list_school_class(self,gradeid=None):

        params = {
            'vcode': g_vcode,
            'action': 'list_classes_by_schoolgrade',
        }
        if gradeid != None:
            params['gradeid'] = int(gradeid)


        response = requests.get(self.URL, params=params)
        bodyDict=response.json()

        pprint(bodyDict,indent=2)  #indent=2缩进等于二
        return bodyDict



    # 添加班级
    #加参数idSaveName，获取返回id
    def add_school_class(self,gradeid,name,studentlimit,idSaveName=None):
        payload = {
            'vcode': g_vcode,
            'action': 'add',
            'grade': int(gradeid),
            'name': name,
            'studentlimit': int(studentlimit),
        }

        response=requests.post(self.URL,data=payload)
        bodyDict=response.json()
        pprint(bodyDict,indent=2)

        # #idSaveName传值时，需要获取并保存
        # if idSaveName:
        #     BuiltIn().set_global_variable('${%s}'%idSaveName,bodyDict['id'])

        return bodyDict


    #修改学生
    def modify_school_class(self,classid,newname,newstudentlimit):
        payload={
            'vcode':g_vcode,
            'action':'modify',
            'name':newname,
            'studentlimit':int(newstudentlimit)
        }

        url='{}/{}'.format(self.URL,classid)

        response=requests.put(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict



    #删除学生
    def delete_school_class(self,classid):
        payload={
            'vcode':g_vcode,
        }

        url='{}/{}'.format(self.URL,classid)

        response=requests.delete(url,data=payload)

        bodyDict=response.json()

        pprint(bodyDict,indent=2)
        return bodyDict



    #删除所有学生
    def delete_all_school_classes(self):
        #列出所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)

        #删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        rd = self.list_school_class()
        pprint(rd, indent=2)

        #仍有班级，报异常
        if rd['retlist']!=[]:
            raise Exception("cannnot delete all school classes!")

    def classlist_should_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid,
                                expectedtimes=1
                                    ):

        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []
        }

        occurTimes = classlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != expectedtimes:
            # 通过抛出异常来让关键字Fail

            raise Exception(
                'class list contain your class info {} times,expect {} times!!'.format(
                    occurTimes, expectedtimes)
            )



    def classlist_should_not_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid
                                    ):

        item = {
            "name": classname,
            "grade__name": gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []
        }

        occurTimes = classlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes > 0:
            # 通过抛出异常来让关键字Fail

            raise Exception('班级包含了指定班级信息')







if __name__ == '__main__':
    scm = SchoolClassLib()

    ret1 = scm.list_school_class(1)
    #
    # ret2 = scm.add_school_class(1,'1班',60)
    #
    # ret3 = scm.list_school_class(1)
    #
    # ret4 = scm.delete_all_school_classes()