

a=[["a1","b1","c1","d1"],["a2","b2","c2","d2"],["a3","b3","c3","d3"],["a4","b4","c4","d4"]]
b=[[1,2,4,4],[2,0,0,0],[1,1,2,0],[1,2,3,4]]
#n=[2,3,4,5]


def proData(qipan):
    # 处理棋盘一行数据
    temp = [0, 0, 0, 0]
    pos = 0
    for i in range(0, 4):
        # 左移不为0的数据
        if (qipan[i] != 0):
            temp[pos] = qipan[i]
            pos += 1
    qipan = temp
    #print(qipan)
    for j in range(0, 3):
        # 合并相同的数字
        if (qipan[j] == qipan[j + 1]):
            qipan[j] = qipan[j + 1] * 2
            qipan[j + 1] = 0
            #print(j)
        #print(j)
    return qipan
'''
w=[0,0,0,0]
for i in range(0,4):
    for j in range(3,-1,-1):
        w[i]=n[j]
print(w)


a=[0,0,0,0]
w=0

for i in b:
    n = 0
    for j in range(3, -1, -1):
        a[n]=i[j]
        n += 1
    b[w] = proData(a)
    w+=1

h=[0,0,0,0]
l=0

for m in b:
    g = 0
    for f in range(3, -1, -1):
        h[g]=m[f]
        g += 1
    b[l] = proData(h)
    l+=1


a = [0, 0, 0, 0]
w = 0

for i in b:
    n = 0
    for j in range(3, -1, -1):
        a[n] = i[j]
        n += 1
    b[w] = proData(a)
    w += 1

h=[0,0,0,0]
z=0
for x in b:
    m=0
    for y in range(3,-1,-1):
        h[m]=x[y]
        m+=1
    #print(h)
    b[z]=h
    print(z)
    print(y)
    print(m)

    z+=1
    #print(z)

#print(b)



a = [0, 0, 0, 0]
for i in range(0, 4):
    k = 0
    for j in range(3,-1,-1):
        a[k] = b[j][i]
        k += 1
    a = proData(a)
    k = 0
    for j in range(3,-1,-1):
        b[j][i] = a[k]
        k += 1

print(b)

'''

