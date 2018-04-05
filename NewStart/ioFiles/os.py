import os

def mycopy(file1, file2):

    f1=open(file1,'rb')
    f2=open(file2,'wb')

    content=f1.readline()
    while len(content)>0:
        f2.write(content)
        content=f1.readline()
    f1.close()
    f2.close()

def copydd(dir1, dir2):
    dlist = os.listdir(dir1)
    os.mkdir(dir2)

    for f in dlist:
        file1 = os.path.join(dir1, f)
        file2 = os.path.join(dir2, f)
        if os.path.isfile(file1):
            mycopy(file1,file2)
        if os.path.isdir(file1):
            copydd(file1,file2)


copydd("../ioFiles/aa","../ioFiles/bb")