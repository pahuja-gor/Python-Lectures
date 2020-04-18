import random

class Location:
    def __init__(self, input_X, input_Y):
        self.__x = input_X
        self.__y = input_Y

    def move_up(self):
        self.__y += 1
        if self.__y > 5:
            self.__y = 5

    def move_down(self):
        self.__y -= 1
        if self.__y < -5:
            self.__y = -5

    def move_left(self):
        self.__x -= 1
        if self.__x < -5:
            self.__x = -5

    def move_right(self):
        self.__x += 1
        if self.__x > 5:
            self.__x = 5

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def print_location(self, name):
        print("(", self.__x, ",", self.__y, ")")

    def isColliding(self, player2):
        return (self.__x == player2.get_x() and self.__y == player2.get_y())

def main():
    human_player = Location(0, 0)
    computer_player = Location(random.randint(-5, 5), random.randint(-5, 5))
    moves = 0

    while (True):
        direction = input("Pick a direction to go in: ").lower()
        if direction == 'left':
            human_player.move_left()
        elif direction == 'right':
            human_player.move_right()
        elif direction == 'up':
            human_player.move_up()
        elif direction == 'down':
            human_player.move_down()
        else:
            print("INVALID COMMAND!")

        human_player.print_location("Human")

        if human_player.isColliding(computer_player):
            break

        comp_random = random.randint(1, 4)
        if comp_random == 1:
            computer_player.move_left()
        elif comp_random == 2:
            computer_player.move_right()
        elif comp_random == 3:
            computer_player.move_up()
        elif comp_random == 4:
            computer_player.move_down()

        computer_player.print_location("Computer")

        if computer_player.isColliding(human_player):
            break

        moves += 1

    print("You won using", moves, "moves!")



main()