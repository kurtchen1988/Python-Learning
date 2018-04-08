'''
print("start......")
try:
    a=int(input("请输入一个值："))
    print("你输入的值：",a)
    print(100/a)
except ValueError:
    print("值错误")
except ZeroDivisionError:
    print("除数为0错误")
except:
    print("未知错误")
'''

print("end")

print("start......")
try:
    a=int(input("请输入一个值："))
    print("你输入的值：",a)
    print(100/a)
except (ValueError, ZeroDivisionError) as info:
    print("错误,原因为: ",info)
    raise #再次将当前错误抛出
except:
    print("未知错误")


print("end")
