#乘法口诀
#end=""代表不换行输出
for i in range(1,10):
    for j in range (1,i+1):
        print(str(i)+str("*")+str(j)+"="+str(i*j),end="  ")
    print()
