import math
import random

class BoardObject:
    def __init__(self, ix, iy):
        self.__x = ix
        self.__y = iy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY

class Player(BoardObject):
    def __init__(self, ix, iy, ipn):
        super().__init__(ix, iy)
        # self.__x = ix
        # self.__y = iy
        self.__playerNum = ipn

    # def getX(self):
    #     return self.__x
    #
    # def getY(self):
    #     return self.__y

    def getPlayerNum(self):
        return self.__playerNum

    # def setX(self, newX):
    #     self.__x = newX
    #
    # def setY(self, newY):
    #     self.__y = newY

    def setPlayerNum(self, newNum):
        self.__playerNum = newNum

    def move(self, direction, distance):
        if direction == 'up':
            self.setY(self.getY() + distance)
        elif direction == 'down':
            self.setY(self.getY() - distance)
        elif direction == 'left':
            self.setY(self.getX() - distance)
        elif direction == 'right':
            self.setY(self.getX() + distance)
        else:
            print('Incorrect Direction!!!')

    def getInput(self):
        direction = input("Input a direction: ")
        distance = input("Input a distance: ")
        return (direction, int(distance))


class Treasure(BoardObject):
    def __init__(self, ix, iy, iValue):
        super().__init__(ix, iy)
        # self.__x = ix
        # self.__y = iy
        self.__value = iValue

    # def getX(self):
    #     return self.__x
    #
    # def getY(self):
    #     return self.__y

    def getValue(self):
        return self.__value

    # def setX(self, newX):
    #     self.__x = newX
    #
    # def setY(self, newY):
    #     self.__y = newY

    def setValue(self, newValue):
        self.__value = newValue


class Board:
    def __init__(self):
        self.__player1 = Player(self.randomValue(), self.randomValue(), 1)
        self.__player2 = Player(self.randomValue(), self.randomValue(), 2)
        self.__treasure = Treasure(self.randomValue(), self.randomValue(), 500)

    def randomValue(self):
        return random.randint(-10, 10)

    def playRound(self):
        print("\nPlayer 1's Turn")
        self.printBoard(1)
        (direction, distance) = self.__player1.getInput()
        self.__player1.move(direction, distance)

        p1_dist = self.computeDistance(1)
        if p1_dist == 0:
            return

        print("\nPlayer 2's Turn")
        self.printBoard(2)
        (direction, distance) = self.__player2.getInput()
        self.__player2.move(direction, distance)

    def printBoard(self, turn):
        print('')
        if turn == 1:
            x = self.__player1.getX()
            y = self.__player1.getY()
        elif turn == 2:
            x = self.__player2.getX()
            y = self.__player2.getY()
        print("Current Position: (" + str(x) + ", " + str(y) + ")")
        print("Distance to Treasure:", str(self.computeDistance(turn)))

    def computeDistance(self, turn):
        # dist = sqrt((x2-x1)^2 + (y2-y1)^2)
        if turn == 1:
            x_diff = self.__player1.getX() - self.__treasure.getX()
            y_diff = self.__player1.getY() - self.__treasure.getY()
        elif turn == 2:
            x_diff = self.__player1.getX() - self.__treasure.getX()
            y_diff = self.__player1.getY() - self.__treasure.getY()
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def didPlayerWin(self):
        p1_distance = self.computeDistance(1)
        p2_distance = self.computeDistance(2)
        return p1_distance == 0 or p2_distance == 0


game = Board()
while ~game.didPlayerWin():
    game.playRound()
print('\nGame Won Successfully!!!')
if game.computeDistance(1) == 0:
    print("Player 1 was Victorious")
else:
    print("Player 2 was Victorious")
