# -*-coding:utf-8 -*-

from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib
from pylib.StudentLib import StudentLib

from cfg import g_subject_7_id
#from loguru import logger

sc = SchoolClassLib()
st = TeacherLib()
ss = StudentLib()

class c002001:


    def listSchoolClass(self):
        # 列出七年级一班班级id
        return sc.list_school_class(g_subject_7_id)


    def saveClassId(self,retlist):
        # 把列出课程的返回值中的name为'1班'的classId取出来i[id]
        return [i['id'] for i in retlist if '1班' in i['name']]


    def add_student(self,classId):
        # 添加一个学生七年级

        return ss.add_student("zhang","zhang",g_subject_7_id,
                              classId,17600000000)


    def steps(self):
        print('\n\n***** step 1 **** 列出课程id   \n')
        # 列出课程
        ret = self.listSchoolClass()
        retlist = ret['retlist']
        print(ret)


        # 把课程id存到列表,并调整格式
        classId = self.saveClassId(retlist)


        print('\n\n***** step 2 **** 添加一个学生   \n')
        ret1 = self.add_student(classId)
        retcode = ret1['retcode']
        print(ret1)


        if retcode != 0:
            print(ret)
            raise Exception('添加失败')


        print('''\n\n***** step 3 **** 获取学生的id   \n''')
        studentId = ret1['id']
        print(studentId)

        studentList=ss.list_student()
        retId=studentList['retlist'][0]['id']

        if studentId != retId:
            raise Exception('未找到该学生id')


    def setup(self):
        ss.delete_all_students()


    def teardown(self):
        ss.delete_all_students()



if __name__ == '__main__':
    c = c002001()
    c.setup()
    c.steps()
    c.teardown()