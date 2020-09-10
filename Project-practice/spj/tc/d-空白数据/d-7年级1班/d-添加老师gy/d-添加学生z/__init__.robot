*** Settings ***
#只有一个班级，老师
Library    pylib.SchoolClassLib
#Library    pylib.TeacherLib
Library    pylib.StudentLib


Suite Setup     add_student  ke  ke   1
           ...  ${suite_g7c1_classid}
           ...  suite_student_id

Suite Teardown    delete_student   ${suite_g7c1_classid}


#Suite Teardown    delete_all_students
