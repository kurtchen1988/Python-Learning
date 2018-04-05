import os

class Week1():

    dirSize = 0
    #目录大小
    bankAccount =[{'cardNum':'123456','name':'chen','passwd':'123456','balance':1000},
                  {'cardNum': '123457', 'name':'zhang', 'passwd': '123456', 'balance': 1001},
                  {'cardNum': '123458', 'name':'wang', 'passwd': '123456', 'balance': 1002},
                  {'cardNum': '123459', 'name':'li', 'passwd': '123456', 'balance': 1003},
                  {'cardNum': '123450', 'name':'zhao', 'passwd': '123456', 'balance': 1004},
                  {'cardNum': '123411', 'name':'huang', 'passwd': '123456', 'balance': 1005},
                  {'cardNum': '123412','name':'tian', 'passwd': '123456', 'balance': 1006}]
    #所有银行账户信息
    bankPerson = {}
    #存储被查询的银行账户

    def whileLoop(self):
        '''
        用while方法显示四种九九乘法效果图
        :return: None
        '''
        a=1
        print("While loop ordered:")

        while(a<10):
            b = 1
            while(b<=a):
                self.display(a, b, a * b, True)
                b+=1
            a+=1
            print("")

        print("="*79)

        c = 9
        while(c>0):
            d = 1
            while(d<=c):
                self.display(c, d, c * d, True)
                d+=1
            c-=1
            print("")

        print("")
        print("While loop reversed:")

        e=1
        while(e<10):
            f=e
            while(f>0):
                self.display(f,e,f*e, False)
                f-=1
            e+=1
            print("")

        print("=" * 79)

        g=9
        while(0<g<10):
            h=g
            while(h>0):
                self.display(h,g,h*g, False)
                h-=1
            g-=1
            print("")

    def forLoop(self):
        '''
        用for in方法显示四种九九乘法效果图
        :return: None
        '''
        print("For in loop ordered:")
        for a in range(1,10):
            for b in range(1,a+1):
                self.display(a, b, a*b, True)
            print("")

        print("="*79)

        for c in range(9,0,-1):
            for d in range(c,0,-1):
                self.display(c,d,c*d, True)
            print("")

        print("For in loop reversed:")
        for e in range(1,10):
            for f in range(e,0,-1):
                self.display(f, e, e*f, False)
            print("")

        print("="*79)

        for g in range(9,0,-1):
            for h in range(g,0,-1):
                self.display(h,g,g*h, False)
            print("")


    def display(self,i,j,k,order):
        '''
        处理乘法表显示
        有四个参数，前三个为int，最后一个为bool，前三分别表示被乘数，乘数和结果，最后一个参数表示是否正序显示
        :return: None
        '''
        if(order==True):
            print("{}*{}={:<4}".format(i,j,k),end=' ')
        elif(order==False):
            a=" "*(9-j)*9
            if(i==j):
                print(a+"{}*{}={:<4}".format(i, j, k), end=' ')
            else:
                print("{}*{}={:<4}".format(i, j, k), end=' ')
        else:
            print("程序错误")

    def calSize(self,dir):
        '''
        计算文件夹的大小
        :param dir:文件夹路径
        :return: None
        '''
        if(os.path.isdir(dir)):
            dlist = os.listdir(dir)
            for f in dlist:
                file1 = os.path.join(dir, f)
                if os.path.isdir(file1):
                    self.calSize(file1)
                if os.path.isfile(file1):
                    self.dirSize=self.dirSize+os.path.getsize(file1)
                print("文件夹大小为： " + str(self.dirSize) + " Bytes")
        else:
            print("输入的并不是正确的路径，请重新执行程序")

    def calEntry(self):
        '''
        计算文件夹大小的入口程序，控制输入文件夹路径
        :return:
        '''
        folder = str(input("请输入文件夹路径:"))
        self.calSize(folder)

    def login(self, accountNum, passWD):
        '''
        控制登录
        :param accountNum:银行账户
        :param passWD: 密码
        :return: 登录成功为True,登录失败为False
        '''
        for i in range(len(self.bankAccount)):
            if(self.bankAccount[i]["cardNum"]==accountNum and self.bankAccount[i]["passwd"]==passWD):
                self.bankPerson=self.bankAccount[i]
                self.bankPerson["id"]=i
                return True
            else:
                return False

    def showBalance(self):
        '''
        显示余额功能
        :return: None
        '''
        print("您的余额为："+str(self.bankPerson["balance"]))

    def withDraw(self,debt):
        '''
        取钱功能
        :param debt: 取出的钱数
        :return: None
        '''
        if(int(debt)<0):
            print("对不起，您输入的金额有误，请重试")
        else:
            if(self.bankPerson["balance"]-int(debt)<0):
                print("对不起，您输入的金额超出您的余额，请重试")
            else:
                print("取钱成功！")
                self.bankPerson["balance"]=self.bankPerson["balance"]-int(debt)
                self.bankAccount[self.bankPerson["id"]]["balance"]=self.bankPerson["balance"]

    def deposite(self,credit):
        '''
        存钱功能
        :param credit: 存入的钱数
        :return: None
        '''
        if (int(credit) < 0):
            print("对不起，您输入的金额有误，请重试")
        else:
            print("存钱成功！")
            self.bankPerson["balance"] = self.bankPerson["balance"] + int(credit)
            self.bankAccount[self.bankPerson["id"]]["balance"] = self.bankPerson["balance"]

    def bankEntry(self):
        '''
        银行系统进入程序。主要控制界面显示和业务逻辑
        :return: None
        '''
        if (len(self.bankAccount) == 0):
            print("=================银行系统有误，没有任何账户信息！===================")
        else:
            while True:
                print("=" * 12, "银行管理系统", "=" * 14)
                print("{0:1} {1:13} {2:15}".format(" ", "1. 登录账户", "2. 退出"))
                print("=" * 40)
                key = input("请输入对应的选择：")
                # 根据键盘值，判断并执行对应的操作
                if key == "1":
                    account=str(input("请输入账户,返回请按回车："))
                    passwd=str(input("请输入密码,返回请按回车："))
                    if(self.login(account, passwd)==True):
                        while len(self.bankPerson)!=0:
                            personAccount=self.bankPerson
                            print("=" * 12, personAccount["name"]+" 欢迎光临！", "=" * 11)
                            print("{0:1} {1:13} {2:15}".format(" ", "1. 查询余额", "2. 取钱"))
                            print("{0:1} {1:13} {2:17}".format(" ", "3. 存钱", "4. 退出"))
                            print("=" * 40)
                            keyin = input("请输入对应的选择：")
                            if keyin=="1":
                                print("=" * 12, personAccount["name"] + " 查询余额", "=" * 13)
                                self.showBalance()
                                input("按回车键继续")
                            elif keyin=="2":
                                print("=" * 12, personAccount["name"] + " 取钱", "=" * 14)
                                debt=input("请输入取钱金额：")
                                self.withDraw(debt)
                                self.showBalance()
                                input("按回车键继续")
                            elif keyin=="3":
                                print("=" * 12, personAccount["name"] + " 存钱", "=" * 14)
                                credit = input("请输入存钱金额：")
                                self.deposite(credit)
                                self.showBalance()
                                input("按回车键继续")
                            elif keyin=="4":
                                self.bankPerson={}
                                print("=" * 12, "您已成功退出账户 ", "=" * 14)
                                input("按回车键继续")
                                break
                    else:
                        print("======== 账号或者密码输入错误！ ==========")
                        input("按回车键继续")
                elif key == "2":
                    print("=" * 12, "再见", "=" * 14)
                    break
                else:
                    print("======== 无效的键盘输入！ ==========")

if __name__== "__main__":
    '''
    入口函数，分别调用各个方法。可以单独调用每个方法来测试。
    '''
    a = Week1()
    #a.whileLoop() #用while循环跑出4种九九乘法表
    #a.forLoop() #用for循环跑出4中九九乘法表
    #a.calEntry() #计算文件夹大小
    a.bankEntry()