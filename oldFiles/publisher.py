import re
import urllib.request

class getPublisher():

    url="https://read.douban.com/provider/all"
    pat="\"name\">{1}\w+</{1}"
    pat2=">\w+<"
    filePath="D:/Python/练习/iofile/1.txt"

    def getContent(self):
        content=urllib.request.urlopen(self.url).read().decode("UTF-8")
        return content

    def findContent(self):
        #print(self.pat)
        #return re.match(self.pat,content)
        content=self.getContent()
        a=re.compile(self.pat).findall(content)
        #aPro=re.compile(self.pat2).findall(a)
        b=[]
        c=[]
        x=0
        for j in a:
            b.append(re.compile(self.pat2).findall(j))
            #i+=1
        for i in range(0,len(b)):
            c.append(str(b[i]).replace("<","").replace(">",""))
        return c

    def writeFile(self):
        a=open(self.filePath,"w")
        for b in self.findContent():
            for c in b:
                a.write(c)

        a.close()


if __name__ == "__main__":
    getPublisher().writeFile()