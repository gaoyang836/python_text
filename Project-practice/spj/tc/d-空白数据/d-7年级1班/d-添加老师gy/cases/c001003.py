from pylib.SchoolClassLib import SchoolClassLib
from pylib.TeacherLib import TeacherLib

import json

sc = SchoolClassLib()
st = TeacherLib()


class c001003:
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
            #print(id)
            return id

        print('''\n\n***** step 2 **** 添加一个老师   \n''')

        self.ret1 = st.add_teacher('gao','gaoyang','15200000000', '123456@qq.com', '13000000000', '1',
                                   json.dumps(id))
        print(self.ret1)

        if self.ret1['retcode'] != 1:
            print(self.ret1)
            raise Exception('添加同名课程失败')


    def setup(self):
        pass

    def teardown(self):
        pass

if __name__ == '__main__':
    c = c001003()
    c.setup()
    c.steps()
    c.teardown()