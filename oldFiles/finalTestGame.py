import random

rowNum=4
colNum=4
randNum=[2,4]
randList=[]

class GameProMain:

    def __init__(self,rowNum=rowNum,colNum=colNum):
    #建立一个刚开始游戏的棋盘
        self.rowNum=rowNum
        self.colNum=colNum
        #self.randdata[2,4]
        self.gameBoard = [[0 for i in range(0, rowNum)] for i in range(0, colNum)]
        #self.gameBoard=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]



    def showBoard(self):
    #打印棋盘
        print("---------------")
        for i in range(0,colNum):
            print(str(self.gameBoard[i][0])+"   "+str(self.gameBoard[i][1])+"   "+str(self.gameBoard[i][2])+"   "+
              str(self.gameBoard[i][3]))
        print("---------------")
           # print(i)

    def proData(self,qipan):
    #处理棋盘一行数据
        temp=[0,0,0,0]
        pos=0
        for i in range(0,rowNum):
        #左移不为0的数据
            if(qipan[i]!=0):
                temp[pos]=qipan[i]
                pos+=1
        qipan=temp

        for j in range(0,rowNum-1):
        #合并相同的数字
                if(qipan[j]==qipan[j+1]):
                    qipan[j]=qipan[j+1]*2
                    qipan[j+1]=0

        return qipan



    def checkSame(self,row):
    #检查相邻是否为相等并且不为0
        same=False
        for i in range(1,len(row)-1):
            if(row[i]!=0&row[i-1]==row[i]):
                same=True
        return same

    def randData(self,randNum=randNum,):
    #把随机生成的2或4放在随机的0位置
        self.genData=random.choice(randNum)
        #self.randList
        for i in range(0,rowNum):
            for j in range(0,colNum):
                if(self.gameBoard[i][j]==0):
                    randList.append([i,j])

        #print(randList)
        a=random.choice(randList)
        self.gameBoard[a[0]][a[1]]=self.genData
        #for i in self.gameBoard

    def moveLeft(self):
    #往左移动
        n=0
        for i in self.gameBoard:
           self.gameBoard[n]=self.proData(i)
           n+=1


    def moveRight(self):
    #往右移动
        a = [0, 0, 0, 0]
        for i in range(0, rowNum):
            k = 0
            for j in range(rowNum-1, -1, -1):
                a[k] = self.gameBoard[i][j]
                k += 1
            a = self.proData(a)
            k = 0
            for j in range(rowNum-1, -1, -1):
                self.gameBoard[i][j] = a[k]
                k += 1


    def moveUp(self):
    #往上移动
        a = [0, 0, 0, 0]
        for i in range(0, 4):

            for j in range(0, 4):
                a[j] = self.gameBoard[j][i]

            a = self.proData(a)

            for k in range(0, 4):
                self.gameBoard[k][i] = a[k]

    def moveDown(self):
    #往下移动
        a = [0, 0, 0, 0]
        for i in range(0, 4):
            k = 0
            for j in range(3, -1, -1):
                a[k] = self.gameBoard[j][i]
                k += 1
            a = self.proData(a)
            k = 0
            for j in range(3, -1, -1):
                self.gameBoard[j][i] = a[k]
                k += 1

    def mainMethod(self):
        a=GameProMain()
        a.randData()
        a.showBoard()
        while(a.deterGame()>0):
            key=input()
            if(key=="w"):
                a.moveUp()
                a.randData()
                a.showBoard()
            elif(key=="s"):
                a.moveDown()
                a.randData()
                a.showBoard()
            elif(key == "a"):
                a.moveLeft()
                a.randData()
                a.showBoard()
            elif(key == "d"):
                a.moveRight()
                a.randData()
                a.showBoard()
            else:
                continue

    def countZero(self):
        a=0
        for i in range(0,4):
            for j in range (0,4):
                if(self.gameBoard[i][j]==0):
                        a+=1

        return a

    def deterGame(self):
    #判断游戏是否结束或胜利
        for i in range(0,rowNum):
            for j in range(0,colNum):
                if(self.gameBoard[i][j]==2048):
                    print("恭喜，游戏胜利")
                    return 1
                elif(self.countZero()==0):

                    print("游戏结束")
                    return 0
                else:
                    return 2

    def returnBoard(self):
        return self.gameBoard



if __name__ == "__main__":
    GameProMain().mainMethod()
   # print(GameProMain().returnBoard())

