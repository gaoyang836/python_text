# -*-coding:utf-8 -*-
# -*-coding:utf-8 -*-
# -*-coding:utf-8 -*-
from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib
from pylib.WebOpLib import WebOpLib
import json
from fnmatch import fnmatch, fnmatchcase


sc = SchoolClassLib()
st = TeacherLib()
web = WebOpLib()


class c005101:

    def steps(self):
        web.open_browser()

        print('''\n\n***** step 1 **** 教师登录   \n''')
        web.teacher_login('yang','888888')

        teacherText = web.get_teacher_homepage_info()
        print(teacherText)


        print('''\n\n***** step 2 **** 发布作业   \n''')
        web.teacher_deliver_task('测试作业第一个')


        print('''\n\n***** step 3 **** 学生登录做作业   \n''')
        web.student_login('ke','888888')
        web.studentDoExam()


        print('''\n\n***** step 4 **** 教师登录检查   \n''')
        web.teacher_login('yang','888888')


        student_task=web.teacher_get_latest_student_task()

        if student_task != ['A','A','A']:
            raise Exception('教师作业验证失败')



        web.close_browser()


    def setup(self):
        pass



    def teardown(self):
        pass



if __name__ == '__main__':
    c = c005101()
    c.setup()
    c.steps()
    c.teardown()