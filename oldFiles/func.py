'''
#作用域
i=10
def func():
    j=10
    print(j)
print(i)
func()
#print(j)
'''

'''
函数定义的格式
def 函数名（参数）：
函数体
'''
def abc():
    print("abcde")
    print("456")
#调用函数：函数名（参数）
abc()

#参数：与外界沟通的接口
#参数：形参和实参
#一般在函数定义的时候使用的参数是形参
#一般在函数调用的时候使用的参数是实参
def func2(a,b):
    if(a>b):
        print(str(a)+" is larger than "+str(b))
    else:
        print(str(b)+" is larger than "+str(a)+", or they are equal")
#4,5
func2(9,5)
func2(10,9)
