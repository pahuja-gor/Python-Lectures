import math
import random


def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)


def drawCircle(myTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(myTurtle, sideLength, 360)


def archimedes(numSides):
    innerAngleB = 360 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = 2 * oneHalfSideS
    polygonCircumference = numSides * sideS
    return polygonCircumference / 2


def monteCarlo(numDarts):
    inCircle = 0
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance <= 1:
            inCircle += 1
    pi = inCircle / numDarts * 4
    return pi


def leibniz(terms):
    sum = 0
    denominator = 1
    for i in range(terms):
        sum += 4 / denominator * (-1) ** i
        denominator += 2
    return sum


def main():
    # turtle.setup(500, 500, None, None)
    # turtle.reset()

    # drawPolygon(turtle, 5, 360)
    # drawCircle(turtle, 150)

    # turtle.done()

    for i in range(3, 10000):
        pi = archimedes(i)
        print("A: For " + str(i) + " sides, pi = " + str(pi))
        pi = leibniz(i)
        print("L: For " + str(i) + " sides, pi = " + str(pi))
        pi = monteCarlo(i)
        print("M: For " + str(i) + " sides, pi = " + str(pi))
        print('\n')


main()
