# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TabError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# # print(my_abs(-99))
#     # print(my_abs('a'))


# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

import math

def quadratic(a, b, c):
    s = b*b-a*c*4
    if s > 0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/a*2
        x2 = (-b-math.sqrt(b*b-4*a*c))/a*2
        print(round(x1,2), round(x2,2))
    else:
        print('此方程无解')

quadratic(1,8,1)
# print(quadratic(a=1,b=2,c=3))