*** Settings ***
#空白数据环境
Library    pylib.SchoolClassLib
Library    pylib.TeacherLib

#Suite Setup   delete_all_school_classes
Suite Setup     Run Keywords   delete_all_teachers   AND
                ...  delete all school classes
