a=[["a1","b1","c1","d1"],["a2","b2","c2","d2"],["a3","b3","c3","d3"],["a4","b4","c4","d4"]]
b=[[1,2,4,4],[1,1,1,1],[1,1,2,2],[1,2,3,4]]
#print(a[0])
#print(a[0][2])
'''
for i in range(0,4):
    for j in range(1,4):
        if (b[i][j-1]==b[i][j]):
            b[i][j-1]=b[i][j]*2
            b[i][j] = 0
'''
for i in range(0,4):
    for j in range(1,4):
        if (b[i][j]==b[i][j-1]):
            b[i][j]=b[i][j-1]*2
            b[i][j - 1] = 0
'''
for i in range(0,4):
    for j in range(1,4):
        if (b[i][j]==b[i][j-1]):
            b[i][j] = b[i][j-1] * 2
            b[i][j-1]=0
'''

print(b)

'''
for i in range(0, 4):
    for j in range(1,4):
        if(b[i][j-1]==b[i][j]):
            print(j)
'''
    #print(i)

        #if(b[i][])

        #print(n)

        #print(j)
        #if (j<3):
         #print(b[i][j + 1])
        #if (i < 3 & j == b[i][j + 1]):
            #print(j)
            #b[i][j] = j * 2
            #b[i][j + 1] = 0

#print(b)
