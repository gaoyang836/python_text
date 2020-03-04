#号码筛选器

#答案
# def tel_select():
#     m_tel_num=['187','139','137','188']#移动
#     u_tel_num=['135','130','177','155']#联通
#     t_tel_num=['199','133','181','180']#电信
#
#     tel=input('请您输入要查询的手机号：')
#
#     #判断纯数字
#     # if tel.isdigit is True:
#     if tel.isdigit():
#         #判断位数
#         if len(tel)==11:
#             #切片
#             temp=tel[:3]
#             if temp in m_tel_num:
#                 # print('移动')
#                 return 1
#             elif temp in u_tel_num:
#                 # print('联通')
#                 return 2
#             elif temp in t_tel_num:
#                 # print('电信')
#                 return 3
#             else:
#                 # print('没有该号段')
#                 return 0
#
#         else:
#             # print('手机号位数有错误')
#             return -1
#
#     else:
#         # print('手机号必须为纯数字')
#         return -2
#
#
# print(tel_select())

#三大运营商号段

#移动
m_tel_num=['134','135','136','137','138','139','147','150','151',
           '152','155','157','158','159','182','183','187','188','198']
#电信
t_tel_num=['133','149','153','173','177','180','181','189','199']
#联通
u_tel_num=['130','131','132','145','155','156','166','171','175','176','185','186']


#查询封装成一个函数
def phone_Operator():

    phone=input('请输入您想查询的手机号码：')
    # 先判断是否纯数字
    if phone.isdigit():
        # 再判断是否11位
        if len(phone) ==11:
            phone_num = phone[:3]   #切片取前三位，判断号段
            if phone_num in m_tel_num:
                print('您的手机号运营商为：中国移动')
                return 11
            elif phone_num in t_tel_num:
                print('您的手机号运营商为：中国电信')
                return 12
            elif phone_num in m_tel_num:
                print('您的手机号运营商为：中国联通')
                return 13
            else:
                #注意前三位不属于任何号段的情况
                print('无该号段手机号,请重新输入！')
                return 20
        else:
            print('手机号应为11位,请重新输入！')
            return 30
    else:
        print('手机号请输入纯数字,请重新输入！')
        return 40
#取返回值
status = str(phone_Operator())
#状态位数第二位是0的，都是没有判断出运营商的，前一位方便区分不同情况
#状态位数第一位是1的，都是判断出运营商的，后一位方便区分不同运营商

# print(type(status[-1:]))

#判断用户没有判断出手机号运营商的，需要重新输入
while True:
    if status[-1:] is '0':
        phone_Operator()
    else:
        break


