import urllib.request
import re
import os

class JDPachong:

    urlPage = "https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&page="
    #每一页的url
    urlComment = "https://sclub.jd.com/comment/productPageComments.action?score=0&sortType=5&pageSize=10&productId="
    #评论的url
    times = 50
    #普通商品执行多少页数
    pageNum = 1
    #普通商品开始页码
    commTimes = 2
    #详细评论执行多少页数
    commNum = 1
    #详细评论的开始页码
    patName = '<div class="p-name p-name-type-2">.*?<em>(.*?)</em>'
    #商品名称正则
    patPrice = '<em>￥</em><i>(.*?)</i></strong>'
    #商品价格正则
    patComment = '<div class="p-commit">.*?<strong>.*?>(.*?)</strong>'
    #商品评价个数正则
    patStore = '<div class="p-shop".*?>(.*?)</div>'
    #商品商店正则
    patProdID = 'data-pid="(.*?)"'
    #商品ID正则
    patDetail = '"content":"(.*?)"'
    #详细评论正则
    storeKey = {"商品名称":"","商品价格":"","商品评论数":"","商品出售方":""}
    #储存商品信息的字典
    nameData = []
    #储存商品名称的列表
    priceData = []
    #储存商品价格的列表
    commentData = []
    #储存商品评论个数的列表
    storeData = []
    #存储商品商店信息的列表
    IDData = []
    # 存储商品ID
    comDetaData = []
    # 存储商品详细评论信息的列表
    folder = "D:\\Python\\练习\\iofile\\"
    #存储文件的目录
    fileName = "JDProdInfo"
    #存储商品信息文件的名称


    def __init__(self):
    #构造函数，同样是程序的主控
        for i in range(0,self.times):
            thisurl=self.urlPage+str(self.pageNum)
            try:
                data = urllib.request.urlopen(thisurl).read().decode('utf-8','ignore')
                self.nameData = re.compile(self.patName,re.S).findall(data)
                self.priceData = re.compile(self.patPrice,re.S).findall(data)
                self.commentData = re.compile(self.patComment, re.S).findall(data)
                self.storeData = re.compile(self.patStore, re.S).findall(data)
                self.IDData = re.compile(self.patProdID, re.S).findall(data)
                self.pageNum += 2
                #得到基础数据，并翻页
                self.nameData = self.processData(self.nameData)
                self.commentData = self.processData(self.commentData)
                self.storeData = self.processData(self.storeData)
                #处理基本数据（价格与ID不用处理）

                for j in range(0,len(self.nameData)):
                    self.storeKey["商品名称"] = self.nameData[j]
                    self.storeKey["商品价格"] = self.priceData[j]
                    self.storeKey["商品评论数"] = self.commentData[j]
                    self.storeKey["商品出售方"] = self.storeData[j]

                    self.insertData(self.fileName, self.storeKey)
                    self.commDetail(self.IDData[j])
                #将所有的信息放入字典中，并把字典传给另外方法，把它写入文件。把抓出来的产品ID传给另外方法单独处理

            except Exception as err:
                print(err)




    def processData(self,prodList):
    # 处理商品所有信息的基本数据
        nameList = self.nameData
        htmlTag = re.compile('<[^>]+>')
        # 去除html标签的正则
        enterTag = re.compile('\\n')
        # 去除换行的正则
        table = re.compile('\\t\\t')
        # 去除制表符的正则
        for x in range(0, len(prodList)):

            if(prodList[x]!='\n\t\t'):
                prodList[x]=htmlTag.sub("",prodList[x])
                prodList[x]=enterTag.sub("",prodList[x])
                prodList[x]=table.sub("",prodList[x])
            else:
                prodList[x] = '京东自营'

        return prodList

    def insertData(self,fileName,infoDict):
    #将数据用字典形式写入文件
        file=open(self.folder+str(fileName)+".txt", "a+")
        file.write(str(infoDict)+"\n")
        file.close()


    def commDetail(self,prodID):
    #单独处理详细评论

        htmlTag = re.compile('<[^>]+>')
        #去除html标签正则

        for i in range(0, self.commTimes):
            commURL = self.urlComment + str(prodID) + "&page=" + str(self.commNum)

            try:
                comData = urllib.request.urlopen(commURL).read().decode('GBK')
                self.comDetaData = re.compile(self.patDetail, re.S).findall(comData)
                self.commNum += 1
                # 得到数据，并翻页


                commentData=[]
                #临时列表储存评论数据

                for k in self.comDetaData:
                    if k not in commentData:
                        commentData.append(k)
                #把评论数据中的重复数据去除

                for n in range(0, len(commentData)):
                    if (os.path.exists(self.folder + "comment")):
                        comFile = open(self.folder + "comment\\" + "ID" + str(prodID) + ".txt", "a+")
                        comFile.write(htmlTag.sub("", commentData[n]) + "\n")
                    else:
                        os.mkdir(self.folder + "comment")
                        comFile = open(self.folder + "comment\\" + "ID" + str(prodID) + ".txt", "a+")
                        comFile.write(htmlTag.sub("", commentData[n]) + "\n")

                comFile.close()

            except Exception as err:
                print (err)

        self.commNum = 1
        #评论页码归回第一页



if __name__ == "__main__":
    JDPachong()