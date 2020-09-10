*** Settings ***
#只有一个班级
Library    pylib.SchoolClassLib
Library    pylib.TeacherLib


Suite Setup     add_school_class    1   '1班'  0   suite_g7c1_classid
Suite Teardown    delete_school_class   ${suite_g7c1_classid}