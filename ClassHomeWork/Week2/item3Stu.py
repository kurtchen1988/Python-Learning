import pymysql

class stuManage():
    '''
    在运行本程序之前，请先执行在根目录下的student.sql创建好数据库与表
    '''


    def __init__(self):
        '''
        构造方法，数据库连接。为了准从原程序，这里把数据库里的信息封装入stulist字典列表中，stulist字典当中仅加一个id项。
        '''
        try:
            db = pymysql.connect(host="localhost",user="root",password="root",db="stumanage",charset="utf8")
            self.cursor = db.cursor()
            print("成功建立连接!")
            self.stulist = self.findAll()
            print("数据成功读取，进入程序")
        except Exception as error:
            print("数据库连接失败或数据读取失败，具体错误为： ",error)

    def findAll(self):
        sqlID = "select id from student order by id"
        sqlName = "select name from student order by id"
        sqlAge = "select age from student order by id"
        sqlClass = "select classid from student order by id"

        allCursor = self.cursor
        stu = []


        try:
            allCursor.execute(sqlID)
            a = allCursor.rowcount
            ID = allCursor.fetchall()
            allCursor.execute(sqlName)
            Name = allCursor.fetchall()
            allCursor.execute(sqlAge)
            Age = allCursor.fetchall()
            allCursor.execute(sqlClass)
            Class = allCursor.fetchall()

            for i in range(0,a):
                stuSin = {}
                stuSin['id']= ID[i][0]
                stuSin['name'] = Name[i][0]
                stuSin['age'] = Age[i][0]
                stuSin['classid'] = Class[i][0]
                stu.append(stuSin)
            return stu
        except Exception as error:
            print("系统处理数据时遇到错误，具体错误为：",error)
            pass

    def delete(self, id):
        sql ="delete from student where id = '%d'"%(id)
        try:
            self.cursor.execute(sql)
            print("成功删除！")
        except Exception as error:
            print("未能删除记录，具体信息为：",error)

    def insert(self, data):
        sql = "insert into student(name,age,classid) values ('%s','%d','%s')"%(data)
        try:
            self.cursor.execute(sql)
            print("成功添加记录！")
        except Exception as error:
            print("未能添加记录，具体信息为：",error)

    def showStu(self, stulist):
        if len(stulist)==0:
            print("---------没有学员信息可以输出---------")
            return
        print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format("sid","name","age","classid"))
        print("-"*40)
        for i in range(len(stulist)):
            print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format(stulist[i]['id'], stulist[i]['name'], stulist[i]['age'], stulist[i]['classid']))

    def programCon(self):
        while True:
            print("="*12,"学员管理系统","="*14)
            print("{0:1} {1:13} {2:15}".format(" ","1. 查看学员信息", "2. 添加学员信息"))
            print("{0:1} {1:13} {2:15}".format(" ","3. 删除学员信息","4. 退出系统"))
            print("="*40)
            key = input("请输入对应的选择")
            if key == "1":
                print("="*12,"学员信息浏览","="*14)
                self.showStu(self.findAll())
                input("按回车键继续：")
            elif key == "2":
                print("="*12,"学员信息添加","="*14)

                stuName = input("请输入要添加的学生姓名：")
                stuAge = input("请输入要添加的学生年龄：")
                stuClass = input("请输入要添加的课程ID：")
                stu = (str(stuName),int(stuAge),str(stuClass))
                self.insert(stu)
                self.showStu(self.findAll())
                input("按回车键继续：")
            elif key == "3":
                print("="*12,"学员信息删除","="*14)
                self.showStu(self.findAll())
                sid = input("请输入你要删除的信息id号：")
                self.delete(int(sid))
                self.showStu(self.findAll())
                input("按回车键继续：")
            elif key == "4":
                print("="*12,"再见","="*14)
                break
            else:
                print("==========无效的键盘输入===========")

if __name__ == '__main__':
    a=stuManage()
    a.programCon()