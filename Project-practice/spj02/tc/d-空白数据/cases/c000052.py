from pylib.SchoolClassLib import SchoolClassLib

sc = SchoolClassLib()


class c000052:

    def steps(self):
        print('''\n\n***** step 1 ****  修改班级 7年级5班为6班 \n''')
        self.ret1 = sc.modify_school_class(self.ret2['id'], '6班', 60)

        if self.ret1['retcode'] != 1:
            print(self.ret1)
            raise Exception('返回值不正确')


    def setup(self):

        print('''\n\n***** step 1 ****  添加 7年级5班 \n''')
        self.ret2 = sc.add_school_class(1, '5班', 50)

        if self.ret2['retcode'] != 0:
            print(self.ret2)
            raise Exception('返回值非0,添加班级不成功')


        print('''\n\n***** step 2 ****  添加 7年级6班 \n''')
        self.ret3 = sc.add_school_class(1, '6班', 60)

        if self.ret3['retcode'] != 0:
            print(self.ret3)
            raise Exception('返回值非0,添加班级不成功')


    def teardown(self):
        sc.delete_school_class(self.ret2['id'])
