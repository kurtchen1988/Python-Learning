#单一分支结构

print("开始")
if 10>5:
    print("选择性语句的执行")
print("结束。。。")

#双向分支结构

num=int(input("请输入一个成绩："))

if num>=60:
    print("result is good")

else:
    print("result is failed")

#巢状分支结构

num = int(input("请输入一个成绩："))

if num>=75:
    if num>=90:
        print("成绩优秀！")
    else:
        print("成绩良好！")
else:
    if num>=60:
        print("成绩及格")
    else:
        print("成绩不及格")