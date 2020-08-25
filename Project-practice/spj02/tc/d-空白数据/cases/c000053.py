from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c000053:
    def steps(self):
        print('''\n\n***** step 1 ****  修改班级 7年级8班 \n''')
        self.ret1 = sc.modify_school_class(9999999999999999, '8班', 80)

        if self.ret1['retcode'] != 404:
            print(self.ret1)
            raise Exception('返回值不正确')



    def setup(self):

        print('''\n\n***** step 1 ****  添加 7年级7班 \n''')
        self.ret2 = sc.add_school_class(1, '7班', 70)

        if self.ret2['retcode'] != 0:
            print(self.ret2)
            raise Exception('返回值非0,添加班级不成功')

    def teardown(self):
        sc.delete_school_class(self.ret2['id'])
