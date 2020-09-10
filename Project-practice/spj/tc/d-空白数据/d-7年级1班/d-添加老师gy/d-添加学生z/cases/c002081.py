# -*-coding:utf-8 -*-
# -*-coding:utf-8 -*-

from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib
from pylib.StudentLib import StudentLib

from cfg import g_subject_7_id
#from loguru import logger

sc = SchoolClassLib()
st = TeacherLib()
ss = StudentLib()

class c002081:


    def listSchoolClass(self):
        # 列出七年级一班班级id
        return sc.list_school_class(g_subject_7_id)


    def saveClassId(self,retlist):
        # 把列出课程的返回值中的name为'1班'的classId取出来i[id]
        return [i['id'] for i in retlist if '1班' in i['name']]


    def add_student(self,classId):
        # 添加一个学生七年级

        return ss.add_student("ke","ke",g_subject_7_id,
                              classId,18700000000)


    def steps(self):
        print('\n\n***** step 1 **** 列出课程id   \n')
        # 列出课程
        ret = self.listSchoolClass()
        retlist = ret['retlist']
        print(ret)


        # 把课程id存到列表,并调整格式
        classId = self.saveClassId(retlist)



        print('\n\n***** step 2 **** 添加一个学生   \n')
        # 先列出学生
        bStudentlist = ss.list_student()

        #d-添加学生z
        ret1 = self.add_student(classId)
        retcode = ret1['retcode']
        print(ret1)


        if retcode != 0:
            print(ret)
            raise Exception('添加失败')



        print('''\n\n***** step 3 **** 获取学生的id   \n''')
        studentId = ret1['id']
        print(studentId)

        #校验添加成功
        studentList=ss.list_student()
        retId=studentList['retlist'][0]['id']

        if studentId != retId:
            raise Exception('未找到该学生id')



        print('''\n\n***** step 4 **** 删除学生   \n''')
        #删除学生
        deleteSSList=ss.delete_student(studentId)
        deleteSSRecode=deleteSSList['retcode']

        if deleteSSRecode != 0:
            print(deleteSSList)
            raise Exception('删除失败')


        # 后列出学生
        aStudentlist = ss.list_student()
        if aStudentlist != bStudentlist:
            raise Exception('删除校验失败')



    def setup(self):
        pass


    def teardown(self):
        ss.delete_all_students()



if __name__ == '__main__':
    c = c002081()
    c.setup()
    c.steps()
    c.teardown()