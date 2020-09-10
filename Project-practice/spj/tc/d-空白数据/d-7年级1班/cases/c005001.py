# -*-coding:utf-8 -*-
from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib
from pylib.WebOpLib import WebOpLib
import json
from fnmatch import fnmatch, fnmatchcase


sc = SchoolClassLib()
st = TeacherLib()
web = WebOpLib()


class c005001:
    def steps(self):
        web.open_browser()

        print('''\n\n***** step 1 **** 列出课程id   \n''')

        #列出课程
        self.ret=sc.list_school_class(1)
        retlist=self.ret['retlist']
        print(retlist)

        #把课程id存到列表,并调整格式
        id=[]
        for i in retlist:
            id.append({"id":i['id']})
            print(id)
        # return id



        print('''\n\n***** step 2 **** 添加一个老师   \n''')

        self.ret1 = st.add_teacher('zhang','zhangke','17600000000',
                                   '123456@qq.com','13500000000',
                                   '1',json.dumps(id))
        print(self.ret1)

        if self.ret1['retcode'] != 0:
            print(self.ret1)
            raise Exception('添加失败')



        print('''\n\n***** step 3 **** 用新建账号登录   \n''')
        web.teacher_login('zhang','888888')

        teacherText=web.get_teacher_homepage_info()
        print(teacherText)

        if teacherText != ['松勤学院01093', 'zhangke', '初中数学', '0', '0', '0']:
            raise Exception('教师信息验证失败')



        print('''\n\n***** step 4 **** 查看学生列表   \n''')
        studentText = web.get_teacher_class_students_info()
        print(studentText)
        # {"七年级'1班'": []}
        if studentText != {"七年级'1班'": []}:
            raise Exception('学生列表不为空')


        web.close_browser()


    def setup(self):
        st.delete_all_teachers()


    def teardown(self):
        st.delete_all_teachers()



if __name__ == '__main__':
    c = c005001()
    c.setup()
    c.steps()
    c.teardown()