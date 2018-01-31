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
        self.randData()
        self.showBoard()
        print(self.deterGame())

    def showBoard(self):
    #打印棋盘
        print("---------------")
        for i in range(0,colNum):
            print(str(self.gameBoard[i][0])+"   "+str(self.gameBoard[i][1])+"   "+str(self.gameBoard[i][2])+"   "+
              str(self.gameBoard[i][3]))
        print("---------------")
           # print(i)

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
        for i in range(0,rowNum):
            for j in range(1,colNum):
                if(self.gameBoard[i][j-1]==self.gameBoard[i][j]):
                    self.gameBoard[i][j-1]=self.gameBoard[i][j]*2
                    self.gameBoard[i][j]=0


    def moveRight(self):
        for i in range(0,rowNum):
            for j in(1,colNum):
                if(self.gameBoard[i][j]==self.gameBoard[i][j-1]):
                    self.gameBoard[i][j] = self.gameBoard[i][j - 1] * 2
                    self.gameBoard[i][j-1]=0


    def moveUp(self):
        pass

    def moveDown(self):
        pass

    def mainMethod(self):
        pass

    def deterGame(self):
    #判断游戏是否结束或胜利
        for i in range(0,rowNum):
            for j in range(0,colNum):
                if(self.gameBoard[i][j]==2048):
                    return 1
                elif(self.gameBoard[i][j]!=2048&self.gameBoard.count(0)==0):
                    return 0
                else:
                    return 2

    def returnBoard(self):
        return self.gameBoard



if __name__ == "__main__":
    GameProMain()
   # print(GameProMain().returnBoard())

