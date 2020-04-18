import random
# import unittest, nose, nose2, pytest

def computerGuess():
    return random.randint(1, 100)
    # return 0

def userGuess():
    user = 0
    while user < 1 or user > 100:
        user = int(input("Pick a number between 1-100: "))
    return user

def provideFeedback(computerGuess, userGuess):
    if userGuess < computerGuess:
        return "too low"
    elif computerGuess < userGuess:
        return "too high"
    else:
        return "correct"

def main():
    # testComputerNumberGreaterThan0()
    # testComputerNumberLessThan101()
    # testUserNumberGreaterThan0()
    # testUserNumberLessThan101()
    # testGuessTooLow()
    # testGuessTooHigh()
    # testGuessCorrectly()
    print("All tests passed!")

########################################################################################################################

# def testComputerNumberGreaterThan0():
#     assert computerGuess() > 0, "Computer Number was NOT greater than 0"
#
# def testComputerNumberLessThan101():
#     assert computerGuess() < 101, "Computer Number is too large!"
#
# def testUserNumberGreaterThan0():
#     assert userGuess() > 0, "user number was too small"
#
# def testUserNumberLessThan101():
#     assert userGuess() < 101, "user number was too large"
#
# def testGuessTooLow():
#     assert provideFeedback(50, 49) == "too low", "number is too high"
#
# def testGuessTooHigh():
#     assert provideFeedback(49, 50) == "too high", "number is too low"
#
# def testGuessCorrectly():
#     assert provideFeedback(50, 50) == "user's guess was correct", "user's guess was incorrect"
#
# main()