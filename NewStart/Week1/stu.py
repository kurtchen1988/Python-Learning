#输出初始界面

stulist=[
    {'name':'zhangsan','age':20,'classid':'python02'},
    {'name':'lisi','age':22,'classid':'python03'},
    {'name':'wangwu','age':25,'classid':'python04'}]

def showStu(stulist):
    if len(stulist)==0:
        print("---------没有学员信息可以输出---------")
        return
    print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format("sid","name","age","classid"))
    print("-"*40)
    for i in range(len(stulist)):
        print("|{0:<5}|{1:<10}|{2:<5}|{3:<10}|".format(i+1, stulist[i]['name'], stulist[i]['age'], stulist[i]['classid']))

while True:
    print("="*12,"学员管理系统","="*14)
    print("{0:1} {1:13} {2:15}".format(" ","1. 查看学员信息", "2. 添加学员信息"))
    print("{0:1} {1:13} {2:15}".format(" ","3. 删除学员信息","4. 退出系统"))
    print("="*40)
    key = input("请输入对应的选择")
    if key == "1":
        print("="*12,"学员信息浏览","="*14)
        showStu(stulist)
        input("按回车键继续：")
    elif key == "2":
        print("="*12,"学员信息添加","="*14)
        stu={}
        stu['name']=input("请输入要添加的姓名：")
        stu['age'] = input("请输入要添加的姓名：")
        stu['classid'] = input("请输入要添加的姓名：")
        stulist.append(stu)
        showStu(stulist)
        input("按回车键继续：")
    elif key == "3":
        print("="*12,"学员信息删除","="*14)
        showStu(stulist)
        sid = input("请输入你要删除的信息id号：")
        del stulist[int(sid)-1]
        showStu(stulist)
        input("按回车键继续：")
    elif key == "4":
        print("="*12,"再见","="*14)
        break
    else:
        print("==========无效的键盘输入===========")