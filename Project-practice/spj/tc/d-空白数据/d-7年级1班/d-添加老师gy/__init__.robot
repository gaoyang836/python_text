*** Settings ***
#只有一个班级，老师
Library    pylib.SchoolClassLib
Library    pylib.TeacherLib


#添加一个老师
Suite Setup    add_teacher   yang  yang  15200000000   123456@qq.com  13000000000
           ...  1
           ...  [{"id":${suite_g7c1_classid}}]
           ...  suite_math_teacher_id

Suite Teardown    delete_teacher   ${suite_math_teacher_id}
