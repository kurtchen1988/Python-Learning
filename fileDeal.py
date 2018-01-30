import os

class fileProcess:
#读取文件夹下所有文件名

    def __init__(self,filePath):
        self.filePath=filePath

    def readFolder(self):
        return os.listdir(self.filePath)

class fileContent:
#读取文件内容

    def __init__(self,filePath,fileName):
        self.filePath=filePath
        self.fileName=fileName

    def readContent(self):
        content=open(str(self.filePath)+"/"+str(self.fileName),"r")
        read=content.read()
        content.close()
        return read

class zeroReplace:
#替换数字

    i=[0,1,2,3,4,5,6,7,8,9]

    def __init__(self,content):
        self.content=content

    def replaceZero(self):
        preContent=self.content
        for a in preContent:
            for b in self.i:
                if(str(b)==str(a)):
                    preContent=preContent.replace(a,"")

        return preContent


class contentWrite:
#写入文件

    def __init__(self,newPath,newFile,newContent):
        self.newPath=newPath
        self.newFile=newFile
        self.newContent=newContent

    def writeFile(self):
        writeTo=open(str(self.newPath)+"/"+str(self.newFile),"w")
        writeTo.write(self.newContent)
        writeTo.close()


class mainProgram:
#主程序与程序入口

    def __init__(self):
        print("请输入文件夹目录（注意文件夹分隔符用/）：")
        inputA=input()
        folderName=fileProcess(str(inputA)).readFolder()
        print("以下为输入的文件夹内的所有文件名：")
        for i in folderName:
            print(i)
        print("请输入去除数字后的文件拷贝目录（注意文件夹分隔符用/）")
        inputB=input()
        for a in folderName:
            contentWrite(str(inputB),a,zeroReplace(fileContent(str(inputA),a).readContent()).replaceZero()).writeFile()


if __name__ == "__main__":
   mainProgram()
