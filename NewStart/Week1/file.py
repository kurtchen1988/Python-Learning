# Python的文件操作
'''
f = open("../ioFiles/a.txt","r")
content = f.read(5)
print(content)
f.close()
'''
'''
f =open("../ioFiles/a.txt","r")
content=f.readline()
#print(content)
while len(content)>0:
    print(content)
    content=f.readline()

f.close()

print()
print("="*60)

f=open("../ioFiles/a.txt","r")
flist = f.readlines()
for line in flist:
    print(line,end="")
f.close()
'''

f = open("../ioFiles/b.txt","w")
f.write("Hello Python!\n")
f.write("Hello MySQL!\n")

a=["hello world\n","hello html\n","hello php\n"]
f.write(a)
f.close()