"""
   计算器功能（加减乘除）
"""
class Calculator():
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    #1. 加法
    def add(self):
        return self.a+self.b
    #2. 减法
    def sub(self):
        return self.a-self.b
    #3. 乘法
    def mul(self):
        return self.a*self.b
    #4. 除法
    def div(self):
        return self.a/self.b

    # 5. 加法2
    def add2(self,x,y):
        # if x==1:
        #     return 0
        return x + y

if __name__ == '__main__':
    calculator = Calculator(9, 3)
    print(calculator.add())
    print(calculator.sub())
    print(calculator.mul())
    print(calculator.div())
    print(calculator.add2(3,4))