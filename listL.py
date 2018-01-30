abc=["Python","PHP","R","C#","Go","C++","Java"]
#遍历1
for i in abc:
    print(i)
#遍历2
for i in range(0,len(abc)):
    print(str(i+1)+" times review, the element is: "+str(abc[i]))

abc=("Python","PHP","R","C#","Go","C++","Java")
#遍历1
for i in abc:
    print(i)
#遍历1的变形
n=1
for i in abc:
    print(str(n)+" times, the elements is "+str(i))
    n+=1
#遍历2
for i in range(0,len(abc)):
    print(str(i+1)+" times review, the element is: "+str(abc[i]))

#字典遍历
#key:value
#键：值
msg={"name":"Kurt","Job":"Da Za","email":"ceo@iqianyue.com"}
for i in msg:
    print(i+":"+msg[i])

msg=[{"name":"Kurt","Job":"Da Za","email":"ceo@iqianyue.com"},
    {"name":"okok","Job":"Da Za2","email":"ceo2@iqianyue.com"},
    {"name":"yeye","Job":"Da Za3","email":"ceo3@iqianyue.com"},
    {"name":"hoho","Job":"Da Za4","email":"ceo4@iqianyue.com"}]

for i in msg:
    for j in i:
        print(j+"------"+i[j])
    print("--------------------")