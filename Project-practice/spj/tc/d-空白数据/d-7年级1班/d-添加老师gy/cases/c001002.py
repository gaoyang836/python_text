from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib

import json

sc = SchoolClassLib()
st = TeacherLib()


class c001002:

    def steps(self):
        print('''\n\n***** step 1 **** 列出课程id   \n''')

        # 列出课程
        self.ret = sc.list_school_class(1)
        retlist = self.ret['retlist']
        print(retlist)

        # 把课程id存到列表,并调整格式
        id = []
        for i in retlist:
            id.append({"id": i['id']})
            print(id)


        print('''\n\n***** step 2 **** 添加一个老师   \n''')

        self.ret1 = st.add_teacher('zhang', 'zhangke', '17600000000', '123456@qq.com', '13500000000', '1',
                                   json.dumps(id))
        print(self.ret1)

        if self.ret1['retcode'] != 0:
            print(self.ret1)
            raise Exception('添加失败')




        print('''\n\n***** step 3 **** 获取教师id   \n''')

        global teacherid
        teacherid = self.ret1['id']
        print(teacherid)

        self.teacherid = self.ret1['id']

        list = st.list_teacher()
        retid = list['retlist'][0]['id']

        if teacherid != retid:
            raise Exception('未找到该教师id')

        return teacherid



    def setup(self):
        pass



    def teardown(self):
        st.delete_teacher(teacherid)



if __name__ == '__main__':
    c = c001002()
    c.setup()
    c.steps()
    c.teardown()