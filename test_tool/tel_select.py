#号码筛选器

def tel_select():
    m_tel_num=['187','139','137','188']#移动
    u_tel_num=['135','130','177','155']#联通
    t_tel_num=['199','133','181','180']#电信

    tel=input('请您输入要查询的手机号：')

    #判断纯数字
    # if tel.isdigit is True:
    if tel.isdigit():
        #判断位数
        if len(tel)==11:
            #切片
            temp=tel[:3]
            if temp in m_tel_num:
                # print('移动')
                return 1
            elif temp in u_tel_num:
                # print('联通')
                return 2
            elif temp in t_tel_num:
                # print('电信')
                return 3
            else:
                # print('没有该号段')
                return 0

        else:
            # print('手机号位数有错误')
            return -1

    else:
        # print('手机号必须为纯数字')
        return -2


print(tel_select())