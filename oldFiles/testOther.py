import random
class okok:
    gameMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    print(gameMatrix[1][1])
    print('{0:4} {1:4} {2:4} {3:4}'.format(gameMatrix[0][0], gameMatrix[0][1], gameMatrix[0][2], gameMatrix[0][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(gameMatrix[1][0], gameMatrix[1][1], gameMatrix[1][2], gameMatrix[1][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(gameMatrix[2][0], gameMatrix[2][1], gameMatrix[2][2], gameMatrix[2][3]))
    print('{0:4} {1:4} {2:4} {3:4}'.format(gameMatrix[3][0], gameMatrix[3][1], gameMatrix[3][2], gameMatrix[3][3]))


    def stDemo(self, gMatrix):
        self.matrix = gMatrix
        print(self.matrix[2][2])

    stDemo(gameMatrix)